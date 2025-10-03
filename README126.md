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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef55be62-8065-39bf-814f-5f9f0636305d | -15.17364 | -43.62929 | 2025-10-03 04:34:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 36b15fb9-f73e-3d0f-a98f-f50c64d1125a | -20.13233 | -44.01322 | 2025-10-03 04:34:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b308bbf5-6d67-3300-afb9-61df1c6e7f51 | -14.11648 | -45.65729 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 578e9618-c665-31c7-9398-53e50233229b | -19.71875 | -47.21939 | 2025-10-03 04:34:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42752a3d-03bf-30bb-8d43-0d407c11f1c3 | -13.55313 | -47.58676 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e912abdd-e27d-3598-bd69-d420ec612f94 | -13.13977 | -47.8946 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 049924d5-c099-3f4f-a947-338c4eb49530 | -17.09379 | -48.56165 | 2025-10-03 04:34:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3352d33e-dd7d-3ebf-b167-10d01bd886fa | -12.82224 | -46.91105 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c25dbf62-7622-336b-9460-5397b2fdb359 | -20.00364 | -44.18913 | 2025-10-03 04:34:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 62218cc5-708e-3ff1-beeb-7f8b2f02079f | -13.20876 | -47.82646 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3c83187b-b5b3-37ad-9c1a-a186e943160b | -13.12366 | -47.85469 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 128accfb-2301-3fc9-9e97-330c60de053a | -14.85821 | -48.28254 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e5402325-0d5c-383e-97b0-fd2fb7509b6f | -14.30103 | -45.8842 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83efcd56-5cb5-342b-9355-b237b51e286c | -13.47984 | -47.25685 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecf374be-2cc6-32bf-8ad4-e5fb312b0f88 | -13.97959 | -48.12573 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0adac0a0-88f2-3ea2-a012-a94049c2a23f | -13.33948 | -47.79464 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b83e8f83-df6a-377e-87c9-72c5c4b483b9 | -13.122 | -47.86555 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83654743-a641-3179-86a7-f35be738da64 | -15.48286 | -45.92862 | 2025-10-03 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0cd8ba8c-3082-392e-9b3d-d5eb80eb29a6 | -14.67933 | -48.07621 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2da77470-05ff-3d46-a757-e3ad213b1486 | -14.89861 | -48.28905 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e7645e3-3e40-3da1-8013-cbc8b48ea611 | -14.89888 | -47.82554 | 2025-10-03 04:34:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a297c841-28f9-39e5-be69-0445b0a8215d | -14.93974 | -46.87714 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b229e91-bf64-3271-915a-f7c51f4ee4c3 | -12.60644 | -49.89769 | 2025-10-03 04:34:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81a66c49-e8e3-3930-ae0f-8c9167464c9b | -16.41108 | -52.15561 | 2025-10-03 04:34:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b4bae98d-43a7-3c70-ae67-a8e49f70756d | -15.21631 | -47.18526 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90611216-d902-3733-9076-7fc4c3c20da9 | -16.04803 | -50.91529 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c31890c5-2ebe-3d76-a8a7-eaf266d305e6 | -13.33931 | -48.10048 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff14c427-436a-3583-92d8-83e69f44701f | -14.65255 | -48.29882 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0c5dd1ed-1ded-3fff-b4ca-13153fe34a4b | -13.93193 | -48.08881 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b759f70-ed33-3bdd-986e-b94d8fc60ed2 | -15.21979 | -47.18595 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 477081ce-7dab-3855-8eb2-4003db696a4d | -13.31542 | -47.18921 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c9a976e-f73b-34df-a4c4-030e0ffd5212 | -14.28644 | -45.91704 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c592f85-c286-3144-a308-2b7c914387ef | -14.90027 | -48.34599 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06065311-0779-39b4-85f4-6ec03ba26a11 | -14.70929 | -48.1981 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b61f0270-e351-303c-b485-c423f61b283e | -14.85336 | -47.21835 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5087acf3-06df-3641-bbfe-f5c5830507e3 | -18.22368 | -53.36355 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98b1385d-18d8-3fb0-9a9a-37050838b9a5 | -12.99298 | -47.75029 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 459e9249-4dba-3da1-922c-d4033c5e0a88 | -13.14088 | -47.88729 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7e302e1-b0d7-304c-b7ce-6d6187254544 | -13.54134 | -47.29301 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ec8e2133-0bad-354a-b2d7-4a5026cf3960 | -20.13068 | -44.00599 | 2025-10-03 04:34:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 7f433d89-6905-37e6-84e8-c9317aa16127 | -12.62329 | -46.95691 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34c27543-798c-321d-9bf7-2a704cf960ab | -13.33544 | -48.12596 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b263c80-1410-326c-b2ae-99213ac36c17 | -12.59417 | -49.89276 | 2025-10-03 04:34:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86dc5011-ee33-36d1-a3e7-31e2984eae17 | -18.64866 | -43.87503 | 2025-10-03 04:34:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15dbb039-b540-3d4b-8505-d32dc87360b6 | -13.58718 | -48.19132 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 300b5f02-08ce-3ffd-ba3d-394e5dc62866 | -12.71916 | -48.58332 | 2025-10-03 04:34:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16309954-fc28-3137-b188-c732be8bc407 | -13.76416 | -48.04693 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 510df674-5191-3e3f-91e2-75287c6fb23d | -13.30716 | -47.59513 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ac12e79b-15ad-3f2c-8509-61c28775c8ca | -12.60543 | -47.005 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e97697fd-e545-3128-8696-07c356454ba2 | -13.14921 | -47.83191 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6983d7b-3e69-3e86-8460-47aec8ca219f | -13.24208 | -48.49558 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 540ee0fb-2985-3f0c-9459-4fdd344bba08 | -14.72967 | -48.11797 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67944218-f7fe-309c-9715-f7629fc6b58d | -12.80325 | -47.01416 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6dca15cf-28f8-38ab-90ed-433287f9c404 | -13.49342 | -48.57914 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5499b2cc-9e71-3a2d-90c0-41c2637d666b | -18.46276 | -49.44133 | 2025-10-03 04:34:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79695a9f-5ce4-3d31-98c0-bf55989138f6 | -20.27141 | -44.79098 | 2025-10-03 04:34:00 | NOAA-20 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7df82589-2eb7-34e3-8424-522b84be396c | -13.94877 | -48.1366 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb888ed1-7635-3f05-98dd-7101d43415e5 | -13.45474 | -47.2598 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f87bb11f-3112-3c77-ae40-fda3236dee0c | -16.87508 | -52.80055 | 2025-10-03 04:34:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1b0947c-ea18-3d15-aa68-04834472839b | -17.51789 | -43.48352 | 2025-10-03 04:34:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd05686a-bc16-3497-9dbd-3ae1d019c68d | -13.79147 | -47.58336 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e74c65d2-ad81-3dca-9d91-a8c618453bb6 | -19.02014 | -48.48463 | 2025-10-03 04:34:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d638b772-3447-397d-be4b-92ca5162bf85 | -13.66845 | -47.30413 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5d399a6-ab44-3d51-b4ac-aeb54f17a9c8 | -13.12368 | -47.87711 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5185ffd3-8a6b-3c56-bab6-98c61cfe80d8 | -16.33304 | -49.94017 | 2025-10-03 04:34:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d5ba58b-a3af-386d-ba9a-866ebe335559 | -12.92618 | -46.3788 | 2025-10-03 04:34:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb2d69f2-1367-3945-8ce1-ce93746d43de | -15.27343 | -47.91709 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e2a1917d-f72d-3813-b1bf-9dcf89e84197 | -13.21535 | -50.89628 | 2025-10-03 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d656afec-7e38-3467-84af-4b64286f5211 | -12.62625 | -46.9519 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9da58de-4324-3c70-bcde-212473b11a7b | -18.22797 | -53.33839 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7994399f-8de8-30b6-92c9-8f24cbc362e4 | -12.67983 | -46.85294 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6e22ad2-3c06-3e22-ba19-800396b4f68d | -20.38506 | -44.09045 | 2025-10-03 04:34:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cd7e4428-4139-31c1-b513-7d21bcf1164e | -12.83153 | -46.94366 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75f6b903-0b59-3a5e-817d-f959fa746941 | -13.77097 | -47.58027 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f9672f91-b4d1-3919-81c1-ec1da979d41c | -16.01313 | -50.86068 | 2025-10-03 04:34:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 725863ef-12f6-377a-b79c-c3e66b832a7c | -18.161 | -53.34621 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e5029b44-007b-3d4e-be4e-fff1dd2c2fa3 | -12.29884 | -46.88036 | 2025-10-03 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e76d045a-df8e-382a-b65a-06fb4df74446 | -15.98802 | -50.86768 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 510b65fe-116f-31a8-b28c-ecf5b2222f7a | -13.20095 | -47.80967 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc28442f-e80d-390f-a24f-e8cc0a751aba | -13.95551 | -48.09254 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ded1b78-60e9-3073-98d4-638760b9bcf1 | -13.97687 | -48.16651 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c044597f-39d4-3018-8bdc-5adf91820b16 | -14.5993 | -46.71489 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1a41cce-17e2-3c85-8d01-4528d4e04234 | -12.81072 | -47.01146 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bdcc3b74-576a-37b8-bf9e-44afb18634b2 | -12.19219 | -47.81815 | 2025-10-03 04:34:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e9fb0f0-f064-357c-b1eb-6004b5291205 | -12.59474 | -49.88921 | 2025-10-03 04:34:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6291c7a4-55a8-3c9f-81c3-974acdba5331 | -13.54952 | -47.30473 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9e718edb-e509-3896-bdb5-33bdd9fbc3f7 | -12.62862 | -46.98372 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| d1478273-8625-3c02-a1ac-5de08072caed | -12.90786 | -46.36028 | 2025-10-03 04:34:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a91527d-d80e-3382-a7d0-dd4723fa4c68 | -16.36687 | -47.01244 | 2025-10-03 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8285b5bf-703d-3408-8578-7f674eec7384 | -14.89313 | -46.97418 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2c07993-17ed-3ad5-8a61-c0274cddd448 | -19.46443 | -43.64825 | 2025-10-03 04:34:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3726f329-6ffe-34d5-aa34-1202b6370dbb | -11.20369 | -54.08992 | 2025-10-03 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 680496b0-f997-39ff-baf7-215ad635e11a | -13.77204 | -48.06331 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c5fc3ecd-b328-3642-9750-d7ff9956e7f9 | -13.20267 | -47.33543 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a13e2f2b-dfd0-3ea0-9aee-bfa043fd1fdb | -14.68667 | -48.09646 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57964a33-8c13-34bd-953c-565f9c9dea55 | -16.93364 | -54.14933 | 2025-10-03 04:34:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 29ecff6e-9453-346f-8699-cfc14dddc6bf | -14.90979 | -48.35127 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57bb6993-a9c0-3052-8e58-c9881897f352 | -20.13018 | -44.01039 | 2025-10-03 04:34:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| bef0c568-6889-3a84-99eb-6c969844ecf6 | -12.90277 | -46.93074 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c6e183d9-2214-3180-ae48-9be8fb057c3a | -14.29839 | -45.88662 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README127.md)
