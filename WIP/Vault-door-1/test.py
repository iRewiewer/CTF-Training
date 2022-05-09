test = {0:"d", 29:"3", 4:"r", 2:"5", 23:"r", 3:"c", 17:"4", 1:"3", 7:"b", 10:"_", 5:"4", 9:"3", 11:"t", 15:"c", 8:"l", 12:"H", 20:"c", 14:"_", 6:"m", 24:"5", 18:"r", 13:"3", 19:"4", 21:"T", 16:"H", 27:"f", 30:"b", 25:"_", 22:"3", 28:"6", 26:"f", 31:"0"}

password = """
password.charAt(0)  == 'd'
password.charAt(29) == '3'
password.charAt(4)  == 'r'
password.charAt(2)  == '5'
password.charAt(23) == 'r'
password.charAt(3)  == 'c'
password.charAt(17) == '4'
password.charAt(1)  == '3'
password.charAt(7)  == 'b'
password.charAt(10) == '_'
password.charAt(5)  == '4'
password.charAt(9)  == '3'
password.charAt(11) == 't'
password.charAt(15) == 'c'
password.charAt(8)  == 'l'
password.charAt(12) == 'H'
password.charAt(20) == 'c'
password.charAt(14) == '_'
password.charAt(6)  == 'm'
password.charAt(24) == '5'
password.charAt(18) == 'r'
password.charAt(13) == '3'
password.charAt(19) == '4'
password.charAt(21) == 'T'
password.charAt(16) == 'H'
password.charAt(27) == 'f'
password.charAt(30) == 'b'
password.charAt(25) == '_'
password.charAt(22) == '3'
password.charAt(28) == '6'
password.charAt(26) == 'f'
password.charAt(31) == '0'"""

pwd = {}
value = "-x1"
key = "-x1"

for i in password.split("'"):
    if len(i) == 1: value = i
    elif len(i) == 24:
        if i[19:22] == ") =": key = i[17:18]
        else: key = i[17:19]

    if not value == "-x1" and not key == "-x1":
        pwd[key] = value
        key = "-x1"
        value = "-x1"

pwdSorted = dict(sorted(pwd.items()))

for i in pwdSorted.values():
    print(i, end="")