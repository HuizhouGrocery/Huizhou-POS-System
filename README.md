<div align="center">
  <h1 align = "center">Huizhou Grocery POS System (Beta) </h1>
</div>

[![License: MIT](https://cdn.prod.website-files.com/5e0f1144930a8bc8aace526c/65dd9eb5aaca434fac4f1c34_License-MIT-blue.svg)](/LICENSE)

This is POS(Point of Sale) system of Huizhou Grocery(beta) and it is our open-source project on Github. 

With this Python script and one Sqlite database on your desktop, you could realize simple and lightweight POS system management. At the same time, you could print your grocery receipt with this Python script.

First of all, you need to download python code, and change your directory name on script. Please do not forget about your path of Sqlite database.
Next thing is to set up your environment(Windows-oriented).

```shell
pip install ttkbootstrap
```
```shell
pip install win32printing
```
```shell
pip install pywin32
```
After you can run python code on your terminal, you need to run this code below.
```shell
pyinstaller --onefile --name huizhou-pos -i logo.jpg --windowed huizhou_pos.py
```

<p align="center">
  <img src="screenshot/01.JPG" width="1000" title="hover text">
</p>

You will get an exe file in your working directory.
