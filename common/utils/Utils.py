import os

from anthropic import Anthropic


# 유틸리티 클래스
class Utils:
    # Anthropic 클라이언트 가져오기
    @staticmethod
    def get_anthropic_client() -> Anthropic:
        return Anthropic()

    # Anthropic 모델 가져오기
    @staticmethod
    def get_anthropic_model() -> str:
        return "claude-3-5-sonnet-20240620"

    # Anthropic 최대 토큰 수 가져오기
    @staticmethod
    def get_anthropic_max_tokens() -> int:
        return 8192

    # 프로젝트 루트 디렉토리 경로 가져오기
    @staticmethod
    def get_project_root():
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))