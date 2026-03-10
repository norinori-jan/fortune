"""
易アプリ バックエンドのユニットテスト
"""

import sys
import os
import pytest

# backend ディレクトリをパスに追加
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hexagrams import (
    TRIGRAMS,
    HEXAGRAMS,
    get_trigram,
    get_hexagram,
    get_changing_hexagram,
    _lines_to_trigram_number,
    get_line_names,
)
from app import app as flask_app


# ─────────────────── フィクスチャ ───────────────────

@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as c:
        yield c


# ─────────────────── 八卦データのテスト ───────────────────

class TestTrigrams:
    def test_eight_trigrams_exist(self):
        """八卦が8つすべて定義されていること"""
        assert len(TRIGRAMS) == 8

    def test_trigram_numbers_range(self):
        """八卦番号が1〜8であること"""
        assert set(TRIGRAMS.keys()) == {1, 2, 3, 4, 5, 6, 7, 8}

    def test_trigram_lines_length(self):
        """各八卦の爻が3本であること"""
        for num, trigram in TRIGRAMS.items():
            assert len(trigram["lines"]) == 3, f"八卦{num}の爻が3本でない"

    def test_trigram_lines_binary(self):
        """爻が0か1のみであること"""
        for num, trigram in TRIGRAMS.items():
            for line in trigram["lines"]:
                assert line in (0, 1), f"八卦{num}に不正な爻値: {line}"

    def test_qian_lines(self):
        """乾（1）は全て陽（1）であること"""
        assert TRIGRAMS[1]["lines"] == [1, 1, 1]

    def test_kun_lines(self):
        """坤（8）は全て陰（0）であること"""
        assert TRIGRAMS[8]["lines"] == [0, 0, 0]

    def test_get_trigram_valid(self):
        """有効な番号でget_trigramが正しく動作すること"""
        t = get_trigram(1)
        assert t["name"] == "乾"

    def test_get_trigram_invalid(self):
        """無効な番号でValueErrorが発生すること"""
        with pytest.raises(ValueError):
            get_trigram(0)
        with pytest.raises(ValueError):
            get_trigram(9)


# ─────────────────── 六十四卦データのテスト ───────────────────

class TestHexagrams:
    def test_sixty_four_hexagrams_exist(self):
        """六十四卦が64卦すべて定義されていること"""
        assert len(HEXAGRAMS) == 64

    def test_hexagram_numbers_unique(self):
        """卦番号（1〜64）が重複なく存在すること"""
        numbers = [h["number"] for h in HEXAGRAMS.values()]
        assert sorted(numbers) == list(range(1, 65))

    def test_hexagram_keys_range(self):
        """下卦・上卦のキーが1〜8の範囲内であること"""
        for lower, upper in HEXAGRAMS.keys():
            assert 1 <= lower <= 8
            assert 1 <= upper <= 8

    def test_get_hexagram_includes_lines(self):
        """get_hexagramが6本の爻を含むこと"""
        h = get_hexagram(1, 1)
        assert len(h["lines"]) == 6

    def test_get_hexagram_qian(self):
        """乾為天（1番）が正しく取得できること"""
        h = get_hexagram(1, 1)
        assert h["number"] == 1
        assert h["name"] == "乾為天"
        assert h["lines"] == [1, 1, 1, 1, 1, 1]

    def test_get_hexagram_kun(self):
        """坤為地（2番）が正しく取得できること"""
        h = get_hexagram(8, 8)
        assert h["number"] == 2
        assert h["name"] == "坤為地"
        assert h["lines"] == [0, 0, 0, 0, 0, 0]

    def test_get_hexagram_all_combinations(self):
        """8×8=64の全組み合わせでget_hexagramが成功すること"""
        for lower in range(1, 9):
            for upper in range(1, 9):
                h = get_hexagram(lower, upper)
                assert "number" in h
                assert "name" in h
                assert "lines" in h
                assert len(h["lines"]) == 6


# ─────────────────── 変爻・之卦のテスト ───────────────────

class TestChangingLines:
    def test_changing_line_flips_yang_to_yin(self):
        """変爻で陽が陰に変わること（乾為天の初爻変化）"""
        original = get_hexagram(1, 1)
        assert original["lines"][0] == 1  # 初爻は陽
        shike = get_changing_hexagram(1, 1, 1)
        assert shike["lines"][0] == 0  # 変爻後は陰

    def test_changing_line_flips_yin_to_yang(self):
        """変爻で陰が陽に変わること（坤為地の初爻変化）"""
        original = get_hexagram(8, 8)
        assert original["lines"][0] == 0  # 初爻は陰
        shike = get_changing_hexagram(8, 8, 1)
        assert shike["lines"][0] == 1  # 変爻後は陽

    def test_changing_upper_line(self):
        """上爻（6爻）が変わること"""
        original = get_hexagram(1, 1)
        assert original["lines"][5] == 1  # 上爻は陽
        shike = get_changing_hexagram(1, 1, 6)
        assert shike["lines"][5] == 0  # 変爻後は陰

    def test_all_lines_changeable(self):
        """全ての爻位置（1〜6）で変爻が可能であること"""
        for line in range(1, 7):
            shike = get_changing_hexagram(1, 1, line)
            assert "number" in shike
            assert len(shike["lines"]) == 6

    def test_qian_changes_all_lines_to_kun(self):
        """乾為天の全爻を変爻すると坤為地になること（各爻の順次変化は別卦）"""
        # 乾為天(1,1)の初爻変: 下卦が [0,1,1]=兌 になる
        shike = get_changing_hexagram(1, 1, 1)
        assert shike["lines"][0] == 0
        assert shike["lines"][1] == 1
        assert shike["lines"][2] == 1

    def test_lines_to_trigram_number(self):
        """爻配列から八卦番号が正しく引けること"""
        assert _lines_to_trigram_number([1, 1, 1]) == 1  # 乾
        assert _lines_to_trigram_number([0, 0, 0]) == 8  # 坤


# ─────────────────── API エンドポイントのテスト ───────────────────

class TestAPI:
    def test_health_check(self, client):
        """/api/health が 200 を返すこと"""
        resp = client.get("/api/health")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["status"] == "ok"

    def test_divine_returns_200(self, client):
        """/api/divine が 200 を返すこと"""
        resp = client.post("/api/divine")
        assert resp.status_code == 200

    def test_divine_response_structure(self, client):
        """/api/divine のレスポンスが必要なフィールドを持つこと"""
        resp = client.post("/api/divine")
        data = resp.get_json()
        assert "lower_number" in data
        assert "upper_number" in data
        assert "changing_line" in data
        assert "changing_line_name" in data
        assert "honke" in data
        assert "shike" in data

    def test_divine_lower_upper_range(self, client):
        """/api/divine の下卦・上卦番号が1〜8の範囲であること（10回試行）"""
        for _ in range(10):
            resp = client.post("/api/divine")
            data = resp.get_json()
            assert 1 <= data["lower_number"] <= 8
            assert 1 <= data["upper_number"] <= 8

    def test_divine_changing_line_range(self, client):
        """/api/divine の変爻が1〜6の範囲であること（10回試行）"""
        for _ in range(10):
            resp = client.post("/api/divine")
            data = resp.get_json()
            assert 1 <= data["changing_line"] <= 6

    def test_divine_honke_has_six_lines(self, client):
        """/api/divine の本卦が6本の爻を持つこと"""
        resp = client.post("/api/divine")
        data = resp.get_json()
        assert len(data["honke"]["lines"]) == 6

    def test_divine_shike_has_six_lines(self, client):
        """/api/divine の之卦が6本の爻を持つこと"""
        resp = client.post("/api/divine")
        data = resp.get_json()
        assert len(data["shike"]["lines"]) == 6

    def test_trigrams_endpoint(self, client):
        """/api/trigrams が8つの八卦を返すこと"""
        resp = client.get("/api/trigrams")
        assert resp.status_code == 200
        data = resp.get_json()
        assert len(data) == 8

    def test_divine_changing_line_name(self, client):
        """/api/divine の変爻名称が正しい形式であること"""
        line_names = {"1": "初爻", "2": "二爻", "3": "三爻",
                      "4": "四爻", "5": "五爻", "6": "上爻"}
        resp = client.post("/api/divine")
        data = resp.get_json()
        assert data["changing_line_name"] in line_names.values()


# ─────────────────── get_line_names のテスト ───────────────────

class TestLineNames:
    def test_six_line_names(self):
        """爻位置名が6つであること"""
        names = get_line_names()
        assert len(names) == 6

    def test_line_name_first(self):
        """初爻の名称が正しいこと"""
        names = get_line_names()
        assert names[1] == "初爻"

    def test_line_name_last(self):
        """上爻の名称が正しいこと"""
        names = get_line_names()
        assert names[6] == "上爻"
