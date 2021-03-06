from app import db


class Animal(db.Model):
    """
    Animal model class
    """
    __tablename__ = 'animals'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(250))
    age = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float)
    center_id = db.Column(db.Integer, db.ForeignKey('centers.id'))
    species_id = db.Column(db.String(80), db.ForeignKey('species.id'))

    def __init__(self, center_id, name, age, species_id, description=None, price=None):
        self.center_id = center_id
        self.name = name
        self.age = age
        self.species_id = species_id
        self.description = description
        self.price = price

    def __str__(self):
        return f'{self.name} - {self.id} - {self.species_id}'

    @classmethod
    def get_all_animals(cls):
        """
        :return: list of animals converted to string
        """
        return [str(animal) for animal in cls.query.all()]

    @classmethod
    def add_animal(cls, center_id, name, age, species_id, description=None, price=None):
        """
        Add new animal
        :param center_id:
        :param name:
        :param age:
        :param species_id:
        :param description:
        :param price:
        :return: autogenerated id of created animal
        """
        new_animal = cls(center_id, name, age, species_id, description, price)
        db.session.add(new_animal)
        db.session.commit()
        return new_animal.id

    @classmethod
    def get_animal(cls, animal_id):
        """
        :param animal_id:
        :return: animal with appropriate id
        """
        return cls.query.filter_by(id=animal_id).first()

    @classmethod
    def delete_animal(cls, animal_id):
        """
        :param animal_id:
        :return: deletion bool status
        """
        is_successful = cls.query.filter_by(id=animal_id).delete()
        db.session.commit()
        return bool(is_successful)

    @classmethod
    def replace_animal(cls, animal_id, center_id, name, age, species_id, description=None, price=None):
        """
        Replace animal with specified parameters
        :param animal_id:
        :param center_id:
        :param name:
        :param age:
        :param species_id:
        :param description:
        :param price:
        :return:
        """
        animal_to_replace = Animal.query.filter_by(id=animal_id).first()
        animal_to_replace.center_id = center_id
        animal_to_replace.name = name
        animal_to_replace.age = age
        animal_to_replace.species_id = species_id
        animal_to_replace.description = description
        animal_to_replace.price = price
        db.session.commit()
