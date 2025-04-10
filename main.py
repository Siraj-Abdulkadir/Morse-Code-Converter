from playsound import playsound
import time


translate_dic={
    'A':'._',
    'B':'_...',
    'C':'_._.',
    'D':'_..',
    'E':'.',
    'F':'.._.',
    'G':'__.',
    'H':'....',
    'I':'..',
    'J':'.___',
    'K':'_._',
    'L':'._..',
    'M':'__',
    'N':'_.',
    'O':'___',
    'P':'.__.',
    'Q':'__._',
    'R':'._.',
    'S':'...',
    'T':'_',
    'U':'.._',
    'V':'..._',
    'W':'.__',
    'X':'_.._',
    'Y':'_.__',
    'Z':'__..',
    '0':'_____',
    '1':'.____',
    '2':'..___',
    '3':'...__',
    '4':'...._',
    '5':'.....',
    '6':'_....',
    '7':'__...',
    '8':'___..',
    '9':'____.',
    ' ':'/',
    
}

message = input("Enter Your Text: ")
message= " ".join(translate_dic[c] for c in message.upper())

print(message)


def play_sound(message):
    for c in message:
        if c==".":
            playsound('resourse/short.wav')
            time.sleep(0.001)

        elif c=="_" :
            playsound('resourse/long.wav')
            time.sleep(0.001)

        elif c==" " or "/" :
            time.sleep(0.01)

        else:
            print("There was an Error...")


play_sound(message)            


reverse_dic={v:k for k,v in translate_dic.items()}

nw_message=input("Enter Your Morse Code: ")

morse_message= "".join(reverse_dic[c] for c in nw_message.split(" "))

print(morse_message)