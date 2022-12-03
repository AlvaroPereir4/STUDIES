from modelo import *
filme1 = Filme('estranho Mundo de Jack', 2010, '2h')
serie1 = Serie('Atlanta', 2019, 3)

planejamento_fds = Playlist(filme1, serie1)
for programa in planejamento_fds:
    print(programa)