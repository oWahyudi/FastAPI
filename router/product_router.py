from fastapi import APIRouter,status
from fastapi.responses import Response,HTMLResponse,PlainTextResponse


router=APIRouter(prefix='/product',tags=['product'])

products=['watch','camera','phone']

@router.get('/all')
def get_all_products():
    data=" ".join(products)
    return Response(content=data,media_type="text/plain")

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

