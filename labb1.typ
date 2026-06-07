#import "preamble.typ": *
#import "@preview/meander:0.4.2"
#show: template.with(logo: "./RFS-two-no-wisps.png", title: [Labb 1 --- Grunder])
Välkomna till första labben! Dessa övningar är gjorda för att testa era kunskaper från föreläsningen och ger er en chans att öva.

Det finns ett facit för alla frågor, men tyvärr har HAL krypterat allting! Ni måste lösa _facitfrågan_ i varje nivå för att hitta en krypteringsnyckeln som låser upp facit.

Handledarna har lyckats knäcka krypteringsalgoritmen, men inte nyckeln. Därför har vi levererat ett avkodningsskript med er labbspec. Den kör ni som nedan, i en terminal, i den mapp där facit ligger.
```
> ./decrypt.py <namn-på-facit>
Ange krypteringsnyckeln: <er-kryptonyckel>
```

För att testa era kunskaper så har vi skickat med ett testfacit i filen `facit-test.enc`, med nyckeln "hej". Kör avkodaren på detta facit för att se att allt funkar:
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

=== Miniräknaren
Skriv en enkel miniräknare. Den skall fråga användaren om två tal: `a` och `b`. Därefter skall den summera talen, och skriva ut resultatet.

=== Ålderspådom
Du har vält att bli spåperson. Din tjänst går ut på att förutspå hur gammal någon kommer att vara om 10 år. Skriv ett program som frågar användaren om deras ålder och skriver ut hur gamla de är om 10 år.

=== Udda eller jämnt? <odd-even>
Fråga användaren om ett tal och avgöra om det är jämnt eller udda. Printa resultatet.

*Ledning:* Kom ihåg att modulooperatorn (`%`) ger resten vid division av dess vänstra operand med dess högra operand.

=== Amerikansk termometer
Som alla vet, så är amerikanerna envisa med att ha sina egna enheter. Temperatur är en av de jobbigaste. Skriv ett program som konverterar en temperature given av användare från Celcius till Farenheit enligt formeln
$
  t_(degree"F") = (t_(degree"C") dot 9 / 5) + 32.
$


=== Differensen
En elev på matematiklektionen vill kontrollera en uträkning för hand. Skriv ett program som frågar användaren om två tal, `a` och `b`, och sedan skriver ut differensen `a - b`.

=== Medelvärdet
En lärare vill veta det genomsnittliga resultatet av två delprov. Låt användaren mata in två tal och skriv ut deras medelvärde.

=== Kvadrera talet
För att träna på multiplikation vill man ofta se vad som händer när ett tal multipliceras med sig självt. Fråga efter ett tal och skriv ut dess kvadrat.

=== Namn och hälsning
En enkel välkomstskylt ska visa besökarens namn. Fråga efter ett namn och skriv ut en kort hälsning där namnet förekommer i samma rad. Ett exempel: "Välkommen, Marcell!"

=== Minuter till timmar
En träningsapp visar tiden i minuter, men användaren vill se timmar i decimalform. Fråga efter ett antal minuter och skriv ut hur många timmar det motsvarar.

*Bonus*: Kan du göra så att ditt svar alltid har som mest 2 decimaler?

=== Rabattkalkyl
En butik har en kampanj där alla varor får rabatt i procent. Fråga efter ett pris och en rabatt i procent, och skriv ut det nya priset efter rabatt.

=== Den omvända termometern
I ett amerikanskt väderprogram anges temperaturen i Fahrenheit, men en svensk användare vill se Celsius. Skriv ett program som konverterar temperatur från Fahrenheit till Celsius.

*Ledning*: Kom ihåg formeln från ovan.

=== Bromssträcka --- Facitfråga
Bromsträckan för en bil beräknas
$
  s_b = v_0^2 / (2 a_b)
$
där $s_b$ är bromssträckan i meter, $a_b$ är _beloppet_ av bromsaccelerationen i $"m"slash "s"^2$ och $v_0$ är utgångshastigheten i $"m"slash"s"$. Du behöver skriva en kod som konverterar en hastighet, angiven i $"km"slash"tim"$, till en bromssträcka för en bil.

Ditt program skall fråga efter både utgångshastighet och bromssaceleration separat.

Beräkna bromssträckan med programmet för specifikt en bil med $v_0 = 100 "km"slash"tim"$ och $a_b = 3.2 "m"slash"s"^2$. Avrunda svaret till tre decimaler, det är nyckeln för att låsa upp facit.
// Svaret är : 120.563

*Bonus:* Ändra i koden så att du kan ange bromssacceleration i enheten [g], dvs. multipel av tyngdaccelerationen $g approx 9.81 "m"slash"s"^2$.
#pagebreak(weak: true)

== Nivå 2

=== Betygssystemet
#meander.reflow({
  import meander: *
  placed(top + right, table(
    columns: (auto, auto),
    [*F*], [0],
    [*E*], [10],
    [*D*], [12.5],
    [*C*], [15],
    [*B*], [17.5],
    [*A*], [20],
  ))
  container()
  content[
    Som känt är skalan för betyg i det svenska gymnasiet egentligen numeriskt. Lärare brukar dock sätta betyg som bokstäver. Visst är det jobbigt att försöka komma ihåg siffrorna? Skriv en kod som tar in ett betyg från användaren och gör om det till dess motsvarande siffra. Programmet skriver ut siffran efter betyget.
  ]
})


=== Lösenordscheck
En vanlig grej man måste göra är att kolla lösenord. Ta in ett lösenord från användaren och jämför det med ett förinställt lösenord i koden. Det förinställda lösenordet _måste_ vara lagrat i en konstant variabel. Skriv ut om lösenordet är rätt eller fel.

=== Betygsättning
#meander.reflow({
  import meander: *
  placed(top + right, table(
    columns: (auto, auto),
    [*F*], [\<50],
    [*E*], [50-60],
    [*D*], [60-70],
    [*C*], [70-80],
    [*B*], [80-90],
    [*A*], [90-100],
  ))
  container()
  content[
    Nu är det dags för en tvist på första fråga i detta kapitel! Denna gång skall ni sätta ett betyg baserat på provresultat. Det finns som mest 100 poäng att få, och betygen är fördelade som i tabellen. För varje betyg är undre gränsken _inklusiv_ medan övre gränsen är _exklusiv_. Dvs. att $50 <= x < 60$ för E t.ex. Låt användaren skriva in en poäng mellan 0-100 och skriv ut betyget. Det ska vara åket att ha ej hela poäng och programmet skall klaga om en omöjlig poängsumma har givits.
  ]
})


=== Bibliotekets förseningsavgift
Ett bibliotek tar ut förseningsavgift på återlämnade böcker. För de första 7 försenade dagarna kostar det 2 kr per dag. Därefter kostar varje extra dag 5 kr per dag. Fråga efter hur många dagar en bok är försenad och skriv ut avgiften. Om antalet dagar är negativt skall programmet klaga.

=== Biobiljetten
En biograf har ett enkelt prissystem. Barn under 15 år betalar 90 kr, ungdomar mellan 15 och 18 år betalar 110 kr och alla som är 18 år eller äldre betalar 140 kr. Fråga efter ålder och skriv ut rätt biljettpris. Om åldern är negativ skall programmet klaga.

=== Fraktkostnaden
En nätbutik räknar frakt efter paketets vikt. Om paketet väger högst 2 kg kostar frakten 49 kr. Om det väger mer än 2 kg men högst 5 kg kostar det 79 kr. Tyngre paket kostar 119 kr. Fråga efter vikt i kilogram och skriv ut fraktkostnaden.

=== Träningspasset
En träningsapp vill anpassa sitt pass efter hur många minuter användaren har. Om tiden är kortare än 20 minuter visas ett kort pass. Om tiden är mellan 20 och 45 minuter visas ett normalt pass. Om tiden är längre än 45 minuter visas ett långt pass. Fråga efter antal minuter och skriv ut vilken passkategori som passar bäst.

=== Veckodag med match
En kalenderapp lagrar veckodagar som heltal där måndag är 1 och söndag är 7. Fråga efter ett heltal mellan 1 och 7 och skriv ut rätt veckodag med `match`-satsen. Programmet skall klaga om talet inte är giltigt.

=== Antal dagar i månaden
En resebokning behöver veta hur många dagar som finns i en viss månad. Fråga efter en månad som text och skriv ut hur många dagar månaden har. Februari kan antas ha 28 dagar.

=== Tillåten färg
En fabrik använder bara ett fåtal godkända färger på sina maskiner. Lägg de tillåtna färgerna i en mängd. Fråga efter en färg och skriv ut om den är tillåten eller inte.

=== Välj djur
I ett litet spel finns tre djur som spelaren kan välja mellan. Lägg tre djurnamn i en lista. Fråga efter ett index 0-2 och skriv ut djuret på den platsen. Om indexet är fel skall programmet klaga.

=== Skottåret - Facitfråga
Som bekant går \~365.25 dagar på ett år. Den ursprungliga Julianska algoritmen lade till en skottdag vart 4:e år. Detta är dock inte helt exakt, vilket ledde till den Gregorianska kalendern som lägger till en dag på alla år som är delbara med 4, förutom de år som är _delbara_ med 100 men _inte delbara_ med 400. Skriv ett program som tar in ett år från användaren och skriver ut ifall det är ett skottår eller inte. Programmet måste klaga till användaren om ett negativt årtal har angivits.

*Ledning:* Kom ihåg vår kära vän modulus (`%`) från #ref(<odd-even>, supplement: "uppg.").

För att låsa upp facit: beräkna ifall år 13874844 är ett skottår. Nyckeln är "ja" om det är ett skottår, och "nej" annars.
// Svaret: ja

== Nivå 3

=== Lösare för pq-formeln
Som ni alla sett innan kan vi lösa ekvationer på formen
$
  x^2 + p x + q = 0
$
med hjälp av pq-formeln:
$
  x = - p / 2 plus.minus sqrt((p / 2)^2 - q).
$

Skriv ett program som läser in $p$ och $q$ för att sedan skriva ut lösningen, eller att det inte finns någon lösning. Vid en dubbelrot skall endast ena lösningen skrivas ut.

*Ledning:* Ni kan ta roten ur ett tal genom att höja upp det till `0.5` eller `1 / 2`. Ni höjer upp med `**`-operatorn.

=== Trianglar

Be om tre sidlängder för en triangel. Avgör sedan ifall de sidorna kan bilda en triangel. Om de kan bilda en triangel avgör även om denna triangel är liksidig, likbent eller rätvinklig. Skriv därefter ut programmets fynd.

*Ledning:* Ni kan avgöra om en triangel är giltig m.h.a. triangelolikhetssatsen:
$
  a + b > c quad "och" quad a + c > b quad "och" quad b + c > a <==> "giltig"
$
där $a,b,c$ är triagelns sidlängder. Visst finns det också en tjusig sats om räta vinklar från en grek?

=== Taxametern
Du skall skriva en taxameter för ett taxibolag. Deras priser funkar såhär: 200 kr basavgift sedan 12 kr / km för de första 5 km, därefter 8 kr / km. Om du beställer mellan kl. 22-06 så utgår även kvällstaxa på +25%.

Skriv ett program som tar in färdsträcka och beställningstimme för att sedan skriva ut priset avrundat till 2 decimaler. Du kan använda `round(a, b)` för att avrunda talet `a` till `b` decimaler.


=== Datumkontroll
Ett bokningssystem tar emot datum som dag, månad och år, men måste skydda sig mot orimliga inmatningar. Fråga efter ett datum i form av dag, månad och år. Avgör sedan om datumet är giltigt. Programmet skall klaga om något av värdena är omöjligt.

=== Kvadrantbestämning
En robot i ett koordinatsystem ska avgöra var den befinner sig. Fråga efter koordinaterna `x` och `y` för en punkt i planet. Skriv sedan ut om punkten ligger i någon av de fyra kvadranterna, på någon av axlarna, eller i origo.

=== Telefonbok
En liten digital telefonbok ska kunna slå upp kontaktuppgifter snabbt. Lagra några namn och telefonnummer i en `dict`. Fråga efter ett namn och skriv ut telefonnumret, eller att personen saknas om namnet inte finns i ordboken.

=== Dubbla medlemskap
Två lärare jämför närvarolistor från varsin grupp och vill veta var en viss elev finns. Skapa två mängder med namn, till exempel två grupper i en kurs. Fråga efter ett namn och skriv ut om personen finns i båda grupperna, bara i den ena eller i ingen av dem.

=== Prismeny
En enkel kassasnurra i en skolcafeteria ska räkna ut priset för en beställning. Lagra ett par varor och deras priser i en `dict`. Fråga efter ett varunamn och ett antal, och skriv ut totalsumman. Om varan saknas skall programmet klaga.


=== Födelseår och myndighet
En elev har fyllt i både födelseår och nuvarande ålder i ett formulär, och systemet vill kontrollera att uppgifterna hänger ihop. Fråga efter ett födelseår och en nuvarande ålder. Kontrollera om värdena hänger ihop rimligt, och skriv därefter ut om personen är myndig om tio år.

=== Färgkod med uppslag
En manual använder färgnamn som nycklar till korta beskrivningar. Lägg olika färger i en `dict` där varje färg mappas till en kort beskrivning. Fråga efter en färg och skriv ut beskrivningen, eller att färgen saknas om den inte finns i ordboken.

=== Primfaktoruppdelare (Grov överkurs --- innehåller mycket från Föreläsning 2)
Ibland behöver man veta vilka primfaktorer som bygger upp ett tal, till exempel för att förenkla bråkuttryck. Skriv ett program som ber användaren om ett heltal större än 1 och skriver ut dess primfaktorer i stigande ordning, t.ex. `12 -> 2, 2, 3`. Om talet är mindre än eller lika med 1 skall programmet klaga.

*Ledning:* Använd division och modulo (`//`, `%`) för att testa delbarhet och dra ner faktorer i en loop.

=== Växelmaskin - Facitfråga
Du skall konstruera ett program som räknar ut hur du kan dela upp en godtycklig summa hela kronor på kontanter. De giltiga kontantvalörerna idag är:
- 1000 kr
- 500 kr
- 200 kr
- 100 kr
- 50 kr
- 20 kr
- 10 kr
- 5 kr
- 2 kr
- 1 kr
*Ledning:* Modulo (`%`) är din vän, likaså tillsättande operatörer som `+=` och `-=`. Även trunkerande division (`//`) kan vara fiffigt.

För att låsa upp facit: Beräkna växeln av 135874348 kr. Nyckeln kommer att vara "`<1000><500><200><100><50><20><10><5><2><1>`" där du sätter in antal för varje sedel. En hypotetisk nyckel skulle kunna vara "2120001010". noterat att "`<1000>`" kan vara mycket större än en siffra, men det är okej och formatet följs ändå.
// Svar: 135874011020111
