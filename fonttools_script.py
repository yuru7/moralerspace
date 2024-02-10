#!/bin/env python3

import configparser
import glob
import os
import xml.etree.ElementTree as ET
from pathlib import Path

import fontTools.ttx

# iniファイルを読み込む
settings = configparser.ConfigParser()
settings.read("build.ini", encoding="utf-8")

FONT_NAME = settings.get("DEFAULT", "FONT_NAME")
SUFFIX_NEON = settings.get("DEFAULT", "SUFFIX_NEON")
SUFFIX_ARGON = settings.get("DEFAULT", "SUFFIX_ARGON")
SUFFIX_XENON = settings.get("DEFAULT", "SUFFIX_XENON")
SUFFIX_RADON = settings.get("DEFAULT", "SUFFIX_RADON")
SUFFIX_KRYPTON = settings.get("DEFAULT", "SUFFIX_KRYPTON")
INPUT_PREFIX = settings.get("DEFAULT", "FONTFORGE_PREFIX")
OUTPUT_PREFIX = settings.get("DEFAULT", "FONTTOOLS_PREFIX")
BUILD_FONTS_DIR = settings.get("DEFAULT", "BUILD_FONTS_DIR")
HALF_WIDTH_STR = settings.get("DEFAULT", "HALF_WIDTH_STR")
HALF_WIDTH_12 = int(settings.get("DEFAULT", "HALF_WIDTH_12"))
FULL_WIDTH_35 = int(settings.get("DEFAULT", "FULL_WIDTH_35"))


def main():
    fix_font_tables(SUFFIX_NEON)
    fix_font_tables(SUFFIX_ARGON)
    fix_font_tables(SUFFIX_XENON)
    fix_font_tables(SUFFIX_RADON)
    fix_font_tables(SUFFIX_KRYPTON)

    # 一時ファイルを削除
    # スタイル部分はワイルドカードで指定
    for filename in glob.glob(f"{BUILD_FONTS_DIR}/{OUTPUT_PREFIX}{FONT_NAME}*"):
        os.remove(filename)
    for filename in glob.glob(f"{BUILD_FONTS_DIR}/{INPUT_PREFIX}{FONT_NAME}*"):
        os.remove(filename)


def fix_font_tables(suffix):
    """フォントテーブルを編集する"""

    # ファイルをパターンで指定
    filenames = glob.glob(f"{BUILD_FONTS_DIR}/{INPUT_PREFIX}{FONT_NAME}{suffix}*.ttf")
    # ファイルが見つからない or 複数見つかった場合はエラー
    if len(filenames) == 0:
        print(f"Error: {INPUT_PREFIX}{FONT_NAME}{suffix}*.ttf not found")
        return
    paths = [Path(f) for f in filenames]

    for path in paths:
        style = path.stem.split("-")[-1]
        variant = path.stem.split("-")[0].replace(
            f"{INPUT_PREFIX}{FONT_NAME}{suffix}", ""
        )

        output_name_base = f"{OUTPUT_PREFIX}{FONT_NAME}{suffix}{variant}-{style}"
        input_name_base = f"{INPUT_PREFIX}{FONT_NAME}{suffix}{variant}-{style}"
        completed_name_base = f"{FONT_NAME}{suffix}{variant}-{style}"

        # OS/2, post テーブルのみのttxファイルを出力
        xml = dump_ttx(input_name_base, output_name_base)
        # OS/2 テーブルを編集
        fix_os2_table(xml, style, flag_hw=HALF_WIDTH_STR in variant)
        # post テーブルを編集
        fix_post_table(xml)

        # ttxファイルを上書き保存
        xml.write(
            f"{BUILD_FONTS_DIR}/{OUTPUT_PREFIX}{FONT_NAME}{suffix}{variant}-{style}.ttx",
            encoding="utf-8",
            xml_declaration=True,
        )

        # ttxファイルをttfファイルに適用
        fontTools.ttx.main(
            [
                "-o",
                f"{BUILD_FONTS_DIR}/{output_name_base}_os2_post.ttf",
                "-m",
                f"{BUILD_FONTS_DIR}/{input_name_base}.ttf",
                f"{BUILD_FONTS_DIR}/{output_name_base}.ttx",
            ]
        )

        # ファイル名を変更
        os.rename(
            f"{BUILD_FONTS_DIR}/{output_name_base}_os2_post.ttf",
            f"{BUILD_FONTS_DIR}/{completed_name_base}.ttf",
        )


def dump_ttx(input_name_base, output_name_base) -> ET:
    """OS/2, post テーブルのみのttxファイルを出力"""
    fontTools.ttx.main(
        [
            "-t",
            "OS/2",
            "-t",
            "post",
            "-f",
            "-o",
            f"{BUILD_FONTS_DIR}/{output_name_base}.ttx",
            f"{BUILD_FONTS_DIR}/{input_name_base}.ttf",
        ]
    )

    return ET.parse(f"{BUILD_FONTS_DIR}/{output_name_base}.ttx")


def fix_os2_table(xml: ET, style: str, flag_hw: bool = False):
    """OS/2 テーブルを編集する"""
    # xAvgCharWidthを編集
    # タグ形式: <xAvgCharWidth value="1000"/>
    if flag_hw:
        x_avg_char_width = HALF_WIDTH_12
    else:
        x_avg_char_width = FULL_WIDTH_35
    for elem in xml.iter("xAvgCharWidth"):
        elem.set("value", str(x_avg_char_width))

    # fsSelectionを編集
    # タグ形式: <fsSelection value="00000000 11000000" />
    # スタイルに応じたビットを立てる
    if style == "Regular":
        fs_selection = "00000001 01000000"
    elif style == "Italic":
        fs_selection = "00000001 00000001"
    elif style == "Bold":
        fs_selection = "00000001 00100000"
    elif style == "BoldItalic":
        fs_selection = "00000001 00100001"

    if fs_selection:
        for elem in xml.iter("fsSelection"):
            elem.set("value", fs_selection)

    # panoseを編集
    # タグ形式:
    # <panose>
    #   <bFamilyType value="2" />
    #   <bSerifStyle value="11" />
    #   <bWeight value="6" />
    #   <bProportion value="9" />
    #   <bContrast value="6" />
    #   <bStrokeVariation value="3" />
    #   <bArmStyle value="0" />
    #   <bLetterForm value="2" />
    #   <bMidline value="0" />
    #   <bXHeight value="4" />
    # </panose>
    if style == "Regular" or style == "Italic":
        bWeight = 5
    else:
        bWeight = 8
    if flag_hw:
        panose = {
            "bFamilyType": 2,
            "bSerifStyle": 11,
            "bWeight": bWeight,
            "bProportion": 9,
            "bContrast": 2,
            "bStrokeVariation": 2,
            "bArmStyle": 3,
            "bLetterForm": 2,
            "bMidline": 2,
            "bXHeight": 7,
        }
    else:
        panose = {
            "bFamilyType": 2,
            "bSerifStyle": 11,
            "bWeight": bWeight,
            "bProportion": 3,
            "bContrast": 2,
            "bStrokeVariation": 2,
            "bArmStyle": 3,
            "bLetterForm": 2,
            "bMidline": 2,
            "bXHeight": 7,
        }

    for key, value in panose.items():
        for elem in xml.iter(key):
            elem.set("value", str(value))


def fix_post_table(xml: ET):
    """post テーブルを編集する"""
    # isFixedPitchを編集
    # タグ形式: <isFixedPitch value="0"/>
    is_fixed_pitch = 0
    for elem in xml.iter("isFixedPitch"):
        elem.set("value", str(is_fixed_pitch))


if __name__ == "__main__":
    main()
