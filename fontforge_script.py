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
JP_FONT_RADON = settings.get("DEFAULT", "JP_FONT_RADON")
JP_FONT_KRYPTON = settings.get("DEFAULT", "JP_FONT_KRYPTON")
JP_FONT_BIZUD = settings.get("DEFAULT", "JP_FONT_BIZUD")
ENG_FONT = settings.get("DEFAULT", "ENG_FONT")
SOURCE_FONTS_DIR = settings.get("DEFAULT", "SOURCE_FONTS_DIR")
BUILD_FONTS_DIR = settings.get("DEFAULT", "BUILD_FONTS_DIR")
VENDER_NAME = settings.get("DEFAULT", "VENDER_NAME")
FONTFORGE_PREFIX = settings.get("DEFAULT", "FONTFORGE_PREFIX")
IDEOGRAPHIC_SPACE = settings.get("DEFAULT", "IDEOGRAPHIC_SPACE")
HALF_WIDTH_STR = settings.get("DEFAULT", "HALF_WIDTH_STR")
# INVISIBLE_ZENKAKU_SPACE_STR = settings.get("DEFAULT", "INVISIBLE_ZENKAKU_SPACE_STR")
JPDOC_STR = settings.get("DEFAULT", "JPDOC_STR")
# SLASHED_ZERO_STR = settings.get("DEFAULT", "SLASHED_ZERO_STR")
EM_ASCENT = int(settings.get("DEFAULT", "EM_ASCENT"))
EM_DESCENT = int(settings.get("DEFAULT", "EM_DESCENT"))
HALF_WIDTH_12 = int(settings.get("DEFAULT", "HALF_WIDTH_12"))
FULL_WIDTH_35 = int(settings.get("DEFAULT", "FULL_WIDTH_35"))

COPYRIGHT = """[Monaspace]
Copyright (c) 2023, GitHub https://github.com/githubnext/monaspace

[IBM Plex]
Copyright © 2017 IBM Corp. https://github.com/IBM/plex

[Kiwi Maru]
Copyright 2020 The Kiwi Maru Project Authors https://github.com/Kiwi-KawagotoKajiru/Kiwi-Maru

[Stick]
Copyright 2020 The Stick Project Authors https://github.com/fontworks-fonts/Stick

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

    """日本語フォントをBIZ UDにする"""
    # Regular スタイルを生成する
    generate_font(
        jp_style="Regular",
        eng_style="Regular",
        merged_style="Regular",
        suffix=SUFFIX_NEON,
        jp_font_base=JP_FONT_BIZUD
    )
    # Bold スタイルを生成する
    generate_font(
        jp_style="Bold",
        eng_style="Bold",
        merged_style="Bold",
        suffix=SUFFIX_NEON,
        jp_font_base=JP_FONT_BIZUD
    )

    # Regular Italic スタイルを生成する
    generate_font(
        jp_style="Regular",
        eng_style="Italic",
        merged_style="Italic",
        suffix=SUFFIX_NEON,
        italic=True,
        jp_font_base=JP_FONT_BIZUD
    )
    # Bold Italic スタイルを生成する
    generate_font(
        jp_style="Bold",
        eng_style="BoldItalic",
        merged_style="BoldItalic",
        suffix=SUFFIX_NEON,
        italic=True,
        jp_font_base=JP_FONT_BIZUD
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

    """BIZUDベースを生成する"""
    # Regular スタイルを生成する
    generate_font(
        jp_style="Regular",
        eng_style="Regular",
        merged_style="Regular",
        suffix=SUFFIX_ARGON,
        jp_font_base=JP_FONT_BIZUD
    )
    # Bold スタイルを生成する
    generate_font(
        jp_style="Bold",
        eng_style="Bold",
        merged_style="Bold",
        suffix=SUFFIX_ARGON,
        jp_font_base=JP_FONT_BIZUD
    )

    # Regular Italic スタイルを生成する
    generate_font(
        jp_style="Regular",
        eng_style="Italic",
        merged_style="Italic",
        suffix=SUFFIX_ARGON,
        italic=True,
        jp_font_base=JP_FONT_BIZUD
    )
    # Bold Italic スタイルを生成する
    generate_font(
        jp_style="Bold",
        eng_style="BoldItalic",
        merged_style="BoldItalic",
        suffix=SUFFIX_ARGON,
        italic=True,
        jp_font_base=JP_FONT_BIZUD
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
        jp_style="Medium",
        eng_style="Regular",
        merged_style="Regular",
        suffix=SUFFIX_RADON,
        jp_font_base=JP_FONT_RADON
    )
    # Bold スタイルを生成する
    generate_font(
        jp_style="Bold",
        eng_style="Bold",
        merged_style="Bold",
        suffix=SUFFIX_RADON,
        jp_font_base=JP_FONT_RADON
    )

    # Regular Italic スタイルを生成する
    generate_font(
        jp_style="Medium",
        eng_style="Italic",
        merged_style="Italic",
        suffix=SUFFIX_RADON,
        italic=True,
        jp_font_base=JP_FONT_RADON
    )
    # Bold Italic スタイルを生成する
    # generate_font(
    generate_font(
        jp_style="Bold",
        eng_style="BoldItalic",
        merged_style="BoldItalic",
        suffix=SUFFIX_RADON,
        italic=True,
        jp_font_base=JP_FONT_RADON
    )


def generate_krypton():
    """Krypton系統を生成する"""
    # Regular スタイルを生成する
    generate_font(
        jp_style="Regular",
        eng_style="Regular",
        merged_style="Regular",
        suffix=SUFFIX_KRYPTON,
        jp_font_base=JP_FONT_KRYPTON
    )
    # Bold スタイルを生成する
    generate_font(
        jp_style="Bold",
        eng_style="Bold",
        merged_style="Bold",
        suffix=SUFFIX_KRYPTON,
        jp_font_base=JP_FONT_KRYPTON
    )

    # Regular Italic スタイルを生成する
    generate_font(
        jp_style="Regular",
        eng_style="Italic",
        merged_style="Italic",
        suffix=SUFFIX_KRYPTON,
        italic=True,
        jp_font_base=JP_FONT_KRYPTON
    )
    # Bold Italic スタイルを生成する
    generate_font(
        jp_style="Bold",
        eng_style="BoldItalic",
        merged_style="BoldItalic",
        suffix=SUFFIX_KRYPTON,
        italic=True,
        jp_font_base=JP_FONT_KRYPTON
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
        elif arg == "--jpdoc":
            options["jpdoc"] = True
        else:
            options["unknown-option"] = True
            return


def generate_font(jp_style, eng_style, merged_style, suffix, italic=False, jp_font_base=JP_FONT):
    print(f"=== Generate {suffix} {merged_style} ===")

    # 合成するフォントを開く
    jp_font, eng_font = open_fonts(jp_style, f"{suffix}-{eng_style}", jp_font_base, suffix)

    # fonttools merge エラー対処
    jp_font = fonttools_merge_error_workaround(jp_font)

    # フォントのEMを1000に変換する
    em_1000(jp_font)
    em_1000(eng_font)

    # いくつかのグリフ形状に調整を加える
    adjust_some_glyph(jp_font, eng_font)

    # 日本語文書に頻出する記号を英語フォントから削除する
    if options.get("jpdoc"):
        remove_jpdoc_symbols(jp_font, eng_font)

    # 重複するグリフを削除する
    delete_duplicate_glyphs(jp_font, eng_font)

    # Radonの場合は日本語フォントを少し斜めにする
    if suffix == SUFFIX_RADON:
        make_italic_radon(jp_font)

    # 日本語グリフの斜体を生成する
    if italic:
        transform_italic_glyphs(jp_font)

    # スラッシュ付きゼロ
    if options.get("slashed-zero"):
        slashed_zero(eng_font)

    # eng_fontを半角幅(600)にする
    width_600(eng_font)

    # jp_fontで半角幅(500)のグリフの幅を3:5になるよう調整する
    width_600_or_1000(jp_font)

    # 3:5幅版との差分を調整する
    if options.get("half-width"):
        # 1:2 幅にする
        transform_half_width(jp_font, eng_font)

    # GSUBテーブルを削除する (ひらがな等の全角文字が含まれる行でリガチャが解除される対策)
    remove_lookups(jp_font)

    # 全角スペースを可視化する
    if not options.get("invisible-zenkaku-space"):
        visualize_zenkaku_space(jp_font, eng_font)

    # オプション毎の修飾子を追加する
    variant = HALF_WIDTH_STR if options.get("half-width") else ""
    variant += (
        INVISIBLE_ZENKAKU_SPACE_STR if options.get("invisible-zenkaku-space") else ""
    )
    variant += JPDOC_STR if options.get("jpdoc") else ""
    # variant += SLASHED_ZERO_STR if options.get("slashed-zero") else ""

    # base fontがBIZUDのときだけ情報を入れる
    jp_base = "BIZUD" if jp_font_base == JP_FONT_BIZUD else ""

    # メタデータを編集する
    edit_meta_data(eng_font, merged_style, variant, suffix, jp_base)
    edit_meta_data(jp_font, merged_style, variant, suffix, jp_base)

    # ttfファイルに保存
    eng_font.generate(
        f"{BUILD_FONTS_DIR}/{FONTFORGE_PREFIX}{FONT_NAME}{suffix}{jp_base}{variant}-{merged_style}-eng.ttf"
    )
    jp_font.generate(
        f"{BUILD_FONTS_DIR}/{FONTFORGE_PREFIX}{FONT_NAME}{suffix}{jp_base}{variant}-{merged_style}-jp.ttf"
    )

    # ttfを閉じる
    jp_font.close()
    eng_font.close()


def open_fonts(jp_style: str, eng_style: str, jp_font_base: str, suffix: str = ""):
    """フォントを開く"""
    jp_font = fontforge.open(f"{SOURCE_FONTS_DIR}/{jp_font_base}{jp_style}.ttf")
    eng_font = fontforge.open(f"{SOURCE_FONTS_DIR}/{ENG_FONT}{eng_style}.otf")

    if suffix == SUFFIX_RADON:
        # 足りないグラフをIBM Plex Sans JPで補う
        if jp_style == "Medium":
            jp_font.mergeFonts(fontforge.open(f"{SOURCE_FONTS_DIR}/{JP_FONT}Text.ttf"))
        elif jp_style == "Bold":
            jp_font.mergeFonts(fontforge.open(f"{SOURCE_FONTS_DIR}/{JP_FONT}Bold.ttf"))
    elif suffix == SUFFIX_KRYPTON:
        # 足りないグラフをIBM Plex Sans JPで補う
        if jp_style == "Regular":
            jp_font.mergeFonts(fontforge.open(f"{SOURCE_FONTS_DIR}/{JP_FONT}Text.ttf"))
        elif jp_style == "Bold":
            jp_font.mergeFonts(fontforge.open(f"{SOURCE_FONTS_DIR}/{JP_FONT}Bold.ttf"))

    # フォント参照を解除する
    jp_font.unlinkReferences()
    eng_font.unlinkReferences()

    return jp_font, eng_font


def fonttools_merge_error_workaround(jp_font):
    # fonttools merge エラー対処
    # "Have non-identical duplicates to resolve for 'IBM Plex Sans JP Text' but no GSUB. Are duplicates intended?"
    font_path = jp_font.path
    if "IBMPlexSansJP" in font_path:
        for glyph_name in [
            "uni02CA",
            "endash",
            "uni0336",
        ]:
            # Alternate Unicodeになっているグリフをコピーする
            glyph = jp_font[glyph_name]
            encoding = glyph.encoding
            altuni = glyph.altuni
            if altuni is not None:
                glyph.altuni = None
                copy_target_glyph = jp_font.createChar(encoding)
                copy_target_glyph.clear()
                copy_target_glyph.width = glyph.width
                copy_target_glyph.addReference(glyph.glyphname)
            # グリフを削除する
            jp_font.removeGlyph(glyph_name)
        # エンコーディングを整理するため、開き直す
        jp_font.generate(
            f"{BUILD_FONTS_DIR}/{FONTFORGE_PREFIX}{FONT_NAME}_temp_jp_font.ttf"
        )
        jp_font.close()
        return fontforge.open(
            f"{BUILD_FONTS_DIR}/{FONTFORGE_PREFIX}{FONT_NAME}_temp_jp_font.ttf"
        )
    else:
        return jp_font


def adjust_some_glyph(jp_font, eng_font):
    """いくつかのグリフ形状に調整を加える"""
    # アンダースコアが隣接すると繋がっているように見えるため短くする
    underscore = eng_font[0x005F]
    underscore_before_width = underscore.width
    underscore.transform(psMat.scale(0.77, 1))
    underscore.transform(
        psMat.translate((underscore_before_width - underscore.width) / 2, 0)
    )
    underscore.width = underscore_before_width
    # 全角括弧の開きを広くする
    full_width = jp_font[0x3042].width
    for glyph_name in [0xFF08, 0xFF3B, 0xFF5B]:
        glyph = jp_font[glyph_name]
        glyph.transform(psMat.translate(-180, 0))
        glyph.width = full_width
    for glyph_name in [0xFF09, 0xFF3D, 0xFF5D]:
        glyph = jp_font[glyph_name]
        glyph.transform(psMat.translate(180, 0))
        glyph.width = full_width
    # LEFT SINGLE QUOTATION MARK (U+2018) ～ DOUBLE LOW-9 QUOTATION MARK (U+201E) の幅を全角幅にする
    for glyph in jp_font.selection.select(
        ("ranges", "unicode"), 0x2018, 0x201E
    ).byGlyphs:
        glyph.transform(psMat.translate((full_width - glyph.width) / 2, 0))
        glyph.width = full_width
    jp_font.selection.none()


def make_italic_radon(jp_font):
    # 斜体の傾き
    ITALIC_SLOPE = 4
    # 全グリフを斜体に変換
    for glyph in jp_font.glyphs():
        if glyph.isWorthOutputting():
            glyph.transform(psMat.skew(ITALIC_SLOPE * math.pi / 180))


def em_1000(font):
    """フォントのEMを1000に変換する"""
    em_size = EM_ASCENT + EM_DESCENT
    font.em = em_size


def clear_glyph_range(font, start: int, end: int):
    """グリフを削除する"""
    for i in range(start, end + 1):
        for glyph in font.selection.select(("ranges", None), i).byGlyphs:
            glyph.clear()
    font.selection.none()


def delete_duplicate_glyphs(jp_font, eng_font):
    """jp_fontとeng_fontのグリフを比較し、重複するグリフを削除する"""

    eng_font.selection.none()
    jp_font.selection.none()

    for glyph in jp_font.glyphs():
        try:
            if glyph.isWorthOutputting() and glyph.unicode > 0:
                eng_font.selection.select(("more", "unicode"), glyph.unicode)
        except ValueError:
            # Encoding is out of range のときは継続する
            continue
    for glyph in eng_font.selection.byGlyphs:
        # if glyph.isWorthOutputting():
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


def remove_jpdoc_symbols(jp_font, eng_font):
    """日本語文書に頻出する記号を削除する"""
    eng_font.selection.none()
    # § (U+00A7)
    eng_font.selection.select(("more", "unicode"), 0x00A7)
    # ± (U+00B1)
    eng_font.selection.select(("more", "unicode"), 0x00B1)
    # ¶ (U+00B6)
    eng_font.selection.select(("more", "unicode"), 0x00B6)
    # ÷ (U+00F7)
    eng_font.selection.select(("more", "unicode"), 0x00F7)
    # × (U+00D7)
    eng_font.selection.select(("more", "unicode"), 0x00D7)
    # ⇒ (U+21D2)
    eng_font.selection.select(("more", "unicode"), 0x21D2)
    # ⇔ (U+21D4)
    eng_font.selection.select(("more", "unicode"), 0x21D4)
    # ■-□ (U+25A0-U+25A1)
    eng_font.selection.select(("more", "ranges"), 0x25A0, 0x25A1)
    # ▲-△ (U+25B2-U+25B3)
    eng_font.selection.select(("more", "ranges"), 0x25A0, 0x25B3)
    # ▼-▽ (U+25BC-U+25BD)
    eng_font.selection.select(("more", "ranges"), 0x25BC, 0x25BD)
    # ◆-◇ (U+25C6-U+25C7)
    eng_font.selection.select(("more", "ranges"), 0x25C6, 0x25C7)
    # ○ (U+25CB)
    eng_font.selection.select(("more", "unicode"), 0x25CB)
    # ◎-● (U+25CE-U+25CF)
    eng_font.selection.select(("more", "ranges"), 0x25CE, 0x25CF)
    # ◥ (U+25E5)
    eng_font.selection.select(("more", "unicode"), 0x25E5)
    # ◯ (U+25EF)
    eng_font.selection.select(("more", "unicode"), 0x25EF)
    # √ (U+221A)
    eng_font.selection.select(("more", "unicode"), 0x221A)
    # ∞ (U+221E)
    eng_font.selection.select(("more", "unicode"), 0x221E)
    # ‐ (U+2010)
    eng_font.selection.select(("more", "unicode"), 0x2010)
    # ‘-‚ (U+2018-U+201A)
    eng_font.selection.select(("more", "ranges"), 0x2018, 0x201A)
    # “-„ (U+201C-U+201E)
    eng_font.selection.select(("more", "ranges"), 0x201C, 0x201E)
    # †-‡ (U+2020-U+2021)
    eng_font.selection.select(("more", "ranges"), 0x2020, 0x2021)
    # … (U+2026)
    eng_font.selection.select(("more", "unicode"), 0x2026)
    # ‰ (U+2030)
    eng_font.selection.select(("more", "unicode"), 0x2030)
    # ←-↓ (U+2190-U+2193)
    eng_font.selection.select(("more", "ranges"), 0x2190, 0x2193)
    # ∀ (U+2200)
    eng_font.selection.select(("more", "unicode"), 0x2200)
    # ∂-∃ (U+2202-U+2203)
    eng_font.selection.select(("more", "ranges"), 0x2202, 0x2203)
    # ∈ (U+2208)
    eng_font.selection.select(("more", "unicode"), 0x2208)
    # ∋ (U+220B)
    eng_font.selection.select(("more", "unicode"), 0x220B)
    # ∑ (U+2211)
    eng_font.selection.select(("more", "unicode"), 0x2211)
    # ∥ (U+2225)
    eng_font.selection.select(("more", "unicode"), 0x2225)
    # ∧-∬ (U+2227-U+222C)
    eng_font.selection.select(("more", "ranges"), 0x2227, 0x222C)
    # ≠-≡ (U+2260-U+2261)
    eng_font.selection.select(("more", "ranges"), 0x2260, 0x2261)
    # ⊂-⊃ (U+2282-U+2283)
    eng_font.selection.select(("more", "ranges"), 0x2282, 0x2283)
    # ⊆-⊇ (U+2286-U+2287)
    eng_font.selection.select(("more", "ranges"), 0x2286, 0x2287)
    # ─-╿ (Box Drawing) (U+2500-U+257F)
    eng_font.selection.select(("more", "ranges"), 0x2500, 0x257F)
    for glyph in eng_font.selection.byGlyphs:
        if glyph.isWorthOutputting():
            glyph.clear()
    eng_font.selection.none()


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
        # 600の場合はそのまま


def width_600(eng_font):
    """英語フォントを半角幅になるように変換する"""
    before_width = eng_font[0x0030].width
    x_scale = 600 / before_width
    for glyph in eng_font.glyphs():
        if glyph.width > 0:
            # 縮小してから幅を設定
            glyph.transform(psMat.scale(x_scale, 1))
            glyph.width = 600


def transform_half_width(jp_font, eng_font):
    """1:2幅になるように変換する。既に3:5幅になっていることを前提とする。"""
    before_width_eng = eng_font[0x0030].width
    after_width_eng = HALF_WIDTH_12
    # グリフそのものは550幅相当で縮小し、最終的に HALF_WIDTH_12 の幅を設定する
    x_scale = 550 / before_width_eng
    for glyph in eng_font.glyphs():
        if glyph.width > 0:
            # 縮小
            glyph.transform(psMat.scale(x_scale, 1))
            # 幅を設定
            glyph.transform(psMat.translate((after_width_eng - glyph.width) / 2, 0))
            glyph.width = after_width_eng

    for glyph in jp_font.glyphs():
        if glyph.width == 600:
            # 英数字グリフと同じ幅にする
            glyph.transform(psMat.translate((after_width_eng - glyph.width) / 2, 0))
            glyph.width = after_width_eng
        elif glyph.width == 1000:
            # 全角は after_width_eng の倍の幅にする
            glyph.transform(psMat.translate((after_width_eng * 2 - glyph.width) / 2, 0))
            glyph.width = after_width_eng * 2


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


def edit_meta_data(font, weight: str, variant: str, suffix: str, jp_base: str):
    """フォント内のメタデータを編集する"""
    font.ascent = EM_ASCENT
    font.descent = EM_DESCENT
    font.os2_typoascent = EM_ASCENT
    font.os2_typodescent = -EM_DESCENT

    ascent_offset = 80
    descent_offset = 160
    if HALF_WIDTH_STR in variant:
        ascent_offset = 60
        descent_offset = 140

    font.hhea_ascent = EM_ASCENT + ascent_offset
    font.hhea_descent = -(EM_DESCENT + descent_offset)
    font.os2_winascent = EM_ASCENT + ascent_offset
    font.os2_windescent = EM_DESCENT + descent_offset
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
    # jp_baseは空文字のことがあるので後ろのスペースを詰める
    font.familyname = f"{FONT_NAME} {suffix} {jp_base}{variant}".strip()
    font.fontname = f"{FONT_NAME}{suffix}{jp_base}{variant}-{weight}"
    font.fullname = f"{FONT_NAME} {suffix} {jp_base}{variant}".strip() + f" {weight}"
    font.os2_vendor = VENDER_NAME
    font.copyright = COPYRIGHT


if __name__ == "__main__":
    main()
