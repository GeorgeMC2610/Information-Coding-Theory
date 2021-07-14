msg                     = "Geo" #input, has to be until diastasi_coded-1
input_msg               = [("0"*8+bin(ord(c))[2:])[-8:] for c in msg]

print(input_msg)