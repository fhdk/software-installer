#!/usr/bin/env python3

import collections
import json
import subprocess
import os
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

TITLE = "Openbox Application Installer"


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title=TITLE, border_width=6)
        # set data
        self.packages = []
        self.groups = []
        self.apps = self.get_app_data("./apps.json")

        # setup main box
        self.set_default_size(600, 600)
        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.main_box)

        # create title box
        self.title_box = Gtk.Box()
        self.title_image = Gtk.Image()
        self.title_image.set_size_request(100, 100)
        self.title_image.set_from_file('./openbox.png')
        self.title_label = Gtk.Label()
        self.title_label.set_markup("<big>Openbox Application Installer</big>\n"
                                    "Select the apps you want to install\n"
                                    "Click 'Install' when ready.")
        self.title_box.pack_start(self.title_image, expand=False, fill=False, padding=0)
        self.title_box.pack_start(self.title_label, expand=True, fill=True, padding=0)

        # pack title box to main box
        self.main_box.pack_start(self.title_box, expand=False, fill=False, padding=0)

        # setup grid
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.main_box.add(self.grid)

        # setup list store model
        self.app_list_model = Gtk.ListStore(str, str, bool, str, str, str)
        for group in self.apps:
            self.groups.append(group["gid"])
            for app in group["apps"]:
                list_item = (app["name"],
                             app["description"],
                             False,
                             group["gid"],
                             app["pkg"],
                             app["icon"])
                # get install status
                status = self.app_installed(app["pkg"])
                if status:
                    list_item = (app["name"],
                                 app["description"],
                                 True,
                                 group["gid"],
                                 app["pkg"],
                                 app["icon"])
                self.app_list_model.append(list_item)

        # initial filter on first group
        self.current_filter_group = self.groups[0]

        # create a filter, feed it with the list store model
        self.group_filter = self.app_list_model.filter_new()
        self.group_filter.set_visible_func(self.group_filter_func)

        # create a treeview, using the filter, adding columns
        self.tree_view = Gtk.TreeView.new_with_model(self.group_filter)

        # model: icon
        renderer = Gtk.CellRendererPixbuf()
        column = Gtk.TreeViewColumn("", renderer, icon_name=5)
        self.tree_view.append_column(column)

        # model: name column
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Application", renderer, text=0)
        self.tree_view.append_column(column)

        # model: description column
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Description", renderer, text=1)
        self.tree_view.append_column(column)

        # model: install column
        renderer = Gtk.CellRendererToggle()
        renderer.connect("toggled", self.on_toggle)
        column = Gtk.TreeViewColumn("Installed", renderer, active=2)
        self.tree_view.append_column(column)

        # --------------------------------------  start button box ---------------------------------
        # create box with execute buttons
        self.button_box = Gtk.Box(spacing=10)
        # create filter buttons
        self.filter_buttons = list()
        for group in self.groups:
            button = Gtk.Button(label=group)
            self.filter_buttons.append(button)
            button.connect("clicked", self.on_selection_button_clicked)
            self.button_box.pack_start(button, expand=False, fill=False, padding=0)

        self.install_button = Gtk.Button(label="Install")
        self.install_button.connect("clicked", self.run_installer)

        self.button_box.pack_end(self.install_button, expand=False, fill=False, padding=0)
        # --------------------------------------  end  button box ---------------------------------

        # create a scrollable window
        self.tree_list = Gtk.ScrolledWindow()
        self.tree_list.set_vexpand(True)
        self.tree_list.add(self.tree_view)
        self.grid.attach(self.tree_list, 0, 0, 8, 10)
        # pack button box
        self.main_box.pack_end(self.button_box, expand=False, fill=False, padding=10)
        self.show_all()

    def group_filter_func(self, model, iter, data):
        if self.current_filter_group is None or self.current_filter_group == "None":
            return True
        else:
            return model[iter][3] == self.current_filter_group

    def on_selection_button_clicked(self, widget):
        self.current_filter_group = widget.get_label()
        self.group_filter.refilter()

    def on_toggle(self, widget, path):
        if self.app_list_model[path][2] == "Yes":
            return
        self.app_list_model[path][2] = not self.app_list_model[path][2]
        pkg = self.app_list_model[path][5]
        if self.app_list_model[path][2]:
            self.packages.append(pkg)
        else:
            self.packages.remove(pkg)

    def run_installer(self, widget):
        self.app_installation(self.packages)

    @staticmethod
    def app_installed(app):
        cmd = subprocess.run(["pacman", "-Q", f"{app}"],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             encoding="utf8")
        return app in cmd.stdout

    @staticmethod
    def get_app_data(filename, dictionary=True):
        """Read json data from file"""
        result = list()
        try:
            if dictionary:
                with open(filename, "rb") as infile:
                    result = json.loads(
                        infile.read().decode("utf8"),
                        object_pairs_hook=collections.OrderedDict)
            else:
                with open(filename, "r") as infile:
                    result = json.load(infile)
        except OSError:
            pass
        return result

    @staticmethod
    def app_installation(package_list):
        if not package_list:
            return
        file = "{}/.packages.txt".format(os.environ["HOME"])

        with open(file, "w") as outfile:
            for p in package_list:
                outfile.write("{} ".format(p))


win = MainWindow()
win.connect("delete-event", Gtk.main_quit)
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
