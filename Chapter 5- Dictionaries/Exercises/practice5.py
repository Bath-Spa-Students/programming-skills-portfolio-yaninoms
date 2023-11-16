# Practice Question : Q5
'''Write a Python program to merge two dictionaries into one.'''
# the orginal dictionary first dictionary
me = {
    'first_name':'Miliani',
    'last_name':'Leopoldo',
    'age':17,
    'cat':'Nacci',
    }
# second dictionary
me_2 = {
    'favorite_song':'Vienna',
    'instrument_play':'Piano',
    'birth_place':'Singapore',
}
# merging the two dictionary
merged = {**me, **me_2}
# print results
print("The Merged List:")
for key, value in merged.items():
    print(f"{key} : {value}")




