import datetime as dt
import os


def create_document(user_id: int) -> str:
    path = f"{user_id}{dt.datetime.now()}.dat".replace(' ', '-')

    open(f"local_save/{path}", 'w')

    return path


def write_to_document(path: str, data: bytes) -> None:
    with open(f"local_save/{path}", 'wb') as file:
        file.write(data)


def delete_document(path: str) -> None:
    os.remove(f"local_save/{path}")
