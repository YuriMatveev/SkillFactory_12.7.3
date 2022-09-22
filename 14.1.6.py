def check_palindrome(str_):
   str_ = str_.lower()
   str_ = str_.replace(" ", "")

   if str_ == str_[::-1]:
       return True
   else:
       return False

c = check_palindrome("test")  # False
d = check_palindrome("Кит на море не романтик")  # True
print(c)
print(d)