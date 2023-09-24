# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Cleanliness", pos = wx.DefaultPosition, size = wx.Size( 650,405 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

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

		self.m_toggleBtn4 = wx.ToggleButton( self.m_panel1, wx.ID_ANY, u"Count", wx.DefaultPosition, wx.DefaultSize, 0 )
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

		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer7 = wx.GridSizer( 0, 1, 0, 0 )

		self.m_searchCtrl1 = wx.SearchCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl1.ShowSearchButton( True )
		self.m_searchCtrl1.ShowCancelButton( False )
		gSizer7.Add( self.m_searchCtrl1, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel3.SetSizer( gSizer7 )
		self.m_panel3.Layout()
		gSizer7.Fit( self.m_panel3 )
		bSizer5.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer8 = wx.GridSizer( 4, 2, 0, 0 )

		self.m_staticText2 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Number of comments :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		gSizer8.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		gSizer8.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_staticText51 = wx.StaticText( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		gSizer8.Add( self.m_staticText51, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		gSizer8.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		gSizer8.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		gSizer8.Add( self.m_staticText8, 0, wx.ALL, 5 )


		self.m_panel4.SetSizer( gSizer8 )
		self.m_panel4.Layout()
		gSizer8.Fit( self.m_panel4 )
		bSizer5.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer10 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button9 = wx.Button( self.m_panel6, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.m_button9, 0, wx.ALL, 5 )

		self.m_button10 = wx.Button( self.m_panel6, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.m_button10, 0, wx.ALL, 5 )


		self.m_panel6.SetSizer( gSizer10 )
		self.m_panel6.Layout()
		gSizer10.Fit( self.m_panel6 )
		bSizer5.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


