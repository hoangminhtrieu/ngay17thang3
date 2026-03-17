import math

class TranspositionCipher:
    def encrypt(self, text, key):
        key = str(key)
        n = len(key)
        m = len(text)
        num_rows = math.ceil(m / n)
        grid = [['' for _ in range(n)] for _ in range(num_rows)]
        
        for i in range(m):
            grid[i // n][i % n] = text[i]
            
        key_order = sorted(range(n), key=lambda k: key[k])
        result = ""
        for col in key_order:
            for row in range(num_rows):
                result += grid[row][col]
        return result

    def decrypt(self, cipher, key):
        key = str(key)
        n = len(key)
        m = len(cipher)
        num_rows = math.ceil(m / n)
        
        # Calculate number of characters in each column
        col_lengths = [num_rows] * n
        num_short_cols = (num_rows * n) - m
        
        key_order = sorted(range(n), key=lambda k: key[k])
        
        # Mark short columns (at the end of the last row)
        short_col_indices = set(range(n - num_short_cols, n))
        for idx in short_col_indices:
            col_lengths[idx] -= 1
            
        grid = [['' for _ in range(n)] for _ in range(num_rows)]
        current_idx = 0
        for col in key_order:
            length = col_lengths[col]
            for row in range(length):
                grid[row][col] = cipher[current_idx]
                current_idx += 1
                
        result = ""
        for row in range(num_rows):
            for col in range(n):
                if grid[row][col]:
                    result += grid[row][col]
        return result
