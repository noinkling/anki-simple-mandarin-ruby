# -*- coding: utf-8 -*-

# Modified from https://github.com/mozillazg/python-pinyin/blob/master/tidy_phrases_dict.py

import sys
import os


def get_pinyins_via_pinyin_dict(phrases):
    pinyins = []
    for han in phrases:
        pinyin = env['pinyin_dict'][ord(han)].split(',')[0]
        pinyins.append([pinyin])

    return pinyins


def save(new_dict, output_file):
    with open(output_file, 'w') as out_fp:
        out_fp.write('''# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Warning: Auto-generated file, don't edit.
phrases_dict = {
''')
        hanzi_pairs = sorted(new_dict.items(), key=lambda x: x[0])
        for hanzi, pinyin_list in hanzi_pairs:
            #     中国: [[zhōng], [guó]]
            new_line = "    '{hanzi}': {pinyin_list},\n".format(
                hanzi=hanzi.strip(), pinyin_list=pinyin_list
            )
            out_fp.write(new_line)
        out_fp.write('}\n')


def double_check(new_dict):
    os.environ['PYPINYIN_NO_PHRASES'] = '1'
    from src._vendor import pypinyin
    pypinyin.load_phrases_dict(new_dict)

    missing_dict = {}
    for phrases, pinyins in env['phrases_dict'].items():
        if pypinyin.pinyin(phrases, heteronym=True) != pinyins:
            missing_dict[phrases] = pinyins

    return missing_dict


def tidy():
    new_dict = {}
    for phrases, pinyins in env['phrases_dict'].items():
        try:
            pinyins_via_pinyin_dict = get_pinyins_via_pinyin_dict(phrases)
        except KeyError:
            new_dict[phrases] = pinyins
            continue

        if pinyins != pinyins_via_pinyin_dict:
            new_dict[phrases] = pinyins

    return new_dict


def main():
    output = sys.argv[2] or 'src/data/phrases_dict_tidied.py'
    new_dict = tidy()
    save(new_dict, output)

    # This makes the file too big with no benefit for our specific purposes,
    # since we don't use the heteronym functionality.
    # Refer to: https://github.com/mozillazg/python-pinyin/issues/231#issuecomment-794013362
    # missing_dict = double_check(new_dict.copy())
    # new_dict.update(missing_dict)
    # save(new_dict, output)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("""Usage: python tidy_phrases_dict.py INPUT OUTPUT""")
        sys.exit(1)

    input_file = sys.argv[1] or 'src/data/phrases_dict_large.py'
    env = {}

    with open('./src/_vendor/pypinyin/pinyin_dict.py') as fp:
        exec(fp.read(), env, env)

    with open(input_file) as fp:
        exec(fp.read(), env, env)

    main()
