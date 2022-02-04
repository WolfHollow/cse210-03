  
import random

def get_word():
    word_list = ["abruptly","absurd","abyss","affix","askew","avenue","awkward","axiom","azure","bagpipes","bandwagon","banjo","bayou","bayou","beekeeper",
            "blitz","blizzard","boggle","bookworm","boxcar","boxful","buckaroo","buffalo","buffoon","buxom","buzzard","buzzing","buzzwords","cobweb",
            "cockiness","croquet","crypt","curacao","cycle","disavow","dizzying","duplex","dwarves","embezzle","equip","espionage","euouae","exodus",
            "faking","fishhook","fixable","flapjack","flopping","fluffiness","flyby","foxglove","frazzled","frizzled","fuchsia","funny","gabby","galaxy",
            "galvanize","gazebo","giaour","gizmo","glowworm","glyph","gnarly","gnostic","gossip","grogginess","haiku","haphazard","hyphen","icebox","injury",
            "ivory","ivy","jackpot","jaundice","jawbreaker","jaywalk","jazziest","jazzy","jelly","jigsaw","jinx","jiujitsu","jockey","jogging","joking","jovial",
            "joyful","juicy","jukebox","jumbo","kayak","kazoo","keyhole","khaki","kilobyte","kiosk","kitsch","kiwifruit","klutz","knapsack","larynx","lengths",
            "lucky","luxury","lymph","marquis","matrix","megahertz","microwave","mystify","naphtha","nightclub","nowadays","numbskull","nymph","onyx","oxidize",
            "oxygen","pajama","peekaboo","phlegm","pixel","pizazz","pneumonia","polka","pshaw","psyche","puppy","puzzling","quartz","queue","quips","quixotic",
            "quiz","quizzes","quorum","razzmatazz","rhubarb","rhythm","rickshaw","schnapps","scratch","shiv","snazzy","sphinx","spritz","squawk","staff","strength",
            "strengths","stretch","stronghold","stymied","subway","swivel","syndrome","thriftless","thumbscrew","topaz","transcript","transgress","transplant",
            "triphthong","twelfth","twelfths","unknown","unworthy","unzip","uptown","vaporize","vixen","vodka","voodoo","vortex","walkway","waltz","wave","wavy",
            "waxy","wellspring","wheezy","whiskey","whizzing","whomever","wimpy","witchcraft","wizard","woozy","wristwatch","wyvern","xylophone","yachtsman","yippee",
            "yoked","youthful","yummy","zephyr","zigzag","zigzagging","zilch","zipper","zodiac","zombie"]

    
    i = random.randint(0, len(word_list)-1)
    key_word = word_list[i]
    return key_word
