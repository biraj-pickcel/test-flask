from app.constants.knowledge_file import KnowledgeFileType
from app.models.knowledge_file import KnowledgeFile


def start_crawling(url: str):
    print(f"started crawling {url}")


def digest_apify_dataset(dataset_id: str):
    print(f"digesting apify dataset with id '{dataset_id}'")
    KnowledgeFile(title="some title", type=KnowledgeFileType.CRAWLED).save()
