class Boy:
    """Simple Boy class with instance attributes and behavior methods."""
    def __init__(self, name="Aref", lastname="Rezvan Panah", father="Mohammad",
                 age=17, edu="12th Grade", height=180, weight=75,
                 hobby="Programming", city="kabul", country="Afghanistan",
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

    def playing_football(self):
        return f"{self.name} is playing football."

    def eating_food(self):
        return f"{self.name} is eating food."

    def sleeping(self):
        return f"{self.name} is sleeping."

    def coding_javaScript(self):
        return f"{self.name} is coding JavaScript."
    