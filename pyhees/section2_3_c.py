# 付録 C 冷房設備の基準一次エネルギー消費量の算定に係る設定


# C.1 冷房方式 冷房方式は、当該住戸に設置される冷房設備に応じて第四章「暖冷房設備」第一節「全般」の付録 B により 定まる。

# C.2 標準的な冷房設備

# C.2.1 冷房設備の種類 冷房設備の種類は、当該住戸戸の冷房方式に応じて表 C.1 により定まる。

# 表 C.1 冷房設備の種類
def get_table_c_1():
    """付録 C 冷房設備の基準一次エネルギー消費量の算定に係る設定
    表 C.1 冷房設備の種類

    Args:

    Returns:
      tuple: 冷房設備の種類

    """
    table_c_1 = [
        ('ダクト式セントラル空調機', None, 'ルームエアコンディショナー', None, 'ルームエアコンディショナー')
    ]
    return table_c_1

# C.2.2 ダクト式セントラル空調機

# C.2.3 ルームエアコンディショナー

