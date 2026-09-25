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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b237fdb-9557-39f0-8ede-0540dc124360 | -9.11018 | -59.50035 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3077474b-c2de-38b4-90d2-e62d96e73055 | -12.70271 | -63.07777 | 2026-09-25 06:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e28c458-e716-3a66-a041-f6490ec7b159 | -8.07084 | -72.40396 | 2026-09-25 06:08:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 196e095d-2a08-3935-b2e4-d6072ecee066 | -11.56009 | -61.24027 | 2026-09-25 06:08:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6afa9b8f-d428-3d7f-a969-ae40d90b7759 | -9.06383 | -65.70092 | 2026-09-25 06:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70452cf9-7233-355e-9b15-ee4b57dec62e | -9.15859 | -59.47412 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a8687b4-7a18-393b-bf9b-c5e5931f2a07 | -9.02165 | -60.52546 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8aea5f79-f9a2-3c34-a3ac-0e9de26ab2e3 | -7.86239 | -72.86482 | 2026-09-25 06:08:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a155d2f3-177b-3fb6-a512-42efcc02119c | -7.6628 | -67.07837 | 2026-09-25 06:08:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6ea29b2-bc7f-323c-8193-2ce92ddb8455 | -7.67772 | -67.14031 | 2026-09-25 06:08:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37636669-d1d7-3843-bef0-226ea77bdf66 | -9.43065 | -68.09155 | 2026-09-25 06:08:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a92062d5-b414-3d34-ab97-e62518a91e59 | -7.32012 | -72.82364 | 2026-09-25 06:08:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e7a7fcc-1f4d-39d0-b2e5-468a72fdf2b7 | -8.68239 | -70.12158 | 2026-09-25 06:08:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65226a39-e75d-3a5b-a408-2a0746ee5870 | -9.82543 | -67.57215 | 2026-09-25 06:08:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bd01654-ab9c-3b1d-a2e1-2700635cc09d | -8.00616 | -71.31036 | 2026-09-25 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| caa20c3c-615d-3575-89c4-f789bcb348f7 | -9.31658 | -59.67421 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c64dc4c-6884-3c4a-bdd7-f380203429c6 | -8.26767 | -70.81038 | 2026-09-25 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f37d6a5-4331-35ad-a46c-1f45106e730a | -7.85562 | -71.74414 | 2026-09-25 06:08:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98c61231-dbf0-3075-bb5c-077e698a1def | -9.15068 | -59.49122 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9afe1f46-0220-386b-b881-ef149a64fd27 | -9.16083 | -59.41503 | 2026-09-25 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26293232-28f7-38ee-b940-b708e22b8cdc | -15.18924 | -56.05397 | 2026-09-25 06:10:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5cfcecea-e97b-3c38-84cb-e6bc9ee55ee3 | -15.18904 | -56.05693 | 2026-09-25 06:10:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ea44528-e6cf-314e-8945-be2a4d62a94c | -15.18168 | -56.05661 | 2026-09-25 06:10:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93dd2354-5f9a-3905-85d5-ecbce6906bc5 | -15.18187 | -56.05381 | 2026-09-25 06:10:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aecbbc66-acf8-3ef2-84b8-0bbaf075f162 | -12.21 | -50.76 | 2026-09-25 06:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3799c7fe-0cf7-3a1b-9308-dc3ea7810f6c | -12.25 | -50.83 | 2026-09-25 06:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9b063ddb-0b7d-3f58-878a-ee64ec58bcaa | -12.22 | -50.82 | 2026-09-25 06:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4f5425df-f44f-3d7a-aa97-769c5fdccb7a | -8.32578 | -44.13971 | 2026-09-25 06:16:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e53d484a-f3fc-3fa5-bfde-8995b95b431f | -3.23509 | -46.93408 | 2026-09-25 06:16:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| ae6eaead-8dce-34f2-af59-519437f3dc35 | -3.23388 | -46.92625 | 2026-09-25 06:16:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 5c204f35-f297-3855-9462-61b387d4643d | -8.33412 | -44.15409 | 2026-09-25 06:16:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 25e01fbb-9f30-3347-8ac0-ac7faf5b1104 | -8.33622 | -44.14128 | 2026-09-25 06:16:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 1018acc5-efc8-3d61-b9fd-8b7740037770 | -12.22659 | -50.70413 | 2026-09-25 06:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 1e9dc1e9-de09-363a-bae2-3e5283189175 | -12.24269 | -50.70726 | 2026-09-25 06:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 562.1 |
| 2f270c28-7a79-32cf-9b35-b8d1e3a1e29b | -11.28461 | -51.26891 | 2026-09-25 06:18:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 0310c478-14bf-3f4a-a3b3-665d8b1bf7d3 | -12.25012 | -50.70366 | 2026-09-25 06:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 206.9 |
| b2d06cef-9665-35bf-9936-ab3c20713da4 | -12.23403 | -50.70047 | 2026-09-25 06:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 225.8 |
| 0736c3de-9789-38f5-82b2-40659ac45878 | -9.63276 | -43.95202 | 2026-09-25 06:18:00 | AQUA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 37f7a711-c03d-3998-b2a7-1c514f629b48 | -11.27703 | -51.30934 | 2026-09-25 06:18:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 3210a0eb-bfa2-392a-8f7b-97c509865147 | -9.62271 | -43.95034 | 2026-09-25 06:18:00 | AQUA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 57801246-50cb-366b-bcef-5d1b1738d679 | -12.23596 | -50.74218 | 2026-09-25 06:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 780.8 |
| 6b41962f-f977-350a-bcbc-68b17c23cd70 | -12.22097 | -50.77061 | 2026-09-25 06:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 206.3 |
| 73e901c0-ccc6-3bbc-a221-ee59529a7295 | -12.22237 | -50.81264 | 2026-09-25 06:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 228ad949-13e6-3d01-9266-2b7f431d99aa | -12.20614 | -50.80949 | 2026-09-25 06:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| dae2a1fb-72f9-30e8-99a3-779a868f3859 | -12.24366 | -50.73864 | 2026-09-25 06:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 472.4 |
| 29208dcb-531f-3260-934b-ac9e22cec6f8 | -11.17256 | -51.36893 | 2026-09-25 06:18:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 3467475b-3cef-33a9-9c38-3a3ec5f9ee07 | -11.17559 | -51.37403 | 2026-09-25 06:18:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| ce9d71e4-1a41-35bf-8fe9-4672261d36f5 | -13.2192 | -51.5481 | 2026-09-25 06:18:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 205.5 |
| 86dd6309-cb31-35f9-aaea-21d2a0fd4575 | -9.62081 | -43.96224 | 2026-09-25 06:18:00 | AQUA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 3d249450-eb19-3c50-a438-d726e7b5fe9e | -12.23715 | -50.77381 | 2026-09-25 06:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 108.4 |
| e0897baf-2c12-3801-b0d2-53eb01fba4bb | -12.213 | -50.77415 | 2026-09-25 06:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 8010da08-92d4-3baf-a121-22d2571d8877 | -12.22752 | -50.73545 | 2026-09-25 06:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 814.3 |
| 015e9918-4782-333a-96f9-da932162a0c6 | -12.21982 | -50.73904 | 2026-09-25 06:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 194.1 |
| b56233e4-5b7c-3055-873a-dc30fe6cb6c1 | -13.21396 | -51.54258 | 2026-09-25 06:18:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 191.9 |
| a8a76aaa-bea6-381a-9c99-e8bcd4aef604 | -9.63087 | -43.96389 | 2026-09-25 06:18:00 | AQUA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 7a25e435-cfce-3eff-b854-0b1094904077 | -12.21437 | -50.806 | 2026-09-25 06:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 499f4561-db5f-346f-a5c7-3f660f6f1cd9 | -12.22919 | -50.77729 | 2026-09-25 06:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 218.6 |
| bc91cb6a-a2ec-399c-ab2e-e4c453b999d6 | -11.28498 | -51.27707 | 2026-09-25 06:18:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 75e2fc29-312c-3df9-b2bd-64eda1112434 | -19.60241 | -45.19339 | 2026-09-25 06:22:00 | AQUA_M-M | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 28950f71-0e9f-36f8-958f-6bb9cfcc7bc0 | -19.60067 | -45.20402 | 2026-09-25 06:22:00 | AQUA_M-M | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 87de21a9-e58a-33ba-bee7-9a09a4ce89a8 | -6.91911 | -71.7514 | 2026-09-25 06:27:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8564fcd8-9c52-3d46-b608-7adc320883d7 | -7.67409 | -67.14838 | 2026-09-25 06:27:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a1f7bc2-dc01-3bee-9738-17e2af938f3e | -7.67491 | -67.14269 | 2026-09-25 06:27:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e7142dbe-1dbc-33f5-ae0e-f49e648bbbaf | -6.99641 | -71.58624 | 2026-09-25 06:27:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 089405dc-748e-3de2-a13a-3dd41d9c7533 | -7.66368 | -67.07797 | 2026-09-25 06:27:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb24f871-2e48-3f9d-b3ad-319c0130099e | -6.95114 | -71.78677 | 2026-09-25 06:27:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0712783c-2bcc-3c97-92a8-24dcb8d1c2d0 | -7.67515 | -67.14455 | 2026-09-25 06:27:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ec14906e-10c1-3c21-b28d-4b677db4de89 | -6.95049 | -71.79105 | 2026-09-25 06:27:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2b0cb7d-79aa-3c5e-b029-1c7190f9f016 | -8.38742 | -71.07566 | 2026-09-25 06:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06260e4e-9c1e-357f-b7af-738eb4401964 | -8.26669 | -70.80955 | 2026-09-25 06:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3498725d-831c-39b8-aefb-767d851fb86f | -8.66291 | -70.9194 | 2026-09-25 06:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3172853-5c62-3289-8417-1e813dc67f84 | -8.9406 | -71.84843 | 2026-09-25 06:29:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f16ee26-b031-3356-af31-b494b3f1fc24 | -7.94603 | -71.34018 | 2026-09-25 06:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1d79500-f76a-324c-8eb3-81f5b4f52124 | -8.77679 | -68.72536 | 2026-09-25 06:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82dce722-4e03-33fd-bbc9-03ed8b0e85d5 | -9.06316 | -65.7046 | 2026-09-25 06:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e71b3db8-3706-3993-bd3e-045918f713ee | -9.38542 | -66.51426 | 2026-09-25 06:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82d49495-fed4-3689-bc92-323da3a00c03 | -7.38874 | -72.5248 | 2026-09-25 06:29:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c5f1e26b-e707-34b9-a6c7-6e8faaf1affd | -8.63723 | -66.8624 | 2026-09-25 06:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4432cd7b-b132-3e7a-9c56-4ba607246028 | -8.83892 | -72.30016 | 2026-09-25 06:29:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eecf2008-5304-3f9d-8884-211bb1ccd6ee | -7.86857 | -72.86369 | 2026-09-25 06:29:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95a9f949-6e0f-3dc0-9315-4e5cc0331fe5 | -9.54716 | -65.98525 | 2026-09-25 06:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e799203-e397-3ac8-9db3-a4924d86f21c | -7.28553 | -72.04408 | 2026-09-25 06:29:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98394d7a-83d7-34e6-88a8-9163eac1f273 | -9.37851 | -66.50987 | 2026-09-25 06:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f5135d8-c113-372d-a9d9-63855aac45db | -9.38588 | -66.51089 | 2026-09-25 06:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aab58c3b-8197-3b69-b080-a324eb638b50 | -7.60244 | -69.89347 | 2026-09-25 06:29:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4d847a6-ada3-3cd3-8fe0-b718c8ca96fd | -9.54647 | -65.98727 | 2026-09-25 06:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| de835864-e0a3-334a-8494-a8f7f58b87ee | -9.67348 | -66.83203 | 2026-09-25 06:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3a7ad12-67e9-32f8-b168-caf0dc8f7c51 | -7.70581 | -71.98532 | 2026-09-25 06:29:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3667467-f27c-3264-91a7-87090c5a9d98 | -7.85429 | -72.33873 | 2026-09-25 06:29:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 173177af-0b77-3742-8351-c01c1bba0d30 | -7.86507 | -72.86317 | 2026-09-25 06:29:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c283410a-3fc1-3f37-a085-6167607edefe | -9.38054 | -66.51012 | 2026-09-25 06:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c470d7a0-5c62-3cac-819c-c7529e57dd91 | -9.38385 | -66.51065 | 2026-09-25 06:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13821c56-2f51-385e-874d-02078e71fb2d | -9.37895 | -66.50645 | 2026-09-25 06:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b16d79c-06c2-324c-82d1-16d1a4fe7447 | -8.32662 | -72.84564 | 2026-09-25 06:29:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4e1a5ef-4fe6-387f-a085-ddb0e9c1bb25 | -9.06924 | -65.70184 | 2026-09-25 06:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e9f4b23-e2aa-3345-8fba-d92363b064b3 | -9.54667 | -65.9889 | 2026-09-25 06:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d061895-bc72-335a-862d-2d8b9871fb57 | -8.02749 | -71.36468 | 2026-09-25 06:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18789b57-b488-397d-aeef-de9ba9fc8f31 | -8.96126 | -72.85525 | 2026-09-25 06:29:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32c00f3f-b687-354e-b74f-8d74030fd8f6 | -9.39975 | -65.91013 | 2026-09-25 06:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc57ba79-69b0-35bb-a2db-e68e714502a6 | -8.4846 | -72.73469 | 2026-09-25 06:29:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README39.md)
