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
    def make_dict_with_required_keys(func):
        def format_dict(*args, **kwargs):
            new_keys = {k: k.split('__') for k in required_keys}
            input_dict = func(*args, **kwargs)
            flat_list_of_new_keys_value = [item for sublist in new_keys.values() for item in sublist]

            for k in flat_list_of_new_keys_value:
                if k not in input_dict.keys():
                    raise ValueError

            new_dict = {key: ' '.join([input_dict[v] if input_dict[v] != '' else 'Empty value' for v in value]) for
                        key, value in new_keys.items()}
            return new_dict

        return format_dict

    return make_dict_with_required_keys


def add_method_to_instance(klass):
    pass
