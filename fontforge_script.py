#!fontforge --lang=py -script

# 2つのフォントを合成する

import configparser
import math
import os
import shutil
import sys
import uuid
from decimal import ROUND_HALF_UP, Decimal

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
ENG_FONT = settings.get("DEFAULT", "ENG_FONT")
HACK_FONT = settings.get("DEFAULT", "HACK_FONT")
SOURCE_FONTS_DIR = settings.get("DEFAULT", "SOURCE_FONTS_DIR")
BUILD_FONTS_DIR = settings.get("DEFAULT", "BUILD_FONTS_DIR")
VENDER_NAME = settings.get("DEFAULT", "VENDER_NAME")
FONTFORGE_PREFIX = settings.get("DEFAULT", "FONTFORGE_PREFIX")
IDEOGRAPHIC_SPACE = settings.get("DEFAULT", "IDEOGRAPHIC_SPACE")
HALF_WIDTH_STR = settings.get("DEFAULT", "HALF_WIDTH_STR")
INVISIBLE_ZENKAKU_SPACE_STR = settings.get("DEFAULT", "INVISIBLE_ZENKAKU_SPACE_STR")
JPDOC_STR = settings.get("DEFAULT", "JPDOC_STR")
NERD_FONTS_STR = settings.get("DEFAULT", "NERD_FONTS_STR")
EM_ASCENT = int(settings.get("DEFAULT", "EM_ASCENT"))
EM_DESCENT = int(settings.get("DEFAULT", "EM_DESCENT"))
OS2_ASCENT = int(settings.get("DEFAULT", "OS2_ASCENT"))
OS2_DESCENT = int(settings.get("DEFAULT", "OS2_DESCENT"))
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

[Hack]
Copyright 2018 Source Foundry Authors https://github.com/source-foundry/Hack

[Nerd Fonts]
Copyright (c) 2014, Ryan L McIntyre https://ryanlmcintyre.com

[Moralerspace]
Copyright 2022 Yuko Otawara
"""  # noqa: E501

options = {}
nerd_font = None


def main():
    # オプション判定
    get_options()
    if options.get("unknown-option"):
        usage()
        return

    # buildディレクトリを作成する
    if os.path.exists(BUILD_FONTS_DIR) and not options.get("do-not-delete-build-dir"):
        shutil.rmtree(BUILD_FONTS_DIR)
        os.mkdir(BUILD_FONTS_DIR)
    if not os.path.exists(BUILD_FONTS_DIR):
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

    # デバッグモードの場合はRegularのみ生成する
    if options.get("debug"):
        return

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


def generate_argon():
    """Argon系統を生成する"""
    # Regular スタイルを生成する
    generate_font(
        jp_style="Text",
        eng_style="Regular",
        merged_style="Regular",
        suffix=SUFFIX_ARGON,
    )

    # デバッグモードの場合はRegularのみ生成する
    if options.get("debug"):
        return

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

    # デバッグモードの場合はRegularのみ生成する
    if options.get("debug"):
        return

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
    )

    # デバッグモードの場合はRegularのみ生成する
    if options.get("debug"):
        return

    # Bold スタイルを生成する
    generate_font(
        jp_style="Bold",
        eng_style="Bold",
        merged_style="Bold",
        suffix=SUFFIX_RADON,
    )

    # Regular Italic スタイルを生成する
    generate_font(
        jp_style="Medium",
        eng_style="Italic",
        merged_style="Italic",
        suffix=SUFFIX_RADON,
        italic=True,
    )
    # Bold Italic スタイルを生成する
    # generate_font(
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
        jp_style="Regular",
        eng_style="Regular",
        merged_style="Regular",
        suffix=SUFFIX_KRYPTON,
    )

    # デバッグモードの場合はRegularのみ生成する
    if options.get("debug"):
        return

    # Bold スタイルを生成する
    generate_font(
        jp_style="Bold",
        eng_style="Bold",
        merged_style="Bold",
        suffix=SUFFIX_KRYPTON,
    )

    # Regular Italic スタイルを生成する
    generate_font(
        jp_style="Regular",
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
        f"Usage: {sys.argv[0]} " "[--invisible-zenkaku-space] [--half-width] [--jpdoc]"
    )


def get_options():
    """オプションを取得する"""

    global options

    # オプションなしの場合は何もしない
    if len(sys.argv) == 1:
        return

    for arg in sys.argv[1:]:
        # オプション判定
        if arg == "--do-not-delete-build-dir":
            options["do-not-delete-build-dir"] = True
        elif arg == "--invisible-zenkaku-space":
            options["invisible-zenkaku-space"] = True
        elif arg == "--half-width":
            options["half-width"] = True
        elif arg == "--jpdoc":
            options["jpdoc"] = True
        elif arg == "--debug":
            options["debug"] = True
        else:
            options["unknown-option"] = True
            return


def generate_font(jp_style, eng_style, merged_style, suffix, italic=False):
    print(f"=== Generate {suffix} {merged_style} ===")

    # 合成するフォントを開く
    jp_font, eng_font = open_fonts(jp_style, eng_style, suffix)

    # フォントのEMを1000に変換する
    # jp_font は既に1000なので eng_font のみ変換する
    em_1000(eng_font)

    # Hack フォントをマージする
    merge_hack(eng_font, eng_style)

    # 日本語文書に頻出する記号を英語フォントから削除する
    if options.get("jpdoc"):
        remove_jpdoc_symbols(eng_font)

    # 重複するグリフを削除する
    delete_duplicate_glyphs(jp_font, eng_font)

    # いくつかのグリフ形状に調整を加える
    adjust_some_glyph(jp_font, eng_font)

    # Radonの場合は日本語フォントを少し斜めにする
    if suffix == SUFFIX_RADON:
        make_italic_radon(jp_font)

    # 日本語グリフの斜体を生成する
    if italic:
        transform_italic_glyphs(jp_font)

    # eng_fontを半角幅(600)にする
    width_600(eng_font)

    # jp_fontで半角幅(500)のグリフの幅を3:5になるよう調整する
    width_600_or_1000(jp_font)

    # 3:5幅版との差分を調整する
    if options.get("half-width"):
        # 1:2 幅にする
        transform_half_width(jp_font, eng_font)
        # 規定の幅からはみ出したグリフサイズを縮小する
        down_scale_redundant_size_glyph(eng_font)

    # GSUBテーブルを削除する (ひらがな等の全角文字が含まれる行でリガチャが解除される対策)
    remove_lookups(jp_font)

    # 全角スペースを可視化する
    if not options.get("invisible-zenkaku-space"):
        visualize_zenkaku_space(jp_font)

    # Nerd Fontのグリフを追加する
    add_nerd_font_glyphs(jp_font, eng_font)

    # オプション毎の修飾子を追加する
    variant = HALF_WIDTH_STR if options.get("half-width") else ""
    variant += (
        INVISIBLE_ZENKAKU_SPACE_STR if options.get("invisible-zenkaku-space") else ""
    )
    variant += JPDOC_STR if options.get("jpdoc") else ""

    # macOSでのpostテーブルの使用性エラー対策
    # 重複するグリフ名を持つグリフをリネームする
    delete_glyphs_with_duplicate_glyph_names(eng_font)
    delete_glyphs_with_duplicate_glyph_names(jp_font)

    # メタデータを編集する
    cap_height = int(
        Decimal(str(eng_font[0x0048].boundingBox()[3])).quantize(
            Decimal("0"), ROUND_HALF_UP
        )
    )
    x_height = int(
        Decimal(str(eng_font[0x0078].boundingBox()[3])).quantize(
            Decimal("0"), ROUND_HALF_UP
        )
    )
    edit_meta_data(eng_font, merged_style, variant, suffix, cap_height, x_height)
    edit_meta_data(jp_font, merged_style, variant, suffix, cap_height, x_height)

    # ttfファイルに保存
    # なんらかフラグを立てるとGSUB, GPOSテーブルが削除されて後続の生成処理で影響が出るため注意
    eng_font.generate(
        f"{BUILD_FONTS_DIR}/{FONTFORGE_PREFIX}{FONT_NAME}{suffix}{variant}-{merged_style}-eng.ttf",
    )
    jp_font.generate(
        f"{BUILD_FONTS_DIR}/{FONTFORGE_PREFIX}{FONT_NAME}{suffix}{variant}-{merged_style}-jp.ttf",
    )

    # ttfを閉じる
    jp_font.close()
    eng_font.close()


def open_fonts(jp_style: str, eng_style: str, suffix: str = ""):
    """フォントを開く"""
    suffix_eng_style = f"{suffix}-{eng_style}"
    if suffix == SUFFIX_RADON:
        jp_font = fontforge.open(
            f"{SOURCE_FONTS_DIR}/{JP_FONT_RADON}{jp_style}_dehint.ttf"
        )
        eng_font = fontforge.open(
            f"{SOURCE_FONTS_DIR}/{ENG_FONT}{suffix_eng_style}.otf"
        )
        # 足りないグラフをIBM Plex Sans JPで補う
        if jp_style == "Medium":
            jp_font.mergeFonts(
                fontforge.open(f"{SOURCE_FONTS_DIR}/{JP_FONT}Medium.ttf")
            )
        elif jp_style == "Bold":
            jp_font.mergeFonts(fontforge.open(f"{SOURCE_FONTS_DIR}/{JP_FONT}Bold.ttf"))
    elif suffix == SUFFIX_KRYPTON:
        jp_font = fontforge.open(f"{SOURCE_FONTS_DIR}/{JP_FONT_KRYPTON}{jp_style}.ttf")
        eng_font = fontforge.open(
            f"{SOURCE_FONTS_DIR}/{ENG_FONT}{suffix_eng_style}.otf"
        )
        # 足りないグラフをIBM Plex Sans JPで補う
        if jp_style == "Regular":
            jp_font.mergeFonts(fontforge.open(f"{SOURCE_FONTS_DIR}/{JP_FONT}Text.ttf"))
        elif jp_style == "Bold":
            jp_font.mergeFonts(fontforge.open(f"{SOURCE_FONTS_DIR}/{JP_FONT}Bold.ttf"))
    else:
        jp_font = fontforge.open(f"{SOURCE_FONTS_DIR}/{JP_FONT}{jp_style}.ttf")
        eng_font = fontforge.open(
            f"{SOURCE_FONTS_DIR}/{ENG_FONT}{suffix_eng_style}.otf"
        )

    # fonttools merge エラー対処
    jp_font = altuni_to_entity(jp_font)

    # フォント参照を解除する
    for glyph in jp_font.glyphs():
        if glyph.isWorthOutputting():
            jp_font.selection.select(("more", None), glyph)
    jp_font.unlinkReferences()
    for glyph in eng_font.glyphs():
        if glyph.isWorthOutputting():
            eng_font.selection.select(("more", None), glyph)
    eng_font.unlinkReferences()

    return jp_font, eng_font


def altuni_to_entity(jp_font):
    """Alternate Unicodeで透過的に参照して表示している箇所を実体のあるグリフに変換する"""
    for glyph in jp_font.glyphs():
        if glyph.altuni is not None:
            # 以下形式のタプルで返ってくる
            # (unicode-value, variation-selector, reserved-field)
            # 第3フィールドは常に0なので無視
            altunis = glyph.altuni

            # variation-selectorがなく (-1)、透過的にグリフを参照しているものは実体のグリフに変換する
            before_altuni = ""
            for altuni in altunis:
                # 直前のaltuniと同じ場合はスキップ
                if altuni[1] == -1 and before_altuni != ",".join(map(str, altuni)):
                    glyph.altuni = None
                    copy_target_unicode = altuni[0]
                    try:
                        copy_target_glyph = jp_font.createChar(
                            copy_target_unicode,
                            f"uni{hex(copy_target_unicode).replace('0x', '').upper()}copy",
                        )
                    except Exception:
                        copy_target_glyph = jp_font[copy_target_unicode]
                    copy_target_glyph.clear()
                    copy_target_glyph.width = glyph.width
                    # copy_target_glyph.addReference(glyph.glyphname)
                    jp_font.selection.select(glyph.glyphname)
                    jp_font.copy()
                    jp_font.selection.select(copy_target_glyph.glyphname)
                    jp_font.paste()
                before_altuni = ",".join(map(str, altuni))
    # エンコーディングの整理のため、開き直す
    font_path = f"{BUILD_FONTS_DIR}/{jp_font.fullname}_{uuid.uuid4()}.ttf"
    jp_font.generate(font_path)
    jp_font.close()
    reopen_jp_font = fontforge.open(font_path)
    # 一時ファイルを削除
    os.remove(font_path)
    return reopen_jp_font


def delete_glyphs_with_duplicate_glyph_names(font):
    """重複するグリフ名を持つグリフをリネームする"""
    glyph_name_set = set()
    for glyph in font.glyphs():
        if glyph.glyphname in glyph_name_set:
            glyph.glyphname = f"{glyph.glyphname}_{glyph.encoding}"
        else:
            glyph_name_set.add(glyph.glyphname)


def adjust_some_glyph(jp_font, eng_font):
    """いくつかのグリフ形状に調整を加える"""
    # アンダースコアが隣接すると繋がっているように見えるため短くする
    # 位置も少し上にずらす
    underscore = eng_font[0x005F]
    underscore_before_width = underscore.width
    underscore.transform(psMat.scale(0.91, 1))
    underscore.transform(
        psMat.translate((underscore_before_width - underscore.width) / 2, 60)
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
    for uni in range(0x2018, 0x201E + 1):
        try:
            glyph = jp_font[uni]
            glyph.transform(psMat.translate((full_width - glyph.width) / 2, 0))
            glyph.width = full_width
        except TypeError:
            # グリフが存在しない場合は継続する
            continue
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
    font.em = EM_ASCENT + EM_DESCENT


def delete_duplicate_glyphs(jp_font, eng_font):
    """jp_fontとeng_fontのグリフを比較し、重複するグリフを削除する"""

    eng_font.selection.none()
    jp_font.selection.none()

    for glyph in jp_font.glyphs("encoding"):
        try:
            if glyph.isWorthOutputting() and glyph.unicode > 0:
                eng_font.selection.select(("more", "unicode"), glyph.unicode)
        except ValueError:
            # Encoding is out of range のときは継続する
            continue
    for glyph in eng_font.selection.byGlyphs:
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


def remove_jpdoc_symbols(eng_font):
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
    # ∴-∵ (U+2234-U+2235)
    eng_font.selection.select(("more", "ranges"), 0x2234, 0x2235)
    # ∽ (U+223D)
    eng_font.selection.select(("more", "unicode"), 0x223D)
    # ≒ (U+2252)
    eng_font.selection.select(("more", "unicode"), 0x2252)
    # ≠-≡ (U+2260-U+2261)
    eng_font.selection.select(("more", "ranges"), 0x2260, 0x2261)
    # ≦-≧ (U+2266-U+2267)
    eng_font.selection.select(("more", "ranges"), 0x2266, 0x2267)
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
    mona_original_half_width = eng_font[0x0030].width
    after_width = 600
    x_scale = after_width / mona_original_half_width
    for glyph in eng_font.glyphs():
        if 0 < glyph.width < after_width:
            # after_width より幅が狭い場合は位置合わせしてから幅を設定
            glyph.transform(psMat.translate((after_width - glyph.width) / 2, 0))
            glyph.width = after_width
        elif after_width < glyph.width <= mona_original_half_width:
            # after_width より幅が広い、かつ元の半角幅より狭い場合は縮小してから幅を設定
            glyph.transform(psMat.scale(x_scale, 1))
            glyph.width = after_width
        elif mona_original_half_width < glyph.width:
            # after_width より幅が広い (おそらく全てリガチャ) の場合は600の倍数にする
            multiply_number = round(glyph.width / mona_original_half_width)
            glyph.transform(psMat.scale(x_scale, 1))
            glyph.width = after_width * multiply_number


def transform_half_width(jp_font, eng_font):
    """1:2幅になるように変換する。既に3:5幅になっていることを前提とする。"""
    before_width_eng = eng_font[0x0030].width
    after_width_eng = HALF_WIDTH_12
    # グリフそのものは550幅相当で縮小し、最終的に HALF_WIDTH_12 の幅を設定する
    x_scale = 550 / before_width_eng
    for glyph in eng_font.glyphs():
        if glyph.width > 0:
            # リガチャ考慮
            after_width_eng_multiply = after_width_eng * round(glyph.width / 600)
            # 縮小
            glyph.transform(psMat.scale(x_scale, 0.99))
            # 幅を設定
            glyph.transform(
                psMat.translate((after_width_eng_multiply - glyph.width) / 2, 0)
            )
            glyph.width = after_width_eng_multiply

    for glyph in jp_font.glyphs():
        if glyph.width == 600:
            # 英数字グリフと同じ幅にする
            glyph.transform(psMat.translate((after_width_eng - glyph.width) / 2, 0))
            glyph.width = after_width_eng
        elif glyph.width == 1000:
            # 全角は after_width_eng の倍の幅にする
            glyph.transform(psMat.translate((after_width_eng * 2 - glyph.width) / 2, 0))
            glyph.width = after_width_eng * 2


def down_scale_redundant_size_glyph(eng_font):
    """規定の幅からはみ出したグリフサイズを縮小する"""

    # 元々の x=0 の位置が縮小後、はみ出した場合の位置
    x_zero_pos_after_reduction = -10

    for glyph in eng_font.glyphs():
        bounding_x_min = glyph.boundingBox()[0]
        if (
            glyph.width > 0
            and bounding_x_min < 0
            and not (
                0x0020 <= glyph.unicode <= 0x02AF
            )  # latin 系のグリフ 0x0020 - 0x0192 は無視
            and not (
                0xE0B0 <= glyph.unicode <= 0xE0D4
            )  # Powerline系のグリフ 0xE0B0 - 0xE0D4 は無視
            and not (
                0x2500 <= glyph.unicode <= 0x257F
            )  # 罫線系のグリフ 0x2500 - 0x257F は無視
            and not (
                0x2591 <= glyph.unicode <= 0x2593
            )  # SHADE グリフ 0x2591 - 0x2593 は無視
        ):
            before_width = glyph.width
            if bounding_x_min > x_zero_pos_after_reduction:
                x_scale = 1 + (bounding_x_min * 2) / glyph.width
            else:
                # はみ出し幅が特定の値以上の場合は縮小率を固定する
                x_scale = 1 + (x_zero_pos_after_reduction * 2) / glyph.width
            glyph.transform(psMat.scale(x_scale, 1))
            glyph.transform(psMat.translate((before_width - glyph.width) / 2, 0))
            glyph.width = before_width


def visualize_zenkaku_space(jp_font):
    """全角スペースを可視化する"""
    # 全角スペースを差し替え
    glyph = jp_font[0x3000]
    width_to = glyph.width
    glyph.clear()
    jp_font.mergeFonts(fontforge.open(f"{SOURCE_FONTS_DIR}/{IDEOGRAPHIC_SPACE}"))
    # 幅を設定し位置調整
    jp_font.selection.select("U+3000")
    for glyph in jp_font.selection.byGlyphs:
        width_from = glyph.width
        glyph.transform(psMat.translate((width_to - width_from) / 2, 0))
        glyph.width = width_to
    jp_font.selection.none()


def merge_hack(eng_font, eng_style):
    """Hack フォントをマージする"""
    hack_font = fontforge.open(f"{SOURCE_FONTS_DIR}/{HACK_FONT}{eng_style}.ttf")
    hack_font.em = EM_ASCENT + EM_DESCENT
    # 既に英語フォント側に存在する場合はhackグリフは削除する
    for glyph in eng_font.glyphs():
        if glyph.unicode != -1:
            try:
                for g in hack_font.selection.select(
                    ("unicode", None), glyph.unicode
                ).byGlyphs:
                    g.clear()
            except Exception:
                pass
    # monaspace を EM 1000 にしたときの幅に合わせて調整
    half_width = 620
    for glyph in hack_font.glyphs():
        if glyph.width > 0:
            glyph.transform(psMat.translate((half_width - glyph.width) / 2, 0))
            glyph.width = half_width
    # Hack フォントをオブジェクトとして扱いたくないので、一旦ファイル保存して直接マージする
    font_path = f"{BUILD_FONTS_DIR}/tmp_hack_{uuid.uuid4()}.ttf"
    hack_font.generate(font_path)
    hack_font.close()

    # Box Drawing, Block Elements のマージのため、英語フォントから削除する
    eng_font.selection.none()
    for uni in range(0x2500, 0x259F + 1):
        try:
            eng_font.selection.select(("more", "unicode"), uni)
        except Exception:
            pass
    for glyph in eng_font.selection.byGlyphs:
        glyph.clear()

    eng_font.mergeFonts(font_path)
    os.remove(font_path)


def add_nerd_font_glyphs(jp_font, eng_font):
    """Nerd Fontのグリフを追加する"""
    global nerd_font
    # Nerd Fontのグリフを追加する
    if nerd_font is None:
        nerd_font = fontforge.open(
            f"{SOURCE_FONTS_DIR}/nerd-fonts/SymbolsNerdFont-Regular.ttf"
        )
        nerd_font.em = EM_ASCENT + EM_DESCENT
        glyph_names = set()
        for nerd_glyph in nerd_font.glyphs():
            nerd_glyph.glyphname = f"{nerd_glyph.glyphname}-nf"
            # postテーブルでのグリフ名重複対策
            # fonttools merge で合成した後、MacOSで `'post'テーブルの使用性` エラーが発生することへの対処
            if nerd_glyph.glyphname in glyph_names:
                nerd_glyph.glyphname = f"{nerd_glyph.glyphname}-{nerd_glyph.encoding}"
            glyph_names.add(nerd_glyph.glyphname)
            # 幅を調整する
            half_width = eng_font[0x0030].width
            # Powerline Symbols の調整
            if 0xE0B0 <= nerd_glyph.unicode <= 0xE0D4:
                # 位置と幅合わせ
                if nerd_glyph.width < half_width:
                    nerd_glyph.transform(
                        psMat.translate((half_width - nerd_glyph.width) / 2, 0)
                    )
                elif nerd_glyph.width > half_width:
                    nerd_glyph.transform(psMat.scale(half_width / nerd_glyph.width, 1))
                # グリフの高さ・位置を調整する
                nerd_glyph.transform(psMat.scale(1, 1.21))
                nerd_glyph.transform(psMat.translate(0, -24))
            elif nerd_glyph.width < 600:
                # 幅が狭いグリフは中央寄せとみなして調整する
                nerd_glyph.transform(
                    psMat.translate((half_width - nerd_glyph.width) / 2, 0)
                )
            # 幅を設定
            nerd_glyph.width = half_width
    # 日本語フォントにマージするため、既に存在する場合は削除する
    for nerd_glyph in nerd_font.glyphs():
        if nerd_glyph.unicode != -1:
            # 既に存在する場合は削除する
            try:
                jp_font[nerd_glyph.unicode].clear()
            except Exception:
                pass
            try:
                eng_font[nerd_glyph.unicode].clear()
            except Exception:
                pass
    jp_font.mergeFonts(nerd_font)


def edit_meta_data(
    font, weight: str, variant: str, suffix: str, cap_height: int, x_height: int
):
    """フォント内のメタデータを編集する"""
    font.ascent = EM_ASCENT
    font.descent = EM_DESCENT

    os2_ascent = OS2_ASCENT
    os2_descent = OS2_DESCENT

    font.os2_winascent = os2_ascent
    font.os2_windescent = os2_descent

    font.os2_typoascent = os2_ascent
    font.os2_typodescent = -os2_descent
    font.os2_typolinegap = 0

    font.hhea_ascent = os2_ascent
    font.hhea_descent = -os2_descent
    font.hhea_linegap = 0

    font.os2_xheight = x_height
    font.os2_capheight = cap_height

    # VSCode のターミナル上のボトム位置の表示で g, j などが見切れる問題への対処
    # 水平ベーステーブルを削除
    font.horizontalBaseline = None

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
