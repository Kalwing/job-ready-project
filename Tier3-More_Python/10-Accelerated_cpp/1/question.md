1. Those are both valid. `hello + ", world" + "!";` is processed as `(std::string + char[]) + char[]`
2. Those are invalid: `"Hello" + ", world" + exclam;` is processed as `(char[] + char[]) + std::string` but you cannot add arrays of chars.
3. The program is valid. It writes on std::cout
```a string
another string```
4. This one is fine too. Which means that variable can be redefined in inferior scopes. Changing `}}` to `};}` work. `;` is the void instruction.
5. It's not valid as `x` is declared in an inferior scope than the one where it is used. for a proper version see  [./5.cpp](5.cpp)
