from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = '123456'  # Used for session management

# Dummy data for books
books = [
    {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'description': 'A classic novel about the American Dream.', 'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIcTcj27FApks2OszI1Jq5sxSXLJPnrpQ_Mg&s', 'genre': 'Fiction', 'price': 10.99},

    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'description': 'A novel about racial injustice in the deep South.', 'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBbmHyPCCMuOHrf_wCUbdDcURsEXybFvfGvg&s', 'genre': 'Fiction', 'price': 12.99},

    {'id': 3, 'title': '1984', 'author': 'George Orwell', 'description': 'A dystopian novel about surveillance and totalitarianism.', 'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRM1k7QNP_48y1nNMkXTZxtAejkB_fIkV1ipg&s', 'genre': 'Dystopian', 'price': 14.99},

    {'id': 4, 'title': 'The Shining', 'author': 'Stephen King', 'description': 'A psychological horror novel about isolation and madness.', 'image_url': 'https://m.media-amazon.com/images/I/91U7HNa2NQL._AC_UF1000,1000_QL80_.jpg', 'genre': 'Horror', 'price': 15.99},

    {'id': 5, 'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'description': 'A novel about teenage rebellion and existential angst.', 'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvp36HucRI20iE3ccdFVGNy8fieQrSbzCuig&s', 'genre': 'Fiction', 'price': 11.99},

    {'id': 6, 'title': 'The Silent Patient', 'author': 'Alex Michaelides', 'description': 'A psychological thriller about a woman who shoots her husband.', 'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSe-cYwGgM47tDkH9s2CIGEspbQMMa4gUN6Ag&s', 'genre': 'Mystery', 'price': 13.99},

    {'id': 7, 'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'description': 'A classic romance novel about love and social class.', 'image_url': 'https://rukminim2.flixcart.com/image/850/1000/xif0q/book/1/w/r/pride-and-prejudice-original-imagrvgefgppadqp.jpeg?q=90&crop=false', 'genre': 'Romance', 'price': 9.99},

    {'id': 8, 'title': 'The Da Vinci Code', 'author': 'Dan Brown', 'description': 'A historical mystery thriller involving secret societies.', 'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZkUzl4gqnmBQaDQZKxzO6_Jfo-8ifzMaKUA&s', 'genre': 'Mystery', 'price': 16.99},

    {'id': 9, 'title': 'The Girl with the Dragon Tattoo', 'author': 'Stieg Larsson', 'description': 'A mystery thriller about solving a decades-old disappearance.', 'image_url': 'https://m.media-amazon.com/images/I/81YW99XIpJL._UF1000,1000_QL80_.jpg', 'genre': 'Mystery', 'price': 14.99},

    {'id': 10, 'title': 'Gone Girl', 'author': 'Gillian Flynn', 'description': 'A thriller about a woman’s mysterious disappearance.', 'image_url': 'https://m.media-amazon.com/images/I/71+khXHbe5L.jpg', 'genre': 'Thriller', 'price': 12.99},

    {'id': 11, 'title': 'It', 'author': 'Stephen King', 'description': 'A horror novel about a group of kids confronting an ancient evil.', 'image_url': 'https://m.media-amazon.com/images/I/71ZIovNjw+L._AC_UF1000,1000_QL80_.jpg', 'genre': 'Horror', 'price': 17.99},

    {'id': 12, 'title': 'The Alchemist', 'author': 'Paulo Coelho', 'description': 'A philosophical novel about following one’s dreams.', 'image_url': 'https://m.media-amazon.com/images/I/81FPzmB5fgL._AC_UF1000,1000_QL80_.jpg', 'genre': 'Fiction', 'price': 10.49},

    {'id': 13, 'title': 'The Fault in Our Stars', 'author': 'John Green', 'description': 'A poignant love story about two teens with cancer.', 'image_url': 'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1660273739i/11870085.jpg', 'genre': 'Romance', 'price': 8.99},

    {'id': 14, 'title': 'Frankenstein', 'author': 'Mary Shelley', 'description': 'A classic horror novel about a scientist and his monstrous creation.', 'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTH1QIuF4NPq_ZXEH40359lGSShtdU4F8KAtg&s', 'genre': 'Horror', 'price': 9.99},

    {'id': 15, 'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'description': 'A fantasy novel about a hobbit’s unexpected adventure.', 'image_url': 'https://m.media-amazon.com/images/I/81mCE+uclxL._UF1000,1000_QL80_.jpg', 'genre': 'Fantasy', 'price': 14.49},

    {'id': 16, 'title': 'Brave New World', 'author': 'Aldous Huxley', 'description': 'A dystopian novel about a future society based on conformity.', 'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSpC7CXDorRstQlSIeanXmylVVIAFP2pWNc2w&s', 'genre': 'Dystopian', 'price': 12.99},

    {'id': 17, 'title': 'Murder on the Orient Express', 'author': 'Agatha Christie', 'description': 'A famous mystery novel featuring Hercule Poirot.', 'image_url': 'https://m.media-amazon.com/images/I/61rRmiz9HvL._AC_UF1000,1000_QL80_.jpg', 'genre': 'Mystery', 'price': 10.99},

    {'id': 18, 'title': 'The Picture of Dorian Gray', 'author': 'Oscar Wilde', 'description': 'A novel about vanity, corruption, and the consequences of indulgence.', 'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2f1yBAWXHpHATryDEaVozatMu51pQFMGiDg&s', 'genre': 'Gothic', 'price': 11.49},

    {'id': 19, 'title': 'Dracula', 'author': 'Bram Stoker', 'description': 'A gothic horror novel about the legendary vampire, Count Dracula.', 'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQapwj529X6xqxmWUlrZAbQLhi-jEpU1-gx8A&s', 'genre': 'Horror', 'price': 9.99},

    {'id': 20, 'title': 'The Secret Garden', 'author': 'Frances Hodgson Burnett', 'description': 'A classic children’s novel about a magical garden.', 'image_url': 'https://m.media-amazon.com/images/I/71ppraw-V4L._AC_UF1000,1000_QL80_.jpg', 'genre': 'Children', 'price': 7.99},

    {'id': 21, 'title': 'A Game of Thrones', 'author': 'George R.R. Martin', 'description': 'A fantasy epic of political intrigue and conflict in Westeros.', 'image_url': 'https://m.media-amazon.com/images/I/714ExofeKJL.jpg', 'genre': 'Fantasy', 'price': 18.99},
]



# Home page route with genre filter
@app.route('/')
def index():
    genre = request.args.get('genre')
    filtered_books = books
    if genre:
        filtered_books = [book for book in books if book['genre'].lower() == genre.lower()]
    genres = list(set(book['genre'] for book in books))
    return render_template('index.html', books=filtered_books, genres=genres)

# Book detail page
@app.route('/book/<int:book_id>')
def book_detail(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    
    if not book:
        return redirect(url_for('index'))  # Redirect to home page if book not found
    
    # Filter books by the same genre
    similar_books = [b for b in books if b['genre'] == book['genre'] and b['id'] != book['id']]
    
    return render_template('book.html', book=book, similar_books=similar_books)

@app.route('/add_to_cart/<int:book_id>', methods=['POST', 'GET'])
def add_to_cart(book_id):
    # Initialize cart if it doesn't exist
    if 'cart' not in session:
        session['cart'] = []

    # Add the book to the cart
    session['cart'].append(book_id)
    session.modified = True  # Ensure changes are saved
    print("Updated Cart:", session['cart'])  # Debugging output

    return redirect(url_for('index'))

# View cart page
@app.route('/cart')
def view_cart():
    cart_books = [book for book in books if book['id'] in session.get('cart', [])]
    total = sum(book['price'] for book in cart_books)
    return render_template('cart.html', cart_books=cart_books, total=total)
    print("Session Cart:", session.get('cart'))  # To check cart contents


# Place order
@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        session.pop('cart', None)  # Clear the cart
        return redirect(url_for('index'))
    cart_books = [book for book in books if book['id'] in session.get('cart', [])]
    total = sum(book['price'] for book in cart_books)
    return render_template('order.html', cart_books=cart_books, total=total)





if __name__ == '__main__':
    app.run(debug=True)
