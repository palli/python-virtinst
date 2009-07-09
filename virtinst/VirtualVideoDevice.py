#
# Copyright 2009  Red Hat, Inc.
# Cole Robinson <crobinso@redhat.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free  Software Foundation; either version 2 of the License, or
# (at your option)  any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA.

import VirtualDevice

class VirtualVideoDevice(VirtualDevice.VirtualDevice):

    _virtual_device_type = VirtualDevice.VirtualDevice.VIRTUAL_DEV_VIDEO

    # Default models list
    _model_types = [ "cirrus", "vga", "vmvga", "xen" ]

    def __init__(self, conn):
        VirtualDevice.VirtualDevice.__init__(self, conn=conn)

        self._model_type    = None
        self._vram          = None
        self._heads         = None

    def get_model_types(self):
        return self._model_types[:]
    model_types = property(get_model_types)

    def get_model_type(self):
        return self._model_type
    def set_model_type(self, val):
        self._model_type = val
    model_type = property(get_model_type, set_model_type)

    def get_vram(self):
        return self._vram
    def set_vram(self, val):
        self._vram = val
    vram = property(get_vram, set_vram)

    def get_heads(self):
        return self._heads
    def set_heads(self, val):
        self._heads = val
    heads = property(get_heads, set_heads)

    def get_xml_config(self):
        model_xml = "      <model"
        if self.model_type:
            model_xml += " type='%s'" % self.model_type
        if self.vram:
            model_xml += " vram='%s'" % self.vram
        if self.heads:
            model_xml += " heads='%s'" % self.heads
        model_xml += "/>\n"

        xml = ("    <video>\n" +
               model_xml +
               "    </video>")
        return xml
