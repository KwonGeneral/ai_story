from model.ResultModel import ResultModel


# 아이디어 관련 RepositoryUseCase
class IdeaRepositoryUseCase:
    # 세계관 아이디어 추천
    @staticmethod
    def get_world_idea_recommendation() -> ResultModel:
        return ResultModel(prompt="세계관 아이디어 추천", response="세계관 아이디어 추천")

    # 부가적인 요소 아이디어 추천
    @staticmethod
    def get_additional_element_idea_recommendation() -> ResultModel:
        return ResultModel(prompt="부가적인 요소 아이디어 추천", response="부가적인 요소 아이디어 추천")

    # 인물 설정 아이디어 추천
    @staticmethod
    def get_character_setting_idea_recommendation() -> ResultModel:
        return ResultModel(prompt="인물 설정 아이디어 추천", response="인물 설정 아이디어 추천")

    # 주요 갈등 아이디어 추천
    @staticmethod
    def get_main_conflict_idea_recommendation() -> ResultModel:
        return ResultModel(prompt="주요 갈등 아이디어 추천", response="주요 갈등 아이디어 추천")