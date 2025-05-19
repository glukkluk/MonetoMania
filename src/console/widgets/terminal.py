from textual.containers import Grid


class BaseTerminal(Grid):
    DEFAULT_CSS = """
    BaseTerminal {
        height: 45;
        width: 100;
    }
    """
