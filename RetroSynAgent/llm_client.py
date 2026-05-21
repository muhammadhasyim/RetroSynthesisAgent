"""Pluggable LLM backend for RetroSynAgent."""

from __future__ import annotations

import os


class SkipLLMError(RuntimeError):
    """Raised when LLM is required but RETRO_LLM_BACKEND=skip."""


def complete(prompt: str, content: str | None = None) -> str:
    backend = os.environ.get("RETRO_LLM_BACKEND", "skip").strip().lower()
    if backend == "openai":
        from .GPTAPI import GPTAPI

        llm = GPTAPI(temperature=0.0)
        return llm.answer_wo_vision(prompt, content)
    if backend == "skip":
        raise SkipLLMError(
            "RETRO_LLM_BACKEND=skip; no cached llm_res found. "
            "Submit extractions via biologix-ai submit_retro_extractions, "
            "or set RETRO_LLM_BACKEND=openai with API_KEY configured."
        )
    raise ValueError(f"Unknown RETRO_LLM_BACKEND: {backend}")
