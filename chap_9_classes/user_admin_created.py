import user_admin_privileges as uap

def main():
    admin_1 = uap.Admin(
            'lina', 'thomas', 1985, 'lthomas@gmail.com',
            'thomc@t'
    )
    admin_1.greet_user()
    admin_1.privileges.show_privileges()

if __name__ == '__main__':
    main()
