#morse_codeconv

char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}


def encode_morse(strr):

    ustrr = strr.upper()

    resultt=""
    for i in strr:
        resultt+=char_to_dots[i]
        resultt+=" "

    return resultt[:-1]

print(encode_morse("HELP ME !"))



def can_see_stage(listoflists):
    cansee=True
    templ = [ 0 for i in range (len(listoflists[0]))]
    #templ =listoflists[0]
    
    for subl in listoflists:
        c=0
        outbreak=False
        if outbreak:
            break
        else:

            for v in subl:
                if v > templ[c]:
                    templ[c]=v
                    c+=1
                else: 
                    cansee=False
                    outbreak=True
                    break

    return cansee


print(can_see_stage([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]))

print(can_see_stage([
  [2, 0, 0], 
  [1, 1, 1], 
  [2, 2, 2]
]))

print(can_see_stage([
  [1, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]) )




