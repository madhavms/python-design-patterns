"""Python Data Classes"""
from dataclasses import dataclass

@dataclass
class DataClassCard:
    """Class representing a standard playing card."""
    rank: str
    suit: str

queen_of_hearts = DataClassCard('Q', 'Hearts')
print(queen_of_hearts == DataClassCard('Q', 'Hearts')) # True
print(queen_of_hearts) # DataClassCard(rank='Q', suit='Hearts')


