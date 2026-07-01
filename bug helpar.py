from search import search_error, search_by_category
from utils import print_title, save_history
from add_error import add_error
from edit_error import edit_error
from delete_error import delete_error
from history import show_history
from about import show_about
from statistics import show_statistics
from backup import backup_database
from restore import restore_database
from favorite import (
    add_favorite,
    show_favorites,
    remove_favorite
)
from language import set_language


def menu():
    while True:
        print_title()

        print("1. Search Error")
        print("2. Search by Category")
        print("3. Add Error")
        print("4. Edit Error")
        print("5. Delete Error")
        print("6. Search History")
        print("7. About")
        print("8. Statistics")
        print("9. Backup Database")
        print("10. Restore Database")
        print("11. Add Favorite")
        print("12. Show Favorites")
        print("13. Remove Favorite")
        print("14. Change Language")
        print("15. Exit")

        choice = input("\nSelect: ").strip()

        if choice == "1":
            error = input("\nEnter Error Name: ").strip()
            result = search_error(error)

            if result:
                print("\n========== RESULT ==========")
                print(result)
                print("============================")
                save_history(error)
            else:
                print("\n❌ Error Database-এ পাওয়া যায়নি!")

            input("\nPress Enter...")

        elif choice == "2":
            category = input("\nEnter Category: ").strip()
            search_by_category(category)
            input("\nPress Enter...")

        elif choice == "3":
            add_error()
            input("\nPress Enter...")

        elif choice == "4":
            edit_error()
            input("\nPress Enter...")

        elif choice == "5":
            delete_error()
            input("\nPress Enter...")

        elif choice == "6":
            show_history()
            input("\nPress Enter...")

        elif choice == "7":
            show_about()
            input("\nPress Enter...")

        elif choice == "8":
            show_statistics()
            input("\nPress Enter...")

        elif choice == "9":
            backup_database()
            input("\nPress Enter...")

        elif choice == "10":
            restore_database()
            input("\nPress Enter...")

        elif choice == "11":
            add_favorite()
            input("\nPress Enter...")

        elif choice == "12":
            show_favorites()
            input("\nPress Enter...")

        elif choice == "13":
            remove_favorite()
            input("\nPress Enter...")

        elif choice == "14":
            set_language()
            input("\nPress Enter...")

        elif choice == "15":
            print("\n👋 Goodbye!")
            break

        else:
            if choice == "":
                print("\n⚠️ কোনো Option নির্বাচন করা হয়নি!")
            else:
                print("\n❌ Invalid Option!")

            input("\nPress Enter...")


if __name__ == "__main__":
    menu()