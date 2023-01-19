import string
alpha_range = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def encrypt(unencrypted, shift_distance):
    unencrypted = open('unencrypted.txt', 'r')
    encrypted = open('encrypted.txt', 'w')
    # unencrypted = "i like tox eat cakez"
    shift_distance = int(input("Please enter a shift distance: "))
    shifted_line = ""

    for line in unencrypted:
        for char in line:


            if char in alpha_range:
                    new_char = chr(ord(char)+shift_distance)

                    if new_char not in alpha_range:
                        new_char = chr(96 + (ord(new_char) - 122))

            elif char in string.whitespace or string.punctuation:
                        new_char = char

            shifted_line = shifted_line + new_char

    encrypted.write("%s = %s\n" % ("Encrypted text", shifted_line))
    return shifted_line

# encrypt(unencrypted, shift_distance)

def decrypt(encrypted):

    encrypted1 = open('encrypted.txt')
    encrypted = encrypted1.read()



    charCount = {}
    former_word = ""
    for line in encrypted:
        for char in line:
            if char in alpha_range:
                if char in charCount:
                        charCount[char] += 1
                else:
                        charCount[char] = 1

    frequent_letter = max(charCount, key=charCount.get)

    print(frequent_letter)

    new_shift = ord(frequent_letter)-ord('e')

    for line in encrypted:
        for char in line:
            if char in alpha_range:
                old_char = chr(ord(char)-new_shift)

                if old_char not in alpha_range:
                    old_char = chr(123 - (97 - ord(old_char)))
            elif char in string.whitespace or string.punctuation:
                old_char = char

            former_word = former_word + old_char

    print(former_word)


decrypt(encrypt('unencrypted.txt', 3))
