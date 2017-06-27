#Symbol Level Backwards: An Add-on for nvda that does <Insert thing here>
#Copyright (C) 2017 Hrvoje Katic
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

import config
import ui
import characterProcessing
from globalCommands import SCRCAT_SPEECH
import globalPluginHandler
import addonHandler
addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def script_cycleSpeechSymbolLevelBackwards(self,gesture):
		curLevel = config.conf["speech"]["symbolLevel"]
		for level in reversed(characterProcessing.CONFIGURABLE_SPEECH_SYMBOL_LEVELS):
			if level < curLevel:
				break
		else:
			level = characterProcessing.SYMLVL_ALL
		name = characterProcessing.SPEECH_SYMBOL_LEVEL_LABELS[level]
		config.conf["speech"]["symbolLevel"] = level
		# Translators: Reported when the user cycles through speech symbol levels
		# which determine what symbols are spoken.
		# %s will be replaced with the symbol level; e.g. none, some, most and all.
		ui.message(_("Symbol level %s") % name)
	# Translators: Input help mode message for cycle speech symbol level backwards command.
	script_cycleSpeechSymbolLevelBackwards.__doc__=_("Cycles backwards through speech symbol levels which determine what symbols are spoken")
	script_cycleSpeechSymbolLevelBackwards.category=SCRCAT_SPEECH

	__gestures = {
		"kb:NVDA+shift+p": "cycleSpeechSymbolLevelBackwards",
	}
