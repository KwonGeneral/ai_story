from model.ResultModel import ResultModel


# 챕터 관련 RepositoryUseCase
class ChapterRepositoryUseCase:
    # 제목 설정
    @staticmethod
    def get_chapter_title() -> ResultModel:
        return ResultModel(prompt="챕터 제목 설정", response="챕터 제목 설정")