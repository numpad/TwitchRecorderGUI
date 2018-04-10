# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jan 23 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

ID_ONCOMPLETE_CLOSE = 1000
ID_ONCOMPLETE_SHUTDOWN = 1001
ID_ONCOMPLETE_STANDBY = 1002

###########################################################################
## Class SetupRecorder
###########################################################################

class SetupRecorder ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Twitch Recorder", pos = wx.DefaultPosition, size = wx.Size( 350,285 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.Size( 150,276 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		self.recorder_statusbar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.recorder_menubar = wx.MenuBar( 0 )
		self.recorder_menu_file = wx.Menu()
		self.recorder_menu_file_downloadpath = wx.MenuItem( self.recorder_menu_file, wx.ID_ANY, u"Download-Ordner setzen...", wx.EmptyString, wx.ITEM_NORMAL )
		self.recorder_menu_file_downloadpath.SetBitmap( wx.NullBitmap )
		self.recorder_menu_file.Append( self.recorder_menu_file_downloadpath )
		
		self.recorder_menubar.Append( self.recorder_menu_file, u"Datei" ) 
		
		self.recorder_menu_tools = wx.Menu()
		self.recorder_menu_tools_onfinish = wx.Menu()
		self.recorder_menu_tools_onfinish_noop = wx.MenuItem( self.recorder_menu_tools_onfinish, wx.ID_ANY, u"Nichts tun...", wx.EmptyString, wx.ITEM_RADIO )
		self.recorder_menu_tools_onfinish.Append( self.recorder_menu_tools_onfinish_noop )
		
		self.recorder_menu_tools_onfinish_exit = wx.MenuItem( self.recorder_menu_tools_onfinish, ID_ONCOMPLETE_CLOSE, u"Programm schließen", wx.EmptyString, wx.ITEM_RADIO )
		self.recorder_menu_tools_onfinish.Append( self.recorder_menu_tools_onfinish_exit )
		
		self.recorder_menu_tools_onfinish_shutdown = wx.MenuItem( self.recorder_menu_tools_onfinish, ID_ONCOMPLETE_SHUTDOWN, u"Shutdown", wx.EmptyString, wx.ITEM_RADIO )
		self.recorder_menu_tools_onfinish.Append( self.recorder_menu_tools_onfinish_shutdown )
		
		self.recorder_menu_tools_onfinish_standby = wx.MenuItem( self.recorder_menu_tools_onfinish, ID_ONCOMPLETE_STANDBY, u"Standby", wx.EmptyString, wx.ITEM_RADIO )
		self.recorder_menu_tools_onfinish.Append( self.recorder_menu_tools_onfinish_standby )
		
		self.recorder_menu_tools.AppendSubMenu( self.recorder_menu_tools_onfinish, u"Nach fertigem Download..." )
		
		self.recorder_menubar.Append( self.recorder_menu_tools, u"Tools" ) 
		
		self.recorder_menu_help = wx.Menu()
		self.recorder_menu_help_cute = wx.MenuItem( self.recorder_menu_help, wx.ID_ANY, u"Süße Häschenbilder!", wx.EmptyString, wx.ITEM_NORMAL )
		self.recorder_menu_help.Append( self.recorder_menu_help_cute )
		
		self.recorder_menu_help.AppendSeparator()
		
		self.recorder_menu_help_help = wx.MenuItem( self.recorder_menu_help, wx.ID_ANY, u"Anleitung", wx.EmptyString, wx.ITEM_NORMAL )
		self.recorder_menu_help.Append( self.recorder_menu_help_help )
		
		self.recorder_menubar.Append( self.recorder_menu_help, u"Hilfe" ) 
		
		self.SetMenuBar( self.recorder_menubar )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.AddGrowableCol( 1 )
		fgSizer1.AddGrowableRow( 4 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.label_streamurl = wx.StaticText( self, wx.ID_ANY, u"Stream URL:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_streamurl.Wrap( -1 )
		fgSizer1.Add( self.label_streamurl, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		input_stream_urlChoices = [ u"twitch.tv/gronkh", u"twitch.tv/numpad0to9", u"twitch.tv/lpmassive" ]
		self.input_stream_url = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), input_stream_urlChoices, wx.CB_SORT )
		self.input_stream_url.SetSelection( 0 )
		self.input_stream_url.SetToolTip( u"URL des Streams" )
		
		fgSizer1.Add( self.input_stream_url, 1, wx.ALL|wx.EXPAND, 2 )
		
		self.label_recordchat = wx.StaticText( self, wx.ID_ANY, u"Chat aufnehmen:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_recordchat.Wrap( -1 )
		fgSizer1.Add( self.label_recordchat, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		input_stream_recordchatChoices = [ u"Nein", u"Ja, nur in Datei", u"Ja, Neben dem Video", u"Ja, Auf dem Video" ]
		self.input_stream_recordchat = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, input_stream_recordchatChoices, 0 )
		self.input_stream_recordchat.SetSelection( 0 )
		self.input_stream_recordchat.SetToolTip( u"Ob und wie der Chat aufgenommen werden soll" )
		
		fgSizer1.Add( self.input_stream_recordchat, 0, wx.ALL|wx.EXPAND, 2 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline1, 0, wx.BOTTOM|wx.EXPAND|wx.TOP, 5 )
		
		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline2, 0, wx.BOTTOM|wx.EXPAND|wx.TOP, 5 )
		
		self.label_streamisonline = wx.StaticText( self, wx.ID_ANY, u"Streamer:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_streamisonline.Wrap( -1 )
		fgSizer1.Add( self.label_streamisonline, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.textmsg_isonline = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RICH2|wx.NO_BORDER )
		fgSizer1.Add( self.textmsg_isonline, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.label_streamdesc = wx.StaticText( self, wx.ID_ANY, u"Beschreibung:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_streamdesc.Wrap( -1 )
		fgSizer1.Add( self.label_streamdesc, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.textmsg_desc = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_NO_VSCROLL|wx.TE_READONLY|wx.TE_RICH2|wx.TE_WORDWRAP|wx.NO_BORDER )
		fgSizer1.Add( self.textmsg_desc, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.label_stream_starttime = wx.StaticText( self, wx.ID_ANY, u"Streambeginn:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_stream_starttime.Wrap( -1 )
		fgSizer1.Add( self.label_stream_starttime, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.textmsg_starttime = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RICH2|wx.NO_BORDER )
		fgSizer1.Add( self.textmsg_starttime, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline11 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline11, 0, wx.BOTTOM|wx.EXPAND|wx.TOP, 5 )
		
		self.m_staticline21 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline21, 0, wx.BOTTOM|wx.EXPAND|wx.TOP, 5 )
		
		
		bSizer1.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		self.button_record = wx.Button( self, wx.ID_ANY, u"Aufnahme starten", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.button_record, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.timer_waitforstart = wx.Timer()
		self.timer_waitforstart.SetOwner( self, wx.ID_ANY )
		self.timer_fetchinfo_after = wx.Timer()
		self.timer_fetchinfo_after.SetOwner( self, wx.ID_ANY )
		self.timer_fetchinfo_after.Start( 1500, true )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.action_on_create )
		self.Bind( wx.EVT_MENU, self.action_choosedir, id = self.recorder_menu_file_downloadpath.GetId() )
		self.Bind( wx.EVT_MENU, self.action_select_oncomplete, id = self.recorder_menu_tools_onfinish_noop.GetId() )
		self.Bind( wx.EVT_MENU, self.action_select_oncomplete, id = self.recorder_menu_tools_onfinish_exit.GetId() )
		self.Bind( wx.EVT_MENU, self.action_select_oncomplete, id = self.recorder_menu_tools_onfinish_shutdown.GetId() )
		self.Bind( wx.EVT_MENU, self.action_select_oncomplete, id = self.recorder_menu_tools_onfinish_standby.GetId() )
		self.Bind( wx.EVT_MENU, self.action_help_bunnies, id = self.recorder_menu_help_cute.GetId() )
		self.Bind( wx.EVT_MENU, self.action_help_show, id = self.recorder_menu_help_help.GetId() )
		self.input_stream_url.Bind( wx.EVT_COMBOBOX, self.action_enter_streamurl_now )
		self.input_stream_url.Bind( wx.EVT_TEXT, self.action_enter_streamurl )
		self.input_stream_url.Bind( wx.EVT_TEXT_ENTER, self.action_enter_streamurl_now )
		self.button_record.Bind( wx.EVT_BUTTON, self.action_recordstream )
		self.Bind( wx.EVT_TIMER, self.timertick_fetchinfo_after, id=wx.ID_ANY )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def action_on_create( self, event ):
		event.Skip()
	
	def action_choosedir( self, event ):
		event.Skip()
	
	def action_select_oncomplete( self, event ):
		event.Skip()
	
	
	
	
	def action_help_bunnies( self, event ):
		event.Skip()
	
	def action_help_show( self, event ):
		event.Skip()
	
	def action_enter_streamurl_now( self, event ):
		event.Skip()
	
	def action_enter_streamurl( self, event ):
		event.Skip()
	
	
	def action_recordstream( self, event ):
		event.Skip()
	
	def timertick_fetchinfo_after( self, event ):
		event.Skip()
	

###########################################################################
## Class DialogSetDownloadPath
###########################################################################

class DialogSetDownloadPath ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Download Pfad", pos = wx.DefaultPosition, size = wx.Size( 430,150 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHints( wx.Size( 430,150 ), wx.Size( -1,150 ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.label_dialog_downloadpath = wx.StaticText( self, wx.ID_ANY, u"In welchem Ordner soll der Stream gespeichert werden?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_dialog_downloadpath.Wrap( -1 )
		bSizer2.Add( self.label_dialog_downloadpath, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.input_dialog_dir = wx.DirPickerCtrl( self, wx.ID_ANY, u"<automatisch>", u"Downloadpfad auswählen...", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer2.Add( self.input_dialog_dir, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		input_dialog_choice = wx.StdDialogButtonSizer()
		self.input_dialog_choiceOK = wx.Button( self, wx.ID_OK )
		input_dialog_choice.AddButton( self.input_dialog_choiceOK )
		self.input_dialog_choiceCancel = wx.Button( self, wx.ID_CANCEL )
		input_dialog_choice.AddButton( self.input_dialog_choiceCancel )
		input_dialog_choice.Realize();
		
		bSizer2.Add( input_dialog_choice, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class DialogShowHelp
###########################################################################

class DialogShowHelp ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Anleitung", pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.dialog_help_text = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_AUTO_URL|wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		bSizer3.Add( self.dialog_help_text, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class DialogStreamOffline
###########################################################################

class DialogStreamOffline ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Aufnahme fehlgeschlagen", pos = wx.DefaultPosition, size = wx.Size( 452,125 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.label_dialog_stream_offline = wx.StaticText( self, wx.ID_ANY, u"Aufnahme nicht möglich, der Stream ist zur Zeit offline.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_dialog_stream_offline.Wrap( -1 )
		bSizer4.Add( self.label_dialog_stream_offline, 0, wx.ALL, 5 )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		
		bSizer4.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		self.input_startrecord_onstart = wx.CheckBox( self, wx.ID_ANY, u"Aufnahme starten, wenn der Stream beginnt.", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.input_startrecord_onstart, 0, wx.ALL, 5 )
		
		button_stream_offline_ok = wx.StdDialogButtonSizer()
		self.button_stream_offline_okOK = wx.Button( self, wx.ID_OK )
		button_stream_offline_ok.AddButton( self.button_stream_offline_okOK )
		button_stream_offline_ok.Realize();
		
		bSizer4.Add( button_stream_offline_ok, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

