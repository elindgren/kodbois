import random
from sys import argv
import json


def main(argv):
    word = {"drak", "Mannen", "Öhl", "pojken", "pleb", "tnoy", "helvete", "förgöraren", "kuk",
            "röv", "fan", "dödlig", "kränkt", "döden", "f5xrk", "Quantum", "Dataterminal",
            "Jesus", "senpai", "MILF", "smuts", "fitt", "penis", "gamer", "girl", "boy", "röven",
            "Satan", "Baldur", "Kawaii"}
    try:
        with open('roligaord.json') as json_file:
            data = json.load(json_file).keys()
    except: 
        data = {"Giftlarv", "Kofotsr\u00e5nare", "L\u00f6nef\u00f6rh\u00f6jning", "Ostmarod\u00f6r", "Fnask", "Avloppskrokodil", "traktor", "Snopph\u00e5na", "B\u00e4verk\u00e4rlek", "Bajsmysterie", "Batongluder", "Skr\u00e4ckl\u00e4ger", "Bajsvandal", "Fl\u00e4sk", "Smygfj\u00e4rt", "Dysterkvist", "Stj\u00e4rtbandit", "Framstj\u00e4rt", "Stj\u00e4rtgosse", "runkattack", "Rumpetroll", "venusberg", "gl\u00e4fsa", "strutar", "Bajs", "fruktpadda", "kjolsken", "Munh\u00e5lepulver", "straffknulla", "brunnplockare", "bergsluder", "Fejkmexikan", "hoppj\u00e4rka", "Komutta", "K\u00e5ta", "Raketbanta", "B\u00e5tskalle", "Pump", "Skithuset", "Stj\u00e4rtklyvare", "Hoja", "Porrbluffare", "Kl\u00e4ggveck", "Geggv\u00e4ck", "F\u00e4nk\u00e5l", "Fisk", "Laserturken", "Pruttskatt", "Skr\u00e4ckpadda", "R\u00f6vakrobat", "Apr\u00e5nk", "Urolog", "bastukorv", "Stj\u00e4rtj\u00e4gare", "sillhora", "Torskfusk", "Snusmumrik", "D\u00f6dsost", "p\u00e4rskaft", "Storhora", "Gr\u00f6tb\u00f6g", "bajsh\u00e5l", "Bajsbomba", "\u00c5ngb\u00e5tsrunkare", "Bluffjuice", "Pluskvamperfekt", "Skinkryttare", "sprutluder", "Bajsl\u00e5da", "Purjobonde", "Flak", "Glassh\u00e5na", "Kotte", "Gr\u00f6t", "firremurra", "Lasersex", "tuttar", "R\u00f6vkn\u00e4", "G\u00f6ka", "Buksv\u00e5ger", "Snaska", "Discopulla", "R\u00e4nnskita", "Dumstrut", "Kuckelura", "M\u00f6j", "Varnagel", "Tjyv", "Igga", "Attackh\u00e5ngla", "Chilla", "R\u00f6vhatt", "r\u00e4khj\u00e4rta", "Dalmraggare", "tr\u00e4skfiskare", "Grisabil", "Berikare", "kamelf\u00f6sare", "R\u00e4fsa", "Tuttpsykos", "Domkraft", "Spuggelfitta", "Avf\u00f6ringsattack", "Sugga", "lullerull", "Snopp\u00e4lskare", "Bussfitta", "Noob", "fjortismj\u00e4rd", "Dansbandshingst", "\u00c5derp\u00e5le", "Skr\u00e4cktackling", "Rulleb\u00f6r", "Krumelur", "Fn\u00f6ske", "Bajsklubba", "Kruka", "Smartskalle", "Fnissattack", "Feministfitta", "Fittskaft", "sneknullad", "Fladderfitta", "Solarieknarkare", "Alkopung", "Chipspyroman", "Rumpfett", "Inv\u00e4llare", "Pantoffel", "Porrattack", "slaskfitta", "D\u00f6dsmagneter", "Stj\u00e4rtlapp", "K\u00e5dden", "Roliga ordlistan", "Gitarronani", "Baconterror", "lokt\u00e4vling", "rafsa", "Bondlurk", "Proktolog", "Br\u00f6fitta", "Flensost", "Putsb\u00f6g", "sprutattack", "Klisterlapp", "Slutstation", "Muff", "Attackkyss", "Lurifax", "Hial\u00f6s", "L\u00f6spitt", "Arselgr\u00e4vare", "S\u00e4l", "Framfall", "Pjuck", "Brandbricka", "Dajmkrysset", "trasprolet\u00e4r", "Lismare", "H\u00e5ngelattack", "r\u00e4lsblandare", "Spock", "Krafsa", "Bagbananen", "Horhus", "tjocksmock", "Bergsslyna", "Konkelb\u00e4r", "Julchock", "Rumpkompis", "s\u00f6tm\u00f6ssa", "Runkb\u00f6g", "Lattekris", "Rump\u00e5ngest", "Gnupung", "bertofili", "Sexmass\u00f6r", "Rakabajsare", "R\u00e5b\u00e4ng", "Sj\u00f6korv", "Kringelikrok", "glyttig", "Sp\u00e5n", "Snabel", "Paddgris", "Finska valsen", "buffelmumba", "Flaskfitta", "Ravechock", "Kukpump", "Pottsork", "Rumpfl\u00f6rt", "Afrikanrunk", "stinkmurkla", "Dampa", "Gl\u00f6ttig", "koprolog", "Viktigpetter", "Mupp", "r\u00e4vkn\u00e4", "tokfrans", "knullattack", "Bylingen", "luderdam", "Demondv\u00e4rg", "Skruvad", "Diggeridoo", "v\u00e5rtg\u00e5rd", "sporreluder", "\u00c5lahue", "slapptask", "Avf\u00f6ringskudde", "Dv\u00e4rgliga", "oomkullrunkelig", "Superpippo", "\u00c5ngestrunka", "Grytslyna", "Fetta", "Batongligan", "Bajspackare", "strutkuk", "Gr\u00e5trunka", "Havreporr", "Hunkhelg", "Pung", "Snopprullare", "Fuskskinka", "Slashas", "Bajsnazist", "B\u00e4vernylon", "G\u00f6rg\u00f6tt", "Apskaft", "Snoppskvaller", "Konglomerat", "Knycka", "tr\u00f6skelslickare", "Suggehue", "Sumprunkare", "sk\u00e4ggbiff", "Ballongpr\u00e4st", "Gynekolog", "klottp\u00e5se", "Slumbrand", "Porrpr\u00e4st", "Fl\u00e4sksv\u00e5l", "Hypnosr\u00e5nare", "Kravla", "Fjong", "Gurkburk", "B\u00e4ver"}
    word = word | data

    separator = ["", " ", "/", "\\", "-", "_", "&", "@"]

    def print_names(n):
        output_json = {}
        for i in range(n):
            new_name = ""
            nr_word = random.randint(1, 3)
            for j in range(nr_word):
                #new_name += random.choice(word)
                new_name += random.sample(word, 1)[0]
                if not j == nr_word - 1:
                    new_name += random.choice(separator)
            output_json[i] = new_name
        print(json.dumps(output_json))


    try:
        # num = int(input("Enter number of desired names: "))
        num = int(argv[1])
        print_names(num)
    except:
        print_names(1)

    return 0


if __name__ == "__main__":
    main(argv)
