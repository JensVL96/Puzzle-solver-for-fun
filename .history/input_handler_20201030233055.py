class Input_handler():
    def __init__(self):
        pass

    def event_keys(self, ):
        if event.type == pg.MOUSEBUTTONDOWN:
                flag1 = 1
                pos = pg.mouse.get_pos()
                get_cord(pos)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                val = 1
            if event.key == pg.K_2:
                val = 2
            if event.key == pg.K_3:
                val = 3
            if event.key == pg.K_4:
                val = 4
            if event.key == pg.K_5:
                val = 5
            if event.key == pg.K_6:
                val = 6
            if event.key == pg.K_7:
                val = 7
            if event.key == pg.K_8:
                val = 8
            if event.key == pg.K_9:
                val = 9