# Moralerspace

Moralerspace は、欧文フォント [Monaspace](https://github.com/githubnext/monaspace) と日本語フォント [IBM Plex Sans JP](https://github.com/IBM/plex) などを合成したプログラミング向けフォントです。

```
  ∧＿＿∧
 (  ・∀・) マターリしようよ
 (       )
 ｜  ｜  ｜
 (＿＿)＿_)
```

[🆕 **ダウンロード**](https://github.com/yuru7/moralerspace/releases)  
※「Assets」内の zip ファイルをダウンロードしてご利用ください。

> 💡 その他、公開中のプログラミングフォント
> - 日本語文字に源柔ゴシック、英数字部分に Hack を使った [**白源 (はくげん／HackGen)**](https://github.com/yuru7/HackGen)
> - 日本語文字に IBM Plex Sans JP、英数字部分に IBM Plex Mono を使った [**PlemolJP (プレモル ジェイピー)**](https://github.com/yuru7/PlemolJP)
> - 日本語文字にBIZ UDゴシック、英数字部分に JetBrains Mono を使った [**UDEV Gothic**](https://github.com/yuru7/udev-gothic)

## 特徴

以下のような特徴があります。

- Texture healing システムを搭載した、GitHub 製 [Monaspace](https://github.com/githubnext/monaspace) 由来の英数字
- 文字の懐が広く読みやすい IBM 製 [IBM Plex Sans JP](https://github.com/IBM/plex) 由来の日本語文字
    - Radon 系統には [キウイ丸 (Kiwi-Maru)](https://github.com/Kiwi-KawagotoKajiru/Kiwi-Maru) をベースに、足りないグリフを IBM Plex Sans JP で補完
    - Krypton 系統には [Stick](https://github.com/fontworks-fonts/Stick) をベースに、足りないグリフを IBM Plex Sans JP で補完
- 罫線素片などの一部半角記号は、 [Hack](https://github.com/source-foundry/Hack) より追加合成
- 文字幅比率が 半角3:全角5、ゆとりのある半角英数字
    - 半角1:全角2 幅のバリエーションもあり
- バグの原因になりがちな全角スペースが可視化される

![sample](https://github.com/yuru7/moralerspace/assets/13458509/21d90d22-0178-4c41-a28c-7b15b7b17ecf)

## ビルド

ビルドに使用するツール、ランタイム

- fontforge: `20230101` \[[Windows](https://fontforge.org/en-US/downloads/windows/)\] \[[Linux](https://fontforge.org/en-US/downloads/gnulinux/)\]
- Python: `>=3.8`

### Windows (PowerShell)

```sh
# 必要パッケージのインストール
pip install -r requirements.txt
# ビルド
& "C:\Program Files (x86)\FontForgeBuilds\bin\ffpython.exe" .\fontforge_script.py && python fonttools_script.py
```

### Linux

coming soon...

## ライセンス

SIL Open Font License, Version 1.1 が適用され、個人・商用問わず利用可能です。

ソースフォントのライセンスも同様に SIL Open Font License, Version 1.1 が適用されています。詳しくは `source_fonts` ディレクトリに含まれる LICENSE ファイルを参照してください。
