def greeter(func):
    def aloha(*args, **kwargs):
        name = ' '.join(list(map(lambda s: s.capitalize(), func(*args, **kwargs).split(' '))))
        name = 'Aloha ' + name
        return name
    return aloha


def sums_of_str_elements_are_equal(func):
    pass


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass
