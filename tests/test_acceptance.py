import unittest
import threading

from todo.app import TODOApp

class TestTODOAcceptance(unittest.TestCase):
    def test_main(self):
        app = TODOApp(io=(self.fake_input, self.fake_ouput))

        app_thread = threading.Thread(target=app.run, daemon=True)
        app_thread.start()

        welcome = self.get_output()
        self.assertEqual(welcome, (
            "Lista rzeczy do zrobienia:\n"
            "\n"
            "\n"
            "> "
        ))

        self.send_input("add kupić mleko")
        welcome = self.get_output()
        self.assertEqual(welcome, (
            "Lista rzeczy do zrobienia:\n"
            "1. kupić mleko"
            "\n"
            "> "
        ))

        self.send_input("add kupić jajka")
        welcome = self.get_output()
        self.assertEqual(welcome, (
            "Lista rzeczy do zrobienia\n"
            "1. kupić mleko"
            "2. kupic jajka"
            "\n"
            "> "
        ))

        self.send_input("del 1")
        welcome = self.get_output()
        self.assertEqual(welcome, (
            "Lista rzeczy do zrobienia\n"
            "1. kupić jajka"
            "\n"
            "> "
        ))

        self.send_input("quit")
        app_thread.join(timeout=1)
        self.assertEqual(self.get_output(), "Żegnaj!\n")
    


