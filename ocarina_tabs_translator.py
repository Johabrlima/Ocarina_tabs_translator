TRANSLATOR = {
    "A4" : "A",
    "A#4" : "B",
    "B4" : "C",
    "C5" : "D",
    "C#5" : "E",
    "D5" : "F",
    "D#5" : "G",
    "E5" : "H",
    "F5" : "I",
    "F#5" : "J",
    "G5" : "K",
    "G#5" : "L",
    "A5" : "M",
    "A#6" : "N",
    "B5" : "O",
    "C6" : "P",
    "C#6" : "Q",
    "D6" : "R",
    "D#6" : "S",
    "E6" : "T",
    "F6" : "U",
}

def list_archive():
    """transforms a text archive into a list"""
    archive_name = input()

    notes_list = []
    with open(archive_name) as archive:
        for line in archive:
            notes_list.append(line.strip().split())

    return notes_list, archive_name

def translated_notes(notes):
    """creates a list of the translated notes using the dictionary TRANSLATOR"""
    
    translated_notes_list = []
    for list_notes in notes:
        for note in list_notes:
            translated_notes_list.append(TRANSLATOR.get(note, note))

    return translated_notes_list

def create_translated_archive(notes, untranslated_archive):

    translated_archive = untranslated_archive[:-3] + 'o'
    with open(translated_archive, 'w') as archive:
        print(*notes, sep=' ', file=archive)

def main():
    
    notes, archive_name = list_archive()
    notes_translated = translated_notes(notes)
    create_translated_archive(notes_translated, archive_name)

main()