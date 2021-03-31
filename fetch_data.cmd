curl.exe --create-dirs -o data/large_pinyin.txt https://raw.githubusercontent.com/mozillazg/phrase-pinyin-data/master/large_pinyin.txt&& ^
curl.exe -O https://raw.githubusercontent.com/mozillazg/python-pinyin/master/gen_phrases_dict.py&& ^
py -X utf8 gen_phrases_dict.py data/large_pinyin.txt data/phrases_dict_large.py&& ^
py -X utf8 tidy_phrases_dict.py data/phrases_dict_large.py src/data/custom_phrases_dict.py