#Day 2 - Challenge
#Text Compressor Using Run Length Encoding (RLE)

text = input("Enter your text: ")

if not text:         # it handles if user gives empty input 
    print("Input is Empty")
    exit()

compressed = "" #Initialize or define the variable compressed which stores our compressed text 
prev_char = text[0]  # Initialize the previous character
count = 1 #These variable stores the count of similar character observed 

for char in range(1, len(text)):


    if text[char] == prev_char:  # If the current character is the same as the previous one
        count+=1 #Then stores the count of no of times current character observed
    else:
        compressed += prev_char + str(count) #Stores the No of characters visited in string 
        prev_char = text[char]  #If the current character is different from the previous one then resets the count and prev character 
        count = 1
compressed += prev_char + str(count) # Finally gets the Compressed text output 
print("Original text:", text)
print("Compressed text:", compressed)

original_len = len(text)
compressed_len = len(compressed)

com_ratio = compressed_len/original_len  # claculates the compression Ratio
print(f"The Compression Ratio is : {com_ratio}")
