import electric_car as ec

def main():
    my_leaf = ec.ElectricCar('nissan', 'leaf', 2024)
    print(my_leaf.get_descriptive_name())
    my_leaf.battery.describe_battery()
    my_leaf.battery.get_range()

if __name__ == '__main__':
    main()
