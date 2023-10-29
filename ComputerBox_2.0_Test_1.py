#encoding=UTF-8
#主窗口代码
import sys
import tkinter
from tkinter import Menu,Toplevel,messagebox,Button,Tk,ttk,filedialog,Entry,Label
import subprocess
import os

CBmain=Tk()
CBmain.title('ComputerBox')
CBmain.resizable(False,False)
CBmain.geometry('480x240')
CBmain.iconbitmap('CBico.ico')
CBmain.wm_iconbitmap('CBico.ico')
#主窗口两个选项卡
mainmenu=Menu(CBmain)
#1
mainfilemenu=Menu(mainmenu,tearoff=False)
def exit() :
    sys.exit()
mainfilemenu.add_command(label='退出',command=exit)
mainmenu.add_cascade(label='文件',menu=mainfilemenu)
#2
mainbzmenu=Menu(mainmenu,tearoff=False)
def about() :
    messagebox.showinfo('''关于 "ComputerBox"''','''ComputerBox 2.0 Test 1
© 2023 Fxxndxn Team 版权所有''')
mainbzmenu.add_command(label='关于',command=about)
mainmenu.add_cascade(label='帮助',menu=mainbzmenu)
#mod1
def mod1code() :
    #代码从此开始
    mod1=Toplevel()
    mod1.resizable(False,False)
    mod1.iconbitmap('CBico.ico')
    def shutdown() :
        mod1sd = messagebox.askokcancel(title='确认',detail='确定要关机吗？')
        if(mod1sd==True):
            subprocess.Popen('shutdown  -s  -t 0', shell=True)
    shutdown=ttk.Button(mod1,text='关机',command=shutdown,width=16)
    shutdown.grid(row=0,column=0)
    def reboot() :
        mod1rb = messagebox.askokcancel(title='确认',detail='确定要重启吗？')
        if(mod1rb==True):
            subprocess.Popen('shutdown  -r  -t 0', shell=True)
    reboot=ttk.Button(mod1,text='重启',command=reboot,width=16)
    reboot.grid(row=0,column=1)
    #代码结束
mod1bt = ttk.Button(text='电源管理',
                   command=mod1code,
                   width=16)
mod1bt.grid(row=0,column=0)
#mod2
def mod2code() :
    #代码从此开始
    mod2=Toplevel()
    mod2.resizable(False,False)
    mod2.iconbitmap('CBico.ico')
    def scannow() :
        subprocess.Popen('sfc /scannow&pause', shell=True)
    scannow=ttk.Button(mod2,text='全部扫描',command=scannow,width=16)
    scannow.grid(row=0,column=0)
    mod2.mainloop()
    #代码结束
mod2bt=ttk.Button(text='SFC扫描修复',
                   command=mod2code,
                   width=16)
mod2bt.grid(row=1,column=0)
#mod3
def mod3code() :
    #代码从此开始
    mod3=Toplevel()
    mod3.resizable(False,False)
    mod3.iconbitmap('CBico.ico')
    
    def dism() :
        subprocess.Popen('Dism /Online /Cleanup-Image /RestoreHealth&pause', shell=True)
    dismfix=ttk.Button(mod3,text='DISM修复',command=dism,width=16)
    dismfix.grid(row=0,column=0)
    
    def mount() :
        subprocess.Popen(f'Dism /Mount-Wim /WimFile:"{dismimgwimmount}" /Index:{dismimgnamestr} /MountDir:"{dismimgdir}"', shell=True)
    mount=ttk.Button(mod3,text='挂载映像',command=mount,width=16)
    mount.grid(row=1,column=0)

    def unmount() :
        subprocess.Popen(f'Dism /Unmount-Wim /MountDir:"{dismimgdirmount}" /Commit', shell=True)
    unmount=ttk.Button(mod3,text='卸载映像',command=unmount,width=16)
    unmount.grid(row=2,column=0)
    
    def release() :
        subprocess.Popen(f'Dism /Unmount-Wim /MountDir:"{dismimgdirmount}" /Discard', shell=True)
    release=ttk.Button(mod3,text='释放映像',command=release,width=16)
    release.grid(row=3,column=0)

    def save_wim_file():
        dismimgwimsave = filedialog.asksaveasfilename(filetypes=[("WIM文件", "*.wim")])
        return dismimgwim

    def select_folder():
        dismimgdir = filedialog.askdirectory()
        return dismimgdir
    folder_button = ttk.Button(mod3, text='选择文件夹', command=select_folder, width=16)
    folder_button.grid(row=4, column=0)
    
    wim_file_button = ttk.Button(mod3, text='保存映像', command=save_wim_file, width=16)
    wim_file_button.grid(row=5, column=0)

    dismimgnameinst = Label(mod3,text='在此输入镜像名称')
    dismimgnameinst.grid(row=6,column=0)

    dismimgname = ttk.Entry(mod3)
    dismimgname.grid(row=7, column=0)
    
    dismimgnameinst = Label(mod3,text='在此输入镜像描述')
    dismimgnameinst.grid(row=8,column=0)

    dismimgdisc = ttk.Entry(mod3)
    dismimgdisc.grid(row=9, column=0)
    
    dismimgnamestr = dismimgname.get()
    dismimgdiscstr = dismimgdisc.get()
   
    mod3.mainloop()
    # 代码结束

mod3bt = ttk.Button(text='DISM操作', command=mod3code, width=16)
mod3bt.grid(row=2, column=0)
#mod4
def mod4code() :
    #代码从此开始
    mod4 = Toplevel()
    mod4.resizable(False,False)
    mod4.iconbitmap('Cbico.ico')

    def deltemp():
        temp_folder = os.environ['TEMP']
        subprocess.Popen(f'for /D %folder in ("{temp_folder}\\*") do (rd /S /Q "%folder")&pause', shell=True)
        subprocess.Popen(f'del /F /Q "{temp_folder}\\*"&pause', shell=True)
    
    deltempbt = ttk.Button(mod4, text='一键清理', command=deltemp, width=16)
    deltempbt.grid(row=0, column=0)

    mod4.mainloop()
    # 代码结束

mod4bt = ttk.Button(text='缓存清理', command=mod4code, width=16)
mod4bt.grid(row=3,column=0)
#mod5
def mod5code():
    #代码从此开始
    subprocess.Popen('control /name Microsoft.ProgramsAndFeatures', shell=True)
    # 代码结束

mod5bt = ttk.Button(text='程序管理', command=mod5code, width=16)
mod5bt.grid(row=4, column=0)




















#主要的主循环
CBmain.config(menu=mainmenu)
CBmain.mainloop()
#后面不要放东西


