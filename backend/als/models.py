from django.db import models

class AL(models.Model):
    name = models.CharField(max_length=50, null=False, blank=True)
    n_instances = models.IntegerField(null=False, default=10)
    accuracy_goal = models.FloatField(null=False, default=85)

    technics = (
        ('RandomSampling', 'RandomSampling'),
        ('UncertaintySampling', 'UncertaintySampling'),
        ('ClusterBasedSampling', 'ClusterBasedSampling'),
        ('OutlierSampling', 'OutlierSampling'),
        ('RepresentativeSampling', 'RepresentativeSampling'),
        ('UncertaintyWithClusteringSampling', 'UncertaintyWithClusteringSampling'),
        ('UncertaintyWithModelOutliersSampling', 'UncertaintyWithModelOutliersSampling'),
        ('RepresentativeWithClusteringSampling','RepresentativeWithClusteringSampling'),
        ('HighestEntropyClusteringSampling', 'HighestEntropyClusteringSampling'),
        ('UncertaintyWithRepresentativeSampling', 'UncertaintyWithRepresentativeSampling'),
        ('HighestEntropyUncertaintySampling', 'HighestEntropyUncertaintySampling'),
        ('OutliersWithRepresentativeSampling', 'OutliersWithRepresentativeSampling'),
    )
    query_technic = models.CharField(max_length=50, choices=technics, default='RandomSampling')