"""@author: Kartikei Mittal

Unit tests file for current project."""

# Python module(s)
import sys
import unittest
import HtmlTestRunner

# Utility methods
from utility import update_readme, clear_trailling_space


class DummyTests(unittest.TestCase):
    # Tests for project Connect-N.
    def setUp(self):
        """setUp"""
        pass

    def tearDown(self):
        """tearDown"""
        pass

    def test_dummy(self):
        """Dummy Test"""
        self.assertEqual(2 + 2, 4)


def main():
    # Seprating coustom arguments from normal unittest argument
    argv_tpl = (
        "--update-readme",
        "--clear-trailling-space",
    )  # Expected coustom arguments
    del_lst = []
    coustom_argv = [sys.argv[0]]
    for i, argv in enumerate(sys.argv):
        if argv in argv_tpl:
            del_lst.append(i)
            coustom_argv.append(argv)
    del_lst.reverse()  # Faster deletion when deleting higher index element first
    for i in del_lst:
        del sys.argv[i]

    testRunner = HtmlTestRunner.HTMLTestRunner(
        verbosity=2,
        descriptions=False,
        open_in_browser=False,
        combine_reports=True,
        report_name="test_result",
        add_timestamp=False,
    )
    unittest.main(testRunner=testRunner, exit=False)

    if "--update-readme" in coustom_argv:
        update_readme()
    if "--clear-trailling-space" in coustom_argv:
        clear_trailling_space()


if __name__ == "__main__":
    main()
