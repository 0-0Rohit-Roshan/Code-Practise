### Strings
-Can use `'..'` or `".."` for string but use the same pair.
-Single quote makes it easier to write HTML within javascript.No need to escape the line with double quote.
-Use opposite quotation mark outside ,if you have one inside a string. Or use a backslash, this lets javascript know you are useing a special character.
-String Methods and Properties are `.length` , `.toLowerCase()` , `.toUpperCase()` , `.trim()` ....

### Numbers
-No special syntax required.
-`1234;`
-`10 + 3.141;`
-`1/3;`
-`11/10;`
-`1+(4/3);`
-`-3;`
-`5-7;`
-Every above code sample is legit for numbers.

### Booleans
-`var kitchenLights = false;`
-`kitchenLights = true;`
-`kitchenLights;`

### Operators
-`1+2;`
-`3-2;`
-`3*4;`
-`4/2;`
-`1+2*3;` follows BODMAS.
-`(1+2)*5;` Grouping to avoid BODMAS.
-`+` operator performs concatenation of strings.

### Variables
-`var x = 100;`
-`var x = 100; 
  x + 102;`
-`var x = 100;`
  var y = x + 102;
  y;`
-`var weather = "rainy";
  weather = "sunny";
  weather;`
-Naming variables
	-Start them with a letter,underscore or dollar.
	-Then after can use "123..","abkjsd..",_,$.
	-No javascript reserved keywords are allowed.
	-Var names are case sensitive.

### Functions
-Function names are just like variable and Reusable.
- `function` `function name` (`parameters`){
	`function logic`
	}
-Parameters are separated by comma.

### Conditionals
- “If” statements: where if a condition is true it is used to specify execution for a block of code.
- “Else” statements: where if the same condition is false it specifies the execution for a block of code.
- “Else if” statements: this specifies a new test if the first condition is false.

### Arrays
```Javascript
 var breakfast = ["coffee","croissant"];
 breakfast;
 ```
["cofee","croissant"]

```Javascript
 var store = [100,"paint",[200,"brush"],false];
 store;
 ```
[100,"paint",[200,"brush"],false]
- Elements can be accessed by index numbers.
```Javascript
store[0];
```
100
- Setting an elements value
```Javascript
var letters = ["a","d","c"];
letters[1] = "b";
letters;
```
["a","b","c"]
-Properties and methods
-Length 
```Javascript
EXAMPLE
["a", "b", "c", 1, 2, 3].length;
OUTPUT
6
```
-Concat
```Javascript
EXAMPLE
["tortilla chips"].concat(["salsa", "queso", "guacamole"]);
OUTPUT
["tortilla chips", "salsa", "queso", "guacamole"]
```
-Pop
```Javascript
EXAMPLE
["Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"].pop();
OUTPUT
"Pluto"
```
-Push
```Javascript
EXAMPLE
["John", "Kate"].push(8);
OUTPUT
3
```
-Reverse
```Javascript
EXAMPLE
["a", "b", "c"].reverse();
OUTPUT
["c", "b", "a"]
```

### [Objects](https://www.javascript.com/learn/objects)
