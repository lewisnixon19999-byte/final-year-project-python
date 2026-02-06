import time
import threading

class PomodoroTimer:
    def __init__(self, onWorkStart=None, onBreakStart=None, onTick=None):
        self.workDuration = 25 * 60
        self.breakDuration = 5 * 60
        self.timeRemaining = self.workDuration
        self.isWorkSession = True
        self.isRunning = False
        self.isPaused = False
        self.timerThread = None
        self.onWorkStart = onWorkStart
        self.onBreakStart = onBreakStart
        self.onTick = onTick

    def start(self):
        if not self.isRunning:
            self.isRunning = True
            self.isPaused = False
            self.timerThread = threading.Thread(target=self.run, daemon=True)
            self.timerThread.start()
            if self.isWorkSession and self.onWorkStart:
                self.onWorkStart()

    def pause(self):
        self.isPaused = not self.isPaused

    def stop(self):
        self.isRunning = False
        self.isPaused = False

    def run(self):
        while self.isRunning:
            if not self.isPaused:
                time.sleep(1)
                self.timeRemaining -= 1

                if self.onTick:
                    self.onTick()

                if self.timeRemaining <= 0:
                    self.switchSession()

    def switchSession(self):
        self.isWorkSession = not self.isWorkSession

        if self.isWorkSession:
            self.timeRemaining = self.workDuration
            if self.onWorkStart:
                self.onWorkStart()
        else:
            self.timeRemaining = self.breakDuration
            if self.onBreakStart:
                self.onBreakStart()

    def getTimeRemaining(self):
        minutes = self.timeRemaining // 60
        seconds = self.timeRemaining % 60
        return f"{minutes:02d}:{seconds:02d}"

    def getSessionType(self):
        return "Work" if self.isWorkSession else "Break"

    def reset(self):
        self.timeRemaining = self.workDuration
        self.isWorkSession = True
        self.isPaused = False
