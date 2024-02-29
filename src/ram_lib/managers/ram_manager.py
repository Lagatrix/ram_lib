"""Manage RAM of unix system."""
from shell_executor_lib import CommandManager

from ram_lib import RamModule
from ram_lib.managers.getters import RamGetter, UseGetter


class RamManager:
    """Manage RAM of unix system."""

    def __init__(self, command_manager: CommandManager):
        """Initialize the RAM manager.

        Args:
            command_manager: The command manager to execute commands.
        """
        self.__ram_getter = RamGetter(command_manager)
        self.__use_getter = UseGetter(command_manager)

    async def get_ram(self) -> list[RamModule]:
        """Get RAM modules of the system.

        Returns:
            The list of RAM modules of the system.

        Raises:
            CommandError: If the exit code is not 0.
        """
        return await self.__ram_getter.get_ram()

    async def get_use(self) -> tuple[int, int]:
        """Get use of RAM in the system.

        Returns:
            The capacity and the use of the RAM in bytes.

        Raises:
            CommandError: If the exit code is not 0.
        """
        return await self.__use_getter.get_use()
