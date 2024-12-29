import unittest

class TestSeleniumScraper(unittest.TestCase):
    def test_return_data(self):
        # Simulação do retorno esperado
        expected_data = [
            [
                "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”",
                "Albert Einstein",
                "https://quotes.toscrape.com/author/Albert-Einstein"
            ],
            [
                "“It is our choices, Harry, that show what we truly are, far more than our abilities.”",
                "J.K. Rowling",
                "https://quotes.toscrape.com/author/J-K-Rowling"
            ],
            [
                "“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”",
                "Albert Einstein",
                "https://quotes.toscrape.com/author/Albert-Einstein"
            ],
            [
                "“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”",
                "Jane Austen",
                "https://quotes.toscrape.com/author/Jane-Austen"
            ],
            [
                "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”",
                "Marilyn Monroe",
                "https://quotes.toscrape.com/author/Marilyn-Monroe"
            ],
            [
                "“Try not to become a man of success. Rather become a man of value.”",
                "Albert Einstein",
                "https://quotes.toscrape.com/author/Albert-Einstein"
            ],
            [
                "“It is better to be hated for what you are than to be loved for what you are not.”",
                "André Gide",
                "https://quotes.toscrape.com/author/Andre-Gide"
            ],
            [
                "“I have not failed. I've just found 10,000 ways that won't work.”",
                "Thomas A. Edison",
                "https://quotes.toscrape.com/author/Thomas-A-Edison"
            ],
            [
                "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”",
                "Eleanor Roosevelt",
                "https://quotes.toscrape.com/author/Eleanor-Roosevelt"
            ],
            [
                "“A day without sunshine is like, you know, night.”",
                "Steve Martin",
                "https://quotes.toscrape.com/author/Steve-Martin"
            ]
        ]

        # Importa a função a ser testada
        import main  # Substitua pelo nome do seu arquivo Python

        # Executa a função e captura o retorno
        actual_data = main.main()

        # Valida se o retorno é igual ao esperado
        self.assertEqual(actual_data, expected_data, "Os dados retornados não correspondem ao esperado.")

if __name__ == "__main__":
    unittest.main()
