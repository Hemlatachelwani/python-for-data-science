Problem:
Here is a list of faculty teaching this MOOC. Can you write a function and apply it using map() to get a list of all faculty titles and last names (e.g. ['Dr. Brooks', 'Dr. Collins-Thompson', …]) ?



Solution:
  Initial draft- incorrect 
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(people):
    for itm in people:
      return(itm.split(" ")[1])

list(map(split_title_and_name,people))


Correct:
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    #person.split(" ")[0]
    #person.split(" ")[2]
    return("{} {}".format(person.split(" ")[0],person.split(" ")[-1]))

list(map(split_title_and_name,people))

Map will iterate function on each item in the list passed in second argument. 

