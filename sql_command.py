import mysql.connector

# Note: Please use string as all arguments' type

mydb = mysql.connector.connect(
    host="localhost",
    user="manager",
    password="toServer111550009",
    database="db_final"
)
mycursor = mydb.cursor()

# all possible tags
genresList = ['Action', 'Free to Play', 'Strategy', 'Adventure', 'Indie', 'RPG', 'Animation & Modeling', 'Video Production', 'Casual', 'Simulation', 'Racing', 'Violent', 'Massively Multiplayer', 'Nudity', 'Sports', 'Early Access', 'Gore', 'Utilities', 'Design & Illustration', 'Web Publishing', 'Education', 'Software Training', 'Sexual Content', 'Audio Production', 'Game Development', 'Photo Editing', 'Accounting', 'Documentary', 'Tutorial']
categoriesList = ['Multi-player', 'Online Multi-Player', 'Local Multi-Player', 'Valve Anti-Cheat enabled', 'Single-player', 'Steam Cloud', 'Steam Achievements', 'Steam Trading Cards', 'Captions available', 'Partial Controller Support', 'Includes Source SDK', 'Cross-Platform Multiplayer', 'Stats', 'Commentary available', 'Includes level editor', 'Steam Workshop', 'In-App Purchases', 'Co-op', 'Full controller support', 'Steam Leaderboards', 'SteamVR Collectibles', 'Online Co-op', 'Shared/Split Screen', 'Local Co-op', 'MMO', 'VR Support', 'Mods', 'Mods (require HL2)', 'Steam Turn Notifications']
spytagsList = ['appid', '1980s', '1990s', '2.5d', '2d', '2d_fighter', '360_video', '3d', '3d_platformer', '3d_vision', '4_player_local', '4x', '6dof', 'atv', 'abstract', 'action', 'action_rpg', 'action_adventure', 'addictive', 'adventure', 'agriculture', 'aliens', 'alternate_history', 'america', 'animation_&_modeling', 'anime', 'arcade', 'arena_shooter', 'artificial_intelligence', 'assassin', 'asynchronous_multiplayer', 'atmospheric', 'audio_production', 'bmx', 'base_building', 'baseball', 'based_on_a_novel', 'basketball', 'batman', 'battle_royale', 'beat_em_up', 'beautiful', 'benchmark', 'bikes', 'blood', 'board_game', 'bowling', 'building', 'bullet_hell', 'bullet_time', 'crpg', 'capitalism', 'card_game', 'cartoon', 'cartoony', 'casual', 'cats', 'character_action_game', 'character_customization', 'chess', 'choices_matter', 'choose_your_own_adventure', 'cinematic', 'city_builder', 'class_based', 'classic', 'clicker', 'co_op', 'co_op_campaign', 'cold_war', 'colorful', 'comedy', 'comic_book', 'competitive', 'conspiracy', 'controller', 'conversation', 'crafting', 'crime', 'crowdfunded', 'cult_classic', 'cute', 'cyberpunk', 'cycling', 'dark', 'dark_comedy', 'dark_fantasy', 'dark_humor', 'dating_sim', 'demons', 'design_&_illustration', 'destruction', 'detective', 'difficult', 'dinosaurs', 'diplomacy', 'documentary', 'dog', 'dragons', 'drama', 'driving', 'dungeon_crawler', 'dungeons_&_dragons', 'dynamic_narration', 'dystopian_', 'early_access', 'economy', 'education', 'emotional', 'epic', 'episodic', 'experience', 'experimental', 'exploration', 'fmv', 'fps', 'faith', 'family_friendly', 'fantasy', 'fast_paced', 'feature_film', 'female_protagonist', 'fighting', 'first_person', 'fishing', 'flight', 'football', 'foreign', 'free_to_play', 'funny', 'futuristic', 'gambling', 'game_development', 'gamemaker', 'games_workshop', 'gaming', 'god_game', 'golf', 'gore', 'gothic', 'grand_strategy', 'great_soundtrack', 'grid_based_movement', 'gun_customization', 'hack_and_slash', 'hacking', 'hand_drawn', 'hardware', 'heist', 'hex_grid', 'hidden_object', 'historical', 'hockey', 'horror', 'horses', 'hunting', 'illuminati', 'indie', 'intentionally_awkward_controls', 'interactive_fiction', 'inventory_management', 'investigation', 'isometric', 'jrpg', 'jet', 'kickstarter', 'lego', 'lara_croft', 'lemmings', 'level_editor', 'linear', 'local_co_op', 'local_multiplayer', 'logic', 'loot', 'lore_rich', 'lovecraftian', 'mmorpg', 'moba', 'magic', 'management', 'mars', 'martial_arts', 'massively_multiplayer', 'masterpiece', 'match_3', 'mature', 'mechs', 'medieval', 'memes', 'metroidvania', 'military', 'mini_golf', 'minigames', 'minimalist', 'mining', 'mod', 'moddable', 'modern', 'motocross', 'motorbike', 'mouse_only', 'movie', 'multiplayer', 'multiple_endings', 'music', 'music_based_procedural_generation', 'mystery', 'mystery_dungeon', 'mythology', 'nsfw', 'narration', 'naval', 'ninja', 'noir', 'nonlinear', 'nudity', 'offroad', 'old_school', 'on_rails_shooter', 'online_co_op', 'open_world', 'otome', 'parkour', 'parody_', 'party_based_rpg', 'perma_death', 'philisophical', 'photo_editing', 'physics', 'pinball', 'pirates', 'pixel_graphics', 'platformer', 'point_&_click', 'political', 'politics', 'pool', 'post_apocalyptic', 'procedural_generation', 'programming', 'psychedelic', 'psychological', 'psychological_horror', 'puzzle', 'puzzle_platformer', 'pve', 'pvp', 'quick_time_events', 'rpg', 'rpgmaker', 'rts', 'racing', 'real_time_tactics', 'real_time', 'real_time_with_pause', 'realistic', 'relaxing', 'remake', 'replay_value', 'resource_management', 'retro', 'rhythm', 'robots', 'rogue_like', 'rogue_lite', 'romance', 'rome', 'runner', 'sailing', 'sandbox', 'satire', 'sci_fi', 'science', 'score_attack', 'sequel', 'sexual_content', 'shoot_em_up', 'shooter', 'short', 'side_scroller', 'silent_protagonist', 'simulation', 'singleplayer', 'skateboarding', 'skating', 'skiing', 'sniper', 'snow', 'snowboarding', 'soccer', 'software', 'software_training', 'sokoban', 'souls_like', 'soundtrack', 'space', 'space_sim', 'spectacle_fighter', 'spelling', 'split_screen', 'sports', 'star_wars', 'stealth', 'steam_machine', 'steampunk', 'story_rich', 'strategy', 'strategy_rpg', 'stylized', 'submarine', 'superhero', 'supernatural', 'surreal', 'survival', 'survival_horror', 'swordplay', 'tactical', 'tactical_rpg', 'tanks', 'team_based', 'tennis', 'text_based', 'third_person', 'third_person_shooter', 'thriller', 'time_attack', 'time_management', 'time_manipulation', 'time_travel', 'top_down', 'top_down_shooter', 'touch_friendly', 'tower_defense', 'trackir', 'trading', 'trading_card_game', 'trains', 'transhumanism', 'turn_based', 'turn_based_combat', 'turn_based_strategy', 'turn_based_tactics', 'tutorial', 'twin_stick_shooter', 'typing', 'underground', 'underwater', 'unforgiving', 'utilities', 'vr', 'vr_only', 'vampire', 'video_production', 'villain_protagonist', 'violent', 'visual_novel', 'voice_control', 'voxel', 'walking_simulator', 'war', 'wargame', 'warhammer_40k', 'web_publishing', 'werewolves', 'western', 'word_game', 'world_war_i', 'world_war_ii', 'wrestling', 'zombies', 'e_sports']

# dict used in "searchByRnage", format: "condiction":[[use, lowerbound, upperbound],[possible ranges]], use(bool): 0 if not use, lower/upper(int): close interval of range index
rangedict = {
    # for the owner column, range[i] means from range[i] to range[i+1], ex: range[0] = 0 means from 0 to 20000
    "owners":[[0, 0, 11],[0, 20000, 50000, 100000, 200000, 500000, 1000000, 2000000, 5000000, 10000000, 20000000, 50000000]],
    # for following column, use between function as a condiction
    "date":[[0, 0, 22],[1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]],
    "pratio":[[1, 0, 10],[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]],
    "prating":[[0, 0, 11],[0, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 1000000, 10000000]],
    "price":[[0, 0, 9],[0, 1, 2, 5, 10, 20, 50, 100, 200, 500]],
    # for below condiction, 0: not use, 1: use
    "platform":[[1, 1, 1],["windows", "mac", "linux"]]
}


def funList():
    global mydb, mycursor
    taglist = list()
    sql_command = "SELECT count(*) FROM steam_basic_data WHERE price <5"
    mycursor.execute(sql_command)
    results = mycursor.fetchall()
    mycursor.reset()
    for col in results:
        taglist.append(col[0])
    return taglist


def resetAI(tablename):
    global mydb, mycursor
    sql_command = "ALTER TABLE "+tablename+" AUTO_INCREMENT = 1"
    mycursor.execute(sql_command)
    mydb.commit()
    mycursor.reset()

#dictionary with a lot of keys
def appDetailInfo(appid):
    global mydb, mycursor
    infodict=dict()
    if type(appid) != str:
        appid = str(appid)
    mytup = (appid, )
    sql_command = "SELECT * FROM steam_basic_data WHERE appid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    results = results[0]
    mycursor.reset()
    # infodict["id"] = results[0]
    infodict["name"] = results[1]
    infodict["date"] = results[2]
    infodict["developer"] = results[4]
    infodict["publisher"] = results[5]
    infodict["platforms"] = results[6].split(";")
    infodict["age"] = results[7]
    infodict["categories"] = results[8].split(";")
    infodict["genres"] = results[9].split(";")
    infodict["tags"] = results[10].split(";")
    infodict["achievements"] = results[11]
    infodict["pratings"] = results[12]
    # pratio: float, pratiopct: str(percentage)
    if results[12] + results[13] == 0:
        infodict["pratio"] = 0
    else:
        infodict["pratio"] = results[12] / (results[12]+results[13])
    infodict["pratiopct"] = str(round(infodict["pratio"], 3)*100)+"%"
    infodict["avetime"] = results[14]
    infodict["medtime"] = results[15]
    infodict["owners"] = results[16]
    infodict["price"] = results[17]
    sql_command = "SELECT * FROM steam_requirements_data WHERE appid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    results = results[0]
    mycursor.reset()
    if "windows" in infodict["platforms"]:
        infodict["pcreq"] = results[1]
    if "mac" in infodict['platforms']:
        infodict["macreq"] = results[2]
    if 'linux' in infodict['platforms']:
        infodict["linuxreq"] = results[3]
    sql_command = "SELECT * FROM steam_desc_data WHERE appid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    results = results[0]
    mycursor.reset()
    infodict["about"] = results[2]
    infodict["desc"] = results[1]
    sql_command = "SELECT * FROM steam_media_data WHERE appid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    results = results[0]
    mycursor.reset()
    infodict["headimg"] = results[1]
    infodict["backimg"] = results[3]
    infodict["screenshots"] = results[2]
    return infodict

# -1: name has been used, id: new list id
def createFList(uid, listname):
    global mydb, mycursor
    if type(uid) != str:
        uid = str(uid)
    mytup = (listname, uid)
    sql_command = "SELECT COUNT(*) FROM flist_conn_data WHERE listname = %s AND userid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    mycursor.reset()
    if int(results[0][0]) != 0:
        return -1
    sql_command = "INSERT INTO flist_conn_data (listname, userid) VALUES (%s, %s)"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    sql_command = "SELECT last_insert_id()"
    mycursor.execute(sql_command)
    results = mycursor.fetchall()
    mycursor.reset()
    id = int(results[0][0])
    return id

# -1: no flist, list[name, id]: list of flist
def showFList(uid):
    global mydb, mycursor
    if type(uid) != str:
        uid = str(uid)
    flistlist = list()
    mytup = (uid, )
    sql_command = "SELECT COUNT(*) FROM flist_conn_data WHERE userid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    if int(results[0][0]) == 0:
        return -1
    sql_command = "SELECT listname, listid FROM flist_conn_data WHERE userid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    for col in results:
        flistlist.append([str(col[0]), int(col[1])])
    return flistlist

def deleteFList(listid):
    global mydb, mycursor
    if type(listid) != str:
        listid = str(listid)
    mytup = (listid, )
    sql_command = "DELETE FROM flist_data WHERE listid = %s"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    sql_command = "DELETE FROM flist_conn_data WHERE listid = %s"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()

def deleteUserFLists(uid):
    global mydb, mycursor
    mytup = (uid, )
    sql_command = "SELECT listid FROM flist_conn_data WHERE userid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    mycursor.reset()
    for col in results:
        try:
            lid = int(col[0])
            mytup = (lid, )
            sql_command = "DELETE FROM flist_data WHERE listid = %s"
            mycursor.execute(sql_command, mytup)
            mydb.commit()
            mycursor.reset()
        except:
            break
    mytup = (uid, )
    sql_command = "DELETE FROM flist_conn_data WHERE userid = %s"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()

# 0: already in this flist, 1: success
def insertAppIntoFList(appid, listid):
    global mydb, mycursor
    if type(appid) != str:
        appid = str(appid)
    if type(listid) != str:
        listid = str(listid)
    mytup = (listid, appid)
    sql_command = "SELECT COUNT(*) FROM flist_data WHERE listid = %s AND appid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    cnt = int(results[0][0])
    if cnt != 0:
        return 0
    sql_command = "INSERT INTO flist_data VALUES (%s, %s)"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    return 1

# -1: no app, list[id]: list of app
def showAppFromFList(listid):
    global mydb, mycursor
    if type(listid) != str:
        listid = str(listid)
    flistlist = list()
    mytup = (listid, )
    sql_command = "SELECT COUNT(*) FROM flist_data WHERE listid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    if int(results[0][0]) == 0:
        return -1
    sql_command = "SELECT f.appid FROM flist_data AS f WHERE listid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    for col in results:
        flistlist.append([str(col[0]), int(col[1])])
    return flistlist

# 0: not in this flist, 1: success
def deleteAppFromFList(appid, listid):
    global mydb, mycursor
    if type(appid) != str:
        appid = str(appid)
    if type(listid) != str:
        listid = str(listid)
    mytup = (listid, appid)
    sql_command = "SELECT COUNT(*) FROM flist_data WHERE listid = %s AND appid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    cnt = int(results[0][0])
    if cnt != 0:
        return 0
    sql_command = "DELETE FROM flist_data WHERE listid = %s AND appid = %s"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    return 1

# -1: account has been used, id: new account id
def createUserAccount(userName, userPass):
    global mydb, mycursor
    sql_command = "SELECT COUNT(username) FROM user_data WHERE username = %s"
    mytup = (userName, )
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    mycursor.reset()
    cnt = int(results[0][0])
    if cnt != 0:
        return -1
    mytup = (userName, userPass)
    sql_command = "INSERT INTO user_data (username, userpassword) VALUES (%s, %s)"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    sql_command = "SELECT last_insert_id()"
    mycursor.execute(sql_command)
    results = mycursor.fetchall()
    mycursor.reset()
    id = int(results[0][0])
    return id

# -1: account does not exist, 0: password fail, 1: success
def deleteUserAccount(uid, userPass):
    global mydb, mycursor
    if type(uid) != str:
        uid = str(uid)
    sql_command = "SELECT * FROM user_data WHERE userid = %s"
    mytup = (uid, )
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    mycursor.reset()
    try:
        password = str(results[0][2])
    except:
        return -1
    if userPass != password:
        return 0
    deleteUserFLists(uid)
    mytup = (uid, )
    sql_command = "DELETE FROM user_data WHERE userid = %s"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    return 1

# -1: account does not exist, 0: password fail, id: login
def login(userName, userPass):
    global mydb, mycursor
    sql_command = "SELECT * FROM user_data WHERE username = %s"
    mytup = (userName, )
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    mycursor.reset()
    try:
        id = int(results[0][0])
        password = str(results[0][2])
    except:
        return -1
    if userPass != password:
        return 0
    return id

# input should be a list
# -1: input type not list, list[id] sorted by match tags
def searchByTag(taglist):
    global mydb, mycursor
    if type(taglist) != list:
        return -1
    sql_command = "SELECT sb.appid FROM steam_basic_data AS sb WHERE genres LIKE %s OR categories like %s OR steamspy_tags like %s"
    appdict = dict()
    for tag in taglist:
        mytup = ("%"+tag+"%", "%"+tag+"%", "%"+tag+"%")
        mycursor.execute(sql_command, mytup)
        results = mycursor.fetchall()
        mycursor.reset()
        for col in results:
            id = int(col[0])
            if id not in appdict:
                appdict[id] = 1
            else:
                appdict[id] += 1
    applist = sorted(appdict.items(), key = lambda x:(x[1],x[0]), reverse=True)
    for i in range(len(applist)):
        applist[i] = applist[i][0]
    return applist

def searchByRange():
    global mydb, mycursor, rangedict
    sql_command = "SELECT appid FROM steam_basic_data WHERE "
    condiction = '('
    keys = rangedict["platform"][0]
    cnt = 0
    use = 0
    for i in range(0,3):
        if keys[i] == 1:
            if cnt > 0:
                condiction += 'OR '
            condiction += 'platforms like "%'+rangedict["platform"][1][i]+'%" '
            cnt += 1
    if cnt > 0:
        use += 1
        condiction += ')'
    else:
        condiction = ''
    cnt = 0
    if rangedict["owners"][0][0] == 1:
        if use > 0:
            condiction += 'AND '
        use += 1
        condiction += ('substring_index(owners, "-", 1) between '+str(rangedict["owners"][1][rangedict["owners"][0][1]])\
                       +' AND '+str(rangedict["owners"][1][rangedict["owners"][0][2]])+' ')
    if rangedict["date"][0][0] == 1:
        if use > 0:
            condiction += 'AND '
        use += 1
        condiction += ('left(release_date, 4) between '+str(rangedict["date"][1][rangedict["date"][0][1]])\
                       +' AND '+str(rangedict["date"][1][rangedict["date"][0][2]])+' ')
    if rangedict["pratio"][0][0] == 1:
        if use > 0:
            condiction += 'AND '
        use += 1
        condiction += ('if(positive_ratings+negative_ratings=0, 0, positive_ratings/(positive_ratings+negative_ratings)) between '\
                       +str(rangedict["pratio"][1][rangedict["pratio"][0][1]])\
                       +' AND '+str(rangedict["pratio"][1][rangedict["pratio"][0][2]])+' ')
    if rangedict["prating"][0][0] == 1:
        if use > 0:
            condiction += 'AND '
        use += 1
        condiction += ('positive_ratings between '+str(rangedict["prating"][1][rangedict["prating"][0][1]])\
                       +' AND '+str(rangedict["prating"][1][rangedict["prating"][0][2]])+' ')
    if rangedict["price"][0][0] == 1:
        if use > 0:
            condiction += 'AND '
        use += 1
        condiction += ('price between '+str(rangedict["price"][1][rangedict["price"][0][1]])\
                       +' AND '+str(rangedict["price"][1][rangedict["price"][0][2]])+' ')
    mycursor.execute(sql_command + condiction)
    results = mycursor.fetchall()
    mycursor.reset()
    applist = []
    for col in results:
        applist.append(col[0])
    return applist

# input should be a list
# -1: input type not list, list[id] sorted by match words and accuracy
def searchByName(wordlist):
    global mydb, mycursor
    if type(wordlist) != list:
        return -1
    sql_command = "SELECT sb.appid FROM steam_basic_data AS sb WHERE sb.name LIKE %s"
    appdict = dict()
    for word in wordlist:
        mytup = ("%"+word+"%",)
        mycursor.execute(sql_command, mytup)
        results = mycursor.fetchall()
        mycursor.reset()
        for col in results:
            id = int(col[0])
            if id not in appdict:
                appdict[id] = 1
            else:
                appdict[id] += 1
        sql_command = "SELECT sb.appid FROM steam_basic_data AS sb WHERE sb.name LIKE %s OR sb.name LIKE %s OR sb.name LIKE %s OR sb.name LIKE %s"
        mytup = ("% "+word+" %", word+" %", "% "+word, word)
        mycursor.execute(sql_command, mytup)
        results = mycursor.fetchall()
        mycursor.reset()
        for col in results:
            id = int(col[0])
            appdict[id] += 100
    applist = sorted(appdict.items(), key = lambda x:(x[1],x[0]), reverse=True)
    for i in range(len(applist)):
        applist[i] = applist[i][0]
    return applist


"""
#testing code
uid = createUserAccount("A","0800000123")
lid = createFList(str(uid),"MHY")
insertAppIntoFList(1610, lid)
insertAppIntoFList(1670, lid)
flist = showFList(uid)
print(flist)
flist = showAppFromFList(lid)
print(flist)
deleteUserAccount(uid,"0800000123")
resetAI("user_data")
resetAI("flist_conn_data")
"""
