import subprocess

class StartButton:
    def __init__(self, button):
        self.button = button
        self.button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        mark.execute_command(["waydroid",  "session", "start"])
class StopButton:
    def __init__(self, button):
        self.button = button
        self.button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        mark.execute_command(["waydroid",  "session", "stop"])
        print("Hooray!")
class RestartButton:
    def __init__(self, button):
        self.button = button
        self.button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        mark.execute_command(["waydroid",  "session", "stop"])
class FreezeButton:
    def __init__(self, button):

        self.button = button
        self.button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        if self.button.isChecked():
            mark.execute_command(["waydroid",  "container", "freeze"])
        else:
            mark.execute_command(["waydroid",  "session", "unfreeze"])
class mark:
    def execute_command(command):
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')