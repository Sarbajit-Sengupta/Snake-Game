import importlib.util
from pathlib import Path
import sys
import types
import unittest
from unittest.mock import patch


class StateTests(unittest.TestCase):
    def test_independent_instances_and_initial_direction(self):
        spec = importlib.util.spec_from_file_location('snake_test', Path(__file__).with_name('snake.py'))
        module = importlib.util.module_from_spec(spec)
        with patch.dict(sys.modules, {'pygame': types.ModuleType('pygame')}):
            spec.loader.exec_module(module)
        first = module.snake((255, 0, 0), (5, 5))
        second = module.snake((255, 0, 0), (10, 10))
        first.addCube()
        first.turns[(5, 5)] = (1, 0)
        self.assertEqual(len(second.body), 1)
        self.assertEqual(second.turns, {})
        self.assertEqual(first.body[-1].pos, (5, 4))
        first.reset((6, 6))
        self.assertEqual((first.head.dirnx, first.head.dirny), (0, 1))
        self.assertEqual(module.cube((0, 0), -1, 0).dirnx, -1)


if __name__ == '__main__':
    unittest.main()
