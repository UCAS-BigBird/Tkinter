import tkinter as tk
import tkinter.messagebox as tm
from requests import get as rget
from bs4 import BeautifulSoup

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
        tk.Label(self.page,text='账户: ').grid(row=1,stick=tk.W,pady=10)
        tk.Entry(self.page,textvariable=self.username).grid(row=1,column=1,stick=tk.E)
        tk.Label(self.page,text='密码: ').grid(row=2,stick=tk.W,pady=10)
        tk.Entry(self.page,textvariable=self.password).grid(row=2,column=1,stick=tk.E)
        tk.Button(self.page,text='登陆',command=self.logincheck).grid(row=3,stick=tk.W,pady=10)
        tk.Button(self.page,text='退出',command=self.page.quit).grid(row=3,column=1,stick=tk.E)

    def logincheck(self):
        name=self.username.get()
        secret=self.password.get()
        try:
            code=[]
            html = rget('https://github.com/UCAS-BigBird/Tkinter/blob/master/code.txt')
            soup = BeautifulSoup(html.content, 'lxml')
            d = soup.findAll('td', class_="blob-code blob-code-inner js-file-line")
            for dd in d:
                code.append(dd.string)
            if name in code and secret == '123456':
                self.page.destroy()
                tm.showinfo(title='正确', message='恭喜你获得了密码')
                MainPage(self.root)
            else:
                tm.showinfo(title='错误', message='账号或密码错误')
        except:
            print("程序有问题")



class MainPage(object):
    def __init__(self,master=None):
        self.root=master
        self.root.geometry("%dx%d"%(600,400))
        self.createPage()

    def createPage(self):
        self.inputpage=InputFrame(self.root)
        self.inputpage.pack()


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
        tk.Entry(self,text=self.importPrice).grid(row=3,stick=tk.W,pady=10)





root=tk.Tk()
root.title("小程序")
LoginPage(root)
root.mainloop()