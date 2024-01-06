@echo off
chcp 65001

echo 正在安裝 Python 和必要的套件...

:: 檢查 Python 是否已安裝
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python 未安裝. 正在下載...
    :: 下載並安裝 Python
    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe -OutFile python-installer.exe"
    :: 安裝 Python。'/quiet InstallAllUsers=1 PrependPath=1' 參數使安裝在背景進行
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
    del python-installer.exe
)

echo Python 已安裝.
echo 正在安裝必要的套件...

:: 安裝 selenium 和 webdriver_manager
pip install selenium webdriver_manager
pip install --upgrade selenium webdriver_manager

echo 套件安裝完成.
echo 正在執行程式...

:: 執行您的 Python 程式
python port3_2.py

pause
