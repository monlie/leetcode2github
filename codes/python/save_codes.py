# -*- coding: utf-8 -*-
"""
Created on 2018/6/3 1:42:07

@author: Mon
"""

import codecs
from os import system, chdir, getcwd


def save(name, language, code):
    lan_dict = {'python': '.py',
                'python3': '.py',
                'cpp': '.cpp',
                'javascript': '.js'}
    # use your real path of git repository
    with codecs.open(r'/root/work/LeetCode/via_l2g/'+name+lan_dict[language], 'w', 'utf-8') as f:
        f.write(code)


def upload(name):
    cur = getcwd()
    chdir('/root/work/LeetCode/')
    system('git add /root/work/LeetCode/via_l2g')
    system('git commit -m "%s"' % name)
    system('git push')
    chdir(cur)

