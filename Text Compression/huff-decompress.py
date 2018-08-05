import time
import pickle

start1 = time.clock()
#unpickling the symbol model
pkl_file = open("infile-symbol-model.pkl", 'rb')
code = pickle.load(pkl_file)

with open("infile.bin", 'rb') as file,open('infile-decompressed.txt', 'w') as output:
    # transfate the encode 
    bit_string = ""
    byte = file.read(1)

    while(len(byte) > 0):
        byte = ord(byte)
        bits = bin(byte)[2:].rjust(8, '0')
        bit_string += bits
        byte = file.read(1)
        
    padded_info = bit_string[:8]
    extra_padding = int(padded_info, 2)
    padded_encoded_text = bit_string[8:]
    encoded_text = padded_encoded_text[:-1*extra_padding]
    
    #decode the txt file
    code1 = {value:key for key,value in code.items()}
    current_code = ""
    for letter in encoded_text:  
        current_code += letter  
        if code1.get(current_code):  
            output.write(code1[current_code])  
            current_code = '' 

    output.close() 

elapsed1 = (time.clock() - start1)   
print('it takes',elapsed1,'s to decode the compressed file')  
    

