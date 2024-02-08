import configparser

import fontforge

settings = configparser.ConfigParser()
settings.read("build.ini", encoding="utf-8")
SOURCE_FONTS_DIR = settings.get("DEFAULT", "SOURCE_FONTS_DIR")


def main():
    radon_jp_font = fontforge.open(f"{SOURCE_FONTS_DIR}/KiwiMaru-Medium.ttf")
    krypton_jp_font = fontforge.open(f"{SOURCE_FONTS_DIR}/Stick-Regular.ttf")

    print("***** Radon用の太字フォントを作成します *****")

    for i, glyph in enumerate(radon_jp_font.glyphs()):
        if i % 100 == 0:
            print(f"{i}文字目を処理中")
        if glyph.isWorthOutputting():
            glyph.stroke("circular", 35, removeinternal=True, removeoverlap="none")
            glyph.removeOverlap()

    print("***** Krypton用の太字フォントを作成します *****")

    for i, glyph in enumerate(krypton_jp_font.glyphs()):
        if i % 100 == 0:
            print(f"{i}文字目を処理中")
        if glyph.isWorthOutputting():
            glyph.stroke("circular", 38, removeinternal=True, removeoverlap="none")
            glyph.removeOverlap()

    # ttfファイルを保存
    radon_jp_font.generate(f"{SOURCE_FONTS_DIR}/KiwiMaru-Bold.ttf")
    krypton_jp_font.generate(f"{SOURCE_FONTS_DIR}/Stick-Bold.ttf")


if __name__ == "__main__":
    main()
