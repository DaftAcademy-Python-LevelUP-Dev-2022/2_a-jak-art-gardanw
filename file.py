def greeter(func):
    def aloha(*args, **kwargs):
        name = ' '.join(list(map(lambda s: s.capitalize(), func(*args, **kwargs).split(' '))))
        name = 'Aloha ' + name
        return name

    return aloha


def sums_of_str_elements_are_equal(func):
    def sums(*args, **kwargs):
        str_n = func(*args, **kwargs).split(' ')
        sum_n = list(map(sum, list(map(lambda s: [int(n) if s[0] != '-' else -int(n) for n in s if n != '-'], str_n))))
        if sum_n[0] == sum_n[1]:
            return f'{sum_n[0]} == {sum_n[1]}'
        else:
            return f'{sum_n[0]} != {sum_n[1]}'

    return sums


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass
