from types import SimpleNamespace

from app import ask


def test_ask_prints_input_and_output_token_counts(monkeypatch, capsys):
    call = {}

    class FakeClient:
        class models:
            @staticmethod
            def generate_content(model, contents, config):
                call.update(model=model, contents=contents, config=config)
                return SimpleNamespace(
                    usage_metadata=SimpleNamespace(
                        prompt_token_count=12,
                        candidates_token_count=7,
                    ),
                    text="回答",
                )

    monkeypatch.setattr(ask.genai, "Client", lambda api_key: FakeClient())
    monkeypatch.setattr(ask, "get_api_key", lambda: "test-key")
    monkeypatch.setattr(ask.time, "perf_counter", iter([1.0, 2.25]).__next__)

    assert ask.ask("質問") == "回答"
    assert call["model"] == ask.MODEL
    assert call["contents"] == "質問"
    assert call["config"].temperature == ask.TEMPERATURE == 0.2
    assert capsys.readouterr().out == (
        "[response_time] 1.25 sec\n"
        "[tokens] input=12 output=7\n"
    )


def test_run_chat_reuses_chat_for_follow_up_questions(monkeypatch, capsys):
    sent_messages = []
    create_call = {}

    class FakeChat:
        def send_message(self, message):
            sent_messages.append(message)
            return SimpleNamespace(
                usage_metadata=SimpleNamespace(
                    prompt_token_count=12,
                    candidates_token_count=7,
                ),
                text=f"回答{len(sent_messages)}",
            )

    class FakeClient:
        class chats:
            @staticmethod
            def create(model, config):
                create_call.update(model=model, config=config)
                return FakeChat()

    questions = iter(["続きの質問", ""])
    monkeypatch.setattr(ask.genai, "Client", lambda api_key: FakeClient())
    monkeypatch.setattr(ask, "get_api_key", lambda: "test-key")
    monkeypatch.setattr("builtins.input", lambda prompt: next(questions))
    monkeypatch.setattr(
        ask.time,
        "perf_counter",
        iter([1.0, 1.5, 2.0, 3.25]).__next__,
    )

    ask.run_chat("最初の質問")

    assert create_call["model"] == ask.MODEL
    assert create_call["config"].temperature == ask.TEMPERATURE
    assert sent_messages == ["最初の質問", "続きの質問"]
    assert capsys.readouterr().out == (
        "[response_time] 0.50 sec\n"
        "回答1\n"
        "[tokens] input=12 output=7\n"
        "[response_time] 1.25 sec\n"
        "回答2\n"
        "[tokens] input=12 output=7\n"
    )