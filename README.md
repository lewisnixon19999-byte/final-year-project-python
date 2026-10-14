Focus Assistant — Adaptive Pomodoro Timer
A Python desktop application developed as a final-year project. Focus Assistant combines a Pomodoro-style work and break timer with engagement monitoring, session logging and duration recommendations. Its system-tray interface provides controls without requiring a main application window.
Features
The included application controller provides:
- Tray controls: start a session, pause or resume, and quit.
- Session indicators: red for work, green for breaks and yellow for automatic idle pauses.
- Status tooltip: remaining time, session type, engagement score and current work/break durations.
- Desktop notifications: work and break transitions, pauses and resumes.
- Idle checks: during work, checks engagement every 300 timer ticks and requests an automatic pause when the detector reports an idle state.
- Session logging integration: passes work-session metrics and configured durations to the logger when a break begins.
- Adaptive timing integration: requests duration adjustments based on engagement and applies recommendations supplied by the logger, including a stored recommendation at startup.
- Duplicate-instance check: uses a temporary lock file to detect an existing instance.
Technologies
- Python — application logic and coordination.
- pystray — system-tray icon, menu and notifications.
- Pillow — generates the coloured tray icons in memory.
- Python standard library — temporary files, process identification and Windows message-box integration through ctypes.
Project Structure
File	Responsibility	Included in this upload
focusAssistant.py	Entry point, tray interface and coordination of supporting components	Yes
engagementDetector.py	Provides the imported EngagementDetector class and engagement metrics	No
pomodoroTimer.py	Provides the imported PomodoroTimer class and timer operations	No
sessionLogger.py	Provides the imported SessionLogger class, logging and recommendations	No


The controller uses callbacks for timer ticks, work starts, break starts and automatic pauses. It connects those events to tray updates, notifications, engagement monitoring and logging.
Setup and Running
The current upload is incomplete and cannot run by itself. Restore the three supporting modules listed above before launching the application. Their implementations may require additional dependencies or data files that cannot be determined from the included controller.
The controller includes a Windows-specific duplicate-instance message box. Windows is the intended environment for these instructions; compatibility with other operating systems has not been verified.
From the project directory, create and activate a virtual environment:
py -m venv .venv
.venv\Scripts\Activate.ps1
Install the external dependencies visible in the included file:
python -m pip install pystray Pillow
After restoring the supporting modules and installing any dependencies they need, launch:
python focusAssistant.py
Open the system-tray menu and select Start. Use Pause / Resume to control the session and Quit to close the application. The icon may appear in Windows' hidden tray icons area.
Current Limitations
- The supplied archive contains only the application controller. Timer defaults, engagement measurement, log storage and recommendation calculations cannot be verified without the supporting modules.
- No dependency version pins or automated tests are included in the supplied archive. Runtime behaviour has not been verified from this upload.
- The lock-file check relies on file existence. If a previous process terminates without cleanup, a stale focusassistant.lock file in the system temporary directory can prevent startup. Remove it only after confirming that Focus Assistant is no longer running.
Author
Lewis Nixon — final-year project.
