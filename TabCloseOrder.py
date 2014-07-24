import sublime
import sublime_plugin
import operator

class TabCloseOrder(sublime_plugin.EventListener):
    def __init__(self):
        self.viewlist = {}
        self.closedview = -1

    def on_activated(self, view):
        window = view.window().id()
        if window not in self.viewlist:
            self.viewlist[window] = list(map(operator.methodcaller('id'), view.window().views()))

        if self.closedview >= 0 and self.closedview in self.viewlist[window]:
            self.closedview = -1
            for v in view.window().views():
                if v.id() == self.viewlist[window][-1]:
                    view.window().focus_view(v)

        if view.id() in self.viewlist[window]:
            self.viewlist[window].remove(view.id())

        self.viewlist[window].append(view.id())

    def on_close(self, view):
        self.closedview = view.id()