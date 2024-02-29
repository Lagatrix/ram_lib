"""Test the RamManager class."""
import unittest
from unittest import mock

from shell_executor_lib import CommandManager

from mock_ram_lib import mock_command_executor_method, use_ram_formatted, use_ram, mock_ram_memories, \
    mock_ram_memories_entities
from ram_lib import RamManager


class TestRamManager(unittest.IsolatedAsyncioTestCase):
    """Test the RamManager class."""

    def setUp(self) -> None:
        """Set up the test."""
        self.ram_manager = RamManager(CommandManager("augusto", "augusto"))

    async def test_get_ram(self) -> None:
        """Test get ram modules correctly."""
        with mock.patch(mock_command_executor_method, return_value=mock_ram_memories):
            self.assertEqual(await self.ram_manager.get_ram(), mock_ram_memories_entities)

    async def test_get_uses(self) -> None:
        """Test get uses correctly."""
        with mock.patch(mock_command_executor_method, return_value=use_ram):
            self.assertEqual(await self.ram_manager.get_use(), use_ram_formatted)
