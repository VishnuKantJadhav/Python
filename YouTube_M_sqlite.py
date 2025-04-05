import sqlite3

conn = sqlite3.connect("youtube_videos_db")
cursor = conn.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL   )"""
)


def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?,?)", (name, time))
    # cursor.commit()


def update_video(video_id, name, time):
    cursor.execute(
        "UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id)
    )
    # cursor.commit()


def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id = ?", (video_id,))
    # cursor.commit()


def main():
    while True:
        print("\n YOUTUBE MANAGER App with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. EXIT")

        choice = input("\n Enter your choice : ")

        if choice == "1":
            list_videos()

        elif choice == "2":
            name = input("Enter the video name : ")
            time = input("Enter the video time : ")
            add_video(name, time)

        elif choice == "3":
            video_id = input("Enter video id to update : ")
            name = input("Enter the video name : ")
            time = input("Enter the video time : ")
            update_video(video_id, name, time)

        elif choice == "4":
            video_id = input("Enter video id to delete : ")
            delete_video(video_id)

        elif choice == "5":
            break

        else:
            print("Invalid Chioce")

    conn.close()


if __name__ == "__main__":
    main()
