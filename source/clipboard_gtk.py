#
#  Anamnesis clipboard manager.
#
#  Copyright (C) 2010  Fabio Guerra <fabiowguerra@users.sourceforge.net>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import clipboard
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk 
from gi.repository import Gdk 
import time

class Clipboard(clipboard.AbstractClipboard):

	def __init__(self):
		clipboard.AbstractClipboard.__init__(self)
		self.selection = {}
		
		# max time to wait after writing to the clipboard
		self.write_timeout = 2
		
		if self.can_read_from_selection("clipboard") or self.can_write_to_selection("clipboard"):
			self.selection["clipboard"] = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
			self.selection["clipboard"].request_text(self.callback_clipboard)
			self.selection["clipboard"].connect("owner-change", self.__owner_change_clipboard)

		if self.can_read_from_selection("primary") or self.can_write_to_selection("primary"):
			self.selection["primary"] = Gtk.Clipboard.get(Gdk.SELECTION_PRIMARY)
			self.selection["primary"].request_text(self.callback_primary)
			self.selection["primary"].connect("owner-change", self.__owner_change_primary)

		self.data = {"primary": None, "clipboard": None}

	def callback_clipboard(self, clipboard, text):
		self.data["clipboard"] = text
		self.on_data_changed("clipboard", text)

	def callback_primary(self, clipboard, text):
		self.data["primary"] = text
		self.on_data_changed("primary", text)

	def __owner_change_clipboard(self, clipboard, event, data=None):
		self.selection["clipboard"].request_text(self.callback_clipboard)
	def __owner_change_primary(self, clipboard, event, data=None):
		self.selection["primary"].request_text(self.callback_primary)

	def write_to_selection(self, type, text):
		if text and self.can_write_to_selection(type):
			self.selection[type].set_text(text, -1)
			self.selection[type].store()
			
			t0 = time.time()
			while self.data[type] != text and time.time() - t0 < self.write_timeout:
				self.__wait_Gtk()

	def __wait_Gtk(self):
		while Gtk.events_pending():
			Gtk.main_iteration()
		time.sleep(0.05)

