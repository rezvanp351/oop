class Girl:
    """Simple Girl class with instance attributes and behavior methods."""
    def __init__(self, name="Sara", lastname="Ahmadi", father="Hassan",
                 age=16, edu="11th Grade", height=165, weight=55,
                 hobby="Reading", city="kabul", country="Afghanistan",
                 language="Dari", religion="Islam"):
        self.name = name
        self.lastname = lastname
        self.father = father
        self.age = age
        self.edu = edu
        self.height = height
        self.weight = weight
        self.hobby = hobby
        self.city = city
        self.country = country
        self.language = language
        self.religion = religion

    def going_school(self):
        return f"{self.name} is going to school."

    def reading_books(self):
        return f"{self.name} is reading books."

    def eating_food(self):
        return f"{self.name} is eating food."

    def sleeping(self):
        return f"{self.name} is sleeping."

    def drawing_pictures(self):
        return f"{self.name} is drawing pictures."

    def shopping_clothes(self):
        return f"{self.name} is shopping clothes."

    def chatting_friends(self):
        return f"{self.name} is chatting with friends."