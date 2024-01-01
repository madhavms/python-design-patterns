from abc import ABC, abstractmethod

# Product
class Message:
    def __init__(self):
        self.text = ""
        self.sender = ""
        self.receiver = ""

    def set_text(self, text):
        self.text = text
        return self  # Return self for chaining

    def set_sender(self, sender):
        self.sender = sender
        return self  # Return self for chaining

    def set_receiver(self, receiver):
        self.receiver = receiver
        return self  # Return self for chaining

    def send(self):
        print(f"Message sent from {self.sender} to {self.receiver}: {self.text}")


# Builder Interface (not mandatory here)
class MessageBuilder(ABC):
    @abstractmethod
    def set_text(self, text):
        pass

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def send(self):
        pass


# Concrete Builder (not mandatory here)
class SimpleMessageBuilder(MessageBuilder):
    def __init__(self):
        self.message = Message()

    def set_text(self, text):
        self.message.set_text(text)
        return self

    def set_sender(self, sender):
        self.message.set_sender(sender)
        return self

    def set_receiver(self, receiver):
        self.message.set_receiver(receiver)
        return self

    def send(self):
        self.message.send()


# Client code
if __name__ == "__main__":
    # Creating a message using method chaining
    message = Message().set_sender("Alice").set_receiver("Bob").set_text("Hello, Bob!")
    message.send()
