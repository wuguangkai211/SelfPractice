# encoding=utf-8

import io

f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"神秘的帅哥")        # Imagine non-English language here
f.close()

text = io.open("abc.txt", encoding="utf-8").read()
print(text)


""" 每当我们诸如上面那番使用 Unicode 字面量编写一款程序时，我们必须确保 Python 程序已经被告知我们使用的是 UTF-8，
因此我们必须将 `# encoding=utf-8` 这一注释放置在我们程序的顶端。 """
