# test_filesystem.py

import unittest
from filesystem import InMemoryFileSystem

class TestInMemoryFileSystem(unittest.TestCase):
    def setUp(self):
        self.file_system = InMemoryFileSystem()

    def test_mkdir(self):
        self.file_system.mkdir("test_directory")
        self.assertIn("/test_directory", self.file_system.file_system)

    # Add tests for other operations...

if __name__ == '__main__':
    unittest.main()
