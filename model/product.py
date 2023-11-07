from pydantic import BaseModel, Field



class NewProduct(BaseModel):
    name: str = Field(..., title="Product Name", description="The name of the product")
    category: str = Field(..., title="Category", description="The category of the product")
    product_type: str = Field(..., title="Product Type", description="The type of the product")