# Moralerspace

Moralerspace は、欧文フォント [Monaspace](https://github.com/githubnext/monaspace) と日本語フォント [IBM Plex Sans JP](https://github.com/IBM/plex) などを合成したプログラミング向けフォントです。

```
  ∧＿＿∧
 (  ・∀・) マターリしようよ
 (       )
 ｜  ｜  ｜
 (＿＿)＿_)
```

## インストール

リリースページより ttf ファイルをダウンロードし、各 OS ごとの方法でインストールしてください。

[🆕 **ダウンロードはこちら**](https://github.com/yuru7/moralerspace/releases/latest)

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

## バリエーション


| 種類                                | 説明                                                                                    | 命名パターン                       |
| --------------------------------- | ------------------------------------------------------------------------------------- | ---------------------------- |
| 通常版 (半角3:全角5 幅)                   | 半角5文字と全角3文字が同等の幅になっているバリエーション。半角英数字が合成元オリジナルのサイズで広く表示されるため読みやすい。                          | `Moralerspace*-*.ttf`        |
| 半角1:全角2 幅                         | 半角2文字と全角1文字が同等の幅になっているバリエーション。半角幅と全角幅を倍の幅で表示させたい方はこちら。                                   | `Moralerspace*HW-*.ttf`      |
| 通常版 (半角3:全角5 幅) & 日本語文書で頻出する記号が全角 | 通常版に対し、日本語文書で頻出する記号類 ( `← ↓ ↑ → □ ■ …` など) を全角幅にしたバリエーション。                      | `Moralerspace*JPDOC-*.ttf`   |
| 半角1:全角2 幅 & 日本語文書で頻出する記号が全角       | 半角 1:2 幅版に対し、日本語文書で頻出する記号類 ( `← ↓ ↑ → □ ■ …` など) を全角幅にしたバリエーション。                | `Moralerspace*HWJPDOC-*.ttf` |
| 通常版 (半角3:全角5 幅) + Nerd Fonts      | 通常版に対し、ターミナル表示をお洒落にする [Nerd Fonts](https://www.nerdfonts.com/) を追加で合成したバリエーション。       | `Moralerspace*NF-*.ttf`      |
| 半角1:全角2 幅 + Nerd Fonts            | 半角 1:2 幅版に対し、ターミナル表示をお洒落にする [Nerd Fonts](https://www.nerdfonts.com/) を追加で合成したバリエーション。 | `Moralerspace*HWNF-*.ttf`    |


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
