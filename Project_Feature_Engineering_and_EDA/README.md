# 📊 Analiza danych środowiskowych ESA

## 📚 Spis treści

1. [Zapoznanie z biblioteką Seaborn](#1-zapoznanie-z-biblioteką-seaborn)
2. [Charakterystyka portalu Dane.gov.pl](#2-charakterystyka-portalu-danegovpl)
3. [Wybór zestawu danych](#3-wybór-zestawu-danych)
4. [Etapy pipeline’u ML](#4-etapy-pipelineu-ml)
5. [Podsumowanie](#5-podsumowanie)
6. [Licencja danych](#6-licencja-danych)

---

## 1. Zapoznanie z biblioteką Seaborn

**Seaborn** to wysokopoziomowa biblioteka do tworzenia statystycznych wizualizacji danych, oparta na **Matplotlib**.  
Umożliwia szybkie tworzenie estetycznych wykresów i wspiera eksploracyjną analizę danych dzięki intuicyjnemu API.

---

## 2. Charakterystyka portalu Dane.gov.pl

**Dane.gov.pl** to centralne repozytorium danych publicznych w Polsce.  
Dane udostępniane są m.in. przez **GUS**, **Ministerstwo Finansów**, **CEIDG** – w formatach CSV, XLS(X), JSON oraz przez API (REST, SOAP, GraphQL).

Zakres tematyczny obejmuje: **środowisko, transport, edukację, zdrowie, gospodarkę** i wiele innych.

---

## 3. Wybór zestawu danych

### 3.1 Opis zbioru

Zbiór: **„Dane pomiarowe ESA (Edukacyjna Sieć Antysmogowa)”**  
Dane środowiskowe rejestrowane przy placówkach edukacyjnych – z częstotliwością co 15 minut.

### 3.2 Powody wyboru

- Zmienność czasowo-przestrzenna
- Znaczenie tematyki (zdrowie publiczne)
- Możliwość zastosowania EDA + ML

---

## 4. Etapy pipeline’u ML

- Wczytanie i łączenie danych z 24 plików CSV (z dnia 28.04.2025)
- Analiza braków danych i ich imputacja
- Rozdzielenie znaczników czasu
- Wizualizacja rozkładów i wartości odstających
- Mapy i heatmapy
- Budowa modelu predykcyjnego (np. regresja)

---

## 5. Podsumowanie

- Projekt pokazuje zastosowanie **EDA** i **Feature Engineeringu** w analizie jakości powietrza
- Wykorzystano: `pandas`, `seaborn`, `matplotlib`, `plotly`, `sklearn`
- Kluczowa zmienna docelowa: **PM10_AVG**
- Projekt może być podstawą dla **modeli predykcyjnych i systemów ostrzegania smogowego**

---

## 6. Licencja danych

Dane wykorzystane w projekcie pochodzą z portalu **[dane.gov.pl](https://dane.gov.pl/)**  
i zostały udostępnione na licencji:

**[CC0 1.0 Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/legalcode.pl)**

> Brak praw autorskich.  
> Można swobodnie kopiować, zmieniać, rozpowszechniać i wykorzystywać dane, nawet w celach komercyjnych – bez pytania o zgodę.

---


🛠 Autor: Dominik Sakłaski📅 Data: 2025-05-08📘 Język: Python (Pandas, Seaborn, Plotly, Scikit-learn)

