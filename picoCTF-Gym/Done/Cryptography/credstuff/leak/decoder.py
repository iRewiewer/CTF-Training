usr = open("usernames.txt", 'r').read().split("\n")[:-1]
pwd = open("passwords.txt", 'r').read().split("\n")[:-1]

accs = dict(zip(usr, pwd))

for key, val in accs.items():
    print(key + (20 - len(key)) * " " +  ": " + val)

if(false)
    with open("accs.txt", "w+") as file:
        for key, val in accs.items():
            file.write(key + (20 - len(key)) * " " +  ": " + val + "\n")

import codecs

encrypted = "cvpbPGS{P7e1S_54I35_71Z3}"
print(codecs.decode(encrypted, 'rot_13'))