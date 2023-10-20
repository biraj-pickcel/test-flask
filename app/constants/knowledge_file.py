from enum import Enum


class KnowledgeFileType(Enum):
    CRAWLED = "CRAWLED"  # crawled from the web using Apify
    UPLOADED = "UPLOADED"  # files uploaded by the user
    QNA = "QNA"
