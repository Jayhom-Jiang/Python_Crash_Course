# coding: utf-8
# 重构模块，然后隔离事件便于管理循环
import sys
import pygame

from bullet import Bullet

def check_keydown_event(event,ai_settings,screen,ship,bullets):
	"""响应按键"""
	if event.key == pygame.K_RIGHT:
		# 向右移飞动
		ship.moving_right=True
	elif event.key == pygame.K_LEFT:
		# 向左移飞动
		ship.moving_left=True
		# 按空格键发送子弹
	elif event.key == pygame.K_SPACE:
		# 将未消失的子弹设置在3颗以内(从这个设置不难得出ai_settings的重要性和方便性和项目扩展性)
		fire_bullet(ai_settings,screen,ship,bullets)

def check_keyup_event(event,ship):
	"""响应松开按键"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right=False
	elif event.key == pygame.K_LEFT:
		ship.moving_left=False

def check_events(ai_settings,screen,ship,bullets):

	"""监视键盘和鼠标事件"""
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
			# 响应按键
		elif event.type==pygame.KEYDOWN:
			check_keydown_event(event,ai_settings,screen,ship,bullets)
			# 松开按键
		elif event.type == pygame.KEYUP:
			check_keyup_event(event,ship)



def update_screen(ai_settings,screen,ship,bullets):
	"""次循环时都重新绘制屏幕"""
	screen.fill(ai_settings.bgcolor)


	# 调用Ship类方法将飞船对象描绘在屏幕上
	ship.blitme()

	# 在飞船和外星人后面重绘所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()


	# 让最近绘制的屏幕可见
	pygame.display.flip()

def update_bullets(bullets):
	"""更新子弹的位置，并删除已消失的子弹"""
	# 更新子弹的位置
	bullets.update()

	# 删除已经消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom < 0:
			bullets.remove(bullet)

def fire_bullet(ai_settings,screen,ship,bullets):
	"""控制子弹在屏幕中的数目只有三颗，若没有达到限制数目就可以再次发射子弹知道达到限制为止"""
	if len(bullets) < ai_settings.bullets_allowed:
		# 先通过Bullet类创建对象
		new_bullet = Bullet(ai_settings,screen,ship)
		# 再将对象加入到编组bullets中
		bullets.add(new_bullet)
