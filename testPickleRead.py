import pickle
file = open('mypickledlist.pkl','r')
list = pickle.load(file)
print list

