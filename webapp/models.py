from django.db import models

class Record(models.Model): #step 50
    
    creation_date = models.DateTimeField( auto_now_add=True) #step52,51
    

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    email = models.CharField(max_length=100)

    phone = models.CharField(max_length=100)

    address = models.CharField(max_length=100)

    city = models.CharField(max_length=100)

    province = models.CharField(max_length=100)

    country = models.CharField(max_length=100)


    def __str__(self):
        return self.first_name + "   "+self.last_name  #step 53 both 23 and 24 line will see in detail after 


