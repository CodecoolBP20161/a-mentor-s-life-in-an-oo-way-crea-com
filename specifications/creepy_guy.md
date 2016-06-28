# Creepy Guy

## Description
This class represents a real class @ Codecool, containing Creepy Guy who gives feedback to mentors, and freaks out people
around him.

## Parent class
It has Staff as parent class, which comes from the abstract class Person
Inherits checking_progress(), feedback(), drink_coffe(), lunch_break methods,

## Attributes

* ```creepiness_level```
  * data type: boolean value
  * description: when this value True it changes the mentors feelings



## Class methods

### ```arrive```

The title pretty self describing, CG arrives to the scene which should affect others feelings
Sets feelings to nervous
#### Return value
```Feeling``` a string

### ```creeping_around```

CG walks around the class, overseeing the mentors actions, and making notes. This is going to affect
the mentors and students feelings

#### Return value
```Feeling``` a string





A list of strings, representing the objects mood.
CG has effect on others around him, usually makes them nervous, but if the mentor gets a good feedback, it can make them happy.

## Instance methods

### ```__init__``` ###
The constructor of the object. Takes feeling, energy from Person class.
