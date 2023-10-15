## Installationsprocess för de olika teknikerna och program som används för projektet.


Installation av Visual Studio Code
1. Sök efter ’vscode’ eller ’visual studio code’.
2. Klicka på ’Download’ eller ’Ladda ner’ beroende på språk.
3. Välj sen installation utefter operativsystem och följ installationsprocessen.

---------------------------------------------------------------------------------------------------------------------


Installation av Python, pip och Flask (För Linux och Windows)

Linux | Python
1. Öppna terminal (Ctrl + Alt + T)
2. Skriv ’sudo apt install python3’

Linux | pip
1. Öppna terminal (Ctrl + Alt + T)
2. Skriv ’sudo apt install python3-pip’

Linux | Flask
1. Öppna terminal (Ctrl + Alt + T)
2. Skriv ’pip install Flask’

Sett upp Flask i vscode terminalen
1. För att kunna köra virtual environmenten behöver vi även installera venv. Skriv ’sudo apt install python3.10-venv’ i terminalen.
2. Sett upp flask app och environment med:
    set FLASK_APP=[projektnamn]
    set FLASK_ENV=development
    source venv/bin/activate
3. Starta dev servern med 'flask run --debug'
    
    EXTRA: Om du behöver installera ett python package:
    Klicka Ctrl + C för att stänga flask servern.
    Skriv deactivate för att ta dig ur venv, annars hamnar det i venv miljön, sen gå tillbaka in i miljön igen med 'source [projektnamn]/bin/activate'
    
Linux | Bootstrap
1. Öppna terminal (Ctrl + Alt + T)
2. Skriv 'sudo apt-get install npm'
3. Skriv sedan 'npm install bootstrap'

---------------------------------------------------------------------------------------------------------------------

Windows | Python
1. Öppna Microsoft Store
2. Sök efter ’Python3’
3. Installera paketet/appen

Windows | pip
1. Öppna terminal (Win + R, skriv cmd, enter)
2. Skriv ’python get-pip.py’

Windows | Flask
1. Öppna terminal (Win + R, skriv cmd, enter)
2. Skriv ’pip install Flask’

Sett upp Flask i vscode terminalen
1. För att kunna köra virtual environmenten behöver vi även installera venv. Skriv ’pip install virtualenv’ i terminalen.
2. Sett upp flask app och environment med:
    set FLASK_APP=[projektnamn]
    set FLASK_ENV=development
    $env:FLASK_APP=[projektnamn]
    [projektnamn]/Scripts/activate
3. Starta dev servern med 'flask run --debug'
    
    EXTRA: Om du behöver installera ett python package:
    Klicka Ctrl + C för att stänga flask servern.
    Skriv deactivate för att ta dig ur venv, annars hamnar det i venv miljön, sen gå tillbaka in i miljön igen med '[projektnamn]/Scripts/activate'

Windows | Bootstrap
1. Öppna en webbläsare och sök upp Node.js.
2. Hitta nedladdningen (LTS) och följ installationsprocessen.
3. Öppna sen terminal och skriv 'npm install bootstrap'.

Om npm eventuellt inte funkar för att windows säger att kommandot inte hittas, starta om datorn.

---------------------------------------------------------------------------------------------------------------------

Skapande av projektmapp, initiering av Flask samt länkande till bootstrap
1. Öppna Visual Studio Code.
2. Klicka på ’File’ uppe till vänster, klicka där på ’Open Folder’.
3. Gå dit du vill spara mappen, sen skapa en mapp med valfritt namn,
4. Öppna terminalen i visual studio code, Skriv ’python3 -m venv .venv’.
5. Skapa ’index.html’, 'data.json' och 'style.css' filer
7. För att påbörja index.html filen kan du skriva ! sen tab.
8. Länka sen bootstrap stylesheet till filen inne i head. 

Exempel:
```hmtl
<head>
<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css'>
</head>
```
