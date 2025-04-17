from playsound import playsound
from flask import Flask,render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

import time


app=Flask(__name__)

app.config['SECRET_KEY']= "NEW"

class UserInput(FlaskForm):
    user_input=StringField("Enter Your Text: ", default="")
    morse_input=StringField("Morse Input", default="")
    submit=SubmitField("Submit")



@app.route("/", methods=['POST', 'GET'])
def home():
    form=UserInput()
    user_input = form.user_input.data
    translate_dic={
        'A':'._','B':'_...','C':'_._.',
        'D':'_..','E':'.', 'F':'.._.',
        'G':'__.','H':'....', 'I':'..','J':'.___',
        'K':'_._', 'L':'._..','M':'__','N':'_.', 'O':'___',
        'P':'.__.', 'Q':'__._','R':'._.', 'S':'...',
        'T':'_', 'U':'.._', 'V':'..._','W':'.__','X':'_.._',
        'Y':'_.__','Z':'__..', '0':'_____', '1':'.____',
        '2':'..___', '3':'...__','4':'...._','5':'.....',
        '6':'_....', '7':'__...', '8':'___..','9':'____.',
        ' ':'/',
         }
    
    user_input = " ".join(translate_dic[c] for c in user_input.upper())
    output=user_input

    def play_sound(user_input):
        for c in user_input:
            if c==".":
                playsound('resourse/short.wav')
                time.sleep(0.001)

            elif c=="_" :
                playsound('resourse/long.wav')
                time.sleep(0.001)

            elif c==" " or "/" :
                time.sleep(0.01)

            else:
                return "There was an Error...Sorry try again please!" 
    play_sound(user_input)            

    
    return render_template("index.html", form=form,output=output)



#From Morse code to Text
@app.route("/Morse-Converter", methods=['POST', 'GET'])
def morse():
    form=UserInput()
    morse_input = form.morse_input.data
    translate_dic={
        'A':'._','B':'_...','C':'_._.',
        'D':'_..','E':'.', 'F':'.._.',
        'G':'__.','H':'....', 'I':'..','J':'.___',
        'K':'_._', 'L':'._..','M':'__','N':'_.', 'O':'___',
        'P':'.__.', 'Q':'__._','R':'._.', 'S':'...',
        'T':'_', 'U':'.._', 'V':'..._','W':'.__','X':'_.._',
        'Y':'_.__','Z':'__..', '0':'_____', '1':'.____',
        '2':'..___', '3':'...__','4':'...._','5':'.....',
        '6':'_....', '7':'__...', '8':'___..','9':'____.',
        ' ':'/','':''
         }

    reverse_dic={v:k for k,v in translate_dic.items()}
    try:
     morse_message= "".join(reverse_dic[c] for c in morse_input.split(" "))

     text_output=morse_message
    except KeyError:
        error_message="Invalid Input!!! Please Enter valid Morse code"
        return error_message


    return render_template("morse.html",form=form, text_output=text_output)










if __name__ == "__main__":
    app.run(debug=True)   