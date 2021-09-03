#OTP encoder
import sys
import secrets

if(len(sys.argv) > 1):
    print("file given, proceeding")
else:
    sys.exit("missing argument; no file given --> aborting")
    

filehandle = open(sys.argv[1], 'r')
file = filehandle.readlines()
filehandle.close()
string = ''.join(file)
string = string.replace('\n', ' ')
rand_list = []
derived_list = []

#create random letter string
for i in list(string):    
    rand_number = secrets.choice(range(32, 128))
    rand_list.append(chr(rand_number))
    
#create derived string
    derived = ()
    if(ord(i) - rand_number >= 1):
        derived = ord(i) - rand_number + 31
    else:
        derived = ord(i) - rand_number + 31 + 96
    derived_list.append(chr(derived))

#decode into original string as test
decoded_list = []
for i in range(len(rand_list)):
    if(ord(rand_list[i]) + ord(derived_list[i]) - 64 > 90):
        decoded_list.append(chr(ord(rand_list[i]) + ord(derived_list[i]) - 31 - 96))
    else:
       decoded_list.append(chr(ord(rand_list[i]) + ord(derived_list[i]) - 31))

#print all strings to console
print("string0: ", string)
print("string1: ", "".join(rand_list))
output_file1 = sys.argv[1][:-4] + "_String1.txt"
output_file2 = sys.argv[1][:-4] + "_String2.txt"
filehandle = open(output_file1, "w")
filehandle.write("".join(rand_list))
filehandle.close()
print("string2: ", "".join(derived_list))
filehandle = open(output_file2, "w")
filehandle.write("".join(derived_list))
filehandle.close()
print("decoded: ", "".join(decoded_list))
