# https://play.picoctf.org/practice/challenge/144
# flag is: picoCTF{next_time_I'll_try_2_rounds_of_rot13_TLcKBUdK}

import codecs

rot13 = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_GYpXOHqX}"
print(codecs.decode(rot13, 'rot_13'))