from itertools import count
from tkinter import *
from tkinter.tix import COLUMN
root = Tk()

##Dictonary with what proficiency bonus is at what level
proficiency_bonus_level_dic = {
    '1':2, '2':2, '3':2, '4':2,
    '5':3, '6':3, '7':3, '8':3,
    '9':4, '10':4, '11':4, '12':4,
    '13':5, '14':5, '15':5, '16': 5,
    '17':6, '18':6, '19':5, '20':6
}

##Dictionarys for skills to Abilities
skill_to_ability_dic = {
    'Acrobatics': 'Dexterity',
    'Animal Handling': 'Wisdom',
    'Arcana': 'Intelligence',
    'Athletics': 'Strength',
    'Deception': 'Charisma',
    'History': 'Intelligence',
    'Insight': 'Wisdom',
    'Intimidation': 'Charisma',
    'Investigation': 'Intelligence',
    'Medicine': 'Wisdom',
    'Nature': 'Intelligence',
    'Perception': 'Wisdom',
    'Performance': 'Charisma',
    'Persuasion': 'Charisma',
    'Religion': 'Intelligence',
    'Slight of hand': 'Dexterity',
    'Stealth': 'Dexterity',
    'Survival': 'Wisdom'
}

ability_to_skill = {
    'Strength': ['Athletics'],
    'Dexterity': ['Acrobatics', 'Slight of hand', 'Stealth'],
    'Consitution': None,
    'Intelligence':['Arcana','History','Investigation','Nature','Religion'],
    'Wisdom': ['Animal Handling', 'Insight', 'Medicine', 'Perception','Survival'],
    'Charisma': ['Deception', 'Intimidation','Performance', 'Persuasion' ]
}

##Character Stuff-----------------------------------
ability_scores_dic = {
    'Strength':15,
    'Dexterity': 8,
    'Consitiution': 10,
    'Intelligence':11,
    'Wisdom': 13,
    'Charisma': 14
}

skill_proficiencies = ['Arcana', 'History', 'Persuasion']
skill_expertise = ['Persuasion']
saving_throws = []
current_level = 3
##------------------------------------------------------


##Displays ability scores in a frame
ability_container = LabelFrame(root, text=' Abilities ', padx= 10, pady=10)
ability_container.grid(column=0, row=0, padx=10, pady=10)
line_count = 0
for ability in ability_scores_dic:
    ##Fetches modifer then adds + if needed
    modifer = (ability_scores_dic[ability]-10)//2
    if modifer > 0:
        modifer = '+' + str(modifer)
    display_ability_text = ability
    ##makes all ability names equally sized
    while len(display_ability_text) < 14:
        display_ability_text = ' '+display_ability_text+" "
    ##Makes Frame of ability
    ability_frame = LabelFrame(ability_container, text=display_ability_text, padx= 10, pady= 10, labelanchor='n')
    ability_frame.grid(row=line_count)
    line_count += 1
    ##makes label of modifer
    modifer_label = Label(ability_frame, text=str(modifer), font='Helvetica 18 bold')
    modifer_label.config(anchor=CENTER)
    modifer_label.pack()
    ##Makes label of score
    score_label = Label(ability_frame, text= str(ability_scores_dic[ability]))
    score_label.config(anchor=CENTER)
    score_label.pack()
    

##Displays Skills in a frame
skill_frame = LabelFrame(root, text=' Skills ', padx= 10, pady= 10)
skill_frame.grid(row=0, column=1, padx=10, pady=10)
line_count = 0
##Iterates through all the skills
for skill in skill_to_ability_dic:
    ##Calculates the modifier
    modifer = ability_scores_dic[skill_to_ability_dic[skill]]
    modifer = (modifer - 10) // 2
    skill_name = skill+' ('+skill_to_ability_dic[skill][0:3]+')'
    ##Adds proficiency bullet point, if not makes adds spaces
    if skill in skill_proficiencies:
        modifer += proficiency_bonus_level_dic[str(current_level)]
        if skill in skill_expertise:
             modifer += proficiency_bonus_level_dic[str(current_level)]
        skill_name = ' \u2022'+skill_name 
    else:
        skill_name = '  '+skill_name
    ##Make the labels for the value and skill name and display them
    skill_label_value = Label(skill_frame, text=str(modifer), font='Helvetica 18 bold').grid(row=line_count, column=0, sticky=W)
    skill_label_name = Label(skill_frame, text=skill_name).grid(row=line_count, column=1, sticky=W)
    line_count += 1
   
 



root.mainloop()


