import os
'''
读取日志文件,统计ERROR,WARNING,INFO,DEBUG出现的次数
file_path 日志文件的路径
'''
def count_log_levels(file_path):
    # 使用字典保存每个级别的计数，初始均为0
    cnt = {
        "ERROR":0,
        "WARNING":0,
        "INFO":0,
        "DEBUG":0}
    try:
        # encoding = 'utf-8'防止中文乱码
        with open(file_path,"r",encoding = 'utf-8')as f:

            # 一行一行的读，适合大文件，不会占满内存
            for line in f:

                # 先把日志中开头结尾的空格和换行符去掉
                # 再全部转为大写
                line_upper  = line.strip().upper()

                if "ERROR" in line_upper:
                    cnt["ERROR"]+=1
                elif "WARNING" in line_upper:
                    cnt["WARNING"]+=1
                elif "INFO" in line_upper:
                    cnt["DEBUG"]+=1
                elif "DEBUG" in line_upper:
                    cnt["DEBUG"]+=1

            #打印统计结果 
        print("日志级别统计结果:")
        for level,count in cnt.items:
            print(f"{level}: {count}")
    # 文件找不到时的提示
    except FileNotFoundError:
        print(f"错误，找不到文件：{file_path}")
    # 文件不存在时的提示
    except Exception as e:
        print(f"读取文件时发生错误：{e}")

    # 文件自身运行时，__name__为__main__(内置属性)
    # 当别的文件import本文件时，__name__为文件名(不带后缀)
    if __name__ == "__main__":
        # 日志和文件在同一个文件夹下，直接写文件名即可
        # log_file = "app.log"

        # 不管在哪运行此文件，都可以计算出脚本所在文件夹，然后去找app.log,都可以找到
        #先找到脚本的绝对路径，然后去掉文件名字
        script_dir = os.path.dirname(os.path.abspath("__file__"))
        log_file = os.path.join(script_dir,"app.log")

        count_log_levels(log_file)