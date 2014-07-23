import sublime
import sublime_plugin

class TabCloseOrder(sublime_plugin.EventListener):
	def __init__(self):
		self.viewlist = {}

    def on_activated(self, view):
    	window = view.window().id()
        if window not in self.viewlist:
        	self.viewlist[window] = view.window().views().map(operator.methodcaller('id'))

        if view in self.viewlist[window]:
        	self.viewlist[window].remove(view)

    	self.viewlist[window].append(view)

    def on_close(self, view):
    	window = view.window().id()
        if view in self.viewlist[window]:
        	self.viewlist[window].remove(view)
    	view.window().focus_view(self.viewlist[window][-1])
