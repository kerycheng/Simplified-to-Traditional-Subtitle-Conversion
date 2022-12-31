# 簡體轉繁體中文字幕轉換工具

## 程式介面
![image](https://imgur.com/gMwfdWB.jpg)

### 程式介紹
  使用OpenCC作為轉換工具，將簡體中文的.ass字幕檔轉成繁體中文
  
### 安裝
```sh
pip install opencc-python-reimplemented
```

### 使用說明
  * 選擇簡體中文字幕檔  
  * 選擇儲存路徑  
  * 按下開始  
  * 轉換完成  
  
### 注意事項
  如果要將程式打包成.exe檔，請輸入以下指令  
```sh
pyinstaller -F --collect-data=opencc start.py -w  
```
