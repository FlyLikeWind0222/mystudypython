import pickle
mylist = ['Fred','b','c','d']
file = open('mypickledlist.pkl','w')
pickle.dump(mylist,file)
file.close()
