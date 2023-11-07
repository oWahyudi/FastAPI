from fastapi import APIRouter,status,Header,Cookie,Form
from fastapi.responses import Response,HTMLResponse,PlainTextResponse
from typing import Optional,List
from model.product import NewProduct


router=APIRouter(prefix='/product',tags=['product'])

products=['watch','camera','phone']  # Sample data storage for testing



@router.post('/createnewwithform')
async def create_product(product_data: NewProduct):
    products.append(product_data.name)
    return products



@router.get('/all')
async def get_all_products():
    data=" ".join(products)
    return Response(content=data,media_type="text/plain")

@router.get('/allwithsetcookie')
async def get_all_products():
    data=" ".join(products)
    response=Response(content=data,media_type="text/plain")
    response.set_cookie(key='test_cookie', value='test_cookie_value')
    return response


@router.get('/withheader')
async def get_products(
    response:Response,
    custom_header: Optional[str] = Header(None) 
):
    return products

@router.get('/withcookie')
async def get_products(
    response:Response,
    test_cookie: Optional[str] = Cookie(None) 
):
    return {
        'data': products,
        'my_cookie': test_cookie
    } 


@router.get('/withlistheader')
def get_products(
    response:Response,
    custom_header: Optional[List[str]] = Header(None) 
):
    response.headers['custom_response_header']= ", ".join(custom_header)
    return products



@router.get('/{id}',responses={
    200:{
        "content":{
            "text/html":{
                "example": "<div>Product</div>"
            }
        },
        "description": "Return the HTML for an object"
    },
    400:{
        "content":{
            "text/plain":{
                "example": "Product not available"
            }
        },
        "description": "Clear text error message"
    }
})
def get_product(id:int):
    if id > len(products):
        out="product not available"
        return PlainTextResponse(content=out,media_type="text/plain",status_code=status.HTTP_404_NOT_FOUND)
    else:
        product=products[id]
        out=f"""
        <head>
            <style>
                .product {{
                    width:500px;
                    height: 30px;
                    border: 2px inset green;
                    background-color: lightblue;
                    text-align: center;

                }}
            </style>
        </head>
        <div class="product">{product}</div>
        """
        return HTMLResponse(content=out,media_type="text/html")

