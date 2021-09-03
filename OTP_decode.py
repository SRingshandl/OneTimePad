#OTP decoder
import sys
import random

if(len(sys.argv) == 3):
    print("files given, proceeding")
else:
    sys.exit("missing or to many arguments --> aborting")
    

filehandle = open(sys.argv[1], 'r')
file1 = filehandle.readlines()
filehandle.close()
string1_list = list(''.join(file1).replace('\n', ' '))

filehandle = open(sys.argv[2], 'r')
file2 = filehandle.readlines()
filehandle.close()
string2_list = list(''.join(file2).replace('\n', ' '))


#decode into original string as test
decoded_list = []
for i in range(len(string1_list)):
    if(ord(string1_list[i]) + ord(string2_list[i]) - 64 > 90):
        decoded_list.append(chr(ord(string1_list[i]) + ord(string2_list[i]) - 31 - 96))
    else:
       decoded_list.append(chr(ord(string1_list[i]) + ord(string2_list[i]) - 31))

#write output to console and file
print("decoded: \n", "".join(decoded_list))
filehandle = open("Decoded_text.txt", "w")
filehandle.write("".join(decoded_list))
filehandle.close()

    
