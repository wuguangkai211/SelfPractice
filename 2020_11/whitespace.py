# 1
print("Python")
print("\tPython")

# 2
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# 3
print("python .")
print(" python")
print("python .".rstrip())  
print(" python".rstrip())
print("python ".rstrip())   # 只识别字符串末尾的空白符

ttstr = "python\n"
print(ttstr.rstrip())
print(ttstr)            # 原变量未改变
ttstr = ttstr.rstrip()  # 原变量永久改变
print(ttstr)

# 4
favorite_language = " python\n"
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
