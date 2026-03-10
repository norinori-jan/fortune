"""
易（周易）の八卦・六十四卦データ
八卦（はっけ）の定義と六十四卦の組み合わせを管理するモジュール
"""

# 八卦（はっけ）の定義
# number: 1-8 の番号
# lines: 爻（こう）の配列 [初爻, 二爻, 三爻] (1=陽, 0=陰, 下から順)
TRIGRAMS = {
    1: {"name": "乾", "reading": "けん", "symbol": "☰", "element": "天", "lines": [1, 1, 1]},
    2: {"name": "兌", "reading": "だ",  "symbol": "☱", "element": "沢", "lines": [0, 1, 1]},
    3: {"name": "離", "reading": "り",  "symbol": "☲", "element": "火", "lines": [1, 0, 1]},
    4: {"name": "震", "reading": "しん","symbol": "☳", "element": "雷", "lines": [0, 0, 1]},
    5: {"name": "巽", "reading": "そん","symbol": "☴", "element": "風", "lines": [1, 1, 0]},
    6: {"name": "坎", "reading": "かん","symbol": "☵", "element": "水", "lines": [0, 1, 0]},
    7: {"name": "艮", "reading": "ごん","symbol": "☶", "element": "山", "lines": [1, 0, 0]},
    8: {"name": "坤", "reading": "こん","symbol": "☷", "element": "地", "lines": [0, 0, 0]},
}

# 六十四卦（ろくじゅうしけ）のデータ
# キー: (下卦番号, 上卦番号) — どちらも 1-8 の八卦番号
# 王弼序（周易の伝統的な順序）に基づく
HEXAGRAMS = {
    (1, 1): {"number":  1, "name": "乾為天",   "reading": "けんいてん",   "meaning": "健全・創造・天の力", "description": "元亨利貞。天は絶えず動き、万物を生み出す。強くあれ。"},
    (8, 8): {"number":  2, "name": "坤為地",   "reading": "こんいち",     "meaning": "従順・包容・大地の力", "description": "元亨、利牝馬之貞。大地は万物を育む。柔らかく従順であれ。"},
    (4, 6): {"number":  3, "name": "水雷屯",   "reading": "すいらいちゅん","meaning": "困難の始まり・創業の苦労", "description": "元亨利貞。勿用有攸往。困難を乗り越え、地固めをせよ。"},
    (6, 7): {"number":  4, "name": "山水蒙",   "reading": "さんすいもう", "meaning": "無知・啓蒙・学びの始まり", "description": "亨。匪我求童蒙、童蒙求我。学ぶ姿勢を持ち、師を尊重せよ。"},
    (1, 6): {"number":  5, "name": "水天需",   "reading": "すいてんじゅ", "meaning": "待機・忍耐・機会を待つ", "description": "有孚、光亨、貞吉。利渉大川。時を待つことが大切だ。"},
    (6, 1): {"number":  6, "name": "天水訟",   "reading": "てんすいしょう","meaning": "争い・訴訟・対立", "description": "有孚窒惕、中吉、終凶。争いは避け、和解を目指せ。"},
    (6, 8): {"number":  7, "name": "地水師",   "reading": "ちすいし",     "meaning": "軍勢・規律・指導力", "description": "貞、丈人吉、无咎。秩序と規律を保ち、大義のために動け。"},
    (8, 6): {"number":  8, "name": "水地比",   "reading": "すいちひ",     "meaning": "親しむ・協力・結束", "description": "吉。原筮元永貞、无咎。志を同じくする者と結びつけ。"},
    (1, 5): {"number":  9, "name": "風天小畜", "reading": "ふうてんしょうちく","meaning": "小さな蓄積・漸進", "description": "亨。密雲不雨、自我西郊。小さな力でも積み重ねよ。"},
    (2, 1): {"number": 10, "name": "天沢履",   "reading": "てんたくり",   "meaning": "礼節・慎重な行動", "description": "履虎尾、不咥人、亨。礼儀を守り慎重に進め。"},
    (1, 8): {"number": 11, "name": "地天泰",   "reading": "ちてんたい",   "meaning": "平和・繁栄・調和", "description": "小往大来、吉亨。天地が交わり万物が栄える。好機だ。"},
    (8, 1): {"number": 12, "name": "天地否",   "reading": "てんちひ",     "meaning": "停滞・閉塞・行き詰まり", "description": "否之匪人、不利君子貞。天地が離れ交流が絶える。忍耐せよ。"},
    (3, 1): {"number": 13, "name": "天火同人", "reading": "てんかどうじん","meaning": "協同・一致・団結", "description": "同人于野、亨。利渉大川。仲間と力を合わせて大事を成せ。"},
    (1, 3): {"number": 14, "name": "火天大有", "reading": "かてんたいゆう","meaning": "大いなる所有・繁栄", "description": "元亨。豊かな収穫と大きな成功が待っている。"},
    (7, 8): {"number": 15, "name": "地山謙",   "reading": "ちざんけん",   "meaning": "謙遜・謙虚・控えめ", "description": "亨、君子有終。謙虚であることが成功の道だ。"},
    (8, 4): {"number": 16, "name": "雷地豫",   "reading": "らいちよ",     "meaning": "喜び・準備・楽観", "description": "利建侯行師。喜びの時、しかし油断は禁物だ。"},
    (4, 2): {"number": 17, "name": "沢雷随",   "reading": "たくらいずい",  "meaning": "随う・適応・追随", "description": "元亨利貞、无咎。時勢に従い、柔軟に対応せよ。"},
    (5, 7): {"number": 18, "name": "山風蠱",   "reading": "さんぷうこ",   "meaning": "腐敗の修正・改革", "description": "元亨。利渉大川。古い問題を正し、改革を進めよ。"},
    (2, 8): {"number": 19, "name": "地沢臨",   "reading": "ちたくりん",   "meaning": "臨む・近づく・監督", "description": "元亨利貞。至于八月有凶。積極的に関わり、指導せよ。"},
    (8, 5): {"number": 20, "name": "風地観",   "reading": "ふうちかん",   "meaning": "観察・洞察・見渡す", "description": "盥而不薦、有孚顒若。よく観察し、内省せよ。"},
    (4, 3): {"number": 21, "name": "火雷噬嗑", "reading": "からいぜいこう","meaning": "噛み砕く・決断・刑罰", "description": "亨。利用獄。障害を取り除き、問題を解決せよ。"},
    (3, 7): {"number": 22, "name": "山火賁",   "reading": "さんかひ",     "meaning": "装飾・文明・外見の美", "description": "亨。小利有攸往。外見を整えつつ、本質を忘れるな。"},
    (8, 7): {"number": 23, "name": "山地剥",   "reading": "さんちはく",   "meaning": "剥落・崩壊・衰退", "description": "不利有攸往。衰退の時。静かに守り、再起を待て。"},
    (4, 8): {"number": 24, "name": "地雷復",   "reading": "ちらいふく",   "meaning": "回帰・復活・新たな始まり", "description": "亨。出入无疾、朋来无咎。陽が戻り、復活の兆しがある。"},
    (4, 1): {"number": 25, "name": "天雷无妄", "reading": "てんらいむもう","meaning": "無為・自然・純粋な行動", "description": "元亨利貞。自然の道に従い、作為なく行動せよ。"},
    (1, 7): {"number": 26, "name": "山天大畜", "reading": "さんてんたいちく","meaning": "大いなる蓄積・制約", "description": "利貞。不家食吉。利渉大川。力を蓄え、時を待て。"},
    (4, 7): {"number": 27, "name": "山雷頤",   "reading": "さんらいい",   "meaning": "養う・育む・口を慎む", "description": "貞吉。観頤、自求口実。何を養い、何を求めるかに注意せよ。"},
    (5, 2): {"number": 28, "name": "沢風大過", "reading": "たくふうたいか","meaning": "過剰・限界・大きな過ち", "description": "棟撓。利有攸往、亨。大きな重圧がある。勇気を持って行動せよ。"},
    (6, 6): {"number": 29, "name": "坎為水",   "reading": "かんいすい",   "meaning": "険難・試練・危険", "description": "有孚、維心亨、行有尚。危険の中にあっても誠実さを保て。"},
    (3, 3): {"number": 30, "name": "離為火",   "reading": "りいか",       "meaning": "輝き・依存・明快", "description": "利貞、亨。畜牝牛吉。明るく輝きながら、何かに依りかかれ。"},
    (7, 2): {"number": 31, "name": "沢山咸",   "reading": "たくざんかん",  "meaning": "感応・交感・引き合い", "description": "亨利貞、取女吉。心が通じ合う。素直に感じ、応じよ。"},
    (5, 4): {"number": 32, "name": "雷風恒",   "reading": "らいふうこう",  "meaning": "恒久・継続・不変", "description": "亨无咎、利貞。利有攸往。継続することが成功の鍵だ。"},
    (7, 1): {"number": 33, "name": "天山遯",   "reading": "てんざんとん",  "meaning": "退却・隠遁・引き下がる", "description": "亨小利貞。時には退くことが賢明だ。"},
    (1, 4): {"number": 34, "name": "雷天大壮", "reading": "らいてんたいそう","meaning": "大いなる力・勢力", "description": "利貞。強い力がある。しかし行き過ぎを戒めよ。"},
    (8, 3): {"number": 35, "name": "火地晋",   "reading": "かちしん",     "meaning": "進歩・前進・昇進", "description": "康侯用錫馬蕃庶。昼三接。積極的に前進する時だ。"},
    (3, 8): {"number": 36, "name": "地火明夷", "reading": "ちかめいい",   "meaning": "暗闇・逆境・光を隠す", "description": "利艱貞。困難の中でも内なる光を守れ。"},
    (3, 5): {"number": 37, "name": "風火家人", "reading": "ふうかかじん",  "meaning": "家族・家庭・役割", "description": "利女貞。家庭の秩序を大切にせよ。"},
    (2, 3): {"number": 38, "name": "火沢睽",   "reading": "かたくけい",   "meaning": "乖離・相違・反目", "description": "小事吉。対立する状況でも、小さな合意点を見つけよ。"},
    (7, 6): {"number": 39, "name": "水山蹇",   "reading": "すいざんけん",  "meaning": "困難・障害・足踏み", "description": "利西南、不利東北。利見大人、貞吉。困難な道。助けを求めよ。"},
    (6, 4): {"number": 40, "name": "雷水解",   "reading": "らいすいかい",  "meaning": "解放・解決・緊張の緩和", "description": "利西南。困難が解けていく。過去を手放し前へ進め。"},
    (2, 7): {"number": 41, "name": "山沢損",   "reading": "さんたくそん",  "meaning": "減少・献身・犠牲", "description": "有孚、元吉无咎可貞。下を減らして上に捧げることで吉となる。"},
    (4, 5): {"number": 42, "name": "風雷益",   "reading": "ふうらいえき",  "meaning": "増益・利益・成長", "description": "利有攸往、利渉大川。上を減らして下に与える。大きな利益がある。"},
    (1, 2): {"number": 43, "name": "沢天夬",   "reading": "たくてんかい",  "meaning": "決断・突破・明快", "description": "揚于王庭。断固として決断し、小人を追い払え。"},
    (5, 1): {"number": 44, "name": "天風姤",   "reading": "てんぷうこう",  "meaning": "出会い・誘惑・偶然の遭遇", "description": "女壮、勿用取女。偶然の出会いがある。しかし慎重に。"},
    (8, 2): {"number": 45, "name": "沢地萃",   "reading": "たくちすい",   "meaning": "集合・結集・団結", "description": "亨。王仮有廟。多くが集まる時。指導者のもとに結集せよ。"},
    (5, 8): {"number": 46, "name": "地風升",   "reading": "ちふうしょう",  "meaning": "上昇・昇進・着実な成長", "description": "元亨。用見大人、勿恤。南征吉。着実に上へ進め。"},
    (6, 2): {"number": 47, "name": "沢水困",   "reading": "たくすいこん",  "meaning": "困窮・苦境・行き詰まり", "description": "亨、貞大人吉、无咎。困難の中でも誠実さを失うな。"},
    (5, 6): {"number": 48, "name": "水風井",   "reading": "すいふうせい",  "meaning": "井戸・源泉・不変の価値", "description": "改邑不改井、无喪无得。源泉は枯れない。本質的な価値を守れ。"},
    (3, 2): {"number": 49, "name": "沢火革",   "reading": "たくかかく",   "meaning": "変革・革命・改革", "description": "巳日乃孚、元亨利貞悔亡。時が来たら大胆に変革せよ。"},
    (5, 3): {"number": 50, "name": "火風鼎",   "reading": "かふうてい",   "meaning": "鼎・変容・新秩序", "description": "元吉亨。古いものを取り込み、新しい価値を生み出せ。"},
    (4, 4): {"number": 51, "name": "震為雷",   "reading": "しんいらい",   "meaning": "雷・衝撃・覚醒", "description": "亨。震来虩虩、笑言哑哑。衝撃の後に笑いが訪れる。"},
    (7, 7): {"number": 52, "name": "艮為山",   "reading": "ごんいざん",   "meaning": "静止・静寂・止まる", "description": "艮其背、不獲其身。時には立ち止まり、動じないことが大切だ。"},
    (7, 5): {"number": 53, "name": "風山漸",   "reading": "ふうざんぜん",  "meaning": "漸進・段階的発展・着実", "description": "女帰吉。利貞。焦らず、段階を踏んで着実に進め。"},
    (2, 4): {"number": 54, "name": "雷沢帰妹", "reading": "らいたくきまい","meaning": "嫁ぐ・関係・従属", "description": "征凶、无攸利。関係において分を守ることが大切だ。"},
    (3, 4): {"number": 55, "name": "雷火豊",   "reading": "らいかほう",   "meaning": "豊かさ・最盛期・栄光", "description": "亨、王仮之。勿憂、宜日中。今が最盛期。明るく輝け。"},
    (7, 3): {"number": 56, "name": "火山旅",   "reading": "かざんりょ",   "meaning": "旅・流浪・異境", "description": "小亨、旅貞吉。旅人として謙虚に、礼儀を守れ。"},
    (5, 5): {"number": 57, "name": "巽為風",   "reading": "そんいふう",   "meaning": "柔順・浸透・従う", "description": "小亨、利有攸往、利見大人。柔らかく、しかし着実に浸透せよ。"},
    (2, 2): {"number": 58, "name": "兌為沢",   "reading": "だいたく",     "meaning": "喜び・説得・交流", "description": "亨利貞。喜びと対話が吉をもたらす。真の喜びを分かち合え。"},
    (6, 5): {"number": 59, "name": "風水渙",   "reading": "ふうすいかん",  "meaning": "離散・分散・統合", "description": "亨。王仮有廟。利渉大川、利貞。散らばったものを集め直せ。"},
    (2, 6): {"number": 60, "name": "水沢節",   "reading": "すいたくせつ",  "meaning": "節制・制限・中庸", "description": "亨。苦節不可貞。適度な節制が調和をもたらす。"},
    (2, 5): {"number": 61, "name": "風沢中孚", "reading": "ふうたくちゅうふ","meaning": "誠信・内なる誠実さ", "description": "豚魚吉。利渉大川、利貞。誠実な心が万物を動かす。"},
    (7, 4): {"number": 62, "name": "雷山小過", "reading": "らいざんしょうか","meaning": "小さな過ち・慎重さ", "description": "亨利貞。可小事、不可大事。小さなことに徹し、大きなことは慎め。"},
    (3, 6): {"number": 63, "name": "水火既済", "reading": "すいかきさい",  "meaning": "完成・成就・完了", "description": "亨小、利貞。初吉終乱。物事が成就した。しかし油断するな。"},
    (6, 3): {"number": 64, "name": "火水未済", "reading": "かすいびさい",  "meaning": "未完成・移行期・可能性", "description": "亨。小狐汔済、濡其尾、无攸利。まだ完成していない。慎重に進め。"},
}


def get_trigram(number: int) -> dict:
    """八卦番号(1-8)から八卦データを取得する"""
    if number not in TRIGRAMS:
        raise ValueError(f"八卦番号は1〜8の整数で指定してください: {number}")
    return TRIGRAMS[number]


def get_hexagram(lower: int, upper: int) -> dict:
    """下卦・上卦番号から六十四卦データを取得する"""
    key = (lower, upper)
    if key not in HEXAGRAMS:
        raise ValueError(f"卦の組み合わせが見つかりません: 下卦={lower}, 上卦={upper}")
    hexagram = HEXAGRAMS[key].copy()
    hexagram["lower_trigram"] = TRIGRAMS[lower]
    hexagram["upper_trigram"] = TRIGRAMS[upper]
    # 六爻（ろくこう）: 下卦3爻 + 上卦3爻
    hexagram["lines"] = TRIGRAMS[lower]["lines"] + TRIGRAMS[upper]["lines"]
    return hexagram


def get_changing_hexagram(lower: int, upper: int, changing_line: int) -> dict:
    """変爻後の之卦（しか）を求める

    Args:
        lower: 下卦番号 (1-8)
        upper: 上卦番号 (1-8)
        changing_line: 変爻の位置 (1-6, 1=初爻, 6=上爻)

    Returns:
        之卦のデータ
    """
    original_lines = TRIGRAMS[lower]["lines"] + TRIGRAMS[upper]["lines"]
    new_lines = original_lines.copy()
    # 変爻: 陽→陰, 陰→陽
    idx = changing_line - 1
    new_lines[idx] = 1 - new_lines[idx]
    new_lower_lines = new_lines[:3]
    new_upper_lines = new_lines[3:]

    # 爻の配列から八卦番号を逆引き
    new_lower = _lines_to_trigram_number(new_lower_lines)
    new_upper = _lines_to_trigram_number(new_upper_lines)

    return get_hexagram(new_lower, new_upper)


def _lines_to_trigram_number(lines: list) -> int:
    """爻の配列 [初爻, 二爻, 三爻] から八卦番号を返す"""
    for num, trigram in TRIGRAMS.items():
        if trigram["lines"] == lines:
            return num
    raise ValueError(f"対応する八卦が見つかりません: {lines}")


def get_line_names() -> dict:
    """爻の位置名称を返す"""
    return {
        1: "初爻",
        2: "二爻",
        3: "三爻",
        4: "四爻",
        5: "五爻",
        6: "上爻",
    }
