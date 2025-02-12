#!/usr/bin/env python3
import wx
import art

if __name__ == "__main__":
    app = wx.App()
    window = wx.Frame(None, title="Hello World", size=(800, 400))
    panel = wx.Panel(window)

    fancy_hello = art.text2art("Hello\nWorld", "random")
    font = wx.Font(12, wx.FONTFAMILY_TELETYPE, 0, 100,
                   underline=False, faceName="")
    label = wx.StaticText(panel, label=fancy_hello, pos=(10, 10))
    label.SetFont(font)

    window.Show(True)
    app.MainLoop()
