from django.contrib import admin
from .models import EmailRecord

@admin.register(EmailRecord)
class EmailRecordAdmin(admin.ModelAdmin):
    list_display = ('subject', 'recipient', 'cc', 'bcc', 'sent_at')
    search_fields = ('subject', 'recipient', 'cc', 'bcc')
