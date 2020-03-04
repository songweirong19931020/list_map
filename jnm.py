"""
@File : jnm.py
@copyright : GG
@Coder: Leslie_s
@Date: 2020/3/4
"""
import jpype
import os.path
'''
:param jvmpath jvm.dll存放路径
:param jarpath  jar包存放路径
'''
jvmpath=r"C:\Program Files\Java\jdk1.8.0_91\jre\bin\server\jvm.dll" #jvm.dll存放路径
jarpath=os.path.join(os.path.abspath('.'),"b.jar")

#print(jarpath)
#启动JVM虚拟机
jpype.startJVM(jvmpath,"-ea","-Djava.class.path=%s"% jarpath)
# Main()
#调用jar包里的class
result = jpype.JClass('com.JavaDemo')
#实例化类
JavaDemo = result()
#调用方法
JavaDemo.sayHello(",leslie")
JavaDemo.calc(2,3)
#关闭虚拟机
jpype.shutdownJVM()