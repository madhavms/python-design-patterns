from abc import ABC, abstractmethod

# Abstract products
class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass

class Sofa(ABC):
    @abstractmethod
    def lie_on(self):
        pass

class CoffeeTable(ABC):
    @abstractmethod
    def place_on(self):
        pass

class DiningTable(ABC):
    @abstractmethod
    def dine_on(self):
        pass

# Concrete Products
class ArtDecoChair(Chair):
    def sit_on(self):
        return "Sitting on an Art Deco chair"

class VictorianChair(Chair):
    def sit_on(self):
        return "Sitting on a Victorian chair"

class ModernChair(Chair):
    def sit_on(self):
        return "Sitting on a Modern chair"

class ArtDecoSofa(Sofa):
    def lie_on(self):
        return "Lying on an Art Deco sofa"

class VictorianSofa(Sofa):
    def lie_on(self):
        return "Lying on a Victorian sofa"

class ModernSofa(Sofa):
    def lie_on(self):
        return "Lying on a Modern sofa"

class ArtDecoCoffeeTable(CoffeeTable):
    def place_on(self):
        return "Placing things on an Art Deco coffee table"

class VictorianCoffeeTable(CoffeeTable):
    def place_on(self):
        return "Placing things on a Victorian coffee table"

class ModernCoffeeTable(CoffeeTable):
    def place_on(self):
        return "Placing things on a Modern coffee table"


# Abstract Factory
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass

    @abstractmethod
    def create_coffee_table(self) -> CoffeeTable:
        pass
    
# Concrete Factories for each style
class ArtDecoFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ArtDecoChair()

    def create_sofa(self) -> Sofa:
        return ArtDecoSofa()

    def create_coffee_table(self) -> CoffeeTable:
        return ArtDecoCoffeeTable()

class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()

    def create_coffee_table(self) -> CoffeeTable:
        return VictorianCoffeeTable()

class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_sofa(self) -> Sofa:
        return ModernSofa()

    def create_coffee_table(self) -> CoffeeTable:
        return ModernCoffeeTable()
    

# Client
def get_furniture(factory: FurnitureFactory):
    chair = factory.create_chair()
    sofa = factory.create_sofa()
    coffee_table = factory.create_coffee_table()

    return chair, sofa, coffee_table

# Client code
if __name__ == "__main__":
    print("Client: Using Art Deco furniture:")
    art_deco_factory = ArtDecoFurnitureFactory()
    art_deco_chair, art_deco_sofa, art_deco_coffee_table = get_furniture(art_deco_factory)
    print(art_deco_chair.sit_on())
    print(art_deco_sofa.lie_on())
    print(art_deco_coffee_table.place_on())

    print("\n")

    print("Client: Using Victorian furniture:")
    victorian_factory = VictorianFurnitureFactory()
    victorian_chair, victorian_sofa, victorian_coffee_table = get_furniture(victorian_factory)
    print(victorian_chair.sit_on())
    print(victorian_sofa.lie_on())
    print(victorian_coffee_table.place_on())

    print("\n")

    print("Client: Using Modern furniture:")
    modern_factory = ModernFurnitureFactory()
    modern_chair, modern_sofa, modern_coffee_table = get_furniture(modern_factory)
    print(modern_chair.sit_on())
    print(modern_sofa.lie_on())
    print(modern_coffee_table.place_on())