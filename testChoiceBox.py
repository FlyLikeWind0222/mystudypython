import easygui as eg
flavor = eg.choicebox("What is your favorite ice cream flavor?",
choices = ['Vanilla', 'Chocolate', 'Strawberry'] )
eg.msgbox ("You picked " + flavor)
