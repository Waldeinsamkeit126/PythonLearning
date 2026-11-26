# Python程序设计 第三次作业 第1题（25分）
# 只补全下面两个函数，保留测试与输出代码。


def decode(text, shift):
    # TODO: 逐个处理字符，英文字母沿加密的相反方向循环移动shift格
    result = ""
    for ch in text:
        if 'a' <= ch <= 'z':
            pos = ord(ch) - ord('a')
            new_pos = (pos - shift) % 26
            new_ch = chr(new_pos + ord('a'))
            result += new_ch
        elif 'A' <= ch <= 'Z':
            pos = ord(ch) - ord('A')
            new_pos = (pos - shift) % 26
            new_ch = chr(new_pos + ord('A'))
            result += new_ch
        else:
            result += ch
    # TODO: 保留大小写，其他字符保持不变，返回完整字符串
    return result
    pass


def find_message(ciphertext, clue):
    # TODO: 尝试0～25的偏移量，调用decode得到候选明文
    for i in range(0, 26):
        trial = decode(ciphertext, i)
    # TODO: 利用已知线索找到原文，匹配时忽略大小写
        if clue.lower() in trial.lower():
    # TODO: 返回(加密偏移量, 原文)
            return i, trial
    pass


# 以下为提供的测试与输出代码，请保留，不需要修改。
clue = "the eagle has landed"
test_cases = [('Wkh hdjoh kdv odqghg. Phhw dw jdwh 7.', 3, 'The eagle has landed. Meet at gate 7.'),
 ('Le 09:00, ESP PLRWP SLD WLYOPO. Hlte!', 11, 'At 09:00, THE EAGLE HAS LANDED. Wait!'),
 ('Lhrrhnm bnlokdsd: sgd dzfkd gzr kzmcdc', 25, 'Mission complete: the eagle has landed'),
 ('The eagle has landed.', 0, 'The eagle has landed.'),
 ('Iypun thw G. Aol Lhnsl Ohz Shuklk. Nv!', 7, 'Bring map Z. The Eagle Has Landed. Go!')]
passed_count = 0
for index, (ciphertext, expected_shift, expected_text) in enumerate(test_cases, 1):
    result = find_message(ciphertext, clue)
    passed = result == (expected_shift, expected_text)
    print(f"情报{index}：{'通过' if passed else '未通过'}")
    if passed:
        passed_count += 1
    if index == 1:
        print(f"截获密文：{ciphertext}")
        print(f"破解结果：{result}")

# 另外独立检查解密函数，包含字母表边界、标点、数字与空字符串。
decode_cases = [("Abc XYZ! 123", 3, "Xyz UVW! 123"), ("", 7, "")]
for index, (text, shift, expected) in enumerate(decode_cases, 1):
    passed = decode(text, shift) == expected
    print(f"字符解密{index}：{'通过' if passed else '未通过'}")
    if passed:
        passed_count += 1
print(f"通过测试：{passed_count}/{len(test_cases) + len(decode_cases)}")
