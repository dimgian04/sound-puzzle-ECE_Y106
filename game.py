import pygame
from pygame import mixer
from random import sample
from time import sleep

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
light_blue = (51, 255, 255)
bg_rect_color = (0, 0, 0)  # by default
# Dimensions
screen_width = 800
screen_height = 600
rects_size = 0  # by default
bgRects_margin = 12.5
play_sound_rect_width = 30
play_sound_rect_height = 30
pygame.init()

# Πόσα lock_rects/images/image_rects/play_sound_rects
s = 0  # by default
# Χρησιμοποιείται για να κάνει index τα παραμύθια και να καλεί κατάλληλη συναρτήση που δημιουργεί τα απαραίτητα class objects 'κομμάτια παζλ' με βάση το παραμύθι
r = 0  # by default
# Δημιουργία Pygame Window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ηχητικό Πάζλ')


def f(x):  # Επιστρέφει το μήκος για το οποίο θα ισαπέχουν μεταξύ τους όλα τα x εισαγώμενα rects και θα απέχουν εξίσου πολύ και απο τα borders.
    return (screen_width - rects_size * x) / (x + 1)


def get_font(size):
    return pygame.font.Font('assets/font.ttf', size)


def volume(v):
    mixer.music.set_volume(v)

# Load assets
click = mixer.Sound('assets/click.wav')
click.set_volume(1)
mixer.music.load('assets/background.wav')
volume(0.6)
background_image = pygame.image.load('assets/background.png')
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)


def game():
    global r, score
    # Λίστα που περίεχει s τον αριθμό στοιχεία (τους αριθμούς απο 0 έως s-1) με τυχαία σειρά.
    random_list = sample(range(s), s)

    class Fairytale:
        """ Class for loading up the images and sound clips of the fairytales
        and randomizing the order in which they show up. It also contains methods
        for playing the sound clips and blitting the images."""

        def __init__(self, image, sound, randomizer):
            self.image = pygame.image.load(image)
            self.sound = sound
            self.randomizer = random_list[randomizer]
            self.image_rect = self.image.get_rect(topleft=(x_cords[self.randomizer], y_cords[self.randomizer]))  # Δεν χρειάζεται το topleft attribute, επειδή οι φωτογραφίες και στο (0, 0) να εμφανιστούν, στο game loop θα ικανοποιείται το τελευταίο elif και θα τις κάνει reset στα start position, οπότε αρκεί να είναι καλώς ορισμένο εκεί.
            self.play_sound_rect = pygame.Rect(x_cords1[self.randomizer], y_cords1[self.randomizer], play_sound_rect_width, play_sound_rect_height)
            self.start_rect = pygame.Rect(x_cords[self.randomizer], y_cords[self.randomizer], rects_size, rects_size)
            start_rects_list.append(self.image_rect)
            play_sound_rects.append(self.play_sound_rect)

        def play_sound(self):
            mixer.music.load(self.sound)
            mixer.music.play()

        def pause_sound(self):
            mixer.music.pause()

        def image_blit(self):
            pygame.draw.rect(screen, white, self.start_rect)
            screen.blit(self.image, self.image_rect)

    def gourounakia_objects():  # r = 1
        global objects
        gourounakia1 = Fairytale('gourounakia/gourounakia1.png', 'gourounakia/gourounakia1.wav', 0)
        gourounakia2 = Fairytale('gourounakia/gourounakia2.png', 'gourounakia/gourounakia2.wav', 1)
        gourounakia3 = Fairytale('gourounakia/gourounakia3.png', 'gourounakia/gourounakia3.wav', 2)
        objects = [gourounakia1, gourounakia2, gourounakia3]

    def kokkinoskoufitsa_objects():  # r = 2
        global objects
        kokkinoskoufitsa1 = Fairytale('kokkinoskoufitsa/kokkinoskoufitsa1.png', 'kokkinoskoufitsa/kokkinoskoufitsa1.wav', 0)
        kokkinoskoufitsa2 = Fairytale('kokkinoskoufitsa/kokkinoskoufitsa2.png', 'kokkinoskoufitsa/kokkinoskoufitsa2.wav', 1)
        kokkinoskoufitsa3 = Fairytale('kokkinoskoufitsa/kokkinoskoufitsa3.png', 'kokkinoskoufitsa/kokkinoskoufitsa3.wav', 2)
        kokkinoskoufitsa4 = Fairytale('kokkinoskoufitsa/kokkinoskoufitsa4.png', 'kokkinoskoufitsa/kokkinoskoufitsa4.wav', 3)
        kokkinoskoufitsa5 = Fairytale('kokkinoskoufitsa/kokkinoskoufitsa5.png', 'kokkinoskoufitsa/kokkinoskoufitsa5.wav', 4)
        kokkinoskoufitsa6 = Fairytale('kokkinoskoufitsa/kokkinoskoufitsa6.png', 'kokkinoskoufitsa/kokkinoskoufitsa6.wav', 5)
        objects = [kokkinoskoufitsa1, kokkinoskoufitsa2, kokkinoskoufitsa3, kokkinoskoufitsa4, kokkinoskoufitsa5, kokkinoskoufitsa6]

    def lagosxelona_objects():  # r = 3
        global objects
        lagosxelona1 = Fairytale('lagosxelona/lagosxelona1.png', 'lagosxelona/lagosxelona1.wav', 0)
        lagosxelona2 = Fairytale('lagosxelona/lagosxelona2.png', 'lagosxelona/lagosxelona2.wav', 1)
        lagosxelona3 = Fairytale('lagosxelona/lagosxelona3.png', 'lagosxelona/lagosxelona3.wav', 2)
        lagosxelona4 = Fairytale('lagosxelona/lagosxelona4.png', 'lagosxelona/lagosxelona4.wav', 3)
        lagosxelona5 = Fairytale('lagosxelona/lagosxelona5.png', 'lagosxelona/lagosxelona5.wav', 4)
        objects = [lagosxelona1, lagosxelona2, lagosxelona3, lagosxelona4, lagosxelona5]

    # Lock Position Rects
    lock_rects = []
    for i in range(s):
        lock_rects.append(pygame.Rect(f(s) + i * (rects_size + f(s)), screen_height - 2 * bgRects_margin - rects_size, rects_size, rects_size))

    # Background Rect behind lock rects and img_rects
    bg_rect1_height = rects_size + 2 * bgRects_margin
    bg_rect2_height = screen_height - 5 * bgRects_margin - rects_size
    bg_rect1 = pygame.Rect(bgRects_margin, screen_height - 3 * bgRects_margin - rects_size, screen_width - 2 * bgRects_margin, bg_rect1_height)
    bg_rect2 = pygame.Rect(bgRects_margin, bgRects_margin, screen_width - 2 * bgRects_margin, bg_rect2_height)

    # Start Position Rects
    x_cords = []
    y_cords = []
    start_rects_list = []
    for i in range(s):
        x_cords.append(f(s) + i * (rects_size + f(s)))
    for i in range(s):
        y_cords.append(2 * bgRects_margin)

    # Play Sound Rects
    play_sound_image = pygame.image.load('assets/play_30.png')
    x_cords1 = []
    y_cords1 = []
    play_sound_rects = []
    for i in range(s):
        x_cords1.append((f(s) + rects_size / 2 - play_sound_rect_width / 2) + i * (rects_size + f(s)))
    for i in range(s):
        y_cords1.append(3 * bgRects_margin + rects_size)

    # Check answer rect
    h = bg_rect2_height - play_sound_rect_height - 4 * bgRects_margin - rects_size
    check_text = get_font(30).render('ΕΠΙΒΕΒΑΙΩΣΗ', True, white)
    check_rect = check_text.get_rect(center=(screen_width/2, bg_rect2_height - h / 2))
    correct_rects = []

    if r == 1:
        gourounakia_objects()
    elif r == 2:
        lagosxelona_objects()
    elif r == 3:
        kokkinoskoufitsa_objects()

    running = True
    selected = False
    while running:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.mixer.music.load('assets/background.wav')
                pygame.mixer.music.play(-1)
                running = False
            for i in range(s):  # Cycle Play Sound Rects
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and play_sound_rects[i].collidepoint(event.pos):
                    if not mixer.music.get_busy():  # returns True μόνο αν παίζεται μουσική
                        for obj in objects:
                            if obj.randomizer == random_list[i]:  # Ελέγχω ποιό από τα objects του class, δηλαδή ποιό κομμάτι του puzzle, έχει randomizer ίσο με το στοιχείο στην i-οστή θέση του random list. Τα rectangles στις λίστες start_rects και play_sound_rects προστίθενται στην αντίστοιχη λίστα με σειρά που δημιουργείται απο τα objects άρα στις λίστες αυτές το στοιχείο 0 είναι αυτό που έχει συνενταγμένες pou παίρνονραι απο τις λίστες των x_cords, y_cords στη θέση randomizer[0]
                                obj.play_sound()
                    else:
                        for obj in objects:
                            if obj.randomizer == random_list[i]:
                                obj.pause_sound()
            for j in range(s):  # Cycle Start Rectangles
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and start_rects_list[j].collidepoint(event.pos):
                    start_rect_var = j  # Αν δεν το ορίσω, τότε κατα την διάρκεια του mouse motion το selected είναι True και απλά το πρώτο loop περνάει όλες τις τιμές του j και φέρνει όλα τα start rects το ένα πάνω στο άλλο
                    selected = True
                    selected_offset_x = start_rects_list[j].x - event.pos[0]
                    selected_offset_y = start_rects_list[j].y - event.pos[1]
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    selected = False
                elif event.type == pygame.MOUSEMOTION and selected is True:
                    start_rects_list[start_rect_var].x = event.pos[0] + selected_offset_x
                    start_rects_list[start_rect_var].y = event.pos[1] + selected_offset_y
                for i in range(s):  # cycle ta lock rects
                    if lock_rects[i].x - rects_size < start_rects_list[j].x < lock_rects[i].x + rects_size and lock_rects[i].y - rects_size < start_rects_list[j].y < lock_rects[i].y + rects_size and selected is False:  # Η εντολή colliderect που ελέγχει colission μεταξύ δύο rectangles δεν δούλευε και έπρεπε να φτιαχτούν οι ανισώσεις ελέγχου.
                        start_rects_list[j].x = lock_rects[i].x
                        start_rects_list[j].y = lock_rects[i].y
                    elif (lock_rects[i].x - rects_size > start_rects_list[j].x or start_rects_list[j].x > lock_rects[i].x + rects_size) and (lock_rects[i].y - rects_size > start_rects_list[j].y or start_rects_list[j].y > lock_rects[i].y + rects_size) and selected is False:
                        start_rects_list[j].x = x_cords[random_list[j]]  # Αν δεν υπάρχει collide μεταξυ των rectangles, Θέλω να τα πηγαίνει στην αρχική τους θέση που έχει προκύψει τυχαία με το randomizer
                        start_rects_list[j].y = y_cords[random_list[j]]
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and check_rect.collidepoint(event.pos):
                for i in range(s):  # Cycle Lock Rects
                    for obj in objects:  # Cycle Fairytale Class Objects
                        if lock_rects[i].x == obj.image_rect.x and lock_rects[i].y == obj.image_rect.y and obj.randomizer == random_list[i]:
                            correct_rects.append(obj.image_rect)
                score = int((len(correct_rects) / s) * 100)
                if len(correct_rects) == s:  # Όλες οι εικόνες στην σωστή θέση
                    correct_rects.clear()
                    mixer.music.stop()
                    mixer.music.load('assets/background.wav')
                    mixer.music.play(-1)
                    game_over_win()
                else:
                    correct_rects.clear()
                    mixer.music.stop()
                    mixer.music.load('assets/background.wav')
                    mixer.music.play(-1)
                    game_over_lose()
        pygame.draw.rect(screen, bg_rect_color, bg_rect1)
        pygame.draw.rect(screen, bg_rect_color, bg_rect2)
        for r in lock_rects:
            pygame.draw.rect(screen, black, r)
        for r in play_sound_rects:
            screen.blit(play_sound_image, r)
        pygame.draw.rect(screen, black, check_rect)
        screen.blit(check_text, check_rect)
        for obj in objects:
            obj.image_blit()
        pygame.display.update()


def play():
    global s, r, rects_size, bg_rect_color
    while True:
        screen.fill(black)
        screen.blit(background_image, (0, 0))
        # Mute Button
        mute_on_img = pygame.image.load('assets/mute2.png')
        mute_off_img = pygame.image.load('assets/mute1.png')
        mute_on_rect = mute_on_img.get_rect(center=(760, 40))
        mute_off_rect = mute_off_img.get_rect(center=(760, 40))
        if mixer.music.get_volume() == 0:
            screen.blit(mute_off_img, mute_off_rect)
        else:
            screen.blit(mute_on_img, mute_on_rect)
        # Back Button
        back_text = get_font(20).render("ΠΙΣΩ", True, white)
        back_rect = back_text.get_rect(topleft=(20, 20))
        screen.blit(back_text, back_rect)
        # Fairytale Choice Text
        main_text = get_font(40).render('ΕΠΙΛΟΓΗ ΠΑΡΑΜΥΘΙΟΥ', True, white)
        main_rect = main_text.get_rect(center=(400, 125))
        screen.blit(main_text, main_rect)
        # Fairytale 1 Button
        fairytale1_button_background = pygame.image.load('assets/fairytale_bg.jpg')
        fairytale1_button_rect = fairytale1_button_background.get_rect(center=(400, 225))
        screen.blit(fairytale1_button_background, fairytale1_button_rect)
        gourounakia_text = get_font(30).render('ΤΑ 3 ΓΟΥΡΟΥΝΑΚΙΑ', True, white)
        gourounakia_rect = gourounakia_text.get_rect(center=(339.75, 225))
        screen.blit(gourounakia_text, gourounakia_rect)
        # Fairytale 2 Button
        fairytale2_button_background = pygame.image.load('assets/fairytale_bg.jpg')
        fairytale2_button_rect = fairytale2_button_background.get_rect(center=(400, 350))
        screen.blit(fairytale2_button_background, fairytale2_button_rect)
        lagosxelona_text = get_font(30).render('ΛΑΓΟΣ ΚΑΙ ΧΕΛΩΝΑ', True, white)
        lagosxelona_rect = lagosxelona_text.get_rect(center=(339.75, 350))
        screen.blit(lagosxelona_text, lagosxelona_rect)
        # Fairytale 3 Button
        fairytale3_button_background = pygame.image.load('assets/fairytale_bg.jpg')
        fairytale3_button_rect = fairytale3_button_background.get_rect(center=(400, 475))
        screen.blit(fairytale3_button_background, fairytale3_button_rect)
        kokkinoskoufitsa_text = get_font(30).render('ΚΟΚΚΙΝΟΣΚΟΥΦΙΤΣΑ', True, white)
        kokkinoskoufitsa_rect = kokkinoskoufitsa_text.get_rect(center=(339.75, 475))
        screen.blit(kokkinoskoufitsa_text, kokkinoskoufitsa_rect)
        # Difficulties
        easy = pygame.image.load('assets/difficulty/easy.jpg')
        medium = pygame.image.load('assets/difficulty/medium.jpg')
        hard = pygame.image.load('assets/difficulty/hard.jpg')
        easy_rect = easy.get_rect(center=(710, 225))
        medium_rect = medium.get_rect(center=(710, 350))
        hard_rect = hard.get_rect(center=(710, 475))
        screen.blit(easy, easy_rect)
        screen.blit(medium, medium_rect)
        screen.blit(hard, hard_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                click.play()
                main_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and back_rect.collidepoint(event.pos):
                click.play()
                main_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (mute_on_rect.collidepoint(event.pos) or mute_off_rect.collidepoint(event.pos)):
                if mixer.music.get_volume() == 0:
                    click.play()
                    volume(0.6)
                else:
                    click.play()
                    volume(0)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and fairytale1_button_rect.collidepoint(event.pos):
                click.play()
                bg_rect_color = (255, 186, 242)
                s = 3
                r = 1
                rects_size = 200
                mixer.music.stop()
                volume(0.6)
                game()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and fairytale2_button_rect.collidepoint(event.pos):
                click.play()
                bg_rect_color = (255, 186, 203)
                s = 5
                r = 2
                rects_size = 135
                mixer.music.stop()
                volume(0.6)
                game()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and fairytale3_button_rect.collidepoint(event.pos):
                click.play()
                bg_rect_color = (175, 234, 255)
                s = 6
                r = 3
                rects_size = 110
                mixer.music.stop()
                volume(0.6)
                game()
        pygame.display.update()


def game_over_win():
    while True:
        screen.fill(black)
        screen.blit(background_image, (0, 0))
        # Game Over
        game_over_text = get_font(50). render("ΝΙΚΗΣΕΣ!", True, white)
        game_over_rect = game_over_text.get_rect(center=(400, 125))
        screen.blit(game_over_text, game_over_rect)
        # Score
        score_text = get_font(40).render(f'SCORE: {score}/100', True, white)
        score_rect = score_text.get_rect(center=(400, 212.5))
        screen.blit(score_text, score_rect)
        # Play Again
        play_again_text = get_font(40).render("ΠΑΙΞΕ ΞΑΝΑ", True, white)
        play_again_rect = play_again_text.get_rect(center=(400, 300))
        screen.blit(play_again_text, play_again_rect)
        # Exit
        exit_text = get_font(40).render("ΕΞΟΔΟΣ", True, white)
        exit_rect = exit_text.get_rect(center=(400, 400))
        screen.blit(exit_text, exit_rect)
        # Mute Button
        mute_on_img = pygame.image.load('assets/mute2.png')
        mute_off_img = pygame.image.load('assets/mute1.png')
        mute_on_rect = mute_on_img.get_rect(center=(760, 40))
        mute_off_rect = mute_off_img.get_rect(center=(760, 40))
        if mixer.music.get_volume() == 0:
            screen.blit(mute_off_img, mute_off_rect)
        else:
            screen.blit(mute_on_img, mute_on_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                click.play()
                sleep(0.2)
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and play_again_rect.collidepoint(event.pos):
                click.play()
                main_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and exit_rect.collidepoint(event.pos):
                click.play()
                sleep(0.2)
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (mute_on_rect.collidepoint(event.pos) or mute_off_rect.collidepoint(event.pos)):
                if mixer.music.get_volume() == 0:
                    click.play()
                    volume(0.6)
                else:
                    click.play()
                    volume(0)

        pygame.display.update()


def game_over_lose():
    while True:
        screen.fill(black)
        screen.blit(background_image, (0, 0))
        # Game Over
        game_over_text = get_font(50).render("ΕΧΑΣΕΣ", True, white)
        game_over_rect = game_over_text.get_rect(center=(400, 125))
        screen.blit(game_over_text, game_over_rect)
        # Score
        score_text = get_font(40).render(f'SCORE: {score}/100', True, white)
        score_rect = score_text.get_rect(center=(400, 212.5))
        screen.blit(score_text, score_rect)
        # Play Again
        play_again_text = get_font(40).render("ΠΑΙΞΕ ΞΑΝΑ", True, white)
        play_again_rect = play_again_text.get_rect(center=(400, 300))
        screen.blit(play_again_text, play_again_rect)
        # Exit
        exit_text = get_font(40).render("ΕΞΟΔΟΣ", True, white)
        exit_rect = exit_text.get_rect(center=(400, 400))
        screen.blit(exit_text, exit_rect)
        # Mute Button
        mute_on_img = pygame.image.load('assets/mute2.png')
        mute_off_img = pygame.image.load('assets/mute1.png')
        mute_on_rect = mute_on_img.get_rect(center=(760, 40))
        mute_off_rect = mute_off_img.get_rect(center=(760, 40))
        if mixer.music.get_volume() == 0:
            screen.blit(mute_off_img, mute_off_rect)
        else:
            screen.blit(mute_on_img, mute_on_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                click.play()
                sleep(0.2)
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and play_again_rect.collidepoint(event.pos):
                click.play()
                main_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and exit_rect.collidepoint(event.pos):
                click.play()
                sleep(0.2)
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (mute_on_rect.collidepoint(event.pos) or mute_off_rect.collidepoint(event.pos)):
                if mixer.music.get_volume() == 0:
                    click.play()
                    volume(0.6)
                else:
                    click.play()
                    volume(0)
        pygame.display.update()


def main_menu():
    while True:
        screen.fill(black)
        screen.blit(background_image, (0, 0))
        # Mute Button
        mute_on_img = pygame.image.load('assets/mute2.png')
        mute_off_img = pygame.image.load('assets/mute1.png')
        mute_on_rect = mute_on_img.get_rect(center=(760, 40))
        mute_off_rect = mute_off_img.get_rect(center=(760, 40))
        if mixer.music.get_volume() == 0:
            screen.blit(mute_off_img, mute_off_rect)
        else:
            screen.blit(mute_on_img, mute_on_rect)
        # Sound Puzzle
        name_text = get_font(60).render("ΗΧΗΤΙΚΟ ΠΑΖΛ", True, white)
        name_rect = name_text.get_rect(center=(400, 125))
        screen.blit(name_text, name_rect)
        # Play Button
        play_text = get_font(40).render("ΕΝΑΡΞΗ", True, white)
        play_rect = play_text.get_rect(center=(400, 300))
        screen.blit(play_text, play_rect)
        # Exit Button
        exit_text = get_font(40).render("ΕΞΟΔΟΣ", True, white)
        exit_rect = exit_text.get_rect(center=(400, 400))
        screen.blit(exit_text, exit_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                click.play()
                sleep(0.2)
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and play_rect.collidepoint(event.pos):
                click.play()
                play()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and exit_rect.collidepoint(event.pos):
                click.play()
                sleep(0.2)
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and (mute_on_rect.collidepoint(event.pos) or mute_off_rect.collidepoint(event.pos)):
                if mixer.music.get_volume() == 0:
                    click.play()
                    volume(0.6)
                else:
                    click.play()
                    volume(0)
        pygame.display.update()


# Execute main game
if __name__ == '__main__':
    pygame.mixer.music.play(-1)
    main_menu()
