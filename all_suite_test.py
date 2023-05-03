import unittest

from unittest.loader import makeSuite

from test_cases.add_player import TestAddPlayer
from test_cases.clear_player_form import TestClearPlayerForm
from test_cases.log_out_of_the_system import TestLogOutPage
from test_cases.login_to_the_system import TestLoginPage
from test_cases.sort_players_by_age import TestSortPlayersByAgePage


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(TestAddPlayer))
    test_suite.addTest(makeSuite(TestClearPlayerForm))
    test_suite.addTest(makeSuite(TestLogOutPage))
    test_suite.addTest(makeSuite(TestSortPlayersByAgePage))

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
