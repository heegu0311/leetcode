class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        self.current += 1
        self.history = self.history[:self.current]
        self.history.append(url)

    def back(self, steps: int) -> str:
        while steps > 0 and self.current > 0:
            self.current -= 1
            steps -= 1
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current < len(self.history) - 1:
            self.current += 1
            steps -= 1
        return self.history[self.current]