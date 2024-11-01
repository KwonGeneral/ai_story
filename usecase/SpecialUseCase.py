from model.ResultModel import ResultModel


# 특이사항 관련 RepositoryUseCase
class SpecialNoteRepositoryUseCase:
    # 특이사항 업데이트
    @staticmethod
    def get_special_note_update() -> ResultModel:
        return ResultModel(prompt="특이사항 업데이트", response="특이사항 업데이트")