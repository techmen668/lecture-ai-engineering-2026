"""第1回: 素のLLMに質問するスクリプト。

使い方:
    uv run python -m app.ask "LoRAとは何ですか？"
    uv run python -m app.ask            # 質問を省略すると、講座に固有の質問をする
                                        # 回答後、空欄を入力するまで会話を続ける

ツールを使わない「素の」呼び出し。
講座に固有のことを聞くと、「分からない」と答えるか、一般論でもっともらしく答える
（講座の実際とは違う）ことを確かめよう。
（第3回で、用語集を検索できるエージェントにして改善する）
"""

import argparse
import time

from google import genai
from google.genai import errors
from google.genai import types

from app.config import MODEL, api_error_message, get_api_key

# 講座に固有の質問。正しい答えは data/glossary.json の homework-levels にある
DEFAULT_QUESTION = "AIE2026の講座の宿題にある「3レベル」とは何ですか？"
TEMPERATURE = 0.7


def ask(question: str) -> str:
    client = genai.Client(api_key=get_api_key())
    # 発展課題: モデルやtemperatureごとの比較用に、API応答時間を計測する。
    started_at = time.perf_counter()
    response = client.models.generate_content(
        model=MODEL,
        contents=question,
        config=types.GenerateContentConfig(temperature=TEMPERATURE),
    )
    print(f"[response_time] {time.perf_counter() - started_at:.2f} sec")

    # 演習6: 応答の usage_metadata から入力・出力トークン数を表示
    usage = response.usage_metadata
    if usage is not None:
        print(f"[tokens] input={usage.prompt_token_count} output={usage.candidates_token_count}")

    return response.text


def run_chat(initial_question: str) -> None:
    client = genai.Client(api_key=get_api_key())
    chat = client.chats.create(
        model=MODEL,
        config=types.GenerateContentConfig(temperature=TEMPERATURE),
    )

    question = initial_question
    while question:
        # 発展課題: モデルやtemperatureごとの比較用に、API応答時間を計測する。
        started_at = time.perf_counter()
        response = chat.send_message(question)
        print(f"[response_time] {time.perf_counter() - started_at:.2f} sec")
        print(response.text)

        usage = response.usage_metadata
        if usage is not None:
            print(f"[tokens] input={usage.prompt_token_count} output={usage.candidates_token_count}")

        try:
            question = input("\n続けて質問してください（空欄で終了）: ").strip()
        except EOFError:
            print()
            break


def main() -> None:
    parser = argparse.ArgumentParser(description="素のLLMに質問する")
    parser.add_argument("question", nargs="?", default=DEFAULT_QUESTION)
    args = parser.parse_args()

    print(f"[model] {MODEL}")
    print(f"[temperature] {TEMPERATURE}")
    print(f"[質問] {args.question}\n")
    try:
        run_chat(args.question)
    except errors.APIError as e:
        print(api_error_message(e.code, e.message))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
