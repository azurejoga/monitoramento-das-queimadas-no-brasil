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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3826a1b-4211-305b-b92a-dde17b1a615c | -5.3277 | -56.0263 | 2026-09-05 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| b345c97f-c22d-3a6f-b609-d85e38967ebb | -6.6514 | -59.945 | 2026-09-05 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 200.3 |
| 342a79bb-1ad9-33cd-a07e-37a0ed5cfa7a | -5.3462 | -56.0256 | 2026-09-05 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 68ffaf15-a5fb-3b4b-88b8-0bd2f6c30c5a | -6.6697 | -59.9635 | 2026-09-05 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 43b5a85e-361c-3c73-94ad-c6bb2f933993 | -9.5721 | -40.3475 | 2026-09-05 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 83.6 |
| 430c4d18-92e6-3a7d-9359-c0742d7471c3 | -4.6853 | -55.6343 | 2026-09-05 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 770cb7f7-973c-38c9-81a5-0a3a3eebdc5e | -6.6515 | -59.9258 | 2026-09-05 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 58059038-830f-3697-87a9-8193de698512 | -13.4458 | -43.8128 | 2026-09-05 02:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 4015f200-af9c-3bd1-9e38-09e922ad328f | -6.6697 | -59.9635 | 2026-09-05 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 134.7 |
| aeda379b-7f20-3ef6-80dc-f95ded52086a | -5.9197 | -47.8927 | 2026-09-05 02:30:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 824914f0-f84c-3ed3-b1fb-50cd4fd85262 | -9.5725 | -40.3227 | 2026-09-05 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 123.1 |
| 1df4c753-1adb-3fce-9469-e4dd7354576b | -6.6513 | -59.9642 | 2026-09-05 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 63d71677-7bfe-3730-80e6-5210f0dae84f | -13.4264 | -43.8163 | 2026-09-05 02:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 565e39dc-a008-319d-9b95-7a69875dcb0d | -15.0769 | -52.5396 | 2026-09-05 02:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| ea74ccf7-f161-3b30-80f9-5e09f4037cf3 | -9.5534 | -40.3254 | 2026-09-05 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 433.3 |
| ad7bc171-cc03-3cfc-ba18-d81191901839 | -6.0244 | -60.1781 | 2026-09-05 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| ecdb145c-e3cf-33dd-a4c9-fbf0bc45068f | -4.6669 | -55.635 | 2026-09-05 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 578cff7c-c527-3912-877e-4b194903c159 | -13.4259 | -43.8401 | 2026-09-05 02:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 674b46cd-89cb-3852-894a-09b777f0224f | -5.6566 | -60.2284 | 2026-09-05 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 9a9c52d0-18aa-33f8-9290-5f001bbb546e | -5.6382 | -60.2289 | 2026-09-05 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| ae9aacda-d1ad-3db9-82b9-2aef0210202a | -9.553 | -40.3503 | 2026-09-05 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 77.0 |
| e233c185-6140-313a-843c-ccb3f085685d | -6.6699 | -59.9251 | 2026-09-05 02:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| cdf46505-03a8-380f-ae46-f900c2708d38 | -15.0773 | -52.5183 | 2026-09-05 02:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 19f695da-7551-3da9-b537-11224d4dea09 | -9.5538 | -40.3005 | 2026-09-05 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 102.4 |
| f610e291-7f3b-39c8-b69c-5a1cc454a2ff | -13.4453 | -43.8366 | 2026-09-05 02:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| a92fdeb6-8e32-334f-b60b-0efc145c1bb5 | -6.6514 | -59.945 | 2026-09-05 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 165.6 |
| 63a5d6c2-ebac-355a-bf45-ae6ddaefe4c9 | -5.7756 | -45.0826 | 2026-09-05 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| ecafb6b8-f174-3faa-8ac4-4fece6aabc95 | -5.6565 | -60.2475 | 2026-09-05 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| c89f8f9d-a012-3219-b951-12a011bad625 | -6.6698 | -59.9443 | 2026-09-05 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 204.7 |
| 56782ccb-b6f7-3c9c-b276-e27bba670381 | -9.5343 | -40.3282 | 2026-09-05 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 99.7 |
| 56835eb7-a5dc-3bce-a8a4-6798a74aad02 | -5.7758 | -45.0599 | 2026-09-05 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 56d60dcf-b1c8-38f6-bfb8-fcfa3f0e8245 | -17.1078 | -56.8304 | 2026-09-05 02:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.3 |
| 01d859ae-592e-3d8b-9dea-4ce8c0e36374 | -6.6513 | -59.9642 | 2026-09-05 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 98.4 |
| ca34c73d-73a4-3b96-8bd9-b5cf7cb755fc | -4.6853 | -55.6343 | 2026-09-05 02:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 6614854b-a8dc-3267-9591-0cb9f587729c | -6.6697 | -59.9635 | 2026-09-05 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 95.0 |
| b08500e6-184f-3843-bfaf-4c1f73fc7033 | -6.6699 | -59.9251 | 2026-09-05 02:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| fb6b8fcb-7cc2-30bb-98af-34c3ade01fc5 | -4.6669 | -55.635 | 2026-09-05 02:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| f56e245e-4eb4-3677-8455-c172a534ecf6 | -17.1074 | -56.851 | 2026-09-05 02:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.0 |
| 27276cc7-84eb-3bf0-bd63-bdf427425acc | -9.5534 | -40.3254 | 2026-09-05 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 108.0 |
| 533bb91d-1b08-3f70-9b66-394d73d28838 | -6.6514 | -59.945 | 2026-09-05 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 179.0 |
| be9fda21-a17c-3e58-b15a-bed7de119738 | -5.3277 | -56.0263 | 2026-09-05 02:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 90f65a9e-b7be-3759-bd0b-33090d7a6303 | -6.6515 | -59.9258 | 2026-09-05 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| cd3af1fa-a249-36f3-a20b-e7a529dd312c | -5.6565 | -60.2475 | 2026-09-05 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 0d0f6955-f7df-32b2-b1bf-86cc8f86ce4c | -5.3462 | -56.0256 | 2026-09-05 02:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 877de701-3a55-3fe3-abe3-970a9c4ef712 | -5.6566 | -60.2284 | 2026-09-05 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| eaf0ba5e-9049-3ec1-9c61-eac97bfc9bc2 | -5.9197 | -47.8927 | 2026-09-05 02:40:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 945566a9-ea3f-3f0b-b462-f9ec6d2503d8 | -5.346 | -56.0454 | 2026-09-05 02:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 4c6a2a44-a35b-3124-8050-7fed561ec44f | -6.6698 | -59.9443 | 2026-09-05 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 166.0 |
| 4cd30c9d-a36c-3205-8803-a8083001d4ec | -5.3462 | -56.0256 | 2026-09-05 02:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 150.2 |
| 6b98bfb4-de11-3f1c-b4fb-b4786f22a9cd | -5.3277 | -56.0263 | 2026-09-05 02:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| b9d6e0f0-cbc2-3e89-b48f-0bd412acc251 | -5.565 | -60.1739 | 2026-09-05 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| dd48cd67-1b55-3f03-81da-7ccab8e256b3 | -6.0244 | -60.1781 | 2026-09-05 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| ed91f903-87f5-352f-ab22-4678a3f91cf8 | -6.5963 | -59.9087 | 2026-09-05 02:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 04719c39-5ac9-3f63-abce-338abacfee4e | -5.6566 | -60.2284 | 2026-09-05 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 6b8c349f-e0b4-3db5-84a2-d1e73ed75e80 | -5.3463 | -56.0059 | 2026-09-05 02:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| e1002c8b-4b28-393e-92ef-65d6c54c4afd | -4.6853 | -55.6343 | 2026-09-05 02:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 0c19c80e-27d8-38cf-b647-f9d1a441caa0 | -5.6565 | -60.2475 | 2026-09-05 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 91d6ae68-cde0-3dd5-b55b-7e6b6927c6aa | -5.346 | -56.0454 | 2026-09-05 02:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 402953d8-1759-3be8-9c08-f84854f8de48 | -5.3276 | -56.0461 | 2026-09-05 02:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 760d051b-deac-3825-9a6f-efa34c98a98e | -17.1078 | -56.8304 | 2026-09-05 02:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.8 |
| 38aff1b5-a6d8-31bf-9be2-a79239b70331 | -5.1802 | -56.0518 | 2026-09-05 02:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| a46c2639-2281-396c-a9c7-1a6c9a3793ad | -6.6697 | -59.9635 | 2026-09-05 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 7f832590-864f-3ed4-9027-c129a09c785b | -5.3646 | -56.0249 | 2026-09-05 03:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| da8773bd-f216-3f5b-b5eb-cf0cbe3bca29 | -5.3277 | -56.0263 | 2026-09-05 03:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 7a8b8ce5-b0fe-325d-b396-fb52a23bf978 | -5.3276 | -56.0461 | 2026-09-05 03:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| c585996c-3fa2-3379-85cf-5b8e04c5b4b1 | -5.346 | -56.0454 | 2026-09-05 03:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 5e6b140e-f238-3955-bd00-a35e176fa93b | -6.6698 | -59.9443 | 2026-09-05 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 157.1 |
| f25ed069-a09b-305a-90fa-cd265bdc214f | -6.6514 | -59.945 | 2026-09-05 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 169.9 |
| 4c12b45a-1339-341b-8034-26881e162e7b | -5.6566 | -60.2284 | 2026-09-05 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 145959a4-8b7b-3460-bc6f-7594d585cd19 | -6.5963 | -59.9087 | 2026-09-05 03:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 6085ee83-ff85-3989-8ab4-ee10533fac5f | -6.6515 | -59.9258 | 2026-09-05 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 77db65ef-981b-337f-acdb-d1d8a4c1903a | -4.6669 | -55.635 | 2026-09-05 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| f8382556-5521-3080-a759-dd2f01001300 | -6.6699 | -59.9251 | 2026-09-05 03:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 3328515f-3502-3171-9b21-1f40d74f095b | -5.9197 | -47.8927 | 2026-09-05 03:00:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 635d45e9-1eb4-3f35-a95d-c9c267451166 | -6.6513 | -59.9642 | 2026-09-05 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 439ffd45-0fe7-3b14-a37c-dbb001c6e1a2 | -5.6565 | -60.2475 | 2026-09-05 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 2caa4873-1fe2-3548-a71d-79ddc156aa45 | -4.6853 | -55.6343 | 2026-09-05 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| f636d8e6-a3f3-3622-bcbb-e40d2a336ee0 | -5.3462 | -56.0256 | 2026-09-05 03:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 164.9 |
| 93e37366-41ce-3deb-af64-9d4a8e244b4c | -6.6513 | -59.9642 | 2026-09-05 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 49771c19-ffa1-3802-97d8-2cb521328038 | -5.6381 | -60.248 | 2026-09-05 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 08c8e08d-cc92-3205-8909-3736ef43ea99 | -5.6566 | -60.2284 | 2026-09-05 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 60bbde62-c94e-348f-90c6-eb72d890734c | -6.6697 | -59.9635 | 2026-09-05 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 0ad21da1-0a1e-352c-87ab-9d493d4a27a6 | -5.3462 | -56.0256 | 2026-09-05 03:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 144.0 |
| ac066df5-e94c-38ab-aa3b-194821999721 | -4.6669 | -55.635 | 2026-09-05 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 3f50c475-0746-3d57-8e96-c0c68bb9a472 | -5.3646 | -56.0249 | 2026-09-05 03:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 49f3b34c-d879-33c0-b94c-2b031ffe71f5 | -5.9197 | -47.8927 | 2026-09-05 03:10:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 36aff100-59ca-3ee7-8352-ebc976b29f4c | -6.6699 | -59.9251 | 2026-09-05 03:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 3e9dc000-33e4-3906-8f33-70a5a8a9cd22 | -5.3277 | -56.0263 | 2026-09-05 03:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 0d55d882-044f-314c-b9af-dadbb66a1101 | -5.346 | -56.0454 | 2026-09-05 03:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 895c81e8-01d3-3822-af1b-65995ddc701e | -6.6514 | -59.945 | 2026-09-05 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 136.9 |
| 06f2a6b2-45f3-3976-825e-ee52e6d4db63 | -5.6565 | -60.2475 | 2026-09-05 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 72870ad2-30a3-33a5-9ec9-59a08b1c41c7 | -6.6515 | -59.9258 | 2026-09-05 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 797b9d3c-805e-3c06-ba93-088130b90d32 | -6.6698 | -59.9443 | 2026-09-05 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 168.0 |
| 1af702ce-a82b-34b2-b65e-56c7877fe3bb | -5.6565 | -60.2475 | 2026-09-05 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| a398962b-6f96-3f7b-8939-df5f84a8ba3c | -5.3276 | -56.0461 | 2026-09-05 03:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 202b7b88-4b3f-3847-83e5-81c3d2842028 | -17.1274 | -56.828 | 2026-09-05 03:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.6 |
| 0c5e0d75-c690-3813-be9e-b2cd04c5a362 | -6.6699 | -59.9251 | 2026-09-05 03:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| d7ff9ce4-d0ea-3a55-bc62-ce21406d1185 | -6.6514 | -59.945 | 2026-09-05 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 139.0 |
| 55b64f4f-a7eb-3a63-a73d-2bbff4989c9d | -6.6513 | -59.9642 | 2026-09-05 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 56053c81-f37a-341f-989c-95eef710db9c | -6.6698 | -59.9443 | 2026-09-05 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 145.8 |


[Clique aqui para ver as próximas entradas](README10.md)
