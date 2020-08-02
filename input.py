"""简单的解决判断回文问题"""

def reverse(text):
    """倒转字符串"""
    return text[::-1]   # 使用切片功能反转字符串
# end

def is_palindrome(text):
    """检测字符串是否为回文"""
    return text == reverse(text)
# end



something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome.")
else:
    print("No, it is NOT a palindrome.")
