def stop_words(words: list):
    def decorate_to_func(func):
        def arguments(*args):
            name = args[0]
            slogan = (func(name))
            for word in words:
                slogan = slogan.replace(word, '*')
            print(slogan)
            return slogan
        return arguments
    return decorate_to_func
 #.replace(words[0], '*').replace(words[1], '*')

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f'{name}, drinks pepsi in his brand new BMW!'

create_slogan('Steve')

@stop_words(['cat', 'dog', 'mary ivanna'])
def pets(name):
    return f'{name}, loves she cat Petrovich and like sleep with dog Topik'

pets('mary ivanna')