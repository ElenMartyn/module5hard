import hashlib
import time


class User:
    def __init__(self, nickname, password, age): # имя пользователя, пароль, возраст
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest() #  Хэшируем пароль
        self.age = age


class Video:
    def __init__(self, title, duration, adult_mode=False): # заголовок, продолжительность, остановки
        self.title = title
        self.duration = duration  # продолжительность в секундах
        self.time_now = 0  # текущая время просмотра
        self.adult_mode = adult_mode  # режим для взрослых


class UrTube:
    def __init__(self):
        self.users = [] # список объектов
        self.videos = [] # список объектов
        self.current_user = None # текущий пользователь

    def log_in(self, nickname, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f'Пользователь {nickname} вошел в систему.')
                return
        print("Неправильный логин или пароль.")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует.')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user  # Вход после регистрации
        print(f'Пользователь {nickname} зарегистрирован и вошёл в систему.')

    def log_out(self): # Выход
        self.current_user = None
        print("Вы вышли из аккаунта.")

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)
                print(f'Видео "{video.title}" добавлено.')
            else:
                print(f'Видео "{video.title}" уже существует.')

    def get_videos(self, search_word):
        found_videos = [video.title for video in self.videos if search_word.lower() in video.title.lower()]
        return found_videos

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео.")
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу.")
                    return

                print(f'Начинаем просмотр видео: "{video.title}".')
                while video.time_now < video.duration:
                    print(f'Просмотр {video.time_now} сек. из {video.duration} сек.')
                    time.sleep(1)  # Пауза 1 сек.
                    video.time_now += 1
                print("Конец видео")
                video.time_now = 0  # Сброс текущего времени
                return
        print(f'Видео с названием "{title}" не найдено.')



ur = UrTube()


v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Как сделать вовремя домашнюю, при нагруженном графике', 7)

print('Добавление видео')
ur.add(v1, v2, v3)

print('Проверка поиска')
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
print(ur.get_videos('домашн'))

print('Проверка возвраст и пользователя')
ur.watch_video('Для чего девушкам парень программист?')
ur.register('tola_dydkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('tolka_rymka_na_stole', 'tixoBolu', 18)
ur.watch_video('Как сделать вовремя домашнюю, при нагруженном графике')

print('вход в другой аккаунт')
ur.register('tola_dydkin', 'F123FM8fjm9jmi', 55)
print(ur.current_user)

print('Существует видео?')
ur.watch_video('Лучший язык программирования 2024 года!')