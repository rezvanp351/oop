class Father:
    """Simple Father class with instance attributes and behavior methods."""
    def __init__(self, name="Mohammad", lastname="Rezvani", age=45,
                 job="Engineer", city="kabul"):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.job = job
        self.city = city

    def take_out_trash(self):
        return f"{self.name} is taking out the trash."

    def work(self):
        return f"{self.name} is working at his job ({self.job})."

    def cooking(self):
        return f"{self.name} is cooking dinner."

    def eating_food(self):
        return f"{self.name} is eating food."

    def sleeping(self):
        return f"{self.name} is sleeping."

    def grumble(self):
        return f"{self.name} is grumbling."

    def __repr__(self):
        return f"Father(name={self.name!r}, job={self.job!r})"
