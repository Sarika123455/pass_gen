from django.db import models
from django.contrib.auth.models import User
from django.db.models.enums import Choices
from multiselectfield import MultiSelectField


# from django.db.models import F


# Create your models here.

MEMBER_CHOICES=(
        ('RD Member','RD Member'),
        ('Loan Member','Loan Member')
)



class Member(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
        full_name=models.CharField(max_length=100)
        # last_name=models.CharField(max_length=100)
        date_of_birth=models.DateField(auto_now_add=False,auto_now=False,blank=True)
        mobile_no=models.IntegerField()
        email_id=models.EmailField()
        address=models.TextField()
        aadhar_card_number=models.IntegerField()
        pan_card_number=models.CharField(max_length=100)
        aadhar_card_upload=models.ImageField(upload_to="images")
        pan_card_upload=models.ImageField(upload_to="images")
        member_loan_choice=MultiSelectField(choices=MEMBER_CHOICES,max_length=50)

        @staticmethod
        def get_all_member():
                return Member.objects.all()

        def __str__(self):
            return self.full_name
   
MONTH_CHOICES=(
        ('January','January'),
        ('February','February'),
        ('March','March'),
        ('April','April'),
        ('May','May'),
        ('June','June'),
        ('August','August'),
        ('September','September'),
        ('November','November'),
        ('December','December'),
)

class Societyloan(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
        full_name=models.ForeignKey(Member, on_delete=models.CASCADE)
       
        date = models.DateField(auto_now_add=False,auto_now=False,blank=True)
        # start_month=models.CharField(choices=MONTH_CHOICES, max_length=100) 
        # end_month=models.CharField(choices=MONTH_CHOICES, max_length=100)
        year=models.IntegerField()
        rate_of_interest=models.FloatField()
        loan_amount=models.FloatField()
        total_amount=models.FloatField(null=True)

        def __str__(self) :
            return self.start_month

        @property
        def total_amount(self):
                if(self.loan_amount != None):
                        rate_of_interest = self.year * self.rate_of_interest * self.loan_amount/100
                        total_amount = self.loan_amount + rate_of_interest
                        total_amount = total_amount/(self.year*12)
                        return total_amount
        
        
# total_amount=Societyloan.objects.annotate(total_amount=F('rate_of_interest') * F('loan_amount'))

STATUS_CHOICES=(
        ('Paid','Paid'),
        ('Unpaid','Unpaid'),
        ('Complete Loan','Complete Loan'),
)       

class Loan(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
        member_name=models.ForeignKey(Member, on_delete=models.CASCADE)
        # month =models.CharField(choices=MONTH_CHOICES, max_length=100) 
        total_amounts=models.FloatField(null=True,default=True)
        monthly_pay=models.IntegerField()
        total_paid=models.IntegerField(default=True)
        status=models.CharField(choices=STATUS_CHOICES,max_length=100)
        remaining_balance=models.IntegerField()

        @property
        def remaining_balance(self):
                if(self.total_amounts != None):
                        remaining_balance= self.total_amounts - self.monthly_pay 
                        return remaining_balance

        def total_paid(self):
                if(self.total_amounts != None):
                        total_paid = self.total_amounts - self.remaining_balance
                        return total_paid                