from typing import Protocol, Self, Sequence

import sqlite3


type ReviewID = int
type ReviewDBResponse = tuple[ReviewID, str, str, str]


class ReviewRepositoryProtocol(Protocol):
    def create(self: Self, text: str, sentiment: str) -> ReviewID: ...

    def get_by_sentiment(
        self: Self,
        sentiment: str,
    ) -> Sequence[ReviewDBResponse]: ...


class ReviewSQLiteRepository:
    def __init__(
        self: Self,
        connection: sqlite3.Connection,
    ) -> None:
        self.connection = connection

    def create(
        self: Self,
        text: str,
        sentiment: str,
        created_at: str,
    ) -> ReviewID:
        cursor = self.connection.cursor()

        cursor.execute(
            '''
            INSERT INTO reviews (text, sentiment, created_at) 
            VALUES (?, ?, ?)
            ''',
            (text, sentiment, created_at,)
        )
        self.connection.commit()

        review_id = cursor.lastrowid
        return review_id

    def get_by_sentiment(
        self: Self,
        sentiment: str,
    ) -> Sequence[ReviewDBResponse]:
        cursor = self.connection.cursor()

        cursor.execute(
            '''
            SELECT * 
            FROM reviews
            WHERE sentiment = ?
            ''',
            (sentiment,),
        )
        reviews = cursor.fetchall()
        
        return reviews
