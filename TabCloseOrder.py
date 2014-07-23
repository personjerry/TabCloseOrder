import sublime
import sublime_plugin
import operator

class TabCloseOrder(sublime_plugin.EventListener):
    def __init__(self):
        self.viewlist = {}
        self.activewindow = None
        # print ("initialized")

    def on_activated(self, view):
        # print ("new window activated")
        # print (self.viewlist)
        self.activewindow = view.window()
        if self.activewindow.id() not in self.viewlist:
            # print ("window not in repository, adding")
            self.viewlist[self.activewindow.id()] = self.activewindow.views()
            # print (self.viewlist)

        if view in self.viewlist[self.activewindow.id()]:
            # print ("removed self from viewlist")
            self.viewlist[self.activewindow.id()].remove(view)
            # print (self.viewlist)

        # print ("adding self to viewlist")
        self.viewlist[self.activewindow.id()].append(view)
        # print (self.viewlist)

    def on_deactivated(self, view):
        # print ("closed view")
        # print (self.viewlist)
        if self.window() == None
            if view in self.viewlist[self.activewindow.id()]:
                self.viewlist[self.activewindow.id()].remove(view)
            # print (view.window())
            self.activewindow.focus_view(self.viewlist[self.activewindow.id()][-1])
