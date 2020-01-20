import os
#os.chdir("ML")
import wx
app=[]
app = wx.App()
color = wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND)

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Alan turing encryption' , size=(710, 1070))
        self.Center()

#---------------------------------------------------------------
### to add an image as a back ground
        try:
            img ="dr-ibrahim.jpg"
            im = wx.Image(img , wx.BITMAP_TYPE_JPEG). ConvertToBitmap()
            self.my_bitmap = wx.StaticBitmap(self , -1 , im ,(0,0))
        except IOError :
            print("Image file %s not found" % imageFile)
            raise SystemExit
#--------------------------------------------------------------


# to add a Widgets 3 buttons and 3 textcrl
       
        panel = wx.Panel(self)
        
#---------------------------------------------------------
        # txt get button
        str1="UR text"
        self.label1 = wx.StaticText(self.my_bitmap, -1, str1 , wx.Point(30, 120), size=(450 ,30))

        #----------------------------- getval input
        self.gettext_ctrl = wx.TextCtrl(self.my_bitmap ,size=(500,40),
                                   pos=(30, 155))
#------------------------------------------------------------------

        K="UR K"
        self.label2 = wx.StaticText(self.my_bitmap, -1, K , wx.Point(30, 230) , size=(450 ,30))

        #----------------------------- outtval
        self.Ktxt = wx.TextCtrl(self.my_bitmap ,size=(500,40),
                                   pos=(30, 260))
        
#-----------------------------------------------------       
        # txt out button
        O ='UR encrypted Text'
        #self.label1 = wx.StaticText(self.my_bitmap, -1, O , wx.Point(35, 255), size=(450 ,30))
        self.clac = wx.Button(self.my_bitmap, -1 ,O, pos=(45, 400))

        #----------------------------- outtval
        self.outttext_ctrl = wx.TextCtrl(self.my_bitmap ,size=(500,40),
                                   pos=(50, 430))  
        self.outttext_ctrl.Disable()

        # add an evet 
        self.clac.Bind(wx.EVT_BUTTON, self.encrypt)

#----------------------------------------------------------------
        self.Show()

    def encrypt(self , event):
        #K= self.Ktxt.GetValue()
        K = int(self.Ktxt.GetValue())

        text = self.gettext_ctrl.GetValue()
        result = ""
        for i in range(len(text)):
            char = text[i]
            if (char.isupper()):
                result += chr((ord(char) + K-65) % 26 + 65)
            else:
                result += chr((ord(char) + K - 97) % 26 + 97) 
        
        self.outttext_ctrl.Enable()
        self.outttext_ctrl.SetValue("Cipher: " + " " + result )

        

    
        

        

frame = MyFrame()
app.MainLoop()
del app
