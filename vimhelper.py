# -*- coding:UTF-8 -*-
import os
print("欢迎你使用Vim配置文件向导！\n\n我将带着你一步一步，配置你顺手的Vim配置！\n\n")
configFileType = int(input('首先，请选择你安装的Vim类型：？\n1.传统Vim\n2.neovim\n请输入编号：'))
if configFileType == 1:
    configFile = open('~/.vimrc','w')
    plugDirection = '~/.vim/autoload/'
else:
    configFile = open('~/.config/nvim/.init.vim','w')
    plugDirection = '~/.config/nvim/autoload/plug.vim'

print('正在安装插件框架vim-plug...')
os.system('wget -x -p %s https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim' % plugDirection)
configFile.write('''
call plug#begin('~/.vim/plugged')
" ADD YOUR PLUGIN\n
''')
configFile.seek(2,0)

def setPlugin(name):
    pluginName = "Plugin '%s'" % name
    configFile.writelines(pluginName + '\n'*2)

print('''第一步：配置插件
Vim有很多强大的插件，如自动补全、变量修改等，通过插件你甚至可以自定义底栏的样式。
请输入指定类型的插件名，详情可参考 https://github.com/junegunn/vim-plug/wiki/tutorial （无需输入Plugin参数）
每输入一行，请按回车继续输入，完成后直接回车即可。你也可以直接回车跳过此步骤。''')

while True:
    name = input()
    if name == None:
        break
    setPlugin(name)

configFile.writelines('\ncall plug#end()\n')

print('恭喜！你已完成了第一步！\n现在，我们开始配置你的Vim小细节。\n')

def decide(configName,config):
    while True:
        if config == 'y':
            configFile.writelines('set ' + configName + '\n')
            break
        elif config == 'n':
            configFile.writelines('set ' + configName + '!\n')
            break
        else:
            config = input('输入错误！请重新输入:')

def decide_Value(configName,value):
    configFile.writelines('set %s=%s\n'%(configName,value))

lineNumberConfig1 = input('是否启用行号？(y/n):')
decide('number',lineNumberConfig1)

lineNumberConfig2 = input('是否启用相对行号？(y/n):')
decide('relativenumber',lineNumberConfig2)

if lineNumberConfig1 or lineNumberConfig2 == 'y':
    lineNumberConfig3 = int(input('那么，行号前面要空多少格呢？:'))
    decide_Value('numberwidth',lineNumberConfig3)

captitalSearchConfig = input('''接下来，设置查找模式：
大小写查找模式：
1.大小写不敏感查找
2.智能大小写查找（若有一个大写字母，则切换到大小写敏感查找）
3.大小写敏感查找
请输入你选择的模式序号：''')
if captitalSearchConfig == 1:
    configFile.writelines('set ignorecase')
elif captitalSearchConfig == 3:
    configFile.writelines('set smartcase')

hlsearchConfig = input('搜索时结果是否高亮显示？(y/n):')
decide('hlsearch',hlsearchConfig)

cmdConfig = input('是否显示在底栏中显示指令？(y/n):')
decide('showcmd',cmdConfig)

leaderKeyConfig = input("是否设置leaderkey?（默认为r'\'）(y/n):\n（关于什么是leaderkey，参见：https://stackoverflow.com/questions/1764263/what-is-the-leader-in-a-vimrc-file/1764336#1764336）")
if leaderKeyConfig == 'y':
    while True:
        keyconfig = input('设成什么键呢？')
        if len(keyconfig) == 1:
            configFile.writelines('let mapleader="%s"' % keyconfig)
        else:
            print('输入错误，请重新输入！')

print('''缩进选项：

1.文字的缩进模式是什么？
    1)新增加的行和前一行使用相同的缩进形式。
    2)半自动缩进模式（每一行都和前一行有相同的缩进量，且当遇到右花括号（}）时取消缩进形式等特性）
    3)全自动缩进模式（智能识别C和Java等结构化程序设计语言，并且能用C语言的缩进格式来处理程序的缩进结构。）''')
indentmode = {1:'autoindent',2:'smartindent',3:'cindent'}
configFile.writelines('set %s' % indentmode[int(input('请输入序号:'))])

tabConfig = int(input("2.一个Tab等于多少个空格？:"))
decide_Value('tabstop',tabConfig)

wrapConfig = input('3.是否开启自动折行？(y/n):')
while True:
    if wrapConfig == 'n':
        shiftWidthConfig = int(input('那么，文字滚动的速度为每次几字符？:'))
        decide_Value('shiftwidth',shiftWidthConfig)
        break
    else:
        break

mouseConfig = input('是否开启鼠标操作？((y/n)):')
decide_Value('mouse','a')

rulerConfig = input('是否显示标尺？（右下角显示光标位置）(y/n):')
decide('ruler',rulerConfig)

configFile.writelines('let &termencoding=&encoding\nset fileencodings=utf-8,gbk ')

print('恭喜！最基本的设置已经基本完成！\n但是，如果你想更方便的使用Vim，请使用VScode+Vim插件，\n或者Spacemaacs+evil插件（笑），别像我一样跳到这个坑结果被虐的死去活来...')
configFile.close()
print('感谢你的使用，按任意键即可打开Vim！再见')
os.system('read')
os.system('vim')