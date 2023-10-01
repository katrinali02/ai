dis_map = {
    'John_Stevens':{ 'John_Stevens':0, 'John_Doe':3, 'Kim_Lee':5, 'Raj_Gupta':5, 'Walter_Walker':1, 'Alex_Robbinson':2, 'Mariana_Cardoso':12 },
    'John_Doe':{ 'John_Stevens':3, 'John_Doe':0, 'Kim_Lee':3, 'Raj_Gupta':3, 'Walter_Walker':4, 'Alex_Robbinson':5, 'Mariana_Cardoso':8 },
    'Kim_Lee':{ 'John_Stevens':5, 'John_Doe':3, 'Kim_Lee':0, 'Raj_Gupta':8, 'Walter_Walker':5, 'Alex_Robbinson':7, 'Mariana_Cardoso':12 },
    'Raj_Gupta':{ 'John_Stevens':5, 'John_Doe':3, 'Kim_Lee':8, 'Raj_Gupta':0, 'Walter_Walker':7, 'Alex_Robbinson':7, 'Mariana_Cardoso':2 },
    'Walter_Walker':{ 'John_Stevens':1, 'John_Doe':4, 'Kim_Lee':5, 'Raj_Gupta':7, 'Walter_Walker':0, 'Alex_Robbinson':1, 'Mariana_Cardoso':15 },
    'Alex_Robbinson':{ 'John_Stevens':2, 'John_Doe':5, 'Kim_Lee':7, 'Raj_Gupta':7, 'Walter_Walker':1, 'Alex_Robbinson':0, 'Mariana_Cardoso':12 },
    'Mariana_Cardoso':{ 'John_Stevens':12, 'John_Doe':8, 'Kim_Lee':12, 'Raj_Gupta':2, 'Walter_Walker':15, 'Alex_Robbinson':12, 'Mariana_Cardoso':0 } }

time_map1 = {
    'John_Stevens':{ 'John_Stevens':None, 'John_Doe':14, 'Kim_Lee':13, 'Raj_Gupta':None, 'Walter_Walker':11, 'Alex_Robbinson':None, 'Mariana_Cardoso':None },
    'John_Doe':{ 'John_Stevens':14, 'John_Doe':None, 'Kim_Lee':14, 'Raj_Gupta':13, 'Walter_Walker':None, 'Alex_Robbinson':None, 'Mariana_Cardoso':None },
    'Kim_Lee':{ 'John_Stevens':14, 'John_Doe':14, 'Kim_Lee':None, 'Raj_Gupta':None, 'Walter_Walker':None, 'Alex_Robbinson':None, 'Mariana_Cardoso':None },
    'Raj_Gupta':{ 'John_Stevens':None, 'John_Doe':14, 'Kim_Lee':None, 'Raj_Gupta':None, 'Walter_Walker':None, 'Alex_Robbinson':None, 'Mariana_Cardoso':12 },
    'Walter_Walker':{ 'John_Stevens':11, 'John_Doe':None, 'Kim_Lee':None, 'Raj_Gupta':None, 'Walter_Walker':None, 'Alex_Robbinson':11, 'Mariana_Cardoso':None },
    'Alex_Robbinson':{ 'John_Stevens':None, 'John_Doe':None, 'Kim_Lee':None, 'Raj_Gupta':None, 'Walter_Walker':12, 'Alex_Robbinson':None, 'Mariana_Cardoso':15 },
    'Mariana_Cardoso':{ 'John_Stevens':None, 'John_Doe':None, 'Kim_Lee':None, 'Raj_Gupta':13, 'Walter_Walker':None, 'Alex_Robbinson':15, 'Mariana_Cardoso':None } }
time_map2 = {
    'John_Stevens':{ 'John_Stevens':None, 'John_Doe':28, 'Kim_Lee':13, 'Raj_Gupta':None, 'Walter_Walker':11, 'Alex_Robbinson':None, 'Mariana_Cardoso':None },
    'John_Doe':{ 'John_Stevens':14, 'John_Doe':None, 'Kim_Lee':14, 'Raj_Gupta':13, 'Walter_Walker':None, 'Alex_Robbinson':None, 'Mariana_Cardoso':None },
    'Kim_Lee':{ 'John_Stevens':14, 'John_Doe':14, 'Kim_Lee':None, 'Raj_Gupta':None, 'Walter_Walker':None, 'Alex_Robbinson':None, 'Mariana_Cardoso':None },
    'Raj_Gupta':{ 'John_Stevens':None, 'John_Doe':14, 'Kim_Lee':None, 'Raj_Gupta':None, 'Walter_Walker':None, 'Alex_Robbinson':None, 'Mariana_Cardoso':12 },
    'Walter_Walker':{ 'John_Stevens':11, 'John_Doe':None, 'Kim_Lee':None, 'Raj_Gupta':None, 'Walter_Walker':None, 'Alex_Robbinson':11, 'Mariana_Cardoso':None },
    'Alex_Robbinson':{ 'John_Stevens':None, 'John_Doe':None, 'Kim_Lee':None, 'Raj_Gupta':None, 'Walter_Walker':12, 'Alex_Robbinson':None, 'Mariana_Cardoso':15 },
    'Mariana_Cardoso':{ 'John_Stevens':None, 'John_Doe':None, 'Kim_Lee':None, 'Raj_Gupta':13, 'Walter_Walker':None, 'Alex_Robbinson':15, 'Mariana_Cardoso':None } }
time_map3 = {
    'John_Stevens':{ 'John_Stevens':None, 'John_Doe':22, 'Kim_Lee':13, 'Raj_Gupta':None, 'Walter_Walker':11, 'Alex_Robbinson':None, 'Mariana_Cardoso':None },
    'John_Doe':{ 'John_Stevens':14, 'John_Doe':None, 'Kim_Lee':14, 'Raj_Gupta':13, 'Walter_Walker':None, 'Alex_Robbinson':None, 'Mariana_Cardoso':None },
    'Kim_Lee':{ 'John_Stevens':14, 'John_Doe':14, 'Kim_Lee':None, 'Raj_Gupta':None, 'Walter_Walker':None, 'Alex_Robbinson':None, 'Mariana_Cardoso':None },
    'Raj_Gupta':{ 'John_Stevens':None, 'John_Doe':14, 'Kim_Lee':None, 'Raj_Gupta':None, 'Walter_Walker':None, 'Alex_Robbinson':None, 'Mariana_Cardoso':12 },
    'Walter_Walker':{ 'John_Stevens':11, 'John_Doe':None, 'Kim_Lee':None, 'Raj_Gupta':None, 'Walter_Walker':None, 'Alex_Robbinson':11, 'Mariana_Cardoso':None },
    'Alex_Robbinson':{ 'John_Stevens':None, 'John_Doe':None, 'Kim_Lee':None, 'Raj_Gupta':None, 'Walter_Walker':12, 'Alex_Robbinson':None, 'Mariana_Cardoso':17 },
    'Mariana_Cardoso':{ 'John_Stevens':None, 'John_Doe':None, 'Kim_Lee':None, 'Raj_Gupta':15, 'Walter_Walker':None, 'Alex_Robbinson':15, 'Mariana_Cardoso':None } }
time_map4 = {
    'John_Stevens':{ 'John_Stevens':None, 'John_Doe':29, 'Kim_Lee':13, 'Raj_Gupta':None, 'Walter_Walker':11, 'Alex_Robbinson':None, 'Mariana_Cardoso':None },
    'John_Doe':{ 'John_Stevens':14, 'John_Doe':None, 'Kim_Lee':14, 'Raj_Gupta':23, 'Walter_Walker':None, 'Alex_Robbinson':None, 'Mariana_Cardoso':None },
    'Kim_Lee':{ 'John_Stevens':14, 'John_Doe':14, 'Kim_Lee':None, 'Raj_Gupta':None, 'Walter_Walker':None, 'Alex_Robbinson':None, 'Mariana_Cardoso':None },
    'Raj_Gupta':{ 'John_Stevens':None, 'John_Doe':14, 'Kim_Lee':None, 'Raj_Gupta':None, 'Walter_Walker':None, 'Alex_Robbinson':None, 'Mariana_Cardoso':12 },
    'Walter_Walker':{ 'John_Stevens':11, 'John_Doe':None, 'Kim_Lee':None, 'Raj_Gupta':None, 'Walter_Walker':None, 'Alex_Robbinson':11, 'Mariana_Cardoso':None },
    'Alex_Robbinson':{ 'John_Stevens':None, 'John_Doe':None, 'Kim_Lee':None, 'Raj_Gupta':None, 'Walter_Walker':12, 'Alex_Robbinson':None, 'Mariana_Cardoso':16 },
    'Mariana_Cardoso':{ 'John_Stevens':None, 'John_Doe':None, 'Kim_Lee':None, 'Raj_Gupta':10, 'Walter_Walker':None, 'Alex_Robbinson':15, 'Mariana_Cardoso':None } }
