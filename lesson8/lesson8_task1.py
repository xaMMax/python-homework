# def oops():
#     a = [1, 2]
#     return print(a[3])
#
#
# def some_func():
#     try:
#         oops()
#     except IndexError:
#         print(f'oops() Ooops has an index error')
#     return
#
#
# some_func()

##############################################################################################
def oops():
    a = {1: 2}
    return print(a[3])


def some_func():
    try:
        oops()
    except IndexError:
        print(f'oops() Ooops has an index error')
    return


some_func()