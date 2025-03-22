from adafruit_circuitplayground import cp
import time
dictionary = {'a':'.-','b':'-...','c':'-.-.',
              'd':'-..','e':'.','f':'..-.','g':'--.','h':'....',
              'i':'..','j':'.---','k':'-.-','l':'.-..',
              'm':'--','n':'-.','o':'---','p':'.--.','q':'--.-',
              'r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--',
              'x':'-..-','y':'-.--','z':'--..','1':'.----','2':'..---',
              '3':'...--','4':'....-','5':'.....','6':'-....',
              '7':'--...','8':'---..','9':'----.','0':'-----',' ':'/'}
while True:
    phrase = input("Enter a phrase:")
    time_input = float(input("Enter a time (0-1):"))
    phrase = phrase.lower()
    phrase_list = []
    morse_list = []
    for x in phrase:
        if x not in dictionary:
            print("Sorry, we don't have that phrase")
            break
        elif x in dictionary:
            phrase_list.append(x)
    print(phrase_list)
    for i in phrase_list:
        morse_list.append(dictionary[i])
    for q in morse_list:
        cp.pixels.fill((0,0,0))
        if q != '/':
            time.sleep(3)
        else:
            time.sleep(0)
        for i in q:
            cp.pixels.fill((0,0,0))
            time.sleep(time_input*3)
            if i == '.':
                cp.pixels.brightness =0.01
                cp.pixels.fill((255,0,255))
                time.sleep(time_input)
            elif i == '-':
                cp.pixels.brightness =0.01
                cp.pixels.fill((255,0,255))
                time.sleep(time_input*4)
            elif i == '/':
                cp.pixels.brightness =0.01
                cp.pixels.fill((255,0,0))
                time.sleep(7)
        cp.pixels.fill((0,0,0))

            
            
 