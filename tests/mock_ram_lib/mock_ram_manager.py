"""Mocks of the RAMs memories."""
from ram_lib import RamModule

mock_ram_memories = [
    "   Error Correction Type: None",
    "   Size: 8 GB",
    "   Locator: ChannelA-DIMM0",
    "   Bank Locator: BANK 0",
    "   Type: DDR4",
    "   Manufacturer: 029E",
    "   Part Number: CMV8GX4M1A2133C15",
    "   Configured Memory Speed: 2133 MT/s",
    "   Size: No Module Installed",
    "   Locator: ChannelA-DIMM1",
    "   Bank Locator: BANK 1",
    "   Type: Unknown",
    "   Size: 8 GB",
    "   Locator: ChannelB-DIMM0",
    "   Bank Locator: BANK 2",
    "   Type: DDR4",
    "   Manufacturer: Kingston",
    "   Part Number: 9905622-058.A00G",
    "   Configured Memory Speed: 2133 MT/s",
    "   Size: No Module Installed",
    "   Locator: ChannelB-DIMM1",
    "   Bank Locator: BANK 3",
    "   Type: Unknown"
]

mock_ram_memories_entities = [
    RamModule(
        size="8 GB",
        locator="ChannelA-DIMM0",
        bank_locator="BANK 0",
        memory_type="DDR4",
        manufacturer="029E",
        part_number="CMV8GX4M1A2133C15",
        configured_memory_speed="2133 MT/s"
    ),
    RamModule(
        size="8 GB",
        locator="ChannelB-DIMM0",
        bank_locator="BANK 2",
        memory_type="DDR4",
        manufacturer="Kingston",
        part_number="9905622-058.A00G",
        configured_memory_speed="2133 MT/s"
    ),
]

use_ram = ["used free", "16725721088 6934065152", "1023406080 0"]

use_ram_formatted = (16725721088, 6934065152)
