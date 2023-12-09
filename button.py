import pygame.font#Pygame Font文本和字体模块

class Button():

    def __init__(self, ai_settings, screen, msg):#msg是要在按钮中显示的文本
        #初始化按钮的属性
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #设置按钮的尺寸和其他属性
        self.width, self.height =  200, 50
        self.button_color = (0, 255, 0)  #绿
        self.text_color = (255, 255, 255)  #白
        self.font = pygame.font.SysFont(None, 48) #默认字体，字号48

        #创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height) #对象
        self.rect.center = self.screen_rect.center #位置居中

        # 按钮的标签只需川建一次
        self.prep_msg(msg) #perp_msg()是将字符串渲染成能绘制在sceen中的图像

    def prep_msg(self, msg):
        #将msg渲染为图像， 并使其在按钮上居中
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        #font.render()将存储在msg中的文本转换为图像#True为是否开启反锯齿功能
        self.msg_image_rect = self.msg_image.get_rect()#绘制文本框
        self.msg_image_rect.center = self.rect.center#将文字放在中间
        
    def draw_button(self):
        # 绘制一个用颜色填充的按钮，在绘制文本
        self.screen.fill(self.button_color, self.rect)#调用screen.fill()来绘制表示按钮的矩形
        self.screen.blit(self.msg_image, self.msg_image_rect)
        #调用screen.blit()，并向它传递一幅图像以及该图像相关联的rect对象，从而在屏幕上绘制文本图像。