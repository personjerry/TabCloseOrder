import sublime
import sublime_plugin

class TabCloseOrder(sublime_plugin.EventListener):
    def on_load(self, view):
        print (view.file_name() + "just got loaded")

    def on_pre_save(self, view):
        print (view.file_name(), "is about to be saved")

    def on_post_save(self, view):
        print (view.file_name(), "just got saved")
        
    def on_new(self, view):
        print ("new file")

    def on_modified(self, view):
        print (view.file_name(), "modified")

    def on_activated(self, view):
        print (view.file_name(), "is now the active view")

    def on_close(self, view):
        print (view.file_name(), "is no more")

    def on_clone(self, view):
        print (view.file_name(), "just got cloned")
