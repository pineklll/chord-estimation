# 12 root classes * 14 pitch classes + N(none) + X(unknown) = 170
pitchClass = ['7', 'min', 'maj', 'dim', 'aug', 'min6', 'maj6', 'min7', 'maj7', 'minmaj7', 'dim7', 'hdim7', 'sus2', 'sus4']
rootClass = ['A', 'Ab', 'B', 'Bb', 'C', 'C#', 'D', 'D#', 'Db', 'E', 'Eb', 'F', 'F#', 'G', 'G#', 'Gb', 'N']

def pitchClassExtract(chordStr):
    root = 'N'; pitch = 'X'

    if len(chordStr) == 1:
        root = chordStr
    elif chordStr[1] == 'b' or chordStr[1] == '#':
        root = chordStr[:2]
    else:
        root = chordStr[0]
    if chordStr[0] == 'N':
        root = 'N'

    # 七和弦
    if ':7' in chordStr:
        pitch = '7'
    for pitchEle in pitchClass[1:][::-1]:
        if pitchEle in chordStr:
            pitch = pitchEle
            break

    return root , pitch

def test_pitchClassExtract():
    with open('chord.txt') as chord:
        for line in chord:
            root, pitch = pitchClassExtract(line)
            print(root, pitch)