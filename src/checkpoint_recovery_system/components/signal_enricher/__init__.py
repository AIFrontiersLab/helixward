"""Signal Enricher.

Annotates candidates with token counts and query overlap, and collapses duplicate passages.
"""

from checkpoint_recovery_system.components.signal_enricher.adapter import ROLE, build
from checkpoint_recovery_system.components.signal_enricher.config import CONFIG, SignalEnricherConfig
from checkpoint_recovery_system.components.signal_enricher.errors import SignalEnricherError
from checkpoint_recovery_system.components.signal_enricher.service import SignalEnricherService

__all__ = ["CONFIG", "ROLE", "build", "SignalEnricherConfig", "SignalEnricherError", "SignalEnricherService"]
