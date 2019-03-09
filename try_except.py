dict={"x":1,"y":2,"z":3}
try:
    value=dict["n"]
except KeyError:
    print("That key doesn't exist!")



list=[1,2,3,4,5]
try:
    list[7]
except IndexError:
    print("That index is not in the list!")



try:
    assert False
except AssertionError:
    pass
print('Congratulation! We made it!')
