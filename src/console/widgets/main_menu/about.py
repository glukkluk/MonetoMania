from textual.widgets import Link


class AboutWidget(Link):
    def on_mount(self):
        self.url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
