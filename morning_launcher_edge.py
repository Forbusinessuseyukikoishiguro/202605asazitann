"""
================================================
  朝の自動サイト起動スクリプト（Edge固定版）
  使い方: python morning_launcher_edge.py
================================================
"""

import os
import time
import sys
import subprocess

# ============================================================
#  ★ ここを編集してください ★
# ============================================================

# 開きたいURLをリストに入れてください（上から順に同一ウィンドウのタブで開きます）
URLS = [
    "https://www.google.com",
    "https://www.yahoo.co.jp",
    "https://github.com",
    # "https://example.com",  # 追加したい場合はここに書く
]

# 各タブを開く間隔（秒）— 0.5〜1 推奨
INTERVAL = 0.5

# ============================================================
#  Edgeのパス（通常は変更不要）
# ============================================================

EDGE_PATHS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

# ============================================================
#  メイン処理
# ============================================================

def find_edge() -> str:
    for path in EDGE_PATHS:
        if os.path.exists(path):
            return path
    return None


def open_tabs():
    exe = find_edge()

    if exe is None:
        print("[エラー] Microsoft Edge が見つかりませんでした。")
        print("  EDGE_PATHS のパスを確認してください。")
        sys.exit(1)

    if not URLS:
        print("[エラー] URLS リストが空です。URLを追加してください。")
        sys.exit(1)

    print(f"ブラウザ : Microsoft Edge")
    print(f"タブ数   : {len(URLS)} 個")
    print("-" * 40)

    # 1つ目のURLで新しいウィンドウを開く
    print(f"[1/{len(URLS)}] 新規ウィンドウで開く: {URLS[0]}")
    subprocess.Popen([exe, "--new-window", URLS[0]])
    time.sleep(1.5)  # ウィンドウが立ち上がるのを待つ

    # 2つ目以降は同じウィンドウの新しいタブで開く
    for i, url in enumerate(URLS[1:], start=2):
        print(f"[{i}/{len(URLS)}] 新規タブで開く  : {url}")
        subprocess.Popen([exe, url])
        time.sleep(INTERVAL)

    print("-" * 40)
    print("完了！全タブを開きました。")


if __name__ == "__main__":
    open_tabs()
