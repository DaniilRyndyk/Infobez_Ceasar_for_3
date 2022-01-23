# -*- coding: utf-8 -*-
from notepad.break_notepad.generate_frequency_dict import generate_list_for_frequency_analyse, generate_frequency_dict
from notepad.main import encrypt


def break_notepad(text: str, d: dict = {}) -> str:
    lst = generate_list_for_frequency_analyse()
    lst_from_txt = generate_list_for_frequency_analyse(generate_frequency_dict(text))

    notepad = generate_notepad_from_two_lists(lst, lst_from_txt)
    notepad = modificate_dict(notepad, d)

    return encrypt(text, notepad)


def generate_notepad_from_two_lists(lst1: list, lst2: list) -> dict:
    return {k: v for v, k in zip(lst1, lst2)}


def modificate_dict(notepad: dict, d: dict):

    for key, value in d.items():
        notepad_reversed = {v: k for k, v in notepad.items()}
        orignal_letter = notepad_reversed[value]
        notepad[orignal_letter] = notepad[key]
        notepad[key] = value

    return notepad

print(break_notepad('''ауч ентнлвпу т вйпс 1805 ензу вщтсюаэуц уээу бутпнтэу гслсл, олсшпвэу в блвмпвъсээуц врбслуалвжд рулвв оснзнлнтэд, тюалсыуц туъэнен в ывэнтэнен чэцщц туювпвц, бслтнен блвсьутгсен эу сс тсысл. уээу бутпнтэу чугпцпу эсючнпичн зэсш, к эсс мдп елвбб, чуч нэу ентнлвпу (елвбб мдп анезу энтнс юпнтн, кбналсмпцтгссюц анпичн лсзчврв). т щубвюнычуь, лущнюпуээдь калнр ю члуюэдр пучсср, мдпн эубвюуэн мсщ лущпвывц тн тюсь'''))