from dataclasses import dataclass

@dataclass
class Person: 
  name: str
  age: int
  job: str

person = Person(name="Branson", age=99, job="Enginer")
print(person)

#test for equivalence with data class
person2 = Person(name="Allan", age=89, job="Engineer")
print(person == person2)
