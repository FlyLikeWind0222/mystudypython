file = open("a.txt")
f_line = file.readline()
s_line = file.readline()
t_line = file.readline()
file.seek(2)
ss = file.readline()
print f_line
print  s_line
print  t_line
print  repr(ss)