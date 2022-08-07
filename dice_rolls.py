import PySimpleGUI as sg
import random as rand

def roll(sides, num_dice = 1, effect = 'standard'):
    if int(num_dice) > 1 and effect == 'standard':
        result = []
        for i in range(num_dice):
            result.append(rand.randint(1, sides))
        return f'{result} \nTotal: {sum(result)}'
    elif num_dice == 1 and effect == 'Disadvantage':
        result = []
        for i in range(num_dice + 1):
            result.append(rand.randint(1, sides))
        return f'{result} \nRoll Result: {min(result)}'
    elif num_dice == 1 and effect == 'Advantage':
        result = []
        for i in range(num_dice + 1):
            result.append(rand.randint(1, sides))
        return f'{result} \nRoll Result: {max(result)}'
    else:
        result = rand.randint(1, sides)
        return result

sg.theme('Reddit')
layout = [
          [sg.T("Choose your dice:"), sg.T("            "), sg.T("Dice Effect:")],
          [sg.Radio('D20', 'dice01', default = True, key = "-DICE20-"),  sg.Radio('D12', 'dice01', default = False, key = "-DICE12-"), sg.T("            "), sg.Radio('Standard Roll', 'effect01', default= True, key= "-EFFECT_STAND-"), sg.Radio('Advantage', 'effect01', default= False, key= "-EFFECT_ADJ-"), sg.Radio('Disadvantage', 'effect01', default= False, key= "-EFFECT_DIS-")],
          [sg.Radio('D10', 'dice01', default = False, key = "-DICE10-"), sg.Radio('D8', 'dice01', default = False, key = "-DICE8-")],
          [sg.Radio('D6  ', 'dice01', default = False, key = "-DICE6-"),  sg.Radio('D4', 'dice01', default = False, key = "-DICE4-")],
          [sg.T("")], [sg.T("                                   "), sg.Button('Roll!', size=(20, 4))], [sg.T("")]
            ]
window = sg.Window('Let\'s Roll!', layout, size=(525, 250))
event, values = window.read()

#########Button Functions#########
while True:      # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Roll!' and values["-DICE20-"] == True:
        if values["-EFFECT_STAND-"]:
            sg.popup(roll(20, 1))
        elif values["-EFFECT_ADJ-"]:
            sg.popup(roll(20, 1, "Advantage"))
        elif values["-EFFECT_DIS-"]:
            sg.popup(roll(20, 1, "Disadvantage"))
    elif event == 'Roll!' and values["-DICE12-"] == True:
        if values["-EFFECT_STAND-"]:
            sg.popup(roll(12, 1))
        elif values["-EFFECT_ADJ-"]:
            sg.popup(roll(12, 1, "Advantage"))
        elif values["-EFFECT_DIS-"]:
            sg.popup(roll(12, 1, "Disadvantage"))
    elif event == 'Roll!' and values["-DICE10-"] == True:
        if values["-EFFECT_STAND-"]:
            sg.popup(roll(10, 1))
        elif values["-EFFECT_ADJ-"]:
            sg.popup(roll(10, 1, "Advantage"))
        elif values["-EFFECT_DIS-"]:
            sg.popup(roll(10, 1, "Disadvantage"))
    elif event == 'Roll!' and values["-DICE8-"] == True:
        if values["-EFFECT_STAND-"]:
            sg.popup(roll(8, 1))
        elif values["-EFFECT_ADJ-"]:
            sg.popup(roll(8, 1, "Advantage"))
        elif values["-EFFECT_DIS-"]:
            sg.popup(roll(8, 1, "Disadvantage"))
    elif event == 'Roll!' and values["-DICE6-"] == True:
        if values["-EFFECT_STAND-"]:
            sg.popup(roll(6, 1))
        elif values["-EFFECT_ADJ-"]:
            sg.popup(roll(6, 1, "Advantage"))
        elif values["-EFFECT_DIS-"]:
            sg.popup(roll(6, 1, "Disadvantage"))
    elif event == 'Roll!' and values["-DICE4-"] == True:
        if values["-EFFECT_STAND-"]:
            sg.popup(roll(4, 1))
        elif values["-EFFECT_ADJ-"]:
            sg.popup(roll(4, 1, "Advantage"))
        elif values["-EFFECT_DIS-"]:
            sg.popup(roll(4, 1, "Disadvantage"))