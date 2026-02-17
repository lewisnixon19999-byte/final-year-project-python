import json
import os
from datetime import datetime

class SessionLogger:
    def __init__(self, filename="sessions.json"):
        self.filename = filename
        self.sessions = []
        self.loadSessions()

    def loadSessions(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.sessions = json.load(file)
            except:
                self.sessions = []

    def logSession(self, sessionType, metrics):
        sessionData = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'type': sessionType,
            'keystrokes': metrics['keystrokes'],
            'mouseMoves': metrics['mouseMoves'],
            'clicks': metrics['clicks'],
            'engagementScore': metrics['score']
        }

        self.sessions.append(sessionData)
        self.saveSessions()

    def saveSessions(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.sessions, file, indent=4)
        except:
            pass

    def getSessions(self):
        return self.sessions

    def clearSessions(self):
        self.sessions = []
        self.saveSessions()
