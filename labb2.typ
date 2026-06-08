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
Skapa en funktion som estimerar en satellits omloppstid baserat på dess höjd från jordytan. Jordens radie är $R_plus.o = 6 371 "km"$. Gör sedan ett program som med denna funktion beräknar omloppstiden för exakt 6 satelliter som användare en och en matar in.

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
