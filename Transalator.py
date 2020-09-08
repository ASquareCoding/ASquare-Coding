from googletrans import Translator

#Press Windows+R Then Type "cmd" And Then A Panel Will Open Then Type "pip installl googletrans" And Wait For It To Install And You will Be Ready To Go...

doagain = "yes"
while doagain == "yes":

    sentence = str(input("What Do You Want To Translate? "))
    lang = str(input("What Is Your Language? "))

    trans = Translator()

    Trans_Sentence = trans.translate(sentence,src="en",dest=lang)

    print(Trans_Sentence.text)

    doagain=str(input("Do You Wnat Do Again? "))
