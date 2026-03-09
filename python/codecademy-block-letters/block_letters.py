#Røskva Bjørgfinsdóttir
#I like big butts and I cannot lie
firstName = 'RØSKVA'

ascii_art = { 
  'R': [
    'RRRR ',
    'R   R',
    'R   R',
    'RRRR ',
    'R R  ',
    'R  R ',
    'R   R'
  ],
 'Ø': [
  ' ØØØ ',
  'Ø   Ø',
  'Ø  ØØ',
  'Ø Ø Ø',
  'ØØ  Ø',
  'Ø   Ø',
  ' ØØØ '
],
'S': [
  ' SSS ',
  'S   S',
  'S    ',
  ' SSS ',
  '    S',
  'S   S',
  ' SSS '
],
'K': [
  'K   K',
  'K  K ',
  'K K  ',
  'KK   ',
  'K K  ',
  'K  K ',
  'K   K'
],
'V': [
  'V   V',
  'V   V',
  'V   V',
  'V   V',
  'V   V',
  ' V V ',
  '  V  '
],
'A': [
  '  A  ',
  ' A A ',
  'A   A',
  'AAAAA',
  'A   A',
  'A   A',
  'A   A'
],
'B': [
  'BBBB ',
  'B   B',
  'B   B',
  'BBBB ',
  'B   B',
  'B   B',
  'BBBB '
],
'D': [
  'DDDD ',
  'D   D',
  'D   D',
  'D   D',
  'D   D',
  'D   D',
  'DDDD '
],
'E': [
  'EEEEE',
  'E    ',
  'E    ',
  'EEE  ',
  'E    ',
  'E    ',
  'EEEEE'
],
'F': [
  'FFFFF',
  'F    ',
  'F    ',
  'FFF  ',
  'F    ',
  'F    ',
  'F    '
],
'G': [
  ' GGG ',
  'G   G',
  'G    ',
  'GGGGG',
  'G   G',
  'G   G',
  ' GGG '
],
'H': [
  'H   H',
  'H   H',
  'H   H',
  'HHHHH',
  'H   H',
  'H   H',
  'H   H'
],
'I': [
  'IIIII',
  '  I  ',
  '  I  ',
  '  I  ',
  '  I  ',
  '  I  ',
  'IIIII'
],
'J': [
  'JJJJJ',
  '    J',
  '    J',
  '    J',
  'J   J',
  'J   J',
  ' JJJ '
],
'L': [
  'L    ',
  'L    ',
  'L    ',
  'L    ',
  'L    ',
  'L    ',
  'LLLLL'
],
'M': [
  'M   M',
  'MM MM',
  'MM MM',
  'M M M',
  'M   M',
  'M   M',
  'M   M'
],
'N': [
  'N   N',
  'NN  N',
  'N N N',
  'N  NN',
  'N   N',
  'N   N',
  'N   N'
],
'O': [
  ' OOO ',
  'O   O',
  'O   O',
  'O   O',
  'O   O',
  'O   O',
  ' OOO '
],
'Ó': [
  '   Ó ',
  ' ÓÓÓ  ',
  'Ó   Ó',
  'Ó   Ó',
  'Ó   Ó',
  'Ó   Ó',
  ' ÓÓÓ '
],
'P': [
  'PPPP ',
  'P   P',
  'P   P',
  'PPPP ',
  'P    ',
  'P    ',
  'P    '
],
'Q': [
  ' QQQ ',
  'Q   Q',
  'Q   Q',
  'Q   Q',
  'Q   Q',
  'Q  Q',
  ' QQ Q'
],
'T': [
  'TTTTT',
  '  T  ',
  '  T  ',
  '  T  ',
  '  T  ',
  '  T  ',
  '  T  '
],
'U': [
  'U   U',
  'U   U',
  'U   U',
  'U   U',
  'U   U',
  'U   U',
  ' UUU '
],
'W': [
  'W   W',
  'W   W',
  'W   W',
  'W W W',
  'WW WW',
  'WW WW',
  'W   W'
],
'C': [
  ' CCC ',
  'C   C',
  'C    ',
  'C    ',
  'C    ',
  'C   C',
  ' CCC '
],
'X': [
  'X   X',
  'X   X',
  ' X X ',
  '  X  ',
  ' X X ',
  'X   X',
  'X   X'
],
'Y': [
  'Y  Y',
  ' Y Y ',
  '  Y  ',
  '  Y  ',
  '  Y  ',
  '  Y  ',
  '  Y  '
],
'Z': [
  'ZZZZZ',
  '    Z',
  '   Z ',
  '  Z  ',
  ' Z   ',
  'Z    ',
  'ZZZZZ'
]
}

for char in firstName:
    if char in ascii_art:
        for line in ascii_art[char]:
            print(line)
    else:
        print(f"Character '{char}' not found in ASCII art dictionary")
    print()
