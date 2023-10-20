import datetime

from mongoengine import Document, DateTimeField, EnumField, StringField

from app.constants.knowledge_file import KnowledgeFileType


class KnowledgeFile(Document):
    title = StringField(required=True)
    type = EnumField(required=True, enum=KnowledgeFileType)
    created_at = DateTimeField(default=datetime.datetime.utcnow)

    meta = {"collection": "knowledgefiles"}
