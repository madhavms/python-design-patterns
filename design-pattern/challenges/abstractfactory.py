from abc import ABC, abstractmethod

class CarInterior(ABC):
    @abstractmethod
    def set_seats(self):
        pass

    @abstractmethod
    def set_dashboard(self):
        pass

class CarExterior(ABC):
    @abstractmethod
    def set_body_type(self):
        pass

    @abstractmethod
    def set_paint(self):
        pass

    @abstractmethod
    def set_wheels(self):
        pass

class SedanInterior(CarInterior):
    def set_seats(self):
        return "Setting seats for Sedan"

    def set_dashboard(self):
        return "Setting dashboard for Sedan"

class SedanExterior(CarExterior):
    def set_body_type(self):
        return "Setting body type for Sedan"

    def set_paint(self):
        return "Applying paint for Sedan"

    def set_wheels(self):
        return "Attaching wheels for Sedan"

class SUVInterior(CarInterior):
    def set_seats(self):
        return "Setting seats for SUV"

    def set_dashboard(self):
        return "Setting dashboard for SUV"

class SUVExterior(CarExterior):
    def set_body_type(self):
        return "Setting body type for SUV"

    def set_paint(self):
        return "Applying paint for SUV"

    def set_wheels(self):
        return "Attaching wheels for SUV"

class CarFactory(ABC):
    @abstractmethod
    def create_interior(self) -> CarInterior:
        pass

    @abstractmethod
    def create_exterior(self) -> CarExterior:
        pass

class SedanFactory(CarFactory):
    def create_interior(self) -> CarInterior:
        return SedanInterior()

    def create_exterior(self) -> CarExterior:
        return SedanExterior()

class SUVFactory(CarFactory):
    def create_interior(self) -> CarInterior:
        return SUVInterior()

    def create_exterior(self) -> CarExterior:
        return SUVExterior()
    

# Client
def get_car(factory: CarFactory):
    interior = factory.create_interior()
    exterior = factory.create_exterior()

    return interior, exterior

# Testing the implementation
if __name__ == "__main__":
    sedan_factory = SedanFactory()
    sedan_interior, sedan_exterior = get_car(sedan_factory)

    print(sedan_interior.set_seats())  # Output: Setting seats for Sedan
    print(sedan_interior.set_dashboard())  # Output: Setting dashboard for Sedan
    print(sedan_exterior.set_body_type())  # Output: Setting body type for Sedan
    print(sedan_exterior.set_paint())  # Output: Applying paint for Sedan
    print(sedan_exterior.set_wheels())  # Output: Attaching wheels for Sedan

    suv_factory = SUVFactory()
    suv_interior, suv_exterior = get_car(suv_factory)

    print(suv_interior.set_seats())  # Output: Setting seats for SUV
    print(suv_interior.set_dashboard())  # Output: Setting dashboard for SUV
    print(suv_exterior.set_body_type())  # Output: Setting body type for SUV
    print(suv_exterior.set_paint())  # Output: Applying paint for SUV
    print(suv_exterior.set_wheels())  # Output: Attaching wheels for SUV
