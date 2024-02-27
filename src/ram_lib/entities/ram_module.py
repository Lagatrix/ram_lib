"""This entity represents a RAM memory module."""
from dataclasses import dataclass


@dataclass
class RamModule:
    """This entity represents a RAM memory module.

    Attributes:
        size: The size of the memory module.
        locator: The locator of the memory module.
        bank_locator: The bank locator of the memory module.
        memory_type: The type of the memory module.
        manufacturer: The manufacturer of the memory module.
        part_number: The part number of the memory module.
        configured_memory_speed: The configured memory speed of the memory module.
    """
    size: str
    locator: str
    bank_locator: str
    memory_type: str
    manufacturer: str
    part_number: str
    configured_memory_speed: str
