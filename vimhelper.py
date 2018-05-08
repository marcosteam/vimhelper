# -*- coding:UTF-8 -*-
configFile = open('//home/marcosteam/文档/.vimrc','w')
print("欢迎你使用Vim配置文件向导！\n\n我将带着你一步一步，配置你顺手的Vim配置！\n\n")
configFile.write('''
set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" ADD YOUR PLUGIN\n
''')
def setPlugin(name = 'VundleVim/Vundle.vim'):
    pluginName = "Plugin '%s'" % name
    configFile.seek(2,0)
    configFile.writelines = pluginName + '\n'

print('''第一步：配置插件
...Vim有很多强大的插件，如自动补全、变量修改等，通过插件你甚至可以自定义底栏的样式。
...请输入指定类型的插件名，详情可参考https://github.com/VundleVim/Vundle.vim#quick-start（无需输入Plugin参数）
...每输入一行，请按回车继续输入，完成后直接回车即可。你也可以直接回车跳过此步骤。\n''')

while True:
    name = input()
    if name == '':
        break
    setPlugin(name)

configFile.write('''call vundle#end()\nfiletype plugin indent on''')

