from tkinter_mvc_app.root.views import MainView


class Controller:
    def __init__(self, view: MainView):
        self.view = view

    def run(self):
        self.view.run_mainloop()
