#版权归原作者所有
#开源，制作不易
def C():
    os.system('cls')
def Video(Video,fps):
    cap = cv.VideoCapture(Video);s = 0;ss = 1 / fps if fps != 0 else 0
    while cap.isOpened():
        s %= 2
        if s == 1:
            s(0.1)
            if cv.waitKey(1) == ord('o'):
                s += 1
            if cv.waitKey(1) == ord('q'):
                break
            continue
        s(ss)
        ret, frame = cap.read()
        if not ret:
            print("无法加载或者视频已经播放完毕，退出中……")
            break
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break
        if cv.waitKey(1) == ord('o'):
            s += 1
    cap.release()
    cv.destroyAllWindows()
def load():
    C()
    print('\033[4;32m加载中……\033[0m')
    print('\033[32m 5%  [■------------]\033[0m')
    s(0.75)
    C()
    print('\033[4;32m加载中……\033[0m')
    print('\033[32m 20% [■■■---------]\033[0m')
    try:
        v = open('d:\\sjmnq_file\README.txt')
        v=''
    except:
        os.mkdir('d:\\sjmnq_file')
        os.mkdir('d:\\sjmnq_file\\bjb')
        f= open("d:\\sjmnq_file\\bjb\\note.txt","w+")
        f= open("d:\\sjmnq_file\\README.txt","w+")
        f=''
    finally:
        filename = "d:\\sjmnq_file\\bjb\\note.txt"
    s(0.5)
    C()
    print('\033[4;32m加载中……\033[0m')
    print('\033[32m 35% [■■■■■-------]\033[0m')
    s(0.45)
    C()
    print('\033[4;32m加载中……\033[0m')
    print('\033[32m 50% [■■■■■■------]\033[0m')
    s(0.25)
    C()
    print('\033[4;32m加载中……\033[0m')
    print('\033[32m 60% [■■■■■■■■----]\033[0m')
    s(0.2)
    C()
    print('\033[4;32m加载中……\033[0m')
    print('\033[32m 80% [■■■■■■■■■■--]\033[0m')
    s(0.5)
    C()
    print('\033[4;32m加载中……\033[0m')
    print('\033[32m 99% [■■■■■■■■■■■-]\033[0m')
    s(0.75)
    C()
def first():           #模拟手机启动
    C()
    print('\033[31;44m       / /\033[0m')
    print('\033[31;44m      / / \033[0m')
    print('\033[31;44m     //   \033[0m')
    print('\033[31;44m    ●    \033[0m')
    print()
    print('\033[4;33;44m  中微子工作室  \033[0m')
    print()
    print('\033[4;33;44m  杜绝盗版  \033[0m')
    s(2)
    C()
    load()
    print('\033[4;33;44m 手机 模拟器\033[0m')
    s(2)
    for i in range(3):
        print('\033[32m欢迎来到手机模拟器3.1.0版\033[0m')
def py():
    print('\033[32mpython编程')
    code = ''
    while True:
        print('\033[32m请输入代码(输入q键结束)')
        code = ''
        while True:
            msg = input('\033[32m:')
            if msg == 'q' or msg == '结束' or msg == '退出':
                break
            code += msg
            code += '\n'
        try:
            print(exec(code))       #神奇的exec！！！！！！！！！！
        except Exception as e:
            print('\033[31m错误！',e)
        break_or_not = input('\033[32m是否退出？(y/n)')
        if break_or_not == 'y' or break_or_not == '是' or break_or_not == 'yes':
            break
def mine():
    print('\033[32m我的世界')
    print('\033[32m正在启动中……')
    s(2)
    load()
    print('\033[32m有点无聊，不要太在意……')
    while True:
        print('\033[32m你出生在一个小岛上')
        m1 = input('\033[32m请问你要怎么样？\n1、砍木头\n2、挖矿？')
        if m1 == '1' or m1 == '砍木头':
            print('\033[32m你造了一个工具台，合成了一把木剑',end = '')
            m2 = input('请问你要造房子吗？(y/n)')
            if m2 == '造' or m2 == 'y':
                print('\033[32m你造了房子然后躲过了僵尸大军，你赢了')
                break
            elif m2 == '不造' or m2 == 'n':
                print('\033[32m你用木剑打败了僵尸！成为了奇迹！')
                print('\033[32m你赢了')
                break
        elif m1 == '2' or m1 == '挖矿':
            print('\033[32m啊啊啊啊啊你遇到了僵尸，你逃了出来躲过了一劫，你有许许多多的碎石。',end = '')
            m2 = input('\033[32m你现在要用碎石造武器吗？(y/n)')
            if m2 == 'y' or m2 == '要' or m2 == 'yes':
                print('\033[32m你成功造好了一个石剑，僵尸来了，你把它杀了，你把所有僵尸杀了，大获全胜')
                break
            elif m2 == 'n' or m2 == '不要' or m2 == 'no':
                print('\033[31m啊啊啊你被僵尸杀死了')
                break
        else:
            print('\033[31m输入错误！')
    print('\033[32m最主要的还是我编不出来了……')
    s(2)
    C()
def weather():
    while True:
        city_name = input('\033[32m请输入要查询的城市名称（按q退出）：')
        if city_name == 'q' or city_name == '退出':
            print('\033[32m退出中……')
            break
        url1 = 'http://wthrcdn.etouch.cn/weather_mini?city='+urllib.parse.quote(city_name)
        url2 = 'http://wthrcdn.etouch.cn/weather_mini?citykey=101010100'
        weather_data = urllib.request.urlopen(url1).read()    #爬虫
        weather_data = gzip.decompress(weather_data).decode('utf-8') #解压
        weather_dict = json.loads(weather_data) #转换数据类型
        if weather_dict.get('desc') == 'invilad-citykey':
            print('\033[31m输入的城市有误，或者天气中心不包括此城市')
        if weather_dict.get('desc') == 'OK':
            print('\033[32m========================')
            forecast = weather_dict.get('data').get('forecast')
            print('\033[32m城市：',weather_dict.get('data').get('city'))
            print('\033[32m日期：',forecast[0].get('date'))    
            print('\033[32m气温：',weather_dict.get('data').get('wendu')+'℃ ')
            print('\033[32m昨日最高气温：',weather_dict.get('data').get('yesterday').get('high'))
            print('\033[32m昨日最高气温：',weather_dict.get('data').get('yesterday').get('low'))
            print('\033[32m明日最高气温：',forecast[1].get('high'))
            print('\033[32m明日最低气温：',forecast[1].get('low'))
            print('\033[32m感冒：',weather_dict.get('data').get('ganmao'))
            print('\033[32m风向：',forecast[0].get('fengxiang'))
            print('\033[32m风级：',forecast[0].get('fengli'))
            print('\033[32m高温：',forecast[0].get('high'))
            print('\033[32m低温：',forecast[0].get('low'))
            print('\033[32m天气：',forecast[0].get('type'))
            print('\033[32m*******************************')
def caculation():
    print('\033[32m计算器')
    print('\033[32m*代替乘号，/代替除号，//是求商，%是求余，a的b次方写作a**b，其他的跟正常一样')
    while True:
        num = input('\033[32m请输入算式(q键退出)：')
        if num == 'q' or num == '退出':
            break
        try:
            print(eval(num))
        except:
            print('\033[31m错误，未使用英文输入法或者算式有误!')
def jiami():
    msg = ""         #初始化
    key = 0
    def base_b(num, b):
        return ((num == 0) and "0") or (base_b(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])
    while True:
        message = input("\033[32m请输入字符，我会把它转换成密码,或者q键退出:")
        if message == None:
            break
        while True:
            if message == "q" or message == '退出':
                break
            key = input("\033[32m请输入秘钥：")
            if key == None:
                break
            try:
                key = int(key)
                key = key % 36
                if key == 0:
                    key = 36
                elif key == 1:
                    key = 35
                break
            except:
                if key == "":
                    key = 36
                    break
                else:
                    print("\033[31m请输入数字")
                    continue
        if message == "q" or message == '退出':
            break
        if key == None:
            break
        output = "" 
        for letter in message:
            value = ord(letter)
            value += key
            msg += str(base_b(value,key)) + " "
        msg = "你的密码是：" + msg
        msg = msg.upper()
        print(msg)
        msg = ""
    print("\033[32m感谢你的使用！")
def jiemi():
    output = ""               #初始化
    num = 0
    value = ""
    key = 0
    a = False
    while True:
        message = input("\033[32m请输入ASCII密码，我会把它转换成字符,或者q键退出:")
        if message == None:
            break
        if message == "q" or message == '退出':
            break
        while True:
            if message == "":
                break
            key = input("\033[32m请输入秘钥：")
            if key == None:
                break
            try:
                key = int(key)
                key = key % 36
                if key == 0:
                    key = 36
                elif key == 1:
                    key = 35
                break
            except:
                if key == "":
                    break
                else:
                    print("\033[31m请输入数字")
                    continue
        if key == None:
            break
        if a == True:
            break        
        for letter in message:
            num += 1
            if not letter == " ":
                value += letter
            else:
                if not num == len(message):
                    try:
                        output += chr(int(int(int(value,base = key))-key))
                        value = ""
                    except:
                        print('\033[31m内容有误！')
                        break
        else:
            try:
                output += chr(int(int(int(value,base = key))-key))
                value = ''
            except:
                print('\033[31m内容有误！')
                continue
        output = "\033[32m原先的字符是：" + output           
        print(output)
        output = ""
        num = 0
    print("\033[32m感谢你的使用！")
def notebook():
    global book
    while True:
        print('\033[32m笔记本')
        write_or_read = input('\033[32m请问你是要写入,读取还是删除全部(q键退出)？：')
        if write_or_read == '写入':
            msg = input('\033[32m请问你要写入什么内容？')
            with open(filename, 'a') as book:
                book.write(msg+"\n")
            print('\033[32m写入成功！')
        elif write_or_read == '读取':
            print('\033[32m内容：',end = '')
            with open(filename,'r') as book:
                for i in book.readlines():
                    print(i)
            print()
        elif write_or_read == '删除全部' or write_or_read == '删除':
            with open(filename, "w") as book:
                book.write("")
            print('\033[31m已将笔记本里的内容全部删除')
        elif write_or_read == 'q' or write_or_read == '退出':
            break
        else:
            print('\033[31m无法识别')
            continue
def t():
    if time.strftime("%w",time.localtime()) == '0':
        print (time.strftime("%Y-%m-%d %H:%M:%S  星期天", time.localtime()))
    else:
        print (time.strftime("%Y-%m-%d %H:%M:%S  星期%w", time.localtime()))
    while True:
        do = input('\033[32m请问你要1、计时 2、倒计时3、退出\n:')
        if do == '1' or do == '计时':
            print('\033[32m计时即将开始，如果计时要暂停只要打回车就好了')
            print('3')
            s(1)
            print('2')
            s(1)
            print('1')
            s(1)
            time_start=time.time()
            do2 = input('go！：')
            time_end=time.time()
            print('\033[32m计时总时间为：%s'%(str(time_end - time_start))+'\033[32m秒钟') 
        if do == '2' or do == '倒计时':
            while True:
                try:
                    hour,minute,sec = eval(input('\033[32m请问你要倒计时多少时，分，秒？\n(三个数据用逗号隔开，如果没有的话就写0)\n：'))
                    if type(hour) == float or type(minute) == float or type(sec) == float:
                        print('\033[31m请输入整数')
                    else:
                        break
                except:
                    print('\033[31m请按照正确格式填写！')
            sec = hour*3600 + minute*60 + sec
            C()
            print('\033[32m请等待')
            s(sec)
            for i in range(25):
                print('\033[30m倒计时结束！',end = '')
                print('\033[31m倒计时结束！',end = '')
                print('\033[32m倒计时结束！',end = '')
                print('\033[33m倒计时结束！',end = '')
                print('\033[34m倒计时结束！',end = '')
                print('\033[35m倒计时结束！',end = '')
                print('\033[36m倒计时结束！',end = '')
                print('\033[37m倒计时结束！',end = '')
            print('\033[32m倒计时结束！',end = '')
        if do == '3' or do == '退出':
            break
def race():
    print('\033[32m正在启动中……')
    msg1 = 'avowdpvowzoxnqofpgshq鹅鹅鹅曲项向天歌白毛浮绿水红掌拨清波。594672海内存知己天涯若比邻无为在歧路儿女共沾斤世有伯乐然后有千里马千里马常有而伯乐不常有'
    msg2 = 'gtergoeiqpxmwozpxqnfp举头望明月低头思故乡568576三字经人之初性本善性相近习相远苟不教信乃迁教之道贵以专夫不可陷之盾与无不陷之矛不可同世而立韩非子难一'
    msg3 = 'pgjwpfjvosodvopifbipg679482孙膑是齐国大将田忌的门客，田忌对他非常赏识。楚人有鬻盾与矛着誉之曰吾盾之坚物莫能陷也又誉其矛曰吾矛之利于无物不陷也哈哈哈'
    msg4 = 'qoghzoepfwforfqpgvahw687156塞翁失马焉知非福气不打一处来打开天窗说亮话直言不讳黄鼠狼给鸡拜年不安好心子曰学而时习之不亦说乎有朋自远方来不亦乐乎呵呵呵'
    msg5 = 'qoghswgjenespqpeihnwn572576三皇五帝始尧舜禹相传夏商与西周东周分两段春秋和战国一统秦两汉三分魏蜀吴二晋前后延南北朝并立隋唐五代传宋元明清后皇朝至此完'
    s(2)
    load()
    while True:
        while True:
            print('\033[31m准备')
            msg = c([msg1,msg2,msg3,msg4,msg5])    
            print('\033[32m开始！')
            print(msg)
            start = time.time()
            msg9 = input('\033[32m请输入：')
            end = time.time()
            if len(msg) == len(msg9):
                break
            else:
                print('\033[31m长度不对！')
                s(2)
                C()
                continue
        use_time = end - start
        correct1 = 0
        correct2 = 0
        for i in range(len(msg)):
            correct2 += 1
            if msg[i] == msg9[i]:
                correct1 += 1
        correct = correct1 / correct2
        correct = round(correct*100)
        print('\033[32m你用了%s秒钟，正确率为%s%%'%(use_time,str(correct)))
        break_or_not = input('\033[32m要退出吗？（y/n）：')
        if break_or_not == 'y' or break_or_not == '退出':
            break
def dictionary():
    def is_chinese(strs):
        for _char in strs:
            if not '\u4e00' <= _char <= '\u9fa5':
                return False
        return True
    def with_out_span(strs):
        f = 0
        msg = ''
        for i in str(strs):
            if i == '<':
                f = 0
            if f == 1:
                msg += i
            if i == '>':
                f = 1
        msg2 = ''
        for i in msg:
            if i == ']':
                pass
            else:
                if i == '':
                    pass
                else:
                    msg2 += i
        return msg2
    while(1):
        l = input('\033[32m请输入汉字:')
        if len(l) == 1:
            if is_chinese(l):
                break
            else:
                print('\033[31m请输入汉字！')
        else:
            print('\033[31m请输入一个字符')
    html = 'https://hanyu.baidu.com/s?wd='+l+'&from=zici'
    r = requests.get(html)
    msg = r.text
    msg = BeautifulSoup(msg,'html.parser')
    #print(msg)
    print('\033[32m==================================')
    print('\033[32m拼音：',end = '')
    items = msg.find_all('div',id = 'pinyin')
    items = BeautifulSoup(str(items),'html.parser')
    items = with_out_span(items.find_all('span'))
    print(items)
    print('\033[32m部首：',end = '')
    items = msg.find_all('li',id = 'radical')
    items = BeautifulSoup(str(items),'html.parser')
    items = with_out_span(items.find_all('span'))
    print(items)
    print('\033[32m笔画：',end = '')
    items = msg.find_all('li',id = 'stroke_count')
    items = BeautifulSoup(str(items),'html.parser')
    items = with_out_span(items.find_all('span'))
    print(items)
    print('\033[32m五行：',end = '')
    items = msg.find_all('li',id = 'wuxing')
    items = BeautifulSoup(str(items),'html.parser')
    items = with_out_span(items.find_all('span'))
    print(items)
    print('\033[32m繁体：',end = '')
    items = msg.find_all('li',id = 'traditional')
    items = BeautifulSoup(str(items),'html.parser')
    items = with_out_span(items.find_all('span'))
    print(items)
    print('\033[32m五笔：',end = '')
    items = msg.find_all('li',id = 'wubi')
    items = BeautifulSoup(str(items),'html.parser')
    items = with_out_span(items.find_all('span'))
    print(items)
    print('\033[32m基本解释：',end = '')
    items = msg.find_all('div',class_ = 'tab-content')
    items = BeautifulSoup(str(items),'html.parser')
    items = with_out_span(items)
    print(items)
    print('\033[32m******************************************')
def video():
    '''def with_out_span(strs):
        f = 0
        msg = ''
        for i in str(strs):
            if i == '<':
                f = 0
            if f == 1:
                msg += i
            if i == '>':
                f = 1
        msg2 = ''
        for i in msg:
            if i == ']':
                pass
            else:
                if i == '':
                    pass
                else:
                    msg2 += i
        return msg2
    def x(strs):
        m = ''
        f = 0
        for i in strs:
            f %= 2
            if i == '"':
                f += 1
            if f == 1:
                m += i
        x = 0
        ms=''
        print(m)
        for i in m:
            x += 1
            f %= 2
            if i == '"':
                if x == 2:
                    f += 1
            if f == 1:
                ms += i
        msg = ''
        print(ms)
        for i in ms:
            if i == '"':
                pass
            else:
                msg += i
        return msg
    while(1):
        ask = input('\033[32m请输入关键词：')
        if ask == '':
            print('\033[31m请输入字符！')
        else:
            break
    for i in range(1):
        html = 'https://search.bilibili.com/all?keyword='+ask+'&from_source=nav_suggest_new'
        r = requests.get(html)
        msg = r.text
        msg = BeautifulSoup(msg,'html.parser')
        print(msg)
        items = msg.find_all('a',class_ = 'title')
        i = ""
        i = with_out_span(str(items))
        while True:
            if i == "":
                print('\033[31m错误！搜索不到！可能是搜索时间间隔太短，等一会儿再试！')
                break
            print('\033[32m搜索结果为(用了逗号隔开每一个标题)：',end='')
            print(i)
            try:
                w = int(input('\033[32m请问你要第几个？：'))
                if 0 < w < len(items)+1:
                    break
                else:
                    print('\033[31m请输入有效整数！')
                    continue
            except:
                print('\033[31m请输入数字！')
                continue
        if i == "":
            break
        print(x(items))
        items = 'http:' + list(items)[w-1]
        print(items)'''
    print('\033[32m此部分正在调试中，请等待……')
def qr():
    while True:
        msg = input('\033[32m请输入你要的文字：')
        if msg != '':
            break
        else:
            print('\033[31m请输入字符！')
    while True:
        msg = input('\033[32m请输入二维码要不要带图片(y\n)：')
        if msg == 'n':
            Filepath=None
            break
        elif msg == 'y':
            while True:
                root = tk.Tk()
                root.withdraw()
                Filepath = filedialog.askopenfilename() #获得选择好的文件
                break
            break
    while True:
        print('\033[32m请输入二维码保存路径')
        root = tk.Tk()
        root.withdraw()
        Folderpath = filedialog.askdirectory() #获得选择好的文件夹
        break
    try:
        myqr.run(
            words=msg,
            version=2,
            level='H',
            picture=Filepath,
            colorized=True,  
            contrast=1.0,  
            brightness=1.0,  
            save_dir=Folderpath
        )
        print("已保存！")
    except:
        print("\033[31m出错了~")
def get_mac_address(): 
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:] 
    return ":".join([mac[e:e+2] for e in range(0,11,2)])
mac = get_mac_address()
def apps(a):
    if a == 1:        #python
        py()
    elif a == 2:       #我的世界
        mine()
    elif a == 3:           #天气查询
        weather()
    elif a == 4:   #计算器
        caculation()
    elif a == 5:    #加密
        jiami()
    elif a == 6:   #解密        
        jiemi()
    elif a == 7:      #笔记本
        notebook()
    elif a == 14:  #退出
        return True
    elif a == 15:    #重新启动
        print('\033[32m请等待')
        s(1)
        C()
        first()
    elif a == 8:      #时间
        t()
    elif a == 9:      #打字赛跑
        race()
    elif a == 10:   #字典
        dictionary()
    elif a == 11:           #视频
        video()
    elif a == 12:
        qr()
    elif a == 13:
        print('电脑信息')
        print('mac地址:',end="")
        print(mac)
        print('windows系统')
        print("当前的主机名为" + socket.gethostname())
        print("当前的IP地址为" + socket.gethostbyname(socket.gethostname()))
        print("手机模拟器3.1.0版本，修复了已知错误，新增了软件")
        print("笔记本的数据会保存在D盘，不会丢失")
    return False
def Main():        #主循环
    first()           #启动
    while(1):            #进入循环
        while(1):
            try:         #把输入错误的情况单独拿出来
                a = int(input('\033[32m请问你要打开什么？\n1、python 2、我的世界 3、天气查询 4、计算器 5、加密 6、解密 7、笔记本 8、时间 9、打字赛跑 10、字典 11、视频 12、二维码 13、基本信息 14、退出 15、重新启动\n 请输入：'))
                if a < 1 or a > 15:
                    print('\033[31m请输入1到15的数字')
                    continue
                break
            except:
                print('\033[31m请输入数字')
        if apps(a):
            break
if __main__ == "__name__":
    import uuid
    from time import sleep as s     #导入
    import os
    import urllib.request
    import gzip
    import json
    import time
    from random import choice as c
    import requests
    from bs4 import BeautifulSoup
    import numpy as np
    import cv2 as cv
    from MyQR import myqr
    from MyQR import myqr
    import tkinter as tk
    from tkinter import filedialog
    import socket
    Main()#运行代码
print('\033[4;33;44m谢谢你的观看!\033[0m')     #懒得注释
s(2)
