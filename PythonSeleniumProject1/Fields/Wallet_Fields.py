# -------------------------Trimmer Product Fields ---------------------------

DropDownList = '//ul[@role="menu"]//div[@class="MuiBox-root css-0"]//li'
Search = '//input[@placeholder="Search"]'
# ------------------------------------------------------ Stock and Inventory Details
MeeshoPrice = '//input[@id="meesho_price"]'
MRP = '//input[@id="product_mrp"]'
ReturnPrice = '//input[@id="only_wrong_return_price"]'

HSNCode = '//input[@id="hsn_code"]'
# HSNCodeList = '//ul[@role="menu"]//div[2]/li'

GST = '//input[@id="supplier_gst_percent"]'


Weight = '//*[@id="product_weight_in_gms"]'

Size = '//p[normalize-space()="Size"]//parent::div//parent::div//parent::div//input'
LengthSize = '//input[@id="length_size"]'
WidthSize = '//input[@id="width_size"]'

ProductName = '//input[@id="product_name"]'



# -------------------------------------------------------- Product Details


Country = '//input[@id="country_of_origin"]'

NetQuantity = '//input[@id="multipack"]'

Manufacture = '//input[@id="manufacturer_details"]'

PackageDetail = '//input[@id="packer_details"]'

Color = '//input[@id="color"]'

Material = '//input[@id="material"]'

NoOfCompartments = "//input[@id='no_of_compartments']"

Type = '//input[@id="type"]'


# --------------------------------------------------- other Attribute

CardSlot = "//input[@id='card_slot']"

Pattern = "//input[@id='pattern']"

Description = '//textarea[@id="comment"]'