#####################
#   Title:
#       House water tank supply task
#   Description:
#       - At the beginning, find case that there is only one way to add the tank (e.g. H- ... -H ...-HH-)
#       - Secondly, excludes the fault conditions incl. no space (e.g. HHH, HH@most left or HH@most right)
#         or no house.
#       - Thirdly, consider the three houses condition H-H-H, the most efficient way to add the tank is HTHTH
#       - Next, consider the two houses condition H-H. But need to exclude the case that there is a tank on the
#         left or right
#       - Furthermore, Check if there is any house stand alone and haven't got water tank HH- or --H--
#       - Finally, check the excess tank, in condition of HTHTHTH which be added an extra tank by the previous steps.
######################

def solution(S):
    # find the invalid data
    if "-" not in S or "H" not in S:
        return -1
    if "HHH" in S:
        return -1
    if S[:2] == "HH" or S[-2:] == "HH":
        return -1
    # first consider the cases have only one way to add the tank H- ... -H ...-HH-
    if S[:2] == "H-":
        S = S[:1] + 'T' + S[2:]
    if S[-2:] == "-H":
        S = S[:-2] + 'T' + S[-1:]
    pre_pos = 0
    temp_s = S
    while 1:
        pos = temp_s.find("HH")
        if pos == -1:
            break
        S = S[:pre_pos + pos - 1] + 'THHT' + S[pre_pos + pos + 3:]
        temp_s = temp_s[pos + 3:]
        pre_pos = pre_pos + pos + 3
    # 2nd consider when "H-H-H" there are at least 2 tank needed
    pre_pos = 0
    temp_s = S
    while 1:
        pos = temp_s.find("H-H-H")
        if pos == -1:
            break
        try:
            S = S[:pre_pos + pos + 1] + 'T' + S[pre_pos + pos + 2] + 'T' + S[pre_pos + pos + 4:]
        except Exception as e:
            break
        temp_s = temp_s[pos + 5:]
        pre_pos = pre_pos + pos + 5
    # 3rd consider when "H-H" there are at least 1 tank needed
    pre_pos = 0
    temp_s = S
    # print(S)
    while 1:
        pos = temp_s.find("H-H")
        if pos == -1:
            break
        if pre_pos + pos == 0:
            if pre_pos + pos + 2 == len(S) - 1:
                S = S[:pre_pos + pos + 1] + 'T' + S[pre_pos + pos + 2:]
                break
            if S[pre_pos + pos + 3] != 'T':
                S = S[:pre_pos + pos + 1] + 'T' + S[pre_pos + pos + 2:]
                temp_s = temp_s[pos + 3:]
                pre_pos = pre_pos + pos + 3
            else:
                temp_s = temp_s[pos + 4:]
                pre_pos = pre_pos + pos + 4
        else:
            if S[pre_pos + pos - 1] != 'T':  # exclude the TH-HT case
                if pre_pos + pos + 2 == len(S) - 1:
                    S = S[:pre_pos + pos + 1] + 'T' + S[pre_pos + pos + 2:]
                    break
                else:
                    if S[pre_pos + pos + 3] != 'T':
                        S = S[:pre_pos + pos + 1] + 'T' + S[pre_pos + pos + 2:]
                        temp_s = temp_s[pos + 3:]
                        pre_pos = pos + 3
            else:
                temp_s = temp_s[pos + 1:]
                pre_pos = pre_pos + pos + 1
    # 4th check if there is any house without tank
    pre_pos = 0
    temp_s = S
    while 1:
        pos = temp_s.find("H")
        if pos == -1:
            break
        if pre_pos + pos == 0:
            if S[pre_pos + pos + 1] == '-':
                S = S[:pre_pos + pos + 1] + 'T' + S[pre_pos + pos + 2:]
            temp_s = temp_s[pos + 2:]
            pre_pos = pre_pos + pos + 2
        else:
            if S[pre_pos + pos - 1] == '-':  # exclude the house has tank
                if pre_pos + pos == len(S) - 1 or pre_pos + pos + 1 == len(S) - 1:
                    S = S[:pre_pos + pos - 1] + 'T' + S[pre_pos + pos:]
                    break
                else:
                    if S[pre_pos + pos + 1] == '-':
                        S = S[:pre_pos + pos + 1] + 'T' + S[pre_pos + pos + 2:]
            temp_s = temp_s[pos + 1:]
            pre_pos = pre_pos + pos + 1

    # Finally, remove any excess tank
    pre_pos = 0
    temp_s = S
    while 1:
        pos = temp_s.find("HTHTHTH")
        if pos == -1:
            break
        S = S[:pre_pos + pos + 3] + '-' + S[pre_pos + pos + 4:]
        temp_s = temp_s[pos + 7:]
        pre_pos = pre_pos + pos + 7

    return S


if __name__ == "__main__":
    S = "H--H-H--HH-H-H-H-H-H-H-HH-HH--H-HH-H---------H"
    # S = "H-H-H-HH-H-H-HH-H"
    print(solution(S))
