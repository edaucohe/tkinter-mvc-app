from root.controller import Controller
from root.views import MainView


def main():
    view = MainView()
    controller = Controller(view=view)
    controller.run()


if __name__ == '__main__':
    main()
