# ini から VERSION を取得
$ini = Get-Content .\build.ini
$version = ($ini | Select-String -Pattern "VERSION").ToString().Split("=")[1].Trim()

# スクリプトファイルがある場所に移動する
Set-Location -Path $PSScriptRoot
# 各ファイルを置くフォルダを作成
New-Item -ItemType Directory -Force -Path ".\release_files\"

# ビルド 通常版
& "C:\Program Files (x86)\FontForgeBuilds\bin\fontforge.exe" --lang=py -script .\fontforge_script.py `
    && python fonttools_script.py `
    && Move-Item -Path .\build -Destination ".\release_files\Moralerspace_$version" -Force

# ビルド 1:2幅版
& "C:\Program Files (x86)\FontForgeBuilds\bin\fontforge.exe" --lang=py -script .\fontforge_script.py --half-width `
    && python fonttools_script.py `
    && Move-Item -Path .\build -Destination ".\release_files\MoralerspaceHW_$version" -Force

# ビルド JPDOC版
& "C:\Program Files (x86)\FontForgeBuilds\bin\fontforge.exe" --lang=py -script .\fontforge_script.py --jpdoc `
    && python fonttools_script.py `
    && Move-Item -Path .\build -Destination ".\release_files\MoralerspaceJPDOC_$version" -Force

# ビルド 1:2幅JPDOC版
& "C:\Program Files (x86)\FontForgeBuilds\bin\fontforge.exe" --lang=py -script .\fontforge_script.py --half-width --jpdoc `
    && python fonttools_script.py `
    && Move-Item -Path .\build -Destination ".\release_files\MoralerspaceHWJPDOC_$version" -Force
