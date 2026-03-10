"""
易（周易）占いアプリ — Flask バックエンド API
"""

import os
import random

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

from hexagrams import (
    get_hexagram,
    get_changing_hexagram,
    get_trigram,
    get_line_names,
    TRIGRAMS,
)

# フロントエンドのビルド済みファイルのパス
FRONTEND_DIST = os.path.join(
    os.path.dirname(__file__), '..', 'frontend', 'dist'
)

app = Flask(
    __name__,
    static_folder=FRONTEND_DIST,
    static_url_path='/',
)
CORS(app)


# ─── フロントエンド配信 ───────────────────────────────────────────

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_frontend(path):
    """ビルド済みの React アプリを配信する。"""
    target = os.path.join(FRONTEND_DIST, path)
    if path and os.path.exists(target):
        return send_from_directory(FRONTEND_DIST, path)
    return send_from_directory(FRONTEND_DIST, 'index.html')


# ─── API エンドポイント ───────────────────────────────────────────

@app.route("/api/divine", methods=["POST"])
def divine():
    """占いを実行し、本卦・変爻・之卦を返す。

    Returns:
        JSON:
            - lower_number: 下卦番号 (1-8)
            - upper_number: 上卦番号 (1-8)
            - changing_line: 変爻の位置 (1-6)
            - honke: 本卦データ
            - shike: 之卦データ
    """
    lower_number = random.randint(1, 8)
    upper_number = random.randint(1, 8)
    changing_line = random.randint(1, 6)

    honke = get_hexagram(lower_number, upper_number)
    shike = get_changing_hexagram(lower_number, upper_number, changing_line)
    line_names = get_line_names()

    return jsonify({
        "lower_number": lower_number,
        "upper_number": upper_number,
        "changing_line": changing_line,
        "changing_line_name": line_names[changing_line],
        "honke": honke,
        "shike": shike,
    })


@app.route("/api/trigrams", methods=["GET"])
def trigrams():
    """八卦の一覧を返す。"""
    return jsonify(TRIGRAMS)


@app.route("/api/health", methods=["GET"])
def health():
    """ヘルスチェック用エンドポイント。"""
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(debug=debug, port=5000)
