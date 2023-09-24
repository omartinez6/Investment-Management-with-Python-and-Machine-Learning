# Module to use as an example

def greet(name, say='Hello'):
    '''
    Function that returns a personalized greeting.

    Parameters
    ----------
    name: str
        The name of the person to greet.
    say: str, optional
        How the greeting will start, by default is 'Hello'.

    Returns
    -------
    greeting: str
        The personalized greeting in the form of say + name.

    Raises
    ------
    None

    Examples
    --------
    >>> greet('John')
    'Hello John'
    >>> greet('Emily', say='Hi')
    'Hi Emily'
    '''
    greeting = f'{say} {name}! Changed, second version'
    return greeting