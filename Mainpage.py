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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Report Listings", pos = wx.DefaultPosition, size = wx.Size( 650,305 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Welcome Sydney Airbnb", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer5.Add( self.m_staticText12, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		gSizer9 = wx.GridSizer( 0, 5, 0, 0 )

		self.m_button15 = wx.Button( self, wx.ID_ANY, u"Report Listings", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_button15, 0, wx.ALL, 5 )

		self.m_button16 = wx.Button( self, wx.ID_ANY, u"Display Prices", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_button16, 0, wx.ALL, 5 )

		self.m_button17 = wx.Button( self, wx.ID_ANY, u"Search Keywords", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_button17, 0, wx.ALL, 5 )

		self.m_button18 = wx.Button( self, wx.ID_ANY, u"Counts", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_button18, 0, wx.ALL, 5 )

		self.m_button19 = wx.Button( self, wx.ID_ANY, u"Count Listings", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_button19, 0, wx.ALL, 5 )


		bSizer5.Add( gSizer9, 1, wx.EXPAND, 5 )

		gSizer10 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Start Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		gSizer10.Add( self.m_staticText13, 0, wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )

		self.m_datePicker3 = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gSizer10.Add( self.m_datePicker3, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"End Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		gSizer10.Add( self.m_staticText15, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_datePicker4 = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gSizer10.Add( self.m_datePicker4, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer5.Add( gSizer10, 1, wx.EXPAND, 5 )

		gSizer11 = wx.GridSizer( 2, 1, 0, 0 )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Suburb", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		self.m_staticText16.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer11.Add( self.m_staticText16, 0, wx.ALL, 5 )

		self.m_searchCtrl2 = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl2.ShowSearchButton( True )
		self.m_searchCtrl2.ShowCancelButton( False )
		gSizer11.Add( self.m_searchCtrl2, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer5.Add( gSizer11, 1, wx.EXPAND, 5 )

		gSizer13 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button20 = wx.Button( self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer13.Add( self.m_button20, 0, wx.ALL, 5 )

		self.m_button21 = wx.Button( self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer13.Add( self.m_button21, 0, wx.ALL, 5 )


		bSizer5.Add( gSizer13, 1, wx.EXPAND, 5 )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


