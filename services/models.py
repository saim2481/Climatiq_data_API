from pydantic import BaseModel


class ClimaticBase(BaseModel):

    activity_id:str
    id:str
    name:str
    category:str
    sector:str
    source:str
    source_link:str
    source_dataset:str
    uncertainty:str
    year:int
    year_released:int
    region:str
    region_name:str
    description:str
    unit_type:str
    unit:str
    source_lca_activity:str
    data_quality_flags:str
    access_type:str
    supported_calculation_methods:str
    factor:str
    factor:str
    factor_calculation_origin:str
    constituent_gases:str


