#!/usr/bin/env python3
#
# This file is part of OpenMediaVault.
#
# @license   http://www.gnu.org/licenses/gpl.html GPL Version 3
# @author    Volker Theile <volker.theile@openmediavault.org>
# @copyright Copyright (c) 2009-2017 Volker Theile
#
# OpenMediaVault is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# OpenMediaVault is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with OpenMediaVault. If not, see <http://www.gnu.org/licenses/>.
import sys
import openmediavault
import openmediavault.firstaid
import openmediavault.subprocess

class Module(openmediavault.firstaid.IModule):
	@property
	def description(self):
		return "Clear local upload package repository"

	def execute(self):
		print("Clear out the local repository of uploaded package " \
			"files. Please wait ...")
		path = openmediavault.getenv("OMV_DPKGARCHIVE_DIR")
		openmediavault.subprocess.check_call(
			[ "rm", "-fv", "%s/*.deb" % path ])
		openmediavault.subprocess.check_call(
			"cd %s && apt-ftparchive packages > Packages" % path,
			shell=True)
		openmediavault.subprocess.check_call([ "apt-get", "update" ])
		return 0

if __name__ == "__main__":
	module = Module();
	sys.exit(module.execute())
