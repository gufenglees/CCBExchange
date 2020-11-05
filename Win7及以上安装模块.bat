::Written by xizhi
@echo off
title Win7及以上安装额外模块
python -m ensurepip
python -m pip install requests
python -m pip install pillow
python -m pip install qrcode
echo.&echo 没有红色错误就按任意键完成安装&pause>nul
