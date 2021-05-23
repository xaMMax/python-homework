def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def arguments(*args):
            a = False
            sub = (args[0])
            cont = str(contains).strip(',')
###################################################################################
            if type(sub) is not type_:
                a = False
                print(f'Type ERROR, string must be {type_}')
                return a
            else:
                a = True
###################################################################################
            if max_length < len(sub):
                a = False
                print(f'Length ERROR, string must have {max_length} symbols length')
                return a
            else:
                a = True
###################################################################################
            for text in contains:
                if text not in sub:
                    print(f'ERROR: Your string non validate with this arg: {text}')
                    a = False
                    return a
                else:
                    continue
            print(func(args[0]))
####################################################################################
            return func
        return arguments
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

create_slogan('S@SH05')
create_slogan('ncvhf05n@d')
create_slogan('fcvb0v5v@')
create_slogan('05W')
create_slogan('sdggfhj')
create_slogan({'kjbfbv05@j'})
create_slogan('kjnxifui05@kjnkfngdg')
