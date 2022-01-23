import keep_alive
import os
import vk_api
import threading
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
import requests, time, datetime
def message_vk():
  vk.messages.send(user_id=255620921, random_id=get_random_id(), message="Капча")

def captcha_handler(captcha):
  message_vk()
  key = input("Капча {0}: ".format(captcha.get_url())).strip()
  return captcha.try_again(key)

keep_alive.keep_alive()
vk_session = vk_api.VkApi(token=os.environ['token'], captcha_handler=captcha_handler)
print('Авторизовался')
vk = vk_session.get_api()
# def test2():
#   key = vk.messages.send(user_id=255620921, message='Введи каптчу пжпжпж: ', random_id=get_random_id())
#   time.sleep(20)
#   return(key)
# while True:
#   test2()


group_id = [
    "-172969197", "-179334925", "-204335426", "-183060330", "-204847405",
    "-192051750", "-205895789", "-198250637", "-196847024", "-196670004",
    "-186309915", "-198661600", "-180151311", "-180433001", "-178175096",
    "-182119779", "-188394945", "-203161579", "-184693020", "-194946040",
    "-199582344", "-193107343", "-195800768", "-168414337", "-198088958",
    "-209740531", "-198196294", "-207673269", "-209631358"
]

# 0 = https://vk.com/ioanyt
group_ioan = group_id[0]
group_name_ioan = 'ioanyt'

# 1 = https://vk.com/freeskin_ru
group_free_skins = group_id[1]
group_name_free_skins = 'freeskin_ru'

# 2 = https://vk.com/freeskins
group_free_skins_csgo = group_id[2]
group_name_free_skins_csgo = 'freeskins'

# 3 = https://vk.com/gratis_csgo
group_gratis = group_id[3]
group_name_gratis = 'gratis_csgo'

# 4 = https://vk.com/blacks_csgo
group_black_moon = group_id[4]
group_name_black_moon = 'blacks_csgo'

# 5 = https://vk.com/zlaypchela
group_zlaypchela = group_id[5]
group_name_zlaypchela = 'zlaypchela'

# 6 = https://vk.com/ggdrop_win
group_ggdrop = group_id[6]
group_name_ggdrop = 'ggdrop_win'

# 7 = https://vk.com/free.ekopgisecu
group_free_ekopgisecu = group_id[7]
group_name_free_ekopgisecu = 'free.ekopgisecu'

# 8 = https://vk.com/csgoblink
group_csgoblink = group_id[8]
group_name_csgoblink = 'csgoblink'

# 9 = https://vk.com/halava_ananas
group_halava_ananas = group_id[9]
group_name_halava_ananas = 'halava_ananas'

# 10 = https://vk.com/freealter
group_freealter = group_id[10]
group_name_freealter = 'freealter'

# 11 = https://vk.com/fail_promokod
group_fail_promokod = group_id[11]
group_name_fail_promokod = 'fail_promokod'

# 12 = https://vk.com/ggpromodrop
group_ggpromodrop = group_id[12]
group_name_ggpromodrop = 'ggpromodrop'

# 13 = https://vk.com/xaluavniykimi
group_xaluavniykimi = group_id[13]
group_name_xaluavniykimi = 'xaluavniykimi'

# 14 = https://vk.com/free_skinl
group_free_skinl = group_id[14]
group_name_free_skinl = 'free_skinl'

# 15 = https://vk.com/csgoaffk
group_csgoaffk = group_id[15]
group_name_csgoaffk = 'csgoaffk'

# 16 = https://vk.com/ekopgisecu.csgo
group_ekopgisecu_csgo = group_id[16]
group_name_ekopgisecu_csgo = 'ekopgisecu.csgo'

# 17 = https://vk.com/rubachannel
group_rubachannel = group_id[17]
group_name_rubachannel = 'rubachannel'

# 18 = https://vk.com/promo666code
group_promo666code = group_id[18]
group_name_promo666code = 'promo666code'

# 19 = https://vk.com/lezriland
group_lezriland = group_id[19]
group_name_lezriland = 'lezriland'

# 20 = https://vk.com/nezoxcsgo
group_nezoxcsgo = group_id[20]
group_name_nezoxcsgo = 'nezoxcsgo'

# 21 = https://vk.com/qwerskins
group_qwerskins = group_id[21]
group_name_qwerskins = 'qwerskins'

# 22 = https://vk.com/promorunn
group_promorunn = group_id[22]
group_name_promorunn = 'promorunn'

# 23 = https://vk.com/malyaft
group_malyaft = group_id[23]
group_name_malyaft = 'malyaft'

# 24 = https://vk.com/gocs53
group_gocs53 = group_id[24]
group_name_gocs53 = 'gocs53'

# 25 = https://vk.com/xalyava.csgo1
group_xalyava_csgo1 = group_id[25]
group_name_xalyava_csgo1 = 'xalyava.csgo1'

# 26 https://vk.com/freedim4ik
group_freedim4ik = group_id[26]
group_name_freedim4ik = 'freedim4ik'

# 27 https://vk.com/promo_lime
group_promo_lime = group_id[27]
group_name_promo_lime = 'promo_lime'

# 28 https://vk.com/sweetfreecsgo
group_sweetfreecsgo = group_id[28]
group_name_sweetfreecsgo = 'sweetfreecsgo'

namebot = vk.users.get(fields='screen_name')
name = '✔ ' + namebot[0]['first_name'] + ' ' + namebot[0][
    'last_name'] + ' запустился'
print(name)
count_post = 10
def cool_time():
  time.sleep(7200)
def sleep_like():
  time.sleep(20)
# 0 = https://vk.com/ioanyt
def ioan():
    vk.account.setOnline()
    print('📲 В онлайне на 5 минут')
    name = vk.groups.getById(group_id=group_name_ioan, fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_ioan, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post', item_id=postItem, owner_id=group_ioan)
        if like['liked'] == 0:
            vk.likes.add(type='post', item_id=postItem, owner_id=group_ioan)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
            
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1


# 1 = https://vk.com/freeskin_ru
def free_skins():
    name = vk.groups.getById(group_id=group_name_free_skins,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_free_skins, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_free_skins)
        if like['liked'] == 0:
            vk.likes.add(type='post', item_id=postItem, owner_id=group_free_skins)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1


# https://vk.com/freeskins
def free_skins_csgo():
    name = vk.groups.getById(group_id=group_name_free_skins_csgo,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_free_skins_csgo, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_free_skins_csgo)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_free_skins_csgo)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1


# https://vk.com/gratis_csgo
def gratis():
    name = vk.groups.getById(group_id=group_name_gratis, fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_gratis, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_gratis)
        if like['liked'] == 0:
            vk.likes.add(type='post', item_id=postItem, owner_id=group_gratis)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
            vk.likes.delete(type='post', item_id=postItem, owner_id=group_gratis)
            print(
                f'❌  {job + 1} |    {namebot[0]["first_name"]}: Удалил лайк с публикации! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
            vk.likes.delete(type='post', item_id=postItem, owner_id=group_gratis)
            print(
                f'❌  {job + 1} |    {namebot[0]["first_name"]}: Удалил лайк с публикации! (Публикация №{postItem})'
            )
        job = job + 1


# https://vk.com/blacks_csgo
def black_moon():
    name = vk.groups.getById(group_id=group_name_black_moon,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_black_moon, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_black_moon)
        if like['liked'] == 0:
            vk.likes.add(type='post', item_id=postItem, owner_id=group_black_moon)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1


# https://vk.com/zlaypchela
def zlaypchela():
    name = vk.groups.getById(group_id=group_name_zlaypchela,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_zlaypchela, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_zlaypchela)
        if like['liked'] == 0:
            vk.likes.add(type='post', item_id=postItem, owner_id=group_zlaypchela)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1


# https://vk.com/ggdrop_win
def ggdrop():
    name = vk.groups.getById(group_id=group_name_ggdrop, fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_ggdrop, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_ggdrop)
        if like['liked'] == 0:
            vk.likes.add(type='post', item_id=postItem, owner_id=group_ggdrop)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1


# https://vk.com/free.ekopgisecu
def free_ekopgisecu():
    name = vk.groups.getById(group_id=group_name_free_ekopgisecu,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_free_ekopgisecu, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_free_ekopgisecu)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_free_ekopgisecu)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1


# https://vk.com/csgoblink
def csgoblink():
    name = vk.groups.getById(group_id=group_name_csgoblink,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_csgoblink, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_csgoblink)
        if like['liked'] == 0:
            vk.likes.add(type='post', item_id=postItem, owner_id=group_csgoblink)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1


# https://vk.com/halava_ananas
def halava_ananas():
    name = vk.groups.getById(group_id=group_name_halava_ananas,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_halava_ananas, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_halava_ananas)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_halava_ananas)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1


# https://vk.com/freealter
def freealter():
    name = vk.groups.getById(group_id=group_name_freealter,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_freealter, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_freealter)
        if like['liked'] == 0:
            vk.likes.add(type='post', item_id=postItem, owner_id=group_freealter)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1

# https://vk.com/fail_promokod
def fail_promokod():
    name = vk.groups.getById(group_id=group_name_fail_promokod,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_fail_promokod, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_fail_promokod)
        if like['liked'] == 0:
            vk.likes.add(type='post', item_id=postItem, owner_id=group_fail_promokod)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1



# https://vk.com/ggpromodrop
def ggpromodrop():
    name = vk.groups.getById(group_id=group_name_ggpromodrop,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_ggpromodrop, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_ggpromodrop)
        if like['liked'] == 0:
            vk.likes.add(type='post', item_id=postItem, owner_id=group_ggpromodrop)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1


# https://vk.com/xaluavniykimi
def xaluavniykimi():
    name = vk.groups.getById(group_id=group_name_xaluavniykimi,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_xaluavniykimi, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_xaluavniykimi)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_xaluavniykimi)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1



# https://vk.com/free_skinl
def free_skinl():
    name = vk.groups.getById(group_id=group_name_free_skinl,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_free_skinl, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_free_skinl)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_free_skinl)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1



# https://vk.com/csgoaffk
def csgoaffk():
    name = vk.groups.getById(group_id=group_name_csgoaffk,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_csgoaffk, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_csgoaffk)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_csgoaffk)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1

# https://vk.com/ekopgisecu.csgo
def ekopgisecu_csgo():
    name = vk.groups.getById(group_id=group_name_ekopgisecu_csgo,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_ekopgisecu_csgo, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_ekopgisecu_csgo)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_ekopgisecu_csgo)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1



# https://vk.com/rubachannel
def rubachannel():
    name = vk.groups.getById(group_id=group_name_rubachannel,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_rubachannel, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_rubachannel)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_rubachannel)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1



# https://vk.com/promo666code
def promo666code():
    name = vk.groups.getById(group_id=group_name_promo666code,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_promo666code, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_promo666code)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_promo666code)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1



# https://vk.com/lezriland
def lezriland():
    name = vk.groups.getById(group_id=group_name_lezriland,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_lezriland, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_lezriland)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_lezriland)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1



# https://vk.com/nezoxcsgo
def nezoxcsgo():
    name = vk.groups.getById(group_id=group_name_nezoxcsgo,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_nezoxcsgo, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_nezoxcsgo)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_nezoxcsgo)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1



# https://vk.com/qwerskins
def qwerskins():
    name = vk.groups.getById(group_id=group_name_qwerskins,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_qwerskins, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_qwerskins)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_qwerskins)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1



# https://vk.com/promorunn
def promorunn():
    name = vk.groups.getById(group_id=group_name_promorunn,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_promorunn, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_promorunn)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_promorunn)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1



# https://vk.com/malyaft
def malyaft():
    name = vk.groups.getById(group_id=group_name_malyaft,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_malyaft, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_malyaft)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_malyaft)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1



# https://vk.com/gocs53
def gocs53():
    name = vk.groups.getById(group_id=group_name_gocs53,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_gocs53, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_gocs53)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_gocs53)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1



# https://vk.com/xalyava.csgo1
def xalyava_csgo1():
    name = vk.groups.getById(group_id=group_name_xalyava_csgo1,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_xalyava_csgo1, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_xalyava_csgo1)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_xalyava_csgo1)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1



# https://vk.com/freedim4ik
def freedim4ik():
    name = vk.groups.getById(group_id=group_name_freedim4ik,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_freedim4ik, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_freedim4ik)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_freedim4ik)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1



# https://vk.com/promo_lime
def promo_lime():
    name = vk.groups.getById(group_id=group_name_promo_lime,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_promo_lime, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_promo_lime)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_promo_lime)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1



# https://vk.com/sweetfreecsgo
def sweetfreecsgo():
    name = vk.groups.getById(group_id=group_name_sweetfreecsgo,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_sweetfreecsgo, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_sweetfreecsgo)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_sweetfreecsgo)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1
while True:
    ioan()
    print('---------------------------------------------------')

    free_skins()
    print('---------------------------------------------------')

    free_skins_csgo()
    print('---------------------------------------------------')

    gratis()
    print('---------------------------------------------------')
  
    black_moon()
    print('---------------------------------------------------')

    zlaypchela()
    print('---------------------------------------------------')

    ggdrop()
    print('---------------------------------------------------')

    free_ekopgisecu()
    print('---------------------------------------------------')

    csgoblink()
    print('---------------------------------------------------')

    halava_ananas()
    print('---------------------------------------------------')

    freealter()
    print('---------------------------------------------------')

    fail_promokod()
    print('---------------------------------------------------')
    
    ggpromodrop()
    print('---------------------------------------------------')

    xaluavniykimi()
    print('---------------------------------------------------')

    free_skinl()
    print('---------------------------------------------------')

    csgoaffk()
    print('---------------------------------------------------')

    ekopgisecu_csgo()
    print('---------------------------------------------------')

    rubachannel()
    print('---------------------------------------------------')

    promo666code()
    print('---------------------------------------------------')

    lezriland()
    print('---------------------------------------------------')

    nezoxcsgo()
    print('---------------------------------------------------')

    qwerskins()
    print('---------------------------------------------------')

    promorunn()
    print('---------------------------------------------------')

    malyaft()
    print('---------------------------------------------------')

    gocs53()
    print('---------------------------------------------------')

    xalyava_csgo1()
    print('--------------------------------------------------')

    freedim4ik()
    print('--------------------------------------------------')

    promo_lime()
    print('--------------------------------------------------')
    
    sweetfreecsgo()
    print('--------------------------------------------------')

    os.system('clear')
    today = datetime.datetime.today()
    print(today.strftime("%Y-%m-%d %H:%M:%S") + '| Не работаю 2 часа 🙂......')
    vk.messages.send(user_id=255620921, message='Не работаю 2 часа... ', random_id=get_random_id())
    cool_time()
