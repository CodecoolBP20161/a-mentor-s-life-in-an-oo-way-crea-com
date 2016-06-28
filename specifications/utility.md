# Utility

## Description
This class represents all kinds of utilities in the school.

## Parent class
None

## Attributes

* ```name```
  * data type: string
  * description: stores the name, which is also the type of the utility (e.g. "coffee_machine").
* ```status```
  * data type: boolean
  * description: stores the state of the utility: if working, it's True, if not, it's False. Initialized to True.


## Instance methods

### ```beeping```

Changes the status of the utility to False, meaning it is broken and needs maintenance. Changes the feeling of all Person to mad.

#### Arguments
None

#### Return value

```Utility``` object
```Person``` object


### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None
