from typing import Dict, Tuple, List
from sqlite3 import Connection

class LinksRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
    def registry_link(self, links_infos: Dict) -> None:
        cursor=self.__conn.cursor()
        cursor.execute(
            """
                INSERT INTO links (id, trip_id, link, title)
            VALUES
                (?, ?, ?, ?)
            """, (
                links_infos["id"],
                links_infos["trip_id"],
                links_infos["link"],
                links_infos["title"]
            )
        )
        self.__conn.commit()#Commit the modification in the database. It confirms and save the modification
    def find_links_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor=self.__conn.cursor()
        cursor.execute("""SELECT * FROM links where trip_id = ?""", (trip_id,))
        links=cursor.fetchall()
        return links
    