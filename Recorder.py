#!/usr/bin/env python

# std
import os
import time
from threading import Thread

# lib
import wx
import youtube_dl
# own
import noname as RecorderGUI
RecorderGUI.true = True # hotfix for shitty wxFormBuilder

########
# util #
########

def video_info(ydl, url):
	result = None
	
	with ydl:
		try:
			result = ydl.extract_info(url, download=False)
		except:
			result = None
	
	return result

def set_stream_info(self, status, desc, starttime, online):
	# set stream status
	if online:
		self.textmsg_isonline.SetValue(status)
		self.textmsg_isonline.SetDefaultStyle(wx.TextAttr(wx.Colour(40, 213, 40)))
		self.textmsg_isonline.AppendText(" (online)")
		self.textmsg_isonline.SetDefaultStyle(wx.TextAttr(wx.NullColour))
	else:
		self.textmsg_isonline.SetValue("")
		self.textmsg_isonline.SetDefaultStyle(wx.TextAttr(wx.Colour(210, 30, 30)))
		self.textmsg_isonline.AppendText("offline")
		self.textmsg_isonline.SetDefaultStyle(wx.TextAttr(wx.NullColour))

	self.textmsg_desc.SetValue(desc)
	self.textmsg_starttime.SetValue(starttime)

def fetch_stream_status(self, url):
	info = video_info(self.YDL, url)
	
	if (info is None):
		set_stream_info(self, "offline", "", "", False)
		return False
	else:
		ftime = ""
		try:
			ftime = time.strftime('%H:%M Uhr, %d.%m.%Y', time.localtime(info['timestamp']))
		except:
			ftime = "--:-- Uhr"
		
		set_stream_info(self,
			status=info['uploader'],
			desc=info['description'],
			starttime=ftime,
			online=True
		)
	return True

def fetch_stream_status_parallel(self, url):
	self.THREAD_FETCHINFO = Thread(target = fetch_stream_status, args = (self, url))
	self.THREAD_FETCHINFO.start()

def ydlhook_progress(dl):
	status = dl['status']

	if status == 'finished':
		print('downloaded ' + os.path.abspath(dl['filename']))
	elif status == 'downloading':
		print(dl['filename'], dl['_percent_str'], d['_eta_str'])

##################
# event handlers #
##################
def action_on_create(self, event):
	self.YDL = youtube_dl.YoutubeDL({
		'quiet': True,
		'verbose': False,
		'no_warnings': True,
		'progress_hooks': [ydlhook_progress],
	})
	self.DOWNLOAD_DESTINATION = '.'
	self.LAST_CHECKED_URL = ""
	self.ON_COMPLETE = None

def action_enter_streamurl(self, event):
	if self.timer_fetchinfo_after.IsRunning():
		self.timer_fetchinfo_after.Stop()
	
	if self.LAST_CHECKED_URL == self.input_stream_url.GetValue():
		#print("already checked " + self.input_stream_url.GetValue())
		return
	
	#print("START TIMER: " + str(self.input_stream_url.GetValue()))
	self.timer_fetchinfo_after.StartOnce(550)
	#fetch_stream_status(self, self.input_stream_url.GetValue())
	
	
def action_choosedir(self, event):
	dir_dialog = RecorderGUI.DialogSetDownloadPath(self)
	
	# set currently selected path in the dialog
	dir_dialog.input_dialog_dir.SetPath(self.DOWNLOAD_DESTINATION)
	
	# show dialog, set current path if valid one has been entered and confirmed with "ok"
	if dir_dialog.ShowModal() == wx.ID_OK:
		dstpath = dir_dialog.input_dialog_dir.GetPath()
		if os.path.isdir(dstpath):
			self.DOWNLOAD_DESTINATION = '' + dstpath
		else:
			self.DOWNLOAD_DESTINATION = '.'

def action_help_bunnies(self, event):
	pass

def action_help_show(self, event):
	pass

def action_recordstream(self, event):
	stream_url = self.input_stream_url.GetValue()
	stream_info = video_info(self.YDL, stream_url)
	stream_online = False
	record_onstart = False

	if stream_info is None:
		dialog_offline = RecorderGUI.DialogStreamOffline(self)
		if dialog_offline.ShowModal() == wx.ID_OK:
			record_onstart = dialog_offline.input_startrecord_onstart.GetValue()
	else:
		stream_online = True
	
	print("wait for start: " + str(record_onstart))
	print("is online?: " + str(stream_online))
	print("downloading to: " + self.DOWNLOAD_DESTINATION)
	
	if not stream_online and not record_onstart:
		return
	
	# begin video download
	self.button_record.SetLabel("Warten abbrechen...")
	download_video(self, stream_url)

def timertick_fetchinfo_after(self, event):
	#print("CHECKING: " + str(self.input_stream_url.GetValue()))
	self.LAST_CHECKED_URL = self.input_stream_url.GetValue()
	fetch_stream_status(self, self.input_stream_url.GetValue())

def action_enter_streamurl_now(self, event):
	if self.LAST_CHECKED_URL == self.input_stream_url.GetValue():
		self.timer_fetchinfo_after.Stop()
		return
	
	self.timer_fetchinfo_after.Stop()
	self.LAST_CHECKED_URL = self.input_stream_url.GetValue()
	fetch_stream_status(self, self.input_stream_url.GetValue())

def action_select_oncomplete(self, event):
	if self.recorder_menu_tools.FindItemById(RecorderGUI.ID_ONCOMPLETE_CLOSE).IsChecked():
		self.ON_COMPLETE = 'close'
	elif self.recorder_menu_tools.FindItemById(RecorderGUI.ID_ONCOMPLETE_SHUTDOWN).IsChecked():
		self.ON_COMPLETE = 'shutdown'
	elif self.recorder_menu_tools.FindItemById(RecorderGUI.ID_ONCOMPLETE_STANDBY).IsChecked():
		self.ON_COMPLETE = 'standby'
	else:
		self.ON_COMPLETE = None
	
	
RecorderGUI.SetupRecorder.action_choosedir = action_choosedir
RecorderGUI.SetupRecorder.action_help_bunnies  = action_help_bunnies
RecorderGUI.SetupRecorder.action_help_show = action_help_show
RecorderGUI.SetupRecorder.action_recordstream = action_recordstream
RecorderGUI.SetupRecorder.action_on_create = action_on_create
RecorderGUI.SetupRecorder.action_enter_streamurl = action_enter_streamurl
RecorderGUI.SetupRecorder.timertick_fetchinfo_after = timertick_fetchinfo_after
RecorderGUI.SetupRecorder.action_enter_streamurl_now = action_enter_streamurl_now
RecorderGUI.SetupRecorder.action_select_oncomplete = action_select_oncomplete

if __name__ == '__main__':
	# fix wxfb export
	wx.ST_SIZEGRIP = wx.STB_SIZEGRIP
	
	app = wx.App()
	frame = RecorderGUI.SetupRecorder(None)
	frame.Show()
	app.MainLoop()

