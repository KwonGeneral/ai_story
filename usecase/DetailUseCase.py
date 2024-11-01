from model.ResultModel import ResultModel


# 디테일 관련 RepositoryUseCase
class DetailRepositoryUseCase:
    # 세계관 디테일업
    @staticmethod
    def get_world_detail_up() -> ResultModel:
        return ResultModel(prompt="세계관 디테일업", response="세계관 디테일업")

    # 부가적인 요소 디테일업
    @staticmethod
    def get_additional_element_detail_up() -> ResultModel:
        return ResultModel(prompt="부가적인 요소 디테일업", response="부가적인 요소 디테일업")

    # 인물 설정 디테일업
    @staticmethod
    def get_character_setting_detail_up() -> ResultModel:
        return ResultModel(prompt="인물 설정 디테일업", response="인물 설정 디테일업")

    # 주요 갈등 디테일업
    @staticmethod
    def get_main_conflict_detail_up() -> ResultModel:
        return ResultModel(prompt="주요 갈등 디테일업", response="주요 갈등 디테일업")