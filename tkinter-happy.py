import tkinter as tk
import tkinter.messagebox as tm
from requests import get as rget
from bs4 import BeautifulSoup
from tkinter import font
from requests import exceptions
from threading import Thread

def thread_it(func,*args):
    '''
    将函数打包进线程
    '''
    t=Thread(target=func,args=args)
    t.setDaemon(True)
    t.start()


class LoginPage(object):

    def __init__(self,master=None):
        self.root=master
        self.root.geometry('%dx%d'%(300,180))
        self.username=tk.StringVar()
        self.password=tk.StringVar()
        self.createPage()

    def createPage(self):

        self.page = tk.Frame(self.root)
        self.page.pack()
        tk.Label(self.page).grid(row=0,stick=tk.W)
        tk.Label(self.page,text='密码: ').grid(row=1,stick=tk.W,pady=10)
        tk.Entry(self.page,textvariable=self.username).grid(row=1,column=1,stick=tk.E)
        tk.Button(self.page,text='登陆',command=self.logincheck).grid(row=3,stick=tk.W,pady=10)
        button_check=tk.Button(self.page,text='退出',command=self.page.quit)
        button_check.grid(row=3,column=1,stick=tk.E)
        self.button_check=button_check

        ft = font.Font(size=14, weight=font.BOLD)
        label_attention=tk.Label(self.page,text='请输入给你的密码',font=ft,anchor=tk.NW)
        label_attention.grid(row=4, column=1)
        self.label_attention=label_attention

        button_check.configure(command=lambda :thread_it(self.logincheck))

    def logincheck(self):
        #self.label_attention.config(text='我正在查询你输入的对不对')
        name=self.username.get()
        try:
            code=[]
            html = rget('https://github.com/UCAS-BigBird/Tkinter/blob/master/code.txt')
            soup = BeautifulSoup(html.content, 'lxml')
            d = soup.findAll('td', class_="blob-code blob-code-inner js-file-line")
            for dd in d:
                code.append(dd.string)
            if name in code :
                self.page.destroy()
                tm.showinfo(title='正确', message='恭喜你获得了密码,程序马上打开')
                MainPage(self.root)
            elif:
                pass
            else:
                tm.showinfo(title='错误', message='密码错误')
                self.label_attention.config(text='请输入欧粤给你的密码')
        except:
            #print("http请求错误"+str(e.message))
            tm.showinfo(title='错误', message='可能是你没联网\n也有可能联网程序出了Bug,\n但一般来说应该没问题鸭')



class MainPage(object):

    def __init__(self,master=None):
        self.root=master
        self.root.geometry("%dx%d"%(600,400))
        self.createPage()

    def createPage(self):

        self.inputpage=InputFrame(self.root)
        self.inputpage.pack()
        self.querypage=QueryFrame(self.root)
        menubar=tk.Menu(self.root)
        menubar.add_command(label='数据录入',command=self.inputData)
        q=menubar.add_command(label='查询',command=self.queryData)
        self.root['menu']=menubar

    def inputData(self):
        self.inputpage.pack()
        self.querypage.pack_forget()
        #self.countPage.pack_forget()
        #self.aboutPage.pack_forget()

    def queryData(self):

        self.inputpage.pack_forget()
        self.querypage.pack()
        #self.countPage.pack_forget()
        #self.aboutPage.pack_forget()



class InputFrame(tk.Frame):
    def __init__(self,master=None):

        tk.Frame.__init__(self,master)
        self.root=master
        self.itemName=tk.StringVar()
        self.importPrice=tk.StringVar()
        self.sellPrice=tk.StringVar()
        self.deductPrice=tk.StringVar()
        self.createPage()

    def createPage(self):


        tk.Label(self).grid(row=0,stick=tk.W,pady=10)
        tk.Label(self,text='药品名称').grid(row=1,stick=tk.W,pady=10)
        tk.Entry(self,textvariable=self.itemName).grid(row=1,column=1,stick=tk.E)
        tk.Label(self,text='进价/元: ').grid(row=2,stick=tk.W,pady=10)
        tk.Entry(self,text=self.importPrice).grid(row=2,column=1,pady=10)
        tk.Label(self,text='售价/元： ').grid(row=3,stick=tk.W,pady=10)
        tk.Entry(self,textvariable=self.sellPrice).grid(row=3,column=1,stick=tk.E)
        tk.Label(self,text='优惠/元： ').grid(row=4,stick=tk.W,pady=10)
        tk.Entry(self,textvariable=self.deductPrice).grid(row=4,column=1,stick=tk.E)
        button_check=tk.Button(self,text='录入')
        button_check.grid(row=6,column=1,stick=tk.E,pady=10)
        self.button_check=button_check
        button_check.configure(command=lambda: thread_it(self.logincheck2))


    def logincheck2(self):

        tm.showinfo(title='错误', message='密码错误')



class QueryFrame(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.root=master
        self.itemName=tk.StringVar()
        self.createPage()
    def createPage(self):
        tk.Label(self,text='查询界面').pack()


root=tk.Tk()
root.title("行波管的救赎")
LoginPage(root)
root.mainloop()