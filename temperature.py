#温度转换小程序
#功能：将 摄氏度转换为华氏度

#1、提示用户输入摄氏度
celsius = float(input("请输入摄氏度："))

#2、计算华氏度
fahrenheit = celsius*1.8 + 32

#3、输出结果
print(f"{celsius}摄氏度 = {fahrenheit}华氏度")