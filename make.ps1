# ini から VERSION を取得
$ini = Get-Content .\build.ini
$version = ($ini | Select-String -Pattern "VERSION").ToString().Split("=")[1].Trim()

# スクリプトファイルがある場所に移動する
Set-Location -Path $PSScriptRoot
# 各ファイルを置くフォルダを作成
New-Item -ItemType Directory -Force -Path ".\release_files\"
# ビルドフォルダを削除
Remove-Item -Path .\build -Recurse -Force

$option_and_output_folder = @(
    @("", "-"), # ビルド 通常版
    @("--half-width", "HW-"), # ビルド 1:2幅版
    @("--jpdoc", "JPDOC-"), # ビルド JPDOC版
    @("--half-width --jpdoc", "HWJPDOC-") # ビルド 1:2幅 JPDOC版
)

$option_and_output_folder | Foreach-Object -ThrottleLimit 4 -Parallel {
    Write-Host "fontforge script start. option: `"$($_[0])`""
    Invoke-Expression "& `"C:\Program Files (x86)\FontForgeBuilds\bin\ffpython.exe`" .\fontforge_script.py --do-not-delete-build-dir $($_[0])" `
        && Write-Host "fonttools script start. option: `"$($_[1])`"" `
        && python fonttools_script.py $_[1]
}

$move_file_src_dest = @(
    @("MoralerspaceNeon-*.ttf", "Moralerspace_$version"),
    @("MoralerspaceArgon-*.ttf", "Moralerspace_$version"),
    @("MoralerspaceXenon-*.ttf", "Moralerspace_$version"),
    @("MoralerspaceRadon-*.ttf", "Moralerspace_$version"),
    @("MoralerspaceKrypton-*.ttf", "Moralerspace_$version"),

    @("MoralerspaceNeonHW-*.ttf", "MoralerspaceHW_$version"),
    @("MoralerspaceArgonHW-*.ttf", "MoralerspaceHW_$version"),
    @("MoralerspaceXenonHW-*.ttf", "MoralerspaceHW_$version"),
    @("MoralerspaceRadonHW-*.ttf", "MoralerspaceHW_$version"),
    @("MoralerspaceKryptonHW-*.ttf", "MoralerspaceHW_$version"),

    @("MoralerspaceNeonJPDOC-*.ttf", "MoralerspaceJPDOC_$version"),
    @("MoralerspaceArgonJPDOC-*.ttf", "MoralerspaceJPDOC_$version"),
    @("MoralerspaceXenonJPDOC-*.ttf", "MoralerspaceJPDOC_$version"),
    @("MoralerspaceRadonJPDOC-*.ttf", "MoralerspaceJPDOC_$version"),
    @("MoralerspaceKryptonJPDOC-*.ttf", "MoralerspaceJPDOC_$version"),

    @("MoralerspaceNeonHWJPDOC-*.ttf", "MoralerspaceHWJPDOC_$version"),
    @("MoralerspaceArgonHWJPDOC-*.ttf", "MoralerspaceHWJPDOC_$version"),
    @("MoralerspaceXenonHWJPDOC-*.ttf", "MoralerspaceHWJPDOC_$version"),
    @("MoralerspaceRadonHWJPDOC-*.ttf", "MoralerspaceHWJPDOC_$version"),
    @("MoralerspaceKryptonHWJPDOC-*.ttf", "MoralerspaceHWJPDOC_$version")
)

$timestamp = Get-Date -Format "yyyyMMddHHmmss"
$move_dir = ".\release_files\build_$timestamp"

$move_file_src_dest | Foreach-Object {
    $folder_path = "$move_dir\$($_[1])"
    New-Item -ItemType Directory -Force -Path $folder_path
    Move-Item -Path ".\build\$($_[0])" -Destination $folder_path -Force
}
