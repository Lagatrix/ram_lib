"""Get RAM modules of the system."""
from shell_executor_lib import CommandManager

from ram_lib import RamModule


class RamGetter:
    """Get RAM modules of the system."""

    def __init__(self, command_manager: CommandManager):
        """Initialize the RAM getter.

        Args:
            command_manager: The command manager to execute commands.
        """
        self.__command_manager = command_manager

    async def get_ram(self) -> list[RamModule]:
        """Get RAM modules of the system.

        Returns:
            The list of RAM modules of the system.

        Raises:
            CommandError: If the exit code is not 0.
        """
        modules_list: list[RamModule] = []
        command_filter = "/Size:|Type:|Configured Memory Speed:|Product:|Manufacturer:|Part Number:|Locator:/{print}"
        data_list: list[str] = await self.__command_manager.execute_command(f"dmidecode -t memory | awk '"
                                                                            f"{command_filter}'", True)

        iterator: int = 0
        while iterator < len(data_list):
            size_info: list[str] = data_list[iterator].strip().split(": ")
            if size_info[0] == "Size" and size_info[1] != "No Module Installed":
                modules_list.append(RamModule(
                    size=size_info[1],
                    locator=data_list[iterator + 1].strip().split(": ")[1],
                    bank_locator=data_list[iterator + 2].strip().split(": ")[1],
                    memory_type=data_list[iterator + 3].strip().split(": ")[1],
                    manufacturer=data_list[iterator + 4].strip().split(": ")[1],
                    part_number=data_list[iterator + 5].strip().split(": ")[1],
                    configured_memory_speed=data_list[iterator + 6].strip().split(": ")[1]
                ))
                iterator += 6
            else:
                iterator += 1

        return modules_list
