import sublime
import sublime_plugin
import operator
import copy

class TabCloseOrder(sublime_plugin.EventListener):
    def __init__(self):
        self.view_list = {}
        self.backup_list = {}

    def on_activated(self, view):
        self.backup_list = copy.deepcopy(self.view_list)
        window_id = view.window().id()
        if window_id not in self.view_list:
            self.view_list[window_id] = list(map(operator.methodcaller('id'), view.window().views()))

        if view.id() in self.view_list[window_id]:
            self.view_list[window_id].remove(view.id())

        self.view_list[window_id].append(view.id())

    def on_close(self, view):
        self.view_list = self.backup_list
        for window_id in self.view_list:
            if view.id() in self.view_list[window_id]:
                self.view_list[window_id].remove(view.id())
                sublime_window = None
                for window in sublime.windows():
                    if window.id() == window_id:
                        sublime_window = window
                        break
                sublime_view = None
                for potential_view in sublime_window.views():
                    if potential_view.id() == self.view_list[window_id][-1]:
                        sublime_view = potential_view
                        break
                if sublime_window and sublime_view:
                    sublime_window.focus_view(sublime_view)





