import random       # because we'll need this ha, ha, ha

# the vocabulary could just be a single list but I've organized more-or-less
# in case I want to try a few grammaticaly rules later:

people = [
    'Bruno Brookes',
    'Anthea Turner',
    'Robbie Williams',
    'Sam Plank',
    'Reginald Mitchell',
    'Wendy Turner',
    'Neil Morrisey',
    'Jaybez',
    'James Brindley',
    'mar lady',
    'mar mate',
    'ar yuth',
    'mayun',
    'these do-gooders',
    'may un mar lady',
    'me Dad',
    'me Mum',
    'Lemmy Kilmister',
    'er upstairs',
    'Slash from Guns \'n Roses',
]

places = [
    'up Fegg Hayes',
    'on Silverdale',
    'up Anley duck',
    'up Almerend',
    'dayn Castle',
    'up Albermarl reowd',
    'in Fenton',
    'me caravan in North Wayulz',
    'Jamage Industriul Estate',
    'on the A34',
    'on the dee reowd',
    'along the A500',
    'Anley Museum',
    'dayn the pub',
    'dayn the club',
    'dayn the tayn',
    'dayn pit',
    'me kayne-slice',
    'dayn Westport Lake',
    'up Unity House',
    'up Potteries Shopping Center',
    'dayn Fezzie Park',
    'up at Victoria Orrl',
    'up Auger\'s Bonk',
    'bin up Neck End',
    'over Porthill Bonk',
    'over Adeley way, lark',
    'Pot Banks',
    'the colliery',
    'Jamland',
    'th\'appy-clappy',
]

put_downs = [
    'are anna gorra clew',
    'dooin me-yed in',
    'conner stand im',
    'conner stand er',
    'yer wonner fight',
    'oh yer startin',
    'gerrin on me nerves',
    'serves thee sen rayt',
    'yull catch yer deather cold',
    'rayt mard you are',
    'yull get chin-cough',
    'oh av yerd im',
    'dead sad you are'
]

greetings = [
    'ay up duck.',
    'oow reet.',
    'ay up mar mate.',
    'oow at.',
    'say thee!',
]

beverages = [
    'a pint o Bass',
    'a pint o Mayuld',
    'a seowuderanlime',
    'a brew',
    'a birrer Kaynesul Pop',
    'four tins of Steller',
]

cuisine = [
    'oatcake',
    'cheesey oatcake',
    'bacon cheese oatcake',
    'dead nice oatcakes',
    'mmmmm, oatcakes',
    'sausage, bacon and cheese oatcake',
    'dead nice Balti tharriz',
    'chayz butty',
    'amunchayz butty',
    'bacon bap',
    'packeet o sult un vineeger crisps playz, duck.',
]

stop_words = [
    'may',
    'lark',
    'ast',
    'dunner',
    'dunnerafter',
    'yer woh',
    'conner',
    'anner',
    'reet',
    'onner',
    'onneravvin',
    'worrabite',
    'bostid',
    'abite',
    'thee sen',
    'me sen',
    'a saggermaker\'s bottom knocker',
    'ruddy',
    'ruddy great',
    'dirty great',
    'fer',
    'me duck',
    'worrabite',
]

verbs = [
    'gowin',
    'avvin',
    'ramblin ter me sen',
    'ramblin on and on',
    'gerrin',
    'sez',
    'put th\'binz ite',
    'put ke\'ul on duck',
    'graggin',
    'werritin',
    'shermozzlin',
    'lozerkin',
    'fang owd',
    'purrer dayn!',
    'purrim dayn!',
    'get theesen',
    'gowin wom',
    'slopin off',
]

questions = [
    'ast tha thote abite snappin?',
    'ast tha got thee buz fair',
    'av yer gorra neow meowbiyul',
    'ast tha gorra wotch',
    'ast tha got thee specs?',
    'worrer yer doin neow?',
]

institutions = [
    'Potteries Motor Traction',
    'Scragg\'s Coaches',
    'Stoke Poly',
    'the Mitch',
    'Stoke City',
    'the Vale',
    'on Radio Stoke',
    'Signul',
    'up the Crem',
    'in the Creowun',
    'deowun the Roe-Buck',
    'in the Vine',
    'the Snayd Arms',
    'the Rigger',
    'up Shelton Bar',
    'in th\'Sen-nul',
    'E.R.F',
    'Foden\'s',
    'Caudwell Communications',
    'at Rists',
    'J. Arthur Bower\'s Teapots',
    'Spode\'s',
    'Wedgewood\'s',
    'the Adams family of potters',
]

random_statements = [
    'cost kick a bo againt a wo an then it eet wi thee yed till eet bosses',
    'ar anner gorra peowund!',
    'thars anuther thray peowund up the wall',
    'ar well, thars wun less day ter live',
    'ahm swealterin',
    'ahm frayzin ar ahm',
    'conner get meeyed reowund eet ar conner',
    'werretin on abite sommert',
    'any reowd',
    'pick up thee muskeet',
    'it\'s black over Bill\'s Mother\'s',
    'saves yer mauwlin with eet any reowd',
]

# the corpus is really just a list of the above lists:
corpus = [people, places, put_downs, greetings, beverages, 
    cuisine, stop_words, verbs, questions, institutions, random_statements]

# oh yeah, this is tricky to explain:
sentence_endings = ( '.', '. ', '?', '? ', '!', '! ')

# :
def capitalize(line):
    """Capitalize the first char in a string

    string.capitalize messes up deliberate upper cases in the strings so 
    here's a dedicated function.

    Args:
        line (str): The string to capitalize

    Returns:
        str: The capitalized string

    """
    return line[0].upper() + line[1:len(line)]


def generate_paragraph():
    """Generate a paragraph of North Staffordshire Gibberish

    Args:
        None

    Returns:
        str: A paragraph of North Staffordshire Gibberish

    """
    text = ''
    sentence_word_count = 0
    for i in range(0, random.randint(20, 40)):
        # chose a random section from the corpus
        section = random.choice(corpus)
        # chose a random string from the section
        word = random.choice(section)
        # if the paragraph so far ends with a completed sentence then
        # the new selection needs to be capitalized:
        if text == '' or text.endswith(sentence_endings):
            word = capitalize(word)
        # now it can be appeneded to the paragraph
        text += word
        # reset the counter if we just finished a sentence:
        if text.endswith(sentence_endings):
            sentence_word_count = 0
        else:
            # otherwise increment it:
            sentence_word_count += 1
        # if there are more than 5 "words" (keeping in mind a word
        # can actually contain several words) then reset the counter:
        if sentence_word_count > 6:
            sentence_word_count = 0
            # And if the sentence is complete just add a space
            if text.endswith(sentence_endings):
                text += ' '
            else:
                # otherwise give it a full-stop:
                text += '. '
        else:
            # if the sentence isn't yet 5 words increment the counter
            # and add a space
            text += ' '
            sentence_word_count += 1
    # when the paragraph is complete make sure it has a proper punctuation
    # at the end before returning:
    if text.endswith(sentence_endings):
        return text.strip()
    else:
        return text.strip() + '.'


def generate_potters():
    """Generate a list of 3 paragraphs of North Staffordshire Gibberish

    Args:
        None

    Returns:
        list(str): A list of strings, each containing a paragraph

    """
    paragraphs = []
    for i in range(0, 3):
        paragraphs.append(generate_paragraph())
    return paragraphs