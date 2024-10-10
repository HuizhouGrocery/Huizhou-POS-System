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
<br/>

Win32print is not a very popular library, which means you may get errors. You could run both commands to install it on your environment.
```shell
pip install win32printing
```
or
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

<p align="center">
  <img src="screenshot/02.JPG" width="110" title="hover text">
</p>

You could open this desktop software program with easy UI to test it. We just attached some screenshots. You only need to input product ID and product quantity to calculate price.

<p align="center">
  <img src="screenshot/03.JPG" width="510" title="hover text">
</p>

<p align="center">
  <img src="screenshot/04.JPG" width="510" title="hover text">
</p>


<p align="center">
  <img src="screenshot/05.JPG" width="510" title="hover text">
</p>


<p align="center">
  <img src="screenshot/06.JPG" width="510" title="hover text">
</p>

<p align="center">
  <img src="screenshot/07.JPG" width="510" title="hover text">
</p>

There is our receipt template, and you change languages and formats.
<p align="center">
  <img src="screenshot/09.jpg" width="510">
</p>

Once you have printed your receipt, you could check your Sqlite database.
<p align="center">
  <img src="screenshot/08.jpg" width="501" >
</p>

This python script only have 300 lines code and this lightweight exe program only have 60MB size. You may face many challenges when you start to set a printer. You just need to buy one cheap printer and 58mm paper. Your printer needs to have Windows OS driver and USB interface with your Desktop(Laptop). You need to let your printer become a default printer in your Windows environment. After that, you may find this programs runs smoothly.

We decide to choose txt format for our receipt, do not forget to change your default paper(font) size of txt format on your Windows environment. Or you may find our program can not change this. We do not have this function.

Why beta? We are still devloping some functions for our POS system. Like we could build one Mysql database on our remote server(or Cloud). Once we click check out and all data will be sent to there. We may design Inventory Management System for our grocery to save many, many IT costs. There are many functions you could think about it and develop it.
