def caeser(start_text,shift,direction):
    end_text=[]
    for letter in start_text:
        startindex=alphabet.index(letter)
        if direction=="encode":
            shifted_index=startindex+shift
            end_text.append(alphabet[shifted_index])
        else:
            shifted_index=startindex-shift
            end_text.append(alphabet[shifted_index])
    print(f"The {direction}d message is {''.join(end_text)}")
    
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
caeser(text,shift,direction)
