import pystray
from PIL import Image, ImageDraw
from engagementDetector import EngagementDetector
from pomodoroTimer import PomodoroTimer
from sessionLogger import SessionLogger

class FocusAssistant:
    def __init__(self):
        self.detector = EngagementDetector()
        self.timer = PomodoroTimer(
            onWorkStart=self.handleWorkStart,
            onBreakStart=self.handleBreakStart,
            onTick=self.updateTray
        )
        self.logger = SessionLogger()
        self.trayIcon = None
        self.isRunning = False

    def createIcon(self, color):
        image = Image.new('RGB', (64, 64), color)
        draw = ImageDraw.Draw(image)
        draw.ellipse([8, 8, 56, 56], fill=color)
        return image

    def getRedIcon(self):
        return self.createIcon((220, 50, 50))

    def getGreenIcon(self):
        return self.createIcon((50, 200, 50))

    def updateIcon(self):
        if self.trayIcon:
            if self.timer.isWorkSession:
                self.trayIcon.icon = self.getRedIcon()
            else:
                self.trayIcon.icon = self.getGreenIcon()

    def updateTray(self):
        if self.trayIcon:
            metrics = self.detector.getMetrics()
            timeRemaining = self.timer.getTimeRemaining()
            sessionType = self.timer.getSessionType()
            tooltip = f"{sessionType}: {timeRemaining}\nScore: {metrics['score']}"
            self.trayIcon.title = tooltip

    def handleWorkStart(self):
        self.updateIcon()
        self.detector.reset()
        self.detector.start()

    def handleBreakStart(self):
        self.updateIcon()
        metrics = self.detector.getMetrics()
        self.logger.logSession('Work', metrics)
        self.detector.stop()
        self.detector.reset()

    def startSession(self, icon, item):
        if not self.isRunning:
            self.isRunning = True
            self.timer.start()
            self.detector.start()

    def pauseSession(self, icon, item):
        if self.isRunning:
            self.timer.pause()
            if self.timer.isPaused:
                self.detector.stop()
            else:
                self.detector.start()

    def quitApp(self, icon, item):
        self.detector.stop()
        self.timer.stop()
        icon.stop()

    def createMenu(self):
        return pystray.Menu(
            pystray.MenuItem("Start", self.startSession),
            pystray.MenuItem("Pause", self.pauseSession),
            pystray.MenuItem("Quit", self.quitApp)
        )

    def run(self):
        self.trayIcon = pystray.Icon(
            "FocusAssistant",
            self.getRedIcon(),
            "Focus Assistant",
            self.createMenu()
        )
        self.trayIcon.run()

def main():
    app = FocusAssistant()
    app.run()

if __name__ == "__main__":
    main()
