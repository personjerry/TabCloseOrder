import sublime
import sublime_plugin
import operator

class TabCloseOrder(sublime_plugin.EventListener):
    def __init__(self):
        self.viewlist = {}

    def on_activated(self, view):
        window = view.window().id()
        if window not in self.viewlist:
            self.viewlist[window] = list(map(operator.methodcaller('id'), view.window().views()))

        if view.id() in self.viewlist[window]:
            self.viewlist[window].remove(view.id())

        self.viewlist[window].append(view.id())

    def on_close(self, view):
        for window in self.viewlist:
            if view.id() in self.viewlist[window]:
                self.viewlist[window].remove(view.id())
        for window in sublime.windows():
            if window.get_view_index(view.id()) != -1:
                result = window.get_view_index(self.viewlist[window.id()][-1])
                window.focus_view(result[0][result[1]])





