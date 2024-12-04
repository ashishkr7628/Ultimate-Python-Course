class Employee:
    a = 10

    @classmethod
    def show(cls):
        print(f"The value of a is {cls.a}")


a = Employee()
a.a = 45  # This does not affect the class variable 'a'
a.show()  # Outputs: The value of a is 10
