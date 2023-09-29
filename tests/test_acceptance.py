import unittest
import threading

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

        self.send_input("quit")
        app_thread.join(timeout=1)
        self.assertEqual(self.get_output(), "Żegnaj!\n")


