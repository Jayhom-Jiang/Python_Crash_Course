# coding: utf-8
# 重构模块，然后隔离事件便于管理循环
import sys
import pygame
from alien import Alien
from bullet import Bullet
from time import sleep
from game_stats import GameStats
def get_number_row(ai_settings,ship_height,alien_height):
	"""计算屏幕可容纳多少列外星人"""
	available_space_y = (ai_settings.screen_height - (3*alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	# 返回计算出的列数
	return number_rows

def get_numbers_aliens_x(ai_settings,alien_width):
	"""屏幕一行可以容纳多少外星人"""
	# 屏幕在两边留下一定边距
	available_space_x = ai_settings.screen_width - 2 * alien_width
	# 外星人之间要有一定宽度
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
	"""传递一个外星人并将其放在当前行"""
	# 创建外星人
	alien = Alien(ai_settings,screen)
	# 外星人之间的间距为外星人的宽度
	alien_width = alien.rect.width
	alien_height = alien.rect.height
	# 用浮点变量计算
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.y = alien_height + 2 * alien_height * row_number
	# 将变量的值赋值给rect对象
	alien.rect.x = alien.x
	alien.rect.y = alien.y
	# 在编组中添加外星人
	aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
	"""创建外星人舰群"""
	# 创建一个外星人
	alien = Alien(ai_settings,screen)
	# 计算屏幕screen可容纳多少个外星人
	number_aliens_x=get_numbers_aliens_x(ai_settings,alien.rect.width)
	number_rows = get_number_row(ai_settings,ship.rect.height,alien.rect.height)
	# 循环创建第一行外星人
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings,screen,aliens,alien_number,row_number)


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
		# 添加一个按键模块也就是当用户按q按键时能够快速结束游戏
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_event(event,ship):
	"""响应松开按键"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right=False
	elif event.key == pygame.K_LEFT:
		ship.moving_left=False

def check_events(ai_settings,screen,ship,bullets,play_button,stats,aliens,sb):

	"""监视键盘和鼠标事件"""
	for event in pygame.event.get():
			# 当鼠标点击窗口X键可以结束游戏
		if event.type==pygame.QUIT:
			sys.exit()
			# 响应按键
		elif event.type==pygame.KEYDOWN:
			check_keydown_event(event,ai_settings,screen,ship,bullets)
			# 松开按键
		elif event.type == pygame.KEYUP:
			check_keyup_event(event,ship)
			# 无论玩家单击屏幕任何地方，pygame可以检测到MOUSEBUTTONDOWN事件
		elif event.type == pygame.MOUSEBUTTONDOWN:
			# pygame.mouse.get_pos()方法返回鼠标单击位置(包含x和y)的元组
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(stats,play_button,mouse_x,mouse_y,ai_settings,screen,ship,aliens,bullets,sb)

def check_play_button(stats,play_button,mouse_x,mouse_y,ai_settings,screen,ship,aliens,bullets,sb):
	"""在玩家单击Play的时候开始新游戏"""
	# collidepoint方法是判断是否鼠标单击在Play按钮的rect内，如果是就可以开始游戏了
	button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
	if button_clicked and not stats.game_active :
		# 每次开启新的游戏都需要重新进行游戏设置为初始值，否则会记录之前的数据就会影响游戏效果
		ai_settings.initialize_dynamic_settings()

		# 隐藏光标
		pygame.mouse.set_visible(False)

		# 重新统计游戏信息
		# reset_stats()是重新赋予了飞船的初始数量
		stats.reset_stats()
		stats.game_active = True

		# 重置记分牌图像
		sb.prep_score()
		sb.prep_high_score()
		sb.prep_level()
		sb.prep_ships()

		# 清空外星人舰队列表和子弹列表
		aliens.empty()
		bullets.empty()

		# 创建一群新的外星人舰队，并让飞船居中
		create_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()


def update_screen(ai_settings,screen,ship,aliens,bullets,play_button,stats,sb):
	"""次循环时都重新绘制屏幕"""
	screen.fill(ai_settings.bgcolor)


	# 调用Ship类方法将飞船对象描绘在屏幕上
	ship.blitme()

	# 调用Alien类方法将一个外星人对象描绘在屏幕上
	# alien.blitme()

	# 对编组调用draw()时，Pygame自动绘制编组中每一个元素，绘制位置由元素的属性rect决定
	# 下面这个表示在屏幕绘制编组中的每一个外星人
	aliens.draw(screen)

	# 在飞船和外星人后面重绘所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	# 显示得分
	sb.show_score()

	# 如果游戏处于非活动状态，就绘制Play按钮
	if not stats.game_active:
		play_button.draw_button()


	# 让最近绘制的屏幕可见
	pygame.display.flip()

def update_bullets(ai_settings,screen,ship,aliens,bullets,stats,sb):
	"""更新子弹的位置，并删除已消失的子弹"""
	# 更新子弹的位置
	bullets.update()

	# 删除已经消失的子弹
	# 检查是否有子弹击中外星人的代码一定要放在删除已消失的子弹之后，因为消失的子弹如果再后面那么会影响结果判断
	# 如果子弹打中了外星人，那么删除相应的子弹和外星人
	# 方法sprite.groupcollide()可以将每颗子弹的rect和每个外星人的rect进行比较，并返回一个包含碰撞的的子弹和外星人的键-值对
	# True是告诉pygame删除发生碰撞的子弹或者外星人，若为False则不删除
	#生成新的外星人
	check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets,stats,sb)

def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets,stats,sb):
	"""响应子弹和外星人的碰撞"""
	# 删除已经消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom < 0:
			bullets.remove(bullet)
	# 检查是否有子弹击中外星人的代码一定要放在删除已消失的子弹之后，因为消失的子弹如果再后面那么会影响结果判断
	# 如果子弹打中了外星人，那么删除相应的子弹和外星人
	# 方法sprite.groupcollide()可以将每颗子弹的rect和每个外星人的rect进行比较，并返回一个包含碰撞的的子弹和外星人的键-值对
	# True是告诉pygame删除发生碰撞的子弹或者外星人，若为False则不删除
	collisions = pygame.sprite.groupcollide(bullets,aliens,False,True)

	# 当子弹和外星人发生碰撞，那么就修改积分的值
	if collisions:
		for aliens in collisions.values():
			# 遍历collisions，防止出现一个子弹击中两个或多个外星人但是分数只计算成击中一个外星人
			stats.score += ai_settings.alien_point*len(aliens)
			# 通过调用sb的方法来显示更新最新分值
			sb.prep_score()
			# 判断一下最新值分数是否突破原来的最高分
			check_high_score(stats,sb)

	#生成新的外星人然后游戏等级会提高
	if len(aliens) == 0:
		# 删除清空所有子弹
		bullets.empty()
		# 消灭完一批外星人舰队之后应该加快游戏的节奏
		ai_settings.increase_speed()

		# 提高等级
		stats.level += 1
		sb.prep_level()

		#新建一群外星人舰队
		create_fleet(ai_settings,screen,ship,aliens)


def fire_bullet(ai_settings,screen,ship,bullets):
	"""控制子弹在屏幕中的数目只有三颗，若没有达到限制数目就可以再次发射子弹知道达到限制为止"""
	if len(bullets) < ai_settings.bullets_allowed:
		# 先通过Bullet类创建对象
		new_bullet = Bullet(ai_settings,screen,ship)
		# 再将对象加入到编组bullets中
		bullets.add(new_bullet)

def change_fleet_direction(ai_settings,aliens):
	"""将外星人舰队下移，并改变他们的方向"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def check_fleet_edges(ai_settings,aliens):
	"""有外星人到达边缘时采取的措施"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings,aliens)
			break
def ship_hit(ai_settings,ship,aliens,stats,screen,bullets,sb):
	"""响应被外星人撞到的飞船"""
	if stats.ship_left >0:

		# 将飞船生命数目减去1
		stats.ship_left -= 1

		# 更新飞船生命数
		sb.prep_ships()

		# 清空外星人列表和子弹列表
		aliens.empty()
		bullets.empty()

		# 创建一群新的外星人，并将飞船放在屏幕底部中央
		create_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()

		# 暂替
		sleep(0.5)
	else:
		# 飞船用完后可以将标志游戏开始进行的状态改为False
		stats.game_active = False
		# 显示光标
		pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings,ship,aliens,stats,screen,bullets,sb):
	"""检查是否有外星人达到了屏幕底端"""
	# 获得屏幕的位置
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# 像飞船被撞到一样的处理
			ship_hit(ai_settings,ship,aliens,stats,screen,bullets,sb)
			break


def update_aliens(ai_settings,ship,aliens,stats,screen,bullets,sb):
	"""更新外星人舰队中所有外星人的位置"""
	check_fleet_edges(ai_settings,aliens)
	aliens.update()
	check_aliens_bottom(ai_settings,ship,aliens,stats,screen,bullets,sb)
	# 检测外星人与飞船之间的碰撞
	# 方法spritecollideany()接受两个实参一个是精灵一个是编组，遍历编组检查便组成员是否与精灵发生了碰撞，若有则停止遍历编组
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ai_settings,ship,aliens,stats,screen,bullets,sb)

def check_high_score(stats,sb):
	"""检查是否诞生最新的高分"""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()

