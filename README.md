# PS4离线金手指
可以使用缓存将金手指缓存在PS4上，实现无PC无网络的离线金手指功能
本项目forked from kmeps4/PS4OfflineTrainer

## 特点
* 可缓存，缓存后可脱离网络仅在PS4上操作
* 支持自动显示当前游戏金手指
* 支持代码修改
* 支持添加金手指
* 支持金手指开关功能
* 没有本体限制，只要ID跟版本对应就可使用
* 支持PC部署、服务器部署、路由器部署
* 支持手机，PC，PS4上启动金手指

## 使用方法

### 1. PC电脑部署

 1. 关闭防火墙或者打开80端口
 2. 打开Exploit-Host-Server.exe,或丢到你自建的HTTP服务器上
 3. PS4打开浏览器，输入PC上显示的IP地址如：http://192.168.1.1/index.html（确保PC和PS4在同一个网段）
 4. 此时PS4开始缓存页面，等待缓存100%
 5. 关闭浏览器，并重启PS4
 6. 启动PS4，开始折腾注入使用可使用hen/goldhen/mira的其中一个
 7. 关闭PS4的浏览器并重新打开，然后注入符合自己机器系统版本的 WebRTE payload（在自己的折腾网页上找）
 8. 开始运行你要玩的游戏
 9. 点手柄PS键
 10. 打开PS4浏览到缓存的金手指页如http://192.168.1.1/index.html
 12. 在PS4IP框里写下localhost和并搜索游戏版本(成功运行一次后，自动搜索正在运行的游戏)
 13. 打开需要的金手指开关
 14. 回到游戏Enjoy~!

### 2. 路由器部署

 1. 将所有文件放在路由器的WEB目录下如：PS4Trainer，以Openwrt路由为例,将金手指文件改成PS4Trainer并上传到/www目录下。
 2. 确保PS4和PC或者手机处在同一个网段。
 4. PS4打开浏览器，输入PC上显示的IP地址如：http://192.168.1.1/PS4Trainer/index.html
 5. 此时PS4开始缓存页面，等待缓存100%
 6. 关闭浏览器，并重启PS4
 7. 启动PS4，开始折腾注入使用可使用hen/goldhen/mira的其中一个
 8. 关闭PS4的浏览器并重新打开，然后注入符合自己机器系统版本的 WebRTE payload（在自己的折腾网页上找）
 9. 开始运行你要玩的游戏
 10. 点手柄PS键
 11. 打开PS4浏览到缓存的金手指页如http://192.168.1.1/PS4Trainer/index.html
 12. 在PS4IP框里写下localhost和并搜索游戏版本(成功运行一次后，自动搜索正在运行的游戏)
 13. 打开需要的金手指开关
 14. 回到游戏Enjoy~!

## 注意

> * PS1: 有些金手指可能会导致游戏崩溃，请自行测试
> * PS2: 推荐用路由器方式，方便日后自行添加金手指，添加新金手指需要三清重新缓存
> * PS3: 用PC或者手机启动金手指注意必须与PS4同一网段
> * PS4: 整合版游戏例如刺客信条5.0整合版显示的是1.0，需要使用5.0的代码新建1.0的才可以使用，参考添加金手指操作

## 如何添加金手指文件

可以自定义添加自己所需要的金手指代码文件，将金手指代码json文件和游戏封面jpg文件放至 **files** 目录下面

以添加凯娜-精神之桥为例：

1. 将金手指文件命名为游戏ID加版本号如:CUSA25000_01.13.josn
2. 添加游戏图标,自己添加一个128*128的JPG文件并命名为游戏ID如CUSA25000.jpg
3. 编辑list.josn,在games:项目下添加你的游戏，例如：


```json

    "games": [
        {
            "name": "刺客信条维京纪元（欧版中文）",
            "title": "CUSA18534",
            "version": "05.00",
            "url": "./files/CUSA18534_05.00.json"
        },
	{
	    "name": "凯娜-精神之桥",
            "title": "CUSA25000",
            "version": "01.13",
            "url": "./files/CUSA25000_01.00.json"
	},
```

字段解释：

* name：要显示的游戏名字，你可以自己写自己喜欢的方便记忆的
* title：是游戏的id （怎么找到自己游戏的ID请自己google）
* version:是游戏的版本，跟据实际填写
* url：是对应的金手指JSON文件的位置

> ***注意：金手指只支持JSON格式，不同版本号的代码不能混用***

4. 最后运行MakeCache.bat，生成缓存文件即可

## 关于金手指代码

有能力可以自己制作

国内大神基本上不分享代码，可以偿试去http://ps4trainer.com/上找一下想要的游戏
然后将游戏ID改成你自己的（大部份可以）然后添加进去就可以了

# 感谢
* golden
* ChendoChap
* TylerMods
* LightningMods
* KameleonRE
* Leeful
