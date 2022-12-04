# Co jest zrobione:

23/11/2022 Irek

* Stworzyłem modele Beer, Review, Comment
* Przetestowałem dodawanie i usuwanie recenzji.
    * po każdym zapisaniu recenzji tworzony jest queryset z aktywnych recenzji należacych do tego samego piwa co
      zapisywane
    * obliczana jest średnia recenzji z querryseta i zapisywana do piwa 


01.12.2022
działa get w API

    beers/
    beers/<int:pk>/
    beers/<int:pk/reviews/
    beers/<int:pk/reviews/<int:pk>/
    beers/<int:pk/reviews/<int:pk>/comments/
    beers/<int:pk/reviews/<int:pk>/comments/<int:pk>/

pogrzebałem przy autoryzacji ale na razie nie jest do niczego podłączone

dodałem post, put, delete które wydają się spoko działać

## STRUKTURA API

    api/v1/
    api/v1/ beers/
    api/v1/ beers/<int:beer_pk>/
    api/v1/ reviews/
    api/v1/ reviews/<int:review_pk>/
    api/v1/ comments/
    api/v1/ comments/<int:comment_pk>/

    api/v1/auth/ login/
    api/v1/auth/ user/
    api/v1/auth/ register/
    api/v1/auth/ logout/
    api/v1/auth/ logout_all/

Pobranie obrazu
    
    media/images/<str:image_name>

nie wiem jak to w javie wygląda ale w pythonie tak:

    png = 'http://127.0.0.1:8000/media/images/interfejs.png'
    response = get(png)
    image = Image.open(BytesIO(response.content))
    image.show()

recenzje danego piwa:

    api/v1/ reviews/?beer=<int:beer_pk>

komentarze danej recenzji 
    
    api/v1/ comments/?review=<int:review_pk>

    
