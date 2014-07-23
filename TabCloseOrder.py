import sublime
import sublime_plugin

class WindowCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.viewlist = []

	def onNew(view):
		self.viewlist += view

	def onActivated(view):
		if view in self.viewlist:
			self.viewlist.remove(view)

	def onClose(view):
		self.viewlist.remove(view)
		self.window.focus_view(viewlist[-1])
