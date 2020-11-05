::Written by xizhi
@echo off
title WinXP安装额外模块
python -m ensurepip
python -m pip install requests
python -m pip install pillow==5.3.0
python -m pip install colorama==0.4.1
python -m pip install qrcode
echo.&echo 没有红色错误就按任意键完成安装&pause>nul
