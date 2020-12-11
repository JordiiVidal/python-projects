from madlibs.classes.MadLib import MadLib
from madlibs.classes.Blank import Blank

mad_libs = [
    MadLib(
        "Science",
        "Computer programming",
        "Computer programming is so _! It makes me so excited all the time because I love to _. Stay hydrated and _ "
        "like you are _! ",
        [
            Blank("Adjective"),
            Blank("Verb"),
            Blank("Verb"),
            Blank("Famous Person"),
        ]
    )
]

for mad_lib in mad_libs:

    print(f"---------{mad_lib.category}---------")
    print(f"---------{mad_lib.title}---------")

    for blank in mad_lib.blanks:
        value = input(f"{blank.type_blank} : ")
        blank.set_word(value)

    mad_lib.generate()

    print("---------Result---------")
    print(mad_lib.result)
