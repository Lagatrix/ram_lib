"""Test the RAM getter."""
import unittest
from unittest import mock

from shell_executor_lib import CommandManager

from mock_ram_lib import mock_command_executor_method
from mock_ram_lib import mock_ram_memories_entities, mock_ram_memories
from ram_lib.managers.getters import RamGetter


class TestRamGetter(unittest.IsolatedAsyncioTestCase):
    """Test the RAM getter."""

    def setUp(self) -> None:
        """Set up the test."""
        self.ram_getter = RamGetter(CommandManager("augusto", "augusto"))

    async def test_get_ram(self) -> None:
        """Test get ram modules correctly."""
        with mock.patch(mock_command_executor_method, return_value=mock_ram_memories):
            self.assertEqual(await self.ram_getter.get_ram(), mock_ram_memories_entities)
