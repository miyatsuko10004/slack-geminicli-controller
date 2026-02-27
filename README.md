# Slack GeminiCli Controller

スマホ（Slack）から自宅のMacに指示を送り、ローカルコマンド（`antigravity` や `gemini` CLIなど）を操作・実行するためのツールです。
SlackのSocket Modeを利用するため、Macのポート開放なしでセキュアに通信できます。

## 概要

Slack上でBot宛てにメンション付きでメッセージを送るか、特定のコマンドを送信すると、Mac上で対応する処理が実行され、結果がSlackに返ってきます。

## セットアップ

### 1. Slack Appの作成
1. [Slack API](https://api.slack.com/apps) にアクセスして「Create New App」を選択 (From scratch)
2. 「Socket Mode」を有効化し、App-Level Token (`xapp-...`) を発行
3. 「Event Subscriptions」で `app_mention` と `message.im` (必要に応じて) を追加
4. 「OAuth & Permissions」でBot Token (`xoxb-...`) を発行 (Scopes: `app_mentions:read`, `chat:write` など)

### 2. 環境変数の設定
`.env` ファイルを作成し、トークンを設定します。
```
SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_APP_TOKEN=xapp-your-app-token
```

### 3. 起動
```bash
pip install -r requirements.txt
python app.py
```
