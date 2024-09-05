import json
from fastapi import HTTPException, Depends,APIRouter,Query
from pydantic import BaseModel
from typing import List, Optional
from services.data import fetch_data
from services import models


data = fetch_data()

router = APIRouter()

@router.get('/sectors/',response_model=List[str])
def get_sectors():
    return list(set(item['sector'] for item in data))

@router.get("/categories/", response_model=List[str])
def get_categories(sector: str = Query(..., description="The sector to filter categories by")):
    categories = list(set(item['category'] for item in data if item['sector'] == sector))
    if not categories:
        raise HTTPException(status_code=404, detail="Sector not found")
    return categories

@router.get("/sources/", response_model=List[str])
def get_sources(category: str = Query(..., description="The category to filter sources by")):
    sources = list(set(item['source'] for item in data if item['category'] == category))
    if not sources:
        raise HTTPException(status_code=404, detail="Sector not found")
    return sources

@router.get("/regions/", response_model=List[str])
def get_regions(source: str = Query(..., description="The source to filter regions by"),
                category: str = Query(..., description="The category to filter sources by"),
                sector: str = Query(..., description="The sector to filter categories by")):
    regions = list(set(item['region'] for item in data if (item['source'] == source) and (item['category'] == category) and (item['sector'] == sector) ))
    if not regions:
        raise HTTPException(status_code=404, detail="Sector not found")
    return regions

@router.get("/years/", response_model=List[int])
def get_years(region: str = Query(..., description="The region to filter years by"),
            category: str = Query(..., description="The category to filter sources by"),
            sector: str = Query(..., description="The sector to filter categories by"),
            source: str = Query(..., description="The source to filter years by")):
    years = list(set(item['year'] for item in data if (item['region'] == region) and (item['source'] == source) and (item['category'] == category) and (item['sector'] == sector)))
    if not years:
        raise HTTPException(status_code=404, detail="Sector not found")
    return years

@router.get('/data/',response_model=List[models.ClimaticBase])
def get_data(
    region: str = Query(..., description="The region to filter data by"),
    category: str = Query(..., description="The category to filter data by"),
    sector: str = Query(..., description="The sector to filter data by"),
    source: str = Query(..., description="The source to filter data by"),
    year:int = Query(..., description="The source to filter data by")):
    data_list = list(item for item in data if  (item['sector'] == sector) and (item['category'] == category) and (item['source'] == source) and (item['region'] == region) and (item['year'] == year))
    return data_list