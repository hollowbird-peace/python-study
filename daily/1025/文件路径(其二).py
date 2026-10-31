#python 文件路径(其二).py

#操作：打开文件并写入
#w是写入，使用时会清空已存在的文件
with open("D:\work\python\student\daily\\1025\文本.txt","w",encoding="utf-8") as f:
    f.write("hallo ")
    f.write("world\n")#无换行符变换行
#a是附加，不会清空已存在的文件
with open("D:\work\python\student\daily\\1025\文本.txt","a",encoding="utf-8") as f:
    f.write("你好")
    f.write("世界")

#a+是可读可加（不会覆盖）;r+是可读可写（会覆盖，除非先读取文件）