def km_from_ly(distance_ly):
    """Return distance in km from a distance in ly"""
    return 9.461e12 * distance_ly


# En dict är fiffig för att spara avstånd indexerat på namn.
planets_distance_ly = {
    "40 Eridani A b": 16.3,
    "Proxima Centauri b": 4.2,
    "Barnard's Star b": 6.0,
    "Ross 128 b": 11.0,
    "Luyten b": 12.4,
}

# Vi itererar över både planetnamn och tillhörande avstånd.
for planet, dist in planets_distance_ly.items():
    # :<20 gör att den inskjutna strängen är minst 20
    # karaktärer lång. Det ger oss en nice alignment.
    print(f"{planet:<20}: {dist} ly = {km_from_ly(dist)} km")
