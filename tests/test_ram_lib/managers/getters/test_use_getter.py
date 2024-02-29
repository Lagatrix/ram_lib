"""Test the UseGetter class."""
import unittest
from unittest import mock

from shell_executor_lib import CommandManager

from mock_ram_lib import mock_command_executor_method, use_ram, use_ram_formatted
from ram_lib.managers.getters import UseGetter


class TestUseGetter(unittest.IsolatedAsyncioTestCase):
    """Test the UseGetter class."""

    def setUp(self) -> None:
        """Set up the test."""
        self.use_getter = UseGetter(CommandManager("augusto", "augusto"))

    async def test_get_uses(self) -> None:
        """Test get uses correctly."""
        with mock.patch(mock_command_executor_method, return_value=use_ram):
            self.assertEqual(await self.use_getter.get_use(), use_ram_formatted)
