file = open("ciphertext", 'r')
cipher = list(file.read()[8:-1])

# key is 25
for key in range(-25,26):
   print("picoCTF{", end = "")

   for i in cipher:
      if(ord(i) + key < 0 + ord('a')): print(chr(ord(i) + key + 25), end="")
      elif(ord(i) + key > 25  + ord('a')): print(chr(ord(i) + key - 25), end="")
      else: print(chr(ord(i) + key), end="")

   print("}")