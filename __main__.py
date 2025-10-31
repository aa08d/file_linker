import os
from dataclasses import dataclass
from datetime import date, datetime
from uuid import UUID
from uuid6 import uuid7

from flask import Flask, render_template, request, send_from_directory

from app.database.base import init_db
from app.database.base import get_session
from app.database.crud import create_media, get_media
from app.scheduler.main import init_scheduler

app = Flask(__name__)
UPLOAD_DIR = "media/"


@app.route('/')
def home():
    return render_template("pages/home.html")


@app.route('/upload', methods=["POST"])
def result():
    uploaded_file = request.files.get('fileInput')
    expire = datetime.strptime(
        request.form.get("expiryDate"),
        '%Y-%m-%d'
    ).date()
    
    uuid = uuid7()
    media_name = ''.join([str(uuid), '.', uploaded_file.filename.split(".")[1]])
    link = f"127.0.0.1:5000/download?filename={media_name}"
    session = get_session()
    media = create_media(session=session, expire=expire, uuid=uuid, link=link)
    uploaded_file.save(f'{UPLOAD_DIR}{media_name}')

    return render_template("pages/result.html", link=link)


@app.route('/download')
def download():
    filename = request.args.get("filename")

    file_path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.isfile(file_path):
        return "Файла не существует"

    return send_from_directory(UPLOAD_DIR, filename, as_attachment=True)


@dataclass
class MediaDTO:
    id: UUID
    expire: date
    link: str


@app.route('/history')
def history():
    session = get_session()
    row_media = get_media(session=session)
    media = [
        MediaDTO(
            id=m.id,
            expire=m.expire,
            link=m.link,
        )
        for m in row_media
    ]
    return render_template("pages/history.html", media=media)


def main() -> None:
    init_db()
    session = get_session()
    init_scheduler(session=session)
    app.run(debug=True)


if __name__ == "__main__":
    main()
