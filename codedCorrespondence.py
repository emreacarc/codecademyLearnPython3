eng_abc = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

message_back = "yeah, bro, i like this kind of exercises."
shift_no = -10
message_back_cripted = ""
reversed_abc = {y: x for x, y in eng_abc.items()}

#Message cripting
for letter in message_back:
    if letter in eng_abc:
        cripting_no = (eng_abc[letter] + shift_no) % 26
        message_back_cripted += reversed_abc[cripting_no]
    else:
        message_back_cripted += letter

print(message_back_cripted)

#Solving the cripted message
message_solved = ""
message_cripted = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
shift_back_no = 10

for letter in message_cripted:
    if letter in eng_abc:
        cripting_no = (eng_abc[letter] + shift_back_no) % 26
        message_solved += reversed_abc[cripting_no]
    else:
        message_solved += letter

print(message_solved)

#Defining decocing function
def caesar_decode(message, offset):
    message_decoded = ""
    for letter in message:
        if letter in eng_abc:
            cripting_no = (eng_abc[letter] + offset) % 26
            message_decoded += reversed_abc[cripting_no]
        else:
            message_decoded += letter
    return message_decoded
    print(message_decoded)

first_message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
second_message = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

caesar_decode(first_message, 10)
caesar_decode(second_message, 14)

#Defining encoding function
def caesar_encode(message, offset):
    message_encoded = ""
    offset *= -1
    for letter in message:
        if letter in eng_abc:
            cripting_no = (eng_abc[letter] + offset) % 26
            if cripting_no <= 0:
                while cripting_no <= 0:
                    cripting_no += 26
            message_encoded += reversed_abc[cripting_no]
        else:
            message_encoded += letter
    return message_encoded
    print(message_encoded)

caesar_encode("performing multiple caesar ciphers to code your messages is even more secure!", 14)

#Undefined offsets for caesar cipher
message_2 = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
for num in range(1,26):
    message_dec = caesar_decode(message_2, num)
    print("Number of offsets: " + str(num) + "// " + message_dec)












        
        

