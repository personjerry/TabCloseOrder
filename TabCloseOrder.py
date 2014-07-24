import sublime
import sublime_plugin
import operator

class TabCloseOrder(sublime_plugin.EventListener):
    def __init__(self):
        self.viewlist = {}

    def on_activated(self, view):
        window = view.window()
        if window.id() not in self.viewlist:
            self.viewlist[window.id()] = (window, self.activewindow.views())

        if view in self.viewlist[window.id()][1]:
            self.viewlist[window.id()][1].remove(view)

        self.viewlist[window][1].append(view)

    def on_closed(self, view):
        for window_id in self.viewlist.keys:
            if view in self.viewlist[window_id][1]:
                self.viewlist[window_id][1].remove(view)
                self.viewlist[window_id][0]focus_view(self.viewlist[window_id][1][-1])
                return
