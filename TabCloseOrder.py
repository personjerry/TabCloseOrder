import sublime
import sublime_plugin
import operator

class TabCloseOrder(sublime_plugin.EventListener):
    def __init__(self):
        self.viewlist = {}

    def on_activated(self, view):
        window = view.window()
        if window not in self.viewlist:
            self.viewlist[window] = self.activewindow.views()

        if view in self.viewlist[window]:
            self.viewlist[window].remove(view)

        self.viewlist[window].append(view)

    def on_closed(self, view):
        for window in self.viewlist.keys:
            if view in self.viewlist[window]:
                self.viewlist[window].remove(view)
                print ("Trying to focus on view " + self.viewlist[window][-1] + " from window " + window)
                window.focus_view(self.viewlist[window][-1])
                return
