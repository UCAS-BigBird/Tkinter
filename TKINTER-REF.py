import tkinter as tk
import tkinter.messagebox as tm

class Frame(object):

    def __init__(self,master=None):
        self.root=master
        self.root.geometry('%dx%d'%(300,180))
        self.username=tk.StringVar()
        self.password=tk.StringVar()
        self.createPage()

    def createPage(self):
        self.page=tk.Frame(self.root)
        self.page.pack()
        tk.Label(self.root,text='on the window').pack()

        frm_l=tk.Frame(self.page)
        frm_r=tk.Frame(self.page)

        frm_l.pack(side=tk.LEFT)
        frm_r.pack(side="right")

        tk.Label(frm_l,text='on the farm_l1').pack()
        tk.Label(frm_l,text='on the farm l2').pack()
        tk.Label(frm_r,text='on the farn l3').pack()
#         tk.Label(self.page).grid(row=0,stick=tk.W)
#         tk.Label(self.page,text='账户: ').grid(row=1,stick=tk.W,pady=10)
#         tk.Entry(self.page,textvariable=self.username).grid(row=1,column=1,stick=tk.E)
#         tk.Label(self.page,text='密码: ').grid(row=2,stick=tk.W,pady=10)
#         tk.Entry(self.page,textvariable=self.password).grid(row=2,column=1,stick=tk.E)
#         tk.Button(self.page,text='登陆',command=self.logincheck).grid(row=3,stick=tk.W,pady=10)
#         tk.Button(self.page,text='退出',command=self.page.quit).grid(row=3,column=1,stick=tk.E)
#
#     def logincheck(self):
#         name=self.username.get()
#         secret=self.password.get()
#         if name=='wangliang' and secret=='123456':
#             self.page.destroy()
#             MainPage(self.root)
#         else:
#             tm.showinfo(title='错误',message='账号或密码错误')
#
# class MainPage(object):
#     def __init__(self):
#         self.root=master
#         self.root.geometry("%dx%d"%(600,400))
#         self.createPage()
#     def createPage(self):
#         self.inputpage=InputFrame(self.root)
#         self.inputpage.pack()
#
#     def createPage(self):




root=tk.Tk()
root.title("小程序")
Frame(root)
root.mainloop()