from django.urls import path
from . import views

app_name = "catalogue"

urlpatterns = [
    # Artist
    path("artist/", views.artist.index, name="artist-index"),
    path("artist/create/", views.artist.create, name="artist-create"),
    path("artist/<int:artist_id>/", views.artist.show, name="artist-show"),
    path("artist/<int:artist_id>/edit/", views.artist.edit, name="artist-edit"),
    path("artist/<int:artist_id>/delete/", views.artist.delete, name="artist-delete"),

    # Type
    path("type/", views.type.index, name="type-index"),
    path("type/create/", views.type.create, name="type-create"),
    path("type/<int:type_id>/", views.type.show, name="type-show"),
    path("type/<int:type_id>/edit/", views.type.edit, name="type-edit"),
    path("type/<int:type_id>/delete/", views.type.delete, name="type-delete"),

    # Locality
    path("locality/", views.locality.index, name="locality-index"),
    path("locality/create/", views.locality.create, name="locality-create"),
    path("locality/<int:locality_id>/", views.locality.show, name="locality-show"),
    path("locality/<int:locality_id>/edit/", views.locality.edit, name="locality-edit"),
    path("locality/<int:locality_id>/delete/", views.locality.delete, name="locality-delete"),

    # Show
    path("show/", views.show.index, name="show-index"),
    path("show/create/", views.show.create, name="show-create"),
    path("show/<slug:slug>/", views.show.show, name="show-show"),
    path("show/<slug:slug>/edit/", views.show.edit, name="show-edit"),
    path("show/<slug:slug>/delete/", views.show.delete, name="show-delete"),

    # Location
    path("location/", views.location.index, name="location-index"),
    path("location/create/", views.location.create, name="location-create"),
    path("location/<int:location_id>/", views.location.show, name="location-show"),
    path("location/<int:location_id>/edit/", views.location.edit, name="location-edit"),
    path("location/<int:location_id>/delete/", views.location.delete, name="location-delete"),

    # Price
    path("price/", views.price.index, name="price-index"),
    path("price/create/", views.price.create, name="price-create"),
    path("price/<int:price_id>/", views.price.show, name="price-show"),
    path("price/<int:price_id>/edit/", views.price.edit, name="price-edit"),
    path("price/<int:price_id>/delete/", views.price.delete, name="price-delete"),
    
    # Review
    path("review/<int:review_id>/edit/", views.review.edit, name="review-edit"),
    path("review/<slug:slug>/create/", views.review.create, name="review-create"),
    path("review/<int:review_id>/delete/", views.review.delete, name="review-delete"),

    # Representations
    path('representation/', views.representation.index, name='representation-index'),
    path('representation/<int:id>/', views.representation.show, name='representation-show'),
    path('representation/create/', views.representation.create, name='representation-create'),
    path('representation/edit/<int:id>/', views.representation.edit, name='representation-edit'),
    path('representation/delete/<int:id>/', views.representation.delete, name='representation-delete'),

    # Réservations
    path('reservation/', views.reservation.index, name='reservation-index'),
    path('reservation/<int:id>/', views.reservation.show, name='reservation-show'),
    path("reservation/<int:id>/edit/", views.reservation.edit, name="reservation-edit"),
    path("reservation/<int:id>/delete/", views.reservation.delete, name="reservation-delete"),
    path('reservation//<slug:slug>/create', views.reservation.create, name='reservation-create'),
]
