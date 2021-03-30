def outer():
    def inner():
        print('this is inner')

    print('this is outer, return inner.')
    return inner
