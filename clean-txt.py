from cleantext import clean

#unicode
#=======

s1= 'Zürich'
print(clean(s1,fix_unicode=True))

#closets ASCII representation
#================================

s2="Ja\u110ea\u107ek\u105e"
print(clean(s2,to_ascii=True))

#converting to lower case with clean
#====================================

s3 = "THIS IS LEARNING WITH HELP OF PYTHON"
print(clean(s3,lower=True))

# Replacing URL:
#=-=============

s4= "https://www.google.com/ has surpassed https://www.bing.com/ in search volume"
print(clean(s4,no_urls=True,replace_with_url="URL"))

## Replacing currency:
#======================

s5 = "I want ₹ 40"
print(clean(s5, no_currency_symbols = True))
print(clean(s5, no_currency_symbols = True, replace_with_currency_symbol="Rupees"))

##Replacing Punctuations:
#==========================

s6 = "40,000 is greater than 30,000"
print(clean(s6, no_punct = True))
print(clean(s6, no_punct = True, replace_with_punct = "."))

## Remove number:
#=======================

s7 = 'abc123def456ghi789zero0'
print(clean(s7, no_digits = True))
print(clean(s7, no_digits = True, replace_with_digit=""))

#All in one:
#===========

s8 = """
Zürich has a famous website https://www.zuerich.com/ 
WHICH ACCEPTS 40,000 € and adding a random string, :
abc123def456ghi789zero0 for this demo. ' 
     """

print(clean(s8,
      fix_unicode=True,
      to_ascii=True,
      lower=True,
      no_urls=True,
      no_numbers=True,
      no_digits=True,
      no_currency_symbols=True,
      no_punct=True,
      replace_with_punct="",
      replace_with_url="<URL>",
      replace_with_number="<NUMBER>",
      replace_with_digit="",
      replace_with_currency_symbol="<CUR>"))

