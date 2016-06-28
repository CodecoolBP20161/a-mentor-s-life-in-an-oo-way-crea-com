# Mentor

## Description

This class represents a Mentor in CodecoolClass.

## Parent class
It has Staff as parent class, and inherits also from the Person abstract class.

## Attributes

* ```hobbies```
    * data type: list
    * description: stores various hobbies of the Mentors
* ```feeling```
    * data type: list (containing strings to describe feelings)
    * description: stores the possible feelings of the Mentor in a list
* ```energy```
    * data type: list (containing strings to describe the energy level)
    * description: stores the confidence level of the Mentor

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments
Inherits its arguments from the parent class (Person) and the Mixin class (Staff).

#### Return value
```Mentor``` object

### ```gong```
Change CodecoolClass attention to ```True```.

#### Arguments
None

#### Return value
boolean ```True```

### ```check_attendance```
Check the CodecoolClass's attendance. (So important right now!)

#### Arguments
None

#### Return value
```Mentor``` object

```CodecoolClass``` object

### ```share_knowledge```
Mentor gives a demo to explain why Python sucks etc...

#### Arguments
None

#### Return value
```CodecoolClass``` object

```Mentor``` object

### ```maintain_utility```
Repairs / cleans broken utilities, such as dishwasher, coffee machine. Thanks!

#### Arguments
None

#### Return value
boolean ```True```

### ```check_energy```
Checks the energy level of CodecoolClass.

#### Arguments
None

#### Return value
```Mentor``` object

### ```do_hobby```
After a hard day Mentor does his favorite hobby.

#### Arguments
None

#### Return value
```Mentor``` object
