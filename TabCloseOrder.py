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

        if view in self.viewlist[window]:
            self.viewlist[window].remove(view)

        self.viewlist[window].append(view)

    def on_close(self, view):
    	print (view)
        window = view.window().id()
        if view in self.viewlist[window]:
            self.viewlist[window].remove(view)
        view.window().focus_view(self.viewlist[window][-1])
