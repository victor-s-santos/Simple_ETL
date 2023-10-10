from typing import Optional
from pydantic import BaseModel, conint, confloat, field_validator, FieldValidationInfo
from .validators.validators import validate_null_in_number_field
import logging


class FastFoodObj(BaseModel):
    """Realize the validation of each specific data format for each fastfoodobj"""

    Company: Optional[str] = None
    Item: Optional[str] = None
    Calories: Optional[conint(ge=0)] | None = None
    CaloriesFromFat: Optional[conint(ge=0)] | None = None
    TotalFat: Optional[confloat(ge=0) | conint(ge=0)] | None = None
    SaturatedFat: Optional[confloat(ge=0) | conint(ge=0)] | None = None
    TransFat: Optional[confloat(ge=0) | conint(ge=0)] | None = None
    Cholesterol: Optional[conint(ge=0) | None] = None
    Sodium: Optional[conint(ge=0) | None] = None
    Carbs: Optional[confloat(ge=0) | conint(ge=0)] | None = None
    Fiber: Optional[confloat(ge=0) | conint(ge=0)] | None = None
    Sugars: Optional[confloat(ge=0) | conint(ge=0)] | None = None
    Protein: Optional[confloat(ge=0) | conint(ge=0)] | None = None
    WeightWatchersPnts: Optional[confloat(ge=0) | str] | None = None

    @field_validator("Calories")
    @classmethod
    def validate_calories(
        cls, value: int | None, info: FieldValidationInfo
    ) -> int | None:
        logging.info(info.config.get("title"))
        return validate_null_in_number_field(value)

    @field_validator("CaloriesFromFat")
    @classmethod
    def validate_caloriesfromfat(
        cls, value: int | None, info: FieldValidationInfo
    ) -> int | None:
        logging.info(info.config.get("title"))
        return validate_null_in_number_field(value)

    @field_validator("TotalFat")
    @classmethod
    def validate_totalfat(
        cls, value: float | int | None, info: FieldValidationInfo
    ) -> float | int | None:
        logging.info(info.config.get("title"))
        return validate_null_in_number_field(value)

    @field_validator("SaturatedFat")
    @classmethod
    def validate_saturedfat(
        cls, value: float | int | None, info: FieldValidationInfo
    ) -> float | int | None:
        logging.info(info.config.get("title"))
        return validate_null_in_number_field(value)

    @field_validator("TransFat")
    @classmethod
    def validate_transfat(
        cls, value: float | int | None, info: FieldValidationInfo
    ) -> float | int | None:
        logging.info(info.config.get("title"))
        return validate_null_in_number_field(value)

    @field_validator("Cholesterol")
    @classmethod
    def validate_cholesterol(
        cls, value: int | None, info: FieldValidationInfo
    ) -> int | None:
        logging.info(info.config.get("title"))
        return validate_null_in_number_field(value)

    @field_validator("Sodium")
    @classmethod
    def validate_sodium(
        cls, value: int | None, info: FieldValidationInfo
    ) -> int | None:
        logging.info(info.config.get("title"))
        return validate_null_in_number_field(value)

    @field_validator("Carbs")
    @classmethod
    def validate_carbs(
        cls, value: float | int | None, info: FieldValidationInfo
    ) -> float | int | None:
        logging.info(info.config.get("title"))
        return validate_null_in_number_field(value)

    @field_validator("Fiber")
    @classmethod
    def validate_fiber(
        cls, value: float | int | None, info: FieldValidationInfo
    ) -> float | int | None:
        logging.info(info.config.get("title"))
        return validate_null_in_number_field(value)

    @field_validator("Sugars")
    @classmethod
    def validate_sugars(
        cls, value: float | int | None, info: FieldValidationInfo
    ) -> float | int | None:
        logging.info(info.config.get("title"))
        return validate_null_in_number_field(value)

    @field_validator("Protein")
    @classmethod
    def validate_protein(
        cls, value: float | int | None, info: FieldValidationInfo
    ) -> float | int | None:
        logging.info(info.config.get("title"))
        return validate_null_in_number_field(value)

    @field_validator("WeightWatchersPnts")
    @classmethod
    def validate_weightwatcherspnts(
        cls, value: float | int | None, info: FieldValidationInfo
    ) -> float | int | None:
        logging.info(info.config.get("title"))
        return validate_null_in_number_field(value)
