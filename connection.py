from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'darkrose',
    'database': 'musicdiscovery'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    data = request.form['data']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Artist (Name) VALUES (%s)", (data,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete_account', methods=['POST'])
def delete_account():
    username = request.form['username']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Account WHERE Username = %s", (username,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/update_account', methods=['POST'])
def update_account():
    username = request.form['username']
    new_email = request.form['email']
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("UPDATE Account SET Email = %s WHERE Username = %s", (new_email, username))
    conn.commit()
    cursor.close()
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
    cursor.execute("DELETE FROM Song WHERE SongID = %s", (song_id,))
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
    cursor.execute("UPDATE Song SET Title = %s, Artist = %s WHERE SongID = %s", (new_title, new_artist, song_id))
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

if __name__ == '__main__':
    pass
    app.run(debug=True)