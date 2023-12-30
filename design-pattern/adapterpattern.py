from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET


# Adaptee: The existing service that works with XML data
class XMLUserService:
    def get_user_info_as_xml(self) -> str:
        # Assume data is retrieved from an XML file
        with open(
            "/Users/madhavmanohar/Desktop/python-clean-code/user_info.xml",
            "r",
            encoding="utf-8",
        ) as file:
            return file.read()


# Target: The interface expected by the client code (in this case, a common User format)
class User(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_email(self) -> str:
        pass


# Adapter: Adapts the XMLUserService to work with the User interface
class JSONUserAdapter(User):
    def __init__(self, xml_user_service: XMLUserService):
        self.xml_user_service = xml_user_service

    def get_name(self) -> str:
        xml_data = self.xml_user_service.get_user_info_as_xml()
        root = ET.fromstring(xml_data)
        return root.find("name").text

    def get_email(self) -> str:
        xml_data = self.xml_user_service.get_user_info_as_xml()
        root = ET.fromstring(xml_data)
        return root.find("email").text


# Client code: Utilizing the adapted User interface
def display_user_info(user: User) -> None:
    print(f"Name: {user.get_name()}")
    print(f"Email: {user.get_email()}")


if __name__ == "__main__":
    # Existing XML-based service
    xml_service = XMLUserService()

    # Adapt the XML service to work with the User interface
    adapted_user = JSONUserAdapter(xml_service)

    # Utilize the adapted interface to display user information
    print("Displaying user info using the adapted interface:")
    display_user_info(adapted_user)
