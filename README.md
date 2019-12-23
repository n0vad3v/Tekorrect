# Tekorrect

![](https://img.shields.io/pypi/pyversions/Django.svg)

> 漢學家稱這個空白字元為「盤古之白」，因為它劈開了全形字和半形字之間的混沌。另有研究顯示，打字的時候不喜歡在中文和英文之間加空格的人，感情路都走得很辛苦，有七成的比例會在 34 歲的時候跟自己不愛的人結婚，而其餘三成的人最後只能把遺產留給自己的貓。畢竟愛情跟書寫都需要適時地留白。
>
> 如果真正在意 typography，那麼漢字與西文之間應該插入一個半角空格。Adobe InDesign、Microsoft Word 等對中文與西文混合排版支持較好的軟件，都默認增大漢字和西文的間距。
>
> 漢學家稱這個空白字元爲「盤古之白」，因爲它劈開了全形字和半形字之間的混沌，增加了文字的 readability。
>

此 Python 腳本用於給已經完成的 Markdown 遍寫的文檔進行優化，它會將壹些非標準，或不推薦的排版方式，進行自動格式化、標準化。

使用 [vinta/pangu.py](https://github.com/vinta/pangu.py) 爲基礎製作，對 pangu.py 有所修改，並已經包含在本倉庫中（不再需要單獨安裝 pangu.py）。

# 用法

使用 pip 安裝，例如： `pip3 install tekorrect`。

後對包含 Markdown 文件的文件夾使用以下指令：
```bash
tekorrect -p /path/to/hexo/source/_posts
```
若是針對單獨的文件，可使用以下指令
```bash
tekorrect -f /path/to/hexo/source/_posts/1.md
```

目前版本功能尚未完善，文章標題部分也會被自動添加空格（如不希望使用此功能請對本倉庫進行 Star 並等待後續更新）。

此程序**就地對文件進行修改**，強烈建議在進行前對原始文件進行備份！

# TO-DO

- [ ] 跳過文章 title 優化
- [x] 修复 Markdown 格式标记不当优化问题（例如：加粗的`**`和删除符号`~~`）
- [ ] 自动处理 gitHUB, Http 之类的拼写问题

# Authors

[Nova Kwok](https://github.com/n0vad3v)

[BennyThink](https://github.com/bennythink)
