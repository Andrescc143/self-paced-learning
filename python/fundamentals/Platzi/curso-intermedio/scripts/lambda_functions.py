def run():
    full_name = lambda firstName, lastName: f'Mi nombre es: {firstName.title()} {lastName.title()}'
    print(full_name('andres', 'camilo'))

if __name__ == '__main__':
    run()