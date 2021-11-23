import random
import argparse
import textwrap
import warnings

warnings.filterwarnings("ignore")
from pydub import AudioSegment

parser = argparse.ArgumentParser(description='Build a stream from a string of syllables or n random syllables')
parser.add_argument('--string', type=str, required=False, help='A string of syllables')
parser.add_argument('--random', type=int, required=False, help='Number of random syllables', default=10)
parser.add_argument('--out', type=str, required=True, help='Output file for the stream (.wav)')
parser.add_argument('--spacing', type=int, required=False, help='Syllable spacing in ms', default=0)

args = parser.parse_args()
if args.string:
    syllables = textwrap.wrap(args.string, 2)
else:
    s = ['ha','hy','hä','hö']
    syllables = map(lambda i: s[i], random.choices(range(0,len(s)), k=args.random))

stream = AudioSegment.empty()
for syllable in syllables:
    syllable_audio = AudioSegment.from_wav(f'so_{syllable}.wav')
    stream += syllable_audio + AudioSegment.silent(args.spacing)

stream.export(args.out, format="wav")