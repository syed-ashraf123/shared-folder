#python-Levenshtein
from fuzzywuzzy import fuzz
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


ratio=fuzz.ratio("New York","N York")
print(ratio)
