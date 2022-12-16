﻿# The script of the game goes in this file.

init python:
    # general
    color = "#39876c"
    selected = " "
    count = 0
    aproach = False
    badEnd = 0
    goodEnd = 0
    player_name = ""
    # backyard scene
    search_backyard = False
    by_door = False
    by_tree = False
    by_sniff = False
    finish_search = False
    # Neighbour part 2 scene
    met_clara = False
    explored_claras = False
    scared_cockatiel = False
    # Street scene
    follow_dog = False
    #findingSuspect scene
    question1 = False
    question2 = False
    question3 = False

# Characters
define narrative = Character(" ")
define cat = Character("Você", color ="#c8c7c9")
define vincent = Character("Vicente", color = "#4ddb65")
define teresa = Character("Teresa", color = '#9a63d6')
define orange = Character("Laranjinha", color = "#e07e34")
define strange = Character("???", color = color)
define josue = Character("Josué", color = "#3ea5b3")
define clara = Character("Clara", color = "#182966")
define cockatiel = Character("Calopsita", color = "#c7bc5a")
define femalecat = Character("Gata", color = "#636362")
define kid = Character("Criança", color = "#5e251f")
define crow = Character("Corvo", color = "#2b2727")
define clotilde = Character("Clotilde", color = "#dd3af2")
define frederico = Character("Frederico", color = "#4ad4f0")
define barbara = Character("Bárbara", color = "#39876c")
define radio = Character("Rádio", color = "#542236")
define manchinha = Character("Manchinha", color = "#dbca0f")
define dog = Character("Border Collie", color = "#ed310c")

image vincent_mad = "images/sprites/vincent_mad.png"
image vincent_sad = "images/sprites/vincent_sad.png"
image vincent_happy = "images/sprites/vincent_happy.png"
image vincent_neutral = "images/sprites/vincent_neutral.png"
image vincent_scared = "images/sprites/vincent_scared.png"
image vincent_embarrassed = "images/sprites/vincent_embarrassed.png"
image vincent_suspicious = "images/sprites/vincent_suspicious.png"
image vincent_angry = "images/sprites/vincent_angry.png"
image cat_happy = "images/sprites/cat_happy.png"
image cat_angry = "images/sprites/cat_angry.png"
image cat_bored = "images/sprites/cat_bored.png"
image cat_confident = "images/sprites/cat_confident.png"
image cat_determinated = "images/sprites/cat_determinated.png"
image cat_discussion = "images/sprites/cat_discussion.png"
image cat_funny = "images/sprites/cat_funny.png"
image cat_hunting = "images/sprites/cat_hunting.png"
image cat_love = "images/sprites/cat_love.png"
image cat_mad = "images/sprites/cat_mad.png"
image cat_sad = "images/sprites/cat_sad.png"
image cat_sad2 = "images/sprites/cat_sad2.png"
image cat_satisfied = "images/sprites/cat_satisfied.png"
image cat_surprised = "images/sprites/cat_surprised.png"
image cat_suspicious = "images/sprites/cat_suspicious.png"
image cat_suspicious2 = "images/sprites/cat_suspicious2.png"
image dog_neutral = "images/sprites/dog.png"
image cockatiel_neutral = "images/sprites/cockatiel.png"
image kid_neutral = "images/sprites/kid.png"
image clotilde_neutral = "images/sprites/clotilde.png"
image femalecat_neutral = "images/sprites/femalecat.png"
image manchinha_neutral = "images/sprites/manchinha.png"
image crow_neutral = "images/sprites/crow.png"
image orange_neutral = "images/sprites/orange.png"
image college_dude1 = "images/sprites/college_dude1.png"
image college_dude2 = "images/sprites/college_dude2.png"
image josue_careful = "images/sprites/josue_careful.png"
image josue_mad = "images/sprites/josue_mad.png"
image josue_happy = "images/sprites/josue_happy.png"
image josue_neutral = "images/sprites/josue_neutral.png"
image teresa_angry = "images/sprites/teresa_angry.png"
image teresa_careful = "images/sprites/teresa_careful.png"
image teresa_happy = "images/sprites/teresa_happy.png"
image teresa_joy = "images/sprites/teresa_joy.png"
image teresa_neutral = "images/sprites/teresa_neutral.png"
image teresa_sad = "images/sprites/teresa_sad.png"
image teresa_surprised = "images/sprites/teresa_surprised.png"
image teresa_worried = "images/sprites/teresa_worried.png"
image frederico_angry = "images/sprites/frederico_angry.png"
image frederico_mad = "images/sprites/frederico_mad.png"
image frederico_neutral = "images/sprites/frederico_neutral.png"
image frederico_scared = "images/sprites/frederico_scared.png"
image clara_angry = "images/sprites/clara_angry.png"
image clara_happy = "images/sprites/clara_happy.png"
image clara_interested = "images/sprites/clara_interested.png"
image clara_mad = "images/sprites/clara_mad.png"
image clara_neutral = "images/sprites/clara_neutral.png"
image clara_relieved = "images/sprites/clara_relieved.png"
image clara_surprised = "images/sprites/clara_surprised.png"
image clara_suspicious = "images/sprites/clara_suspicious.png"
image clara_worried = "images/sprites/clara_worried.png"

# Flipped 
image v_neutral = im.Flip("images/sprites/vincent_neutral.png", horizontal = True)
image v_happy = im.Flip("images/sprites/vincent_happy.png", horizontal = True)
image v_suspicious = im.Flip("images/sprites/vincent_suspicious.png", horizontal = True)
image v_embarrassed = im.Flip("images/sprites/vincent_embarrassed.png", horizontal = True)
image v_angry = im.Flip("images/sprites/vincent_angry.png", horizontal = True)
image t_neutral = im.Flip("images/sprites/teresa_neutral.png", horizontal = True)
image t_happy = im.Flip("images/sprites/teresa_happy.png", horizontal = True)
image college_dude3 = im.Flip("images/sprites/college_dude1.png", horizontal = True)
image college_dude4 = im.Flip("images/sprites/college_dude2.png", horizontal = True)
image k_neutral = im.Flip("images/sprites/kid.png", horizontal = True)
image c_happy = im.Flip("images/sprites/clara_happy.png", horizontal = True)
image c_interested = im.Flip("images/sprites/clara_interested.png", horizontal = True)

# Backgrounds
image bg_white = "images/backgrounds/white_bg.jpg"
image bg_black = "images/backgrounds/black_bg.jpg"
image bg_bedroom = "images/backgrounds/bedroom.png"
image bg_backyard = "images/backgrounds/backyard.png"
image bg_tree = "images/backgrounds/tree.jpg"
image bg_housedoor = "images/backgrounds/housedoor.png"
image bg_outside = "images/backgrounds/outside.png"
image bg_park = "images/backgrounds/park.png"
image bg_street = "images/backgrounds/street.png"
image bg_manhole = "images/backgrounds/manhole.png"
image bg_office = "images/backgrounds/office.png"
image bg_alley = "images/backgrounds/alley.png"
image bg_dude = "images/backgrounds/dude_house.jpg"
image bg_josue = "images/backgrounds/josue_house.jpg"
image bg_clara = "images/backgrounds/clara_house.jpeg"
image bg_kennel = "images/backgrounds/kennel.png"
image bg_machine ="images/backgrounds/machine.png"

# The game starts here.
label start:
    stop music
    jump flashback
    return

# ----- Scenes -----

# Barbara's death flashback (Scene 0)
label flashback: # (Don't change)

    narrative "Você está aturdido e com a respiração entrecortada. Uma melodia ardente, aguda e dolorosa mexe com todos seus sentidos. Seus olhos pesam, suas costas ardem, o mundo parece estar girando e você não consegue diferenciar cima de baixo."
    narrative "Uma figura sombria aparece de repente "

    #grito
    play sound "audio/sounds/mulher gritando.mp3"

    strange "O-o que você fez?"
    stop sound

    narrative "A voz soava dolorosamente familiar, de uma maneira que seus sentidos exclamam que deveria ser confortante mas você apenas sentia uma dor aguda em seu coração."
    narrative "Você se perdeu em suas emoções, sentindo calafrios percorrendo todo o seu corpo."
    narrative "Outra figura sombria aparece"

    $color = "#4ad4f0"
    $strange = Character("???", color = color)

    strange "Isso é algo que você não deveria ter se metido."
    strange "Eu diria para você ter mais cuidado na próxima vez, mas não haverá próxima vez."

    #tiro
    play sound "audio/sounds/tirasso.mp3"

    menu:
        "1 - Seguir a sombra.":
            $selected = "Follow"

        "2 - Correr da sombra.":
            $selected = "Run"

    call flashbackChoices from _call_flashbackChoices
    jump vicentes
    return

# Vicent's house (Scene 1)
label vicentes: # (Dont't change)
    scene bg_bedroom:
        zoom 0.4
    with dissolve

    play music "audio/musics/CatJazz 1.wav"

    narrative "Um zunido estourado ecoa pelo quarto. Foi o suficiente para fazer você acordar."

    show cat_angry at center:
        zoom 0.3
        yalign 0.6
        xalign 1
    with dissolve

    cat "Agh, o que há com esse maldito rádio? Talvez roubá-lo não foi uma boa ideia."
    cat "Se bem que seus conteúdos são muito mais interessantes que qualquer coisa que você poderia encontrar no jornal do Vicente."
    narrative "Você pisca freneticamente de forma que seus olhos se acostumassem mais com a luz do dia."
    narrative "O rádio da viatura estava em cima do balcão junto com um monte de outras coisas."

    play sound "audio/sounds/radio-interferencia.mp3"

    narrative "*Estática*"
    radio "Chamando unidades próximas, repito…"

    stop sound

    narrative "Um homem se aproxima. Você o observa caminhando com seus passos barulhentos até o rádio e o desligando."
    cat "Ei, o cara ia falar algo que podia ser importante!"

    hide cat_angry
    show cat_angry at left:
        zoom 0.3
        yalign 0.6
        xalign 1
    with dissolve

    show v_angry at center:
        zoom 0.5
    with dissolve

    vincent "De novo esse troço no volume máximo, foi você quem mexeu?"
    narrative "Vicente o encara por alguns segundos e em seguida, pega um objeto que estava em cima da cadeira."
    narrative "Era um rato de borracha todo estraçalhado. Sua segunda maior vigarice depois de cagar na cama de Vicente por não trocar sua caixa de areia, claro."
    
    hide v_angry
    show v_happy at center:
        zoom 0.5
    with dissolve

    narrative "Vicente se aproxima de você com o brinquedo."

    menu:
        "1 - Brincar.":
            $selected = "Play"

        "2 - Tentar ligar o rádio.":
            $selected = "Turn on"

    call vicentesChoices from _call_vicentesChoices

    show cat_suspicious at center:
        zoom 0.3
        yalign 0.6
        xalign 1
    with dissolve

    play sound "audio/sounds/campainha_normal.mp3"
    narrative "*Campainha*"
    narrative "A campainha toca. Curioso, como um bom gato, você vai lá checar."
    stop sound

    hide cat_suspicious
    jump housedoor
    return

# House door (Scene 2)
label housedoor: # (Don't change)
    scene bg_housedoor:
        zoom 0.4
        yalign 0.5
    with dissolve

    narrative "Uma velhinha um pouco desesperada e trajando um conjunto de roupas de lã tremia a beira de sua porta."

    show teresa_worried at center:
        zoom 0.6
    with dissolve

    cat "Senhora Teresa…"
    cat "Vive na vizinhança e tem um vício em tricotar casacos de lã. Eu a visito de vez em quando, é uma boa companhia desde que você esteja disposto a suportar o cheiro de repolho que permeia em sua casa."
    narrative "Você se esfrega na perna de Teresa em ziguezague, para deixar o seu cheiro. Muito mais agradável."
    teresa "Vicente, querido! A Clotildes sumiu, preciso de sua ajuda."

    show cat_happy at left:
        zoom 0.5
        yalign 1.1
    with dissolve

    cat "Clotilde sumiu? Amém?! Os dias de glória chegaram."
    narrative "Seu humor elevou alguns pontos."

    show v_happy at right:
        zoom 0.5
    with dissolve

    vincent "Ah, Teresa!"

    hide v_happy
    show v_suspicious at right:
        zoom 0.5
    with dissolve

    vincent "A Clotilde sumiu? Tem certeza que ela não saiu por conta própria?"
    teresa "Ela é minha querida companheira, está comigo há 12 anos. Ela é meio ceguinha, mas conhece a vizinhança, nunca sumiria por tanto tempo."

    hide cat_happy
    show cat_suspicious at left:
        zoom 0.5
        yalign 1.1
    with dissolve

    cat "Meio ceguinha? Aquela cachorra sanguinária não conseguiria ver seu próprio nariz nem se tentasse."
    vincent "Poxa, não sei se posso deixar minhas investigações para ir atrás dela, já tenho tanta coisa para fazer."
    teresa "Deixa disso meu anjo, como você não vai ajudar uma senhorinha de idade como eu?"
    vincent "…"

    hide teresa_worried
    show teresa_joy at center:
        zoom 0.6
    with dissolve

    teresa "Eu pago uma boa quantia para você, sei que está precisando, e ainda te faço um belo suéter de lã."
    teresa "Sei que você acabou perdendo os outros que eu dei."

    hide v_suspicious
    show v_embarrassed at right:
        zoom 0.5
    with dissolve

    vincent "Ah, sim, realmente…"
    narrative "Vicente desvia o olhar diretamente a você."

    hide cat_suspicious
    show cat_surprised at left:
        zoom 0.5
        yalign 1.1
    with dissolve

    cat "Blasfêmia!"
    cat "Não olhe para mim! Eles estavam pedindo para serem afofados pelas minhas garras."

    hide v_embarrassed
    show v_neutral at right:
        zoom 0.5
    with dissolve

    narrative "Vicente suspira."
    vincent "Tudo bem, então. Acho que consigo dar uma procurada pela vizinhança."

    hide cat_surprised
    show cat_confident at left:
        zoom 0.5
        yalign 1.1
    with dissolve

    cat "Fraco. Não resiste a uma chantagem emocional de uma senhorinha..."

    hide teresa_joy
    show teresa_happy at center:
        zoom 0.6
    with dissolve

    teresa "Ai, que maravilha! Já vou pegar minhas agulhas de tricô!"
    vincent "Calma! Vamos com calma… Primeiro, preciso saber quando foi a última vez que a senhora viu a Clotilde."

    hide teresa_happy
    show teresa_worried at center:
        zoom 0.6
    with dissolve

    teresa "Ah sim, querido. Eu estava em casa, fazendo bolinho de chuva com repolho e ela estava no quintal. Então ouvi vários latidos da Clotilde, sabe como é né… ela é toda animadinha."
    cat "Animadinha? Essa cachorra é maluca!"
    teresa "Ela sempre faz isso. Começa a latir e persegue quem está passando na rua até o final do quintal. Mas ela sempre volta toda cansadinha para dentro de casa."
    teresa "Então achei estranho quando não a ouvi mais."

    hide v_neutral
    show v_suspicious at right:
        zoom 0.5
    with dissolve

    vincent "De fato, estranho… Você olhou para ver se ela ainda estava no seu quintal?"
    teresa "Olhei por toda parte e não a encontrei."
    teresa "O que eu farei com todas essas roupinhas que eu fiz para minha amada Clotilde…"

    hide teresa_worried
    show t_neutral at center:
        zoom 0.6
    with dissolve

    narrative "Teresa dá uma olhada para você e começa a encará-lo com interesse."

    hide cat_confident
    show cat_surprised at left:
        zoom 0.5
        yalign 1.1
    with dissolve

    cat "Não, não, não. Nem pense nisso."

    hide v_suspicious
    show v_happy at right:
        zoom 0.5
    with dissolve

    hide t_neutral
    show teresa_happy at center:
        zoom 0.6
    with dissolve

    teresa "Talvez o pequenino poderia me fazer companhia enquanto você encontra minha Clotilde?"
    vincent "Não acho que ele vai ter um problema com isso, não é, Gato?"
    cat "Ei, eu não tenho fala nos meus direitos como gato?"

    menu:
        "1 - Ficar na casa.":
            $selected = "Stay"

        "2 - Dar no pé.":
            $selected = "Go away"

    call housedoorChoices from _call_housedoorChoices
    jump outside
    return

# Outside (Scene 3)
label outside: # (Don't change)
    stop music
    scene bg_outside:
        zoom 0.4
    with dissolve

    play music "audio/sounds/praca_cidade.mp3"

    narrative "Você fugiu de cena e agora se encontra na rua."

    show cat_satisfied at center:
        zoom 0.3
    with dissolve

    cat "Eu não vou voltar lá dentro enquanto aquela mulher estiver lá."

    hide cat_satisfied
    show cat_sad at center:
        zoom 0.3
    with dissolve

    cat "Mas eu queria tanto passar a tarde dormindo na minha cama quentinha..."

    hide cat_sad
    show cat_surprised at center:
        zoom 0.3
    with dissolve

    cat "Já sei! Quanto antes a maluca da Clotilde for encontrada, mais rápido a gente se livra da Teresa!"
    narrative "Não é como se você odiasse Teresa. Você gosta dela, apenas… em uma distância saudável daquelas mãos maquiavélicas de tricô."
    cat "Acho que o melhor lugar para começar vai ser no quintal dela. Ela falou que lá foi o último lugar que Clotilde foi vista."
    narrative "Você corre em direção a casa da Teresa."

    hide cat_surprised
    jump backyard
    return

# Teresa's backyard (Scene 4)
label backyard: # (Don't change)
    scene bg_backyard:
        zoom 0.5
    with dissolve

    narrative "Você avista Vicente de longe, que já estava no quintal de Teresa e parecia estar registrando algo em seu bloco de notas."

    show cat_confident at right:
        zoom 0.3
        xalign 0.7
    with dissolve

    cat "Aposto que ele está precisando de ajuda."
    cat "Com minha ajuda esse caso será mais fácil que roubar petisco de filhote."

    menu:
        "1 - Se aproximar de Vicente.":
            $selected = "Vincent"
            stop music
            play music "audio/musics/CatJazz 3.mp3"
            call backyardChoices from _call_backyardChoices

            menu:
                "1 - Seguir Vicente.":
                    hide cat_confident with dissolve
                    narrative "Vicente e você saem do quintal de Teresa e vão visitar um dos vizinhos."
                    jump neighboursPt1

                "2 - Investigar o quintal.":
                    $search_backyard = True

        "2 - Investigar o quintal.":
            $search_backyard = True

    if search_backyard == True:
        stop music
        play music "audio/musics/CatJazz 3.mp3"
        narrative "Você decide ignorar Vicente e explorar o quintal de Teresa por conta própria."
        cat "Onde eu deveria explorar?"
        
        while finish_search == False:
            call backyardSearch from _call_backyardSearch
            hide cat_confident with dissolve

            if selected != " ":
                call backyardChoices from _call_backyardChoices_1
            
                if selected == "Sniff":
                    call catAproach from _call_catAproach
                if by_door == True and by_tree == True and by_sniff == True:
                    $finish_search = True
        
        narrative "Você contempla, se sentindo um pouco derrotado, o que fazer agora que coletou essas informações."
        cat "É, trabalhamos com o que temos."
        cat "Não achei muita coisa. Mas parece que o fato de Clotilde não ter voltado não foi por escolha própria, considerando que sua portinha estava trancada."
        cat "Mas ainda tenho poucas pistas."
        cat "Talvez você conseguiria informações com o Vicente?"
        narrative "Você começa a falar consigo mesmo em segunda pessoa, por algum motivo."
        cat "Mas como você iria pegar a informação de Vicente? Talvez seria melhor procurar por conta própria."
        cat "Afinal de contas, Clotilde foi atrás de um carro, então deve ter seguido a direção da rua."

        menu:
            "1 - Procurar por Vicente.":
                narrative "Você vai a procura de Vicente, seguindo seu cheiro."
                jump neighboursPt2

            "2 - Seguir a rua.":
                narrative "Você corre para fora do quintal, seguindo a rua em busca de alguma pista de onde Clotilde foi."
                jump street
    return

# Neighbours part 1 (Scene 5)
label neighboursPt1: # (Don't change)
    scene dude_house:
        zoom 2.0
        yalign 0.8
    with dissolve
    narrative "Vicente se aproxima do vizinho mais próximo a casa da Teresa e toca a campainha"

    show vincent_neutral at left:
        zoom 0.5
    with dissolve

    play sound "audio/sounds/campainha_normal.mp3"
    narrative "*campainha*"
    stop sound
    narrative "Um jovem abre a porta. Ele parece ser um universitário."

    show college_dude3 at right:
        zoom 0.5
    with dissolve

    strange "Opa! Boa tarde?"
    cat "Que cheiro podre é esse??"
    cat "Esse cara não conhece o conceito de chuveiro?"
    vincent "Boa tarde"
    vincent "Desculpa incomodar, mas por acaso você viu por aí um cachorrinho pequeno, com os olhos esbugalhados?"
    vincent "Ele é meio velhinho e usava um casaco de lã."
    strange "Aquele demoniozinho da dona Tereza?"
    cat "Na mosca!"

    hide vincent_neutral
    show vincent_happy at left:
        zoom 0.5
    with dissolve

    vincent "Esse mesmo!"
    vincent "Você chegou a ver ele por aí?"

    hide college_dude3
    show college_dude4 at right:
        zoom 0.5
    with dissolve

    strange "Ô tio, acabei de acordar, vai com calma... você faz muitas perguntas."
    strange "É policial por acaso?"

    hide vincent_happy
    show vincent_suspicious at left:
        zoom 0.5
    with dissolve

    vincent "Sou um jornalista e estou começando a carreira como detetive, mas isso não vem ao caso."

    hide college_dude4
    show college_dude3 at right:
        zoom 0.5
    with dissolve

    strange "Tá começando a carreira bem... indo atrás de um cachorro perdido."
    cat "Acabou de acordar e já está jantando o Vicente assim?"
    narrative "Você olha atento para a discussão se desenrolando à sua frente."

    hide vincent_suspicious
    show vincent_angry at left:
        zoom 0.5
    with dissolve

    vincent "tsc"

    hide vincent_angry with dissolve

    play sound "audio/sounds/porta bate pesado.mp3"
    narrative "Vicente perde a paciência e vai embora."
    stop sound

    narrative "Você fica um pouco decepcionado pela falta de resposta do mais velho."
    narrative "Vicente se dirige a próxima casa, você o segue e se esconde nos arbustos perto da porta."

    jump neighboursPt2
    return

# Neighbours part 2 (Scene 6)
label neighboursPt2: # (Don't change)
    scene bg_clara:
        zoom 2.0
        yalign 0.8
    with dissolve

    $strange = Character("???", color = "#182966")
    narrative "Após um pouco de procura, você encontra Vicente se dirigindo a uma casa da vizinhança."
    narrative "Se escondendo nos arbustos perto da porta você observa."

    play sound "audio/sounds/campainha_normal.mp3"
    narrative "*Campainha*"
    stop sound
    cat "Ele está perguntando para essas outras pessoas?"
    cat "Não deu muito certo comigo, mas é minha culpa por achar que um gato laranja iria ser qualquer outra coisa além de rude."
    cat "Tomara que Vicente tenha mais sorte."

    show v_neutral at right:
        zoom 0.5
    with dissolve

    narrative "Uma mulher vestindo um uniforme de policial abre a porta."

    show clara_interested at left:
        zoom 0.5
    with dissolve

    strange "Pois não?"
    cat "Que cheirinho de sabão!"

    hide v_neutral
    show v_happy at right:
        zoom 0.5
    with dissolve

    vincent "Boa tarde, por acaso você viu uma cadelinha pequena, desse tamanho aqui, que usa casaco de lã?"
    narrative "Vicente faz gestos com as mãos sinalizando o tamanho de Clotilde."

    hide clara_interested
    show clara_surprised at left:
        zoom 0.5
    with dissolve

    strange "Clotilde????"
    cat "Oh céus, ela conhece a peça!"
    vincent "Isso… ela mesma."

    hide clara_surprised
    show clara_worried at left:
        zoom 0.5
    with dissolve

    strange "Tá tudo bem com ela? O que aconteceu?! Tadinha da dona Teresa."

    hide v_happy
    show v_neutral at right:
        zoom 0.5
    with dissolve

    vincent "A Clotilde sumiu e Teresa me chamou para procurar ela, por isso estou juntando informações."
    strange "Ainnn tadinha da Clotilde! O que eu posso fazer para ajudar?"
    vincent "Como eu ia dizendo… estou juntando informações para resolver isso, todo tipo de pista pode ser útil."
    vincent "Tem algo que você viu ou ouviu recentemente que foi suspeito?"

    hide clara_worried
    show clara_neutral at left:
        zoom 0.5
    with dissolve

    strange "Recentemente estive muito ocupada com um caso na delegacia, e não tenho visto a Clotilde."
    strange "Mas eu conheço a Clotilde, ela não é uma cadelinha que iria sumir dessa maneira."
    vincent "Quando foi o último momento que você viu a Clotilde?"
    strange "Se não me engano dois dias atrás."
    strange "Passei para dar um oi para Teresa, ela é uma senhora tão carinhosa."
    cat "Por acaso essa mulher sabe que Teresa está contribuindo para a intoxicação alimentar, com esses bolinhos-de-chuva com recheio de repolho que ela vai oferecendo por aí?"
    vincent "Ela sumiu hoje mais cedo, então provavelmente isso não ajuda muito, mas mesmo assim, obrigado."
    narrative "Vicente pega seu bloquinho de notas e começa a escrever."
    vincent "Me avise se vir algo ou achar ela, moro nessa rua na casa número 35."

    hide clara_neutral
    show clara_worried at left:
        zoom 0.5
    with dissolve

    strange "Desculpa se não fui de muita ajuda, só estive muito ocupada com esse caso de sequestro de animais e não tive tempo para mais nada."
    cat "Sequestro de animais? Aqui no bairro? Interessante, conte mais."

    hide v_neutral
    show v_suspicious at right:
        zoom 0.5
    with dissolve

    vincent "Sequestro?"

    hide clara_worried
    show clara_neutral at left:
        zoom 0.5
    with dissolve

    strange "Sim, mas não posso te contar mais que isso. Confidencial, sabe?"
    cat "Não, eu não sei! Quero saber mais!"
    cat "Tenho sete vidas se a satisfação não me trazer de volta!!"
    cat "Isso parece muito mais interessante que achar essa peste de cachorro perdido."
    vincent "Sim, entendo."
    cat "Calma aí Vicente, isso não gira algumas das engrenagens enferrujadas em sua cabeça?!"
    cat "Estamos procurando uma cadela sumida e essa pessoa está investigando animais sequestrados!"

    hide v_suspicious
    show v_happy at right:
        zoom 0.5
    with dissolve

    vincent "De qualquer forma, muito obrigado pela ajuda. Você sabe como me contactar."
    narrative "Vicente se vira e começa a ir embora."

    hide clara_neutral
    show clara_interested at left:
        zoom 0.5
    with dissolve

    strange "Calma, você nem se apresentou direito. A propósito, meu nome é Clara. E o seu?"

    $met_clara = True

    cat "Típico do Vicente, Não dá uma dentro. Como ela foi dar bola pra ele?"
    cat "E Clara, você tem um péssimo gosto!"
    cat "Ele toma whisky com café."

    hide v_happy
    show v_embarrassed at right:
        zoom 0.5
    with dissolve

    vincent "Perdão, eu acabo me esquecendo desse tipo de coisa. Pode me chamar de Vicente."

    hide clara_interested
    show clara_happy at left:
        zoom 0.5
    with dissolve

    clara "Agora sim! Até mais, Vicente."
    narrative "Vicente sai da porta da casa de Clara e se dirige ao vizinho ao lado."

    hide v_embarrassed with dissolve
    hide clara_happy with dissolve

    cat "Nem dando uma pausa, indo direto para o próximo vizinho."
    cat "Você não cansa não, Vicente?"
    cat "Mas esse caso ai da Clara parece muito mais interessante que achar a maldita da cadela."
    cat "Aposto que consigo entrar na casa dela e achar uns documentos muito mais interessantes."
    cat "Melhor que qualquer coisa que posso ter lido na mesa de Vicente."
    cat "Mas e minha integridade como gato?"
    cat "Devo continuar seguindo o Vicente, ou dar uma visitinha na casa de Clara?"

    menu:
        "1 - Seguir Vicente para o próximo vizinho.":
            jump neighboursPt3v1

        "2 - Investigar a casa de Clara.":
            $explored_claras = True
            narrative "Você decide infiltrar-se na casa de Clara, quem pode imaginar o que você vai encontrar?"
            narrative "Usando a janela que se encontrava aberta, você entra na casa."
            cat "Mais bagunçado do que imaginei."
            cat "Não é por nada que ela não queria que Vicente entrasse na casa dela."
            narrative "Você explora a sala, encontrando vários papéis por todo lugar."
            cat "Ta um chiqueiro aqui dentro."
            cat "Não dá pra imaginar quanto tempo vai demorar para encontrar qualquer coisa nessa bagunça!"
            cat "Eu sou um gato ocupado, não tenho tempo a perder com isso."
            narrative "Enquanto você contempla o que fazer, seus pensamentos são interrompidos pelo barulho de asas batendo."
            narrative "Olhando para o lado, você percebe que uma Calopsita acabou de pousar sobre um dos montes de papéis."

            show cockatiel_neutral at right:
                zoom 0.1
                yalign 0.5
                xalign 0.7
            with dissolve

            cat "Como se a situação não pudesse piorar."
            cat "Esses pássaros bobos só sabem fazer barulho e atrapalhar."
            cat "Talvez eu devesse ensinar uma lição a esse rato com penas."

            menu:
                "1 - Assustar a calopsita.":
                    $scared_cockatiel = True
                    $selected = "Scare"

                "2 - Deixar a Calopsita em paz.":
                    $selected = "Ignore"

            if selected != " ":
                call clarasHouseChoices from _call_clarasHouseChoices
                jump neighboursPt3v2

    return

# Neighbours part 3 (Scene 7)
label neighboursPt3v1: # (Don't change)
    scene bg_josue:
        zoom 2.0
        yalign 0.8
    with dissolve

    $strange = Character("???", color = "#3ea5b3")
    narrative "Vicente se aproxima da porta e toca a campainha."

    play sound "audio/sounds/campainha_normal.mp3"
    narrative "*campainha*"
    stop sound

    show vincent_neutral at left:
        zoom 0.5
        xalign 0.3
    with dissolve

    narrative "Um homem mau encarado atende a porta."

    show josue_mad at right:
        zoom 0.5
        xalign 0.7
    with dissolve

    strange "Quem é você?"
    cat "Esse aí tem cara de suspeito."
    vincent "Sou o Vicente Jones, moro aqui na vizinhança. Estou procurando por um cachorro, por acaso você viu alguma coisa?"
    strange "Vicente Jones? Acho que eu ouvi falar... você é aquele jornalista da casa 35?"
    cat "Ele conhece o Vicente?"
    vincent "Sim, sou eu. Você viu algo sobre-"

    hide josue_mad
    show josue_happy at right:
        zoom 0.5
        xalign 0.7
    with dissolve

    narrative "Assim que o homem escuta a confirmação, sua expressão muda para uma mais amigável e ele interrompe Vicente."
    strange "Teresinha me falou sobre você... minha esposa também me deixou. Vai ficar tudo bem, não é culpa sua."

    hide vincent_neutral
    show vincent_scared at left:
        zoom 0.5
        xalign 0.3
    with dissolve

    narrative "Vicente entra em um pequeno estado de choque."
    narrative "É nítido para você que a fala desse homem afetou ele."
    narrative "Assim como também te afetam vagarosamente."
    cat "Mas quem é esse cara?"
    cat "Por que ele está dizendo essas coisas?"
    narrative "O homem apoia o braço no ombro de Vicente."
    strange "Meu nome é Josué, trabalho como eletricista."
    josue "Se estiver precisando de amigos pode contar comigo."
    narrative "Vicente ainda parece atordoado com a situação, um pouco constrangido."
    narrative "Você também acaba ficando perdido em seus pensamentos"
    josue "Sou amigo da Teresa, adoro tomar café com ela, comendo aqueles deliciosos bolinhos de chuva."
    cat "Esse cara gosta daqueles bolinhos!"
    josue "Já faz um tempo que ela me fala sobre você."

    hide vincent_scared
    show vincent_suspicious at left:
        zoom 0.5
        xalign 0.3
    with dissolve

    narrative "Vicente volta a consciência, piscando algumas vezes mais que o normal."
    vincent "Ah... que bom que conhece a Teresa, assim fica mais fácil de explicar."
    vincent "A Clotilde sumiu, estou procurando ela. Você a viu em algum lugar?"

    hide josue_happy
    show josue_neutral at right:
        zoom 0.5
        xalign 0.7
    with dissolve

    josue "Hoje mais cedo vi ela correndo atrás de um motoqueiro."
    vincent "Em qual direção o motoqueiro estava indo?"
    josue "Acho que estava indo em direção ao parque."
    vincent "Mais alguma informação?"

    hide josue_neutral
    show josue_happy at right:
        zoom 0.5
        xalign 0.7
    with dissolve

    josue "Tenho folga na sexta, se quiser ir em um barzinho para conversarmos."
    narrative "Mais uma vez, Vicente se perde um pouco do foco das coisas, olhando para os lados."
    cat "Cansei desses papinhos de humanos!"
    cat "Acho melhor ir direto para o parque, eles que fiquem aqui conversando."
    narrative "Vicente continua a conversa com Josué enquanto você segue para o parque."

    jump park
    return

# Neighbours Part 3.2 (Scene 7.2)
label neighboursPt3v2: # (Don't change)

    scene bg_josue:
        zoom 2.0
        yalign 0.8
    with dissolve

    show vincent_scared at left:
        zoom 0.5
        xalign 0.3
    with dissolve

    show josue_happy at right:
        zoom 0.5
        xalign 0.7
    with dissolve

    narrative "Seguindo o cheiro de Vicente você se depara com uma cena extremamente estranha."
    narrative "Vicente se encontrava na frente da porta com um estranho com o braço sobre seu ombro."
    narrative "Vicente parece atordoado com a situação, um pouco constrangido." 
    narrative "Você também acaba ficando perdido em seus pensamentos." 
    cat "É por isso que você não nota os avanços das moças Vicente"
    cat "Não sabia que você era inclinado para esse lado…"
    strange "Sou amigo da Teresa, adoro tomar café com ela, comendo aqueles deliciosos bolinhos de chuva."
    strange "Já faz um tempo que ela me fala sobre você."
    cat "Acho que não estou entendendo algo aqui."

    hide vincent_scared
    show vincent_suspicious at left:
        zoom 0.5
        xalign 0.3
    with dissolve

    narrative "Vicente volta a consciência, piscando algumas vezes mais que o normal."
    vincent "Ah… Que bom que conhece a Teresa, assim fica mais fácil de explicar."
    vincent "A Clotilde sumiu, estou procurando ela. Você a viu em algum lugar?"

    hide josue_happy
    show josue_neutral at right:
        zoom 0.5
        xalign 0.7
    with dissolve

    strange "Hoje mais cedo vi ela correndo atrás de um motoqueiro."
    vincent "Em qual direção o motoqueiro estava indo?"
    strange "Acho que estava indo em direção ao parque."
    vincent "Mais alguma informação?"

    hide josue_neutral
    show josue_happy at right:
        zoom 0.5
        xalign 0.7
    with dissolve

    strange "Tenho folga na sexta, se quiser ir em um barzinho para conversarmos."
    narrative "Mais uma vez, Vicente perde um pouco o foco das coisas, olhando para os lados."
    cat "Cansei desses humanos flertando."
    narrative "Acho melhor ir direto para o parque, eles que fiquem aqui conversando."
    narrative "Vicente continua a conversa com Josué enquanto você segue para o parque."

    jump park
    return

# Street (Scene 8)
label street: # (Don't change)
    stop music
    play music "audio/sounds/praca_cidade.mp3"
    scene bg_street:
        zoom 0.4
        yalign 0.3
    with dissolve

    narrative "Você corre pela rua, procurando por Clotilde ou qualquer informação útil ao seu alcance, até que começa a ficar cansado."
    cat "Puff Puff."
    cat "Estou correndo por tanto tempo, mas ainda não encontrei nada!"
    cat "Talvez eu deveria ter ido atrás do Vicente…"
    cat "Não! Eu não deveria precisar de ajuda. Eu sozinho deveria ser o suficiente para encontrar um estúpido cachorro."
    narrative "Você se senta, decepcionado."
    cat "Mas eu não entendo. Clotilde deveria ter seguido rua abaixo na direção em que os carros estão indo!"
    narrative "De repente, uma gata aparece. Ela parece estar procurando por comida em uma lata de lixo."
    cat "Humm, conversar com outro animal não deu muito certo antes, mas pode ter sido porque ele era um gato laranja."

    menu:
        "1 - Se aproximar da gata.":
            $selected = "Aproach"
            call streetChoices from _call_streetChoices
            jump park
        
        "2 - Continuar seguindo.":
            $selected = "Ignore"
            call streetChoices from _call_streetChoices_1

            menu:
                "1 - Seguir cachorro suspeito.":
                    $selected = "Follow"
                    $follow_dog = True
                    call streetChoices from _call_streetChoices_2
                    jump home

                "2 - Esperar cachorro ir embora e continuar procurando.":
                    $selected = "Wait"
                    $follow_dog = False
                    call streetChoices from _call_streetChoices_3
                    jump home
    return

# Park (Scene 9)
label park: # (Don't change)
    stop music
    play music "audio/sounds/praca_cidade.mp3"
    scene bg_park:
        zoom 0.4
        xalign 0.8
        yalign 0.5
    with dissolve

    narrative "Você chega no parque do bairro com seus espíritos renovados."

    show cat_determinated at center:
        zoom 0.3
        xalign 0.9
    with dissolve

    cat "Ok! Agora é só focar em encontrá-la."
    cat "Ela deve ter deixado algum rastro que possa me ajudar."
    cat "Só me resta saber onde começo a procurar…"
    narrative "No entanto, antes que pudesse terminar a linha de raciocínio uma dor aguda é sentida em seu rabo."
    narrative "Você grita de dor e pula uns 2 metros de altura, subindo no poste de luz que tinha ali."

    hide cat_determinated
    show cat_surprised at center:
        zoom 0.3
        xalign 0.9
    with dissolve

    cat "O QUE ESTÁ ACONTECENDO?"

    hide cat_surprised
    show cat_angry at center:
        zoom 0.3
        xalign 0.9
    with dissolve

    narrative "Seus olhos enchiam de sangue. "
    narrative "Metaforicamente falando, claro."
    narrative "Um homem alto, loiro e trajando um terno bege, era o culpado de quase ter te deixado sem um rabo." 
    narrative "E na mesma proporção que você o olhava com ódio ele o olhava com nojo." 

    $strange = Character("???", color = "#4ad4f0")
    show frederico_angry at left:
        zoom 0.4
        xalign 0.3
    with dissolve

    strange "Esse lugar precisa de um controle de gatos urgente."
    narrative "O homem suprimiu um espirro e saiu caminhando pelo mesmo lugar que você tinha chegado." 
    narrative "Ele segurava uma maleta e parecia ser alguém importante."
    narrative "Mas você não dava a mínima, tudo que desejava era que ele caísse em um bueiro e quebrasse a perna."

    hide frederico_angry with dissolve

    cat "Homem arrogante. Como pode falar aquilo?"
    cat "Se acalme, você tem um caso para resolver e um parque a investigar."
    cat "Não ligue para coisas banais como humanos estúpidos com ternos mais estúpidos ainda."
    cat "Onde devo ir?"
    stop music
    play music "audio/musics/CatJazz 1.wav"

    menu:
        "1 - Procurar por rastros perto do parquinho.":
            $selected = "Tracks"
        
        "2 - Investigar bancos do parque.":
            $selected = "Benchs"

        "3 - Procurar pistas perto da rua.":
            $selected = "Clues"
    
    if selected != " ":
        call parkChoices from _call_parkChoices
        if selected == "Tracks":
            menu:
                "1 - Investigar bancos do parque.":
                    $selected = "Benchs"

                "2 - Procurar pistas perto da rua.":
                    $selected = "Clues"
                    call parkChoices from _call_parkChoices_5

        if selected == "Benchs":
            call parkChoices from _call_parkChoices_1
            menu:
                "1 - Perguntar aos pássaros.":
                    $selected = "Ask"
                    call parkChoices from _call_parkChoices_2

                    if explored_claras == True:
                        narrative "Com um choque a realização do que ocorreu passa por sua cabeça."
                        cat "O cara com a Clotilde era o sequestrador de animais!"
                        cat "Eu estava certo! Afinal todos diziam que Clotilde não era uma cadela que saia andando por aí."
                        narrative "Imediatamente você sente a adrenalina surgindo em seu glorioso corpo de gato."
                        cat "Obrigado pela ajuda, corvo, mas preciso ir agora!"        
                    else:
                        cat "O cachorro que o corvo descreveu encaixa direitinho com a Clotilde."
                        cat "Não pode ser que o corvo se confundiu."
                        narrative "Subitamente uma ideia passa por sua cabeça."
                        cat "Já sei!"
                        cat "Alguém pode ter visto Clotilde e decidido ajudá-la."
                        cat "Do jeito que aquela cadela age, qualquer um acharia que ela está em grave necessidade de primeiros socorros."
                        narrative "Com sua mente feita, você decide ir procurar a Clotilde."
                        cat "Quem sabe o quão longe essa pessoa pode ter ido com ela?"
                        narrative "Saindo de seus pensamentos, você vira para o corvo uma última vez."
                        cat "Obrigado pela… ajuda."

                        hide crow_neutral with dissolve
                        hide cat_suspicious with dissolve
                    jump aaaaa

                "2 - Ignorar os pássaros.":
                    $selected = "Ignore"
                    hide cat_suspicious with dissolve
                    call parkChoices from _call_parkChoices_3
                    $selected = "Clues"
                    call parkChoices from _call_parkChoices_4

        if selected == "Clues":
            hide cat_suspicious with dissolve
            menu:
                "1 - Desistir da busca.":
                    $selected = "Give up"
                    jump home
                
                "2 - Continuar andando.":
                    $selected = "Keep going"
                    jump aaaaa
    return

# Clotilde's whereabouts
label aaaaa: # (Don't change)
    stop music
    play music "audio/sounds/praca_cidade.mp3"

    scene bg_street:
        zoom 0.4
        yalign 0.3
    with dissolve

    narrative "Conforme você anda, o cheiro vai ficando mais intenso."
    cat "Eu consigo sentir o cheiro dela!"
    cat "Ela esteve aqui."
    cat "E ela deixou algo aqui que tem o cheiro dela!"
    narrative "Você finalmente encontra, debaixo de uma árvore que fica próxima à calçada, o casaquinho de lã que Clotilde sempre veste."
    cat "Ela sempre veste essa horrorosidade. Ela deve estar próxima daqui."
    cat "Eu provavelmente vou conseguir achá-la seguindo o rastro de cheiro."
    cat "Mas também tem outro cheiro aqui."

    if explored_claras == True:
        cat "Deve ser o cheiro do sequestrador!"
    else:
        cat "Deve ser o cheiro da pessoa que está ajudando Clotilde."

    narrative "Porém você sente algo no cheiro que o confunde."
    cat "Por alguma razão… Sinto que já cheirei essa pessoa?"
    cat "Não é alguém que conheço bem, mas com certeza já me encontrei com ela."
    cat "Meu olfato superior nunca mentiria."
    narrative "Você contempla o novo mistério, mas decide ignorá-lo pelo momento."
    cat "De qualquer maneira, antes de tudo preciso achar Clotilde."
    cat "Novos mistérios podem ser solucionados depois."
    cat "Mas será que eu deveria buscar Vicente primeiro?"
    cat "Ele poderia ser de ajuda…"

    menu:
        "1 - Continuar sem Vicente.":
            $selected = "Without"
            call aaaaaChoices from _call_aaaaaChoices

            menu:
                "1 - Buscar ajuda do Vicente.":
                    $selected = "Help"
                    call aaaaaChoices from _call_aaaaaChoices_1
                    jump clotildeFound
                
                "2 - Eu não preciso de ajuda.":
                    $selected = "By yourself"
                    call aaaaaChoices from _call_aaaaaChoices_2
                    jump rescueV2
        
        "2 - Buscar Vicente.":
            $selected = "With"
            call aaaaaChoices from _call_aaaaaChoices_3
            jump rescueV1  
    return

# Clotilde Found (scene 9.2)
label clotildeFound: # (Don't change)
    stop music
    play music "audio/musics/CatJazz 1.wav"
    narrative "Você volta no último lugar onde acredita ter visto Vicente."
    cat "Onde era mesmo?"
    cat "Lembro-me de ter o visto caminhando em direção ao parque logo quando saí."
    narrative "E é pra lá que você corre com todas suas forças, carregando o fedido e horroroso casaco de lã em sua boca."

    scene bg_park:
        zoom 0.4
        xalign 0.8
        yalign 0.5
    with dissolve

    narrative "Como esperado, não foi difícil achar Vicente, que estava por aí mais perdido que cego em tiroteio. Ou como, Clotilde em tiroteio."
    narrative "Com todo respeito."

    show cat_confident at center:
        zoom 0.3
        xalign 0.9
    with dissolve

    cat "Miau!" 
    cat "Olha o que tenho aqui, Vicente!"
    narrative "Vicente é atraído pelo miado e nota o casaquinho que você esta carregando"

    show vincent_suspicious at right:
        zoom 0.4
        xalign 0.3
    with dissolve

    vincent "Gato, o que você está fazendo com isso?"
    vincent "Onde é que você achou isso?"
    cat "Siga-me!"
    narrative "Você sai correndo arrastando o casaquinho em direção a trajetória que o cheiro de Clotilde leva."
    narrative "Vicente, mesmo sem entender completamente, sai correndo logo atrás de você. Confiando no que você tinha a fazer."

    hide vincent_suspicious
    show vincent_angry at right:
        zoom 0.4
        xalign 0.3
    with dissolve

    vincent "Vai com calma, Gato!"
    vincent "Volte aqui!"
    narrative "Você continua correndo, seguindo o rastro de Clotilde sem olhar pra trás, até chegar em um buraco de bueiro."
    narrative "Vicente o alcançou minutos depois, extremamente ofegante."
    cat "Esse homem tá sedentário, hein."

    jump rescueV1
    return

# The rescue version 1 (scene 9.3)
label rescueV1: # (Don't change)
    stop music
    play music "audio/sounds/praca_cidade.mp3"

    scene bg_manhole:
        zoom 0.4
    with dissolve

    cat "Miau Miau"
    clotilde "Au! Au!"
    narrative "*Latido* *Miado*"
    narrative "Vicente se aproxima do bueiro, observando lá dentro."
    vincent "Clotilde! Como você foi parar aí?"
    narrative "Vicente estica seu braço e pega Clotilde no colo."
    vincent "Vamos te levar de volta para sua dona!"
    vincent "Obrigado, Gato! Você encontrou a roupinha de lã dela."
    cat "Ahn?? Eu encontrei ela!"
    clotilde "Au! Au! Onde estamos indo?"
    vincent "Toma aqui, Clotilde!"
    narrative "Vicente enrola Clotilde na roupinha de lã a levando embora."

    if explored_claras == True:
        cat "Mas que estranho…"
        cat "Onde é que está o sequestrador?"
        cat "O cheiro dele parece desaparecer completamente…"
        cat "É, talvez não era sequestrador mesmo, só uma coincidência."
        cat "Mah, isso tá me dando uma dor de cabeça."
        cat "Agora que a Clotilde está de volta, só quero dormir mesmo."
        narrative "Saindo de seus pensamentos você segue Vicente."
    else:
        cat "Mas que estranho…"
        cat "Onde é que foi parar a pessoa que estava com Clotilde?"
        cat "O cheiro parece desaparecer completamente."
        cat "Meh, talvez eu estava enganado e era só alguém passando."
        cat "Mas quem liga mesmo."
        cat "Agora que a Clotilde foi achado só quero dormir mesmo."
        narrative "Saindo de seus pensamentos você segue Vicente."

    jump livingroom
    return

# The rescue version 2 (scene 9.4)
label rescueV2: # (Don't change)
    stop music
    play music "audio/sounds/praca_cidade.mp3"

    scene bg_manhole:
        zoom 0.4
    with dissolve
        
    narrative "Cerca de alguns minutos se passam, você e Clotilde escutam alguém se aproximando."
    clotilde "Au! Au! Au!"
    cat "Miau! Miau!"
    vincent "Clotilde??"
    vincent "Gato??"
    vincent "O que está acontecendo aqui, como você veio parar aqui?"
    cat "Longa história, Vicente…"
    narrative "Vicente estica seu braço no bueiro, tirando você e Clotilde de lá."
    narrative "Ele pega vocês no colo e os leva de volta para casa."
    narrative "Por alguma razão você sente que esqueceu de algo."

    jump livingroom
    return

# Home - Previous final (scene 11)
label home: # (Don't change)
    stop music
    play music "audio/musics/CatJazz 1.wav"
    scene bg_outside:
        zoom 0.4
    with dissolve

    narrative "Você chega na frente de casa e olha pela janela. Lá dentro você vê de relance a figura de Teresa na cozinha e, conforme se aproxima, o cheiro de bolinho de chuva invade o seu olfato."
    cat "Ela ficou aqui esse tempo todo mesmo?… Bom, não importa. Pelo menos não tem repolho nesse bolinho."
    narrative "Percebendo que ela está entretida, você entra pela janela aberta e se esgueira até o quarto, finalmente deitando na cama."

    scene bg_bedroom:
        zoom 0.4
    with dissolve

    cat "Ahh, acho que vou tirar um cochilo. Espero que Vicente se dê bem na busca."

    scene bg_black:
        zoom 2.0
    with dissolve

    narrative "---------- H O R A S  D E P O I S ----------"
    narrative "*latidos*"

    scene bg_bedroom:
        zoom 0.4
    with dissolve

    narrative "Você acorda em um sobressalto após ouvir latidos agudos que só podem ser da casa de…"
    cat "Teresa?"
    narrative "Os acontecimentos do dia vieram como um flash em sua cabeça e agora ouvindo esses latidos, só podia ser ela. A única."
    cat "Clotilde voltou?"
    narrative "Você estica suas patas da frente, depois as de trás, se espreguiçando. Levantando de sua cama, você vai até a sala."

    scene bg_office:
        zoom 0.4
    with dissolve

    show teresa_happy at left:
        zoom 0.6
    with dissolve

    show v_happy at right:
        zoom 0.5
    with dissolve

    narrative "Você vê Vicente conversando com Teresa, e logo ao lado a figura de ninguém mais, ninguém menos que…"

    show clotilde_neutral at center:
        zoom 0.2
    with dissolve

    cat "É. Clotilde voltou."
    narrative "No fundo, você estava feliz que nada de ruim aconteceu. Pelo menos nos primeiros minutos."
    cat "Ok, hora de sair daqui."
    narrative "Você ia se virar em direção a sua própria casa quando os latidos perturbadores de Clotilde começam a fazer algum sentido." 
    cat "Peraí-"
    clotilde "Me escutem. Me escutem. Me escutem. Os homens lá fora vão voltar. Teresa."
    narrative "Chegando na sala você se depara com clotilde aos berros lambendo a cara de sua dona, na qual achava graça de tudo."
    cat "Tem como ser mais insuportável não?"
    narrative "Você sobe na lateral do sofá, o mais longe o possível de Clotilde e pergunta o que estava a incomodando."

    hide clotilde_neutral
    hide teresa_happy
    hide v_happy
    show clotilde_neutral at left:
        zoom 0.4
    with dissolve
    show cat_discussion at right:
        zoom 0.7
    with dissolve

    cat "Que homens?"
    narrative "Mas Clotilde não tinha um cérebro muito grande e preferiu continuar falando com quem não ia a ouvir."
    cat "Cala a boca Clotilde, pelo amor dos gatinhos."
    cat "Tô falando com você, peste."
    clotilde "Me escutem. Me escut-"
    narrative "Clotilde parou com os incessantes latidos e se encolheu no colo de Teresa que começou a fazer carinho nela enquanto conversava com Vicente algo totalmente irrelevante."
    cat "Quem vai voltar?"
    clotilde "Os homens vão voltar. Os homens VÃO VOLTAR."
    narrative "Clotilde se engasga no latido."
    narrative "Deplorável."
    cat "Quem são esses homens?"
    cat "Por que eles vão voltar?"
    clotilde "Não sei."
    narrative "E pensar que você estava prestes a dar ouvidos para essa maluca comedora de repolho."
    narrative "Mas então Clotilde retornou a falar, para sua surpresa."
    clotilde "Tinha outros cachorros e eu consegui escapar pela grade e acabei caindo em um buraco, mas alguém me ajudou."
    clotilde "Um bueiro do parque, ela falou."
    clotilde "Achei que tinha caído no inferno."
    clotilde "Aqueles homens vão voltar para pegar eu e você."
    cat "O que? Eu?"
    cat "Pera, você está me falando que esses homens pegaram você e outros cachorros? Você então não fugiu de casa."
    clotilde "Fugi, fugi, fugi. Mas eles me pegaram."
    clotilde "E Manchinha também."
    narrative "Você ficou se perguntando quem era Manchinha."
    cat "E com esse nome bobo só pode ser cão mesmo."
    cat "Ok, eu preciso ser mais objetivo com esse cachorro."
    cat "Talvez a gente tenha um caso muito maior aqui. O que eu pergunto?"

    call clotildeQuests from _call_clotildeQuests
    while selected == "Manchinha" or selected == "Ran away" or selected == "Why?":
        call clotildeQuests from _call_clotildeQuests_1
        call homeChoices from _call_homeChoices
    if selected == "People":
        $finish_search = False
        while finish_search == False:
            call askClotilde from _call_askClotilde
            if selected == "Continue":
                $finish_search = True
            call homeChoices from _call_homeChoices_1

    if selected == "Park" or selected == "Continue":
        jump parkStreet  
    elif selected == "Alley":
        jump alley       
    elif selected == "Ignore":
        jump badEnd
    return

# It is worse that I thought (scene 12)
label livingroom: # (Don't change)
    stop music
    play music "audio/musics/CatJazz 1.wav"

    scene bg_office:
        zoom 0.4
    with dissolve

    narrative "Vicente entrega Clotilde de volta para Teresa, que estava na casa dele preparando bolinhos de chuva."
    cat "Sabia que ela estava aqui! Pelo menos não colocou repolho no bolinho…"

    show t_happy at right:
        zoom 0.6
    with dissolve

    show clotilde_neutral at center:
        zoom 0.2
    with dissolve

    show vincent_happy at left:
        zoom 0.5
    with dissolve
    teresa "Oh, minha amada Clotilde! Que bom que você voltou!"
    narrative "Teresa aperta o rosto contra Clotilde, que lambe o rosto de Teresa, parecendo muito aliviada."
    narrative "Por alguma razão Clotilde tem uma aparência um tanto traumatizada desde que foi salva."
    narrative "Você observa por baixo a cena, totalmente inquieto."
    narrative "Na volta pra casa, enquanto Clotilde se movia inquietamente nos braços de Vicente, você estava morrendo de curiosidade."
    cat "Tem muita coisa que essa cadela precisa me responder."
    narrative "E quando Vicente pôs a cadela no chão de casa para chamar a Teresa, você sabia que era o momento certo."
    cat "Ok, eu só preciso ser mais objetivo com esse cachorro."
    cat "O cérebro simples de cão dela não consegue pegar muita informação de uma vez."
    cat "Ò, Clotilde! Responde ai umas perguntas?"
    cat "Depois que eu calei a boca dela antes, acredito que esteja mais calmo. O que eu devo perguntar?"

    menu:
        "1 - Como é que você acabou naquele bueiro?":
            $selected = "How?"
        "2 - Não pergunte nada. Você não está interessado.":
            $selected = "Ignore"

    hide vincent_happy
    hide t_happy
    hide clotilde_neutral
    show clotilde_neutral at right:
        zoom 0.3
    with dissolve
    show cat_suspicious at left:
        zoom 0.6
    with dissolve
    call livingroomChoices from _call_livingroomChoices
    hide clotilde_neutral
    hide cat_suspicious
    if selected == "How?":
        jump findingSuspect
    elif selected == "Ignore":
        jump badEnd
    return

# Finding Clues (Scene 13)
label badEnd: # (Don't change)
    stop music
    play music "audio/musics/CatJazz 1.wav"

    scene bg_bedroom:
        zoom 0.4
    with dissolve

    narrative "Já se passaram dois dias desde sua aventura."
    narrative "Agora que a sua vida voltou ao normal você pode passar a tarde inteira dormindo."
    cat "Exatamente da maneira que gosto."

    scene bg_office:
        zoom 0.4
    with dissolve

    show cat_happy at right:
        zoom 0.3
        yalign 0.75
    with dissolve

    narrative "Após acabar de acordar você senta na sala, observando Vicente trabalhar."
    cat "Nada que tenho que fazer, nenhuma interrupção."
    cat "Isso sim é viver~"

    stop music
    play music "audio/musics/Cat tensao.wav"

    narrative "De repente você ouve alguém batendo na porta de maneira errática."
    cat "Só foi falar."

    scene bg_housedoor:
        zoom 0.4
        yalign 0.5
    with dissolve

    show teresa_sad at center:
        zoom 0.6
    with dissolve

    show cat_suspicious at left:
        zoom 0.4
    with dissolve

    narrative "Desesperadamente com lágrimas nos olhos. Teresa entra pela porta."

    show v_suspicious at right:
        zoom 0.5
    with dissolve

    vincent "Teresa? O que houve?"
    teresa "É, é a Clotilde."
    vincent "O que foi com a Clotilde agora?"
    cat "Não me diga que a peste sumiu de novo?!"
    teresa "Ela tinha sumido essa manhã de novo."
    cat "Como?!"
    cat "Como ela consegue?"
    teresa "Estava morrendo de preocupação."
    teresa "Mas você sabe esse caso de sequestros de animais que estava no rádio esses dias?"
    teresa "Aquele que acabou fugindo com mais de cinquenta animais diferentes?"

    hide v_suspicious
    show v_angry at right:
        zoom 0.5
    with dissolve

    vincent "Você não quer dizer que…"
    teresa "Eles levaram minha Clotilde!"
    teresa "Minha pobre Clotilde!"

    scene bg_bedroom:
        zoom 0.4
    with dissolve

    cat "Eu não gostava da cadela, mas nem eu queria que algo assim acontecesse com ela."
    cat "Talvez ela não estivesse mentindo e realmente tinha pessoas atrás dela."
    cat "Esses sequestradores de animais."
    cat "O que aconteceria se eu tivesse acreditado nela?"
    cat "É, não é como eu pudesse voltar no tempo para descobrir."
    narrative "Uma dor passa pelo seu peito."
    narrative "Virando para o lado você tenta dormir."
    narrative "Pelo menos nos sonhos não dói."

    menu:
        "Você concluiu um final RUIM.":
            pass
    return

# Park street (Scene 14)
label parkStreet: # (Don't change)
    stop music
    play music "audio/sounds/praca_cidade.mp3"
    scene bg_park:
        zoom 0.4
        xalign 0.8
        yalign 0.5
    with dissolve

    show cat_determinated at center:
        zoom 0.3
        xalign 0.9
    with dissolve

    narrative "Com a respiração ofegante você chega ao parque que Clotilde tinha sido encontrada."
    cat "Então é aqui que Clotilde foi achada."
    cat "Ela disse que caiu em um buraco?"
    cat "Melhor começar olhando ao redor."
    cat "Sei que Clotilde foi capturada por um homem."
    cat "Se apenas eu tivesse alguma descrição para procurar…"
    cat "Procrastinando não vai ajudar eu nada, melhor começar mesmo."
    narrative "Explorando o parque, você facilmente encontra o rastro de Clotilde."
    narrative "Seu cheiro estava fedendo de um aroma de esgoto."
    cat "A coitada realmente tava sem sorte hoje."
    narrative "Seguindo a conclusão lógica, você rapidamente encontra o bueiro onde Clotilde havia caído."

    scene bg_manhole:
        zoom 0.4
    with dissolve

    cat "Ish, eu não iria querer cair lá dentro."
    narrative "Cheirando ao redor do bueiro, você detecta um cheiro fraco, porém definitivamente diferente do odor deixado pela Clotilde."
    cat "Esse deve ser o cheiro do sequestrador."
    cat "Mas está muito fraco para eu conseguir seguir."
    cat "O que faço agora."
    cat "Cheguei quando o rastro já está frio."
    narrative "Subitamente uma ideia lhe veio à cabeça."
    cat "Já sei!"
    cat "Vicente é supostamente um especialista nessas paradas, não?"
    cat "Ele é meio bobinho, mas com minha ajuda ele vai conseguir resolver alguma coisa."
    cat "E com Vicente me levando para o esconderijo do sequestrador, eu derroto ele e salvo o dia!"

    scene bg_outside:
        zoom 0.4
    with dissolve

    cat "Perfeito, agora só preciso do Vicente."
    cat "Ele deve ainda estar em casa, com a Teresa."
    narrative "Entusiasmado com sua ideia, você corre em direção a casa."

    jump collectingVincent
    return

# Alley Street (Scene 15)
label alley: # (Don't change)
    stop music
    play music "audio/sounds/praca_cidade.mp3"
    scene bg_street:
        zoom 0.4
        yalign 0.3
    with dissolve

    narrative "Voltando para o beco onde você tinha avistado o cachorro, você olha ao redor."

    scene _bg_alley with dissolve

    cat "Então foi aqui onde aquele cachorro estranho foi."
    narrative "Olhando ao redor você não consegue avistar nada imediatamente incriminante."
    cat "E se eu cheirar?"
    narrative "Investigando os cheiros ao redor, você encontra o cheiro do cachorro."
    narrative "Por alguma razão o cheiro era bem forte, como se o cão tivesse passado por esse beco múltiplas vezes recentemente."
    cat "O cheiro está bem forte."
    cat "Esse deve ser parte de um caminho comum que esse cachorro faz."
    narrative "Olhando mais a fundo onde o cheiro estava mais forte, você encontra um buraco na cerca ao fundo do beco."
    cat "Parece que ele passou por aqui."
    cat "Meio indignante, mas tenho uma missão importante no momento."
    narrative "Se espremendo pelo buraco, você sai em outra rua, com uma construção meio depredada e com um ar depressivo à sua frente."
    cat "É, esse é com certeza o lugar."
    narrative "Respirando fundo, você recolhe sua coragem."
    narrative "Agora não há volta."

    jump kennelv1
    return

# Finding Suspect (Scene 16)
label findingSuspect: # (Don't change)
    stop music

    scene bg_park:
        zoom 0.4
        xalign 0.8
        yalign 0.5
    with dissolve

    narrative "Você chega ao parque, com respiração ofegante."
    narrative "Imediatamente você vai até o bueiro que Clotilde caiu dentro."

    scene bg_manhole:
        zoom 0.4
    with dissolve

    play music "audio/sounds/praca_cidade.mp3"
    narrative "Prestando muita atenção ao redor do bueiro você consegue sentir um leve cheiro do sequestrador."
    cat "Droga, consigo sentir um pouco do cheiro, mas ele ta muito fraco para eu conseguir seguir."
    cat "Vou ter que achar outra maneira de encontrar o cara…"

    $strange = Character("???", color = "#c7bc5a")

    strange "Craw!"
    narrative "O súbito som vindo de cima, faz você pular de susto."

    scene bg_tree:
            zoom 2.0
    with dissolve

    show cockatiel_neutral at center:
        zoom 0.5
    with dissolve

    narrative "Olhando para onde o som veio, você vê a Calopsita da casa de Clara, te observando de uma árvore."
    stop music
    play music "audio/musics/CatJazz 2.wav"
    cat "Perturbadora como sempre, hein?"
    cat "O que é que tu quer pássaro?"
    cockatiel "Craw!"
    cockatiel "Parece que você está tendo umas dificuldades, gato."
    narrative "Sentindo que a Calopsita estava fazendo você de piada, você se sente irritado."
    cat "Se você veio aqui apenas para atrapalhar, então vá embora."
    cockatiel "Ah, não."
    cockatiel "Eu apenas estou aqui, observando este canto do parque."
    cockatiel "Nada de mais~"
    cat "Observando o parque?"
    cat "Será que ela viu o que ocorreu aqui e sabe para onde o sequestrador foi?"
    cat "Mas também não sei se o que ela falar vai ser confiável."

    menu:
        "1 - Perguntar a calopsita.":
            $selected = "Ask"

        "2 - Ignorar a calopsita.":
            $selected = "Ignore"

    call findingSuspectChoices from _call_findingSuspectChoices
    if selected == "Ask" and scared_cockatiel == True or selected == "Ignore":
        jump collectingVincent
    elif selected == "Ask" and scared_cockatiel == False:
        jump kennelv1
    return

# Collecting Vincent (Scene 17)
label collectingVincent: # (Don't change)
    stop music
    play music "audio/musics/CatJazz 1.wav"
    scene bg_outside:
        zoom 0.4
    with dissolve

    narrative "Correndo pela calçada, você chega à frente de casa."

    scene bg_office:
        zoom 0.4
    with dissolve

    show vincent_neutral at left:
        zoom 0.5
    with dissolve

    show t_neutral at right:
        zoom 0.6
    with dissolve

    narrative "Após entrar pela janela você encontra Vicente e Teresa conversando na sala."
    teresa "Ah, ainda não consigo acreditar que minha pobre Clotilde passou por tanto."
    teresa "Não consigo te agradecer o suficiente."
    vincent "Que nada dona Teresa."

    # campainha
    narrative "Ignorando esse papo de humano, você volta sua atenção quando ouve alguém tocando a campainha."
    cat "Quem será agora?"

    $strange = Character("???", color = "#182966")

    strange "Oi, é a Clara aqui."

    if met_clara == True:
        cat "A mulher de antes?"
        cat "O que ela está fazendo aqui?"
    else:
        cat "Quem é essa?"

    vincent "Clara?"
    narrative "Vicente abre a porta e Clara entra na sala."

    hide t_neutral with dissolve
    show c_happy at center:
        zoom 0.5
    with dissolve

    clara "Eai, Vicente."
    vincent "O que você está fazendo aqui, Clara?"
    clara "Ouvi que Clotilde foi achada. To passando para dar uma olhada."
    teresa "Vicente, é a Clara que eu ouço?"

    hide c_happy
    show clara_happy at center:
        zoom 0.5
    with dissolve
    clara "Sou eu sim, dona Teresa."
    clara "Ouvi que Clotilde voltou."

    show t_happy at right:
        zoom 0.6
    with dissolve

    teresa "Sim, fico muito mais relaxada agora que sei que minha Clotilde está segura."
    teresa "Estava tão preocupada com meu anjinho"
    teresa "Vou preparar muitos bolinhos hoje"
    clara "Os famosos bolinhos de chuva…"
    clara "Enfim, desculpa vir essa hora, sem avisar"
    vincent "Não tem problemas"
    teresa "Que isso minha lindinha, você é super bem-vinda"
    cat "A Teresa age como se a casa fosse dela??"

    hide clara_happy
    show clara_neutral at center:
        zoom 0.5
    with dissolve

    clara "Vim tratar de uns assuntos importantes, achei que vocês poderiam me ajudar" 
    clara "Estou suspeitando de algumas coisas e queria informações de vocês"
    vincent "Agora quer compartilhar informações?"
    teresa "Pode contar com a gente mulher"
    clara "Acredito que o sumiço da Clotilde, possa ter relações em um caso que estou encarregada"
    vincent "Como assim? Quando fui pedir informações você mal ajudou"
    teresa "Quieto Vicente!!! Deixa a mocinha falar"
    narrative "Teresa fala isso apontando o dedo para Vicente"
    narrative "Vicente parece um pouco constrangido"
    cat "HA HA! Tomou puxão de orelha da véia!"
    vincent "Desculpe…"
    clara "Agora as coisas se encaixaram melhor, então achei necessário"
    clara "Então… como ia dizendo…"
    clara "Eu venho trabalhando e investigando um caso muito particular"
    clara "Se trata do sumiço de vários animais, muitos donos estão relatando que seus companheiros estão sumindo"
    clara "Não sabemos quem é o culpado por trás disso, mas desconfiamos que o motivo é contrabando"
    clara "Quando soube do acontecido com a Clotilde, logo presumi que ela poderia ter sido pega" 
    clara "Como esse é um caso delicado, não queria causar pânico, omiti algumas informações"
    clara "Quando eu soube que a Clotilde foi recuperada, eu presumi 2 hipóteses"
    clara "primeira era a mais comum, onde Clotilde simplesmente fugiu por conta própria, não tendo ligação nenhuma"
    clara "A segunda é que Clotilde foi realmente alvo, mas por causa de algum acontecimento ela foi deixada para trás, e seu retorno pode ter pistas que a ligam ao caso do contrabando" 
    clara "Por isso eu gostaria de saber tudo o que aconteceu com a Clotilde"
    teresa "Clotilde pode ter sido alvo de contrabando?!"
    teresa "Minha coitadinha. É por isso que ela tá toda tremendo?"
    vincent "Mas contrabando… isso é muito mais sério."
    clara "Sim, é por isso que estou pedindo a ajuda de vocês."
    clara "Temos o famoso detetive Frederico von Barcelona, trabalhando nesse caso, mas qualquer informação ajuda."
    vincent "Bem, então. Tudo começou…"

    scene bg_black:
        zoom 2.0
    with dissolve

    narrative "Então Vicente explica tudo que aconteceu para Clara."
    narrative "Para seu EXTREMO tédio."
    vincent "Então foi isso que aconteceu."

    show vincent_suspicious at left:
        zoom 0.5
    with dissolve

    show c_interested at center:
        zoom 0.5
    with dissolve

    show t_neutral at right:
        zoom 0.6
    with dissolve
    clara "Isso pode ser mais sério do que pensei."
    clara "Droga, eu realmente não deveria estar envolvendo pessoas de fora, mas essa é uma emergência."
    clara "Vicente, preciso que você me ajude."
    clara "O que você me contou aponta para umas suspeitas que eu tinha, mas torcia para estar errada."
    cat "É? Sério?"
    cat "O que é que ele falou? Não estava prestando atenção."

    hide c_interested
    show clara_angry at center:
        zoom 0.5
    with dissolve

    clara "Desculpe as pressas, mas não temos muito tempo a perder."

    # walkie tockie

    narrative "Segurando seu Walkie Talkie, Clara fala enquanto corre para fora da porta."
    clara "Emergência no setor c, todos as viaturas avaliáveis se d-"

    hide clara_angry with dissolve
    cat "Essa aí sabe como deixar uma impressão ao sair."
    narrative "Vicente finalmente saindo de seu choque, segue ela pela porta."
    vincent "Calma aí, expli-"
    cat "Opa, acho que esse ai foi meu sinal para ir andando."

    scene bg_black:
        zoom 2.0
    with dissolve

    narrative "Seguindo Vicente e Clara, você se exprime no assento de trás, sem eles perceberem."
    # carro ligando
    cat "Só agradeço que estamos indo com o carro da Clara, não me lembro quando foi a última vez que Vicente deu uma arrumada naquela carroceria."
    narrative "Quando o carro para, você salta para fora, finalmente livre."
    cat "Mas o que…"
    narrative "Você se sentiu um tanto desapontado com o estado do local."

    scene bg_kennel:
        zoom 0.5
        xalign 0.9
    with dissolve

    cat "Ta meio caindo aos pedaços."
    cat "Por acaso eles não podiam nem pagar uma renovação, não?"
    cat "Tá parecendo pior que a casa do Vicente."
    narrative "Vicente e Clara também saem do carro."

    jump kennelv2
    return

# Kennel alone (Scene 18)
label kennelv1: # (Don't change)
    scene bg_kennel:
        zoom 0.5
        xalign 0.9
    with dissolve

    stop music
    play music "audio/sounds/canil.mp3"

    narrative "Olhando para a construção a sua frente você engole seco."
    cat "Clotilde escapou por um buraco."
    cat "Se eu olhar bem devo conseguir achá-lo."
    narrative "Olhando ao redor, você encontra um pequeno buraco na parede."
    narrative "Pequeno, mas grande o suficiente para um cachorro como Clotilde possa passar."
    narrative "E em consequência, você também."
    cat "Quem mandou não dar uma boa renovada."
    cat "Agora é só passar para o outro lado."
    narrative "Se esfregando pelo buraco, você chega ao interior da construção."

    show cat_mad at right:
        zoom 0.3
        xalign 0.7
    with dissolve

    cat "Mas que horroridade é essa?"
    narrative "A sua frente havia centenas de jaulas com animais de todos os tipos e tamanhos imagináveis."
    narrative "Surpreendido com a visão, você não nota o residente da jaula ao seu lado."

    $strange = Character("???", color = "#dbca0f")

    strange "Ps, você ai."

    show manchinha_neutral at right:
        zoom 0.1
        xalign 0.9
        yalign 0.9
    with dissolve

    narrative "Levando um susto pela voz, você se depara com um pequeno filhote de gato, com várias manchas marrons pelo seu pelo."
    cat "Quem é você?"

    stop music
    play music "audio/musics/Cat tensao.mp3"

    strange "Isso que eu deveria estar te perguntando, o que você está fazendo aqui?"
    cat "Esse ai deveria aprender a respeitar os mais velhos."
    cat "Mas não tenho tempo a perder com discussões inúteis."

    if player_name == "":
        cat "Eu não sei..."
        cat "Pode me chama apenas de Gato, como o tapado do Vicente."
        strange "..."
        strange "... ok."
        cat "Enfim, estou aqui por uma missão dada por Clotilde."
    else:
        cat "Sou [cat], estou aqui por uma missão dada por Clotilde."
    strange "Clotilde? Ela conseguiu escapar?!"
    cat "Você conhece a Clotilde?"
    strange "Sim! Ela foi colocada na jaula ao meu lado."
    manchinha "Me chamo Manchinha, prazer!"
    narrative "Você se recolhe do tamanho entusiasmo que o gatinho estava mostrando."
    cat "Tem certeza que esse ai é um cachorro e não gato?"
    cat "Clotilde mencionou você."
    cat "Você tinha ajudado Clotilde a fugir, não."
    manchinha "Sim! A jaula que me botaram tem as grades muito largas."
    manchinha "Eu consigo sair a qualquer momento que quero!"
    cat "Então o que você está fazendo aqui?"
    cat "Por que ainda não escapou?"
    manchinha "E deixar todos esses animais para trás?!"
    cat "Que gato é esse? Cade seu senso de sobrevivência?"
    cat "Gato e altruísmo não são coisas que se misturam!"
    cat "E porque, se você pode sair à sua vontade, você ainda não salvou os outros animais."
    manchinha "Eu adoraria!"
    manchinha "Mas eu sou muito pequeno."
    manchinha "Os computadores que controlam as celas são muuuuuinto altos!"
    manchinha "Se apenas eu fosse mais alto!"
    cat "Ele não conseguiu… por que ele é baixo?"
    manchinha "Ah! Mas você é alto!"
    manchinha "Talvez você consiga alcançar os controles!"
    manchinha "Me siga!"
    narrative "Manchinha escapa de sua jaula e sai correndo sem esperar você."
    cat "O que aconteceu com minha aventura épica?"
    cat "Como é que ela se tornou nisso?"
    narrative "Se sentindo sem outra opção, você segue o jovem gato."

    scene bg_machine:
        zoom 2.3
    with dissolve

    narrative "Ele te leva para frente de um grande computador com vários botões."
    manchinha "Olha!"

    show cat_suspicious at left:
        zoom 0.7
    with dissolve

    show manchinha_neutral at right:
        zoom 0.3
    with dissolve

    manchinha "Esse é o computador que controla todas as jaulas!"
    manchinha "Com ele a gente pode libertar todos os animais! Não é genial?!"
    cat "Esse é o plano? E minha batalha contra o boss final?"
    manchinha "Entendeu?! Você só precisa pular e alcançar o teclado."
    narrative "Se sentindo levemente irritado com esse gatinho que não para de falar, você pula para cima do teclado."
    cat "Mesmo considerando outros gatos, eu realmente sou o ápice de perfeição."
    narrative "Concentrando-se na sua missão, você estende uma pata e liga o computador."
    narrative "Na sua frente a tela liga, parando ao pedir a senha de acesso."
    cat "E agora Manchinha, o que a gente faz com seu incrível plano."
    manchinha "Não se preocupe! Eu estive espiando os trabalhadores por muito tempo!"
    cat "Falando em trabalhadores, por que esse local está tão abandonado?"
    cat "Com certeza deve ter alguém tomando conta de tantos animais."
    manchinha "Eu até memorizei a senha!"
    manchinha "Eu fiz uma música para lembrar da senha!"
    cat "Oh não."
    manchinha "Com 7 vidas, eu vou aproveitar, comendo 5 refeições ao dia para me esbaldar!"
    manchinha "11 bolas de pelos para eu soltar!"
    manchinha "Ninguém ficará de pé para me criticar!!!"
    manchinha "Só repete atrás de mim, a senha é 07051100!"
    cat "Hm, parece que esse gato não é tão burro quanto parece."
    narrative "Com um pouco de relutância, você digita a senha no computador."
    narrative "Surpreendentemente a senha realmente é 07051100."
    cat "Quem diria que ele estaria certo."
    manchinha "SIM!"
    manchinha "Agora você só precisa desbloquear as jaulas."
    manchinha "Os controles devem estar facilmente acessíveis."
    narrative "Olhando para onde Manchinha estava apontando, você realmente facilmente achou os controles das celas."
    cat "Estou chocado com o quão isso está dando certo."
    narrative "A sua frente aparece o botão para libertar todos os animais."
    cat "Mas se eu libertar os animais assim… não vou ter minha batalha épica final?"
    cat "E minha glória?"

    stop music
    play sound "audio/musics/Cat tensao.mp3"

    menu:
        "1 - Apertar o botão sozinho.":
            $selected = "Press"

        "2 - Pedir recompensa para os animais.":
            $selected = "Reward"

    stop music
    play music "audio/sounds/canil.mp3"
    call kennelv1Choices from _call_kennelv1Choices
    if selected == "Back":
        menu:
            "Você concluiu um final BOM!!!":
                pass

    elif selected == "Keep going" or selected == "Reward":
        menu:
            "Você concluiu um final RUIM.":
                pass
    return

# Kennel with Vincent (Scene 19)
label kennelv2: # (Don't change)
    stop music
    play music "audio/sounds/canil.mp3"
    scene bg_kennel:
        zoom 0.5
        xalign 0.9
    with dissolve
    vincent "Então, Clara. Por que nos trouxe aqui mesmo?"
    clara "De acordo com minhas investigações esse lugar poderia ser a base do sequestrador."
    cat "Sério mesmo? Porque você só está investigando agora?"
    clara "Mas existe uma razão por que eu não tinha investigado esse local anteriormente."
    clara "Mesmo considerando o quão suspeito ele é."
    vincent "E a razão é…?"
    cat "É., fala logo moça. Não deixa a gente no suspense, não."
    clara "Isso é porque este local está registrado como propriedade do sr. Barcelona, o detetive ocupado desse caso."
    vincent "O que?!"
    clara "Agora você entende. Se esse local realmente for a base de operações isso poderia apenas significar uma coisa."
    clara "A operação estará destinada a falhar."
    clara "Porque no final, o próprio detetive estava trabalhando com os criminosos."
    clara "..."
    cat "Ai você realmente fez a coisa ficar séria."
    narrative "Quebrando o cadeado na porta, Clara entra na construção. Seguida por Vicente e você."
    cat "Que horrorosidade é essa?!"
    narrative "Na sua frente você vê centenas de jaulas com diferentes animais, de diversos tamanhos e formas, dentro."
    vincent "Como alguém pode…"
    clara "Isso é pior que achei."
    femalecat "Ta ruim mesmo."
    narrative "Agora que os humanos já guiaram você aqui, você decide dar uma explorada por conta própria."

    show cat_mad at right:
        zoom 0.3
        xalign 0.7
    with dissolve

    cat "Esses humanos atrapalhados, só vão me incomodar."
    cat "Hm, parece que as portas das gaiolas abrem usando algum sistema automático."
    cat "Não há buraco para a chave-"

    $strange = Character("???", color = "#dbca0f")

    strange "Ps, você ai."
    narrative "Levando um susto pela voz, você se depara com um pequeno filhote de gato, com várias manchas marrons pelo seu pelo."

    show manchinha_neutral at right:
        zoom 0.1
        xalign 0.9
        yalign 0.9
    with dissolve

    cat "Quem é você?"
    strange "Isso que eu deveria estar te perguntando, o que você está fazendo aqui?"
    cat "Esse ai deveria aprender a respeitar os mais velhos."
    cat "Mas não tenho tempo a perder com discussões inúteis."

    if player_name == "":
        cat "Eu não sei..."
        cat "Pode me chama apenas de Gato, como o tapado do Vicente."
        strange "..."
        strange "... ok."
        cat "Enfim, estou aqui por uma missão dada por Clotilde."
    else:
        cat "Sou [cat], estou aqui por uma missão dada por Clotilde."
    strange "Clotilde? Ela conseguiu escapar?!"
    cat "Você conhece a Clotilde?"
    strange "Sim! Ela foi colocada na jaula ao meu lado."
    manchinha "Me chamo Manchinha, prazer!"
    narrative "Você se recolhe do tamanho entusiasmo que o gatinho estava mostrando."
    cat "Tem certeza que esse ai é um cachorro e não gato?"
    cat "Clotilde mencionou você."
    cat "Você tinha ajudado Clotilde a fugir, não."
    manchinha "Sim! A jaula que me botaram tem as grades muito largas."
    manchinha "Eu consigo sair a qualquer momento que quero!"
    cat "Então o que você está fazendo aqui?"
    cat "Por que ainda não escapou?"
    manchinha "E deixar todos esses animais para trás?!"
    cat "Que gato é esse? Cadê seu senso de sobrevivência?"
    cat "Gato e altruísmo não são coisas que se misturam!"
    cat "E porque, se você pode sair à sua vontade, você ainda não salvou os outros animais."
    manchinha "Eu adoraria!"
    manchinha "Mas eu sou muito pequeno."
    manchinha "Os computadores que controlam as celas são muuuuuinto altos!"
    manchinha "Se apenas eu fosse mais alto!"
    cat "Ele não conseguiu… por que ele é baixo?"
    manchinha "Ah! Mas você é alto!"
    manchinha "Talvez você consiga alcançar os controles!"
    manchinha "Me siga!"
    narrative "Manchinha escapa de sua jaula e sai correndo sem esperar você."
    cat "Esse pestinha!"
    narrative "Se sentindo sem outra opção, você segue o jovem gato."

    scene bg_black:
        zoom 2.0
    with dissolve

    narrative "Ele te leva para frente de um grande computador com vários botões."
    manchinha "Olha!"
    manchinha "Esse é o computador que controla todas as jaulas!"
    cat "Então eu estava correto. As portas devem abrir com um comando deste aparelho."
    narrative "Notando passos vindo de trás, você percebe que Vicente te seguiu."

    scene bg_kennel:
        zoom 0.5
        xalign 0.9
    with dissolve

    show cat_bored at center:
        zoom 0.3
        xalign 0.7
    with dissolve

    show vincent_suspicious at left:
        zoom 0.5
    with dissolve

    show manchinha_neutral at right:
        zoom 0.1
        xalign 0.9
        yalign 0.9
    with dissolve

    vincent "O que tem aí, Gato?"
    cat "Vai embora, Vicente. Eu que achei esse computador, ele é meu agora."
    manchinha "Eep!"
    manchinha "Quem é esse?!"
    cat "Não se preocupe, Vicente veio comigo."
    cat "Ele é meio incopetente, mas me obedece bem o suficiente."
    vincent "Um computador? Gato isso não é brinquedo."
    vincent "Esse equipamento é delicado."
    cat "Algumas vezes…"
    manchinha "Uau, esse é seu humano [cat]?!"
    manchinha "Sem querer ofender, mas ele parece acabado!"
    manchinha "Por acaso seu humano não sabe cuidar de si mesmo?"
    manchinha "Eu ouvi que humanos conseguem independência apenas anooos depois de nascer!"
    manchinha "Isso não é muito estranho?!"
    cat "Chega! Já entendi, por que a gente para de fugir do importante."
    cat "Se essa peste fala muito mais minhas orelhas vão estourar."
    cat "Parece que Vicente tá mexendo no computador, mas precisa da senha."
    cat "Por acaso isso era parte de seu plano também?"
    manchinha "Sim! Eu memorizei a senha que os guardas colocavam!"
    manchinha "Foi muito fácil eu até criei uma música!"
    manchinha "Ela vai-"
    narrative "Subitamente alguém grita perto de você, fazendo você levar um susto."

    stop music
    play music "audio/musics/Cat tensao.mp3"

    scene bg_kennel:
        zoom 0.5
        xalign 0.9
    with dissolve

    show frederico_angry at left:
        zoom 0.5
    with dissolve

    show vincent_suspicious at right:
        zoom 0.5
    with dissolve

    strange "Quem é você?!"
    strange "Quem te autorizou a mexer nesse equipamento?"
    narrative "Um homem alto vestindo um terno bege, entrou por uma porta lateral. Ao seu lado estava um border collie."
    vincent "Detetive Barcelona?"
    frederico "Um intruso! O que você está fazendo aqui?"
    frederico "É melhor você responder logo, você não ira gostar das consequências de me irritar."
    vincent "Como você pode! Sequestrando animais!"
    frederico "O que é para você o que faço?" 
    frederico "Agora é melhor você dizer quem está atrás de você ou esteja preparado para bastante dor."
    cat "Vish, o cara não está aqui para brincar, não."
    cat "Vicente realmente se meteu fundo dessa vez."
    frederico "Você não vai falar mesmo?"
    frederico "Vagabundo que não serve para nada."
    vincent "Você vai parar na cadeia, Frederico."
    frederico "Cadeia? Você é muito engraçado com suas piadas."
    frederico "Você realmente não entende sua situação."

    show clara_angry at center:
        zoom 0.5
    with dissolve

    clara "Não."
    narrative "Clara entra, apontando sua arma para Frederico."
    clara "É você que não entende a situação que está."
    cat "Isso aí, mostra pra ele quem manda."
    frederico "Uma policial? O que você está fazendo aqui?!"
    clara "Exatamente o que eu deveria estar fazendo."
    clara "Apreendendo o sequestrador de animais, que esteve aterrorizando a cidade."
    frederico "Há! E quem eles vão acreditar em, o detetive encarregado do caso, ou uma policial qualquer?"
    cat "O drama ta forte."
    clara "Considerando toda a evidência ao nosso redor. Sim, acho que eles vão acreditar em mim."
    frederico "Não! Tudo não pode terminar assim!"
    narrative "Frederico começa a virar para correr, mas você pula direto no seu rosto, fazendo ele perder o equilíbrio e cair no chão."

    hide frederico_angry
    cat "Gato para o resgate!"
    cat "E como esperado, eu salvo o dia novamente."
    clara "Detetive Frederico von Barcelona, você esta preso por várias acusações."
    clara "Vamos ver o que o júri tem a dizer."
    frederico "Isso não pode estra acontecendo!"
    frederico "Meus planos! Minha glória!"
    narrative "Clara arrasta Frederico para fora. O cachorro de Frederico segue com a cabeça abaixada."

    hide clara_angry
    cat "Isso ai! Tomou o que mereceu!"
    cat "Esse charlatão deve passar uns bons anos na prisão."
    cat "E eu sou incrível por solucionar esse caso."
    cat "Agora quero meu muito merecido descanso."
    cat "E você Vicente. Deve-me comprar muita sardinha."
    cat "Nada daquela papa nojenta que você parece achar que é comida."
    cat "Tenho padrões mínimos de qualidade."
    vincent "Porque você está tão barulhento agora, Gato?"
    cat "Barulhento?!"
    cat "Se eu não estivesse tão cansado você iria ver só."
    cat "Quero ver barulhento quando eu arruinar seu rosto."
    cat "Mas agora…"
    cat "Mas por agora estou satisfeito."

    scene bg_black:
        zoom 2.0
    with dissolve

    menu:
        "Você concluiu um final BOM!!!":
            pass
    return

# ----- Choices Lines -----
label flashbackChoices: # (Don't change)
    if selected == "Follow":
        narrative "Você decide correr atrás da sombra, mas percebe que seu corpo não queria sair do lugar."
        narrative "Você sente as paredes ao seu redor descendo sobre você. A escuridão está pronta para te engolir, com seu coração palpitando furiosamente sobre seus ouvidos."
        narrative "Você precisa sair daqui."
        narrative "Você tenta correr, mas suas pernas não o obedecem, ficando congeladas em lugar como se elas fossem feitas de chumbo."
        narrative "Você sente sua respiração acelerar, enquanto seu desespero incessante apenas cresce."
        narrative "Você precisa escapar-"
        narrative "Seus sentidos subitamente desaparecem e tudo fica branco."

        scene bg_white:
            zoom 2.0
        with dissolve

        narrative "O peso da decisão que você fez naquele dia ainda o persegue."
        narrative "Talvez não havia escolha certa. Mas você acredita que tinha uma escolha melhor."

    elif selected == "Run":
        narrative "Você sente as paredes ao seu redor descendo sobre você. A escuridão está pronta para te engolir, com seu coração palpitando furiosamente sobre seus ouvidos."
        narrative "Você precisa sair daqui." 
        narrative "Você tenta correr, mas suas pernas não o obedecem, ficando congeladas em lugar como se elas fossem feitas de chumbo."
        narrative "Você sente sua respiração acelerar, enquanto seu desespero incessante apenas cresce."
        narrative "Você precisa escapar-"
        narrative "Seus sentidos subitamente desaparecem e tudo fica branco."

        scene bg_white:
            zoom 2.0
        with dissolve

        narrative "O peso da decisão que você fez naquele dia ainda o persegue."
        narrative "Talvez não havia escolha certa. Mas você acredita que tinha uma escolha melhor."
    return

label playerName: # (Don't change)
    $player_name = renpy.input("Qual o seu nome?")
    if player_name == "":
        narrative "Na verdade você nem sabe o seu nome, apenas supõem que possue um."
    else:
        $cat = Character(player_name, color = "#c8c7c9")
    return

label vicentesChoices: # (Don't change)
    if selected == "Play":
        narrative "Você começa a brincar com o ratinho de borracha, que nem rabo tinha mais."
        cat "Sim, sinta o medo do predador pequena presa."
        hide v_happy
        hide cat_angry
        show cat_hunting at center:
            zoom 0.3
            yalign 0.6
            xalign 1
        with dissolve

        narrative "Gritos de horror podiam ser ouvidos saindo do pequeno rato… se ele fosse vivo." 

        hide cat_hunting
        show v_happy at center:
            zoom 0.5
        with dissolve 

        vincent "Você é realmente muito fofo brincando, Gato."
        narrative "Você para tudo que estava fazendo para encarar o homem acima de si."

        show cat_bored at left:
            zoom 0.3
            yalign 0.6
            xalign 1
        with dissolve

        cat "Vicente… Tanto tempo e você ainda tem preguiça de me chamar pelo nome."

        call playerName from _call_playerName

        vincent "Você realmente é energético durante a manhã…"

        hide cat_bored
        hide v_happy with dissolve
        show cat_confident at center:
            zoom 0.3
            yalign 0.6
            xalign 1
        with dissolve

        narrative "Vincente sai do quarto e vai para sala."
        cat "Humpf"

        hide cat_confident

    elif selected == "Turn on":
        narrative "Violência não é uma opção."
        narrative "E com esse pensamento, você pula em cima da escrivaninha e desfere vários tapas no rádio até que em certo momento, ele se rende e liga novamente."
        narrative "Só assim para as coisas funcionarem mesmo."

        hide v_happy
        show v_suspicious at center:
            zoom 0.5
        with dissolve

        vincent "Realmente não te entendo, Gato…"
        narrative "Você encara o homem que ainda segurava o falecido rato de borracha."
        cat "Vicente… Tanto tempo e você ainda tem preguiça de me chamar pelo nome."

        call playerName from _call_playerName_1

        hide v_suspicious 
        show v_happy at center:
            zoom 0.5
        with dissolve 
        
        vincent "Você realmente é energético durante a manhã…"

        hide v_happy with dissolve
        hide cat_angry
        show cat_suspicious at center:
            zoom 0.3
            yalign 0.6
            xalign 1
        with dissolve

        narrative "Vicente sai do quarto, largando o rato de borracha sob a cadeira e vai para a sala."
        narrative "Você volta sua atenção às vozes do rádio que não pararam a nenhum momento."
        radio "Ela não estava metida com aquele cracudo? Deve ser uma mula."
        narrative "Uma risada de um terceiro homem foi emitida pelo rádio."
        radio "Não sei. Aparentemente fizeram por causa da grana."
        radio "Não consigo acreditar que pagaram mais pelo resgate desse animal que eu ganho no ano inteiro."
        radio "Enfim…sem papo mole."

        hide cat_suspicious
        show cat_bored at center:
            zoom 0.3
            yalign 0.6
            xalign 1
        with dissolve

        radio "Câmbio desligo."
        narrative "Ninguém mais se pronunciou."
        narrative "*Estática*"
        cat "Grana? É, parece que tem uns dramas ocorrendo."

        hide cat_bored with dissolve
    return

label housedoorChoices: # (Don't change)
    if selected == "Stay":

        hide cat_surprised
        show cat_bored at left:
            zoom 0.5
            yalign 1.1
        with dissolve

        narrative "Você decide ficar no final das contas, pois não tinha o mínimo de interesse em procurar o pulguento perdido."
        cat "Não pode ser tão ruim, pode?"
        teresa "Ah, que maravilha! Muito obrigado, Vicente. Por favor, encontre minha Clotilde."
        vincent "Deixo ele em seus cuidados, Teresa. Vou para sua casa procurar por rastros de onde ela possa ter ido."

        hide v_happy with dissolve

        narrative "Vicente sai pela porta."

        hide teresa_happy
        show t_happy at center:
            zoom 0.6
        with dissolve

        teresa "Agora somos só nós, peludinho. Tenho certeza que Vicente vai encontrar meu anjinho. Um jovem tão carinhoso aquele."
        narrative "Você começa a lamber suas patinhas."
        teresa "Mas agora vamos nos concentrar em colocar o senhor em um casaquinho confortável de lã! Você vai ficar tão bonitinho!"
        narrative "Você para e olha para ela fixamente ainda com a língua para fora."

        hide cat_bored
        show cat_surprised at left:
            zoom 0.5
            yalign 1.1
        with dissolve

        cat "Quê? Não vou não!."
        teresa "Vem cá, gatinho…"
        narrative "Teresa se aproxima e começa a colocar a roupa de lã em você."

        hide cat_surprised
        hide t_happy

        #(Tela fica preta)
        scene bg_black:
            zoom 2.0
        with dissolve

        teresa "Vai ser um pouco desconfortável colocar, mas você vai ficar tão charmoso!"
        cat "O que é isso! Me tira daqui, socorro!"
        narrative "*Roupa sendo colocada*"
        narrative "Você consegue se livrar da roupinha e foge pela janela."

        hide bg_black with dissolve

    elif selected == "Go away":
        hide cat_surprised
        show cat_determinated at left:
            zoom 0.5
            yalign 1.1
        with dissolve

        cat "Não quero ser cobaia, não! Tô caindo fora."
        narrative "Você sai caminhando lentamente pela porta e some nos arbustos."
        vincent "É, acho que ele não está muito a fim."

        hide cat_determinated with dissolve
        hide teresa_happy with dissolve
        hide v_happy with dissolve
    return

label backyardChoices: # (Don't change)
    # Coming up in the backyard
    if selected == "Vincent":
        narrative "Você se aproxima de Vicente fazendo sua presença ser notada."    

        show vincent_suspicious at center:
            zoom 0.4
            xalign 0.2
        with dissolve

        vincent "O que que você está fazendo aqui? Não aguentou a Teresa?"
        narrative "Vicente não estava nada surpreso."
        cat "Miau! Você acha que eu sou masoquista?"
        narrative "Vicente ignora seu miado, olhando para os lados. Parece estar procurando alguma coisa."
        cat "Ele realmente não está nem aí pra mim, humpf… também não ligo pra ele."
        vincent "Talvez seja melhor perguntar para os vizinhos se eles viram onde a Clotilde foi…"
        cat "E como sempre, Vicente segue seu hábito de monologar tudo que pensa."

        hide vincent_suspicious with dissolve


    # Backyard search
    if selected == "Door":
        narrative "Você investiga perto da porta, cheirando e observando qualquer detalhe que indique uma pista."
        cat "As flores ao redor da porta disfarçam qualquer rastro."
        cat "Diversos pelos esparramados pelo chão. Mas eles parecem ser de alguns dias atrás."
        cat "Interessante que a portinha de cachorro está trancada…"
        cat "Será que ela saiu de casa perseguindo um carro e não conseguiu entrar de volta?"

    elif selected == "Tree":
        narrative "Você anda até o pé da maior árvore presente no quintal."
        cat "É, subir nessa árvore poderia me dar um ponto de vantagem, onde eu teria a chance de avistar a Clotilde."
        cat "Porém, entretanto, todavia, eu não tenho confiança de que consigo descer uma vez que subi."
        cat "Acho melhor eu não comprometer esse caso antes mesmo que ele comece."

    elif selected == "Sniff":
        narrative "Você passa por todos os cantos do quintal tentando procurar uma pista recente por onde o cachorro passou. Mas tudo que conseguiu foi impregnar o cheiro de repolho e cachorro molhado em suas preciosas narinas."
        narrative "Você, em certo ponto, para e começa a se limpar quando sente um terceiro aroma estranho."

        scene bg_tree:
            zoom 2.0
        with dissolve

        show cat_love at left:
            zoom 1 
        with dissolve
        
        cat "Peraí…"
        narrative "Você percorre o caminho de onde o cheiro vem. Deparando-se com um outro gato. Seus pelos lustrosos brilhavam na luz do sol, seus olhos brilhavam como gemas preciosas e ele se movia de forma incrivelmente graciosa."
        
        show orange_neutral at right:
            zoom 1
        with dissolve

        cat "Uau..."
        narrative "Você ficou embasbacado com tamanha beleza, delicadeza e elegância."


    # Cat Talk Decisions
    if selected == "Say hi":
        cat "Oi."
        narrative "Você se aproxima normalmente e tenta falar com o outro gato. No entanto, o que você não esperava era uma patada no meio da fuça. Mas não tem o que esperar muito de gatos laranjas."
        narrative "Você tenta relevar já que o gato era MUITO bonito."
        cat "Calma aí, você entendeu errado."
        cat "Eu tenho algumas pergun-"
        narrative "Mas antes que pudesse terminar sua frase, o gato laranja vocifera palavras nada legais de se ouvir."
        orange "O que pensas que está fazendo no meu quintal, seu vira-lata imundo nojento??"
        orange "São gatos do seu tipo que me fazem ter nojo de sair andando pela rua."
        narrative "Você pisca lentamente tentando processar o que acabou de ouvir. Ele sabe com quem está falando?"
        narrative "Sem perceberem, ambos estavam com os estômagos totalmente curvados e rosnando um para o outro."
        cat "Cai dentro, laranjinha!"
        narrative "Mas antes que pudesse fazer qualquer outra coisa, uma senhora com uma vassoura aparece afugentando você para longe."

    if selected == "Say nothing":
        narrative "Você se aproxima cautelosamente, calculando todos os seus passos"
        cat "Ele não está me vendo, ele não está me vendo."
        narrative " Ele está te vendo."
        narrative "Muito bem, por sinal."
        narrative "Você não pode dizer o mesmo, pois além de levar uma patada na fuça, você caia do telhado diretamente no quintal onde vivia Laranjinha."
        narrative "Essa doeu."
        orange "Vira lata imundo! Saia daqui antes que sua raça nojenta emporcalhe todo o meu quintal."
        cat "Como é que é?"
        narrative "No entanto, aquele gato doido não estava para conversa e você não estava afim de conversar com as paredes."
        narrative "Decepcionado, você resolve se retirar. Mas não antes de arranhar as roupas do varal que tinha ali enquanto olhava nos olhos furiosos do gato laranja que, por um milímetro, não te come na porrada."
        narrative "Ainda bem que gato tem 7 vidas. E hoje você tem 6."

    if selected == "Flert":
        narrative "Você é o gato. Confie no seu potencial."
        narrative "Você lambe as patas e ajeita sua pelagem na tentativa falha de parecer mais atraente, como se não tivesse pulando muros por aí e cheirando a pinscher com problemas estomacais por comer muito repolho."                    
        cat "Como que era aquela cantada mesmo?"
    return

label catAproach: # (Don't change)
    menu: 
        "1 - Se aproxime e diga oi.":
            $selected = "Say hi"
            call backyardChoices from _call_backyardChoices_2

        "2 - Se aproxime e não diga nada.":
            $selected = "Say nothing"
            call backyardChoices from _call_backyardChoices_3

        "3 - Se aproxime e lance sua melhor cantada.":
            $selected = "Flert"
            call backyardChoices from _call_backyardChoices_4

            menu:
                "1 - Não sou arranhador, mas adoraria que você afiasse essas garras em mim.":
                    $aproach = True
                    cat "Não sou arranhador, mas adoraria que você afiasse essas garras em mim."

                "2 - Gato, você não é catnip mas eu rolaria a noite inteira em você.":
                    $aproach = True
                    cat "Gato, você não é catnip mas eu rolaria a noite inteira em você."

                "3 - Você é uma caixa? Porque eu quero estar dentro de você.":
                    $aproach = True
                    cat "Você é uma caixa? Porque eu quero estar dentro de você."

                "4 - Gato, você não é catnip, mas seu cheiro me deixa louco.":
                    $aproach = True
                    cat "Gato, você não é catnip, mas seu cheiro me deixa louco."

            if aproach == True:
                narrative "Você estava muito orgulhoso de si mesmo. Não havia dúvidas de que este foi seu melhor ato como gato."
                narrative "O gato laranja ficou te encarando, imóvel, sem rastros de sua alma ali."
                narrative "Antes que pudesse dizer algo como o que foi? O GATO comeu sua língua? O gato sibilou, se afastando em um pulo."
                narrative "Seus olhos eram de puro repúdio."
                orange "ECA."
                narrative "Você entortou a cabeça, não compreendendo a situação."
                narrative "O gato ainda tentou te arranhar, mas você foi mais rápido com seus instintos felinos."
                orange "Nunca mais volte a proferir palavras tão profanas a mim, seu arruaceiro selvagem e imundo. Como odeio vira-latas."
                narrative "O seu mundo caiu."
                narrative "Mas você, orgulhoso como era, não ia deixar isso barato."
                narrative "Perdeu a cantada, mas não vai perder a pose."
                cat "Uau! Te enxerga gato vesgo do caramba! Se não gostou é só falar, não precisa exagerar."
                cat "Aliás, tá sem arranhador em casa? É uma sugestão, mas por que você não pega essas suas garras e afia no seu c-"
                narrative "Antes que pudesse terminar as suas profanidades, uma senhora com uma vassoura aparece o afugentando para longe dali."
                narrative "Você nem lembra mais qual era o seu propósito inicial."
    
    hide cat_love with dissolve
    hide orange_neutral with dissolve
    scene bg_backyard:
        zoom 0.5
    with dissolve
    return

label backyardSearch: # (Don't change)
    menu:
        "1 - Investigar perto da porta.":
            $selected = "Door"
            if by_door == False:
                $count += 1
            $by_door = True

        "2 - Escalar árvore do quintal.":
            $selected = "Tree"
            if by_tree == False:
                $count += 1
            $by_tree = True
        
        "3 - Cheirar ao redor do quintal.":
            $selected = "Sniff"
            if by_sniff == False:
                $count += 1
            $by_sniff = True
    return

label clarasHouseChoices: # (Don't change)
    if selected == "Scare":
        narrative "Para demonstrar a sua superioridade para o pássaro tosco, você se agacha no chão e lentamente se aproxima da Calopsita."
        cat "Só mais um pouco…"
        narrative "Ao se aproximar o suficiente, você salta para cima dando um enorme susto no pássaro."
        cockatiel "Craawwhh!"

        hide cockatiel_neutral with dissolve
        narrative "Aterrorizada a Calopsita sai voando para longe."
        cat "Isso mesmo!"
        cat "Agora você sabe que é bom não se meter com um gato!"
        narrative "Satisfeito com a demonstração de seu poder, você retorna sua atenção para os papéis no chão."
        cat "Agora posso dar uma olhada nesses documentos em paz."
        cat "Deixa eu ver…"
        cat "Preço do gás, o futuro da moda, 5 receitas fáceis…"
        cat "Ah, achei!"
        cat "Sequestro de animais."
        cat "Hmm, aparentemente tem alguém sequestrando animais da região."
        cat "Eles capturam o animal em questão, e depois pedem por valor monetário pelo resgate."
        cat "Interessante, aqui diz que esses casos já ocorreram em outros locais, mas um detetive acabou encontrando a operação, e o sequestrador fugiu."
        cat "Não deve ser um detetive muito bom se deixou o culpado fugir."
        cat "Mas não, aparentemente ele ficou bem famoso por solucionar esse caso!"
        cat "Hm, e esse detetive parece estar investigando esse caso novamente."
        cat "Frederico alguma coisa."
        cat "Mas quem se importa com esse humano qualquer, eu vou ser quem vai solucionar esse mistério!"
        cat "Com essas pistas é óbvio que Clotilde não apenas sumiu, ela foi sequestrada!"
        cat "Primeiro devo achar onde ela foi vista por último."
        cat "Talvez, Vicente tenha sido útil uma vez em sua vida e descoberto alguma coisa."
        cat "Vai ser fácil achar ele seguindo seu cheiro."
        narrative "Determinado, você foge para fora da casa de Clara e segue os rastros de cheiro deixados por Vicente."

    elif selected == "Ignore":
        narrative "Não sentindo a vontade de assustar o pobre pássaro, você decide deixar a Calopsita em paz."
        cat "Afinal de contas, após nascer como um pássaro e não um gato, sua vida já é difícil o suficiente."
        narrative "Tirando sua atenção do pássaro, você olha de volta sua atenção para os documentos espalhados pelo chão."
        cat "Deixa eu ver…"
        cat "Preço do gás, o futuro da moda, 5 receitas fáceis…"
        cat "Ah, achei!"                   
        cat "Sequestro de animais."
        cat "Hmm, aparentemente tem alguém sequestrando animais da região."
        cat "Eles capturam o animal em questão, e depois pedem por valor monetário pelo resgate."
        cat "Interessante, aqui diz que esses casos já ocorreram em outros locais, mas um detetive acabou encontrando a operação, e o sequestrador fugiu."
        cat "Não deve ser um detetive muito bom se deixou o culpado fugir."
        cat "Mas não, aparentemente ele ficou bem famoso por solucionar esse caso!"
        cat "Hm, e esse detetive parece estar investigando esse caso novamente."
        cat "Frederico alguma coisa."
        cat "Mas quem se importa com esse humano qualquer, eu vou ser quem vai solucionar esse mistério!"
        cat "Com essas pistas é óbvio que Clotilde não apenas sumiu, ela foi sequestrada!"
        narrative "Primeiro devo achar onde ela foi vista por último"
        narrative "De repente um som alto vem do outro lado da sala fazendo você saltar de susto."
        cockatiel "Craw!"
        narrative "Olhando para trás você vê o passáro maldito que acabou de te dar um dos maiores sustos da sua vida."
        narrative "Você está prestes a mandar uns insultos merecidos em sua direção, quando você sente calafrios ao notar o olhar incessante que a Calopsita de observa."
        cat "Talvez foi uma boa ideia não assustar esse pássaro."
        cat "Ela parece pronta para me comer inteiro."
        narrative "Sentindo-se pertubado pelo olhar da Calopsita você decide dar no pé."
        cat "Tô dando um fora."
        cat "Vou seguir os rastros do Vicente. Quem sabe ele achou alguma coisa."
        cat "Vai que ele é útil uma vez."
    return

label streetChoices: # (Don't change)
    # Finding the female cat
    if selected == "Aproach":
        cat "Bom, não custa nada fazer algumas perguntas."
        narrative "Você se aproxima da gata, que logo nota sua presença."

        show femalecat_neutral at right:
            zoom 0.5
            yalign 1.3
        with dissolve

        femalecat "Olá, meu prezado companheiro felino. Como você vai nesse dia?"
        femalecat "Espero que você não deseje procurar por comida, pois essa lata já tem dono."

        show cat_discussion at left:
            zoom 0.7
            yalign 1.3
        with dissolve

        cat "Não. Você pode ficar com sua lata."
        cat "Só queria saber, você viu um cachorro passar por aqui?"
        cat "Pequeno, com uma roupa de lã, parecendo bem idiota?"
        femalecat "Cachorro? Bem eu não costumo ficar de olho nesses animais pulguentos…"
        femalecat "Mas vi um cachorro grandão passando por aí."
        narrative "Você fica decepcionado com a notícia. Clotilde é muita coisa, mas grande ela não é."
        femalecat "Mas eu ouvi por aí que um animal pequeno causou uma confusão naquela pequena floresta cercada que os filhotes de humanos costumam marcar seu território."
        narrative "Você fica um pouco mais aliviado."
        cat "Muito obrigado! Você me ajudou muito."
        narrative "A gata perde o interesse e volta a procurar comida na lixeira."
        femalecat "Meh"
        cat "Ótimo, vamos logo, um mistério não espera."
        narrative "Você corre em direção ao parque do bairro."

    elif selected == "Ignore":
        narrative "Você decide deixar a gata em paz e continuar rua abaixo, seguindo o rumo dos carros até chegar no trevo onde as ruas se separaram."
        cat "Não é possível. Eu desci toda a rua e ainda não encontrei nada!"
        cat "Será que eu perdi alguma pista no caminho? Não, não pode ser."
        narrative "Você começa a se questionar e decide fazer o caminho de volta pela rua, para ter certeza de que não deixou passar algo importante."
        narrative "Ao voltar você se depara com uma cena de um cachorro grande muito estranho."
        cat "Não pretendo entender o que se passa na cabeça desses animais, mas até para eles esse ai é o mais esquisito."
        narrative "No caminho, você avistou um border collie agindo de maneira extremamente suspeita."

        show dog_neutral at center:
            zoom 0.5
            yalign 1.3
        with dissolve

        narrative "Como outros cachorros, esse ai tinha uma cara idiota, mas parecia estar tentando parecer sério e intimidador."
        narrative "Mas o que mais o chamou a atenção é porque por alguma razão você sentia algo estranho em seu cheiro."
        cat "Esse ai ta muito suspeito."
        cat "Sinto alguma coisa familiar no seu cheiro."

        hide dog_neutral with dissolve

    # Finding the suspecious dog
    if selected == "Follow":
        narrative "Você decide seguir o cachorro suspeito."
        cat "Já perdi tempo demais procurando Clotilde."
        cat "Esse cara tá muito suspeito."
        cat "Com certeza que ele vai me entreter mais."
        narrative "Seguindo o cachorro pela rua você rapidamente começa a se entediar."
        cat "Talvez essa não tenha sido uma boa ideia."
        narrative "Finalmente você avista o cachorro ao longe se encontrando com uma pessoa."
        narrative "Eles estavam em um beco e a visibilidade era baixa, então você mal conseguia enxergar a silhueta da pessoa com quem o cachorro conversava."
        cat "Tenho confiança em meus olhos superiores, mas até eu entendo que há limites."
        narrative "Percebendo que os dois haviam terminado de conversar."
        narrative "Você observa os dois desaparecerem para dentro dos becos."
        cat "É, isso tá muito estranho."
        cat "Vou voltar para casa mesmo, acho que a falta de sono está me fazendo ver coisas."
        narrative "Ignorando o que acabou de ver, você faz o caminho de volta para casa."

    elif selected == "Wait":
        narrative "Você decide que tem coisas mais importantes que seguir um cachorro repugnante."
        narrative "Após o animal desaparecer de sua vista, você continua sua procura."
        narrative "Depois de um tempo, você chega novamente à casa da Teresa, ainda sem ter encontrado nada."

        scene bg_backyard:
            zoom 0.5
        with dissolve

        cat "Onde esse cachorro se meteu?!"
        narrative "Já com fome e cansado, você está prestes a desistir da busca."
        cat "É. Não é minha culpa que não consegui achá-la."
        cat "Ela só não era… achável!"
        narrative "Você decide então não perder mais tempo de seu dia e retornar para casa."
    return

label parkChoices: # (Don't change)
    # Where do cat investigate?
    if selected == "Tracks":
        hide cat_angry with dissolve

        narrative "Você decide explorar perto dos brinquedos no parquinho."

        show cat_suspicious at center:
            zoom 0.3
            xalign 0.7
        with dissolve

        cat "Será que consigo encontrar algo perto dos filhotes de humano?"

        hide cat_suspicious with dissolve

        narrative "Você se depara com muitas crianças brincando no local, correndo pra lá e pra cá e gritando muito."
        narrative "Era de fato uma tarde de sol, então não muito surpreendente."

        show cat_suspicious at center:
            zoom 0.3
            xalign 0.7
        with dissolve

        cat "Como os humanos aguentam todo esse barulho?!"
        narrative "Tentando ignorar o pandemônio ao seu redor, você tenta cheirar por algum rastro de Clotilde."
        cat "Droga! Com tantos cheiros e barulho ao meu redor, fica difícil encontrar qualquer coisa!"
        narrative "Nesse momento, uma criança que acaba de descer do escorregador te olha fixamente, com brilho nos olhos."

        show k_neutral at right:
            zoom 0.4
            xalign 0.3
        with dissolve

        kid "Olha, mamãe! Um gatinho!"
        cat "E-eu?"

        hide cat_suspicious
        show cat_surprised at center:
            zoom 0.3
            xalign 0.7
        with dissolve

        narrative "Seu pelo arrepia e ela começa a ir até você."
        kid "Pspsps, gatinho, gatinho. Vem, pspsps."
        narrative "Nesse momento, ela acelera o passo, e você começa a se afastar."
        cat "Xô, filhote! Estou no meio de uma investigação."

        hide k_neutral with dissolve
        hide cat_surprised with dissolve

        narrative "A criança corre atrás de você, tentando puxar o seu rabo. E você, claro, corre dela. Corre muito."
        narrative "Depois de correr da criança, você chega em um local onde há algumas pessoas sentadas."

    elif selected == "Benchs":
        narrative "Você decide dar uma olhada ao redor dos bancos."

        show cat_suspicious2 at center:
            zoom 0.3
            xalign 0.9
        with dissolve

        cat "Tem muita chance de ela ter passado por aqui. Aquela cadela adora atenção."
        narrative "Examinando ao redor você não vê nenhum sinal de Clotilde, mas não desanima por isso."
        narrative "O que chama a sua atenção é uma velhinha tacando sementes no chão para um grupo de pássaros."
        cat "É, isso não tem nada a ver com a minha investigação."
        cat "Mas…"
        narrative "Seus instintos de gato falam mais alto e você começa a observá-los com muita empolgação."
        cat "Talvez caçá-los não seja má ideia."
        narrative "Quando você pensa em se aproximar dos pássaros apenas por diversão, algo estala em sua mente e você parece ter uma brilhante ideia."
        cat "E se os pássaros viram a Clotilde?! É isso! Para quem mais eu poderia perguntar aqui?"
        narrative "Porém, logo depois você se demonstra meio relutante."
        cat "Humm, mas não sei se eles vão estar dispostos a responder."
        cat "E também… Um gato pedindo ajuda de um pássaro? O que os outros gatos vão pensar de mim?!"

    elif selected == "Clues":
        narrative "Andando pela calçada, você começa a tentar identificar algum cheiro. "
        narrative "Afinal de contas, pode ser provável que Clotilde tenha passado por ali."
        cat "Mas também é um saco investigar perto dos carros, tudo cheira a fumaça."
        narrative "Depois de um tempo sem encontrar nada, você começa a se cansar."
        cat "Clotilde nunca foi a melhor ferramenta do armário."
        cat "Desde quando ela ficou tão boa de evasão?!"
        narrative "Por um momento, você se vê sem esperanças. E com fome também."
        cat "Será que eu deveria desistir e voltar para casa?"

    # Meeting the birds
    elif selected == "Ask":
        narrative "Ignorando sua apreensão pelo momento, você decide se aproximar dos pássaros lentamente, de forma não agressiva."
        narrative "Afinal de contas, considerando que os pássaros são um grupo de medrosos. Vão fugir no primeiro sinal de perigo."
        cat "Ah, olá pássaros…"
        narrative "O gato se mexeu inquieto, se sentindo incômodo."
        narrative "Um corvo salta até parar na frente do gato."

        show crow_neutral at right:
            zoom 0.1
            xalign 0.39
            yalign 0.7
        with dissolve

        crow "Craw"
        crow "O que você quer, gato?"
        narrative "Você, se sentindo mais nervoso do que jamais se sentiu na frente de um pássaro, engole seco."
        cat "Eh, eu estou procurando por um cachorro que deve ter passado por aqui, e eu estava pensando se vocês-"
        crow "Se nós vimos ele?"
        cat "Ela, e sim."
        crow "E você pensa que somos o quê? Seus seguidores?"
        crow "Por que deveríamos te ajudar?"
        narrative "Você se sente perplexo com o questionamento do corvo."
        cat "Quem esse pássaro pensa que é?!"
        cat "Por que eu tô pedindo ajuda, ué."
        crow "Craw craw!"
        narrative "O corvo cai rindo."
        crow "Você realmente está agindo arrogante para alguém pedindo por um favor."
        crow "Não que eu esperaria algo diferente de um gato."
        crow "Mas decidi que vou entretê-lo."
        narrative "O corvo estende uma asa para um lado do parque."
        crow "Eu vi uma cachorrinha vestindo um casaco de lã horroroso passar por lá, perto da rua."
        crow "A coitadinha devia estar super tonta pois estava batendo de cara em todo lugar."
        narrative "Você fica animado com a nova informação."
        cat "O corvo deve ter confundido a cegueira da Clotilde com tontura. Só pode ser ela!"
        narrative "Com isso, você mal espera para continuar sua busca."
        crow "É mais parecia que ela estava com seu dono."
        narrative "Imediatamente seus altos espíritos caem."
        cat "Dono?"
        crow "Sim, um cara alto de terno bege."
        crow "Tinha um cachorro bem grande com ele também."
        crow "Foi lá e levou a cachorrinha embora."
        narrative "Seus recém criados instintos de detetive soam com essas informações."
        cat "Isso é muito suspeito, tem algo errado aqui."

    elif selected == "Ignore":
        narrative "Você decide que é melhor deixar os pássaros em paz."
        cat "Eu sou um gato muito aberto."
        cat "Mas me rebaixar ao nível de ter que pedir ajuda a um pássaro…"
        cat "É, eu nunca viveria essa humilhação."
        cat "Melhor eu continuar procurando por mim mesmo."
        narrative "Você continua andando, agora em direção à calçada."
        cat "Qualquer coisa que um pássaro possa me dizer eu consigo achar por conta própria!"

    # Decision in the sidewalk
    elif selected == "Give up":
        cat "É. Toda essa procura está realmente me cansando."
        cat "Por que eu tô fazendo isso mesmo?"
        cat "Ah, por que a Teresa ainda pode estar lá em casa."
        cat "Acho que vou dormir no teto."
        cat "Vamos deixar essa coisa de detetive para o Vicente mesmo. Ele é quem gosta dessas coisas."
        cat "Eu tenho uma tarde de fazer nada pela minha frente."
        narrative "Você se espreguiça e começa a voltar para casa sem nenhuma pressa."

    elif selected == "Keep going":
        cat "Mas e se a Teresa ainda estiver lá, querendo me enfiar dentro de um casaco de lã?"
        narrative "Você lembra do sufoco e sente um calafrio."
        cat "Talvez eu deva continuar mais um pouco."
        cat "Esse lugar é bem grande, ela deve ter deixado alguma coisa pra trás que eu possa usar para encontrá-la."
        narrative "Você continua andando, tentando ignorar os obstáculos, quando acaba pisando em algo macio. A sensação te lembra algo…"
        narrative "Mais especificamente, você lembra dos suéteres do Vicente que foram tão gostosos de arranhar."
        cat "Pera aí… Será?!"
        narrative "Ao olhar para baixo você percebe que é, realmente, um fio de lã. Você logo se aproxima para sentir o cheiro."
        cat "É pouco, mas eu sinto! Sinto o cheiro da Clotilde… E de repolho."
        narrative "Você se concentra no que acabou de sentir e continua cheirando tudo ao seu redor."
    return

label aaaaaChoices: # (Don't change)
    if selected == "Without":
        narrative "Você decide que se você conseguiu chegar a esse ponto sem Vicente, você não vai precisar de ajuda."
        cat "Eu consigo sozinho, é só achar Clotilde."

        if explored_claras == True:
            cat "E capturar um sequestrador."
            cat "De boas."
            cat "Afinal eu sou um gato e ele apenas um humano."
            cat "A realidade é cruel, mas ele nasceu com a desvantagem."
        else:
            cat "De boas."

        narrative "Você usa o rastro de cheiro deixado para trás do casaco de lã."
        cat "Ela não deve estar longe."
        narrative "Você continua seguindo o cheiro até se deparar com um bueiro quebrado."

        scene bg_manhole:
            zoom 0.4
        with dissolve

        cat "Que estranho. Por que o cheiro de Clotilde iria me levar a esse bueiro?"
        narrative "É nesse momento que você chega a uma realização."
        cat "Não me diga…"
        narrative "Você olha para dentro do bueiro."
        cat "Clotilde! Você me ouve?!"
        narrative "Você espera por qualquer tipo de barulho, até você ouvir uma resposta fraca."
        clotilde "Sim?"
        narrative "Você encara a cachorrinha que tinha caído de tudo no bueiro."
        cat "Como você foi parar aí, Clotilde?!"
        clotilde "Aqui aonde, querido?"
        narrative "Você se sente um idiota, é claro que ela não sabe como ela foi parar ali. Ela é cega."
        cat "Mas eu realmente não vou conseguir tirar ela dali de dentro sozinho."
        cat "Acho que vou precisar trazer Vicente aqui."

    elif selected == "With":
        narrative "Você decide ir em busca de Vicente."
        cat "Acho que lembro dele indo para o parque logo quando eu estava saindo."
        cat "Vou procurar lá."
        narrative "Você pega o casaquinho horroroso em sua boca e volta para dentro do parque."

        scene bg_park:
            zoom 0.4
            xalign 0.8
            yalign 0.5
        with dissolve

        narrative "Não é difícil achar Vicente, que estava olhando ao seu redor."

        show cat_confident at center:
            zoom 0.3
            xalign 0.9
        with dissolve

        cat "Miau! Olha o que tenho aqui, Vicente!"
        narrative "Vicente é atraído pelo miado e nota o casaquinho que você está carregando."

        show vincent_suspicious at right:
            zoom 0.4
            xalign 0.3
        with dissolve

        vincent "Gato, o que você está fazendo com isso?"
        vincent "Onde é que você achou isso?"
        cat "Siga-me!"
        narrative "Você sai correndo, arrastando o casaquinho em direção a trajetória que o cheiro de Clotilde leva."
        narrative "Vicente, mesmo sem entender completamente, sai correndo logo atrás de você."

        hide vincent_suspicious
        show vincent_angry at right:
            zoom 0.4
            xalign 0.3
        with dissolve

        vincent "Onde você está indo Gato?!"
        vincent "Volte aqui!"
        narrative "Você continua correndo - não muito rápido, porque Vicente tem perna fraca - até chegar em um buraco de bueiro."

        scene bg_manhole:
            zoom 0.4
        with dissolve

        narrative "Ambos chegam juntos no bueiro."

    elif selected == "Help":
        cat "Não se preocupe Clotilde, eu vou buscar ajuda!"
        clotilde "Ah, não se preocupe, querido. Eu estou bem confortável aqui."
        clotilde "Tem um tapete macio nesse chão."
        cat "Ela… Está deitada em musgo…"
        cat "Tá, acho que tinha visto Vicente indo para o parque quando saí."

    elif selected == "By yourself":
        cat "Não se preocupe Clotilde, eu vou tentar te ajudar!"
        clotilde "Ah, não se preocupe, meu bem. Eu estou bem confortável aqui."
        clotilde "Tem um tapete macio nesse chão."
        cat "Ela… Está deitada em musgo…"
        narrative "Você desfia com suas garras o casaquinho de lã e tenta dar um nó para prender em umas partes da grade do bueiro."
        narrative "Você utiliza dos seus belos reflexos felinos e desce até lá embaixo com o fio do casaquinho de lã na boca."
        cat "Clotilde, segura em mim que eu vou te tirar daqui"
        clotilde "Segurar onde?"
        narrative "Você perde um pouco a paciência e morde a coleira de Clotilde fazendo força para puxar ela."
        narrative "Utilizando toda a sua força você começa a escalar a roupa de lã segurando a clotilde."
        clotilde "Onde estamos indo?"
        cat "Cala boca Clotilde!"
        cat "Arghhh, essa demonia é muito pesada!"
        narrative "A roupa de lã começa a romper, não aguentando o peso."
        cat "Mais um pouco, estamos quase lá"
        narrative "A lã se rompe e vocês dois caem"
        cat "MALDITA LÃ BARATA!"
        clotilde "Ahhhh!"
        narrative "Ao cair, o musgo prende vocês."
    return

label homeChoices: # (Don't change)
    if selected == "Manchinha":
        cat "Quem é Manchinha?"
        clotilde "Ele é alguém que encontrei lá."
        clotilde "Apenas um filhote, mas muito corajoso."
        clotilde "Só consegui fugir por causa dele."
        cat "Ok, então esse seu amigo cachorro ainda está lá?"
        clotilde "Cachorro, não."
        clotilde "Manchinha é um gatinho."
        narrative "Você se encontra surpreso."
        cat "Que gato que aceitaria o nome de 'manchinha'?!"
        clotilde "E sim, ele ficou lá para lutar contra os homens."
        cat "Hhm…"

    elif selected == "Ran away":
        cat "Clotilde, por quê você estava fora de casa?"
        clotilde "Ah, eu ouvi esse cachorro, um dos grandes."
        clotilde "Ele me disse que precisava que eu fosse com ele, que a Teresa estava em perigo!"
        clotilde "Foi ele que me levou ao homem."
        cat "Então, parece que é uma operação em conjunto…"
        cat "O cão leva os animais até o sequestrador."

        if follow_dog == True:
            cat "Peraí, eu não acabei vendo um cachorro bem suspeito antes?"
            cat "Não existem coincidências nesse mundo."
            cat "Ele é com certeza parte desse caso."

    elif selected == "People":
        cat "Você não acha que essas pessoas poderiam ser de algum abrigo?"
        clotilde "Abrigo?"
        cat "Sim, tipo um lugar que animais vão para serem adotados."
        clotilde "Não, não. Todo animal lá tinha dono, até o Manchinha."
        cat "Se não era abrigo, não pode ser algo bom."
        cat "tem algo mais fundo ocorrendo aqui."
        cat "Melhor perguntar para ver se a Clotilde sabe de mais alguma coisa."

    elif selected == "How many":
        cat "E Clotilde. Você sabe quantos homens estavam trabalhando lá?"
        clotilde "Não tenho certeza, mas ouvi umas três pessoas."
        cat "Ok, não é tanta gente."
        cat "Parece uma operação bem sigilosa."

    elif selected == "Describe":
        cat "Poderia descrever as pessoas para mim?"
        clotilde "Querido, eu sou cega."
        cat "Opa, esqueci desse detalhe."
        cat "Até os melhores detetives fazem erros de vez em quando."

    elif selected == "Continue":
        cat "Já coletei todas informações que preciso."
        cat "Normalmente não daria bola com o que poderia acontecer com a Clotilde."
        cat "Mas isso acabou de ficar muito mais interessante."
        cat "Um caso digno de alguém como eu."

        if follow_dog == True:
            cat "É, o melhor lugar para procurar será no último lugar que Clotilde foi vista…"
            cat "Ou o beco onde avistei aquele cachorro suspeito."
            cat "Onde devo ir?"

            menu:
                "1 - Parque.":
                    $selected = "Park"
                    cat "É, o lugar mesmo para procurar é o parque."
                    cat "Nem sei se aquele cachorro tem algo a ver com o caso."
                    narrative "Você sai correndo de casa em direção ao parque."

                "2 - Beco.":
                    $selected = "Alley"
                    cat "Aquele cachorro era muito suspeito."
                    cat "Não acredito em coincidências, ele definitivamente tem algo a ver com o caso."
                    cat "Melhor ir procurar por pistas lá."
                    narrative "Sem tempo a perder, você corre em direção ao beco que viu o cachorro."

        else:
            cat "Agora que sei tudo isso, o jeito mesmo é começar a procurar pistas."
            cat "O melhor lugar para começar vai ser o parque, onde a Clotilde foi vista por último."
            narrative "Sem perder tempo você sai correndo em direção ao parque em que Clotilde foi achada."

    elif selected == "Why?":
        cat "Clotilde, por quê você é assim?"
        narrative "Clotilde inclina a cabeça em confusão."
        clotilde "Assim como?"
        cat "Azucrinante, uma completa palerma."
        clotilde "Não te entendo."
        cat "Suspiro"

    elif selected == "Ignore":
        cat "Clotilde, você realmente tem umas altas imaginações."
        cat "Vai sonhar em outro lugar e me deixa em paz."
        clotilde "Não! Mas eles estão vindo!"
        clotilde "Você não entende!"
        narrative "Cansado dos gritos incoherentes dessa cadela maluca, você se vira e vai embora."
        cat "Talvez o teto seja um lugar bom para uma soneca?"
        cat "Não é como se eu nunca tivesse dormido lá antes."
        narrative "Ignorando a cadela em seu desespero, você sai de casa e deita no telhado pronto para mais uma soneca."
    return

label clotildeQuests: # (Don't change)
    menu:
        "1 - Pergunte quem é Manchinha.":
            $selected = "Manchinha"

        "2 - Pergunte o por quê de Clotilde ter fugido.":
            $selected = "Ran away"

        "3 - Pergunte quem são essas pessoas.":
            $selected = "People"

        "4 - Pergunte por que Clotilde é tão insuportável.":
            $selected = "Why?"

        "5 - Não pergunte nada. Você não está interessado.":
            $selected = "Ignore"
    return

label askClotilde: # (Don't change)
    menu:
        "1 - Pergunte quantas pessoas haviam lá.":
            $selected = "How many"

        "2 - Peça para Clotilde descrever as pessoas.":
            $selected = "Describe"

        "3 - Já tenho tudo que preciso.":
            $selected = "Continue"
    return

label livingroomChoices: # (Don't change)
    if selected == "How?":
        narrative "Ao fazer essa pergunta você imediatamente sentiu que algo estava errado."
        narrative "Olhando para Clotilde você viu que suas pupilas tinham retraído e sua expressão mostrava choque."
        clotilde "Os homens! Eles vão vir!"
        narrative "Você estava imediatamente surpreso em ver a Clotilde agindo maluca dessa maneira."
        narrative "Mais maluca que o normal você quer dizer."
        cat "Homens? Que homens?"
        clotilde "Você não entende! Eles estão vindo por mim e você!"
        cat "É, eu acho que ela finalmente pirou de vez."
        cat "Quem são esses homens?"
        cat "Por que eles vão voltar?"
        clotilde "Não sei."
        narrative "E pensar que você estava prestes a dar ouvidos para essa maluca comedora de repolho."
        narrative "Mas então Clotilde retornou a falar, para sua surpresa."
        clotilde "Tinha outros cachorros e eu consegui escapar pela grade e acabei caindo no buraco."
        clotilde "Achei que tinha caído no inferno."
        clotilde "Aqueles homens vão voltar para pegar eu e você."
        cat "O que? Eu?"
        cat "Pera, você está me falando que esses homens pegaram você e outros cachorros? Você então não fugiu de casa."
        clotilde "Fugi, fugi, fugi. Mas eles me pegaram."
        clotilde "E Manchinha também."
        narrative "Você ficou se perguntando quem era Manchinha."
        cat "Com esse nome bobo só pode ser cão mesmo."
        cat "Não, então eu estava certo. Tinha mais alguém com a Clotilde."
        cat "Ela estava fugindo desse lugar…"
        cat "Ok, eu preciso ser mais objetivo com esse cachorro se quero descobrir algo."
        cat "Talvez a gente tenha um caso muito maior aqui. O que eu pergunto?"

        $finish_search = False
        while finish_search == False:
            call askClotilde from _call_askClotilde_1
            if selected == "Continue":
                $finish_search = True
            call homeChoices from _call_homeChoices_2
        $selected = "How?"

    elif selected == "Ignore":
        cat "Na verdade esquece ai."
        cat "Já perdi tempo demais com essa cadela."
        cat "Achei e salvei ela do bueiro, quem se importa como ela chegou lá."
        cat "Agora quero meu muito merecido descanso."
        narrative "Cansado com as atividades do dia, você vai para o quarto e se deita em sua cama."
        cat "Bons sonhos a mim."
        narrative "Fechando os olhos você relaxa e dorme para sonhos que não incluem cachorrinhas malucas."
    return

label findingSuspectChoices: # (Don't change)
    if selected == "Ask":
        cat "Não custa nada perguntar."
        cat "Não gosto de admitir, mas estou meio sem saber como prosseguir."
        cat "O, pássaro."
        cat "Se viu algo estranho aqui neste local?"
        cockatiel "Ah, então você está pedindo minha ajuda?"

        if scared_cockatiel == True:
            cockatiel "É, essa coisa não vai rolar."
            cat "Que?"
            cockatiel "Você lembra quando você me assustou antes?"
            cockatiel "Imagino que você achou muito engraçado?"
            cockatiel "Vamos ver se foi engraçado o suficiente agora."
            cockatiel "Ou se você fica parecendo palhaço."
            narrative "Com essas palavras a calopsita se vira, e voa embora."
            narrative "Você, surpreendido, fica sem palavras."
            cat "..."
            cat "Que rato de penas mais audacioso"
            cat "Quem ela pensa que é?"
            cat "Ela vai ver, eu não preciso de sua ajuda."
            cat "Só porque abaixei a cabeça uma vez ela se acha tão alta."
            cat "Eu não preciso dela."
            cat "Na verdade, tenho alguém bem melhor para me ajudar."
            cat "Vicente diz que sabe o que ele está fazendo."
            cat "Com um empurrãozinho tenho certeza que ele me guia direitinho pra esse sequestrador."
            cat "Ele deve estar em casa com a dona Teresa."
            narrative "Determinado, você sai do parque correndo de volta para casa."

        else:
            cockatiel "Hm, acho que posso fazer uma exceção a você gato."
            cockatiel "Tenho que dizer que você… me interessa."
            cockatiel "Apesar de agir de maneira muito previsível."
            cockatiel "Você é… diferente."
            cat "Disturbador…"
            cat "Apesar de ser apenas um pássaro, estou sentindo calafrios com o olhar dessa Calopsita."
            cat "Melhor fazer as perguntas e dar no pé."

            $finish_search = False
            while finish_search == False:
                call askCockatiel from _call_askCockatiel
                if question1 == True and question2 == True and question3 == True:
                    $finish_search = True

            cat "É, já fiz todas as perguntas que precisava."
            cat "Parece que sei direitinho onde encontrar esse malandro."
            cat "Heheh, o rato caiu na ratoeira."
            cat "Você não escapa de mim agora."
            cat "Pode me guiar para esse canil agora?"
            cockatiel "Sim, sim. Vamos lá então."
            narrative "Estendendo suas asas, a Calopsita sai no voo, mas indo em uma velocidade que você consegue acompanhar."
            narrative "Ela te leva para fora do parque e para uma construção na cidade que tinha uma aparência deprimida."
            cockatiel "Craw!"
            cockatiel "Agora é com você, gato estranho."
            narrative "Falando suas últimas palavras, a calopsita vai embora sem olhar para trás."
            cat "Gato Estranho? Você que é estranha pássaro bobo."
            narrative "Mas você não se deixa distrair neste momento, e foca sua atenção na construção à sua frente."
            cat "É agora ou nunca."

    elif selected == "Ignore":
        cat "É, qualquer informação desse pássaro não vai ser confiável."
        cat "Melhor ignorar a peste."
        cat "Do jeito que tá me olhando eu não confio nela, nada não."

        hide cockatiel_neutral
        narrative "Decidindo ignorar a Calopsita, você observa a área ao redor do bueiro."

        scene bg_street:
            zoom 0.4
            yalign 0.3
        with dissolve
        cat "Mas agora preciso de algum modo para encontrar pistas."
        cat "O cheiro está muito fraco aqui."
        narrative "Subitamente uma ideia surge em sua cabeça."
        cat "Já sei!"
        cat "Vicente supostamente é um profissional nisso, não?"
        cat "Eu só preciso fazê-lo achar o esconderijo do sequestrador para mim."
        cat "Com minha ajuda, não há como falhar."
        narrative "Entusiasmado com sua ideia, você vira e sai correndo de volta para casa."
        narrative "Deixando uma calopsita te observando do galho de uma árvore."
    return

label askCockatiel: # (Don't change)
    menu:
        "1 - Perguntar para onde o homem foi.":
            $question1 = True

            cat "Você saberia me dizer para onde o homem que estva com a Clotilde mais cedo?"
            cockatiel "Clotilde, você quer dizer a cadela que você estava procurando antes, correto?"
            cat "Sim, essa mesma."
            cockatiel "Hm, o homem deixou após não conseguir achar essa Clotilde."
            cockatiel "Ele saiu do parque após isso."
            cat "Sabe mais alguma coisa?"
            cockatiel "Talvez…"
            cockatiel "Eu não vi pessoalmente, mas ouvi outros pássaros mencionarem que o homem está operando na cidade."
            cockatiel "Ele e uns outros trabalham em um canil cheio de outros animais."
            cat "Um canil?"
            cockatiel "Sim, mas eles maltratam os animais lá."
            cockatiel "E tem apenas animais com donos também. Nenhum animal de rua."
            cat "Parece ser realmente o local de operações do sequestrador."
            cockatiel "Eu te guio lá quando você terminar suas perguntas."

        "2 - Pedir para descrever o homem.":
            $question2 = True
            cat "Você pode me descrever o homem?"
            cockatiel "Ele era alto, parecia ter bastante grana também."
            cockatiel "Tava vestindo um terno bege e tinha um rosto arrogante."
            cat "Rosto arrogante e terno bege?"
            cat "Espera! Eu vi esse cara!"
            cat "Eu quase fiquei sem cauda por causa dele!"
            cat "Sabia que tinha que ser vilão por falar aquelas coisas repugnantes!"
            cat "Agora que sei como você se parece, você não vai me escapar."

        "3 - Perguntar se tinha mais alguém com o homem.":
            $question3 = True
            cat "Você viu mais alguém com o homem?"
            cockatiel "Com o homem? Acho que não…"
            cockatiel "Espera, tinha aquele."
            cat "Aquele?"
            cockatiel "Depois de sair do parque o homem se encontrou com um cachorro, um dos maiorzinhos."
            cockatiel "Acho que era um Border Collie."
            cat "Então ele não está operando sozinho…"
            cat "Mas é realmente coisa de cachorro, se meter nessa operação."
    return

label kennelv1Choices: # (Don't change)

    if selected == "Press":
        narrative "Sem hesitação você aperta o botão e solta os animais."
        narrative "No canto do seu olho você pode ver um homem vestindo um terno bege se aproximando de você."
        narrative "Se você tivesse hesitado, você teria perdido sua chance de salvar os animais."

        hide manchinha_neutral with dissolve
        hide cat_suspicious with dissolve

        cat "Corre Manchinha!"
        narrative "Se juntando com o grupo de animais correndo para fora, você escapa da construção."
        cat "Peraí, não consigo ver o Manchinha."
        cat "Será que ele ficou lá atrás?"
        cat "Ele é tão pequeno, é óbvio que vai se perder nessa confusão."
        cat "Mas eu já o ajudei antes, tenho mesmo que voltar agora?"

        menu:
            "1 - Voltar pelo Manchinha.":
                $selected = "Back"
                cat "Droga, minha consciência não me permite deixá-lo."
                cat "Melhor me agradecer pelo que estou fazendo."
                narrative "Dando a volta, você corre de volta para dentro do canil."

                scene bg_kennel:
                    zoom 0.5
                    xalign 0.9
                with dissolve

                narrative "Chegando lá dentro, você vê que está quase vazio, apenas com o homem, Manchinha e um border collie."
                narrative "O border collie estava rosnando para Manchinha."
                cat "Esse cheiro…"
                cat "Esse tem que ser o sequestrador!"

                $strange = Character("???", color = "#4ad4f0")

                show frederico_scared at center:
                    zoom 0.5
                with dissolve

                show dog_neutral at right:
                    zoom 0.4
                with dissolve

                strange "Como meu plano foi arruinado?"
                strange "E por meros gatos!"
                strange "E você!"
                narrative "O homem se vira para o border collie."

                hide frederico_scared
                show frederico_angry at center:
                    zoom 0.5
                with dissolve

                strange "Como é que pode deixar essas pestes andarem soltas dessa maneira!"
                strange "Seu cachorro inútil!"
                cat "Que isso? Sei que cão é burro mas você ta indo meio longe."

                play sound "audio/sounds/cachorrao_late.mp3"

                dog "Desculpe-me."
                cat "Ele vai tomar sem dizer nada?!"
                strange "Agora elimine esse lixo, temos que sair daqui."
                strange "Esses animais causaram uma destruição muito grande."
                strange "Logo esse local vai estar infestado de policiais."
                cat "Elimine? Você quer matar Manchinha?"
                cat "Não na minha frente, você não vai!"
                narrative "Correndo até o Manchinha, você pega o homem e o cachorro de surpresa." 
                narrative "Como uma mãe, você agarra Manchinha pela pelagem de seu pescoço, e dá no pé."
                manchinha "[cat]!"
                manchinha "Você veio!"
                cat "Lutar contra super vilões pode ser deixado para outro dia."
                strange "O que você esta esperando cão idiota?!"
                strange "Vá atrás desses gatos!"

                play sound "audio/sounds/cachorrao_late.mp3"
                #latido
                dog "S-sim!"
                narrative "Trazido para fora de seu estupor, o cachorro começa a te perseguir."
                cat "Normalmente escapar seria mais fácil que roubar comida de gatinho, mas estou carregando Manchinha!"
                cat "Preciso achar uma maneira de me livrar desse cão."
                narrative "Olhando ao seu redor você vê apenas as celas abertas."
                cat "Espera aí!"
                cat "Essas jaulas têm um sistema automático de abrir. E se…"
                narrative "Mudando a direção, você corre para perto da jaula mais próxima."
                narrative "Batendo na porta, você nota que ao fechar ela é automaticamente trancada."
                cat "Perfeito."
                cat "Agora é só atrair a fera."
                narrative "Verificando que o cão ainda estava te seguindo, você corre para frente de uma cela aberta."
                narrative "Atento, você espera na frente da porta o cachorro se aproximar."
                manchinha "O que você está fazendo?! Ele vai alcançar a gente!"
                narrative "Ignorando o gatinho pendurado de sua boca, você se concentra no cão se aproximando."
                dog "Desista, meu dono quer vocês mortos e assim é que vocês serão!"
                narrative "Correndo como um touro desenfreado, o cachorro se move para colidir diretamente com você."
                cat "Agora!"
                narrative "Se deslizando para o lado, o cão vai voando direto para dentro da jaula."
                narrative "Sem esperar um instante, você fecha a porta da jaula, trancando o cachorro lá dentro."
                cat "Agora é nosso momento!"
                narrative "Com o homem não podendo fazer nada, você corre para fora do canil, carregando Manchinha em sua boca."
                manchinha "Uwau!"
                manchinha "Isso foi incrível!"
                manchinha "Você foi incrível!"
                cat "Hm, talvez esse Manchinha não seja tão ruim."
                cat "Possivelmente eu tenha julgado ele de maneira muito pesada."
                narrative "Agora longe do perigo, você coloca o Manchinha de volta no chão."
                manchinha "Isso foi tão irado!"
                cat "Sim, sim, eu sou incrível, mas agora quero voltar para casa e dar uma soneca."
                manchinha "Posso ir com você? Por favor!"
                cat "Hm…"
                manchinha "Por favorzinho!"
                cat "Tudo bem."
                manchinha "Iei!"

                scene bg_outside:
                    zoom 0.4
                with dissolve

                narrative "Agora com um passo relaxado, os dois retornam para casa."
                narrative "Entrando pela janela, você ignora Vincent e vai direto para o quarto."

                scene bg_bedroom:
                    zoom 0.4
                with dissolve

                narrative "Deitando em sua cama, você finalmente pode relaxar."
                narrative "E se o novo acompanhante está fazendo você se sentir mais confortável que o normal."
                narrative "É, esse é um segredo para você apenas."

                scene bg_black:
                    zoom 2.0
                with dissolve

            "2 - Continuar sem ele.":
                $selected = "Keep going"
                cat "Cada um por si só."
                cat "Esse mundo é sobrevivência do mais forte."
                narrative "Sem olhar para trás, você continua fugindo da construção."
                narrative "Seguindo o caminho que irá te levar para casa."

                scene bg_bedroom:
                    zoom 0.4
                with dissolve

                narrative "Chegando em casa, você entra pela janela, direto para o quarto."
                cat "Consigo ouvir que Vicente tem visita."
                cat "Cansei desse dia, agora quero é dormir."
                cat "Música estúpida…"
                narrative "Se encolhendo em sua cama, você fecha os olhos pronto para dormir."
                narrative "Logo esquecendo um pequeno gatinho de olhos sonhadores."

                scene bg_black:
                    zoom 2.0
                with dissolve

    elif selected == "Reward":
        narrative "Você hesita."
        cat "Afinal, não devo ser responsável por libertar esses animais."
        cat "Sim, eu mereço mais."
        cat "Não sou como esse gatinho estupido."
        cat "Você precisa aproveitar as oportunidades que vem na vida."

        scene bg_kennel:
            zoom 0.5
            xalign 0.9
        with dissolve

        narrative "Você vira para os outros animais nas jaulas."
        cat "Ouçam, animais!"
        cat "Eu quer-"
        narrative "Subitamente uma sombra aparece sobre você e te joga para longe."
        cat "Gah!"
        manchinha "[cat]!"

        $strange = Character("???", color = "#4ad4f0")

        stop music
        play sound "audio/musics/Cat tensao.wav"
        show frederico_neutral at center:
            zoom 0.5
        with dissolve

        show dog_neutral at right:
            zoom 0.4
        with dissolve

        strange "O que é que temos aqui?"
        strange "Dois gatos brincando com coisas que não deviam."
        narrative "Em sua frente estava um homem vestindo um terno bege, ao seu lado um border collie sentava de maneira atentiva."
        cat "Esse cheiro! Esse cara é o sequestrador."

        hide frederico_neutral
        show frederico_angry at center:
            zoom 0.5
        with dissolve

        strange "Como ousa esse lixo, quase arruína meu trabalho."
        strange "Cão, coloque esses dois em uma jaula e tenha certeza que ela está trancada!"
        #latido
        dog "S-sim."
        narrative "Você tenta se mover, mas você se sente colorido demais para mover um músculo."
        narrative "Agarrado pelo pescoço, você é arrastado para uma das jaulas vazias."
        cat "Como isso pode ser?"
        cat "Eu fui… derrotado?"
        cat "Isso não pode ser."
        narrative "A última coisa que você vê antes de perder a consciência é Manchinha sendo levado para outra jaula."

        scene bg_black:
            zoom 2.0
        with dissolve
    return