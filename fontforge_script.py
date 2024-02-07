#!fontforge --lang=py -script

# 2つのフォントを合成する

import configparser
import math
import os
import shutil
import sys

import fontforge
import psMat

# iniファイルを読み込む
settings = configparser.ConfigParser()
settings.read("build.ini", encoding="utf-8")

VERSION = settings.get("DEFAULT", "VERSION")
FONT_NAME = settings.get("DEFAULT", "FONT_NAME")
SUFFIX_NEON = settings.get("DEFAULT", "SUFFIX_NEON")
SUFFIX_ARGON = settings.get("DEFAULT", "SUFFIX_ARGON")
SUFFIX_XENON = settings.get("DEFAULT", "SUFFIX_XENON")
SUFFIX_RADON = settings.get("DEFAULT", "SUFFIX_RADON")
SUFFIX_KRYPTON = settings.get("DEFAULT", "SUFFIX_KRYPTON")
JP_FONT = settings.get("DEFAULT", "JP_FONT")
ENG_FONT = settings.get("DEFAULT", "ENG_FONT")
SOURCE_FONTS_DIR = settings.get("DEFAULT", "SOURCE_FONTS_DIR")
BUILD_FONTS_DIR = settings.get("DEFAULT", "BUILD_FONTS_DIR")
VENDER_NAME = settings.get("DEFAULT", "VENDER_NAME")
FONTFORGE_PREFIX = settings.get("DEFAULT", "FONTFORGE_PREFIX")
IDEOGRAPHIC_SPACE = settings.get("DEFAULT", "IDEOGRAPHIC_SPACE")
# HALF_WIDTH_STR = settings.get("DEFAULT", "HALF_WIDTH_STR")
# SLASHED_ZERO_STR = settings.get("DEFAULT", "SLASHED_ZERO_STR")
# INVISIBLE_ZENKAKU_SPACE_STR = settings.get("DEFAULT", "INVISIBLE_ZENKAKU_SPACE_STR")
EM_ASCENT = int(settings.get("DEFAULT", "EM_ASCENT"))
EM_DESCENT = int(settings.get("DEFAULT", "EM_DESCENT"))
HALF_WIDTH_12 = int(settings.get("DEFAULT", "HALF_WIDTH_12"))
FULL_WIDTH_35 = int(settings.get("DEFAULT", "FULL_WIDTH_35"))
ENG_GLYPH_SCALE_12 = float(settings.get("DEFAULT", "ENG_GLYPH_SCALE_12"))

FONT_ASCENT = EM_ASCENT + 120
FONT_DESCENT = EM_DESCENT + 250

COPYRIGHT = """[Monaspace]
Copyright (c) 2023, GitHub https://github.com/githubnext/monaspace

[IBM Plex]
Copyright © 2017 IBM Corp. https://github.com/IBM/plex

[Moralerspace]
Copyright 2022 Yuko Otawara
"""  # noqa: E501

options = {}


def main():
    # オプション判定
    get_options()
    if options.get("unknown-option"):
        usage()
        return

    # buildディレクトリを作成する
    if os.path.exists(BUILD_FONTS_DIR):
        shutil.rmtree(BUILD_FONTS_DIR)
    os.mkdir(BUILD_FONTS_DIR)

    generate_neon()
    generate_argon()
    generate_xenon()
    generate_radon()
    generate_krypton()


def generate_neon():
    """Neon系統を生成する"""
    # Regular スタイルを生成する
    generate_font(
        jp_style="Text",
        eng_style="Regular",
        merged_style="Regular",
        suffix=SUFFIX_NEON,
    )
    # Bold スタイルを生成する
    generate_font(
        jp_style="Bold",
        eng_style="Bold",
        merged_style="Bold",
        suffix=SUFFIX_NEON,
    )
    # # Light スタイルを生成する
    # generate_font(
    #     jp_style="Light",
    #     eng_style="ExtraLight",
    #     merged_style="Light",
    #     suffix=SUFFIX_NEON,
    # )
    # # Medium スタイルを生成する
    # generate_font(
    #     jp_style="Medium",
    #     eng_style="Medium",
    #     merged_style="Medium",
    #     suffix=SUFFIX_NEON,
    # )
    # # SemiBold スタイルを生成する
    # generate_font(
    #     jp_style="SemiBold",
    #     eng_style="SemiBold",
    #     merged_style="SemiBold",
    #     suffix=SUFFIX_NEON,
    # )

    # Regular Italic スタイルを生成する
    generate_font(
        jp_style="Text",
        eng_style="Italic",
        merged_style="Italic",
        suffix=SUFFIX_NEON,
        italic=True,
    )
    # Bold Italic スタイルを生成する
    generate_font(
        jp_style="Bold",
        eng_style="BoldItalic",
        merged_style="BoldItalic",
        suffix=SUFFIX_NEON,
        italic=True,
    )


def generate_argon():
    """Argon系統を生成する"""
    # Regular スタイルを生成する
    generate_font(
        jp_style="Text",
        eng_style="Regular",
        merged_style="Regular",
        suffix=SUFFIX_ARGON,
    )
    # Bold スタイルを生成する
    generate_font(
        jp_style="Bold",
        eng_style="Bold",
        merged_style="Bold",
        suffix=SUFFIX_ARGON,
    )

    # Regular Italic スタイルを生成する
    generate_font(
        jp_style="Text",
        eng_style="Italic",
        merged_style="Italic",
        suffix=SUFFIX_ARGON,
        italic=True,
    )
    # Bold Italic スタイルを生成する
    generate_font(
        jp_style="Bold",
        eng_style="BoldItalic",
        merged_style="BoldItalic",
        suffix=SUFFIX_ARGON,
        italic=True,
    )


def generate_xenon():
    """Xenon系統を生成する"""
    # Regular スタイルを生成する
    generate_font(
        jp_style="Text",
        eng_style="Regular",
        merged_style="Regular",
        suffix=SUFFIX_XENON,
    )
    # Bold スタイルを生成する
    generate_font(
        jp_style="Bold",
        eng_style="Bold",
        merged_style="Bold",
        suffix=SUFFIX_XENON,
    )

    # Regular Italic スタイルを生成する
    generate_font(
        jp_style="Text",
        eng_style="Italic",
        merged_style="Italic",
        suffix=SUFFIX_XENON,
        italic=True,
    )
    # Bold Italic スタイルを生成する
    generate_font(
        jp_style="Bold",
        eng_style="BoldItalic",
        merged_style="BoldItalic",
        suffix=SUFFIX_XENON,
        italic=True,
    )


def generate_radon():
    """Radon系統を生成する"""
    # Regular スタイルを生成する
    generate_font(
        jp_style="Text",
        eng_style="Regular",
        merged_style="Regular",
        suffix=SUFFIX_RADON,
    )
    # Bold スタイルを生成する
    generate_font(
        jp_style="Bold",
        eng_style="Bold",
        merged_style="Bold",
        suffix=SUFFIX_RADON,
    )

    # Regular Italic スタイルを生成する
    generate_font(
        jp_style="Text",
        eng_style="Italic",
        merged_style="Italic",
        suffix=SUFFIX_RADON,
        italic=True,
    )
    # Bold Italic スタイルを生成する
    generate_font(
        jp_style="Bold",
        eng_style="BoldItalic",
        merged_style="BoldItalic",
        suffix=SUFFIX_RADON,
        italic=True,
    )


def generate_krypton():
    """Krypton系統を生成する"""
    # Regular スタイルを生成する
    generate_font(
        jp_style="Text",
        eng_style="Regular",
        merged_style="Regular",
        suffix=SUFFIX_KRYPTON,
    )
    # Bold スタイルを生成する
    generate_font(
        jp_style="Bold",
        eng_style="Bold",
        merged_style="Bold",
        suffix=SUFFIX_KRYPTON,
    )

    # Regular Italic スタイルを生成する
    generate_font(
        jp_style="Text",
        eng_style="Italic",
        merged_style="Italic",
        suffix=SUFFIX_KRYPTON,
        italic=True,
    )
    # Bold Italic スタイルを生成する
    generate_font(
        jp_style="Bold",
        eng_style="BoldItalic",
        merged_style="BoldItalic",
        suffix=SUFFIX_KRYPTON,
        italic=True,
    )


def usage():
    print(
        f"Usage: {sys.argv[0]} "
        "[--slashed-zero] [--invisible-zenkaku-space] [--half-width]"
    )


def get_options():
    """オプションを取得する"""

    global options

    # オプションなしの場合は何もしない
    if len(sys.argv) == 1:
        return

    for arg in sys.argv[1:]:
        # オプション判定
        if arg == "--slashed-zero":
            options["slashed-zero"] = True
        elif arg == "--invisible-zenkaku-space":
            options["invisible-zenkaku-space"] = True
        elif arg == "--half-width":
            options["half-width"] = True
        else:
            options["unknown-option"] = True
            return


def generate_font(jp_style, eng_style, merged_style, suffix, italic=False):
    print(f"=== Generate {merged_style} style ===")

    # 合成するフォントを開く
    jp_font, eng_font = open_fonts(jp_style, f"{suffix}-{eng_style}")

    # フォントのEMを1000に変換する
    # jp_font は既に1000なので eng_font のみ変換する
    em_1000(eng_font)

    # TODO 合成に邪魔なグリフを削除する
    # delete_unwanted_glyphs(eng_font)

    # 重複するグリフを削除する
    delete_duplicate_glyphs(jp_font, eng_font)

    # 日本語グリフの斜体を生成する
    if italic:
        transform_italic_glyphs(jp_font)

    # スラッシュ付きゼロ
    if options.get("slashed-zero"):
        slashed_zero(eng_font)

    # 3:5幅版との差分を調整する
    if options.get("half-width"):
        # 1:2 幅にする
        transform_half_width(jp_font, eng_font)
    else:
        # jp_fontで半角幅(500)のグリフの幅を3:5になるよう調整する
        width_600_or_1000(jp_font)

    # eng_fontを半角幅(600)にする
    width_600(eng_font)

    # GSUBテーブルを削除する (ひらがな等の全角文字が含まれる行でリガチャが解除される対策)
    remove_lookups(jp_font)

    # 全角スペースを可視化する
    if not options.get("invisible-zenkaku-space"):
        visualize_zenkaku_space(jp_font, eng_font)

    # 合成する
    eng_font.mergeFonts(jp_font)

    # TODO オプション毎の修飾子を追加する
    # variant = HALF_WIDTH_STR if options.get("half-width") else ""
    # variant += SLASHED_ZERO_STR if options.get("slashed-zero") else ""
    # variant += (
    #     INVISIBLE_ZENKAKU_SPACE_STR if options.get("invisible-zenkaku-space") else ""
    # )
    variant = ""

    # メタデータを編集する
    edit_meta_data(eng_font, merged_style, variant, suffix)

    # ttfファイルに保存
    eng_font.generate(
        f"{BUILD_FONTS_DIR}/{FONTFORGE_PREFIX}{FONT_NAME}{suffix}{variant}-{merged_style}.ttf"
    )

    # ttfを閉じる
    jp_font.close()
    eng_font.close()


def open_fonts(jp_style: str, eng_style: str):
    return fontforge.open(
        f"{SOURCE_FONTS_DIR}/{JP_FONT}{jp_style}.ttf"
    ), fontforge.open(f"{SOURCE_FONTS_DIR}/{ENG_FONT}{eng_style}.otf")


def em_1000(font):
    """フォントのEMを1000に変換する"""
    em_size = EM_ASCENT + EM_DESCENT
    font.em = em_size


def delete_unwanted_glyphs(font):
    """eng_font側のグリフを削除する。これにより合成時にjp_font側のグリフが優先される"""
    # U+0000
    clear_glyph_range(font, 0x0000, 0x0000)
    # U+FF01-FF5D
    clear_glyph_range(font, 0xFF01, 0xFF5D)
    # U+FF62-FF63
    clear_glyph_range(font, 0xFF62, 0xFF63)
    # U+3001-3015
    clear_glyph_range(font, 0x3001, 0x3015)
    # U+FF0D
    clear_glyph_range(font, 0xFF0D, 0xFF0D)


def clear_glyph_range(font, start: int, end: int):
    """グリフを削除する"""
    for i in range(start, end + 1):
        for glyph in font.selection.select(("ranges", None), i).byGlyphs:
            glyph.clear()
    font.selection.none()


def delete_duplicate_glyphs(jp_font, eng_font):
    """jp_fontとeng_fontのグリフを比較し、重複するグリフを削除する"""
    try:
        for glyph in jp_font.glyphs():
            if glyph.unicode > 0:
                eng_font.selection.select(("more", "unicode"), glyph.unicode)
    except ValueError:
        pass
    for glyph in eng_font.selection.byGlyphs:
        if glyph.isWorthOutputting():
            jp_font.selection.select(("more", "unicode"), glyph.unicode)
    for glyph in jp_font.selection.byGlyphs:
        glyph.clear()
    jp_font.selection.none()
    eng_font.selection.none()


def remove_lookups(font):
    """GSUB, GPOSテーブルを削除する"""
    for lookup in list(font.gsub_lookups) + list(font.gpos_lookups):
        font.removeLookup(lookup)


def transform_italic_glyphs(font):
    # 斜体の傾き
    ITALIC_SLOPE = 11
    # 傾きを設定する
    font.italicangle = -ITALIC_SLOPE
    # 全グリフを斜体に変換
    for glyph in font.glyphs():
        glyph.transform(psMat.skew(ITALIC_SLOPE * math.pi / 180))


def slashed_zero(font):
    # "zero.zero" を "zero" にコピーする
    font.selection.select("zero.zero")
    font.copy()
    font.selection.select(("unicode", None), 0x0030)
    font.paste()
    font.selection.none()


def width_600_or_1000(jp_font):
    """半角幅か全角幅になるように変換する"""
    for glyph in jp_font.glyphs():
        if 0 < glyph.width < 600:
            # グリフ位置を調整してから幅を設定
            glyph.transform(psMat.translate((600 - glyph.width) / 2, 0))
            glyph.width = 600
        elif 600 < glyph.width < 1000:
            # グリフ位置を調整してから幅を設定
            glyph.transform(psMat.translate((1000 - glyph.width) / 2, 0))
            glyph.width = 1000


def width_600(eng_font):
    """半角幅になるように変換する"""
    for glyph in eng_font.glyphs():
        if glyph.width == 620:
            # グリフ位置を調整してから幅を設定
            glyph.transform(psMat.translate((600 - glyph.width) / 2, 0))
            glyph.width = 600


def transform_half_width(jp_font, eng_font):
    """1:2幅になるように変換する"""
    for glyph in eng_font.selection.select(("unicode", None), 0x0030).byGlyphs:
        before_width_eng = glyph.width
    after_width_eng = HALF_WIDTH_12
    for glyph in eng_font.glyphs():
        if glyph.width == before_width_eng:
            # 縮小
            glyph.transform(psMat.scale(ENG_GLYPH_SCALE_12, 1))
            # グリフ位置を調整してから幅を設定
            glyph.transform(psMat.translate(-(glyph.width - after_width_eng) / 2, 0))
            glyph.width = after_width_eng

    for glyph in jp_font.selection.select(("unicode", None), 0x3042).byGlyphs:
        before_half_width_jp = glyph.width / 2
        before_full_width_jp = glyph.width
    after_width_jp = HALF_WIDTH_12 * 2
    for glyph in jp_font.glyphs():
        if glyph.width == before_half_width_jp:
            # 英数字グリフと同じ幅にする
            glyph.transform(psMat.translate(-(glyph.width - after_width_eng) / 2, 0))
            glyph.width = after_width_eng
        elif glyph.width == before_full_width_jp:
            # グリフ位置を調整してから幅を設定
            glyph.transform(psMat.translate(-(glyph.width - after_width_jp) / 2, 0))
            glyph.width = after_width_jp


def visualize_zenkaku_space(jp_font, eng_font):
    """全角スペースを可視化する"""
    # 別名情報を解除
    jp_font.selection.select(("unicode", None), 0x2003)
    for glyph in jp_font.selection.byGlyphs:
        glyph.altuni = None

    jp_font.mergeFonts(fontforge.open(f"{SOURCE_FONTS_DIR}/{IDEOGRAPHIC_SPACE}"))

    # 全角スペースをクリア
    eng_font.selection.select(("unicode", None), 0x3000)
    for glyph in eng_font.selection.byGlyphs:
        glyph.clear()
    eng_font.selection.none()


def edit_meta_data(font, weight: str, variant: str, suffix: str):
    """フォント内のメタデータを編集する"""
    font.ascent = EM_ASCENT
    font.descent = EM_DESCENT
    font.os2_typoascent = EM_ASCENT
    font.os2_typodescent = -EM_DESCENT

    font.hhea_ascent = FONT_ASCENT
    font.hhea_descent = -FONT_DESCENT
    font.os2_winascent = FONT_ASCENT
    font.os2_windescent = FONT_DESCENT
    font.hhea_linegap = 0
    font.os2_typolinegap = 0

    # TODO 必要かどうか検討する
    # 一部ソフトで日本語表示ができなくなる事象への対策
    # なぜかJuliaMonoでは韓国語のビットが立っているので、それを除外し、代わりに日本語ビットを立てる
    # font.os2_codepages = (0b1100000000000100000000111111111, 0)

    font.sfnt_names = (
        (
            "English (US)",
            "License",
            """This Font Software is licensed under the SIL Open Font License,
Version 1.1. This license is available with a FAQ
at: http://scripts.sil.org/OFL""",
        ),
        ("English (US)", "License URL", "http://scripts.sil.org/OFL"),
        ("English (US)", "Version", VERSION),
    )
    font.familyname = f"{FONT_NAME} {suffix} {variant}".strip()
    font.fontname = f"{FONT_NAME}{suffix}{variant}-{weight}"
    font.fullname = f"{FONT_NAME} {suffix} {variant}".strip() + f" {weight}"
    font.os2_vendor = VENDER_NAME
    font.copyright = COPYRIGHT


if __name__ == "__main__":
    main()
