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

- 取り組んだレベル：基礎 


- やったこと

        Search_glossaryのdocstringを書き換えた。
        tools.py 36行目にて「調べたい用語を1つだけ入れる」を「関連する用語をまとめて入れる」と書き換えた。


- 結果

書き換え前「調べたい用語を1つだけ入れる」

        @techmen668 ➜ /workspaces/lecture-ai-engineering-2026 (lec03) $  source /workspaces/lecture-ai-engineering-2026/.venv/bin/activate
        (aie2026-exercises) @techmen668 ➜ /workspaces/lecture-ai-engineering-2026 (lec03) $ uv run python -m app.agent --trace "LoRAとQLoRAの違いは？"

        LoRAとQLoRAの違いは以下のとおりです。

        * **LoRA**: 事前学習済みの重みは固定したまま、重みの更新分を小さな低ランク行列（2つの小さな行列の積）で表し、その部分だけを学習するPEFT（Parameter-Efficient Fine-Tuning）手法です。これにより、学習するパラメータ数を大幅に削減できます。
        * **QLoRA**: LoRAの考え方をベースに、さらにベースモデルの重みを4ビットなどに**量子化**（Quantization）してメモリを極限まで節約した手法です。これにより、より大きなモデルをより小さなGPUメモリで効率よく学習できるようになります。

        （関連する回：第2回）

        --- trace ---
        [tool call]   search_glossary({'query': 'LoRA'})
        [tool call]   search_glossary({'query': 'QLoRA'})
        [tool return] search_glossary -> [{"term": "LoRA", "lecture": 2, "definition": "事前学習済みの重みは固定したまま、重みの更新分を2つの小さな行列の積（低ランク行列）で表し、その小さな行列だけを学習するPEFT手法。学習するパラ…
        [tool return] search_glossary -> [{"term": "QLoRA", "lecture": 2, "definition": "ベースモデルの重みを4ビットなどに量子化してメモリを節約したうえで、LoRAで学習する手法。より大きなモデルを小さなGPUで扱える。本講座の第2…
        [usage] RunUsage(cost=Decimal('0.0008704'), details={'text_prompt_tokens': 1318}, input_text_tokens=1318, input_tokens=1318, output_tokens=190, requests=2, tool_calls=2)


書き換え後「関連する用語をまとめて入れる」

        (aie2026-exercises) @techmen668 ➜ /workspaces/lecture-ai-engineering-2026 (lec03) $ uv run python -m app.agent --trace "LoRAとQLoRAの違いは？"

        LoRAとQLoRAの違いは、ベースモデルの重みをそのまま使うか、量子化してメモリを節約するかにあります。

        * **LoRA（Low-Rank Adaptation）**
        事前学習済みの重みはそのまま（16ビットなど）固定し、追加の小さな低ランク行列（アダプタ）だけを学習することで、効率的に微調整を行うPEFT手法です。学習パラメータや保存ファイルを大幅に削減できます。
        * **QLoRA（Quantized LoRA）**
        ベースモデルの重みを4ビットなどの低ビットに量子化して読み込み、メモリ消費量を劇的に抑えた状態でLoRAの学習を行う手法です。これにより、さらに大きなモデルを限られたGPU環境でも動かせるようになります。

        （関連する回：第2回）

        --- trace ---
        [tool call]   search_glossary({'query': 'LoRA QLoRA'})
        [tool return] search_glossary -> [{"term": "LoRA", "lecture": 2, "definition": "事前学習済みの重みは固定したまま、重みの更新分を2つの小さな行列の積（低ランク行列）で表し、その小さな行列だけを学習するPEFT手法。学習するパラ…
        [usage] RunUsage(cost=Decimal('0.0007821'), details={'text_prompt_tokens': 1007}, input_text_tokens=1007, input_tokens=1007, output_tokens=192, requests=2, tool_calls=1)


書き換え前と書き換え後の相違点

--- trace ---の欄をそれぞれ確認すると

        検索回数と検索語　[tool call]の行
        ・変更前：search_glossary({'query': 'LoRA'})とsearch_glossary({'query': 'QLoRA'})の2行
        ・変更後：search_glossary({'query': 'LoRA QLoRA'})の1行

        ツール呼び出し数：最後の[usage]のtool_calls
        ・変更前：tool_calls=2
        ・変更後：tool_calls=1

        LLM呼び出し数：[usage]のrequests
        変更前・変更後ともにrequests=2

        回答内容：
        「調べたい用語を1つだけ入れる」を「関連する用語をまとめて入れる」いずれの回答も大きな変更点はないが、「関連する用語をまとめて入れる」と記述した際には回答の冒頭に「ベースモデルの重みをそのまま使うか、量子化してメモリを節約するかにあります。」という形で一言で要約した説明が入っている点が特徴的。

- 気づき・疑問

        今回の実施結果を見ると、「用語を1つだけ入れる」「関連する用語をまとめて入れる」というdocstringの中の文言を変えて用語集からの調べ方と使い方を変化させはしたものの、出てくる回答内容自体にさほど大きな本質的な違いは見られなかった。ただし、---trace---のパラメータをよく見てみると、検索の仕方が2回別々にしていたものを1度でまとめて実施するようになるなど内部での呼び出し処理の構造には変化があった。どんな改変を加えれば、構造の変化が回答の仕方に対しても影響を及ぼす程度までになるのか？というのは文言を変える、コード処理自体を変える、といった形で検証の余地があるように感じた。

        ツールの呼び出し数tool_callsはdocstring変更前が2、変更後は1なのに、LLM呼び出し数は変更前・変更後ともにrequests=2はモデルとLLMの関連にどんな関係性があるのか疑問に思った。変更後のrequestsが2であれば、変更前のtool_callsが2である以上、requestsは4になりそうだと素朴に思った。





- 取り組んだレベル：実装 


- やったこと：
　
1.app/tools.pyの更新
 
 save_learning_log(content)を追加、learning_log/ に日時付きの Markdown ファイルを保存。内容が空なら ValueError を出し、同名ファイルがある場合は上書きしないようにした。

2.app/agent.pyの更新

DeferredToolRequests を出力型に追加し、save_learning_log を requires_approval=True で登録した。
保存依頼時はCLIで保存内容を表示して利用者に確認し、承認・拒否の結果と会話履歴をエージェントに返して処理を再開するようにした。

3.tests/test_agent.pyの更新

承認した場合に学習ログが保存され、拒否した場合は保存されないことを確認するテストを追加した。



- 結果：

`save_learning_log` をエージェントに登録し、保存を依頼すると内容が表示されて承認を求めるようにした。`y` または `yes` で承認した場合だけ `learning_log/` に保存され、それ以外の入力では保存されない。

`tests/test_agent.py` に承認・拒否の動作を確認するテストを追加した。一時ディレクトリを使い、承認時にログが作られること、拒否時には作られないことを確認した。`uv run pytest -q` の結果は **13 passed**。

- 気づき・疑問：

保存処理のように取り消しにくい操作は、ツールを登録するだけでなく、実行前に利用者が内容を確認して承認できる流れが必要だと分かった。今回のテストでは実際の API は呼び出していないため、実モデルがどのようなログ内容を作り、承認を求めるかは未確認。
