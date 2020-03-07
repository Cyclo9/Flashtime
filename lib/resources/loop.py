status = 1
while status:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = 0