from typing import List
import os 
from pydub import AudioSegment

def get_all_letters():
    dir = "./audio/"
    letters = []
    for file in os.listdir(dir):
        if not ("dot" in file or "dash" in file):
            letters.append(file.replace(".m4a",""))
            #add special case
    return letters
           
LETTERS = get_all_letters()
dipthongs = list(filter(lambda x: len(x) > 1,LETTERS))
class Syllable():
    def __init__(self,letters:str):
        self.letters = letters
        # self.duration = duration
    def __repr__(self):
        return self.letters
        
def get_word_sound(word:List[Syllable]):
    sound_map = []
    merged = get_sound(word[0])
    sound_map.append((word[0].letters,len(merged)))
    for syllable in word[1:]:
        audio = get_sound(syllable)
        sound_map.append((syllable.letters,len(audio)))
        merged += audio
    merged.export("./merged",format="mp3")
    return sound_map

def get_sound(syllable:Syllable):
    if "!" in syllable.letters:
        return AudioSegment.empty()
    else:
        audio = AudioSegment.from_file(f'./audio/{syllable}.m4a')
        return audio
    
    


    
#get all the syllables in a specific word
def get_syllables(word:str)-> List[Syllable]:
    seek_index = 0
    word_letters = []
    while seek_index < len(word):
        seek_update = 0
        letter = word[seek_index].upper()
        for dipthong in dipthongs:
            if dipthong.startswith(letter):
                next_letter = word[seek_index + 1].upper()
                if dipthong.endswith(next_letter):
                    word_letters.append(Syllable(dipthong))
                    seek_update = 2
        if seek_update != 2:
            if letter in LETTERS:
                word_letters.append(Syllable(letter))
            else:
                word_letters.append(Syllable(f'{letter}!'))
            seek_update = 1

        seek_index += seek_update
        
    return word_letters
            


def process_text(word:str):
    return get_word_sound(get_syllables(word))

