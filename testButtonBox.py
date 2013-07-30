import easygui as eg
msg = "choose a number :"
choices = [1,2,3]
flavor = eg.buttonbox(msg = msg,choices = choices)
eg.msgbox("the number choosed is " + str(flavor))
