"""Get use of RAM in the system."""
from shell_executor_lib import CommandManager


class UseGetter:
    """Get use of RAM in the system."""

    def __init__(self, command_manager: CommandManager):
        """Initialize the use getter.

        Args:
            command_manager: The command manager to execute commands.
        """
        self.__command_manager = command_manager

    async def get_use(self) -> tuple[int, int]:
        """Get use of RAM in the system.

        Returns:
            The capacity and the use of the RAM in bytes.

        Raises:
            CommandError: If the exit code is not 0.
        """
        data_list: list[str] = (await self.__command_manager.execute_command(
            "/bin/free -b | /bin/awk '{ print \\$2, \\$3 }'"))[1].split(" ")

        return int(data_list[0]), int(data_list[1])
