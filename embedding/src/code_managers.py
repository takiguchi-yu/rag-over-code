from interfaces import ICodeManager
import os
from git import Repo


class Git(ICodeManager):
    def __init__(self, repo_url: str, repo_path: str):
        self.repo_url = repo_url
        self.repo_path = repo_path

    def update_code(self) -> None:
        if not os.path.exists(self.repo_path):
            Repo.clone_from(self.repo_url, to_path=self.repo_path)
        else:
            repo = Repo(self.repo_path)
            repo.remotes[0].pull()


class S3(ICodeManager):
    """未実装"""

    def __init__(self, bucket_name: str, repo_path: str):
        self.bucket_name = bucket_name
        self.repo_path = repo_path

    def update_code(self) -> None:
        # 実装は省略
        pass
