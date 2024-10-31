import functools, inspect

def read_values(f):
    """Fetches information about arguments and annotations of a function.

    Returns a dict containing the retrieved information
    f -- The function to analyze, required
    """

    # Fetch the code object, since it contains most of the values we use.
    code = getattr(f, '__code__', None)
    if not inspect.iscode(code):
        t = getattr(type(f), '__name__', repr(type(f)))
        raise TypeError("'{}' object does not have a code child".format(t))

    # Fill the resulting dictionary.
    d = {}

    # These are the normal, non-variadic arguments.
    d['args'] = code.co_varnames[:code.co_argcount]

    # And these, the keyword-only arguments.
    n = code.co_argcount + code.co_kwonlyargcount
    d['keywords'] = code.co_varnames[code.co_argcount:n]

    # These are the normal, variadic arguments (*args).
    # Bitwise AND with 4 of the code.co_flags value checks for existence of a
    # variadic argument receptacle, check the dis module for more information.
    d['varargs'] = code.co_varnames[n] if code.co_flags & 4 else None

    # These are the keyword variadic arguments (**kwargs).
    # Same note as above, with 8, this time.
    n += 1 if code.co_flags & 4 else 0
    d['varkeywords'] = code.co_varnames[n] if code.co_flags & 8 else None

    # The rest is pretty straightforward
    d['defaults'] = f.__defaults__ or tuple()
    d['keyword_defaults'] = f.__kwdefaults__ or {}
    d['annotations'] = f.__annotations__ or {}

    return d

def annotated(f):
    """Applies the decorated function's annotations to its arguments.

    Returns a wrapper around the annotated function.
    f -- The function to annotate, required
    """

    fi = read_values(f)
    a = lambda name, default=(lambda x: x): fi['annotations'].get(name, default)

    @functools.wraps(f)
    def _f(*args, **kwargs):
        new_args = []

        # First, we apply annotations to non-variadic, non-keyword arguments.
        # We loop over registered arguments rather than existing ones to
        # ensure defaults, among other things.
        for i, arg in enumerate(fi['args']):
            if i < len(args):
                new_args.append(a(arg)(args[i]))
            else:
                new_args.append(a(arg)(fi['defaults'][len(args) - i]))

        # Then we apply annotations to variadic, non-keyword arguments.
        if fi['varargs'] is not None:
            new_args.extend(map(a(fi['varargs']), args[len(fi['args']):]))

        # Then we get a dictionary of all annotated default values.
        new_keywords = {k: a(k)(v) for k, v in fi['keyword_defaults'].items()}
        for k, v in kwargs.items():
            nk = k if k in fi['keywords'] else fi['varkeywords']
            print(k, nk)
            new_keywords[k] = a(nk)(v)

        return a('return')(f(*new_args, **new_keywords))

    return _f
