"""
================================================
  朝の自動サイト起動スクリプト
  対応ブラウザ: Chrome / Edge（Windows）
  使い方: python morning_launcher.py
================================================
"""

import time
import sys
import subprocess

# ============================================================
#  ★ ここを編集してください ★
# ============================================================

# 開きたいURLをリストに入れてください（順番に同一ウィンドウのタブで開きます）
URLS = [
    "https://www.google.com",
    "https://www.yahoo.co.jp",
    "https://github.com",
    # "https://example.com",  # 追加したい場合はここに書く
]

# 使用するブラウザを選んでください: "chrome" または "edge"
BROWSER = "chrome"

# 各タブを開く間隔（秒）— 0 でも動きますが 0.5〜1 推奨
INTERVAL = 0.5

# ============================================================
#  ブラウザのパス設定（通常は変更不要）
# ============================================================

BROWSER_PATHS = {
    "chrome": [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ],
    "edge": [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    ],
}

# ============================================================
#  メイン処理
# ============================================================


def find_browser_path(browser: str) -> str:
    """インストールされているブラウザの実行ファイルパスを返す"""
    import os

    paths = BROWSER_PATHS.get(browser.lower(), [])
    for path in paths:
        if os.path.exists(path):
            return path
    return None


def open_tabs(urls: list, browser: str, interval: float):
    browser = browser.lower()
    exe = find_browser_path(browser)

    if exe is None:
        print(f"[エラー] {browser} が見つかりませんでした。")
        print("  BROWSER_PATHS のパスを確認してください。")
        sys.exit(1)

    if not urls:
        print("[エラー] URLS リストが空です。URLを追加してください。")
        sys.exit(1)

    print(f"ブラウザ : {browser.upper()}")
    print(f"タブ数   : {len(urls)} 個")
    print("-" * 40)

    # 1つ目のURLで新しいウィンドウを開く
    first_url = urls[0]
    print(f"[1/{len(urls)}] 新規ウィンドウで開く: {first_url}")
    subprocess.Popen([exe, "--new-window", first_url])
    time.sleep(1.5)  # ウィンドウが立ち上がるのを少し待つ

    # 2つ目以降は同じウィンドウの新しいタブで開く
    for i, url in enumerate(urls[1:], start=2):
        print(f"[{i}/{len(urls)}] 新規タブで開く  : {url}")
        subprocess.Popen([exe, url])
        time.sleep(interval)

    print("-" * 40)
    print("完了！全タブを開きました。")


if __name__ == "__main__":
    # コマンドライン引数でブラウザを上書き可能
    # 例: python morning_launcher.py edge
    if len(sys.argv) >= 2:
        BROWSER = sys.argv[1]

    open_tabs(URLS, BROWSER, INTERVAL)
