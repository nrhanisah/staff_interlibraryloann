from django.contrib import admin
from django.utils.html import format_html
from .models import Library, Book, UserProfile, LoanRequest, TransactionTable

# Fungsi untuk buat butang Delete muncul dalam senarai
class BaseAdmin(admin.ModelAdmin):
    # Ini akan menambah kolum 'Action' yang ada butang Delete merah
    def delete_button(self, obj):
        # Alamat URL automatik untuk delete objek tersebut
        url = f"/admin/staff_app/{obj._meta.model_name}/{obj.pk}/delete/"
        return format_html(
            '<a href="{}" style="background-color: #d9534f; color: white; padding: 5px 10px; text-decoration: none; border-radius: 4px; font-weight: bold;">DELETE</a>',
            url
        )
    
    delete_button.short_description = 'Action'

# Daftar semua model dengan butang delete tersebut
@admin.register(Library)
class LibraryAdmin(BaseAdmin):
    list_display = ('request_id', 'library_name', 'status', 'delete_button')

@admin.register(Book)
class BookAdmin(BaseAdmin):
    list_display = ('book_id', 'title', 'status', 'delete_button')

@admin.register(UserProfile)
class UserProfileAdmin(BaseAdmin):
    list_display = ('user_id', 'email', 'delete_button')

@admin.register(LoanRequest)
class LoanRequestAdmin(BaseAdmin):
    list_display = ('request_id', 'user_id', 'book_id', 'status', 'delete_button')

@admin.register(TransactionTable)
class TransactionTableAdmin(BaseAdmin):
    list_display = ('transaction_id', 'date_borrowed', 'date_returned', 'paid_status', 'delete_button')