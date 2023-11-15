import sys
import tkinter
from tkinter import Menu,Toplevel,messagebox,Button,Tk,ttk,filedialog,Entry,Label
import subprocess
import os
import ctypes

CBmain=Tk()
CBmain.title('ComputerBox')
CBmain.resizable(False,False)
CBmain.geometry('480x240')
CBmain.iconbitmap('CBico.ico')
CBmain.wm_iconbitmap('CBico.ico')

mainmenu=Menu(CBmain)

mainfilemenu=Menu(mainmenu,tearoff=False)
def exit() :
    sys.exit()
mainfilemenu.add_command(label='退出',command=exit)
mainmenu.add_cascade(label='文件',menu=mainfilemenu)

mainbzmenu=Menu(mainmenu,tearoff=False)
def about() :
    aboutw = Toplevel()
    aboutw.resizable(False,False)
    aboutw.title('''关于 "ComputerBox"''')
    aboutl = Label(aboutw, text='''ComputerBox 2.0 Test 1
© 2023 Fxxndxn Team 版权所有''', font=(20))
    aboutl.pack()


mainbzmenu.add_command(label='关于',command=about)
mainmenu.add_cascade(label='帮助',menu=mainbzmenu)

def mod1code() :
    mod1=Toplevel()
    mod1.resizable(False,False)
    mod1.iconbitmap('CBico.ico')
    def shutdown() :
        mod1sd = messagebox.askokcancel(title='确认',detail='确定要关机吗？')
        if(mod1sd==True):
            subprocess.Popen('shutdown  -s  -t 0', creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)
    shutdown=ttk.Button(mod1,text='关机',command=shutdown,width=16)
    shutdown.grid(row=0,column=0)
    def reboot() :
        mod1rb = messagebox.askokcancel(title='确认',detail='确定要重启吗？')
        if(mod1rb==True):
            subprocess.Popen('shutdown  -r  -t 0', creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)
    reboot=ttk.Button(mod1,text='重启',command=reboot,width=16)
    reboot.grid(row=0,column=1)

mod1bt = ttk.Button(text='电源管理',
                   command=mod1code,
                   width=16)
mod1bt.grid(row=0,column=0)

def mod2code() :
    subprocess.Popen('sfc /scannow&pause', creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)

mod2bt=ttk.Button(text='SFC扫描修复',
                   command=mod2code,
                   width=16)
mod2bt.grid(row=1,column=0)

def mod3code() :
    mod6q = messagebox.askokcancel('警告','''该功能未开发完全
    确定继续？''',
    icon='warning')
    mod3=Toplevel()
    mod3.resizable(False,False)
    mod3.iconbitmap('CBico.ico')
    
    def dism() :
        subprocess.Popen('Dism /Online /Cleanup-Image /RestoreHealth&pause', creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)
    dismfix=ttk.Button(mod3,text='DISM修复',command=dism,width=16)
    dismfix.grid(row=0,column=0)
    
    def mount() :
        subprocess.Popen(f'Dism /Mount-Wim /WimFile:"{dismimgwimmount}" /Index:{dismimgnamestr} /MountDir:"{dismimgdir}"', creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)
    mount=ttk.Button(mod3,text='挂载映像',command=mount,width=16)
    mount.grid(row=1,column=0)

    def unmount() :
        subprocess.Popen(f'Dism /Unmount-Wim /MountDir:"{dismimgdirmount}" /Commit', creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)
    unmount=ttk.Button(mod3,text='卸载映像',command=unmount,width=16)
    unmount.grid(row=2,column=0)
    
    def release() :
        subprocess.Popen(f'Dism /Unmount-Wim /MountDir:"{dismimgdirmount}" /Discard', creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)
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

mod3bt = ttk.Button(text='DISM操作', command=mod3code, width=16)
mod3bt.grid(row=2, column=0)

def mod4code() :
    mod4 = Toplevel()
    mod4.resizable(False,False)
    mod4.iconbitmap('Cbico.ico')

    def deltemp():
        temp_folder = os.environ['TEMP']
        subprocess.Popen(f'del /F /Q /S "{temp_folder}\\*"', creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)
        messagebox.showinfo('提示','清理完毕！')
    
    deltempbt = ttk.Button(mod4, text='一键清理', command=deltemp, width=16)
    deltempbt.grid(row=0, column=0)

    mod4.mainloop()

mod4bt = ttk.Button(text='缓存清理', command=mod4code, width=16)
mod4bt.grid(row=3,column=0)

def mod5code():
    subprocess.Popen('control /name Microsoft.ProgramsAndFeatures', creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)

mod5bt = ttk.Button(text='程序管理', command=mod5code, width=16)
mod5bt.grid(row=4, column=0)

def mod6code():
    if(mod6q==True):
        subprocess.Popen('changepk.exe')

mod6bt = ttk.Button(text='更换密钥', command=mod6code, width=16)
mod6bt.grid(row=5, column=0)























CBmain.config(menu=mainmenu)
CBmain.mainloop()
