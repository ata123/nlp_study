#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import jieba
import re

reload(sys)
sys.setdefaultencoding("utf-8")

jieba.load_userdict("jieba_dict")


def stop_words(file_path):
    stop_word_list = []
    with open(file_path, "r") as f:
        for line in f:
            stop_word_list.append(line.strip())
    return stop_word_list


def main():
    # word = "中国美国"
    stop_word_list = stop_words("stop_words")
    with open("shanghai_bank_news", "r") as test_file:
        for line in test_file:
            for sentence in line.strip().split("。"):
                for item in jieba.cut(sentence):
                    if item.strip() in stop_word_list or item.strip() in ["“","”"," ",",","；", "：","，", "(", ")", "、", "（", "）"] or item.isdigit() or re.match(r"[0-9]*\.[0-9]", item) or len(item) == 0:
                        continue
                    else:
                        print item






if __name__ == "__main__":
    main()
