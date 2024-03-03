# import uuid
# import os

# from sqlalchemy import (
#     create_engine,
#     Column,
#     String,
#     Integer,
#     ForeignKey,
# )
# from sqlalchemy.orm import (
#     sessionmaker,
#     relationship,
#     declarative_base,
# )

# from ytserver.models.video import Video

# Base = declarative_base()


# class Videos(Base):
#     __tablename__ = "videos"

#     id = Column(String, primary_key=True, default=lambda: uuid.uuid4().hex)
#     extractor_key = Column(String)
#     display_id = Column(String, unique=True)
#     thumbnail = Column(String)
#     title = Column(String)
#     description = Column(String)
#     webpage_url = Column(String)
#     uploader_url = Column(String)
#     duration_string = Column(String)

#     audio_formats = relationship("AudioFormat", back_populates="video")
#     video_formats = relationship("VideoFormat", back_populates="video")


# class AudioFormat(Base):
#     __tablename__ = "audio_formats"

#     id = Column(String, primary_key=True, default=lambda: uuid.uuid4().hex)
#     video_id = Column(String, ForeignKey("videos.display_id"))
#     format = Column(String)
#     format_note = Column(String)
#     resolution = Column(String)
#     url = Column(String)
#     ext = Column(String)
#     protocol = Column(String)
#     filesize = Column(Integer)
#     video = relationship("Videos", back_populates="audio_formats")


# class VideoFormat(Base):
#     __tablename__ = "video_formats"

#     id = Column(String, primary_key=True, default=lambda: uuid.uuid4().hex)
#     video_id = Column(String, ForeignKey("videos.display_id"))
#     format = Column(String)
#     format_note = Column(String)
#     resolution = Column(String)
#     url = Column(String)
#     ext = Column(String)
#     protocol = Column(String)
#     filesize = Column(Integer)
#     video = relationship("Videos", back_populates="video_formats")


# db_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), "database"))
# os.makedirs(db_directory, exist_ok=True)
# db_path = os.path.join(db_directory, "videos.db")
# engine = create_engine(f"sqlite:///{db_path}")
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()
