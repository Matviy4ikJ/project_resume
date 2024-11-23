from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column
import sqlalchemy as sa
from app import db


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(sa.String(250), unique=True)
    password: Mapped[str] = mapped_column(sa.String(250))

    first_name: Mapped[str] = mapped_column(sa.String(50), nullable=True)
    second_name: Mapped[str] = mapped_column(sa.String(50), nullable=True)
    phone: Mapped[str] = mapped_column(sa.String(15), nullable=True)
    education: Mapped[str] = mapped_column(sa.String(), nullable=True)
    soft_skills: Mapped[str] = mapped_column(sa.String(), nullable=True)
    hard_skills: Mapped[str] = mapped_column(sa.String(), nullable=True)
    address: Mapped[str] = mapped_column(sa.String(), nullable=True)
    profession: Mapped[str] = mapped_column(sa.String(), nullable=True)
    lang: Mapped[str] = mapped_column(sa.String(), nullable=True)
    description: Mapped[str] = mapped_column(sa.Text, nullable=True)
    image: Mapped[bytes] = mapped_column(sa.LargeBinary, nullable=True)

    def __str__(self):
        return f"Resume {self.first_name} {self.second_name}"

    def fullname(self):
        return f"{self.first_name} {self.second_name}"



