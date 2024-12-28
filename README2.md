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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac343227-5bd2-348d-a55c-03c45bb79aa8 | -3.8804 | -47.016602 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 849d1e11-6eaf-3999-9481-5ec68997da4f | -3.2029 | -45.9856 | 2024-12-28 00:21:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 781e8d21-91ed-355b-98f7-64daba9dac4b | -3.9133 | -46.9799 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 00242d52-2940-3c9e-9011-85ec44de3f46 | -4.7584 | -44.6353 | 2024-12-28 00:21:00 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb240ee4-75a3-3acb-84c0-8118c5960e2a | -3.9993 | -46.723099 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 601a9d4f-fc1a-349b-a441-eee43bd0e4f6 | -3.5351 | -42.599899 | 2024-12-28 00:21:00 | METOP-B | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b01d684f-2503-3008-87d9-91df8493e425 | -3.7405 | -47.172699 | 2024-12-28 00:21:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31250b75-c0e2-38c4-b45d-b05738798f1b | -5.3227 | -46.062199 | 2024-12-28 00:21:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 293d3a65-b757-31c9-ba48-20cdab13a345 | -4.0532 | -47.051498 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9dc8419b-e8b4-37ef-a5a3-c290ed219eea | -9.26 | -40.9515 | 2024-12-28 00:21:00 | METOP-B | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b89b7914-44ec-3200-9707-2ae425850cc3 | -3.7833 | -46.8162 | 2024-12-28 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0aa2fe82-edcd-30e9-898d-5cb99d6281c9 | -4.7289 | -44.462898 | 2024-12-28 00:21:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d00bdb43-bdbc-3a59-aabb-242f1f0c224f | -10.2162 | -42.224701 | 2024-12-28 00:21:00 | METOP-B | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 22d49252-8a47-38cf-a4fa-15a326681f0e | -4.0173 | -46.711601 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6af28e52-3936-3ab1-bf63-a5c3bd0caf35 | -3.9665 | -46.760201 | 2024-12-28 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5d0744d7-8c3f-339a-9654-ce77fc88ecf8 | -3.7437 | -47.186699 | 2024-12-28 00:21:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b6b60a4-ebe8-3057-bfd6-181d70bd7a31 | -3.955 | -46.755299 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8e8448ce-69cb-3e38-ac3a-cc2c03f1e696 | -2.7479 | -46.0238 | 2024-12-28 00:21:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 06b74076-9e8a-3b7c-a294-c5ef08816630 | -2.0104 | -47.4044 | 2024-12-28 00:21:00 | METOP-B | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96fa9a38-1612-3747-92df-639187dd5e2f | -4.001 | -46.685299 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 49480bc6-20ae-3fc8-b3b5-6dcc2c7a0d9f | -2.7231 | -46.005299 | 2024-12-28 00:21:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 66c76e27-c924-333f-8736-fb91e661f606 | -4.7564 | -44.6269 | 2024-12-28 00:21:00 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df852041-6424-3544-89df-def94a70d6bd | -3.9766 | -46.668301 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8b15b3dd-f724-348b-8ecd-45302fee49aa | -4.7486 | -44.6376 | 2024-12-28 00:21:00 | METOP-B | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| abccf4d6-6530-367f-89aa-098541ad5cdc | -3.9231 | -46.977699 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3f0a914b-818c-3534-a4de-5b2e702c0e10 | -4.7191 | -43.442699 | 2024-12-28 00:21:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00ad29c2-faa1-38ea-ad78-e6b0e9858f7b | -3.7795 | -47.208 | 2024-12-28 00:21:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 986ed40e-2bd8-3446-86cb-105022c3413b | -3.7134 | -41.692001 | 2024-12-28 00:21:00 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cb3b262b-d13c-31b8-9161-d1052f7ebfe2 | -4.7211 | -44.473701 | 2024-12-28 00:21:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e985679-c79f-3729-8310-3c2a7c3a6ef2 | -4.05 | -47.037498 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 73edb8a5-46bd-3e29-a26b-50bec5b332da | -3.8572 | -46.6875 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e2aa3bb5-ecf6-3634-9780-124fd7fad04c | -3.7551 | -47.191502 | 2024-12-28 00:21:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d3d972b-4be1-3d8b-99d2-276f396de8b7 | -3.9148 | -46.9869 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| baa880e5-aa2c-364c-b619-f23899bb4ce9 | -2.9242 | -54.478298 | 2024-12-28 00:21:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e77fbf45-6879-30b6-a615-2b602e44a6d7 | -4.0305 | -46.5434 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 82e24304-b175-34da-a692-facdffeb1908 | -4.7191 | -44.465099 | 2024-12-28 00:21:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73a7c1bb-8f75-3609-8f14-3e55575a81e3 | -2.9187 | -54.453602 | 2024-12-28 00:21:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f45bb286-9fb4-32dd-8a13-500740c7f36f | -3.8458 | -46.682598 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 67fbc3c0-cdd3-38d9-827d-02d4e9b88fe1 | -3.9667 | -46.670502 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 76eb66cf-475e-361c-8574-4eb8e7d008dd | -3.7473 | -47.339199 | 2024-12-28 00:21:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e0914bd-22cc-3729-bb8c-c16ec8b15251 | -3.7535 | -47.184502 | 2024-12-28 00:21:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1083ed7-2fbc-31af-8386-85b602ad9be6 | -3.2141 | -45.493301 | 2024-12-28 00:21:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b65ab9c3-cbba-3d57-96be-5c464df23f4d | -3.2127 | -45.983398 | 2024-12-28 00:21:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a2129260-d80d-351e-b5c5-c24ea1af2c5e | -4.7466 | -44.6292 | 2024-12-28 00:21:00 | METOP-B | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c2ae1ef3-6196-37e9-aacd-18399a56761b | -5.5843 | -46.125099 | 2024-12-28 00:21:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dec31281-0d39-336c-b2f7-2927888f5fe3 | -3.854 | -46.4921 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 68b3782a-34bf-3131-b7fd-da11af14d6cb | -10.0487 | -36.177799 | 2024-12-28 00:21:00 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b236242e-03ca-333e-94a6-b16e9db59369 | -3.9035 | -46.982101 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| abda2c4c-4218-32b3-9e15-587a1b0ae75b | -3.7519 | -47.177502 | 2024-12-28 00:21:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddbbc689-1989-3154-b1b3-5190164c685e | -4.0026 | -46.692402 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1473411d-3141-3611-a866-ac44306c52ee | -3.8311 | -46.708401 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 60b4bc60-4794-3d70-a1bf-2cd4873abcf7 | -3.965 | -46.6633 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a234f6cf-0222-3de4-bbe5-d11baf9afc25 | -4.1317 | -46.671001 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e61fbd8c-a9f7-3964-b63c-74cd0e4cea36 | -2.9117 | -54.467999 | 2024-12-28 00:21:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2351920e-0157-3884-8941-3910d279fc84 | -2.2318 | -53.6199 | 2024-12-28 00:21:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57da73fc-ee4e-3d99-9bc4-452269dc6d86 | -3.1087 | -46.567902 | 2024-12-28 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cbe132cc-b73d-3325-b1ac-9519d22bdffc | -3.8556 | -46.680401 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| db8b4e95-60f4-3435-8ca8-255545c0fab1 | -3.7713 | -47.217098 | 2024-12-28 00:21:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09021e95-db49-3a4f-bcd3-497f30826913 | -4.1333 | -46.678101 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 025778ec-c28e-393d-8434-424226a9d464 | -2.7462 | -46.016201 | 2024-12-28 00:21:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8df29858-c3a5-3a87-834d-096ff36ee143 | -3.6998 | -47.1745 | 2024-12-28 00:21:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1908d1b4-735d-3255-b34d-202dd5d9f113 | -2.4575 | -49.019901 | 2024-12-28 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2726c6a4-d96e-3290-bc4f-52ec53f6c5ba | -2.4026 | -51.898602 | 2024-12-28 00:21:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b41e4e01-da60-3df4-9a07-ace078d7b7ba | -4.0418 | -47.0467 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 79058448-7982-3d04-b381-f9a360936b21 | -3.1929 | -46.1227 | 2024-12-28 00:21:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b5c52898-e96c-3a25-a677-f5150c54a7a3 | -4.1315 | -46.715801 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5bc1740f-4e2c-3f9e-8951-d5ada5cad1db | -3.0973 | -46.562901 | 2024-12-28 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ea0f1b52-a4ff-3ec9-abf7-4838f26ea518 | -4.0921 | -47.0868 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5ea37c7c-b7fb-3ed7-8e5a-aa18543f3d67 | -5.2451 | -41.388 | 2024-12-28 00:21:00 | METOP-B | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0d235283-6ca6-3937-a134-b9d2e55df368 | -5.9466 | -39.6838 | 2024-12-28 00:21:00 | METOP-B | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| bc48ddaa-b7de-3d5f-bb8f-2db686419150 | -10.0551 | -36.2024 | 2024-12-28 00:21:00 | METOP-B | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b035058e-aa25-332b-8c82-513ecb01ba3c | -4.0107 | -46.728001 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7bd36c30-bd72-3056-a40d-a40f03aa1122 | -3.988 | -46.673302 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c5990a5f-8b5c-35bc-903e-841915cc49a2 | -3.9185 | -46.912201 | 2024-12-28 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e13bf6be-4f2b-3441-957f-4d8b21994451 | -5.9222 | -43.477699 | 2024-12-28 00:21:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e5e28af8-96d8-30e8-81d3-fa5a8443795b | -11.2598 | -44.476501 | 2024-12-28 00:21:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ee40331f-ea87-3880-88d8-5ae58f389961 | -3.9856 | -46.889702 | 2024-12-28 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e431f3ea-07cd-387b-b4e6-a8e251403088 | -3.9986 | -46.9016 | 2024-12-28 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9b518c19-5095-3e4a-8b2a-eb4914d1f819 | -3.9994 | -46.6782 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bbfa0ae8-0dc4-3eff-a201-de1b97f28302 | -4.3737 | -46.466301 | 2024-12-28 00:21:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4561b63e-8e69-32ee-968c-bd1f6923e1a3 | -3.9458 | -46.987301 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8cd7183d-ea47-30f0-b877-f2add1a09ff7 | -3.2122 | -45.485298 | 2024-12-28 00:21:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 31adf1c8-59e1-3e07-96b6-fdde6e203bf0 | -4.7524 | -44.6544 | 2024-12-28 00:21:00 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b1361c1d-d251-3585-bb2e-1d0860525469 | -10.7626 | -37.145699 | 2024-12-28 00:21:00 | METOP-B | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7d1801e0-9a31-343e-bdc1-cb629ec6beb6 | -10.753 | -37.148201 | 2024-12-28 00:21:00 | METOP-B | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2b881326-65a0-35d1-a9ec-8379a7a49faa | -2.558 | -46.865501 | 2024-12-28 00:21:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 275a5733-1470-3cd1-b9dc-a262f8ba0cfb | -4.0042 | -46.6996 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0ba0d39b-d67d-3ba4-b291-291d7d0acef6 | -4.5505 | -44.047901 | 2024-12-28 00:21:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9254fb57-8400-3209-b18b-92b8eebadae7 | -1.6346 | -52.6003 | 2024-12-28 00:21:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f85f5d85-b7e8-3c72-a446-19be79ef9698 | -3.9235 | -46.888802 | 2024-12-28 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 684776fe-5072-360b-a9bc-d52d9ff7e1c0 | -3.9442 | -46.980301 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6b12f874-daee-3747-811a-e3d1a7ee32ad | -3.7571 | -47.337002 | 2024-12-28 00:21:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16f53a3a-e76a-33c6-865c-7704ecb4b4b0 | -4.0214 | -46.911301 | 2024-12-28 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9786a7af-015b-361e-b4d2-dd557959f2d3 | -4.1219 | -46.673199 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 86c45923-4366-390b-85d7-5997e46f9b67 | -4.0075 | -46.713799 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4c0bd25b-7a89-3f50-a50e-f5ddfad06f9a | -2.008 | -45.578899 | 2024-12-28 00:21:00 | METOP-B | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 35c5e0d3-659a-392a-9df3-034f02dcefe0 | -8.1311 | -43.136799 | 2024-12-28 00:21:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1e0b2c1a-8030-3927-a9b5-6914b13f2688 | -3.872 | -46.661701 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6e88a41b-2ae0-3860-9ca7-754d8c315b02 | -3.7421 | -47.179699 | 2024-12-28 00:21:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aef2823b-43b9-389b-9eb1-1647658cd600 | -3.2092 | -45.968201 | 2024-12-28 00:21:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
