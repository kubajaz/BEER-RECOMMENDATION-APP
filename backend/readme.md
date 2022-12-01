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

