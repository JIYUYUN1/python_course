import pygame.font#Pygame Font�ı�������ģ��

class Button():

    def __init__(self, ai_settings, screen, msg):#msg��Ҫ�ڰ�ť����ʾ���ı�
        #��ʼ����ť������
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #���ð�ť�ĳߴ����������
        self.width, self.height =  200, 50
        self.button_color = (0, 255, 0)  #��
        self.text_color = (255, 255, 255)  #��
        self.font = pygame.font.SysFont(None, 48) #Ĭ�����壬�ֺ�48

        #������ť��rect���󣬲�ʹ�����
        self.rect = pygame.Rect(0, 0, self.width, self.height) #����
        self.rect.center = self.screen_rect.center #λ�þ���

        # ��ť�ı�ǩֻ�质��һ��
        self.prep_msg(msg) #perp_msg()�ǽ��ַ�����Ⱦ���ܻ�����sceen�е�ͼ��

    def prep_msg(self, msg):
        #��msg��ȾΪͼ�� ��ʹ���ڰ�ť�Ͼ���
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        #font.render()���洢��msg�е��ı�ת��Ϊͼ��#TrueΪ�Ƿ�������ݹ���
        self.msg_image_rect = self.msg_image.get_rect()#�����ı���
        self.msg_image_rect.center = self.rect.center#�����ַ����м�
        
    def draw_button(self):
        # ����һ������ɫ���İ�ť���ڻ����ı�
        self.screen.fill(self.button_color, self.rect)#����screen.fill()�����Ʊ�ʾ��ť�ľ���
        self.screen.blit(self.msg_image, self.msg_image_rect)
        #����screen.blit()������������һ��ͼ���Լ���ͼ���������rect���󣬴Ӷ�����Ļ�ϻ����ı�ͼ��