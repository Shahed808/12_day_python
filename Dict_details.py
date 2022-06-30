''' Dict is known as key:value pair
Empty dict can be represented by {}
Keys are more important in the dict'''


# r = {1:'hello',2:'python',3:'program'}
# print(r,type(r))                                                          # {1: 'hello', 2: 'python', 3: 'program'} <class 'dict'>


# w = {'a': 12.3,
# 'b':'hii',
# 3:True}
# print(w[True])                                                             # KeyError
# print(w['b'])                                                              # 'hii
# print(w['a'])                                                              # 12.3



''' Dict methods'''

# print(dir(dict))

# s = {1:12.3,                                                                # clear()
# 'hii':'shahed',
# 12.6:5}
# s.clear()
# print(s)                                                                    # {}



# r = [151,12.3,25,556,452,1]                                                 # fromkeys()
# print(dict.fromkeys(r,'getout'))                                            # {151:'getout',12.3:'getout',25:'getout',556:'getout',452:'getout',1:'getout'}


# t = {1:'hello', 2:56, 3:8.652, 4:True, 5:[1,3.6], 6:{'hi',(False,0,1)}, 7:(), 8:{}}   # get()
# print(t.get(5))                                                                 # [1,3.6]
# print(t.get(6))                                                                 # {'hi',(False,0,1)}
# print(t.get(8))                                                                 # {}
# print(t.get(77))                                                                 # None


# d = {1:'hello', 
# 3.6:'python', 
# True:1, 
# 'a':56.32}
# print(d)                                                                        # Doubt



# e = {'s':256,                                                                     # items()
# 12:'welcome!',
#  3.65:True,
#  8 : '123' }

# print(e.items())                                                                  # dict_items([('s', 256), (12, 'welcome!'), (3.65, True), (8, '123')])                         




# e = {'s':256,                                                                       # keys()                                                              
# 12:'welcome!',
#  3.65:True,
#  8 : '123' }

# print(e.keys())                                                                     # dict_keys(['s', 12, 3.65, 8])



# y = {1:'code',                                                                      # pop()
# 's': 125,
# 3.56:True,
# False: 'Boolean'}

# y.pop(False)
# print(y)                                                                            # {1: 'code', 's': 125, 3.56: True}


# y = {1:'code',                                                                      # popitem()
# 's': 125,
# 3.56:True,
# False: 'Boolean'}

# y.popitem()
# print(y)                                                                            # {1: 'code', 's': 125, 3.56: True}



# t = {1:'hello',                                                                       # setdefault()
# 2:56,
#  3:8.652,
#   4:True, 
#   5:[1,3.6], 
#   6:{'hi',(False,0,1)},
#    7:(), 
#    8:{}}   

# t.setdefault(5,(1,2))
# print(t)                                                                            # {1: 'hello', 2: 56, 3: 8.652, 4: True, 5: [1, 3.6], 6: {'hi', (False, 0, 1)}, 7: (), 8: {}}


# t.setdefault(4,(True,False))
# print(t)                                                                            # Nothing changes

# t.setdefault(10,[1,'hello',23.65,True])
# print(t)                                                                            # {1: 'hello', 2: 56, 3: 8.652, 4: True, 5: [1, 3.6], 6: {'hi', (False, 0, 1)}, 7: (), 8: {}, 10: [1, 'hello', 23.65, True]}



# t = {1:'hello',                                                                     # update()
# 2:56,
#  3:8.652,
#   4:True, 
#   5:[1,3.6], 
#   6:{'hi',(False,0,1)},
#    7:(), 
#    8:{1,5,2.36}}   

# t.update({8: 'python'})
# print(t)                                                                             # {8: 'python'}

# t.update({10: 56})
# print(t)                                                                             # {1: 'hello', 2: 56, 3: 8.652, 4: True, 5: [1, 3.6], 6: {'hi', (False, 0, 1)}, 7: (), 8: {1, 2.36, 5}, 10: 56}


t = {1:'hello',                                                                        # values()
2:56,
 3:8.652,
  4:True, 
  5:[1,3.6], 
  6:{'hi',(False,0,1)},
   7:(), 
   8:{1,5,2.36}}   

print(t.values())                                                                      # dict_values(['hello', 56, 8.652, True, [1, 3.6], {'hi', (False, 0, 1)}, (), {1, 2.36, 5}])