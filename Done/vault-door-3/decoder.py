"""
public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) { // 8 - 15
            buffer[i] = password.charAt(23-i); // 15-8
        }
        for (; i<32; i+=2) { // 16 - 32
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
"""

key = list("jU5t_a_sna_3lpm18gb41_u_4_mfr340")

i = 0
r = []

for x in range(0,32):
    r.append(x)

while i < 8:
    r[i] = key[i]
    i += 1

while i < 16:
    r[i] = key[23-i]
    i += 1

while i < 32:
    r[i] = key[46-i]
    i += 2

i = 31

while i >= 17:
    r[i] = key[i]
    i -= 2

print(''.join(r))