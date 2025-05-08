Analiza danych środowiskowych ESA

Spis treści

Zapoznanie z biblioteką Seaborn

Charakterystyka portalu Dane.gov.pl

Wybór zestawu danych

Etapy pipeline’u ML

Podsumowanie

Licencja danych

1. Zapoznanie z biblioteką Seaborn

Seaborn to wysokopoziomowa biblioteka do tworzenia statystycznych wizualizacji danych, oparta na Matplotlib. Umożliwia szybkie tworzenie wykresów i wspiera eksploracyjną analizę danych dzięki intuicyjnemu API.

2. Charakterystyka portalu Dane.gov.pl

Portal Dane.gov.pl to centralne repozytorium danych publicznych w Polsce. Dane udostępniane są m.in. przez GUS, Ministerstwo Finansów czy CEIDG, w formatach CSV, XLS(X), JSON oraz poprzez API (REST, SOAP, GraphQL).

Zbiory obejmują szeroki zakres tematyczny: środowisko, transport, edukacja, zdrowie, gospodarka itp.

3. Wybór zestawu danych

3.1 Opis zbioru

„Dane pomiarowe ESA (Edukacyjna Sieć Antysmogowa)” zawierają środowiskowe dane pomiarowe rejestrowane przy szkołach i przedszkolach, aktualizowane co 15 minut.

3.2 Powody wyboru

Duża częstotliwość pomiarów

Zmienność przestrzenna i czasowa

Możliwość modelowania predykcyjnego

3.3 Znaczenie tematyki

Zanieczyszczenie powietrza ma kluczowe znaczenie dla zdrowia publicznego. Analiza tych danych może wspierać zarządzanie środowiskiem i edukację ekologiczną.

4. Etapy pipeline’u ML

4.1 Wczytanie danych

Wczytano 24 pliki CSV (każdy odpowiadający godzinie 28.04.2025), łącząc je w jeden zbiór (ok. 40 tys. rekordów).

4.2 Analiza brakujących danych

Najwięcej braków dotyczy kolumny STREET (>23%), nieliczne braki pojawiają się też w danych pogodowych. Przeprowadzono klasyfikację typów braków (MNAR, MAR).

4.3 Typy danych i konwersje

Zmienna TIMESTAMP została rozbita na komponenty daty i godziny. Przypisano poprawne typy zmiennym (tekstowe vs numeryczne).

4.4 Inżynieria cech i EDA

Imputacja braków: średnia po mieście lub "nieznana ulica"

Liczba unikalnych etykiet i analiza kardynalności

Statystyki opisowe i rozkłady zmiennych (histogramy, boxploty)

Macierz korelacji i analiza wzorców godzinowych (heatmapy, lineploty)

Mapa stężeń PM10

4.5 Wybór zmiennej docelowej

PM10_AVG – istotna zmienna środowiskowa, z dużą zmiennością i wpływem na zdrowie publiczne.

4.6 Wybór zmiennych wejściowych

Pogodowe: TEMPERATURE_AVG, HUMIDITY_AVG, PRESSURE_AVG

Geograficzne: LATITUDE, LONGITUDE

Czasowe: HOUR

Lokalizacyjne: CITY (po zakodowaniu)

5. Podsumowanie

Projekt umożliwia analizę przestrzenno-czasową jakości powietrza w Polsce z wykorzystaniem EDA i metod uczenia maszynowego. Przygotowane dane są bogate w cechy i wspierają tworzenie modeli predykcyjnych wspierających ochronę zdrowia.

6. Licencja danych

Zbiór danych „Dane pomiarowe ESA (Edukacyjna Sieć Antysmogowa)” pochodzi z portalu dane.gov.pl i udostępniany jest na licencji CC0 1.0 (public domain).

„Brak praw autorskich. Możesz zwielokrotniać, zmieniać, rozpowszechniać i wykonywać utwór, nawet w celu komercyjnym – bez pytania o zgodę.”

Link do licencji: https://creativecommons.org/publicdomain/zero/1.0/legalcode.pl

🛠 Autor: Dominik Sakłaski📅 Data: 2025-05-08📘 Język: Python (Pandas, Seaborn, Plotly, Scikit-learn)

