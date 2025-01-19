#!/usr/bin/env bash

# ini から VERSION を取得
version=$(grep "VERSION" build.ini | cut -d "=" -f 2 | xargs)

# スクリプトファイルがある場所に移動する
cd "$(dirname "$0")"

# 各ファイルを置くフォルダを作成
mkdir -p "./release_files/"

# ビルドフォルダを削除
rm -rf ./build

# 並列処理
option=(
  "--nerd-font"
  "--half-width --nerd-font"
  " "
  "--half-width"
  "--jpdoc"
  "--half-width --jpdoc"
)
output_folder=(
  "NF-"
  "HWNF-"
  "-"
  "HW-"
  "JPDOC-"
  "HWJPDOC-"
)

# 配列を並列処理しやすい形式に変換
function run_build() {
  local option="$1"
  local output_prefix="$2"
  echo "fontforge script start. option: \"$option\""
  python ./fontforge_script.py --do-not-delete-build-dir $option &&
    echo "fonttools script start. option: \"$output_prefix\"" &&
    python fonttools_script.py "$output_prefix"
}
export -f run_build

# parallelコマンドで並列実行
parallel -j -1 --progress --link run_build ::: "${option[@]}" ::: "${output_folder[@]}"

# ファイル移動
declare -A move_file_src_dest=(
  ["MoralerspaceNeon-*.ttf"]="Moralerspace_$version"
  ["MoralerspaceArgon-*.ttf"]="Moralerspace_$version"
  ["MoralerspaceXenon-*.ttf"]="Moralerspace_$version"
  ["MoralerspaceRadon-*.ttf"]="Moralerspace_$version"
  ["MoralerspaceKrypton-*.ttf"]="Moralerspace_$version"

  ["MoralerspaceNeonHW-*.ttf"]="MoralerspaceHW_$version"
  ["MoralerspaceArgonHW-*.ttf"]="MoralerspaceHW_$version"
  ["MoralerspaceXenonHW-*.ttf"]="MoralerspaceHW_$version"
  ["MoralerspaceRadonHW-*.ttf"]="MoralerspaceHW_$version"
  ["MoralerspaceKryptonHW-*.ttf"]="MoralerspaceHW_$version"

  ["MoralerspaceNeonJPDOC-*.ttf"]="MoralerspaceJPDOC_$version"
  ["MoralerspaceArgonJPDOC-*.ttf"]="MoralerspaceJPDOC_$version"
  ["MoralerspaceXenonJPDOC-*.ttf"]="MoralerspaceJPDOC_$version"
  ["MoralerspaceRadonJPDOC-*.ttf"]="MoralerspaceJPDOC_$version"
  ["MoralerspaceKryptonJPDOC-*.ttf"]="MoralerspaceJPDOC_$version"

  ["MoralerspaceNeonHWJPDOC-*.ttf"]="MoralerspaceHWJPDOC_$version"
  ["MoralerspaceArgonHWJPDOC-*.ttf"]="MoralerspaceHWJPDOC_$version"
  ["MoralerspaceXenonHWJPDOC-*.ttf"]="MoralerspaceHWJPDOC_$version"
  ["MoralerspaceRadonHWJPDOC-*.ttf"]="MoralerspaceHWJPDOC_$version"
  ["MoralerspaceKryptonHWJPDOC-*.ttf"]="MoralerspaceHWJPDOC_$version"

  ["MoralerspaceNeonNF-*.ttf"]="MoralerspaceNF_$version"
  ["MoralerspaceArgonNF-*.ttf"]="MoralerspaceNF_$version"
  ["MoralerspaceXenonNF-*.ttf"]="MoralerspaceNF_$version"
  ["MoralerspaceRadonNF-*.ttf"]="MoralerspaceNF_$version"
  ["MoralerspaceKryptonNF-*.ttf"]="MoralerspaceNF_$version"

  ["MoralerspaceNeonHWNF-*.ttf"]="MoralerspaceHWNF_$version"
  ["MoralerspaceArgonHWNF-*.ttf"]="MoralerspaceHWNF_$version"
  ["MoralerspaceXenonHWNF-*.ttf"]="MoralerspaceHWNF_$version"
  ["MoralerspaceRadonHWNF-*.ttf"]="MoralerspaceHWNF_$version"
  ["MoralerspaceKryptonHWNF-*.ttf"]="MoralerspaceHWNF_$version"
)

timestamp=$(date +%Y%m%d%H%M%S)
move_dir="./release_files/build_$timestamp"

for ttf in "${!move_file_src_dest[@]}"; do
  folder_path="$move_dir/${move_file_src_dest[$ttf]}"
  mkdir -p "$folder_path"
  find "./build/" -name "$ttf" -exec mv -t "$folder_path" {} \;
done

echo "Finish build."
