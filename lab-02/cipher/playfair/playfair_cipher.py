class PlayFairCipher:
    def __init__(self):
        pass

    def create_matrix_key(self, key):
        key = key.upper().replace("J", "I")
        key = "".join(dict.fromkeys(key))

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        matrix = list(key)

        for letter in alphabet:
            if letter not in matrix:
                matrix.append(letter)

        playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix

    def tachcap_plain(self, text):
        text = text.upper().replace("J", "I").replace(" ", "")
        pairs = []
        i = 0

        while i < len(text):
            a = text[i]

            if i + 1 < len(text):
                b = text[i + 1]

                if a == b:
                    pairs.append(a + "X")
                    i += 1
                else:
                    pairs.append(a + b)
                    i += 2
            else:
                pairs.append(a + "X")
                i += 1

        return pairs

    def vitri_letter(self, matrix, letter):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        return None

    def playfair_en(self, plain, key):
        matrix = self.create_matrix_key(key)
        pairs = self.tachcap_plain(plain)
        cipher = ""

        for pair in pairs:
            a, b = pair[0], pair[1]
            row1, col1 = self.vitri_letter(matrix, a)
            row2, col2 = self.vitri_letter(matrix, b)

            if row1 == row2:
                cipher += matrix[row1][(col1 + 1) % 5]
                cipher += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                cipher += matrix[(row1 + 1) % 5][col1]
                cipher += matrix[(row2 + 1) % 5][col2]
            else:
                cipher += matrix[row1][col2]
                cipher += matrix[row2][col1]

        return cipher

    def playfair_de(self, cipher, key):
        matrix = self.create_matrix_key(key)
        cipher = cipher.upper().replace("J", "I").replace(" ", "")
        plain = ""

        for i in range(0, len(cipher), 2):
            a = cipher[i]
            b = cipher[i + 1]
            row1, col1 = self.vitri_letter(matrix, a)
            row2, col2 = self.vitri_letter(matrix, b)

            if row1 == row2:
                plain += matrix[row1][(col1 - 1) % 5]
                plain += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                plain += matrix[(row1 - 1) % 5][col1]
                plain += matrix[(row2 - 1) % 5][col2]
            else:
                plain += matrix[row1][col2]
                plain += matrix[row2][col1]

        banro = ""
        i = 0
        while i < len(plain):
            if i < len(plain) - 2 and plain[i] == plain[i + 2] and plain[i + 1] == "X":
                banro += plain[i]
                i += 2
            else:
                banro += plain[i]
                i += 1

        if banro.endswith("X"):
            banro = banro[:-1]

        return banro