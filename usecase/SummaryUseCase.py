from model.ResultModel import ResultModel


# 요약 관련 RepositoryUseCase
class SummaryRepositoryUseCase:
    # 요약 작성
    @staticmethod
    def get_summary_write() -> ResultModel:
        return ResultModel(prompt="요약 작성", response="요약 작성")