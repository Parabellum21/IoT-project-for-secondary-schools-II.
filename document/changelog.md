# Change Log
All notable changes to this project will be documented in this file.

## [2022.1] - 2021-10-04
- consultant definition is now optional

## [2021.3] - 2021-09-29
- specification of the bibliography file removed from the class and added to the thesis.tex

## [2021.2] - 2021-03-23
- full support for English documents
- `readme.md` translated to English

## [2021.1] - 2021-02-08
- znovu zapnuté farebné ramčeky okolo odkazov
- pridaný súbor latexmkrc s konfiguráciou automatického generovania slovníkov (#10)

## [2020.1] - 2020-09-25
- zrušený analytický list a nahradený len abstraktom a kľúčovými slovami
- pozmenené rozloženie strany
- vrátené numerické označovanie literatúry
- zadávanie mena autora v tvare `\author[titul]{Meno}{Priezvisko}[titul]`
- pridaná bibliografická citácia práce na konci strany s abstraktom
- použitie balíka `listings` pre fragmenty kódu namiesto `minted`, ktorý vyžadoval inštaláciu Pythonu
- odstránený neaktualizovaná dokumentácia a šablóna prezentácie
- znovu zlúčené adresáre `dist/` a `thesis/`
- PDF súbor sa neukladá v repozitári, namiesto toho sa generuje pomocou Gitlab-CI
- použitie neproporcionálneho písma `txtt`
- odstránená závislosť na balíku `blindtext`
- zjednodušená štruktúra kapitol a doplnené informácie o ich obsahu
- vypnuté farebné ramčeky okolo odkazov

## [2018.1] - 2018-10-07
- pridaná podpora iso960
- názov kapitoly Literatúra sa dostal do šablóny
- pridaná nová štruktúra práce na základe článku: https://www.scss.tcd.ie/joeran.beel/blog/2010/03/02/how-to-write-a-phd-thesis/
- vytvorený priečinok dist/, kde sa nachádza šablóna

## [2017.7] - 2017-12-19
- opravený problém s odkazom na _Motiváciu_ v obsahu, ktorý ukazoval na nesprávnu stranu
- pridaný zoznam termínov v súbore `glossary.tex`
- pridaný ľahký návod na použitie zoznamu skratiek a termínov priamo v súboroch `glossary.tex` a `acronyms.tex`
- refaktoring
    - výpis literatúry na jeden riadok spolu s položkou v obsahu
    - pre prílohy bol vytvorený samostatný priečinok `appendixes/`

## [2017.6] - 2017-11-22
- do konfigurácie balíka `babel` pridaná konfigurácia pre podporu písania literatúry v iných jazykoch ako slovenských
    - ilustráciou je zdroj napísaný po rusky

## [2017.5] - 2017-05-24
- v prípade, že vytvárate kapitolu bez číslovania, v záhlaví sa zobrazí len jej názov
- popisky (obrázkov, tabuliek) sú aktuálne o niečo menšie, aby boli odlíšiteľné od zvyšného textu
- pridany "magic" root komentar do suborov kapitol
- chyba v slovenskom texte (štúdijný -> študijný)
- zarovnanie cislovania stran vpravo v obsahu od 2. strany
- lepsie zalamovanie linkov v literature


## [2017.4] - 2017-04-25
- akceptovaný merge request od mateja 
    - hlavičky a päty stránok sú orientované vpravo, keďže záverečná práca je tlačená jednostranne a text je na pravej strane 
    - číslovanie stránok je aktuálne v päte a vždy vpravo
    - opravený problém s názvami príloh
- výška stránky sa kvôli číslovaniu zmenšila o 1cm


## [2017.3] - 2017-03-19
- zrušené zvýrazňovanie odkazov v šablóne
    - treba ešte zvážiť ich použitie možno spôsobom draft vs publisher ready verzia dokumentu


## [2017.2] - 2017-03-18
- opravený problém s číslovaním literatúry
    - v súbore thesis.tex došlo k prehodeniu riadkov pri umiestňovaní literatúry kvôli nesprávnej strane v obsahu. z pôvodného 
    ```latex
    \printbibliography[title={Literatúra}]
    \addcontentsline{toc}{chapter}{Literatúra}
    ```
    sa stalo
    ```latex
    \phantomsection
    \addcontentsline{toc}{chapter}{Literatúra}
    \printbibliography[title={Literatúra}]
    ```

## [2017.1] - 2017-01-17
- zrušený balík `parskip`
    - pridaný `\noindent` do čestného vyhlásenia 
    - zrušené odsadzovanie na titulných stranách
- oprava prostredia tabular na titulných stranách
    - na druhej strane už lícuje s okrajom
- vytvorený príkaz `\thesisspec{}` na zadanie cesty k zadaváciemu listu
    - ak nie je použitý, zobrazí sa na príslušnej stránke správa
    - ak je použitý, na príslušnom mieste sa vloží zadávací list
- zvacsena vyska hlavicky dokumentu

## [0.1.0] - 2015-10-19
### Changed
- Názov hlavného súboru bol premenovaný na `thesis.tex`, nakoľko adresuje ako diplomovú, tak aj bakalársku prácu
- Bol opravený problém so starým spôsobom použitia jazykovej verzie

### Added
- Bol pridaný súbor `README.md` so všobecnými informáciami o projekte a jeho používaní
- Bol pridaný súbor `CHANGELOG.md` s informáciami týkajúcimi sa zmien v projekte
