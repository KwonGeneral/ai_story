from model.ResultModel import ResultModel


# 글쓰기 관련 RepositoryUseCase
class WriteRepositoryUseCase:
    # 소설 작성
    @staticmethod
    def get_novel_write() -> ResultModel:
        return ResultModel(prompt="소설 작성", response="소설 작성")