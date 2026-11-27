"""Relevance Scorer.

Scores query-candidate relevance with a deterministic BM25-style reference model.
"""

from checkpoint_recovery_system.components.relevance_scorer.adapter import ROLE, build
from checkpoint_recovery_system.components.relevance_scorer.config import CONFIG, RelevanceScorerConfig
from checkpoint_recovery_system.components.relevance_scorer.errors import RelevanceScorerError
from checkpoint_recovery_system.components.relevance_scorer.service import RelevanceScorerService

__all__ = ["CONFIG", "ROLE", "build", "RelevanceScorerConfig", "RelevanceScorerError", "RelevanceScorerService"]
