from sqlmodel import Session, select
from models import Category, Market, Rule
from .database import engine

def seed():
    categories = [
        {"id": "146b1a88-b3d3-4232-8b8f-c1f006f1e86d", "name": "Alimentação"},
        {"id": "52e81585-f71a-44cd-8bd0-49771e45da44", "name": "Compras"},
        {"id": "57d6e5ff-35f6-4d21-a521-84f23d511d25", "name": "Hospedagem"},
        {"id": "826910d4-187d-4c15-88f4-382b7e056739", "name": "Cinema"},
        {"id": "abce52cf-b33b-4b3c-8972-eb72c66c83e4", "name": "Padaria"},
    ]
    
    markets = [
        # ALIMENTAÇÃO
        {
            "id": "012576ea-4441-4b8a-89e5-d5f32104c7c4",
            "category_id": "146b1a88-b3d3-4232-8b8f-c1f006f1e86d",
            "name": "Sabor Grill",
            "description": "Churrascaria com cortes nobres e buffet variado. Experiência completa para os amantes de carne.",
            "latitude": -23.55974230991911,
            "longitude": -46.65814845249887,
            "coupons": 10,
            "address": "Av. Paulista - Bela Vista",
            "phone": "(11) 94567-1212",
            "cover": "https://images.unsplash.com/photo-1498654896293-37aacf113fd9?w=400&h=300"
        },
        {
            "id": "2bc11e34-5f30-4ba0-90fa-c1c98f649281",
            "category_id": "146b1a88-b3d3-4232-8b8f-c1f006f1e86d",
            "name": "Café Central",
            "description": "Café aconchegante com opções de lanches e bebidas artesanais. Perfeito para uma pausa.",
            "latitude": -23.559457108504436,
            "longitude": -46.66252581753144,
            "coupons": 10,
            "address": "Alameda Jaú - Jardim Paulista",
            "phone": "(12) 3456-7890",
            "cover": "https://images.unsplash.com/photo-1551218808-94e220e084d2?w=400&h=300"
        },
        {
            "id": "4197b830-aa9c-40d4-a22e-c05043588a77",
            "category_id": "146b1a88-b3d3-4232-8b8f-c1f006f1e86d",
            "name": "Burguer Up",
            "description": "Hambúrgueres gourmet preparados na hora. Ingredientes frescos e combinações únicas.",
            "latitude": -23.56011117635681,
            "longitude": -46.65636680690605,
            "coupons": 10,
            "address": "Rua Peixoto Gomide - Jardim Paulista",
            "phone": "(13) 98765-4321",
            "cover": "https://images.unsplash.com/photo-1528605248644-14dd04022da1?w=400&h=300"
        },
        {
            "id": "4209c72f-9d14-410c-91af-c24d08f177cc",
            "category_id": "146b1a88-b3d3-4232-8b8f-c1f006f1e86d",
            "name": "Doce & Delícia",
            "description": "Confeitaria com doces e sobremesas incríveis. Bolo de vitrine e especialidades artesanais.",
            "latitude": -23.562559674925577,
            "longitude": -46.6529362971225,
            "coupons": 10,
            "address": "Rua Treze de Maio - Jardim Paulista",
            "phone": "(14) 2345-6789",
            "cover": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=400&h=300"
        },
        {
            "id": "4e6dd864-f04a-4711-9db2-e5624fd32b8e",
            "category_id": "146b1a88-b3d3-4232-8b8f-c1f006f1e86d",
            "name": "Verde Vida",
            "description": "Restaurante vegano com pratos saudáveis e saborosos. Comida natural em um ambiente acolhedor.",
            "latitude": -23.563839021677836,
            "longitude": -46.65801352185607,
            "coupons": 10,
            "address": "Alameda Jaú - Jardim Paulista",
            "phone": "(15) 9876-5432",
            "cover": "https://images.unsplash.com/photo-1511690743698-d9d85f2fbf38?w=400&h=300"
        },
        # COMPRAS
        {
            "id": "6dbf1cd5-c20a-4e6a-bc9a-a26069825d2c",
            "category_id": "52e81585-f71a-44cd-8bd0-49771e45da44",
            "name": "Loja Nova",
            "description": "Roupas e acessórios modernos para o dia a dia. Estilo casual com ótimos preços.",
            "latitude": -23.564580184943406,
            "longitude": -46.66202724389377,
            "coupons": 10,
            "address": "Rua José Maria Lisboa - Jardim Paulista",
            "phone": "(16) 3456-7890",
            "cover": "https://images.unsplash.com/photo-1504593811423-6dd665756598?w=400&h=300"
        },
        {
            "id": "756b1d53-cc5b-4995-8ebd-8eee3dae01af",
            "category_id": "52e81585-f71a-44cd-8bd0-49771e45da44",
            "name": "Tech Plus",
            "description": "Loja de eletrônicos com produtos de última geração. Gadgets e acessórios para todos.",
            "latitude": -23.56183474903135,
            "longitude": -46.66355095952655,
            "coupons": 10,
            "address": "Alameda Franca - Cerqueira César",
            "phone": "(17) 9876-5432",
            "cover": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=400&h=300"
        },
        {
            "id": "77a5d5eb-bcfa-4457-916d-a5b6fe7aa183",
            "category_id": "52e81585-f71a-44cd-8bd0-49771e45da44",
            "name": "Casa Luxo",
            "description": "Decoração sofisticada para casa e escritório. Produtos exclusivos para ambientes elegantes.",
            "latitude": -23.55870738391179,
            "longitude": -46.66172705741049,
            "coupons": 10,
            "address": "Alameda Santos - Jardim Paulista",
            "phone": "(18) 2345-6789",
            "cover": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=400&h=300"
        },
    ]

    # rules = [
    #     {"market_id": "012576ea-4441-4b8a-89e5-d5f32104c7c4", "description": "Disponível até 31/12/2024"},
    #     {"market_id": "2bc11e34-5f30-4ba0-90fa-c1c98f649281", "description": "Disponível até 15/01/2025"},
    #     {"market_id": "4197b830-aa9c-40d4-a22e-c05043588a77", "description": "Disponível até 20/01/2025"},
    #     {"market_id": "4209c72f-9d14-410c-91af-c24d08f177cc", "description": "Disponível até 31/12/2024"},
    #     {"market_id": "4e6dd864-f04a-4711-9db2-e5624fd32b8e", "description": "Disponível até 15/01/2025"},
    #     {"market_id": "6dbf1cd5-c20a-4e6a-bc9a-a26069825d2c", "description": "Disponível até 20/01/2025"},
    #     {"market_id": "756b1d53-cc5b-4995-8ebd-8eee3dae01af", "description": "Disponível até 31/12/2024"},
    #     {"market_id": "77a5d5eb-bcfa-4457-916d-a5b6fe7aa183", "description": "Disponível até 10/01/2025"},
    #     {"market_id": "78806cca-cfb0-45bc-8dc3-c57a42f0da01", "description": "Disponível até 31/12/2024"},
    #     {"market_id": "78ced7b1-436b-42ca-9c66-747f2b671321", "description": "Disponível até 31/12/2024"},
    #     {"market_id": "7be85f5b-533f-4974-8c9e-75cae740041c", "description": "Disponível até 15/01/2025"},
    #     {"market_id": "806c7934-037b-4dcd-99bb-c0fc6f2c5a45", "description": "Disponível até 20/01/2025"},
    #     {"market_id": "8cf0433e-68de-4c2a-9fff-c0c2941ec521", "description": "Disponível até 07/01/2025"},
    #     {"market_id": "b2c3014d-64bd-4c01-95e9-7f408e12ff6f", "description": "Disponível até 31/12/2024"},
    #     {"market_id": "b3a4dab2-1b83-4015-ba95-22f5770c6108", "description": "Disponível até 31/12/2024"},
    #     {"market_id": "bde73364-95c5-46e4-8084-79a7ca3824c4", "description": "Disponível até 31/12/2024"},
    #     {"market_id": "c5271f4e-6058-4eda-8b08-0e7fb0b73a0d", "description": "Disponível até 15/01/2025"},
    #     {"market_id": "d21b8cad-8d01-4ffd-8117-a34d613cdcf5", "description": "Disponível até 20/01/2025"},
    #     {"market_id": "def71683-e89f-4c3b-a652-868a02f54ae9", "description": "Disponível até 31/12/2024"},
    #     {"market_id": "e4949574-a579-4b07-a005-3fc4b7339752", "description": "Disponível até 15/01/2025"},
    #     {"market_id": "ea097b60-d0fb-41aa-ad44-a7ed850c9ecd", "description": "Disponível até 25/02/2025"},
    #     {"market_id": "ebfecf67-fe4d-4137-90f0-b7083fd58da1", "description": "Disponível até 01/02/2025"},
    #     {"market_id": "012576ea-4441-4b8a-89e5-d5f32104c7c4", "description": "Válido apenas para consumo no local"},
    #     {"market_id": "2bc11e34-5f30-4ba0-90fa-c1c98f649281", "description": "Válido apenas para consumo no local"},
    #     {"market_id": "4197b830-aa9c-40d4-a22e-c05043588a77", "description": "Válido apenas para consumo no local"},
    #     {"market_id": "4209c72f-9d14-410c-91af-c24d08f177cc", "description": "Válido apenas para consumo no local"},
    #     {"market_id": "4e6dd864-f04a-4711-9db2-e5624fd32b8e", "description": "Válido apenas para consumo no local"},
    #     {"market_id": "6dbf1cd5-c20a-4e6a-bc9a-a26069825d2c", "description": "Válido apenas para consumo no local"},
    #     {"market_id": "756b1d53-cc5b-4995-8ebd-8eee3dae01af", "description": "Válido apenas para consumo no local"},
    #     {"market_id": "77a5d5eb-bcfa-4457-916d-a5b6fe7aa183", "description": "Válido apenas para consumo no local"},
    #     {"market_id": "78806cca-cfb0-45bc-8dc3-c57a42f0da01", "description": "Válido apenas para consumo no local"},
    #     {"market_id": "78ced7b1-436b-42ca-9c66-747f2b671321", "description": "Válido apenas para consumo no local"},
    #     {"market_id": "7be85f5b-533f-4974-8c9e-75cae740041c", "description": "Válido apenas para consumo no local"},
    #     {"market_id": "806c7934-037b-4dcd-99bb-c0fc6f2c5a45", "description": "Válido apenas para consumo no local"},
    #     {"market_id": "8cf0433e-68de-4c2a-9fff-c0c2941ec521", "description": "Válido apenas para consumo no local"},
    #     {"market_id": "b2c3014d-64bd-4c01-95e9-7f408e12ff6f", "description": "Válido apenas para consumo no local"},
    #     {"market_id": "b3a4dab2-1b83-4015-ba95-22f5770c6108", "description": "Válido apenas para consumo no local"},
    #     {"market_id": "bde73364-95c5-46e4-8084-79a7ca3824c4", "description": "Válido apenas para consumo no local"},
    #     {"market_id": "c5271f4e-6058-4eda-8b08-0e7fb0b73a0d", "description": "Válido apenas para consumo no local"},
    #     {"market_id": "d21b8cad-8d01-4ffd-8117-a34d613cdcf5", "description": "Válido apenas para consumo no local"},
    #     {"market_id": "def71683-e89f-4c3b-a652-868a02f54ae9", "description": "Válido apenas para consumo no local"},
    #     {"market_id": "e4949574-a579-4b07-a005-3fc4b7339752", "description": "Válido apenas para consumo no local"},
    #     {"market_id": "ea097b60-d0fb-41aa-ad44-a7ed850c9ecd", "description": "Válido apenas para consumo no local"},
    #     {"market_id": "ebfecf67-fe4d-4137-90f0-b7083fd58da1", "description": "Válido apenas para consumo no local"}
    # ]
    
    with Session(engine) as session:
        for category in categories:
            
            existing_category = session.exec(
                select(Category).where(Category.id == category["id"])
            ).first()
            
            if existing_category is None:
                db_category = Category(**category)
                session.add(db_category)
                
        for market in markets:
            existing_market = session.exec(
                select(Market).where(Market.id == market["id"])
            ).first()
            
            if existing_market is None:
                db_market = Market(**market)
                session.add(db_market)
                
        # for rule in rules:
        #     db_rule = Rule(**rule)
        #     session.add(db_rule)
            
                
        session.commit()