# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：
　　　
    第1回のエージェントの回答と比較すると、第3回の回答は断定口調となったのが最も印象的だと思った。第1回の実施時は「可能性が非常に高いです。」という答えや「以下のような分類で宿題が出されることがよくあります。」というように一般例から挙げているような答えだったのが、「どれか1つ**に取り組めばその回の宿題は完了となり、原則として採点は行われません」と今回のケースに特定してはっきりとした回答になっている。　　　　



今回（第3回）の実施結果：

        　(aie2026-exercises) @techmen668 ➜ /workspaces/lecture-ai-engineering-2026 (lec03) $ uv run python -m app.agent "AIE2026の講座の宿題にある「3レベル」とは何ですか？"
        [model] gemini-3.5-flash-lite
                        pydantic-ai v2.57.0 • Python 3.14.2
            / \
            /   \       agent: target • model: google:gemini-3.5-flash-lite • tools: 2 • capabilities: 0
        /___.___\
        /    |    \    observability: off — see every model and tool call live, with cost
        /      |      \    set it up free with Logfire and a GitHub login: https://pydantic.dev/ai-setup.md
        `---.._|_..---'    or use any OpenTelemetry backend: https://pydantic.dev/docs/ai/logfire/#otel

                        goes away once observability is on — or PYDANTIC_AI_NO_BANNER=1
        AIE2026の講座における「3レベル」とは、宿題の構成を段階的に分けた以下の3つのレベルのことを指します。

        1. **基礎**：講義内容の確認を行うレベル
        2. **実装**：自分で実際にコードを書くレベル
        3. **発展**：調査や新たな試行を行うレベル

        3つのうち**どれか1つ**に取り組めばその回の宿題は完了となり、原則として採点は行われません。ご自身の理解度や目的に合わせて選んで取り組んでみてくださいね。

第1回の回答：

        AIE2026の講座において「3レベル」という言葉が出てきた場合、それは学習する内容や宿題の難易度、あるいは課題のステップを**3つの段階（初級・中級・上級、または基礎・応用・実践など）**に分けて取り組む仕組みを指している可能性が非常に高いです。

        AIE（おそらくAI関連や英語・プログラミングなどの先端人材育成プログラム等）では、受講生のスキルや理解度に合わせて、以下のような分類で宿題が出されることがよくあります。

        1. レベル1（基礎・入門）：
        基本用語の理解や、授業の復習、簡単な穴埋めやコピペで動くコードの実行など、まずは基本を定着させるレベル。
        2.　レベル2（応用・発展）：
        少し自分で考えたり、条件を変えたりしてアレンジを加えるレベル。
        3. レベル3（実践・挑戦）：
        ゼロから自分で構築する、あるいは高度な課題に挑むレベル。


- `--trace` で見えたツール呼び出し（ツール名と引数）：

        --- trace ---
        [tool call]   search_glossary({'query': 'LoRA'})
        [tool call]   search_glossary({'query': 'QLoRA'})
        [tool return] search_glossary -> [{"term": "LoRA", "lecture": 2, "definition": "事前学習済みの重みは固定したまま、重みの更新分を2つの小さな行列の積（低ランク行列）で表し、その小さな行列だけを学習するPEFT手法。学習するパラ…
        [tool return] search_glossary -> [{"term": "QLoRA", "lecture": 2, "definition": "ベースモデルの重みを4ビットなどに量子化してメモリを節約したうえで、LoRAで学習する手法。より大きなモデルを小さなGPUで扱える。本講座の第2…
        [usage] RunUsage(cost=Decimal('0.0008088'), details={'text_prompt_tokens': 1196}, input_text_tokens=1196, input_tokens=1196, output_tokens=180, requests=2, tool_calls=2)

- 1つの質問での LLM 呼び出し回数（`requests`）：requests=2


- 追加したツールと、docstring に書いた説明：

    - `make_quiz(lecture: int)`
    - 「指定した回の確認問題を出すときに使う。その回の用語を1つ選び、問題と答えを返す。」

## 宿題

- 取り組んだレベル：基礎 / 実装 / 発展
- やったこと：
- 結果：
- 気づき・疑問：
