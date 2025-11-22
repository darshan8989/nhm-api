from django.db import models

class District(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=40)

    def __str__(self): return f"{self.code} - {self.name}"

class GrantScheme(models.Model):
    scheme_name  = models.CharField(max_length=100)
    total_amount = models.BigIntegerField()

    def __str__(self): return self.scheme_name

class Project(models.Model):
    grant            = models.ForeignKey(GrantScheme, on_delete=models.CASCADE)
    district         = models.ForeignKey(District, on_delete=models.PROTECT)
    name             = models.CharField(max_length=120)
    allocated_amount = models.BigIntegerField()
    status           = models.CharField(max_length=20, default='ongoing')

    def __str__(self): return self.name

class Milestone(models.Model):
    project  = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_name= models.CharField(max_length=80)
    weight   = models.PositiveSmallIntegerField()
    is_done  = models.BooleanField(default=False)

    def __str__(self): return f"{self.project} - {self.task_name}"

class Expenditure(models.Model):
    project    = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount     = models.BigIntegerField()
    spent_date = models.DateField()

    def __str__(self): return f"₹{self.amount} on {self.spent_date}"

class Evidence(models.Model):
    project  = models.ForeignKey(Project, on_delete=models.CASCADE)
    file_url = models.URLField()

    def __str__(self): return f"Evidence {self.project}"

class Anomaly(models.Model):
    project  = models.ForeignKey(Project, on_delete=models.CASCADE)
    severity = models.CharField(max_length=5, choices=[('RED','RED'),('AMBER','AMBER')])
    message  = models.CharField(max_length=200)

    def __str__(self): return f"{self.severity} - {self.project}"