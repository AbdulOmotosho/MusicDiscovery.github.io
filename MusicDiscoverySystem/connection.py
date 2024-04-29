from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'secret5214'

config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Nik2608.MySQL',
    'database': 'artistdiscoverysystem'
}

@app.route('/')
def index():
    if 'username' in session:
        # User is logged in, render the main page
        return render_template('index.html')
    else:
        # Redirect to the login page
        return redirect(url_for('login'))
    
@app.route('/user')
def user():
    if 'username' in session:
        # User is logged in, render the main page
        return render_template('user.html')
    else:
        # Redirect to the login page
        return redirect(url_for('login'))
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        # Connect to the database and verify credentials
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM account WHERE Username = %s AND Password = %s", (username, password))
        account = cursor.fetchone()
        
        if account:
            # Valid credentials, create a session
            session['username'] = username
            print(role)
            if role == 'admin': 
                return redirect(url_for('index'))
            else: 
                return redirect(url_for('user'))
        else:
            # Invalid credentials, show an error message
            return render_template('login.html', error='Invalid username or password')
    
    # Render the login page
    return render_template('login.html')
    
@app.route('/logout', methods=['POST'])
def logout():
    # Clear the session data
    session.pop('username', None)
    # Redirect to the login page
    return redirect(url_for('login'))


@app.route('/submit_account_info', methods=['POST'])
def submit_account_info():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    phone_number = request.form['phone_number']
    artist = request.form.get('artist', False)
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO account (Username,Password,Email,Phone_Number,Artist) VALUES (%s,%s,%s,%s,%s)", (username, password, email, phone_number, artist))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/add', methods=['POST'])
def add():
    data = request.form['data']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Account (Username) VALUES (%s)", (data,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete_account', methods=['POST'])
def delete_account():
    username = request.form['delete_username']
    password = request.form['delete_password']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Account WHERE Username = %s AND Password = %s", (username, password))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/update_account_password', methods=['POST'])
def update_account_password():
    username = request.form['update_username']
    oldPassword = request.form['old_password']
    password = request.form['update_password']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("Update account set Password = %s Where Username = %s And Password = %s",
                   (password,username, oldPassword))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/update_account_email', methods=['POST'])
def update_account_email():
    username = request.form['update_username']
    email = request.form['update_email']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("Update account set Email = %s Where Username = %s",
                   (email,username))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/update_account_phone_number', methods=['POST'])
def update_account_phone_number():
    username = request.form['update_username']
    phone_number = request.form['update_phone_number']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("Update account set Phone_Number = %s Where Username = %s",
                   (phone_number,username))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/update_account_artist', methods=['POST'])
def update_account_artist():
    username = request.form['update_username']
    artist = request.form['update_artist']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("Update account set artist = %s Where Username = %s",
                   (artist,username))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete_listener', methods=['POST'])
def delete_listener():
    phone_number = request.form['phone_number']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Listener WHERE PhoneNumber = %s", (phone_number,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/update_listener', methods=['POST'])
def update_listener():
    phone_number = request.form['phone_number']
    new_full_name = request.form['full_name']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("UPDATE Listener SET Full_Name = %s WHERE PhoneNumber = %s", (new_full_name, phone_number))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))


@app.route('/delete_song', methods=['POST'])
def delete_song():
    song_id = request.form['song_id']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Song WHERE Song_ID = %s", (song_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/update_song', methods=['POST'])
def update_song():
    song_id = request.form['song_id']
    new_title = request.form['title']
    new_artist = request.form['artist']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("UPDATE Song SET Title = %s, Artist = %s WHERE Song_ID = %s", (new_title, new_artist, song_id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route('/delete_artist', methods=['POST'])
def delete_artist():
    artist_id = request.form['artist_id']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Artist WHERE Artist_ID = %s", (artist_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route('/update_artist', methods=['POST'])
def update_artist():
    artist_id = request.form['artist_id']
    new_name = request.form['name']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("UPDATE Artist SET Name = %s WHERE Artist_ID = %s", (new_name, artist_id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete_album', methods=['POST'])
def delete_album():
    album_id = request.form['album_id']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Album WHERE Album_ID = %s", (album_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route('/update_album', methods=['POST'])
def update_album():
    album_id = request.form['album_id']
    new_title = request.form['title']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("UPDATE Album SET Title = %s WHERE Album_ID = %s", (new_title, album_id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))



@app.route('/delete_playlist', methods=['POST'])
def delete_playlist():
    playlist_id = request.form['playlist_id']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Playlist WHERE Playlist_ID = %s", (playlist_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/update_playlist', methods=['POST'])
def update_playlist():
    playlist_id = request.form['playlist_id']
    new_name = request.form['name']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("UPDATE Playlist SET Playlist_Name = %s WHERE Playlist_ID = %s", (new_name, playlist_id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/view_table', methods=['POST'])
def view_table():
    table_name = request.form['table_name']
    print(table_name)
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    query = f"SELECT * FROM `{table_name}`"
    cursor.execute(query)
    columns = [i[0] for i in cursor.description]  # Get column names
    entries = cursor.fetchall()
    conn.close()
    return render_template('table.html', table_name=table_name, columns=columns, entries=entries)


@app.route('/add_song', methods=['POST'])
def add_song():
    artist_id = request.form['artist_id']
    genre = request.form['genre']
    title = request.form['title']
    star_rating = request.form['star_rating']
    runtime = request.form['runtime']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Song (Artist, Genre, Title, Star_Rating, Runtime) VALUES (%s, %s, %s, %s, %s)",
                   (artist_id, genre, title, star_rating, runtime))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/add_artist', methods=['POST'])
def add_artist():
    account = request.form['account']
    name = request.form['name']
    social_media_links = request.form['social_media_links']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Artist (Account, Name, Social_Media_Links) VALUES (%s, %s, %s)",
                   (account, name, social_media_links))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/add_playlist', methods=['POST'])
def add_playlist():
    phone_number = request.form['phone_number']
    playlist_name = request.form['playlist_name']
    star_rating = request.form['star_rating']
    playlist_length = request.form['playlist_length']
    playlist_runtime = request.form['playlist_runtime']
    visibility = request.form['visibility']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Playlist (PhoneNumber, Playlist_Name, Star_Rating, Playlist_Length, Playlist_Runtime, Visibility) VALUES (%s, %s, %s, %s, %s, %s)",
                   (phone_number, playlist_name, star_rating, playlist_length, playlist_runtime, visibility))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/add_listener', methods=['POST'])
def add_listener():
    phone_number = request.form['phone_number']
    account_name = request.form['account_name']
    full_name = request.form['full_name']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Listener (PhoneNumber, Account_name, Full_Name) VALUES (%s, %s, %s)",
                   (phone_number, account_name, full_name))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/add_album', methods=['POST'])
def add_album():
    artist_username = request.form['artist_username']
    title = request.form['title']
    star_rating = request.form['star_rating']
    year = request.form['year']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Album (Artist_Username, Title, Star_Rating, Year) VALUES (%s, %s, %s, %s)",
                   (artist_username, title, star_rating, year))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))   

if __name__ == '__main__':
    app.run(debug=True)