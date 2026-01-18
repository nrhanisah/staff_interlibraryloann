import sqlite3

DB_NAME = 'staff_interlibraryloan.db'

def execute_query(query, params=()):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    result = cursor.fetchall()
    conn.close()
    return result

# --- 1. LIBRARY ---
def manage_library():
    print("\n[LIBRARY MENU]")
    print("1. Add request | 2. View Request | 3. Update Request | 4. Delete request")
    op = input("Choice: ")
    if op == '1':
        rid = input("request_id: ")
        name = input("library name: ")
        execute_query("INSERT INTO Library (request_id, library_name, status) VALUES (?, ?, ?)", (rid, name, 'Pending'))
    elif op == '2':
        rows = execute_query("SELECT * FROM Library")
        for r in rows:
            print(f"request_id: {r[0]}, request status: {r[2]} (Approve/Reject)")
    elif op == '3':
        rid = input("request_id to edit: ")
        new_name = input("Enter new library name: ")
        execute_query("UPDATE Library SET library_name = ? WHERE request_id = ?", (new_name, rid))
    elif op == '4':
        rid = input("request_id: ")
        execute_query("DELETE FROM Library WHERE request_id = ?", (rid,))
        print("request have been deleted.")

# --- 2. BOOK ---
def manage_book():
    print("\n[BOOK MENU]")
    print("1. Add book | 2. View all book | 3. Update book_status | 4. Delete book")
    op = input("Choice: ")
    if op == '1':
        bid = input("book id: ")
        t = input("title: ")
        a = input("author: ")
        execute_query("INSERT INTO Book (book_id, title, author, status) VALUES (?, ?, ?, ?)", (bid, t, a, 'available'))
    elif op == '2':
        rows = execute_query("SELECT * FROM Book")
        for r in rows:
            print(f"ID: {r[0]}, Title: {r[1]}, Author: {r[2]}, Status: {r[3]}")
    elif op == '3':
        bid = input("book id: ")
        st = input("edit book status: ")
        t = input("edit title: ")
        a = input("edit author: ")
        execute_query("UPDATE Book SET status=?, title=?, author=? WHERE book_id=?", (st, t, a, bid))
    elif op == '4':
        bid = input("book id: ")
        execute_query("DELETE FROM Book WHERE book_id=?", (bid,))
        print("book have been deleted.")

# --- 3. USER ---
def manage_user():
    print("\n[USER MENU]")
    print("1. Add user | 2. View user | 3. Update | 4. Delete")
    op = input("Choice: ")
    if op == '1':
        uid = input("user id: ")
        rid = input("request id: ")
        ph = input("phone number: ")
        em = input("email: ")
        execute_query("INSERT INTO User (user_id, request_id, phone_number, email, history) VALUES (?, ?, ?, ?, ?)", (uid, rid, ph, em, 'None'))
    elif op == '2':
        rows = execute_query("SELECT * FROM User")
        for r in rows:
            print(f"Profile: {r[0]}, Request Status: Pending, History: {r[4]}")
    elif op == '3':
        uid = input("user id: ")
        ph = input("update phone number: ")
        em = input("update email: ")
        rid = input("update request (change library): ")
        execute_query("UPDATE User SET phone_number=?, email=?, request_id=? WHERE user_id=?", (ph, em, rid, uid))
    elif op == '4':
        rid = input("Enter request id to delete: ")
        execute_query("DELETE FROM User WHERE request_id=?", (rid,))
        print(f"Request {rid} deleted.")

# --- 4. LOAN REQUEST ---
def manage_loan_request():
    print("\n[LOAN REQUEST MENU]")
    print("1. Add loan request | 2. View loan request | 3. Update | 4. Delete")
    op = input("Choice: ")
    if op == '1':
        rid = input("request id: ")
        uid = input("user id: ")
        bid = input("book id: ")
        fr = input("from library: ")
        to = input("to library: ")
        execute_query("INSERT INTO LoanRequest (request_id, user_id, book_id, from_library, to_library, status) VALUES (?, ?, ?, ?, ?, ?)", (rid, uid, bid, fr, to, 'Not Approved'))
    elif op == '2':
        rows = execute_query("SELECT status FROM LoanRequest")
        for r in rows:
            print(f"Status: {r[0]}")
    elif op == '3':
        rid = input("request id: ")
        st = input("update status (Approve/Not): ")
        execute_query("UPDATE LoanRequest SET status=? WHERE request_id=?", (st, rid))
    elif op == '4':
        rid = input("request id: ")
        execute_query("DELETE FROM LoanRequest WHERE request_id=?", (rid,))
        print("loan request deleted")

# --- 5. TRANSACTION ---
def manage_transaction():
    print("\n[TRANSACTION MENU]")
    print("1. ADD | 2. View | 3. Update | 4. Delete")
    op = input("Choice: ")
    if op == '1':
        tid = input("transaction id: ")
        uid = input("user id: ")
        rid = input("request id: ")
        bid = input("book id: ")
        b = int(input("date borrowed (day): "))
        r = int(input("date returned (day): "))
        execute_query("INSERT INTO TransactionTable (transaction_id, user_id, request_id, book_id, date_borrowed, date_returned, paid_status) VALUES (?, ?, ?, ?, ?, ?, ?)", (tid, uid, rid, bid, b, r, 'No'))
    elif op == '2':
        rows = execute_query("SELECT transaction_id, date_borrowed, date_returned FROM TransactionTable")
        for r in rows:
            # Perubahan serentak: Kira denda dari SQLite
            fine = (r[2] - r[1]) * 0.50
            print(f"Transaction ID: {r[0]} | TOTAL BERAPA: RM {max(0, fine):.2f}")
    elif op == '3':
        tid = input("transaction id: ")
        ps = input("student dah bayar ke belum (Yes/No): ")
        b = int(input("edit date borrowed: "))
        r = int(input("edit date returned: "))
        execute_query("UPDATE TransactionTable SET paid_status=?, date_borrowed=?, date_returned=? WHERE transaction_id=?", (ps, b, r, tid))
    elif op == '4':
        tid = input("delete transaction id: ")
        execute_query("DELETE FROM TransactionTable WHERE transaction_id=?", (tid,))

def main():
    while True:
        print("\n=== SYSTEM INTERLIBRARY LOAN (SQLITE) ===")
        print("1. Library | 2. Book | 3. User | 4. Loan Request | 5. Transaction | 0. Exit")
        c = input("Choice: ")
        if c == '1': manage_library()
        elif c == '2': manage_book()
        elif c == '3': manage_user()
        elif c == '4': manage_loan_request()
        elif c == '5': manage_transaction()
        elif c == '0': break

if __name__ == "__main__":
    main()