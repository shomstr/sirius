Annotated
=========
Annotated provides a decorator that flags a function's annotations as useful, callable expressions. Each annotation will be called with its corresponding argument as first parameter, and the result will replace that argument.

If no annotation was specified for this particular argument, it will behave as if `lambda x: x` had been used as annotation.

`@annotated` Decorator
----------------------
The `@annotated` decorator is meant to decorate functions, or other objects with a `__code__` attribute (a class is **not** one). It indicates that the function decorated has "active" annotations, for example:

```python
from annotated import annotated

@annotated
def hello(name: str):
    print('Hello, ' + name + '!')

hello('world')
# "Hello, world!"
hello(None)
# "Hello, None!"
```

Albeit a bad example (one would rather use `str.format` or the `%` notation to include a value in a string), this illustrates the behaviour of an `@annotated` function.

Used this way, `@annotated` ensures that the `name` argument of the `hello` function is **always** a character string.

`@annotated` also respects default values, and applies annotations to them. Thus, if we were to rewrite `hello` such as:

```python
from annotated import annotated

@annotated
def hello(name: str='world'):
    print('Hello, ' + name + '!')

hello()
# "Hello, world!"
```

The default value would be honored, as well as any non-defaults.

It should be noted that `@annotated` supports both return annotations (`->`), keyword argument annotations and `*`/`**` annotations.

Using `@annotated` on an incompatible (`__code__`-less) object will result in a `TypeError` exception.


