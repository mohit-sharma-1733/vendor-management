from django.db import models
from datetime import timezone
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def __str__(self):
        return self.name
    
    def calculate_average_response_time(self):
        from purchase_orders.models import PurchaseOrder
        acknowledged_orders = PurchaseOrder.objects.filter(vendor=self, acknowledgment_date__isnull=False)
        response_times = [(order.acknowledgment_date - order.issue_date).total_seconds() / 3600 for order in acknowledged_orders]
        if response_times:
            self.average_response_time = sum(response_times) / len(response_times)
        else:
            self.average_response_time = 0
        self.save()
class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor} - {self.date}"
    
    @classmethod
    def update_performance(cls):
        """
        Update historical performance data for all vendors.
        This method can be called periodically or triggered by relevant events.
        """
        vendors = Vendor.objects.all()
        for vendor in vendors:
            historical_data = cls.objects.filter(vendor=vendor)
            performance_metrics = vendor.calculate_performance_metrics()
            # Create or update historical data
            if historical_data.exists():
                # Update existing record
                latest_record = historical_data.latest('date')
                if latest_record.date != timezone.now().date():
                    cls.objects.create(
                        vendor=vendor,
                        date=timezone.now().date(),
                        **performance_metrics
                    )
            else:
                # Create new record
                cls.objects.create(
                    vendor=vendor,
                    date=timezone.now().date(),
                    **performance_metrics
                )