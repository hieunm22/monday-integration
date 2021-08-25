from typing import List

from pydantic import BaseModel

class ChallengePayload(BaseModel):
    challenge: str