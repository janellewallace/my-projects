encryption_option = input("Would you like to Encode or Decode? ") 

should_encode = "encode" in encryption_option.lower()
should_decode = "decode" in encryption_option.lower()

cipher_number = int (input("What is your cipher number? "))
message = input("What is your message? ")

if should_encode:
    output = ""
    all_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for index in range (len(message)):
        message_letter = message[index]
        if (message_letter == " "):
            output += " "
        elif (not message_letter.isalpha()):
            output += message_letter
        for i in range (len(all_letters)):
            letter = all_letters[i]
            if (message_letter.isupper()):
                if (message_letter.lower() == letter):
                    if (i >= (len(all_letters)- cipher_number) ):
                        new_letter = all_letters[cipher_number - (len(all_letters)- i)]
                    else:
                        new_letter = all_letters[i + cipher_number]
                    output += new_letter.upper()
            else:
                if (message_letter.lower() == letter):
                    if (i >= (len(all_letters)- cipher_number) ):
                        new_letter = all_letters[cipher_number - (len(all_letters)- i)]
                    else:
                        new_letter = all_letters[i + cipher_number]
                    output += new_letter
    print (output)
elif should_decode:
    output = ""
    all_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for index in range (len(message)):
        message_letter = message[index]
        if (message_letter == " "):
            output += " "
        elif (not message_letter.isalpha()):
            output += message_letter
        for i in range (len(all_letters)):
            letter = all_letters[i]
            if (message_letter.isupper()):
                if (message_letter.lower() == letter):
                    new_letter = all_letters[i - cipher_number]
                    output += new_letter.upper()
            else:
                if (message_letter.lower() == letter):
                    new_letter = all_letters[i - cipher_number]
                    output += new_letter
    print (output)
else:
    print ("We only support encrypt/decrypt.")
   
