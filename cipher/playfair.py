import re

class PlayfairCipher:
    def __init__(self):
        pass

    def _generate_key_matrix(self, key):
        key = key.upper().replace("J", "I")
        key = re.sub(r'[^A-Z]', '', key)
        matrix = []
        seen = set()
        for char in key:
            if char not in seen:
                matrix.append(char)
                seen.add(char)
        for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if char not in seen:
                matrix.append(char)
                seen.add(char)
        return [matrix[i:i+5] for i in range(0, 25, 5)]

    def _find_position(self, matrix, char):
        for r, row in enumerate(matrix):
            if char in row:
                return r, row.index(char)
        return None

    def _prepare_text(self, text):
        text = text.upper().replace("J", "I")
        text = re.sub(r'[^A-Z]', '', text)
        prepared = ""
        i = 0
        while i < len(text):
            prepared += text[i]
            if i + 1 < len(text) and text[i] == text[i+1]:
                prepared += "X"
                i += 1
            elif i + 1 < len(text):
                prepared += text[i+1]
                i += 2
            else:
                prepared += "X"
                i += 1
        return prepared

    def encrypt(self, text, key):
        matrix = self._generate_key_matrix(key)
        prepared_text = self._prepare_text(text)
        result = ""
        for i in range(0, len(prepared_text), 2):
            char1, char2 = prepared_text[i], prepared_text[i+1]
            r1, c1 = self._find_position(matrix, char1)
            r2, c2 = self._find_position(matrix, char2)
            if r1 == r2:
                result += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
            elif c1 == c2:
                result += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
            else:
                result += matrix[r1][c2] + matrix[r2][c1]
        return result

    def decrypt(self, text, key):
        matrix = self._generate_key_matrix(key)
        result = ""
        for i in range(0, len(text), 2):
            char1, char2 = text[i], text[i+1]
            r1, c1 = self._find_position(matrix, char1)
            r2, c2 = self._find_position(matrix, char2)
            if r1 == r2:
                result += matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
            elif c1 == c2:
                result += matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
            else:
                result += matrix[r1][c2] + matrix[r2][c1]
        return result
