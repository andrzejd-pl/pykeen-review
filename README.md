# PyKEEN - review

## Sposób użycia
Projekt ten skupia się na analizie biblioteki PyKEEN, a wnioski, wraz z przykładowym kodem znajdują się w dokumencie 
"ZTI-PyKEEN-analiza narzędzia".

## Użyte metody
Metody użyte w dokumencie pochodzą z dokumentacji biblioteki PyKEEN gdzie można znaleźć dokładniejsze ich opisanie.
[Link](https://pykeen.readthedocs.io/en/latest/)

### Najważniejsze metody:
* `train_model` - metoda, która pobiera konfigurację z pliku, do którego podajemy ścieżkę, a następnie na jej podstawie
 trenuje model oraz zwraca wyniki po wytrenowaniu modelu
* `print_results` - metoda, która zwraca nam zagregowane podsumowanie wyników treningu modelu
* `visualize_loss_function` - metoda, która wizualizuje na grafie funkcję straty
* `start_predictions_pipeline` - metoda, która przyjmuje jako argumenty pliki z interesującymi nas encjami i relacjami,
a następnie, na ich podstawie, oblicza permutacje połączeń i szacuje ich wiarygodność.