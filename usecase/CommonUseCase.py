from model.ResultModel import ResultModel


# 공용 관련 RepositoryUseCase
class CommonRepositoryUseCase:
    # 작품 이름 추천
    @staticmethod
    def get_recommendation_work_name() -> ResultModel:
        return ResultModel(prompt="추천 작품 이름", response="추천 작품 이름")

    # 작품 설명 추천
    @staticmethod
    def get_recommendation_work_description() -> ResultModel:
        return ResultModel(prompt="추천 작품 설명", response="추천 작품 설명")