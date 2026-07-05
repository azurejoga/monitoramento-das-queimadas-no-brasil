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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cc11525-8ce9-3887-a754-b0a30b5c0f55 | -11.4334 | -46.5969 | 2026-07-05 00:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 71b4b967-c1b8-34c7-adb1-a32b02291ae4 | -10.9397 | -43.0593 | 2026-07-05 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 171.7 |
| c87de665-4016-3536-aba0-659129215bc1 | -11.4337 | -46.5743 | 2026-07-05 00:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| a35c8cb9-f271-3167-8396-c7c76e87a13d | -10.9205 | -43.0622 | 2026-07-05 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 4329ead2-77be-3adc-81fd-14c5b5ad8a23 | -10.9209 | -43.0384 | 2026-07-05 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 220.1 |
| 912e6a32-6db6-3718-9042-1df2a8aae552 | -10.9401 | -43.0355 | 2026-07-05 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 347.1 |
| c068a786-741f-3117-9e84-a84d5ff8d9b1 | -11.4525 | -46.5943 | 2026-07-05 00:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 64c8441e-885b-3a06-b26d-5173c6ee9e35 | -10.9209 | -43.0384 | 2026-07-05 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 359.6 |
| 8aec367f-bd76-37de-9b29-ae457263cefa | -10.9401 | -43.0355 | 2026-07-05 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 344.1 |
| e27a7554-0d9c-3abf-b566-34eeec2dde99 | -11.4334 | -46.5969 | 2026-07-05 00:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 162.8 |
| 09ea6ad2-9522-3278-8413-119200c80d6b | -10.9397 | -43.0593 | 2026-07-05 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 203.1 |
| 1c1964b8-b545-3a28-b1c9-c2484a66d5eb | -10.9205 | -43.0622 | 2026-07-05 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 189.8 |
| 9c28d7f3-2de0-38cb-b06e-b294e5025465 | -10.9405 | -43.0117 | 2026-07-05 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| d7fb3112-4741-3be8-8db8-5c03321eb2c7 | -11.4337 | -46.5743 | 2026-07-05 00:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| ab637436-9e4d-308b-a550-44a49859d8ae | -10.9213 | -43.0145 | 2026-07-05 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 9b10764d-3cbe-33fa-9f88-9be0d66ec05f | -10.9416 | -43.044102 | 2026-07-05 00:16:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1efe37dc-1fa6-387c-8060-b63f9449bd98 | -10.9302 | -43.038799 | 2026-07-05 00:16:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c02b424a-c169-310c-acb1-363e23e68a77 | -11.4344 | -46.589199 | 2026-07-05 00:16:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3bf4594-caa1-37b8-8ae7-83f11c519e13 | -6.8932 | -43.7118 | 2026-07-05 00:16:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9318675b-ef6d-3d7a-a589-ab5965a2ddf0 | -11.892 | -43.822399 | 2026-07-05 00:16:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 92e3a8b6-1579-3d44-8dbe-d0c85e2a630e | -6.9046 | -43.716702 | 2026-07-05 00:16:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fbffdbb8-1d57-3518-9130-6e0db8ffa3d1 | -10.9689 | -48.135101 | 2026-07-05 00:16:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 446f6b33-f2f5-3dfb-877c-d640f4149cf6 | -11.9193 | -43.380299 | 2026-07-05 00:16:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dd7f39b6-32ca-345e-8fd8-b78f03f5371e | -17.623199 | -42.282101 | 2026-07-05 00:16:00 | METOP-C | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2546c627-bcf6-3a2d-8dfe-761ed88011ca | -8.3232 | -45.387299 | 2026-07-05 00:16:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 397b9a96-e939-3882-92b7-b2dd16f677a4 | -13.4465 | -43.852299 | 2026-07-05 00:16:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5821fc33-c650-3db8-ad8a-444e419c9517 | -17.256399 | -48.996498 | 2026-07-05 00:16:00 | METOP-C | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 733ad934-140b-3ee1-ba28-fdb2b2b22504 | -6.8948 | -43.718899 | 2026-07-05 00:16:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| adc5d762-b93c-3928-8a4f-b74bb6f1d6bf | -17.6266 | -42.298199 | 2026-07-05 00:16:00 | METOP-C | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 68fb4b3d-2e4b-314e-9a3d-65ce449296a9 | -11.8955 | -43.838501 | 2026-07-05 00:16:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0145c33e-7c10-3f29-a4e0-992c449144b3 | -8.9479 | -44.2104 | 2026-07-05 00:16:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a067e7d7-240f-3331-8483-07f9933913b8 | -10.922 | -43.048401 | 2026-07-05 00:16:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a2e7009d-6c3e-3f8e-86c4-73ea630f0035 | -17.624901 | -42.2901 | 2026-07-05 00:16:00 | METOP-C | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7914659d-3ecc-3b10-9088-8eac0a5a33ac | -6.9357 | -43.7174 | 2026-07-05 00:16:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2d830427-d7b8-3de6-90b9-39cbf91375aa | -11.439 | -46.611599 | 2026-07-05 00:16:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d12f59b2-e2a2-312c-a859-12568b59b395 | -11.4367 | -46.600399 | 2026-07-05 00:16:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 41e93645-973b-32cc-a6bb-ff1722552105 | -6.9341 | -43.710201 | 2026-07-05 00:16:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1b2b781b-4a95-3fda-8957-ffa170b49b3d | -11.4223 | -46.580101 | 2026-07-05 00:16:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 643a7794-8d32-3d64-a796-68b852494f7d | -11.427 | -46.602402 | 2026-07-05 00:16:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1786954f-5aab-31a8-9ce5-2f996218c52a | -11.4247 | -46.591301 | 2026-07-05 00:16:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5b6f11e5-37ee-33f2-b4b5-a67ccf05fecb | -6.9373 | -43.724602 | 2026-07-05 00:16:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fc767161-c157-3715-b1ff-c47e6945f949 | -11.432 | -46.578098 | 2026-07-05 00:16:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 909e58b0-0125-34d8-a41d-558de8a0b2d5 | -17.26 | -49.016399 | 2026-07-05 00:16:00 | METOP-C | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0b6df666-c45d-3d6f-9e58-23dbeb40408e | -6.903 | -43.709599 | 2026-07-05 00:16:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d06fe036-391e-3cf1-ab7d-788d8ab2744a | -11.8857 | -43.840698 | 2026-07-05 00:16:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| df08bef5-f386-3b8b-9d04-c601a1f9844e | -10.9286 | -43.031502 | 2026-07-05 00:16:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0e3fd79a-8fa7-343c-8698-0e3ea988f042 | -10.9334 | -43.053501 | 2026-07-05 00:16:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8e2d9f92-3b0b-37f2-a13e-db5aef47e25e | -11.921 | -43.388 | 2026-07-05 00:16:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 33265500-a54f-3905-93d8-330034208cb3 | -10.966 | -48.121201 | 2026-07-05 00:16:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7c29e4a-e568-3f55-b29a-d821d04bca0f | -7.4075 | -46.8297 | 2026-07-05 00:16:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e6491c64-f74c-3e07-bf40-7d43be792bae | -11.9095 | -43.382401 | 2026-07-05 00:16:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0fe2652d-34ad-3fbe-afa2-2680bd3228a1 | -8.9381 | -44.212502 | 2026-07-05 00:16:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3a7c7caf-0113-38fa-9cf3-4fea12a42d3a | -11.9112 | -43.390099 | 2026-07-05 00:16:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 23b612ef-73ff-37ee-a927-6d40158d835d | -11.8937 | -43.830399 | 2026-07-05 00:16:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 028ed8b9-8d80-3b47-a48d-956f7939cecc | -10.9318 | -43.0462 | 2026-07-05 00:16:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 519bc615-eb4e-3a61-8133-d9e86cfc01c7 | -11.4293 | -46.613602 | 2026-07-05 00:16:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b7dc6c97-1c47-340d-a51b-6c61e59908c7 | -11.8839 | -43.8326 | 2026-07-05 00:16:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 84d4721e-1897-3f06-8da0-136d48bb9b79 | -8.3214 | -45.3787 | 2026-07-05 00:16:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 84bfb6a3-7cc2-3e53-8708-080252d07726 | -11.4529 | -46.5717 | 2026-07-05 00:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 53a7faf4-405f-3c6f-ae8f-7fb58834f5dd | -10.9397 | -43.0593 | 2026-07-05 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 211.6 |
| fe852db6-204a-3c99-b7e1-42a36695ea0d | -10.9205 | -43.0622 | 2026-07-05 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 2c66454d-bf6e-33a3-944a-ed44cf871671 | -11.4334 | -46.5969 | 2026-07-05 00:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 162.0 |
| fd31516b-28d9-308f-9b57-70e926f53a8c | -11.4525 | -46.5943 | 2026-07-05 00:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| d47fb5a3-4071-3ca0-8ae0-f9f7385eec92 | -10.9401 | -43.0355 | 2026-07-05 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 544.6 |
| 5f69df64-29c2-3ca7-ae88-c5b00e383822 | -11.4337 | -46.5743 | 2026-07-05 00:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 4ba0df56-fedd-3c96-8840-c8040de16b24 | -10.9209 | -43.0384 | 2026-07-05 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 330.0 |
| 830e574f-ef7d-3971-a376-e551873f2350 | -10.92578 | -43.02012 | 2026-07-05 00:20:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 9cf1e552-f40f-3e31-8275-e311627a0d31 | -17.67914 | -52.94201 | 2026-07-05 00:20:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| f2cc8c49-087a-3127-8568-01d7ed17fcde | -17.26561 | -49.00415 | 2026-07-05 00:20:00 | TERRA_M-M | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 1dfb0d0a-8670-3d46-ace2-d053215025f8 | -13.21757 | -54.33503 | 2026-07-05 00:20:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 7c9ce9b0-eb4e-3609-859e-d8c7f7c63219 | -11.66763 | -50.38766 | 2026-07-05 00:20:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cd178df2-dabd-3247-b870-98383394d8e8 | -11.4428 | -46.58448 | 2026-07-05 00:20:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| d18700db-3b37-3237-9692-1c1197bf6008 | -11.65726 | -50.3796 | 2026-07-05 00:20:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 35fdfbe4-7159-3107-ae6a-6517804f696b | -10.96936 | -48.12167 | 2026-07-05 00:20:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 89e30de9-2650-39d9-b180-766979496909 | -10.97319 | -48.12748 | 2026-07-05 00:20:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 72c1b699-932f-38fa-8c99-ff682984228a | -10.97503 | -48.13993 | 2026-07-05 00:20:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 37923670-231d-39a5-9a57-50da8c2444c5 | -11.31792 | -54.47298 | 2026-07-05 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ecf92dbd-0ef4-3a03-be62-ef13917c52e1 | -17.26702 | -49.01388 | 2026-07-05 00:20:00 | TERRA_M-M | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 03dd65ee-99c7-3a4b-b53f-558f047404da | -13.25672 | -54.32972 | 2026-07-05 00:20:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 3d835d6a-4e2b-3028-8d83-83df31fdc03f | -17.6173 | -42.28771 | 2026-07-05 00:20:00 | TERRA_M-M | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.8 |
| a7ef0557-f3cc-353f-97fe-e103c6c443f4 | -11.43376 | -46.60213 | 2026-07-05 00:20:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 285.3 |
| 9534e85d-d724-392c-909c-f0315303556f | -10.97129 | -48.13412 | 2026-07-05 00:20:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 39.8 |
| a5c68580-b0a0-392a-b1b0-bd52e0646974 | -11.30828 | -54.47429 | 2026-07-05 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a2d3df67-c4fd-30c0-b7bc-621d1e9e9f2b | -11.54576 | -48.26308 | 2026-07-05 00:20:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a61caea8-be74-38fc-8f79-7d6e886a40fc | -11.44527 | -46.60037 | 2026-07-05 00:20:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 19787e1f-2f31-3f04-8381-daf5a4c1a681 | -10.931 | -43.05069 | 2026-07-05 00:20:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 945.7 |
| d9d95ddb-8823-3bff-98cb-7f1ad346b1ee | -13.19236 | -54.31049 | 2026-07-05 00:20:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 03adfbce-4ef1-30b4-a844-69204ef0ff4d | -11.43134 | -46.58667 | 2026-07-05 00:20:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 238.6 |
| 64d70787-65c1-3e5a-9f0e-b93f9577fbb2 | -11.88946 | -43.82747 | 2026-07-05 00:20:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 95facbf6-d271-3071-95ff-a83b5ecd67d8 | -16.04113 | -50.56389 | 2026-07-05 00:20:00 | TERRA_M-M | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bd3afa9e-3fe3-3ae0-bebc-a32180d0531f | -11.65859 | -50.38903 | 2026-07-05 00:20:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 454020f4-54cd-37b3-be88-39e4f090a9bb | -12.1719 | -54.53711 | 2026-07-05 00:20:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 75634dfd-63f0-3a04-a90c-d5d3b8e512bc | -6.4278 | -55.79922 | 2026-07-05 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 14b00f34-971e-36e3-bd2b-c8c3d8dfe2b0 | -6.99084 | -55.89225 | 2026-07-05 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 3d2f0d09-9c3a-3304-8b3c-719b531f27f3 | -6.90486 | -43.7309 | 2026-07-05 00:22:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 4945287d-59fb-3eb6-8e95-4b2f31640384 | -6.98941 | -55.88661 | 2026-07-05 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a816b0b1-99b5-3c0f-8efc-96e47e62607e | -5.72944 | -51.72829 | 2026-07-05 00:22:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 5bdf053d-db67-3e62-9a61-c93b50a9920e | -6.93622 | -43.72573 | 2026-07-05 00:22:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 23c258fb-f015-3941-bd09-5763fc8f01e1 | -6.89495 | -43.73771 | 2026-07-05 00:22:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 28b2c7b1-138d-3c1c-b1a8-d9b83be9e337 | -9.39166 | -48.92907 | 2026-07-05 00:22:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |


[Clique aqui para ver as próximas entradas](README2.md)
