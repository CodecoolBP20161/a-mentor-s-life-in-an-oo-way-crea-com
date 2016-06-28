# Student

## Description

This class represents a student in CodecoolClass.

## Parent class
Person

## Attributes

* ```energy_level```
    * data type: list (containing integers 0-10 to describe the energy level)
    * description: stores the energy level of the Student
* ```confidence```
    * data type: list (containing strings to describe the confidence level)
    * description: stores the confidence level of the Student
* ```knowledge_level```
    * data type: list (containing integers 0-10 to describe knowledge level)
    * description: stores the knowledge level of the Student in a list

## Class methods

### ```create_by_csv```

#### Arguments
csv file path

#### Return value
list of students

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

* Inherits its arguments from the parent class (Person)
* ```feeling``` set to ```None```
* ```confidence``` set to ```None```
* ```energy_level``` set to 5
* ```knowledge_level``` set to ```None```


#### Return value
```Student``` object

### ```dojo```

Small coding exercises to practice Python to boost Student's confidence. However energy_level will go down because
of the mental effort.

#### Arguments
None

#### Return value
```Student``` object
