import sublime
import sublime_plugin
import operator

class TabCloseOrder(sublime_plugin.EventListener):
    def __init__(self):
        self.view_list = {}

    def on_activated(self, view):
        window_id = view.window().id()
        if window_id not in self.view_list:
            self.view_list[window_id] = list(map(operator.methodcaller('id'), view.window().views()))

        if view.id() in self.view_list[window_id]:
            self.view_list[window_id].remove(view.id())

        self.view_list[window_id].append(view.id())

    def on_close(self, view):
        for window_id in self.view_list:
            if view.id() in self.view_list[window_id]:
                self.view_list[window_id].remove(view.id())
                sublime_window = None
                for window in sublime.windows():
                    if window.id() == window_id:
                        sublime_window = window
                result = sublime_window.get_view_index(self.view_list[window_id][-1])
                print ("attempting window ", sublime_window.id(), " with ", result[0][result[1]].id())
                sublime_window.focus_view(result[0][result[1]])





