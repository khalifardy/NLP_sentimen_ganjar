from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


def tokenize_text(text):
    """
    fungsi untuk merubah text kedalam lis / tokenisasi

    """
    tokenize_text = text.split()
    return tokenize_text


def lemmatisasi_text(token_list, stopwords):
    """
    fungsi untuk extraksi kata menjadi bentuk dasarnya

    """
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    stopwords = stopwords + stopwords_tambahan()
    stopwords.remove("baik")
    stopwords.remove("terus")
    stopwords.remove("tetap")
    stopwords.remove("lanjut")
    stopwords.remove("enak")
    list_kata = []
    for token in token_list:
        try:
            token = dictionary_normalisasi(token)
        except Exception as _:
            token = token
        if token not in stopwords:
            list_kata.append(stemmer.stem(token))

    return " ".join(list_kata)


def dictionary_normalisasi(kata):
    dictio = {
        'diskus': 'diskusi',
        'dongok': 'dungu',
        'kwalitas': 'kualitas',
        'panjenengan': 'anda',
        'uwes': 'sudah',
        'sing': 'yang',
        'erti': 'arti',
        'filosopi': 'filosofi',
        'ngandelin': 'andal',
        'gimn': 'bagaimana',
        'smakin': 'semakin',
        'bkin': 'bikin',
        'followers': 'pengikut',
        'frekwensi': 'frekuensi',
        'rumahbkalian': 'rumah kalian',
        'isin': 'malu',
        'siaap': 'siap',
        'jend': 'jendral',
        'bodol': 'bodoh',
        'milu': 'pemilu',
        'greng': 'goreng',
        'awat': 'gawat',
        'jdinya': 'jadinya',
        'sybolnya': 'symbolnya',
        'beduke': 'beduknya',
        'aamin': 'amin',
        'njaar': 'anjing',
        'syaa': 'insya',
        'sabaaar': 'sabar',
        'dangerous': 'bahaya',
        'rich': 'kaya',
        'yabg': 'yang',
        'disain': 'desain',
        'dadak': 'mendadak',
        'mingkem': 'diam',
        'piye': 'bagaimana',
        'nesu': 'merajuk',
        'lapo': 'kenapa',
        'duwe': 'punya',
        'togak': 'tonggak',
        'berbohonh': 'berbohong',
        'milu': 'pemilu',
        'mensupport': 'mendukung',
        'membutuhkam': 'membutuhkan',
        'perhati': 'perhatian',
        'sodara': 'saudara',
        'berame': 'ramai',
        'kwalitas': 'kualitas',
        'ndoroh': 'tuan',
        'djokowi': 'jokowi',
        'sepanduk': 'spanduk',
        'alhamdulillqh': 'alhamdulillah',
        'semangkin': 'semakin',
        'moga': 'semoga',
        'justeru': 'justru',
        'scra': 'secara',
        'mbuka': 'membuka',
        'bkta': 'bukti',
        'mbuat': 'membuat',
        'kemiskan': 'kemiskinan',
        'jngn': 'jangan',
        'sdng': 'sedang',
        'ahlivsulap': 'ahli sulap',
        'bangkitbersamaet': 'bangkit bersama',
        'sera': 'serah',
        'keli': 'geli',
        'memalujan': 'memalukan',
        'perhati': 'perhatian',
        'gilaklo': 'gila kamu',
        'sbagai': 'sebagai',
        'sbgi': 'sebagai',
        'president': 'presiden',
        'knapa': 'kenapa',
        'nape': 'kenapa',
        'cemana': 'bagaimana',
        'bjir': 'anjing',
        'kalaw': 'kalau',
        'inovative': 'inovatif',
        'sholr': 'sholat',
        'mbelgedhes': 'buruk',
        'kasiam': 'kasihan',
        'jatu': 'jatuh',
        'sono': 'sana',
        'inten': 'intens',
        'propensi': 'provinsi',
        'indonesi': 'indonesia',
        'inibmuncul': 'ini muncul',
        'siip': 'sip',
        'maaih': 'masih',
        'nehiii': 'tidak',
        'libat': 'melibatkan',
        'hiram': 'hitam',
        'bubaaarrr': 'bubar',
        'wafres': 'wapres',
        'elmen': 'elemen',
        'pabowo': 'prabowo',
        'bgaimn': "bagaimana",
        'bangke': 'bangkai',
        'asuuoo': 'anjing',
        'ngotorjn': 'kotor',
        'wako': 'waktu',
        'nuntaskan': 'menuntaskan',
        'kntl': 'kontol',
        'jing': 'anjing',
        'pokokke': 'pokoknya',
        'brkta': 'berkat',
        'mnykai': 'menyukai',
        'anjeng': 'anjing',
        'incer': 'incar',
        'sangking': 'saking',
        'jang': 'jangan',
        'buln': 'bulan',
        'prabowodua': 'prabowo dua',
        'hemattt': 'hemat',
        'edan': 'gilan',
        'balihonye': 'balihonya',
        'usilin': 'usil',
        'genz': 'gen z',
        'kulo': 'saya',
        'gaamau': 'tidak mau',
        'what': 'apa',
        'anwa': 'anwar',
        'mboten': 'tidak',
        'ngapusi': 'berbohong',
        'bgtu': 'begitu',
        'drun': 'kadrun',
        'israellll': "israel",
        'njing': 'anjing',
        'telujuk': 'telunjuk',
        'kesiap': 'kesiapan',
        'cincong': 'bawel',
        'mbacot': 'berbicara',
        'lbih': 'lebih',
        'kepansan': 'kepanasan',
        'lwat': 'lewat',
        'skkap': 'sikap',
        'tlong': 'tolong',
        'ptran': 'putaran',
        'dongoooo': 'dungu',
        'nyet': 'monyet',
        'yidak': 'tidak',
        'nisa': 'bisa',
        'bengokk': 'bodoh',
        'warbysa': 'luar biasa',
        'kenasikat': 'kena sikat',
        'sbnarnya': 'sebenarnya',
        'cuco': 'cocok',
        'mksudnya': 'maksudnya',
        'bebastugaskan': 'bebas tugaskan',
        'taon': 'tahun',
        'dungkul': 'dengkul',
        'tfak': 'tidak',
        'menjelekkkan': 'menjelekkan',
        'manfa': 'manfaat',
        'turus': 'terus',
        'bhwa': 'bahwa',
        'njabat': 'pejabat',
        'apaaaaa': 'apa',
        'ngebokeppp': 'bokep',
        'besarrr': 'besar'


    }
    return dictio[kata]


def stopwords_tambahan():
    return [
        'suzy', 'barbie', 'cabe', 'oppenheimer', 'yeonjun park jihoon',
        'keysia', 'tang', 'mergo', 'nggih',
        'donk', 'dong', 'gera', 'bhaa', 'kaing', 'kans',
        'erickthohirnews', 'sooor', 'sebagai', 'hahaha',
        'wowww', 'hhhhhhhh', 'cuiihh', 'haaa', 'jiahhhh',
        'wkwkwkkw', 'nich', 'hmmm', 'wkwkwk', 'hayuuuu', 'dech',
        'kwkwkwkk', 'kwkww', 'meong', 'haaa', 'owalah', 'wkkwkwkk'

    ]
