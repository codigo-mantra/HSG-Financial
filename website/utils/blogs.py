import math
import re
from django.utils.html import strip_tags

WORDS_PER_MINUTE = 200

def get_reading_time(html_content):
    text = strip_tags(html_content)
    word_count = len(re.findall(r'\w+', text))
    minutes = math.ceil(word_count / WORDS_PER_MINUTE)
    return max(1, minutes)
