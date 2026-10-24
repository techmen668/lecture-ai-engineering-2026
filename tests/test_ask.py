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

    assert ask.ask("質問") == "回答"
    assert call["model"] == ask.MODEL
    assert call["contents"] == "質問"
    assert call["config"].temperature == ask.TEMPERATURE == 0.2
    assert capsys.readouterr().out == "[tokens] input=12 output=7\n"