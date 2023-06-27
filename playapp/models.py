from django.db import models


class Quota(models.Model):
    """
    Single countable or boolean property of system (limitation).
    """
    codename = models.CharField(
        'codename', max_length=50, unique=True, db_index=True)
    name = models.CharField('name', max_length=100)
    unit = models.CharField('unit', max_length=100, blank=True)
    description = models.TextField('description', blank=True)
    is_boolean = models.BooleanField('is boolean', default=False)
    url = models.CharField(max_length=200, blank=True, help_text='Optional link to page with more information '
                                                                 '(for clickable pricing table headers)')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Quota"
        verbose_name_plural = "Quotas"

    def __str__(self):
        return '{} ({})'.format(
            self.codename,
            'Boolean' if self.is_boolean else 'Numeric'
        )


class PlanQuota(models.Model):
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE, null=True)
    quota = models.ForeignKey('Quota', on_delete=models.CASCADE, null=True)
    value = models.IntegerField(default=0)


class Plan(models.Model):
    name = models.CharField(max_length=200)
    version = models.IntegerField(default=1)
    quotas = models.ManyToManyField(Quota, blank=True, null=True, related_name='Plan', through='PlanQuota')
    base_plan = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='Plan')

    class Meta:
        # ordering = [1]
        verbose_name = "PLAN"
        verbose_name_plural = "plan"

    @property
    def get_quotas(self):
        base_list = []

        if self.base_plan:
            base_list.extend(self.base_plan.quotas.values_list('id', flat=True))
        base_list.extend([quota.id for quota in self.quotas.all()])
        return base_list

    @property
    def all_quotas(self):
        q = set()
        q.update(self.planquota_set.all())

        base_plan = self.base_plan
        while base_plan:
            added_quota_names = [x.quota.name for x in q]
            for p in base_plan.planquota_set.exclude(quota__name__in=added_quota_names):
                q.add(p)

            base_plan = base_plan.base_plan
        return list(q)

    def __str__(self):
        return f"{self.name}:{self.version}"
