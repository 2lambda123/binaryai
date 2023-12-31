# Generated by ariadne-codegen on 2023-09-18 11:53
# Source: ./src/binaryai/query.graphql

from typing import Annotated, List, Literal, Optional, Union

from pydantic import Field

from .base_model import BaseModel


class ASCIIString(BaseModel):
    file: Optional["ASCIIStringFile"]


class ASCIIStringFile(BaseModel):
    executable: Optional[
        Annotated[
            Union[
                "ASCIIStringFileExecutableCOFFInfo",
                "ASCIIStringFileExecutableELFInfo",
                "ASCIIStringFileExecutableMachoInfo",
                "ASCIIStringFileExecutablePEInfo",
            ],
            Field(discriminator="typename__"),
        ]
    ]


class ASCIIStringFileExecutableCOFFInfo(BaseModel):
    typename__: Literal["COFFInfo"] = Field(alias="__typename")
    ascii_strings: Optional[List[str]] = Field(alias="asciiStrings")


class ASCIIStringFileExecutableELFInfo(BaseModel):
    typename__: Literal["ELFInfo"] = Field(alias="__typename")
    ascii_strings: Optional[List[str]] = Field(alias="asciiStrings")


class ASCIIStringFileExecutableMachoInfo(BaseModel):
    typename__: Literal["MachoInfo"] = Field(alias="__typename")
    ascii_strings: Optional[List[str]] = Field(alias="asciiStrings")


class ASCIIStringFileExecutablePEInfo(BaseModel):
    typename__: Literal["PEInfo"] = Field(alias="__typename")
    ascii_strings: Optional[List[str]] = Field(alias="asciiStrings")


ASCIIString.model_rebuild()
ASCIIStringFile.model_rebuild()
ASCIIStringFileExecutableCOFFInfo.model_rebuild()
ASCIIStringFileExecutableELFInfo.model_rebuild()
ASCIIStringFileExecutableMachoInfo.model_rebuild()
ASCIIStringFileExecutablePEInfo.model_rebuild()
