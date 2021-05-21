def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def arguments(*args):
            # if type(args[0]) is type_ and len(args[0]) < max_length and (args.count(cont) for cont in contains):
            #     print(func(args[0]))
            #     return func
            # else:
            #     print('Bad idea')
            a = 0

            if len(args[0]) < len(contains):
                raise ValueError(f'Name must be more than {len(contains)} symbols')

            if type(args[0]) is type_:
                a += 1
                # print(a)
            elif a != 1:
                print('Bad type')
            if a == 1 and len(args[0]) <= max_length:
                a += 1
                # print(a)
            else:
                print('Bad length')
            sub = (args[0])
            # print(f'slogan string is {sub}')
            for text in contains:
                # print(f'first element in contains is {text}')
                # print(f'Is first element = element in slogan str {text in args[0]}')
                if text not in sub:
                    print(f'Your string non validate with this arg: {text}')
                else:
                    a += 1
                    # print(f'if true a = + 1 = {a}')
                    print(func(args[0]))
                    return func
        return arguments
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


create_slogan('05W')

create_slogan('S@SH05')

create_slogan('sdggfhj')
