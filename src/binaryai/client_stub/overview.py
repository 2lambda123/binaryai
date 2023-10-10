# Generated by ariadne-codegen on 2023-09-18 11:53
# Source: ./src/binaryai/query.graphql

from typing import Any, Optional

from pydantic import Field

from .base_model import BaseModel


class Overview(BaseModel):
    file: Optional["OverviewFile"]


class OverviewFile(BaseModel):
    decompile_result: Optional["OverviewFileDecompileResult"] = Field(alias="decompileResult")


class OverviewFileDecompileResult(BaseModel):
    basic_info: "OverviewFileDecompileResultBasicInfo" = Field(alias="basicInfo")


class OverviewFileDecompileResultBasicInfo(BaseModel):
    file_type: str = Field(alias="fileType")
    machine: str
    platform: str
    endian: str
    loader: str
    entry_point: Optional[Any] = Field(alias="entryPoint")
    base_address: Optional[Any] = Field(alias="baseAddress")


Overview.model_rebuild()
OverviewFile.model_rebuild()
OverviewFileDecompileResult.model_rebuild()
OverviewFileDecompileResultBasicInfo.model_rebuild()