#######################################################################
#
#    MyMetrix
#    Coded by iMaxxx (c) 2013
#    HDFreaks by Kraven
#
#
#  This plugin is licensed under the Creative Commons
#  Attribution-NonCommercial-ShareAlike 3.0 Unported License.
#  To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/
#  or send a letter to Creative Commons, 559 Nathan Abbott Way, Stanford, California 94305, USA.
#
#  Alternatively, this plugin may be distributed and executed on hardware which
#  is licensed by Dream Multimedia GmbH.
#
#
#  This plugin is NOT free software. It is open source, you are allowed to
#  modify it (if you keep the license), but it may not be commercially
#  distributed other than under the conditions noted above.
#
#
#######################################################################

from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Screens.ChoiceBox import ChoiceBox
from Screens.Console import Console
from Screens.Standby import TryQuitMainloop
from Components.ActionMap import ActionMap
from Components.AVSwitch import AVSwitch
from Components.config import config, configfile, ConfigYesNo, ConfigSubsection, getConfigListEntry, ConfigSelection, ConfigNumber, ConfigText, ConfigInteger
from Components.ConfigList import ConfigListScreen
from Components.Sources.StaticText import StaticText
from Components.Label import Label
from Components.Language import language
from os import environ, listdir, remove, rename, system
from shutil import move
from skin import parseColor
from Components.Pixmap import Pixmap
from Components.Label import Label
import gettext
from enigma import ePicLoad, getDesktop
from Tools.Directories import fileExists, resolveFilename, SCOPE_LANGUAGE, SCOPE_PLUGINS

#############################################################

lang = language.getLanguage()
environ["LANGUAGE"] = lang[:2]
gettext.bindtextdomain("enigma2", resolveFilename(SCOPE_LANGUAGE))
gettext.textdomain("enigma2")
gettext.bindtextdomain("HDFreaks", "%s%s" % (resolveFilename(SCOPE_PLUGINS), "Extensions/HDFreaks/locale/"))

def _(txt):
	t = gettext.dgettext("HDFreaks", txt)
	if t == txt:
		t = gettext.gettext(txt)
	return t

def translateBlock(block):
	for x in TranslationHelper:
		if block.__contains__(x[0]):
			block = block.replace(x[0], x[1])
	return block


#############################################################

config.plugins.HDFreaks = ConfigSubsection()
config.plugins.HDFreaks.weather_city = ConfigNumber(default="679420")
config.plugins.HDFreaks.refreshInterval = ConfigNumber(default="60")

config.plugins.HDFreaks.BackgroundColorTrans = ConfigSelection(default="22000000", choices = [
				("00000000", _("Nothing")),
				("22000000", _("Lower")),
				("44000000", _("Low")),
				("66000000", _("Middle")),
				("88000000", _("Medium")),
				("AA000000", _("High"))
				])

config.plugins.HDFreaks.SelectionBackground = ConfigSelection(default="00c3461b", choices = [
				("00f0a30a", _("Amber")),
				("001b1775", _("Blue")),
				("007d5929", _("Brown")),
				("000050ef", _("Cobalt")),
				("001ba1e2", _("Cyan")),
				("00999999", _("Grey")),
				("0070ad11", _("Green")),
				("000047d4", _("Medium Blue")),
				("001dff00", _("Neon Green")),
				("00ffff00", _("Neon Yellow")),
				("00c3461b", _("Orange")),
				("00f472d0", _("Pink")),
				("00e51400", _("Red")),
				("00647687", _("Steel")),
				("006c0aab", _("Violet")),
				("00eea00a", _("Yellow")),
				("00fffff6", _("White"))
				])
				
config.plugins.HDFreaks.Font1 = ConfigSelection(default="00fffff3", choices = [
				("00f0a30a", _("Amber")),
				("001b1775", _("Blue")),
				("007d5929", _("Brown")),
				("000050ef", _("Cobalt")),
				("001ba1e2", _("Cyan")),
				("00999999", _("Grey")),
				("0070ad11", _("Green")),
				("000047d4", _("Medium Blue")),
				("001dff00", _("Neon Green")),
				("00ffff00", _("Neon Yellow")),
				("00c3461b", _("Orange")),
				("00f472d0", _("Pink")),
				("00e51400", _("Red")),
				("00647687", _("Steel")),
				("006c0aab", _("Violet")),
				("00eea00a", _("Yellow")),
				("00fffff3", _("White"))
				])
				
config.plugins.HDFreaks.Font2 = ConfigSelection(default="00fffff4", choices = [
				("00f0a30a", _("Amber")),
				("001b1775", _("Blue")),
				("007d5929", _("Brown")),
				("000050ef", _("Cobalt")),
				("001ba1e2", _("Cyan")),
				("00999999", _("Grey")),
				("0070ad11", _("Green")),
				("000047d4", _("Medium Blue")),
				("001dff00", _("Neon Green")),
				("00ffff00", _("Neon Yellow")),
				("00c3461b", _("Orange")),
				("00f472d0", _("Pink")),
				("00e51400", _("Red")),
				("00647687", _("Steel")),
				("006c0aab", _("Violet")),
				("00eea00a", _("Yellow")),
				("00fffff4", _("White"))
				])
				
config.plugins.HDFreaks.Progress = ConfigSelection(default="00c3461b", choices = [
				("00f0a30a", _("Amber")),
				("001b1775", _("Blue")),
				("007d5929", _("Brown")),
				("000050ef", _("Cobalt")),
				("001ba1e2", _("Cyan")),
				("00999999", _("Grey")),
				("0070ad11", _("Green")),
				("000047d4", _("Medium Blue")),
				("001dff00", _("Neon Green")),
				("00ffff00", _("Neon Yellow")),
				("00c3461b", _("Orange")),
				("00f472d0", _("Pink")),
				("00e51400", _("Red")),
				("00647687", _("Steel")),
				("006c0aab", _("Violet")),
				("00eea00a", _("Yellow")),
				("00fffff6", _("White"))
				])
				
config.plugins.HDFreaks.SelFont = ConfigSelection(default="00000000", choices = [
				("00f0a30a", _("Amber")),
				("00000000", _("Black")),
				("001b1775", _("Blue")),
				("007d5929", _("Brown")),
				("000050ef", _("Cobalt")),
				("001ba1e2", _("Cyan")),
				("00999999", _("Grey")),
				("0070ad11", _("Green")),
				("000047d4", _("Medium Blue")),
				("001dff00", _("Neon Green")),
				("00ffff00", _("Neon Yellow")),
				("00c3461b", _("Orange")),
				("00f472d0", _("Pink")),
				("00e51400", _("Red")),
				("00647687", _("Steel")),
				("006c0aab", _("Violet")),
				("00eea00a", _("Yellow")),				
				("00fffff5", _("White"))
				])

config.plugins.HDFreaks.RunningText = ConfigSelection(default="movetype=none", choices = [
				("movetype=running", _("On")),
				("movetype=none", _("Off"))
				])
				
config.plugins.HDFreaks.WeatherStyle = ConfigSelection(default="weather-off", choices = [
				("weather-off", _("Off")),
				("weather-on", _("Weather infobar")),
				("weather-info", _("Weather second infobar"))
				])	
				
#######################################################################

class HDFreaks(ConfigListScreen, Screen):
	skin = """
<screen name="HDFreaks-Setup" position="0,0" size="1280,720" flags="wfNoBorder" backgroundColor="transparent">
   <eLabel font="Regular; 20" foregroundColor="#00ffffff" backgroundColor="ZeroBackground" halign="left" valign="center" position="64,662" size="148,48" text="Cancel" transparent="1" />
  <eLabel font="Regular; 20" foregroundColor="#00ffffff" backgroundColor="ZeroBackground" halign="left" valign="center" position="264,662" size="148,48" text="Save" transparent="1" />
  <eLabel font="Regular; 20" foregroundColor="#00ffffff" backgroundColor="ZeroBackground" halign="left" valign="center" position="464,662" size="148,48" text="Reboot" transparent="1" />
  <widget name="config" position="70,73" itemHeight="28" font="Regular;24" scrollbarMode="showOnDemand" size="708,574" transparent="1" />
  <eLabel position="70,12" size="708,46" text="HDFreaks - Konfigurationstool" font="Regular; 35" valign="center" halign="center" transparent="1" backgroundColor="ZeroBackground" foregroundColor="#00ffffff" name="," />
<eLabel position="891,12" size="372,46" text="Version: 2.1" font="Regular; 35" valign="center" halign="center" transparent="1" backgroundColor="ZeroBackground" foregroundColor="#00ffffff" name="," />
  <ePixmap pixmap="HDFreaks/logo.png" position="913,210" size="300,300" backgroundColor="ZeroBackground" alphatest="blend" name="," />
  <eLabel backgroundColor="ZeroBackground" position="0,0" size="1280,720" transparent="0" zPosition="-9" />
  <widget backgroundColor="ZeroBackground" font="Regular2; 34" foregroundColor="#00ffffff" position="70,12" render="Label" size="708,46" source="Title" transparent="1" halign="center" valign="center" noWrap="1" />
    <ePixmap pixmap="HDFreaks/buttons/key_red1.png" position="22,670" size="32,32" backgroundColor="ZeroBackground" alphatest="blend" />
    <ePixmap pixmap="HDFreaks/buttons/key_green1.png" position="222,670" size="32,32" backgroundColor="ZeroBackground" alphatest="blend" />
    <ePixmap pixmap="HDFreaks/buttons/key_yellow1.png" position="422,670" size="32,32" backgroundColor="ZeroBackground" alphatest="blend" />
    <ePixmap pixmap="HDFreaks/buttons/key_blue1.png" position="622,670" size="32,32" backgroundColor="ZeroBackground" alphatest="blend" />
 <widget source="global.CurrentTime" render="Label" position="1154,666" size="100,28" font="Regular;26" halign="right" backgroundColor="ZeroBackground" transparent="1" valign="center" foregroundColor="#00ffffff">
      <convert type="ClockToText">Default</convert>
    </widget>
   <ePixmap pixmap="HDFreaks/line/line1280.png" position="0,63" size="1280,2" backgroundColor="ZeroBackground" alphatest="blend" /> 
   <ePixmap pixmap="HDFreaks/line/line1280.png" position="0,653" size="1280,2" backgroundColor="ZeroBackground" alphatest="blend" />
   <ePixmap position="0,488" size="1280,234" zPosition="-9" pixmap="HDFreaks/infobar/infobar.png" transparent="1" alphatest="blend" />
   <ePixmap position="0,0" size="1280,334" zPosition="-9" pixmap="HDFreaks/infobar/infobar_oben.png" transparent="1" alphatest="blend" />
</screen> 
"""

	def __init__(self, session, args = None, picPath = None):
		self.skin_lines = []
		Screen.__init__(self, session)
		self.session = session
		self.datei = "/usr/share/enigma2/HDFreaks/skin.xml"
		self.dateiTMP = self.datei + ".tmp"
		self.daten = "/usr/lib/enigma2/python/Plugins/Extensions/HDFreaks/data/"
		self.komponente = "/usr/lib/enigma2/python/Plugins/Extensions/HDFreaks/comp/"
		self.picPath = picPath
		self.Scale = AVSwitch().getFramebufferScale()
		self.PicLoad = ePicLoad()
		self["helperimage"] = Pixmap()
		list = []

		list.append(getConfigListEntry(_(" >>>>>>>>> Weather - ID on weather.open-store.net <<<<<<<<"), ))
		list.append(getConfigListEntry(_("Weather"), config.plugins.HDFreaks.WeatherStyle))
		list.append(getConfigListEntry(_("Weather ID"), config.plugins.HDFreaks.weather_city))
		list.append(getConfigListEntry(_(" >>>>>>>>>>>>>>>>>> System Settings <<<<<<<<<<<<<<<<<"), ))
		list.append(getConfigListEntry(_("Running text"), config.plugins.HDFreaks.RunningText))
		list.append(getConfigListEntry(_("Background transparency"), config.plugins.HDFreaks.BackgroundColorTrans))
		list.append(getConfigListEntry(_(" >>>>>>>>>>>>>>>>>>> Color Settings <<<<<<<<<<<<<<<<<<"), ))
		list.append(getConfigListEntry(_("Listselection"), config.plugins.HDFreaks.SelectionBackground))
		list.append(getConfigListEntry(_("Progress-/Volumebar"), config.plugins.HDFreaks.Progress))
		list.append(getConfigListEntry(_("Primary font"), config.plugins.HDFreaks.Font1))
		list.append(getConfigListEntry(_("Secondary font"), config.plugins.HDFreaks.Font2))
		list.append(getConfigListEntry(_("Listselection font"), config.plugins.HDFreaks.SelFont))
		
		ConfigListScreen.__init__(self, list)
		self["actions"] = ActionMap(["OkCancelActions","DirectionActions", "InputActions", "ColorActions"], {"left": self.keyLeft,"down": self.keyDown,"up": self.keyUp,"right": self.keyRight,"red": self.exit,"yellow": self.reboot, "blue": self.showInfo, "green": self.save,"cancel": self.exit}, -1)
		self.onLayoutFinish.append(self.UpdatePicture)

	def GetPicturePath(self):
		try:
			returnValue = self["config"].getCurrent()[1].value
			returnValue2 = self["config"].getCurrent()[0]
                        
                        if str(returnValue2) == "":
                           if str(returnValue) == "":
                              path = ""
                           else:
                              path = ""
                        else:
                           path = "/usr/share/enigma2/HDFreaks/logo.png"
			
                        return path
		except:
			return "/usr/share/enigma2/HDFreaks/logo.png"

	def UpdatePicture(self):
		self.PicLoad.PictureData.get().append(self.DecodePicture)
		self.onLayoutFinish.append(self.ShowPicture)

	def ShowPicture(self):
		self.PicLoad.setPara([self["helperimage"].instance.size().width(),self["helperimage"].instance.size().height(),self.Scale[0],self.Scale[1],0,1,"#002C2C39"])
		self.PicLoad.startDecode(self.GetPicturePath())

	def DecodePicture(self, PicInfo = ""):
		ptr = self.PicLoad.getData()
		self["helperimage"].instance.setPixmap(ptr)

	def keyLeft(self):
		ConfigListScreen.keyLeft(self)
		self.ShowPicture()

	def keyRight(self):
		ConfigListScreen.keyRight(self)
		self.ShowPicture()

	def keyDown(self):
		self["config"].instance.moveSelection(self["config"].instance.moveDown)
		self.ShowPicture()

	def keyUp(self):
		self["config"].instance.moveSelection(self["config"].instance.moveUp)
		self.ShowPicture()

	def reboot(self):
		restartbox = self.session.openWithCallback(self.restartGUI,MessageBox,_("Do you really want to reboot now?"), MessageBox.TYPE_YESNO)
		restartbox.setTitle(_("Restart GUI"))

	def showInfo(self):
		self.session.open(MessageBox, _("Information"), MessageBox.TYPE_INFO)

	def getDataByKey(self, list, key):
		for item in list:
			if item["key"] == key:
				return item
		return list[0]

	def getFontStyleData(self, key):
		return self.getDataByKey(channelselFontStyles, key)

	def getFontSizeData(self, key):
		return self.getDataByKey(channelInfoFontSizes, key)

	def save(self):
		for x in self["config"].list:
			if len(x) > 1:
					x[1].save()
			else:
					pass

		try:
		    #global tag search and replace in all skin elements
			self.skinSearchAndReplace = []
			self.skinSearchAndReplace.append(["22000000", config.plugins.HDFreaks.BackgroundColorTrans.value])
			self.skinSearchAndReplace.append(["00c3461b", config.plugins.HDFreaks.SelectionBackground.value])
			self.skinSearchAndReplace.append(["00fffff3", config.plugins.HDFreaks.Font1.value])
			self.skinSearchAndReplace.append(["00fffff4", config.plugins.HDFreaks.Font2.value])
			self.skinSearchAndReplace.append(["00fffff5", config.plugins.HDFreaks.SelFont.value])
			self.skinSearchAndReplace.append(["00fffff6", config.plugins.HDFreaks.Progress.value])
			self.skinSearchAndReplace.append(["movetype=running", config.plugins.HDFreaks.RunningText.value])
			
			###Header XML
			self.appendSkinFile(self.daten + "header.xml")

			###Weather XML
			self.appendSkinFile(self.daten + config.plugins.HDFreaks.WeatherStyle.value + ".xml")			
			
	        ###Main XML
			self.appendSkinFile(self.daten + "main.xml")

			###Plugins XML
			self.appendSkinFile(self.daten + "plugins.xml")
			
			xFile = open(self.dateiTMP, "w")
			for xx in self.skin_lines:
				xFile.writelines(xx)
			xFile.close()

			move(self.dateiTMP, self.datei)

			#system('rm -rf ' + self.dateiTMP)
		except:
			self.session.open(MessageBox, _("Error creating Skin!"), MessageBox.TYPE_ERROR)

		configfile.save()
		restartbox = self.session.openWithCallback(self.restartGUI,MessageBox,_("GUI needs a restart to apply a new skin.\nDo you want to Restart the GUI now?"), MessageBox.TYPE_YESNO)
		restartbox.setTitle(_("Restart GUI"))

	def appendSkinFile(self, appendFileName, skinPartSearchAndReplace=None):
		"""
		add skin file to main skin content

		appendFileName:
		 xml skin-part to add

		skinPartSearchAndReplace:
		 (optional) a list of search and replace arrays. first element, search, second for replace
		"""
		skFile = open(appendFileName, "r")
		file_lines = skFile.readlines()
		skFile.close()

		tmpSearchAndReplace = []

		if skinPartSearchAndReplace is not None:
			tmpSearchAndReplace = self.skinSearchAndReplace + skinPartSearchAndReplace
		else:
			tmpSearchAndReplace = self.skinSearchAndReplace

		for skinLine in file_lines:
			for item in tmpSearchAndReplace:
				skinLine = skinLine.replace(item[0], item[1])
			self.skin_lines.append(skinLine)

	def restartGUI(self, answer):
		if answer is True:
			config.skin.primary_skin.setValue("HDFreaks/skin.xml")
			config.skin.save()
			configfile.save()
			self.session.open(TryQuitMainloop, 3)
		else:
			self.close()

	def exit(self):
		for x in self["config"].list:
			if len(x) > 1:
					x[1].cancel()
			else:
					pass
		self.close()

#############################################################

def main(session, **kwargs):
	session.open(HDFreaks,"/usr/share/enigma2/HDFreaks/logo.png")

def Plugins(**kwargs):
	return PluginDescriptor(name="HDFreaks Skin", description=_("Configuration tool for HDFreaks Skin"), where = PluginDescriptor.WHERE_PLUGINMENU, icon="plugin.png", fnc=main)
