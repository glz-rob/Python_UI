from textual.app import App, ComposeResult
from textual.widgets import Footer, Header


class StopwatchApp(App):
    """Stopwatch manager"""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app"""
        yield Header()
        yield Footer()

    def action_toggle_dark(self):
        """Toggles the dark mode"""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

if __name__ == "__main__":
    app = StopwatchApp()
    app.run()