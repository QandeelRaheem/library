import streamlit as st

# Initialize session state
if "book_list" not in st.session_state:
    st.session_state.book_list = []

st.title("Library Management System")

menu = ["Add Book", "Remove Book", "View Books"]
choice = st.sidebar.selectbox("Menu", menu)

# Add book
if choice == "Add Book":
    book_name = st.text_input("Enter the book name:")
    if st.button("Add Book"):
        st.session_state.book_list.append(book_name)
        st.success(f"'{book_name}' added successfully!")

# Remove book
elif choice == "Remove Book":
    book_name = st.text_input("Enter the book name to remove:")
    if st.button("Remove Book"):
        if book_name in st.session_state.book_list:
            st.session_state.book_list.remove(book_name)
            st.success(f"'{book_name}' removed successfully!")
        else:
            st.error("Book not found in the list!")

# View books
elif choice == "View Books":
    st.subheader("Book List")
    if st.session_state.book_list:
        st.write(st.session_state.book_list)
    else:
        st.write("No books in the library.")
