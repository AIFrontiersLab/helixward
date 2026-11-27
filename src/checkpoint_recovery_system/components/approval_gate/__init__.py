"""Approval Gate.

Routes runs touching restricted material to a human approver before release.
"""

from checkpoint_recovery_system.components.approval_gate.adapter import ROLE, build
from checkpoint_recovery_system.components.approval_gate.config import CONFIG, ApprovalGateConfig
from checkpoint_recovery_system.components.approval_gate.errors import ApprovalGateError
from checkpoint_recovery_system.components.approval_gate.service import ApprovalGateService

__all__ = ["CONFIG", "ROLE", "build", "ApprovalGateConfig", "ApprovalGateError", "ApprovalGateService"]
