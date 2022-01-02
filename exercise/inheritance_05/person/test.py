from inheritance_05.person.project.person import Person
from inheritance_05.person.project.child import Child


ch = Child("ma",5)
print(ch.__dict__)
print(ch.name)
print(ch.age)