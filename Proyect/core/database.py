from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://neondb_owner:npg_FZgKiz96WHiwE@ep-jolly-base-apzf0sqf-pooler.c-7.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()