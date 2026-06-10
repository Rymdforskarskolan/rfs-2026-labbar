#import "preamble.typ": *
#import "@preview/meander:0.4.2"
#show: template.with(logo: "./RFS-two-no-wisps.png", title: [Labb 2 --- Funktioner, upprepningsbar kod och klasser])

Välkomna till labb 2! Nu hoppas jag att ni har ett litet hum om hur kod framställs. Vid det här laget så sätter er fantasi gränserna. Vi har i rekordfart lyckats gå igenom alla byggstenar som krävs för att förstå 90% av all kod någonsin skriven, så känn dig stolt om du hängt med!

I denna labb kommer vi att ha mer invecklade och avancerade uppgifter som sätter din problemlösningsförmåga på prov. Samma upplägg som förra gången gäller: ni låser upp varje facit med svaret på _facitfrågan_. Lycka till!

En påminnelse om hur man låser upp facit (alla kommandon i samma mapp som facit):

```
> ./decrypt.py <namn-på-facit>
Ange krypteringsnyckeln: <er-kryptonyckel>
```

För att testa dekrypteringen har vi skickat med ett testfacit i filen `facit-test.enc`, med nyckeln "hej". Kör avkodaren på detta facit för att se att allt funkar:
```
> ./decrypt.py facit-test.enc
Ange krypteringsnyckeln: hej
```

För er som eventuellt använder Windows på egen dator, krävs att ni skriver följande i en terminal:
```
> pip install cryptography click
*vänta tills det är klart, sen*

> python decrypt.py facit-test.enc
Ange krypteringsnyckeln: hej
```

== En not om slumpning
#counter(heading).update(1)
I vissa uppgifter kan det vara användbart för dig att kunna slumpa saker. Då kan du importera biblioteket `random` precis som vi gjorde med `math`. Då kan du anropa `random.randint(start, stop)` och `random.randrange(start, stop)` för att få `int` resp. `float` slumpmässigt på ett givet intervall. Du kan också använda `random.choice(collection)` för att få ett slumpmässigt värde ur en ordnad kollektion.

Exempel
```py
import random

random_integer = random.randint(0, 15)
random_float = random.randrange(1.3, 4.7)

my_list = [1, 3, 5]
random_element = random.choice(my_list)
```


== Nivå 1

=== Raketbränsle
Skriv en funktion som beräknar hur mycket bränsle som krävs för en raket baserat på lastens massa. Formeln är
$
  V_"bränsle" = 1.5 m + 500,
$
och ger bränslevolym i m#super[3] för en massa $m$ i kg. Programmet skall sedan, m.h.a. denna funktion, fråga efter en massa och skriva ut resulterande bränsleåtgång med enhet.

=== Ljusårsräknaren
#meander.reflow({
  import meander: *
  placed(right, table(
    columns: 2,
    table.header([*Planet*], [*Avstånd (ly)*]),
    [40 Eridani A b], [16,3],
    [Proxima Centauri b], [4,2],
    [Barnard's Star b], [6,0],
    [Ross 128 b], [11,0],
    [Luyten b], [12,4],
  ))
  container()
  content[
    Skriv en funktion som kan konvertera ljusår till km.
    $
      1 "ly" = 9.461 dot 10^(12) "km".
    $
    Ditt program skall sedan beräkna avstånd i km för samtliga exoplaneter till höger och skriva ut deras avstånd i _bägge_ enheter till terminalen.
  ]
})

=== Astronautträning

Skriv en klass, `Astronaut`, som lagrar en astronauts träningsinfo. Varje astronaut skall ha ett betyg från 0--100 som bedömer hur "redo" de är. En astronaut med mer än 90 i betyg anses vara redo. Klassen skall därför ha en metod som returnar vare sig astronauten är redo eller ej beroende på dess betyg.

=== Satellitomlopp
Skapa en funktion som estimerar en satellits omloppstid baserat på dess höjd från jordytan. Jordens radie är $R_plus.o = 6 371 "km"$. Jordens massa är $M_plus.o = 5.9722 dot 10^24$. Allmänna gravitationskonstanten är $G approx 6.6743 dot 10^(-11)$. Det gäller att
$
  a_g = G M_plus.o / r^2
$
där $r$ är avstånd från jordens mitt.

Gör sedan ett program som med denna funktion beräknar omloppstiden för exakt 6 satelliter som användare en och en matar in.

=== Rymdskepsskölden
Du är en utvecklar för NASA:s nya interstellära rymdskepp som skall ha sprillans nya energisköldar. De vill ha en terminal där de kan följa sköldens energinivå. Programmet skall ad infinitum fråga användare hur många procent som skölden laddats eller skadats och uppdatera laddningen. Den för aldrig under- eller överskriva 0% resp 100%.

=== Multiplikationstabellen
Skriv ett program som printar multiplikationstabellen (1-10) för vilket tal som helst.

=== Ordmultiplikatorn
Skriv en funktions som tar ett ord och ett antal som argument sedan returnerar en sträng med ordet upprepat det antalet gånger. Skriv sedan ett program som läser in ett ord sedan ett antal för att därefter printa resultatet av funktionen.

=== $Delta v$ kartan --- Facitfråga
#meander.reflow({
  import meander: *
  placed(right, table(
    columns: 2,
    table.header([*Destination*], [$Delta v$]),
    [Månen], [15070 m/s],
    [Merkurius], [25540 m/s],
    [Venus], [43190 m/s],
    [Mars], [18910 m/s],
    [Neptunus], [43750 m/s],
    [Uranus], [42013 m/s],
    [Saturnus], [57340 m/s],
    [Jupiter], [78170 m/s],
  ))
  container()
  content[
    Raketers förmåga att ändra sin hastighet mäter vi i $Delta v$, hur många m/s som raketen kan ändra sin hastighet. Skriv ett program som låter en användare ange ett antal destinationer som de vill åka till och programmet skriver sen total $Delta v$ som krävs för detta. Detta motsvarar att summera $Delta v$ för varje angivet element.

    För facit: Beräkna $Delta v$ för att åka till Månen, Merkurius och Neptunus med programmet. Resultatet utan enhet är din nyckel.
    // Svar: 84360
  ]
})

== Nivå 2

=== Syreförbrukning
En astronauts bränsletank förbrukar 16% syre per minut. Skriv ett program som simulerar detta förlopp. Den skall varannan sekund skriva ut syret kvar i tanken.

*Ledning:* du kan importera `time`, likt `math`, och använda metoden `time.time()` för att erhålla antal sekunder sedan 1 jan 1970, 00:00 UTC. Detta lämpar ju sig till en slinga...

=== Raketbränsle 2
Skriv en funktion som beräknar hur mycket bränsle som krävs för en raket baserat på lastens massa. Formeln är
$
  V_"bränsle" = 1.5 m + 500,
$
och ger bränslevolym i m#super[3] för en massa $m$ i kg. Programmet skall sedan, m.h.a. denna funktion, fråga efter ett godtyckligt antal laster och när användaren skriver "klar" rapportera sammanlagd bränsleförbrukning samt förbrukning för varje last där det framgår vilket nummer varje last har.

=== Rymdkolonin

Skapa en klass `Colony` som har attribut för ett namn på kolonin, populationen och tillväxthastigheten per år av populationen. Skriv en loop som simulerar 3 olika kolonier över tre år och printa sedan deras slutgiltiga population.

=== Avkodaren
<aliens>
Vi har tagit emot chiffrerade meddelanden från utomjordingar! Våra forskare har insett att de använder ett Ceasarchiffer med ett skifte på +3. Skiljetecken lämnas oförändrade. De behöver att du skriver ett program som kan avkoda dessa medellanden i storvolym. Vid varje körning av programmet skall användaren frågas om ett kodat medellande och avkodade svaret skall returneras. Testa ert program genom att avkoda följande medellanden:
#table(
  columns: (1fr, 1fr),
  [yl nrpphu wd hud nrvvru icu yhwhqvndsoljd håshulphqw!], [mrughqv nrpphu dww iculqwdv dy rvv, edud ybqwd!],
  [kdk, ql ndq vbnhuw lqwh hqv obvd ghvvd! pbqqlvnru bu va gxppd.],
  [qbu yl wdjlw hud nru, va nrpphu yl dww wd hud iau qbvw. vhq näfnoljdu. vhq julvdu, rfk va ylgduh.],
)

=== Fibonacci

Skriv en funktion som räknar ut $N$ Fibonaccital utan rekursion. Räkna ut det 256:e Fibonaccitalet.

=== Primtalsfyndet

Skriv en funktion som kollar ifall ett tal är ett primtal. Använd den för att hitta alla primtal mellan 2 och 50.

=== Palindrom

Skriv en funktion som kollar ifall ett ord är ett palindrom. Det vill säga, om ordet stavas likadant bak-och-fram som det gör åt rätt håll. Ett exempel på palindrom är "Racecar".

=== Krypteringen --- Facitfråga

Utomjordingarna från @aliens visade sig vara taskiga. Vi vill därför kunna skicka taskiga medellanden tillbaka. Skriv en funktion som kodar ett medellande som användaren kan ange. Använd samma +3 Ceasarchiffer som i @aliens. Koda sedan följande medellande.

#table(
  columns: (1fr, 1fr),
  [Ni kommer absolut inte vinna, människor är starka!], [Våra kossor är inte för ert vetenskapliga bruk!],
  [Vi kan absolut läsa det ni skriver, och vi skriver till med tillbaka!],
  [Vi förstår inte er fixering på boskap, men vi kommer inte att låta er ta dem.],
)

För att låsa upp facit: Koda medellandet ned till höger. De första 25 bokstäverna från det krypterade medellandet, med endast små bokstäver utan skiljetecken och mellanslag, är er nyckel.
// Svar: ylicuvwaulqwhhuilåhulqjsa

== Nivå 3

=== Rymdkoloni 2: Electric boogaloo

Det är ju väldigt tjusigt att kunna hålla koll på population, men du som sitter i styrelsen vill ju kunna hålla koll på varje individuell kolonist. Skriv en till klass `Colonist` och utöka klassen `Colony` för att kunna lagra en kollektion av kolonister där du med hjälp av en metod `Colony.get_colonist(name)` kan hämta en kolonist via namn. Du ska även kunna ta bort och lägga till kolonister med `Colony.add_colonist(name)` och `Colony.remove_colonist(name)`.

*Bonus:* Gör så att man håller koll på ålder och yrke för varje kolonist. Varje kolonist skall ha en metod `Colonist.birthday()` som printar en festlig hälsning och ökar deras ålder med 1.


=== Asteroidnavigation --- Mycket svår

Skapa en klass `AsteroidField` som representerar ett 10x10 rutnät av ett asteroidfält. Varje cell kan vara en asteroid eller inte. Ett rymdskepp skall kunna börja någonstans på vänstra kanten och ta sig till högra kanten. Koden skall klara samtliga startpositioner. Asteroidfältet får vara samma varje gång eller slumpat. Skeppet får inte lämna området uppåt eller nedåt. Skeppet skall röra sig en kolumn i taget och undvika asteroider.

Det skall finnas åtminstone en metod `AsteroidField.is_asteroid_in_front(x, y)` som berättar ifall du kommer krocka i nästa steg. Det kan krävas fler metoder för att lösa uppgiften. Skeppet kan i sådana fall röra sig sidled, men _aldrig_ till `y < 0` eller `y > 9` med övre vänstra hörnet i (0, 0).

Rymdskeppet skall representeras av klassen `SpaceShip` och denna skall ha en metod `SpaceShip.navigate(asteroid_field, start_row)` som utför denna navigering. Metod skall även printa vägen skeppet har tagit till terminalen när den är klar. Skeppets rutt visas med `X` för varje cell passerad. Asteroider visas med `O`. Ett exempel (parenteser ej obligatoriska):

```stdout
[ ] [ ] [ ] [X] [X] [X] [O] [X] [X] [x]
[ ] [X] [X] [X] [O] [X] [X] [X] [O] [ ]
[X] [X] [O] [ ] [ ] [O] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [O] [ ]
[ ] [ ] [ ] [O] [ ] [ ] [O] [ ] [ ] [ ]
[ ] [ ] [O] [ ] [ ] [O] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [O] [ ] [ ] [ ] [ ] [O] [ ]
[ ] [O] [ ] [ ] [ ] [ ] [O] [ ] [ ] [ ]
[ ] [ ] [ ] [O] [ ] [O] [ ] [ ] [ ] [ ]
[ ] [O] [ ] [ ] [O] [ ] [ ] [O] [ ] [ ]
```

=== Sifferpar

Skriv en funktion som tar en lista med tal och hittar alla par vars summa uppgår till ett visst antal givet som argument. Testa att hitta alla par som adderar till 12 i listan `[6, 6, 7, 1, 10, 2, 5, 8, 9, 3, 14, 67]`.

*Bonus:* Kan du göra detta med hjälp av biblioteket `itertools` för att iterera över alla kombinationer? Läs på själv om hur `itertools` fungerar.

=== Sten, sax, påse

Skriv en klass `RockPaperScissorsPlay` som representerar ett drag i en match Sten, sax, påse. Klassen ska ha en konstruktor som låter dig uttryckligen välja drag och en metod `RockPaperScissorsPlay.random()` som skapar en ny slumpmässig instans. Du skall sedan skriva ett program som låter användaren spela en bäst-av-3-match mot slumpen genom att skriva sitt drag i terminalen varje gång.

*Bonus:* Kan du skriva en klass `RockPaperScissorsGame` som har en metod `RockPaperScissorsGame.run_game()` som hanterar hela spelets gång.

=== Tidhantering

Skriv en class `Time` som låter en lagra en tid i timmar, minuter och sekunder. Det skall finnas metoder för att printa, addera och subtrahera tider. Det skall även gå att jämföra två tider ifall de är större, mindre eller lika.

*Bonus:* Kan du skriva en till klass: `DateTime` som lagrar ett objekt av `Time` och ett objekt av ytterligare en klass: `Date`? Samma operationer gäller, men nu skall även dagar vara inblandade.

*Bonus2:* Kan du implementera de så kallade _dundermetoderna_ `__add__()`, `__sub__()`, `__gt__()`, `__lt__()`, `__le__()`, `__ge__()`, `__eq__()` och `__neq__()` för antingen alla tre klasser eller bara klassen `Time`? Läs på själv om vad dessa är.

=== Anomalidetektorn

Skriv en funktion som upptäcker anomalier i sensordata. En bit sensordata är ett 5x5 rutnät av `float`s där en anomali är ett sådan värde som är minst 1.5 ggr större än _någon_ av dess grannar. Programmet skall sedan rapportera hur många anomalier som upptäcktes och vart de ligger i rutnätet.

Ett exempel:

```
[ 12.5 ] [ 8.7 ] [ 12.4 ] [  4.5 ] [ 12.9 ]
[  9.1 ] [ 7.2 ] [  5.2 ] [  3.5 ] [ 15.3 ]
[ 10.2 ] [ 5.7 ] [  4.0 ] [ 17.3 ] [  9.4 ]
[ 11.3 ] [ 2.1 ] [  1.3 ] [  8.9 ] [ 10.6 ]
[ 13.8 ] [ 3.4 ] [  9.2 ] [ 22.5 ] [ 13.3 ]
```

där anomalierna är `(0, 2): 12.4, (0, 4): 12.9, (1, 4): 15.3, (2, 0): 10.2, (2, 1): 5.7, (2, 2): 4.0, (2, 3): 17.3, (3, 0): 11.3, (3, 1): 2.1, (3, 3): 8.9, (4, 0): 13.8, (4, 1): 3.4, (4, 2): 9.2, (4, 3): 22.5`

=== Rymdstationen

Gör en klass som heter `SpaceStation` som representerar en modulär rymdstation. Gör även en klass som heter `SpaceStationModule` som representerar en sådan modul. Varje modul skall hålla koll på dess besättningskapacitet, namn och elförbrukning.

Den gemensamma rymdstationsklassen skall ha metoder för att lägga till och ta bort moduler samt en metod som sammanfattar besättningskapacitet och elförbrukning på terminalen.

=== Strängkompression --- Facitfråga

*Del A:* När man komprimerar data så spar man ofta plats på att eliminera upprepningar. Skriv en funktion som komprimerar en sträng genom att ersätta upprepade karaktärer med karaktären och dess antal. Några exempel: `"aaaaabb" -> "a3b2"`, `"Hello, there" -> "Hel2o there"`, osv. Testa att komprimera "Jag är sååååå taggad på att träffa alla!".

*Del B:* Skriv en motsvarande funktion som åter inflaterar det komprimerade värdet. Notera att strängen endast kan bestå av bokstäver med detta system.

För facit: inflatera strängen "b3c7h8astronomio9" och resultatet är din nyckel.
// Svar: bbbccccccchhhhhhhhastronomiooooooooo
