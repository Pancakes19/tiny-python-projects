# text based adventure game

print('""""""""""""""""""""""""""""""""""""""""""""""""')
print('            Welcome to to the game ')
print('""""""""""""""""""""""""""""""""""""""""""""""""\n')

play = input('Press P to play and Q to quit: \n')

if play == 'p':
    health = 100
    attack = 100
    char = int(input('Choose your character:\n1. Wizard   2. knight\n'))
    if char == 1:
        print('""""""""""""""""""""""""""""""""""""""""""""""""')
        print(f'health: {health}                          Attack: {attack}\n\n')
        print('You have been re-incarnated as a powerful\nWizard in the magical land of Quintopia.\nIf you look on your left, u see a great,\nvast river and if you look to your right,\nu see an enormous forest\n')
        c1 = int(input('Which path do u wish to tread upon\n1. Left      2. Right\n'))
        if c1 == 1:
            print('You walk for 3 minutes towards the\nriver and after finally getting there,\nu see a giant grizzly bear gaurding a\ncanoe for some weird reason\n')
            c1a = int(input('do u:\n1. turn back     2. attack the bear with a quinto blast'))
        
        
        
        
        
        
        
        
        
        
        
        
    elif char == 2:
        print('""""""""""""""""""""""""""""""""""""""""""""""""')
        print(f'health: {health}                      Attack: attack')
    else:
        print('invalid choice')






else:
    print('bye')
    





























