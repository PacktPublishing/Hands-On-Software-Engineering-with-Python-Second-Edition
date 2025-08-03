# CH17-code README

The code for this chapter is concerned with implementing the final API Gateway API, backed by Python Lambda Functions.

For local development purposes, a FastAPI-based application is also provided with minimal (but functional) displays of the data available through the API.

The overall structure of the API is:

```
(api-root-url)
├╴api/
│ └╴v1/
│   │ # The items in braces, {}, are data-points for the
│   │ # endpoints. A {payload} is a request body, the
│   │ # various {*_oid} values are path-parameters.
│   ├╴artisan/
│   │ ├╴GET ............... {artisan_oid}
│   │ ├╴PATCH ............. {artisan_oid} {payload}
│   │ ├╴PUT ............... {artisan_oid} {payload}
│   │ ├╴POST .............. {payload}
│   │ └╴DELETE ............ {artisan_oid}
│   ├╴artisans/
│   │ └╴GET
│   ├╴product/
│   │ ├╴GET ............... {product_oid}
│   │ ├╴PATCH ............. {product_oid} {payload}
│   │ ├╴PUT ............... {product_oid} {payload}
│   │ ├╴POST .............. {payload}
│   │ └╴DELETE ............ {product_oid}
│   ├╴products/
│   │ └╴GET
│   ├╴product-image/
│   │ ├╴GET ............... {product_image_oid}
│   │ ├╴PATCH ............. {product_image_oid} {payload}
│   │ ├╴PUT ............... {product_image_oid} {payload}
│   │ ├╴POST .............. {payload}
│   │ └╴DELETE ............ {product_image_oid}
│   ├╴product-images/
│   │ └╴GET ............... {product_oid}
│   └╴admin/
│     ├╴artisan/
│     │ ├╴GET ............. {artisan_oid}
│     │ ├╴PATCH ........... {artisan_oid} {payload}
│     │ ├╴PUT ............. {artisan_oid} {payload}
│     │ └╴DELETE .......... {artisan_oid}
│     ├╴artisans/
│     │ └╴GET
│     ├╴product/
│     │ ├╴GET ............. {product_oid}
│     │ ├╴PATCH ........... {product_oid} {payload}
│     │ ├╴PUT ............. {product_oid} {payload}
│     │ └╴DELETE .......... {product_oid}
│     ├╴products/
│     │ └╴GET
│     ├╴product-image/
│     │ ├╴GET ............. {product_image_oid}
│     │ ├╴PATCH ........... {product_image_oid} {payload}
│     │ ├╴PUT ............. {product_image_oid} {payload}
│     │ └╴DELETE .......... {product_image_oid}
│     └╴product-images/
│       └╴GET ............. {product_oid}
│
│ # These endpoints are part of the local API application
│ # only, used to provide a local website that engineers
│ # can use to test functionality without having to
│ # deploy a copy of the project to the cloud. They are
│ # expected to mirror the live website's structure, more
│ # or less, but NOT the look-and-feel (actual user
│ # experience) of the live site.
│
├╴/ ("home page")
│   ├╴artisans/ ........... {Artisan list view}
│   │ ├╴{oid} ............. {Artisan detail view}
│   │ │ └╴my-products ..... {Artisan product-list view}
│   │ │
│   │ │ # Artisan sign-up
│   │ └╴sign-up
│   │
│   │ # Artisan's "self-serve" functionality
│   │ # (Logged-in Artisan only)
│   ├╴artisan/
│   │ └╴products/ ......... {Artisan product-list view}
│   │   └╴{product_oid} ... {Artisan product-detail view}
│   │
│   └╴products/ ........... {Product list view}
│     └╴{oid} ............. {Product detail view}
│
│ # HMS staff administration functionality
│ # (Logged-in HMS staff only)
└╴admin/
  ├╴artisans/ ............. {Artisan list view}
  │ └╴{oid} ............... {Artisan detail view}
  │   └╴products/ ......... {Artisan product-list view}
  │     └╴{product_oid} ... {Artisan product-detail view}
  └╴products/ ............. {Product list view}
    └╴{oid} ............... {Product detail view}
```
