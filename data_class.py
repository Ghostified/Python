from dataclass import dataclass

@dataclass
class Person: 
  name: str
  age: int
  job: str

person = Person(name="Branson", age=99, job="Enginer")
print(person)