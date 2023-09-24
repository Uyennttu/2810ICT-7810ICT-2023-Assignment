# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Count Listings", pos = wx.DefaultPosition, size = wx.Size( 650,378 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer3 = wx.GridSizer( 0, 5, 0, 0 )

		self.m_toggleBtn1 = wx.ToggleButton( self.m_panel1, wx.ID_ANY, u"Report Listings", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_toggleBtn1, 0, wx.ALL, 5 )

		self.m_toggleBtn2 = wx.ToggleButton( self.m_panel1, wx.ID_ANY, u"Display Prices", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_toggleBtn2, 0, wx.ALL, 5 )

		self.m_toggleBtn3 = wx.ToggleButton( self.m_panel1, wx.ID_ANY, u"Search Keywords", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_toggleBtn3, 0, wx.ALL, 5 )

		self.m_toggleBtn4 = wx.ToggleButton( self.m_panel1, wx.ID_ANY, u"Counts", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_toggleBtn4, 0, wx.ALL, 5 )

		self.m_toggleBtn5 = wx.ToggleButton( self.m_panel1, wx.ID_ANY, u"Count Listings", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_toggleBtn5, 0, wx.ALL, 5 )


		self.m_panel1.SetSizer( gSizer3 )
		self.m_panel1.Layout()
		gSizer3.Fit( self.m_panel1 )
		bSizer5.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer6 = wx.GridSizer( 0, 1, 0, 0 )

		self.m_staticText5 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Welcome Sydney Airbnb", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer6.Add( self.m_staticText5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel2.SetSizer( gSizer6 )
		self.m_panel2.Layout()
		gSizer6.Fit( self.m_panel2 )
		bSizer5.Add( self.m_panel2, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer8 = wx.GridSizer( 0, 1, 0, 0 )

		self.m_staticText3 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer8.Add( self.m_staticText3, 0, wx.ALL, 5 )


		self.m_panel4.SetSizer( gSizer8 )
		self.m_panel4.Layout()
		gSizer8.Fit( self.m_panel4 )
		bSizer5.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer10 = wx.GridSizer( 2, 2, 0, 0 )

		self.m_staticText4 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Start Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		gSizer10.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_datePicker1 = wx.adv.DatePickerCtrl( self.m_panel6, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gSizer10.Add( self.m_datePicker1, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"End Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		gSizer10.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.m_datePicker2 = wx.adv.DatePickerCtrl( self.m_panel6, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gSizer10.Add( self.m_datePicker2, 0, wx.ALL, 5 )


		self.m_panel6.SetSizer( gSizer10 )
		self.m_panel6.Layout()
		gSizer10.Fit( self.m_panel6 )
		bSizer5.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel61 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer61 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText8 = wx.StaticText( self.m_panel61, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		gSizer61.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self.m_panel61, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		gSizer61.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self.m_panel61, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		gSizer61.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self.m_panel61, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		gSizer61.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self.m_panel61, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		gSizer61.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self.m_panel61, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		gSizer61.Add( self.m_staticText13, 0, wx.ALL, 5 )


		self.m_panel61.SetSizer( gSizer61 )
		self.m_panel61.Layout()
		gSizer61.Fit( self.m_panel61 )
		bSizer5.Add( self.m_panel61, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer7 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button5 = wx.Button( self.m_panel7, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.m_button5, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self.m_panel7, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.m_button6, 0, wx.ALL, 5 )


		self.m_panel7.SetSizer( gSizer7 )
		self.m_panel7.Layout()
		gSizer7.Fit( self.m_panel7 )
		bSizer5.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


