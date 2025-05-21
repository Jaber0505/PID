# Script PowerShell pour charger les fixtures Django
$fixtures = @(
    "UserFixtures.json",
    "TypeFixtures.json",
    "LocalityFixtures.json",
    "ArtistFixtures.json",
    "LocationFixtures.json",
    "PriceFixtures.json",
    "ShowFixtures.json",
    "ArtistTypeFixtures.json",
    "ArtistTypeShowFixtures.json",
    "RepresentationFixtures.json",
    "ReviewFixtures.json",
    "ReservationFixtures.json",
    "ReservationItemFixtures.json"
)

foreach ($fixture in $fixtures) {
    Write-Host "Chargement de $fixture..."
    python manage.py loaddata $fixture
}