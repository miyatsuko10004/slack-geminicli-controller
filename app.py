import os
import subprocess
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv

load_dotenv()

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

def run_command(cmd_str):
    try:
        # NOTE: In production, consider security implications. Use shlex/safe command parsing if accepting user input.
        result = subprocess.run(cmd_str, shell=True, capture_output=True, text=True, timeout=30)
        output = result.stdout if result.stdout else result.stderr
        return output if output else "✅ 実行完了（出力なし）"
    except Exception as e:
        return f"❌ エラーが発生しました: {str(e)}"

@app.event("app_mention")
def handle_app_mentions(event, say):
    text = event.get("text", "")
    
    if "antigravity" in text:
        say("🚀 antigravityを実行します...")
        out = run_command("python3 -c 'import antigravity'")
        say(f"結果:\\n```\\n{out}\\n```")
    
    elif "gemini" in text:
        # Example: @bot gemini summarize this
        # Extracts everything after 'gemini '
        prompt = text.split("gemini", 1)[-1].strip()
        if not prompt:
            say("geminiコマンドの後にプロンプトを入力してください。")
            return
            
        say(f"🤖 Gemini CLIに問い合わせ中...\\nプロンプト: `{prompt}`")
        # Run gemini cli with the prompt. Make sure gemini cli is installed and in PATH.
        out = run_command(f'gemini "{prompt}"')
        say(f"結果:\\n```\\n{out}\\n```")
        
    else:
        say("利用可能なコマンド: `antigravity`, `gemini <prompt>`")

if __name__ == "__main__":
    app_token = os.environ.get("SLACK_APP_TOKEN")
    if not app_token:
        print("エラー: SLACK_APP_TOKEN が設定されていません。")
        exit(1)
        
    print("⚡️ Slack Mac Controller 起動中...")
    handler = SocketModeHandler(app, app_token)
    handler.start()
