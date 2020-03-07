import random

abc = list("abcdefghijklmnopqrstuvwxyz")

qatext = {
    "Millä ohjelmointikielellä tämä ohjelma on tehty? (perusmuodossa, 6 kirjainta)": "Python",
    "Mikä on seuraavan koodinpätkän ulostulo?\nprint('spameggs'[3:6])": "meg",
    "Mikä on seuraavan koodinpätkän ulostulo?\nspam = ['Hello']\nprint(spam.append('World'))": "None",
    "Millä komennolla otat käyttöön pseudo-satunnaislukujen luomiseen tarkoitetun kirjaston (random)?": "import random",
    "Kuka on ohjelmoinut tämän tietovisan?": "Joel luokalta 9C"
}

qachoose = {
    "Mikä seuraavista vaihtoehdoista on kirjasto, jota voi käyttää pythonilla verkkosivujen haravointiin (web scraping)?": ["urllib.request", "HTTPrequest1.0", "scraperlib"],
    "Ketä pidetään maailman ensimmäisenä ohjelmoijana?": ["Ada Lovelace", "Bill Gates", "Marianne Whiteley", "Tonya Melendez"],
    "Mikä näistä ei ole Pythonin sisäänrakennettu muuttujatyyppi?": ["Kuva", "Boolean", "Merkkijono", "Hakurakenne"],
    "Mitä eroa on metodilla ja funktiolla?": ["Metodi on luokan tai objektin funktio, funktio taas luokkien ja objektien ulkopuolinen funktio.", "Niillä ei ole eroa.", "Metodia voi käyttää vain kerran.", "Funktio antaa ulostulon, metodi taas muuttaa muuttujia."],
    "Mikä näistä on Pythonilla tehty dynaamisia palvelimia käyttävien verkkosivujen (ja niiden palvelinten!) kehittämiseen tarkoitettu verkkokehys (web framework)?": ["Django", "Node.js", "PHP: Hypertext preprocessor (PHP)", "Github"]
}

score = 0
maxscore = len(qachoose) + len(qatext)

while len(qatext) + len(qachoose) > 0:
    if (len(qatext) > 0) and (len(qachoose) > 0):
        text = random.choice([True, False])
    elif len(qatext) > 0:
        text = True
    else:
        text = False

    if text:
        q = random.choice(list(qatext))
        print(q)
        if (input(">").lower() == qatext[q].lower()):
            print("{} on oikein. Sait yhden pisteen.\n".format(qatext[q]))
            score += 1
        else:
            print("Väärin. Oikea vastaus on {}.\n".format(qatext[q]))
        qatext.pop(q)
    else:
        q = random.choice(list(qachoose))
        print(q)
        answers = qachoose[q].copy()
        random.shuffle(answers)
        correct = answers.index(qachoose[q][0])
        i = 0
        for option in answers:
            print(abc[i] + ") " + option)
            i += 1
        a = input(">")
        if (a.lower() == qachoose[q][0].lower()) or ((a.lower() in abc) and (abc.index(a.lower()) == correct)):
            print("{} on oikein. Sait yhden pisteen.\n".format(qachoose[q][0]))
            score += 1
        else:
            print("Väärin. Oikea vastaus on {}.\n".format(qachoose[q][0]))
        qachoose.pop(q)

print("Pisteet: {}/{}\nVastaustarkkuus: {}%".format(score, maxscore, (score / maxscore) * 100))
