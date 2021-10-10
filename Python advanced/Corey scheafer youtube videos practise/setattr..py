class Person():
    pass

person=Person()
first_key="nm"
first_val="hemuu"

setattr(person, first_key, first_val)

print(getattr(person, first_key))
