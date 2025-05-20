
# Script PowerShell pour charger les fixtures Django

$fixtures = @(
    "UserFixtures.json",
    "TypeFixtures.json",
    "LocalityFixtures.json",
    "ArtistFixtures.json",
    "LocationFixtures.json",
    "PriceFixtures.json",
    "ShowFixtures.json",
    "RepresentationFixtures.json",
    "ReviewFixtures.json",
    "ReservationFixtures.json",
    "ReservationItemFixtures.json"
)

foreach ($fixture in $fixtures) {
    Write-Host "Chargement de $fixture..."
    python C:\Users\marwa\ICC\PID\EXAMEN\PROJET\PID\reservationsDjango\manage.py loaddata $fixture
}

