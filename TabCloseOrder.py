import sublime
import sublime_plugin

class TabCloseOrder(sublime_plugin.EventListener):
    def __init__(self):
        self.viewlist = {}
        self.activewindow = None

    def on_activated(self, view):
        self.activewindow = view.window()
        if self.activewindow.id() not in self.viewlist:
            self.viewlist[self.activewindow.id()] = self.activewindow.views()

        if view in self.viewlist[self.activewindow.id()]:
            self.viewlist[self.activewindow.id()].remove(view)

        self.viewlist[self.activewindow.id()].append(view)

    def on_close(self, view):
        if view in self.viewlist[self.activewindow.id()]:
            self.viewlist[self.activewindow.id()].remove(view)
        sublime.setTimeout(self.focus, 0.100)

    def focus(self):
        self.activewindow.focus_view(self.viewlist[self.activewindow.id()][-1])
        self.activewindow = None

