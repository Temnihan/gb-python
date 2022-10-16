def rle_code(data):
    coding = ''
    last_char = ''
    count = 1
    if not data: return ''
    for char in data:
        if char != last_char: #
            if count == 1:
                count = ''
            coding += str(count) +last_char

            count =1
            last_char = char
        else:
            count +=1
    else:
        if count == 1:
            count = ''
        coding += str(count) + last_char
        return coding
encoded_val = rle_code('AAAAAAFDDCCCCCCCAEEEEEw')
print(encoded_val)
def decode_rle(data):
    decode = ''
    count = 1
    for char in data:
        if char.isdigit():
            count = int(char)
        else:
            decode +=char * count
            count = 1
    return decode
print(decode_rle('6AF2D7CA5Ew'))
