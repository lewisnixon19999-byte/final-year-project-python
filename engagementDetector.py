from pynput import keyboard, mouse

class EngagementDetector:
    def __init__(self):
        self.keystrokeCount = 0
        self.mouseMoveCount = 0
        self.clickCount = 0
        self.keyboardListener = None
        self.mouseListener = None

    def start(self):
        self.keyboardListener = keyboard.Listener(on_press=self.handleKeyPress)
        self.mouseListener = mouse.Listener(on_move=self.handleMouseMove, on_click=self.handleClick)
        self.keyboardListener.start()
        self.mouseListener.start()

    def stop(self):
        if self.keyboardListener:
            self.keyboardListener.stop()
        if self.mouseListener:
            self.mouseListener.stop()

    def handleKeyPress(self, key):
        self.keystrokeCount += 1

    def handleMouseMove(self, x, y):
        self.mouseMoveCount += 1

    def handleClick(self, x, y, button, pressed):
        if pressed:
            self.clickCount += 1

    def calculateScore(self):
        score = (self.keystrokeCount * 0.6) + (self.mouseMoveCount * 0.2) + (self.clickCount * 0.2)
        return round(score, 2)

    def getMetrics(self):
        return {
            'keystrokes': self.keystrokeCount,
            'mouseMoves': self.mouseMoveCount,
            'clicks': self.clickCount,
            'score': self.calculateScore()
        }

    def reset(self):
        self.keystrokeCount = 0
        self.mouseMoveCount = 0
        self.clickCount = 0
