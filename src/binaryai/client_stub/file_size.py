# Generated by ariadne-codegen on 2023-09-18 11:53
# Source: ./src/binaryai/query.graphql

from typing import Optional

from .base_model import BaseModel


class FileSize(BaseModel):
    file: Optional["FileSizeFile"]


class FileSizeFile(BaseModel):
    size: int


FileSize.model_rebuild()
FileSizeFile.model_rebuild()