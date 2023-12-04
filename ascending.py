# sample dictionary
my_dict={'banana':3,'apple':1,'cherry':2,'date':4}
print("Orginal list:",my_dict)
#sort in ascending order based on keys
asorted_dict= dict(sorted(my_dict.items()))
print("Ascending order:",asorted_dict)
#sort in decending order based on keys
desorted_dict=dict(sorted(my_dict.items(),reverse=True))
print("Descending order:",desorted_dict)
