from dataclasses import dataclass

@dataclass
class SyllableSeparator:
  def separate(self, word: str) -> list[str]:
    """
    Separates a word into syllables.
    
    Args:
        word (str): The word to separate.
        
    Returns:
        list[str]: A list of syllables.
    """
    # This is a placeholder implementation. Replace with actual logic.
    vowels = "aeiouáéíóú"
    syllables = []
    i= 0
    while i < len(word):        
        if word[i] == 'c' and i + 1 < len(word) and word[i + 1] == 'h':
            syllables.append(word[i:i+3])
            i += 3
        elif word[i] == 'l' and i + 1 < len(word) and word[i + 1] == 'l':
            syllables.append(word[i:i+3])
            i += 3
        elif word[i] == 'r' and i + 1 < len(word) and word[i + 1] == 'r':
            syllables.append(word[i:i+3])
            i += 3
        else:
            if len(word)-i < i + 3:
                if word[i + 3] not in vowels:
                    syllables.append(word[i:i+3])
                    i += 3
            else:
                syllables.append(word[i:i+2])
                i += 2

    return syllables