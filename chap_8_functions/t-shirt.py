def make_shirt(size='large', message='I love Python'):
    """Describe a T-shirt."""
    print(f'This is a {size} shirt that says, "{message}" ')

make_shirt('small', 'Hello World')
make_shirt(size='medium', message='I need coffee today')
make_shirt()
make_shirt(size='medium')
make_shirt(size='small', message='eat, sleep, sleep more')