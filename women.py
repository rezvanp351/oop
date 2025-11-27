class Woman:
    """Simple Woman class with instance attributes and behavior methods."""
    def __init__(self, name="Mina", lastname="Karimi", father="Ahmad",
                 age=20, edu="University", height=170, weight=60,
                 hobby="Painting", city="kabul", country="Afghanistan",
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

    def working(self):
        return f"{self.name} is working."

    def eating_food(self):
        return f"{self.name} is eating food."

    def sleeping(self):
        return f"{self.name} is sleeping."

    def drawing(self):
        return f"{self.name} is drawing pictures."

    def chatting_friends(self):
        return f"{self.name} is chatting with friends."

    def __repr__(self):
        return f"Woman(name={self.name!r}, age={self.age})"

    def shopping_clothes(self):
        """Return a string describing shopping for clothes."""
        return f"{self.name} is shopping for clothes."

    def put_makeup(self):
        """Return a string describing putting on makeup."""
        return f"{self.name} is putting on makeup."

    def grumble(self):
        """Return a string describing grumbling/complaining."""
        return f"{self.name} is grumbling/complaining."

    def act_coy(self):
        """Return a string describing acting coy / flirting."""
        return f"{self.name} is acting coy (flirting)."
