empty_tupl=()
print(empty_tupl)
tupl=('java','cpp','python','html','css','AI')
print(tupl)
#for lenght of item
print(len(tupl))
#calling from index
second_language=tupl[2]
fourth_language=tupl[4]
print(second_language,fourth_language)
#for calculating last index
last_index=len(tupl) -1
print(last_index)
# calling from inverse index
first_item=tupl[-1]
print(first_item)
#slicing tuples
all_items=tupl[0:6]
print(all_items)
selected_items=tupl[3:5]
print(selected_items)
negative_index=tupl[-6:-4]
print(negative_index)
#tuples to list
tupl=list(tupl)
tupl[3]='PHP'
print(tupl)
tupl=tuple(tupl)
print(tupl)
#checking a item in tuple
print('java'in tupl)
print('cnn'in tupl)
#joining tuples
tupl1=('DIP','GNSS','NRM')
tupl2=tupl+tupl1
print(tupl2)
#deleting tuples
del tupl1
print(tupl1)