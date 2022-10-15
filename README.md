


# Taktile Coding Challenge

Your challenge is to implement `fold` in the language of your choice.

## Description

`fold` is a higher order function that takes
* a sequence of type A
* a "starting" value of type B
* a function (A, B) -> B

and returns a B. E.g., the `sum` of an array is a special case of fold, where
* the sequence is an array of numbers
* the starting value is 0
* the function is `+`


You can find more information on [Wikipedia](https://en.wikipedia.org/wiki/Fold_(higher-order_function)).

## Instructions

To import and run fold in your project simply add
`from fold import fold`
