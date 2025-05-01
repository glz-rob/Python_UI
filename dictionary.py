from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, TabbedContent, TabPane, TextArea


class MyApp(App):
    """My Dictionary App"""

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode")
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for app"""
        yield Header()
        yield Footer()

        with TabbedContent():
            with TabPane("English"):
                yield TextArea("English Dictionary")
            with TabPane("Español"):
                yield TextArea("Spanish Dictionary")
            with TabPane("日本語"):
                yield TextArea("Japanese Dictionary")


if __name__ == "__main__":
    MyApp().run()
