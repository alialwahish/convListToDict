name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(l1,l2):
    new_dict={}
    if len(l1) >= len(l2):
        new_dict=dict(zip(l1,l2))
        return new_dict
    else:
        new_dict=dict(zip(l2,l1))
        return new_dict

new_list=make_dict(name,favorite_animal)
print type(new_list)
print new_list
    