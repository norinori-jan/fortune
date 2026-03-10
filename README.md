# 易占い（周易）アプリ

八卦・六十四卦・変爻を使ったデジタル易占いアプリです。

## 機能

- **八卦（はっけ）生成**: 1〜8の乱数を2回生成し、下卦（内卦）と上卦（外卦）を決定
- **六十四卦（ろくじゅうしけ）**: 8×8=64通りの本卦（ほんけ）を導出
- **変爻（へんこう）**: 1〜6のサイコロで変わる爻を決定し、之卦（しか）を算出
- **視覚的な卦表示**: 陽（━）・陰（- -）の爻を画面上に描画
- **卦辞（かじ）表示**: 各卦の意味と卦辞を日本語で表示

## アーキテクチャ

```
fortune/
├── backend/          # Python Flask API
│   ├── app.py        # APIサーバー（フロントエンドも配信）
│   ├── hexagrams.py  # 八卦・六十四卦データとロジック
│   ├── requirements.txt
│   └── tests/
│       └── test_app.py
└── frontend/         # React（Vite）フロントエンド
    ├── src/
    │   ├── App.jsx
    │   ├── App.css
    │   └── components/
    │       ├── Hexagram.jsx        # 卦象の描画
    │       └── DivinationResult.jsx # 占い結果の表示
    └── ...
```

## セットアップ

### バックエンド

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### フロントエンド（開発時）

```bash
cd frontend
npm install
npm run dev
```

### フロントエンド（本番ビルド）

```bash
cd frontend
npm run build
# ビルド後は backend/app.py が dist/ を自動配信
```

## 起動方法

```bash
# バックエンドを起動（フロントエンドも同時に配信）
cd backend
python app.py
# → http://localhost:5000 でアプリが起動
```

## テスト

```bash
cd backend
python -m pytest tests/ -v
```

## API

| メソッド | パス | 説明 |
|--------|------|------|
| POST | `/api/divine` | 占いを実行し、本卦・変爻・之卦を返す |
| GET | `/api/trigrams` | 八卦の一覧を返す |
| GET | `/api/health` | ヘルスチェック |
