import csv
import os
from datetime import datetime

from selenium.webdriver.common.by import By

class Extractor:
    def __init__ (self, driver):
        self.driver = driver

    def extractor_site(self):
        data = []

        # Localiza todas as citações na página inicial
        quotes = self.driver.find_elements(By.CLASS_NAME, "quote")

        for quote in quotes:
            # Extrai o texto da citação, autor e o link para o autor
            text = quote.find_element(By.CLASS_NAME, "text").text.strip()
            author = quote.find_element(By.CLASS_NAME, "author").text.strip()
            author_link = quote.find_element(By.TAG_NAME, "a").get_attribute("href").strip()

            # Adiciona as informações à lista de dados
            data.append([text, author, author_link])

        #print(data)

        # Cria a pasta collectDados, se não existir
        output_dir = "CollectDados"
        os.makedirs(output_dir, exist_ok=True)

        # Gera o nome do arquivo com a data e hora atual
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_file = os.path.join(output_dir, f"extracted_data_{timestamp}.csv")

        # Salva os dados extraídos em um novo arquivo CSV
        with open(output_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Quote", "Author", "Author Link"])  # Cabeçalho
            writer.writerows(data)  # Escreve os dados

        print(f"Dados extraídos e salvos em '{output_file}'.")

        print(data)

        return data