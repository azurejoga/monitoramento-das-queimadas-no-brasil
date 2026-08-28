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

## Dados Diários - Página 170

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f73ce8d-18db-366a-8668-1e5b6a459627 | -8.54964 | -70.47549 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 15.7 |
| a9ffbdeb-6657-3901-87b4-fb6ea5c900d4 | -9.44507 | -70.44745 | 2026-08-28 19:08:00 | NPP-375 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 12.6 |
| aa738d97-c7e9-35a1-ae6f-04ca9540f604 | -8.82494 | -70.63173 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 35.9 |
| acb58002-994c-3d04-a1fc-9d5f7b37ac0c | -9.69985 | -67.34172 | 2026-08-28 19:08:00 | NPP-375 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 049ec461-2d55-3e2e-bebd-818b00c06356 | -8.80499 | -70.78886 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c0a6c41a-d860-3248-9ff1-6f7c3d446bda | -8.90217 | -71.39252 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 71437242-b304-320c-8479-2d0759f05d0d | -10.0464 | -68.98795 | 2026-08-28 19:08:00 | NPP-375 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0c824a05-7ced-3212-902a-91805b2608bb | -9.07049 | -71.94791 | 2026-08-28 19:08:00 | NPP-375 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 938cff34-8c05-3d1a-9112-b36f8a58317d | -8.658 | -70.75075 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 0da24a4c-6394-3bef-9865-cdadea6f8436 | -8.24383 | -70.09828 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a2309b75-80e3-3a3d-ba2b-57982373adbf | -8.45696 | -70.78883 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 0bc892c0-cc0e-3953-82ca-00c5f0cf8ac4 | -8.49925 | -70.31218 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6dde1f7b-19ba-3067-be69-1f368bc8ec7d | -8.95999 | -70.7124 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 2dc3d18b-d2ea-3f54-adc5-0d6debc2327c | -8.27247 | -71.14925 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 9.2 |
| c826f164-a683-38d0-b53a-e5f0d4a09efb | -9.42705 | -70.5817 | 2026-08-28 19:08:00 | NPP-375 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 13.4 |
| daf9f771-7007-3466-8738-e70f16f6a79c | -8.63889 | -70.51256 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 014eb825-57cd-3dc2-a6c9-25e6e9e86de5 | -9.15455 | -70.804 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ad47f4e1-098d-3d85-a8b9-706135e1a90b | -7.55023 | -69.9995 | 2026-08-28 19:08:00 | NPP-375 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 42a08ca1-b410-358d-a35e-851cacbffdd9 | -8.60187 | -72.91673 | 2026-08-28 19:08:00 | NPP-375 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f250f974-f189-3aa1-bafa-63c266b46ae2 | -9.23769 | -71.90623 | 2026-08-28 19:08:00 | NPP-375 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4ea7854f-d4b6-3efe-9000-be9e27987630 | -8.7171 | -70.79107 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 31315b0b-8253-3f1c-aa59-027b1bbddb70 | -8.93652 | -71.32234 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e37667ef-526b-359e-905c-12bdf81dc7bc | -8.90879 | -71.26509 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| db47ec69-1dbd-3425-bbe9-e9c1234789bb | -8.49004 | -70.73128 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 18fcb357-21ee-346c-9e83-780309ab4732 | -8.87557 | -70.56362 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3183a7d5-32ad-3bf8-93d5-ce06a2925154 | -10.38764 | -69.26232 | 2026-08-28 19:08:00 | NPP-375 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 0c51150d-5915-3d1e-9a66-9592a4c73767 | -8.25013 | -70.09709 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 85f4e8ee-5587-36aa-b8e7-c746d9522f00 | -10.0545 | -68.83154 | 2026-08-28 19:08:00 | NPP-375 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 0e7c6f94-4d5e-3ac3-a84d-8862ba6b46d3 | -8.60084 | -70.21523 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 44e500f6-994b-3ee0-bb3d-6ddb2106f7bf | -9.14252 | -71.90978 | 2026-08-28 19:08:00 | NPP-375 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d2626c37-6acb-3326-9b6e-2ff1f67aaad4 | -8.60268 | -70.21317 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4e7abebb-9f28-3408-b5cf-6c544f508041 | -8.63923 | -70.71686 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f284f347-2c35-3d96-8dd4-ebe3ad3bd7d5 | -10.52027 | -69.62421 | 2026-08-28 19:08:00 | NPP-375 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 228e1f58-a445-3694-9707-014e9745cb48 | -8.84717 | -71.28868 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 15.5 |
| da193435-0cc4-34ff-9d37-597117ef6126 | -8.21978 | -70.49724 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6667d2d0-3319-3f2b-b1ae-d286444f113f | -8.85635 | -69.31979 | 2026-08-28 19:08:00 | NPP-375 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 801f006c-92bd-372f-b60a-9744ae684a6e | -9.05495 | -72.26322 | 2026-08-28 19:08:00 | NPP-375 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9c588267-4bab-3861-9b22-3eb969dca334 | -8.40233 | -70.83612 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e292c949-eb14-37e8-9624-ae57438f7cd9 | -8.36224 | -70.74973 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 213ccc09-777d-34eb-96fc-7ce93459b5d5 | -8.38693 | -71.02194 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 8818c568-7704-3e83-aa45-2594f408e482 | -8.99116 | -71.26366 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8c51f8b6-3c77-3149-bdf0-f9fe0de19c82 | -8.67622 | -72.79168 | 2026-08-28 19:08:00 | NPP-375 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57282517-22b7-3c5e-a00b-6546c9e48c99 | -8.01095 | -72.05766 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 17d06f56-e5ed-325f-ae13-74d7a24a6597 | -9.1169 | -72.69715 | 2026-08-28 19:08:00 | NPP-375 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 46ac56a3-8c3f-34fe-905a-369a0ffff486 | -8.8036 | -70.78972 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 22917720-0548-3fd0-96b5-bb4b4bd74723 | -8.374 | -70.851 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 19.0 |
| fea9bb62-ea92-3bdf-ad79-039e05ffb388 | -10.19851 | -69.3544 | 2026-08-28 19:08:00 | NPP-375 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 21.2 |
| b67e87e7-d183-3344-845c-987818620b2e | -8.35694 | -71.05878 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 9d35d44a-9684-38d5-bbe8-dd008befd2c5 | -7.71695 | -71.42369 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9582efef-9276-3321-ae4f-24be9ea71677 | -8.80871 | -69.5284 | 2026-08-28 19:08:00 | NPP-375 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 124f114e-7461-3a8e-81ba-2e9339838ec4 | -10.05732 | -68.83375 | 2026-08-28 19:08:00 | NPP-375 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 18.3 |
| d29d3f0d-4d56-314c-8d9c-ec22207ef270 | -8.90759 | -71.26414 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| db1d5480-3d54-3331-8036-7e24d07e3cbe | -8.12659 | -72.07071 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 65b9feeb-b9e0-34d4-87d4-78e982dc504b | -8.00034 | -72.33839 | 2026-08-28 19:08:00 | NPP-375 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b5b06d7e-81aa-3485-a444-03601fe1d2d5 | -8.56667 | -72.41329 | 2026-08-28 19:08:00 | NPP-375 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 2efec548-e352-3e7f-bd81-6691388a60ea | -8.20319 | -73.03071 | 2026-08-28 19:08:00 | NPP-375 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 92dc0930-57c6-374b-bb71-437934dbce2e | -8.39366 | -71.02514 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 644058be-93dd-396f-af65-579bed2fa9db | -8.14431 | -70.63171 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 830c7d8c-94a1-34a6-a76f-89d03f14b928 | -8.45613 | -70.78435 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 02ac7b42-b7a0-31e3-b6e1-6887eb64de5c | -3.8947 | -60.9399 | 2026-08-28 19:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 936578f5-adf9-37d2-b08a-11075f001a09 | -14.9015 | -52.6055 | 2026-08-28 19:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 245.9 |
| 07e6a583-909b-3c95-b74c-f1989abb4c24 | -6.7832 | -59.4401 | 2026-08-28 19:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 14689611-e5dd-358f-9665-de255d13cd72 | -8.5975 | -54.715 | 2026-08-28 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 70e46028-8ea9-3365-8097-7d881839e63b | -4.1516 | -60.6878 | 2026-08-28 19:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 5f59097b-b081-312f-b5c3-92ead32fe9f8 | -4.3021 | -59.4826 | 2026-08-28 19:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 95.6 |
| abcd217c-12bc-3af9-a70e-5fb489735a62 | -8.5783 | -54.7768 | 2026-08-28 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 151.6 |
| 4e0ef4c1-93de-3a7f-b88a-5ba6da4f0100 | -9.9708 | -53.9419 | 2026-08-28 19:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 5404000f-1683-306c-86cb-eec3e81cf429 | -6.5863 | -55.4546 | 2026-08-28 19:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 1941ae57-4b54-3566-8ba0-98ce90f39cc4 | -6.8358 | -59.9379 | 2026-08-28 19:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| d9ffa165-0cd8-388a-a8ff-e973c84d62d8 | -9.1711 | -59.618 | 2026-08-28 19:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 09112fd7-2f4b-3b52-877a-4c1b6e536e80 | -10.3898 | -61.1925 | 2026-08-28 19:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 3fe5a604-3d59-35a1-a89a-87501f9da78d | -9.5889 | -61.0231 | 2026-08-28 19:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| a30dd0c2-bba5-366f-adf0-87ffd50fcb16 | -7.5845 | -61.3423 | 2026-08-28 19:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 239.0 |
| 91c4fd54-89e6-37b2-bd56-0ef8f2424697 | -13.471 | -57.0373 | 2026-08-28 19:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 23adc8d6-922f-303e-a04c-788fc59d800c | -6.8386 | -59.4379 | 2026-08-28 19:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 5f8eee24-05d1-30cd-9b0c-363434ac8b5d | -6.0005 | -57.6689 | 2026-08-28 19:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 37fc4b92-1be9-37fe-9527-c5673a3108b0 | -6.894 | -59.4164 | 2026-08-28 19:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 819a54c2-ca39-3b9b-993a-ff1d87a6060c | -11.6212 | -54.5947 | 2026-08-28 19:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 5ae3b10a-1bfb-349a-8cfa-4d02816ec81b | -14.8821 | -52.608 | 2026-08-28 19:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 179.2 |
| fd4f52e4-8146-3a79-87d1-a599f007cdd3 | -8.5365 | -55.2826 | 2026-08-28 19:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 930f5037-e41a-3371-a9d2-175407432414 | -8.5785 | -54.7566 | 2026-08-28 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 83c29c07-6264-305e-aa37-eca1f3853998 | -14.9 | -56.3257 | 2026-08-28 19:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 2c6f80ce-9474-35db-9752-70eb7e59c963 | -14.3376 | -51.702 | 2026-08-28 19:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 9bb75cbf-6c53-314c-a957-b3e530f71649 | -10.4499 | -46.2052 | 2026-08-28 19:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 56a24ec1-4d57-3ff1-8ab6-83760adb4673 | -8.8184 | -49.6308 | 2026-08-28 19:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| bcd14595-3c3f-34ee-85eb-67b92159a3b3 | -14.1784 | -48.7703 | 2026-08-28 19:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 88.9 |
| f70d90df-14b2-37a9-a32a-59accd07b216 | -14.1838 | -52.8245 | 2026-08-28 19:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| d839a5a3-e02f-3679-9789-25b7da751b4d | -9.7874 | -43.5742 | 2026-08-28 19:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 596b24da-bbc0-328c-8eda-f60a43cf5f7c | -11.2128 | -53.9976 | 2026-08-28 19:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| d91d1140-359e-3638-a0c8-6ec4bfa918fb | -11.0247 | -49.6656 | 2026-08-28 19:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 580846fb-1588-39eb-a3b4-4e6fc1a06a11 | -9.4329 | -51.6926 | 2026-08-28 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 5b4787cb-0a24-3fd7-811a-923482036506 | -7.9169 | -61.3671 | 2026-08-28 19:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 25c33d4d-1e5f-332a-bee9-8a87c5e76095 | -10.3013 | -49.9801 | 2026-08-28 19:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| f935076f-2e72-338e-835f-4f59c42f2e7e | -8.0548 | -45.8616 | 2026-08-28 19:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 982b57ce-129d-3cf7-ae11-a86d9458e84f | -6.9145 | -43.6351 | 2026-08-28 19:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 130e2e30-ac89-3e3c-816a-3b62371228e6 | -8.631 | -66.5473 | 2026-08-28 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 950d72d2-5794-32da-8895-09f66987a5ac | -4.3022 | -59.4634 | 2026-08-28 19:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 4b8b7c2e-4149-3c56-89ca-9aa917420881 | -14.1645 | -52.8269 | 2026-08-28 19:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 5ea6ce84-81f9-3ecd-9818-c69503eac838 | -14.5448 | -51.9943 | 2026-08-28 19:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 1320c8ca-0736-3082-889d-65348e5b4f53 | -14.9193 | -56.3237 | 2026-08-28 19:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 156.9 |


[Clique aqui para ver as próximas entradas](README171.md)
