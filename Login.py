#/usr/bin/env python
#_*_ coding:utf-8 _*_
__author__ = "Yorick"


import os
import sys
import getpass
LOCAL_DIR = os.path.dirname(os.path.abspath(__file__))
USER_DB = "%s/%s" % (LOCAL_DIR, "UserInfo.db")
PLANTFORM = sys.platform

# 初始化用户[当用户文件不存在时生效]
if os.path.exists(USER_DB):
   pass
else:
    UserInfo = "admin 123456 0\nuser01 123456 0\ntotal 0 0\n"

    # 编辑文件的一种方式，优于open，文件句柄当不用时自动关闭
    with open(USER_DB, "w") as write_file:
        write_file.write(UserInfo)

# 将用户信息生成一个字典，方便操作
user_info = dict()
with open(USER_DB, "r") as read_file:
    for line in read_file:
        if len(line) != 0:
            username, password, times = line.split()
            if username == "total":
                user_info[username] = {"times": int(times), "flag": password}  # flag无实际意义
            else:
                user_info[username] = {"password": password, "times": int(times)}

# 主逻辑区
while user_info["total"]["times"] < 3:
    print("IT 技术管理后台")
    username = input("input your username\n:>>>").strip()
    if PLANTFORM == "linux2":
        password = getpass.getpass("input your password\n:>>>").strip()
    elif PLANTFORM == "linux":
        password = getpass.getpass("input your password\n:>>>").strip()
    else:
        password = input("input your password\n:>>>").strip()
    if username in user_info:
        if user_info[username]["times"] == 3:
            exit("account is lock, Contact the administrator")
        elif password == user_info[username]["password"]:
            print("Good morning %s" % username)
            break
        else:
            input("Enter to wrong account password. (Any key to continue)")
            user_info[username]["times"] += 1
            user_info["total"]["times"] += 1
    else:
        input("Enter to wrong account password. (Any key to continue)")
        user_info["total"]["times"] += 1
else:
    UserInfo = ""
    # 字符串拼接用户信息
    for info in user_info.keys():
        if info == "total":
            userInfo = "%s %s %s \n" % (info, user_info[info]["flag"], user_info[info]["flag"])
        else:
            userInfo = "%s %s %s \n" % (info, user_info[info]["password"], user_info[info]["times"])
        UserInfo = "%s%s" % (UserInfo, userInfo)
    #
    with open(USER_DB, "w") as write_file:
         write_file.write(UserInfo)
    input("Too many retries, please try again later. (Any key to continue)")
    exit("88")

print('''
initializing........
\033[5m////////////////////////////////////////////////////////////////////
//                          _ooOoo_                               //
//                         o8888888o                              //
//                         88" . "88                              //
//                         (| -_- |)                              //
//                         O\  =  /O                              //
//                      ____/`---'\____                           //
//                    .'  \\|      |//  `.                         //
//                   /  \\|||   :  |||//  \                        //
//                  /  _||||| -:- |||||-  \                       //
//                  |   | \\\   -  /// |   |                       //
//                  | \_|  ''\---/''  |   |                       //
//                  \  .-\__  `-`  ___/-. /                       //
//                ___`. .'  /--.--\  `. . ___                     //
//              ."" '<  `.___\_<|>_/___.'  >'"".                  //
//            | | :  `- \`.;`\ _ /`;.`/ - ` : | |                 //
//            \  \ `-.   \_ __\ /__ _/   .-` /  /                 //
//      ========`-.____`-.___\_____/___.-`____.-'========         //
//                           `=---='                              //
//      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^        //
////////////////////////////////////////////////////////////////////
\033[0m''')
input("(Any key to continue)")
