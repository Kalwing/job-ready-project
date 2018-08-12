# Note

## Chapter 1
**PCAP**:   Primitive Combination Abstraction Pattern

## Chapter 3
### Python environments:
`__builtin__`
Module: Each module is created as a different environments, child of `__builtin__`
Procedure: Child of the module or the procedure that is calling it


When modifying a global var inside a procedure, you need to use `global`
```python
a = 3
def incr():
    global a
    a = a +1
```

## Chapter 4
### Definition of a State Machine
**S**: The set of state
**I**: The input vocabulary
**O**: The Output vocabulary
**n(It, St) -> St+1**: next-state function
**o(It, St) -> Ot**: output function
**s0**: initial state
