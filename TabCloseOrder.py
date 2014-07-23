import sublime
import sublime_plugin

class TabCloseOrder(sublime_plugin.EventListener):
    def onLoad(self, view):
        print view.fileName(), "just got loaded"

    def onPreSave(self, view):
        print view.fileName(), "is about to be saved"

    def onPostSave(self, view):
        print view.fileName(), "just got saved"
        
    def onNew(self, view):
        print "new file"

    def onModified(self, view):
        print view.fileName(), "modified"

    def onActivated(self, view):
        print view.fileName(), "is now the active view"

    def onClose(self, view):
        print view.fileName(), "is no more"

    def onClone(self, view):
        print view.fileName(), "just got cloned"
