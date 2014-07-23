import sublime
import sublime_plugin

class WindowCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.viewlist = []

	def on_new(view):
		self.viewlist += view

	def on_activated(view):
		if view in self.viewlist:
			self.viewlist.remove(view)

	def on_close(view):
		self.viewlist.remove(view)
		self.window.focus_view(viewlist[-1])
