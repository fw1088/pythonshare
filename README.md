# pythonshare
主要包括两部分，只能处理单个客户端的服务器
能处理多个客户端的服务器

延伸，比如常见的http服务器，它只是实现了http协议规范，至于使用select，epoll各自不同的框架，使用不同的技术，还可以选择多进程或者多线程模型，比如常见的nginx，apache

比如游戏服务器，通常使用socket来保持长连接，保持客户端和服务器之间实时进行通讯，不过这要求游戏服务器使用自定义的协议，不能适用标准的http协议，因为游戏要保持低延时，数据包应尽可能小，同时还要保持保密性，不被破解，通常自己对协议进行加密和解密。

socket对tcp／ip协议进行了抽象，使得我们可以只是才做api，而不用处理具体的细节

ps:编写python的时候空格键和tab键最好不要混用
因为python是依靠缩进识别各个语句的
