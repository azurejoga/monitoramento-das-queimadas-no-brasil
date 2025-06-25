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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20abcd48-785c-3a91-a538-474184d282b7 | -8.4775 | -50.28273 | 2025-06-25 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a1aee8c0-d3c5-3590-b45c-66c845d7d21d | -11.59149 | -44.64864 | 2025-06-25 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d831a0b-bd97-3b5b-b401-e4ed9979d737 | -9.81419 | -48.39275 | 2025-06-25 04:08:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f5584472-27e7-320d-a469-1b926a8103e3 | -12.75338 | -44.41043 | 2025-06-25 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a28d37aa-8b15-342c-b9ba-dda604e6550c | -10.83408 | -54.04779 | 2025-06-25 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f3ff211-44fb-35de-872f-245ca824e316 | -10.443 | -47.945 | 2025-06-25 04:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 965382c7-3015-35da-aaa7-0645333778ac | -6.1791 | -48.0712 | 2025-06-25 04:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| a04d8509-7c58-3d49-875e-52792edb1c92 | -21.20116 | -48.51855 | 2025-06-25 04:10:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fe9947b2-61c4-3c2f-9a66-176335581fe6 | -19.54766 | -49.67914 | 2025-06-25 04:10:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cd646930-eaa3-3097-a1da-f2e92e54c19a | -20.99511 | -51.79465 | 2025-06-25 04:10:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 05f06b48-5f8e-3914-832e-48010bb203a0 | -20.92632 | -49.09263 | 2025-06-25 04:10:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 9a54eabd-b7bc-3357-b401-2f1b96f707b8 | -17.08073 | -45.95219 | 2025-06-25 04:10:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eea79bce-3ff4-34b5-9c9e-3c52c7271f78 | -19.6403 | -45.18776 | 2025-06-25 04:10:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1948f4bc-de7b-315c-8cbf-0081e498a6d8 | -20.31023 | -44.51797 | 2025-06-25 04:10:00 | NOAA-20 | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 34d52255-93d3-3537-8b77-7991a616aac1 | -17.07732 | -45.95157 | 2025-06-25 04:10:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2db42345-68fa-3aef-964b-abce3b82af10 | -17.08137 | -45.94835 | 2025-06-25 04:10:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d735b69d-f11f-3c85-b4c9-2e1fbf05e218 | -21.81405 | -56.29594 | 2025-06-25 04:10:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d3dc7d0-5fd1-3362-b2e6-fb0178f02264 | -23.33704 | -46.77114 | 2025-06-25 04:10:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ecb62663-001c-3c37-b7e7-3a9966644403 | -22.38393 | -47.09262 | 2025-06-25 04:10:00 | NOAA-20 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f1b7db2-0d6c-31a7-8858-62e699fdc940 | -20.31053 | -45.58662 | 2025-06-25 04:10:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5abfa9b8-7d3f-34ec-8c07-9a38de88097a | -21.2883 | -48.55802 | 2025-06-25 04:10:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a21fe1e-588d-34cc-943c-c60f7a7e0762 | -17.08201 | -45.94451 | 2025-06-25 04:10:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cd87784b-915c-3fa8-aeb2-2a62887efef9 | -23.45337 | -46.72559 | 2025-06-25 04:10:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 85b3df12-5ee7-3a6b-82a8-1b7b3a5b6e09 | -21.14718 | -45.07089 | 2025-06-25 04:10:00 | NOAA-20 | RIBEIRÃO VERMELHO | MINAS GERAIS | Brasil | 3154705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 15658685-443e-325c-8c0d-c8f8a5c2ea77 | -23.59381 | -47.43937 | 2025-06-25 04:10:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d4e5cbbe-7632-3db6-8893-ba93bb56d8a7 | -23.71033 | -46.89693 | 2025-06-25 04:10:00 | NOAA-20 | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 604958d7-3567-38c7-9b32-934d95e86710 | -18.72611 | -47.42126 | 2025-06-25 04:10:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74f465ba-4b9b-324c-be71-7926706b345b | -17.14093 | -44.79525 | 2025-06-25 04:10:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da7087c6-e35f-3180-aead-282ee71c5c9a | -23.40688 | -46.55593 | 2025-06-25 04:10:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 22ef08ff-2c9a-31fa-8c08-df5eaf33646c | -21.18015 | -43.98029 | 2025-06-25 04:10:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4b68f00f-35c9-3c4d-a941-fdab189f60da | -20.01979 | -44.59589 | 2025-06-25 04:10:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 46d2a1a1-0f17-3fdf-8332-2c013b0c3b33 | -21.57807 | -45.30994 | 2025-06-25 04:10:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| dd42c3e7-42dc-3896-a3c9-56136658800d | -22.5405 | -48.8145 | 2025-06-25 04:10:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24a8b879-2dba-3cde-a07a-98b6a4f28d3f | -20.31113 | -45.58292 | 2025-06-25 04:10:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08adb986-03a2-36d7-9505-33e8523b907f | -17.14152 | -44.79161 | 2025-06-25 04:10:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f65e504-7487-32d5-aaaf-5be78c399713 | -20.92546 | -49.09747 | 2025-06-25 04:10:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 2935e3d9-f077-3512-9975-387450929d64 | -19.51281 | -44.27634 | 2025-06-25 04:10:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 60848c5b-716c-3328-a2d6-ac89cf285f28 | -20.22252 | -48.60941 | 2025-06-25 04:10:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9ab98d7-445b-35b1-af6a-77f5c15ce728 | -20.57977 | -44.57536 | 2025-06-25 04:10:00 | NOAA-20 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f7899777-c361-3b5d-97e8-40b804487455 | -21.20557 | -48.51486 | 2025-06-25 04:10:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2bb2dbff-a038-3a24-9733-9a4618ddaa15 | -20.37572 | -45.60171 | 2025-06-25 04:10:00 | NOAA-20 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6316318a-2f4a-37bd-bc35-aa8091fd11c0 | -17.07391 | -45.95095 | 2025-06-25 04:10:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3bd14e4b-5a51-3323-ab83-133591dd966e | -17.14599 | -44.7215 | 2025-06-25 04:10:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7980dca8-9491-31a6-beb2-10499c221c33 | -19.45485 | -45.30619 | 2025-06-25 04:10:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a652aa1-5b68-3b7a-8b82-308c1a0ab7bd | -21.80834 | -56.2947 | 2025-06-25 04:10:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20c5497e-1093-378e-a734-24e922284e8b | -21.20477 | -48.51932 | 2025-06-25 04:10:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| db11b5f8-649b-3aa8-a266-44f8eb8b9a3b | -18.09207 | -54.28506 | 2025-06-25 04:10:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57de0931-d91c-342c-b86a-303022f8d4c7 | -20.103 | -55.24559 | 2025-06-25 04:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c58a5dd-e7cd-3816-a5ee-5883453a29af | -22.40426 | -47.09659 | 2025-06-25 04:10:00 | NOAA-20 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf3c25a9-f98a-3436-8c92-aad575da3296 | -20.92643 | -49.09532 | 2025-06-25 04:10:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| e449819f-faee-36bb-8c05-fe9542ef684c | -21.08517 | -48.68503 | 2025-06-25 04:10:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fcc1108a-724d-3c98-a684-c9c3731463b6 | -21.20196 | -48.51406 | 2025-06-25 04:10:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 27a73e7f-7a77-3e65-8911-8fda3c7c8518 | -23.98525 | -48.91762 | 2025-06-25 04:12:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2457137b-5f4c-30e3-b3a8-eb825115b26d | -29.80809 | -51.22743 | 2025-06-25 04:12:00 | NOAA-20 | NOVA SANTA RITA | RIO GRANDE DO SUL | Brasil | 4313375 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| 9153269e-3b7d-3d33-a24d-a7ea90a0c3aa | -27.82924 | -50.30302 | 2025-06-25 04:12:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d1e141e9-1b87-35ac-9b53-2dbaed29c18b | -25.19214 | -49.32765 | 2025-06-25 04:12:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0350cfab-867c-30cf-8a36-403cdd2299fd | -9.553 | -40.3503 | 2025-06-25 04:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 119.9 |
| bb23a785-9e6c-35ed-9d00-075b5fcc715d | -6.1791 | -48.0712 | 2025-06-25 04:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 9c60cc6d-a11a-387c-bbda-448d8766833f | -10.443 | -47.945 | 2025-06-25 04:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 4446e000-4cda-36bd-84a7-454efd6573ba | -9.5534 | -40.3254 | 2025-06-25 04:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 67.8 |
| f7b6e883-c39a-3c2a-89f2-ff5bb6f2ae38 | -9.553 | -40.3503 | 2025-06-25 04:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 352.7 |
| e1346f72-40cc-34c2-aadc-738d408a43cb | -9.5534 | -40.3254 | 2025-06-25 04:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 146.9 |
| 9e8a8421-9a2c-36a8-b9dc-528f3fabc2dc | -10.443 | -47.945 | 2025-06-25 04:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| c9f33541-d794-3679-ae90-a92c89d6cfa8 | -6.1791 | -48.0712 | 2025-06-25 04:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 84ed6cf5-9f2a-3171-bb05-4416199c68e1 | -9.5534 | -40.3254 | 2025-06-25 04:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 81.0 |
| 00076098-3dab-3033-9618-f55f60744609 | -6.1791 | -48.0712 | 2025-06-25 04:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| b04336f0-eeb0-3866-9d47-894e03ff5458 | -10.443 | -47.945 | 2025-06-25 04:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 47.9 |
| c2a92748-4b61-394c-a542-ccb30504cf7f | -9.553 | -40.3503 | 2025-06-25 04:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 129.4 |
| eea6dab7-30fe-3411-a30e-11a3c1b0e92e | -6.1791 | -48.0712 | 2025-06-25 04:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 41d4e40c-1ec6-3b32-b598-313addcdfe9e | -9.553 | -40.3503 | 2025-06-25 04:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 9adaa2ae-1a50-3ae5-800d-c5670f5a93e1 | -10.443 | -47.945 | 2025-06-25 04:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 6185695c-090e-35d1-87fc-f9563cc53810 | -2.54919 | -47.70224 | 2025-06-25 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7beebd1e-441b-3e4d-b478-0a56c2530ae6 | -2.6392 | -47.30705 | 2025-06-25 04:55:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53bb294d-7a83-3633-a952-d3470ac86c92 | -2.55341 | -47.70288 | 2025-06-25 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d018a0f2-62b8-3fab-bae0-5184b9bb0272 | -2.45259 | -47.50643 | 2025-06-25 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a35a666a-7611-30c7-934f-0a8b64574f98 | -2.45008 | -47.50239 | 2025-06-25 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70d6e402-ad2f-38bf-8777-a8ea3375ccf5 | -2.4495 | -47.49773 | 2025-06-25 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a661dba-d577-346a-824d-00cda3404503 | -2.45319 | -47.5024 | 2025-06-25 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc2f7e5c-e745-3ab6-b34f-64ac5a6a61fc | -2.44891 | -47.50174 | 2025-06-25 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c736c7b-9b30-372f-aa5c-3516eafcdf25 | -2.4507 | -47.49837 | 2025-06-25 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54e4d54d-d073-3ec7-90d4-d4a818edbffd | -4.54164 | -48.00771 | 2025-06-25 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 66da2601-46fd-39b6-a440-fb0fcc7b7077 | -9.50232 | -56.0931 | 2025-06-25 04:57:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 745c1933-2332-3e15-83af-261fa054e777 | -8.87062 | -47.27084 | 2025-06-25 04:57:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 26114fe1-71cf-3aed-9c72-01cf58612eb4 | -10.51897 | -47.58187 | 2025-06-25 04:57:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b115333-8bee-3c7b-9bda-93027ed602a6 | -4.54648 | -48.00441 | 2025-06-25 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5147b25-0eed-3034-b2d8-12eb5ccae9c1 | -8.06479 | -43.10654 | 2025-06-25 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1de5b817-e00c-3848-b99f-b2eeed0745f3 | -3.49703 | -51.17498 | 2025-06-25 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20032627-8f81-3088-8e42-55446da5a023 | -8.15272 | -46.82824 | 2025-06-25 04:57:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60ad88fe-ab2b-3003-b6cb-370d77cab617 | -4.53256 | -48.01021 | 2025-06-25 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1284cd19-f77b-3109-b256-c1c06e82b0be | -11.1152 | -44.52425 | 2025-06-25 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6221919b-53c1-30a9-9576-dba80034575c | -6.18397 | -48.06997 | 2025-06-25 04:57:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 4bcb7e98-c5e9-3bfe-9530-3a762e9c5d4e | -9.50842 | -56.09771 | 2025-06-25 04:57:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8ebdd188-43f1-3b95-acfc-41e63d9ae1ee | -6.17903 | -48.07347 | 2025-06-25 04:57:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| a57c7587-7fd0-31ea-8c6e-ef1294b76d2c | -3.6182 | -47.53564 | 2025-06-25 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 36c8da83-b19d-396c-88f3-6f5c46cbc5f9 | -8.58244 | -48.21543 | 2025-06-25 04:57:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3ddd9a1-0ddc-3cf4-9a78-4673a88b153a | -6.17587 | -48.06447 | 2025-06-25 04:57:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1f0c8c9c-de74-3261-9dcb-11516fd12942 | -9.26032 | -47.64423 | 2025-06-25 04:57:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c59ad5c7-e8f3-3296-b331-7d8147e43466 | -7.02545 | -44.56367 | 2025-06-25 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b70f700d-94a7-3bf5-b39d-854b9de1d483 | -6.18338 | -48.07409 | 2025-06-25 04:57:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| bf84e8a5-7da4-3e9f-a91a-99857af1613c | -7.31012 | -45.77023 | 2025-06-25 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README13.md)
