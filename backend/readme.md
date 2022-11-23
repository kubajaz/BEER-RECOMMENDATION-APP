# Co jest zrobione:

23/11/2022 Irek

* Stworzyłem modele Beer, Review, Comment
* Przetestowałem dodawanie i usuwanie recenzji.
    * po każdym zapisaniu recenzji tworzony jest queryset z aktywnych recenzji należacych do tego samego piwa co
      zapisywane
    * obliczana jest średnia recenzji z querryseta i zapisywana do piwa 
