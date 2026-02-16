# ============================================================================
# Echoes of Spring — A Ren'Py Visual Novel
# A romance / slice-of-life game with branching paths and multiple endings.
# ============================================================================

# ---------------------------------------------------------------------------
# Image definitions — GPU-scaled with smooth bilinear filtering (vector-like)
# ---------------------------------------------------------------------------

# Backgrounds (smooth-scaled to fill screen, cropping to avoid letterboxing)
image bg town      = Transform("images/bg town.png", size=(config.screen_width, config.screen_height), fit="cover", align=(0.5, 0.5))
image bg cafe      = Transform("images/bg cafe.png", size=(config.screen_width, config.screen_height), fit="cover", align=(0.5, 0.5))
image bg bookshop  = Transform("images/bg bookshop.png", size=(config.screen_width, config.screen_height), fit="cover", align=(0.5, 0.5))
image bg apartment = Transform("images/bg apartment.png", size=(config.screen_width, config.screen_height), fit="cover", align=(0.5, 0.5))
image bg park      = Transform("images/bg park.png", size=(config.screen_width, config.screen_height), fit="cover", align=(0.5, 0.5))
image bg festival  = Transform("images/bg festival.png", size=(config.screen_width, config.screen_height), fit="cover", align=(0.5, 0.5))

# CG event images (smooth-scaled to fill screen)
image cg lanterns sakura  = Transform("images/cg lanterns sakura.png", size=(config.screen_width, config.screen_height), fit="cover", align=(0.5, 0.5))
image cg lanterns akira   = Transform("images/cg lanterns akira.png", size=(config.screen_width, config.screen_height), fit="cover", align=(0.5, 0.5))
image cg painting         = Transform("images/cg painting.png", size=(config.screen_width, config.screen_height), fit="cover", align=(0.5, 0.5))
image cg poetry           = Transform("images/cg poetry.png", size=(config.screen_width, config.screen_height), fit="cover", align=(0.5, 0.5))
image cg manuscript       = Transform("images/cg manuscript.png", size=(config.screen_width, config.screen_height), fit="cover", align=(0.5, 0.5))
image cg festival three   = Transform("images/cg festival three.png", size=(config.screen_width, config.screen_height), fit="cover", align=(0.5, 0.5))

# Character sprites (smooth-scaled to 75% of screen height, aspect ratio preserved)
image sakura happy    = Transform("images/sakura happy.png", ysize=int(config.screen_height * 0.75), fit="contain")
image sakura neutral  = Transform("images/sakura neutral.png", ysize=int(config.screen_height * 0.75), fit="contain")
image sakura sad      = Transform("images/sakura sad.png", ysize=int(config.screen_height * 0.75), fit="contain")
image sakura surprise = Transform("images/sakura surprise.png", ysize=int(config.screen_height * 0.75), fit="contain")

image akira neutral   = Transform("images/akira neutral.png", ysize=int(config.screen_height * 0.75), fit="contain")
image akira happy     = Transform("images/akira happy.png", ysize=int(config.screen_height * 0.75), fit="contain")
image akira sad       = Transform("images/akira sad.png", ysize=int(config.screen_height * 0.75), fit="contain")
image akira surprise  = Transform("images/akira surprise.png", ysize=int(config.screen_height * 0.75), fit="contain")

# ---------------------------------------------------------------------------
# Character definitions
# ---------------------------------------------------------------------------
define mc = Character("[player_name]", color="#c8ffc8")
define s  = Character("Sakura",  color="#ff99cc")   # Warm, artistic barista
define a  = Character("Akira",   color="#99ccff")   # Quiet bookshop owner
define n  = Character("Narrator", color="#ffffff")

# ---------------------------------------------------------------------------
# Relationship / flag variables
# ---------------------------------------------------------------------------
default player_name   = "Alex"
default sakura_points = 0
default akira_points  = 0
default visited_cafe  = False
default visited_shop  = False
default helped_festival = False

# ============================================================================
#  CHAPTER 1 — A New Beginning
# ============================================================================
label start:

    scene bg town with fade

    n "The bus lurches to a stop. Through the dusty window you see cherry-blossom
       petals swirling above a quiet main street."

    n "Welcome to Hanamachi — population 3,200 — the town you'll call home
       for the next year while you finish your studies."

    n "But first…"

    $ player_name = renpy.input("What is your name?", default="Alex").strip() or "Alex"

    mc "So this is Hanamachi… Smaller than I expected."

    n "You step off the bus with a single suitcase and a hand-drawn map your
       grandmother mailed you."

    n "The spring air is sweet with blossoms. Two buildings stand out on the
       main street:"

    n "A cozy café called {b}Petal Brew{/b}, its windows glowing warm orange…"
    n "…and a narrow bookshop called {b}Ink & Pages{/b}, its shelves visible
       through ivy-framed glass."

    menu first_choice:
        n "Where do you go first?"

        "Step into Petal Brew (the café)":
            jump cafe_first

        "Browse Ink & Pages (the bookshop)":
            jump bookshop_first

        "Just head to your apartment":
            jump apartment_first

# ---------------------------------------------------------------------------
label cafe_first:
    $ visited_cafe = True
    scene bg cafe with dissolve

    n "A bell chimes as you push open the door. The scent of freshly ground
       coffee wraps around you."

    show sakura happy at center with dissolve

    s "Welcome to Petal Brew! You must be new — I know every face in this town."
    s "I'm Sakura. Barista, amateur painter, professional overthinker."

    mc "I'm [player_name]. I just moved here for school."

    s "A newcomer! Let me make you my special lavender latte — on the house."

    menu:
        "\"That sounds wonderful, thank you!\"":
            $ sakura_points += 2
            s "Most people are suspicious of lavender in coffee.
               I like you already!"

        "\"I'll just take a regular drip, thanks.\"":
            $ sakura_points += 1
            s "A purist! Respectable."

        "\"Actually, I should get going…\"":
            s "No rush — the door's always open!"
            jump day1_continue

    n "Sakura hums a melody while she works. You notice watercolor paintings
       covering every wall — sunsets, flowers, the town square."

    mc "Did you paint all of these?"

    s "Guilty as charged. Painting keeps me sane between espresso shots."

    $ sakura_points += 1

    jump day1_continue

# ---------------------------------------------------------------------------
label bookshop_first:
    $ visited_shop = True
    scene bg bookshop with dissolve

    n "The door creaks open to reveal floor-to-ceiling shelves overflowing
       with books. A cat sleeps on a stack of paperbacks."

    show akira neutral at center with dissolve

    a "…Oh. A customer."

    n "A young man with reading glasses looks up from behind a cluttered
       counter, a half-finished crossword in front of him."

    a "Sorry — I don't get many visitors. I'm Akira. This is my shop."

    mc "I'm [player_name]. I just arrived in town."

    a "Hanamachi is quiet. Perfect for reading."

    menu:
        "\"Any recommendations for a newcomer?\"":
            $ akira_points += 2
            a "Hmm… Try this."
            n "He hands you a slim novel with a faded cover: {i}Letters from
               a Small Town{/i}."
            a "It's about someone who moves somewhere new and discovers the
               place has its own kind of magic. Seemed fitting."

        "\"This place is amazing — how many books do you have?\"":
            $ akira_points += 1
            a "I stopped counting at four thousand. The cat makes it hard
               to do inventory."

        "\"Just looking around.\"":
            a "Take your time. The cat's name is Hemingway, by the way."
            jump day1_continue

    $ akira_points += 1

    jump day1_continue

# ---------------------------------------------------------------------------
label apartment_first:
    scene bg apartment with dissolve

    n "You decide to settle in first. The apartment is small but clean —
       a single room above a bakery."

    mc "Home sweet home… I guess."

    n "From the window you can see the whole main street. The café and
       bookshop beckon."

    n "Maybe you'll explore tomorrow."

    jump day1_continue

# ---------------------------------------------------------------------------
label day1_continue:
    scene bg apartment with dissolve

    n "Evening falls. You unpack your suitcase and sit by the window."
    n "Cherry-blossom petals drift past the glass. The town is quiet."

    mc "Maybe this year won't be so bad after all."

    n "You set an alarm and drift off to sleep."

    jump chapter2

# ============================================================================
#  CHAPTER 2 — Settling In
# ============================================================================
label chapter2:

    scene bg town with fade

    n "Day two. The morning air is crisp and the street is already alive
       with shopkeepers setting out signs."

    n "You have the whole day free before classes start on Monday."

    menu:
        n "How do you spend your Saturday?"

        "Visit Petal Brew" if not visited_cafe:
            jump cafe_day2

        "Visit Ink & Pages" if not visited_shop:
            jump bookshop_day2

        "Go to the park":
            jump park_day2

        "Help set up the Spring Festival booth":
            jump festival_help

# ---------------------------------------------------------------------------
label cafe_day2:
    $ visited_cafe = True
    scene bg cafe with dissolve
    show sakura happy at center with dissolve

    s "[player_name]! You came back — or is this your first time?"

    mc "First time, actually."

    s "Then you {i}definitely{/i} need a lavender latte."

    $ sakura_points += 1

    s "Hey, the Spring Festival is this weekend. I'm doing a live-painting
       booth. You should stop by!"

    mc "I'd like that."

    $ sakura_points += 1

    jump chapter2_evening

# ---------------------------------------------------------------------------
label bookshop_day2:
    $ visited_shop = True
    scene bg bookshop with dissolve
    show akira neutral at center with dissolve

    a "[player_name]. You actually came."

    mc "You sound surprised."

    a "I am. Not many people seek out bookshops twice."

    $ akira_points += 1

    a "The Spring Festival is coming up. I'm running a poetry reading
       corner. If you're interested."

    mc "I might check it out."

    $ akira_points += 1

    jump chapter2_evening

# ---------------------------------------------------------------------------
label park_day2:
    scene bg park with dissolve

    n "The park sits at the edge of town, wrapped in cherry trees. A small
       pond reflects the pink canopy."

    n "You sit on a bench and breathe. For the first time in months,
       your mind is quiet."

    n "After a while, you notice a flyer pinned to a tree:"
    n "{b}Hanamachi Spring Festival — Volunteers Needed!{/b}"

    menu:
        "Take the flyer and sign up":
            $ helped_festival = True
            n "You pocket the flyer. Maybe it's a good way to meet people."
            jump chapter2_evening

        "Leave it":
            n "You enjoy the silence a while longer before heading home."
            jump chapter2_evening

# ---------------------------------------------------------------------------
label festival_help:
    $ helped_festival = True
    scene bg town with dissolve

    n "You find the festival committee setting up stalls in the town square."
    n "An older woman hands you a hammer and points at a half-built booth."

    n "While you work, two familiar faces appear."

    show sakura happy at left with dissolve
    show akira neutral at right with dissolve

    s "Oh! [player_name]'s helping too!"

    a "…Good to see more volunteers."

    n "The three of you spend the afternoon building booths, stringing
       lights, and arguing about banner colours."

    $ sakura_points += 1
    $ akira_points += 1

    s "This is going to be the best festival yet!"

    a "You said that last year."

    s "And I was right!"

    jump chapter2_evening

# ---------------------------------------------------------------------------
label chapter2_evening:
    scene bg apartment with dissolve

    n "That night, your phone buzzes with a message."

    if sakura_points >= akira_points and visited_cafe:
        s "{i}(text message){/i} Hey [player_name]! Thanks for today.
           See you at the festival? 🌸"
        menu:
            "\"Wouldn't miss it!\"":
                $ sakura_points += 1
            "\"Maybe, we'll see.\"":
                pass
    elif akira_points > sakura_points and visited_shop:
        a "{i}(text message){/i} [player_name]. I set aside a book I think
           you'd like. Come by whenever."
        menu:
            "\"I'll be there tomorrow.\"":
                $ akira_points += 1
            "\"Thanks, I'll try.\"":
                pass
    else:
        n "No messages yet. The town still feels new."

    n "You fall asleep to the distant sound of wind chimes."

    jump chapter3

# ============================================================================
#  CHAPTER 3 — The Spring Festival
# ============================================================================
label chapter3:

    scene bg festival with fade

    n "The day of the Spring Festival arrives. Hanamachi is transformed —
       paper lanterns sway from every post, and stalls line the streets
       with food, crafts, and games."

    n "The whole town seems to be here."

    menu festival_choice:
        n "Where do you go?"

        "Sakura's live-painting booth":
            jump festival_sakura

        "Akira's poetry corner":
            jump festival_akira

        "Wander on your own":
            jump festival_solo

# ---------------------------------------------------------------------------
label festival_sakura:
    scene bg festival with dissolve
    show sakura happy at center with dissolve

    s "[player_name]! You came!"

    n "Sakura stands behind a large canvas, brush in hand, a crowd of
       children watching."

    s "I'm painting the festival in real time. Wanna help? I need someone
       to hold the palette."

    menu:
        "\"I'd love to!\"":
            $ sakura_points += 3

            n "You hold her palette while she paints. Her eyes light up
               when the colours blend just right."

            s "You know, most people think art is about talent. But it's
               really about paying attention."

            s "You seem like someone who pays attention, [player_name]."

            mc "Thanks, Sakura. That means a lot."

            n "She smiles — warm as the lantern light."

        "\"I'll watch from here.\"":
            $ sakura_points += 1

            n "You lean against a post and watch her paint. There's
               something calming about the way she moves."

    jump festival_evening

# ---------------------------------------------------------------------------
label festival_akira:
    scene bg festival with dissolve
    show akira neutral at center with dissolve

    a "I didn't think you'd come to the poetry corner."

    mc "Why not?"

    a "Poetry is an acquired taste. Like black coffee."

    n "The corner is a quiet alcove away from the noise, lit by
       string lights. A few listeners sit on cushions."

    a "I'm about to read one of my own. If you don't mind."

    menu:
        "\"I'd like to hear it.\"":
            $ akira_points += 3

            a "{i}We are letters waiting to be read,
               pages pressed between the days,
               ink still wet from words unsaid —
               quiet in our quiet ways.{/i}"

            mc "That was beautiful, Akira."

            a "…Thank you. I don't usually share my own work."

            n "For a moment, behind the glasses and the careful distance,
               you see something open and vulnerable."

        "\"Sure, go ahead.\"":
            $ akira_points += 1
            a "All right."
            n "He reads softly. The words linger in the air like
               smoke from a candle."

    jump festival_evening

# ---------------------------------------------------------------------------
label festival_solo:
    scene bg festival with dissolve

    n "You wander through the stalls, tasting mochi, watching a goldfish
       scooping game, listening to a folk band."

    n "It's nice, but a small part of you wonders what Sakura and Akira
       are up to."

    if sakura_points > 0:
        n "You catch a glimpse of Sakura painting across the square.
           She waves."
        $ sakura_points += 1

    if akira_points > 0:
        n "You spot Akira reading under a string of lights. He gives
           you a brief nod."
        $ akira_points += 1

    jump festival_evening

# ---------------------------------------------------------------------------
label festival_evening:
    scene bg festival with dissolve

    n "As night falls, the sky fills with paper lanterns released from
       the river bank."

    n "Hanamachi glows gold against the dark hills."

    if sakura_points >= 5 and sakura_points > akira_points:
        jump lanterns_sakura
    elif akira_points >= 5 and akira_points > sakura_points:
        jump lanterns_akira
    elif sakura_points >= 3 and akira_points >= 3:
        jump lanterns_both
    else:
        jump lanterns_alone

# ---------------------------------------------------------------------------
label lanterns_sakura:
    show sakura happy at center with dissolve

    s "Hey, [player_name]. Come watch the lanterns with me?"

    n "You stand side by side at the riverbank. The lanterns drift
       upward like earthbound stars."

    s "You know what they say — if you make a wish on a lantern,
       it'll come true."

    mc "What would you wish for?"

    s "…I think my wish already came true. Someone new to share this with."

    $ sakura_points += 2

    jump chapter4

# ---------------------------------------------------------------------------
label lanterns_akira:
    show akira neutral at center with dissolve

    a "[player_name]. The view is better from the bridge."

    n "You follow Akira to a stone bridge where the lanterns float
       directly beneath you, reflections doubling the light."

    a "I come here every year. It's always been… solitary."

    mc "Not this year."

    a "…No. Not this year."

    $ akira_points += 2

    jump chapter4

# ---------------------------------------------------------------------------
label lanterns_both:
    show sakura happy at left with dissolve
    show akira neutral at right with dissolve

    s "There you are! Come on, the lanterns are starting!"

    a "She's been looking for you. I just happened to be here."

    n "The three of you watch the sky fill with floating light."

    s "Best. Festival. Ever."

    a "…I have to admit, it's up there."

    jump chapter4

# ---------------------------------------------------------------------------
label lanterns_alone:
    n "You watch the lanterns alone from your apartment window."
    n "They're beautiful. But you feel like you're watching from
       the outside."

    mc "Maybe I should put myself out there more…"

    jump chapter4

# ============================================================================
#  CHAPTER 4 — Crossroads
# ============================================================================
label chapter4:

    scene bg town with fade

    n "Weeks pass. Spring deepens into early summer. You settle into
       a rhythm — classes, study sessions, and visits to the café
       and bookshop."

    if sakura_points >= 6 and sakura_points > akira_points:
        jump sakura_route
    elif akira_points >= 6 and akira_points > sakura_points:
        jump akira_route
    elif sakura_points >= 4 and akira_points >= 4:
        jump friendship_route
    else:
        jump solo_route

# ---------------------------------------------------------------------------
#  SAKURA ROUTE
# ---------------------------------------------------------------------------
label sakura_route:
    scene bg cafe with dissolve
    show sakura happy at center with dissolve

    n "You've been spending more and more evenings at Petal Brew after
       closing, watching Sakura paint."

    s "[player_name], can I ask you something?"

    mc "Of course."

    s "I got accepted into an art program in the city. A summer intensive.
       It's an incredible opportunity."

    s "But… I'd have to leave Hanamachi for three months."

    menu sakura_choice:
        "\"You should go. This is your dream.\"":
            $ sakura_points += 3
            jump sakura_ending_good

        "\"I'd miss you, but I think you should do it.\"":
            $ sakura_points += 2
            jump sakura_ending_good

        "\"Do you really want to leave everything here?\"":
            jump sakura_ending_bittersweet

# ---------------------------------------------------------------------------
label sakura_ending_good:
    scene bg cafe with dissolve
    show sakura happy at center with dissolve

    s "You really mean that?"

    mc "I do. Your art deserves to be seen by more than just Hanamachi."

    n "Sakura sets down her brush and looks at you — really looks at you."

    s "You're the first person who's ever said that without any 'but'
       attached."

    s "When I come back… can we watch the lanterns again? Just us?"

    mc "It's a date."

    n "She smiles — that wide, paint-smudged smile — and the café
       feels warmer than it ever has."

    scene black with fade

    n "{b}ENDING: Colours of Tomorrow{/b}"
    n "Sakura leaves for the city, and you exchange letters all summer —
       real paper letters, each one decorated with her sketches."
    n "When autumn comes and the bus pulls into Hanamachi, she's the
       first one off."
    n "She's carrying a new canvas under her arm. When she turns it
       around, it's a painting of you — sitting in Petal Brew,
       illuminated by lantern light."
    n "Some distances only make the heart more vivid."

    return

# ---------------------------------------------------------------------------
label sakura_ending_bittersweet:
    scene bg cafe with dissolve
    show sakura happy at center with dissolve

    s "I… I don't know. Leaving is scary."

    n "You see the conflict in her eyes — the pull of ambition
       against the comfort of home."

    s "Maybe you're right. Maybe I should stay."

    n "She stays. The summer is lovely — long evenings painting
       together, lazy mornings at the café."

    n "But sometimes, when she looks at the horizon, you see
       a question she never asks."

    scene black with fade

    n "{b}ENDING: Still Waters{/b}"
    n "Life in Hanamachi is gentle. Sakura keeps painting, and you
       keep watching. The café never changes."
    n "It's peaceful. It's safe. But on quiet nights, you wonder
       what colours she might have found in the city."
    n "Some doors, once closed, stay closed."

    return

# ---------------------------------------------------------------------------
#  AKIRA ROUTE
# ---------------------------------------------------------------------------
label akira_route:
    scene bg bookshop with dissolve
    show akira neutral at center with dissolve

    n "You've been spending your afternoons at Ink & Pages. Akira has
       started saving a chair for you by the window."

    a "[player_name]. I want to show you something."

    n "He pulls a manuscript from a drawer — handwritten pages,
       hundreds of them."

    a "I've been writing a novel. For three years. No one's read it."

    mc "You want me to read it?"

    a "I want… someone's honest opinion. Before I decide whether
       to send it to a publisher."

    menu akira_choice:
        "\"I'd be honoured. I'll read every page.\"":
            $ akira_points += 3
            jump akira_ending_good

        "\"Only if you're sure. This is very personal.\"":
            $ akira_points += 2
            jump akira_ending_good

        "\"Maybe you should ask someone more qualified.\"":
            jump akira_ending_bittersweet

# ---------------------------------------------------------------------------
label akira_ending_good:
    scene bg bookshop with dissolve
    show akira neutral at center with dissolve

    n "You stay up all night reading. The novel is about a small-town
       shopkeeper who befriends a stranger and learns to open up."

    n "It's beautiful. Quiet, honest, and deeply human."

    mc "Akira… this is extraordinary."

    a "…You think so?"

    mc "I know so. Send it."

    n "For the first time, you see Akira smile — really smile.
       It transforms his whole face."

    a "Thank you. For reading. For staying. For…"

    a "…For paying attention."

    scene black with fade

    n "{b}ENDING: Between the Lines{/b}"
    n "Akira sends the manuscript, and months later, a small
       publisher picks it up."
    n "The dedication reads: {i}'For [player_name] — who read me
       before anyone else did.'{/i}"
    n "On the day the first copy arrives, you sit together in the
       shop with Hemingway purring between you, the words on the
       page a mirror of everything unspoken."
    n "Some stories only need one reader to become real."

    return

# ---------------------------------------------------------------------------
label akira_ending_bittersweet:
    scene bg bookshop with dissolve
    show akira neutral at center with dissolve

    a "You're probably right."

    n "He slides the manuscript back into the drawer. The lock clicks."

    a "Forget I mentioned it."

    n "The distance returns to his eyes. You keep visiting, but
       something has shifted — a wall rebuilt brick by brick."

    scene black with fade

    n "{b}ENDING: Unfinished Pages{/b}"
    n "Akira never sends the manuscript. Ink & Pages stays the same —
       quiet, dusty, beautiful."
    n "You graduate and leave Hanamachi wondering what his novel
       was really about."
    n "Years later, in a secondhand shop in another city, you find
       a slim book with a familiar name on the spine."
    n "You buy it. You never open it."
    n "Some stories are easier left unread."

    return

# ---------------------------------------------------------------------------
#  FRIENDSHIP ROUTE
# ---------------------------------------------------------------------------
label friendship_route:
    scene bg town with dissolve
    show sakura happy at left with dissolve
    show akira neutral at right with dissolve

    n "Spring turns to summer, and the three of you have become
       inseparable — coffee at Petal Brew, reading at Ink & Pages,
       long walks under the cherry trees."

    s "[player_name], Akira and I were talking…"

    a "Don't make it sound like a conspiracy."

    s "We want to do something for the Summer Festival. Together.
       An art-and-poetry exhibit. Your help would mean the world."

    menu:
        "\"Count me in!\"":
            jump friendship_ending

        "\"I'll support you both from the crowd.\"":
            jump friendship_ending_quiet

# ---------------------------------------------------------------------------
label friendship_ending:
    scene bg festival with dissolve
    show sakura happy at left with dissolve
    show akira neutral at right with dissolve

    n "The three of you spend weeks preparing. Sakura paints, Akira
       writes, and you bring it all together."

    n "On festival night, the exhibit draws the biggest crowd
       Hanamachi has ever seen."

    s "We actually did it!"

    a "Against all reasonable expectations."

    n "Under the lanterns, surrounded by art and words and laughter,
       you realise something:"

    n "Love isn't always romantic. Sometimes it's two people who
       make a small town feel like the whole world."

    scene black with fade

    n "{b}ENDING: Three Colours{/b}"
    n "The exhibit becomes an annual tradition. Sakura's paintings
       hang beside Akira's poems, and your name is on every
       programme as co-curator."
    n "Hanamachi stays small. But with friends like these, it
       never feels that way."

    return

# ---------------------------------------------------------------------------
label friendship_ending_quiet:
    scene bg festival with dissolve

    n "You watch from the crowd as Sakura and Akira unveil their
       exhibit. It's wonderful."

    n "They wave at you from across the square, and you wave back."

    scene black with fade

    n "{b}ENDING: Gentle Distance{/b}"
    n "You stay close to both of them, but always a step back.
       It's comfortable. It's safe."
    n "When you leave Hanamachi, you carry two friendships that
       shaped you in quiet, lasting ways."

    return

# ---------------------------------------------------------------------------
#  SOLO ROUTE
# ---------------------------------------------------------------------------
label solo_route:
    scene bg apartment with dissolve

    n "The weeks pass quietly. You study, attend class, and keep
       mostly to yourself."

    n "Hanamachi is peaceful, but you haven't quite found your
       place in it."

    n "On a warm evening, you sit by your window and watch the
       sunset paint the rooftops gold."

    mc "There's still time. I don't have to figure everything out today."

    scene black with fade

    n "{b}ENDING: Open Road{/b}"
    n "You finish the year and leave Hanamachi with good grades and
       a quiet appreciation for small-town life."
    n "No grand romance, no dramatic goodbye — just the memory of
       cherry blossoms and the knowledge that some chapters are
       bridges to the next."
    n "The road ahead is wide open."

    return
