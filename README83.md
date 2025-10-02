# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 133a7c89-0f11-338a-b2b0-3cbcfaae736d | -15.46127 | -45.88232 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3273d65c-c79b-3c68-8710-d6459754b8b4 | -12.28205 | -45.37234 | 2025-10-02 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83a14bb3-e35d-3c65-8c86-306a7d7328e1 | -14.87161 | -48.29553 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 21b7bb19-a039-32d8-b241-5e908b1cfd6d | -13.16339 | -47.80313 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e263f284-a4f3-3599-9fc5-df3f34313ab7 | -14.28698 | -45.97312 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf187d3a-9cdf-3cd6-af8a-1cc1f4fe0f14 | -12.79749 | -46.85658 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0fe4e344-0ebe-39db-82e5-b59fd291ace5 | -18.63188 | -50.68732 | 2025-10-02 04:32:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02974d2b-bf5f-34b5-81c8-7ae9dbb8b20e | -12.69112 | -48.57633 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bc6adfba-a46f-375a-87d0-87dea0fdafa1 | -12.82473 | -47.02617 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d73664e-1058-3a4e-b24a-f3c13ba45973 | -11.91353 | -47.88297 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f99146b5-ece9-37d7-ba6a-fe846010f304 | -14.45088 | -46.34685 | 2025-10-02 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2d9af0c-5ab2-3111-bd80-b3b9ee56c4df | -13.41169 | -48.19708 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ff46784-db0e-38d3-9ecc-6ef6e300834b | -12.85631 | -46.86598 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40b4db3d-e8cd-3105-99c9-f023d965094b | -16.14038 | -46.66963 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4cb9649-5d29-343a-9c33-7266a9df2610 | -14.30661 | -45.88823 | 2025-10-02 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99053304-104a-3867-8d66-5a875fcb1b2c | -13.74877 | -48.71076 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d2dba573-f56f-3613-8801-2d501b5954d0 | -12.65585 | -46.87483 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8a18f97-7064-3606-834c-b6edc5408f22 | -14.88813 | -48.12597 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e7fd33e-1665-3344-9e6a-cfe244afc986 | -13.43703 | -44.22801 | 2025-10-02 04:32:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 479b5307-eccd-34e8-9634-7066e4010848 | -14.68846 | -49.61256 | 2025-10-02 04:32:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 769be220-5683-3c3b-9736-229144520bc4 | -15.23556 | -48.73067 | 2025-10-02 04:32:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17ab64a5-b812-3ce9-8b09-7f0990fd64c8 | -15.26402 | -49.30229 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 214d0de5-64d4-3287-b72b-8103936dcedd | -14.22468 | -44.78682 | 2025-10-02 04:32:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95dcc607-3f50-36c8-8376-f47bbeb2e467 | -14.58305 | -46.71666 | 2025-10-02 04:32:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b16fd8f2-0ec4-3e7d-847d-a82c79b72883 | -14.4774 | -48.40942 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b5148b90-2921-3fd9-916b-8da841bdb7f5 | -16.14215 | -46.68141 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aad18390-b7aa-3f7b-b50c-1651e239ba84 | -16.13982 | -46.67339 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66871a88-e10c-3564-aa12-9c678d36eec3 | -12.49535 | -50.2425 | 2025-10-02 04:32:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a5c87223-a78d-376a-8626-82d8ae48ec2e | -13.17002 | -47.82607 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f4c5e34-bc70-30f1-a24e-38d84483b30b | -13.76719 | -48.00411 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91f76e3a-9a9e-3c3e-9e08-71ebd114006f | -14.41208 | -46.09439 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca5c210a-0198-3b9e-ad56-d9c9a8f9bdff | -14.68427 | -48.11096 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca9a2931-f510-33f0-afa2-bccb82a0220c | -14.29911 | -45.96307 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 391cab2e-a78f-3106-a494-49a9169fbd65 | -13.68304 | -48.06636 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4377f8ae-21bb-3656-908a-6111263130bd | -13.79374 | -48.05232 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f203133a-e818-3db5-bfde-c70882b6e0f4 | -14.21291 | -46.12395 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 987b1659-c228-3368-811b-56caebd2a4ce | -13.93874 | -48.09392 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1875ee18-fc55-347b-972f-838d1a204336 | -13.31672 | -48.74618 | 2025-10-02 04:32:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1aa67595-b1ce-375f-851c-41564f66b7c7 | -13.14556 | -47.85117 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7400f2c-a7d2-39f9-84bc-879b74db1e4d | -12.25252 | -47.82935 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa48d278-0400-3fc7-87ff-4525d4d253a9 | -13.74047 | -47.91901 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2d8a70fb-1fa0-3fd8-bb8d-327346f7a7d0 | -13.53584 | -47.25359 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cfdce878-11a0-313e-bdfe-c6c0688386c4 | -13.75556 | -47.99124 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 05d182ce-10e5-3828-a9ef-654a135b3801 | -14.50599 | -48.48754 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 754d4c7d-faed-3100-bbce-8bdcd04498d4 | -15.3074 | -46.39381 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d93fe492-3c81-3519-b4bf-466577ca630e | -15.6972 | -46.25769 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 153a21a0-be0f-39dc-97b6-27b9926118c5 | -13.31599 | -47.00122 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65519054-0275-318f-81d1-0771803461c7 | -11.87879 | -51.227 | 2025-10-02 04:32:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28af464b-1755-3e18-baf4-7309c24f68f1 | -15.22052 | -47.17951 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 25b264cd-36a1-3c09-ade8-7d3c1edd7a05 | -12.89544 | -46.92394 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0efee8c5-b6f5-346d-a7a2-20123e292616 | -15.54816 | -48.17931 | 2025-10-02 04:32:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4e13b53b-3935-38fa-b9a1-4bf07cea3b3b | -14.31819 | -45.8821 | 2025-10-02 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 519cda2b-54c1-3f7e-aace-c8308a6d52e8 | -15.33501 | -47.94923 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d728837-add9-3a2b-b05e-359509e6cd82 | -12.6659 | -46.87646 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e014d6d-371a-3274-b5be-c65a0848c939 | -12.27857 | -45.37181 | 2025-10-02 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b90a06f-25e5-31c4-92e7-85948a4b3015 | -19.72121 | -45.89393 | 2025-10-02 04:32:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8f5c0eff-6904-3974-a5d5-656a67c861d7 | -13.96362 | -48.1309 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2f95fbbd-a252-3dd1-95c8-db6c7fbc09f1 | -12.19906 | -47.80551 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b08cbaa-2f55-3c40-98b5-2d580cca1866 | -15.28106 | -46.40505 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7073dc1c-5452-3f2c-8e30-b802e1226115 | -13.42812 | -47.79942 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 254636ff-6005-39d9-aa76-3c65b009b9eb | -13.771 | -48.0449 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a71ffaa-3c5f-3d41-aa6e-52355e58c243 | -12.70611 | -48.58994 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c39bb5ff-0943-31bb-a40a-c91c12863793 | -15.24543 | -47.89427 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 559ae227-07ab-3358-98df-fc851fea08dc | -15.55205 | -48.17628 | 2025-10-02 04:32:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2e18fc41-68a3-3898-9634-ae802b78752b | -12.18018 | -47.81689 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94bbbae5-cf22-3ba5-89b7-ce8a82c9994f | -16.04061 | -50.8571 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| bd544b78-ef61-33e6-9012-ae371ac0f2e7 | -15.94766 | -43.32208 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 716bd1ee-f8a7-3384-bb8a-a45bb1cc7da6 | -17.11492 | -47.11703 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2ca58a2-d82b-3a32-a50f-b3a7b7cfff2c | -12.50055 | -50.25469 | 2025-10-02 04:32:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aafb1b83-68ae-314c-9d71-eb513657d935 | -12.8671 | -47.0183 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f87bcb35-169e-3bf0-ae94-24e8f42a4593 | -17.17979 | -47.03238 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 26.3 |
| ac83d1e8-ea29-3270-bfda-b6de9e29ec22 | -17.96403 | -45.04512 | 2025-10-02 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d659e806-2c56-3a0c-8e94-37e6822baa3f | -15.39823 | -47.0451 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3dfbb883-7cc3-38c4-931e-80793518fa47 | -13.36573 | -46.63326 | 2025-10-02 04:32:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d24f31e1-e7bb-38d6-80e5-fbc3922e673f | -13.23953 | -48.51252 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a705bd64-3d60-35a9-90f8-619ae72c7427 | -14.48455 | -48.42893 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 495343e7-fd39-3b35-b551-4e9067f06487 | -13.16056 | -47.84271 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b9d4dea-be08-30d6-b2e3-96f4020d4528 | -14.69462 | -49.61741 | 2025-10-02 04:32:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 559f0123-2bcf-3f22-849c-5d957aba9efe | -13.86266 | -47.9538 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e7130a6d-8ed8-355f-96eb-10f9bc46c052 | -11.58617 | -50.1713 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0d9a1155-3a6a-31e8-bcde-5a27f4f398bf | -16.49936 | -46.94697 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d83b97ea-b85c-331b-823f-33ea8ad96c65 | -12.68456 | -48.55315 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e3f0c9c7-409f-36d2-ac42-ac65ace9da9a | -15.15718 | -48.39054 | 2025-10-02 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e8553e8-ecf6-3853-91cd-018b1edeeacb | -12.26475 | -47.81684 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 661038f6-6ed4-328b-b527-b454511dd8d1 | -15.27762 | -46.40449 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc8e905f-3a77-36e5-aaff-60e7c4861136 | -13.40651 | -47.78494 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39b40851-7d57-38df-bdd6-9df9daa07f3f | -14.58806 | -48.20116 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6d27f3b-617a-31f0-b71d-cf365b58af2c | -14.90038 | -48.09139 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12e296cc-725c-3052-b04e-bae08afdd1c1 | -17.01781 | -49.14942 | 2025-10-02 04:32:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d71a42d-b64b-33de-a42b-78456845055b | -13.67531 | -48.05049 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26cf68d9-cc4b-34ab-8f15-e31dbff6dcf7 | -13.78708 | -48.05122 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 973d8e57-287b-3c50-84db-b50b49e44ace | -15.34759 | -46.28946 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9928f1a1-feb0-31a0-a4bf-cf1dfc3e2c00 | -13.29918 | -47.19783 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10503cae-80b6-39c1-a014-00b6a48ed6a0 | -14.02383 | -47.98751 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0443eb99-e5f9-332c-9c24-b35ba2eaf0aa | -14.32573 | -45.87928 | 2025-10-02 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a07ffeff-6518-3ed2-81bc-d9991c17541e | -13.30462 | -47.85212 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aa928af4-057b-3502-8d88-791d01fce81f | -15.92903 | -43.338 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 5ec3595b-9e5d-31bf-9c39-f72f761a2b8d | -12.80083 | -46.90152 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c697125a-878e-35a7-8076-68441cb9f85e | -14.68228 | -49.6078 | 2025-10-02 04:32:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9fa67bb-5aca-3930-95cf-8e9b3d6703ec | -18.4318 | -46.53307 | 2025-10-02 04:32:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README84.md)
