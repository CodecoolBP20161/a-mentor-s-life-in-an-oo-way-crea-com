# Person

## Description
This class represents a parent class for further child classes, which are all "person": Student, Staff(Creepy_guy, Mentor).

## Parent class
None

## Attributes

* ```first_name```
  * data type: string
  * description: first name of a person
* ```last_name```
  * data type: string
  * description: first name of a person
* ```year_of_birth```
  * data type: integer
  * description: year of person's birthday
* ```gender```
  * data type: string
  * description: gender of person (male/female/notsure)
* ```feeling```
  * data type: list
  * description: stores the 8 possible feelings as strings in a list: satisfied, happy, nervous, sad, mad, proud, energized, uncomfortable.


## Class methods

### ```drink_coffee```

Changes both energy level and feeling of Person subclasses.

#### Arguments
None

#### Return value

```Person``` object

### ```lunch_break```

Changes both energy level of a Person instance and attention level of the CodecoolClass.

#### Arguments
None

#### Return value

```CodecoolClass``` object
```Person``` object

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None
