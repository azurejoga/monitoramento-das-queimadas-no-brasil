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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f15fd706-925e-3bb3-95ad-bda27590873b | -17.3158 | -43.6674 | 2025-10-26 13:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 128.1 |
| f9922d7a-e61e-3643-a9db-9739d9065bfe | -5.2355 | -44.87 | 2025-10-26 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| b6871978-77b5-3bb3-ab74-4a706117c4cf | -15.8547 | -53.5771 | 2025-10-26 13:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 196dcf58-7aef-3b4e-81ba-aa72f3c87c5a | -16.1901 | -45.0841 | 2025-10-26 13:30:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 8b16dff0-aaee-3e6d-aa43-2a511ca48829 | -13.0564 | -45.8829 | 2025-10-26 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 4b82b1a2-2ee0-33f1-82c0-1a573fc42e8f | -3.3344 | -44.8586 | 2025-10-26 13:30:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 37d28b87-8f65-3289-b903-c720e97582ae | -3.7896 | -43.4153 | 2025-10-26 13:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 2041e9df-b389-3ae8-9f4b-7c700477f2dd | -3.964 | -45.4173 | 2025-10-26 13:30:00 | GOES-19 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 0698eddc-5ec5-3997-9af8-7ca51b956b82 | -13.2482 | -47.9768 | 2025-10-26 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 0123c8e0-c89d-3480-b88b-7a454f6a2ec6 | -17.3165 | -43.643 | 2025-10-26 13:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 230.3 |
| c230ddde-6e6d-313e-9a8c-0de27661566d | -5.4676 | -37.8278 | 2025-10-26 13:30:00 | GOES-19 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 138.9 |
| 3af19521-d693-3325-8be6-45d81226f437 | -17.3365 | -43.6383 | 2025-10-26 13:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 8e7fe539-493a-3c5b-a8ad-eaba1cc0e4ba | -4.4618 | -43.4248 | 2025-10-26 13:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| b7d6919b-98ea-3995-8ec5-43f3871ddccf | -15.2454 | -50.7564 | 2025-10-26 13:30:00 | GOES-19 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| f1378d5b-6d4e-3727-ba8f-a1e4155c9e63 | -12.3165 | -47.4855 | 2025-10-26 13:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| f4deb813-302c-3177-b273-053cefe5dabb | -15.2649 | -50.7535 | 2025-10-26 13:30:00 | GOES-19 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 89.3 |
| fa5ef2df-4f95-3f8a-b61a-d796e4056148 | -11.5311 | -48.8247 | 2025-10-26 13:30:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 16da49d7-dcb7-32fa-b9b7-d5c5c9c578c8 | -13.3262 | -47.9207 | 2025-10-26 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 56.4 |
| ce79a015-51b1-3fba-995e-78fcc8925f33 | -12.3634 | -48.1016 | 2025-10-26 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| ca5e397e-be85-3087-b556-e45c40de2fea | -12.3169 | -47.4631 | 2025-10-26 13:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 8235a520-af9c-3a2e-bc2e-b69633c300c6 | -14.6031 | -53.1087 | 2025-10-26 13:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 5c350488-3e5d-3b1d-b5b8-c17ebefa5cbe | -5.8857 | -41.3089 | 2025-10-26 13:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 110.2 |
| 7b6be132-6fd6-3f28-8d63-e0d42d3de14c | -5.2542 | -44.8688 | 2025-10-26 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| e5ccae0b-8388-32bc-bff0-70191dcb5cbe | -4.8935 | -43.2115 | 2025-10-26 13:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| c35fe070-0ac9-334a-ac94-2ddba06de361 | -11.1419 | -55.1869 | 2025-10-26 13:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 1603291c-427d-3a05-a179-f4e7e484d19c | -12.3165 | -47.4855 | 2025-10-26 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 7dc22dd5-d994-396b-89f7-b27adff2252d | -4.8931 | -43.2582 | 2025-10-26 13:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| bd1d21b5-43fe-33d6-aee9-078412249276 | -16.1901 | -45.0841 | 2025-10-26 13:40:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 8d19ecb4-cb8f-3ecc-b8db-a2c5a3bab8a4 | -17.3165 | -43.643 | 2025-10-26 13:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 167.4 |
| be6b495c-40c3-3faf-af8f-e5a3b1af63d4 | -13.2482 | -47.9768 | 2025-10-26 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| cbbe7d9b-6c85-3464-bdf5-d065f2a21d9e | -13.547 | -49.5434 | 2025-10-26 13:40:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 62.8 |
| a19d0fee-5dfc-3026-8bc6-43126f69e37b | -3.6533 | -41.2464 | 2025-10-26 13:40:00 | GOES-19 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 90.4 |
| f90ab88a-85ee-301f-a7a0-2d296806dc2b | -4.4618 | -43.4248 | 2025-10-26 13:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 34ac5736-97e5-3052-8fc8-d7d9584e9d1b | -3.964 | -45.4173 | 2025-10-26 13:40:00 | GOES-19 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 163.8 |
| 9083a793-4def-3038-bf39-e4a772941d85 | -17.4311 | -46.884 | 2025-10-26 13:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 4494dff1-bd1d-3294-bea8-cbdc4d81250b | -6.1735 | -42.6221 | 2025-10-26 13:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 91.1 |
| 236d1058-6018-3c95-881d-f2325e5f9da0 | -12.2977 | -47.4658 | 2025-10-26 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| a0152c1b-0c3c-3a75-90b8-a9590db693f7 | -14.6031 | -53.1087 | 2025-10-26 13:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 35da4422-4873-3101-9d32-91e223255ab4 | -14.9235 | -52.454 | 2025-10-26 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 6cdd302d-cbc8-33d4-8be0-322931b68f69 | -3.7661 | -47.5727 | 2025-10-26 13:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 169.3 |
| d0ae9e45-eda1-3f3b-aae5-a878d671a9b1 | -3.7896 | -43.4153 | 2025-10-26 13:40:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 71b63e7c-e529-36f5-936c-a7ae6f4fc633 | -4.8933 | -43.2349 | 2025-10-26 13:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 167.3 |
| d1b7905a-6e9a-33bc-9422-210579efbae8 | -14.9231 | -52.4753 | 2025-10-26 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 801eaae4-bb17-3cc5-8d2e-de549e01bbaf | -13.0315 | -47.2033 | 2025-10-26 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 37d54774-95b4-3895-a10d-2f6cb0848795 | -12.3169 | -47.4631 | 2025-10-26 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| a46c61ac-8b2c-324e-bbc2-124328eb208e | -17.3158 | -43.6674 | 2025-10-26 13:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 15396cff-42f5-3a84-98cc-54a99edf567a | -6.2567 | -41.8298 | 2025-10-26 13:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 100.9 |
| d789058c-f92b-31e8-aef0-eeaf4d9f6a1b | -5.4676 | -37.8278 | 2025-10-26 13:40:00 | GOES-19 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 144.0 |
| 2784d735-ca60-311d-9260-e456d46b3684 | -5.4673 | -37.8536 | 2025-10-26 13:40:00 | GOES-19 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 253.9 |
| c0b56f8f-0537-3de0-b4c3-3f4a0433cd87 | -5.2542 | -44.8688 | 2025-10-26 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 504cf7e4-97ad-3c9f-b7e0-62f630e6d455 | -15.8547 | -53.5771 | 2025-10-26 13:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 942f681d-f324-3e82-b783-ac364eb77933 | -3.7896 | -43.4153 | 2025-10-26 13:50:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| c40b3aa9-2995-3fb7-a134-9636321da0ec | -5.834 | -40.828 | 2025-10-26 13:50:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 95.1 |
| 138227f2-b7d4-355b-82dc-e336e6ddd091 | -13.2586 | -54.3902 | 2025-10-26 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| e8a055e8-51c9-3818-bae5-15ec299149de | -4.8935 | -43.2115 | 2025-10-26 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| fb208b78-5dbe-3747-879c-3a0f9d26d54a | -4.4618 | -43.4248 | 2025-10-26 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 4b32d3f3-4c57-3d4e-8989-1bcbfa305887 | -6.1735 | -42.6221 | 2025-10-26 13:50:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 70.1 |
| 42d19157-8859-31a0-bae9-2e8752e47c39 | -3.0148 | -41.6851 | 2025-10-26 13:50:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 105.4 |
| 054a56aa-77e5-3a11-9ae0-ab90a3cb3877 | -13.8949 | -48.4364 | 2025-10-26 13:50:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 5adbf466-dc11-3d3a-b91f-34c341fcbdec | -13.8953 | -48.4141 | 2025-10-26 13:50:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 91d7bd1d-7aed-3114-9d29-e21f68ca2a26 | -3.6918 | -44.2044 | 2025-10-26 13:50:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 33e4ca18-7cce-3723-a4c1-5d8a46e98495 | -13.2482 | -47.9768 | 2025-10-26 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| d0f2ab27-e6fb-3d97-850c-f495dcbf54a9 | -2.8994 | -42.3552 | 2025-10-26 13:50:00 | GOES-19 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 8666f502-9ecd-3f5f-9c81-61d5c746ccb2 | -14.6031 | -53.1087 | 2025-10-26 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 109.9 |
| a00a5206-0088-37bc-9ad8-53b264488885 | -17.4311 | -46.884 | 2025-10-26 13:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 820695ea-6cfb-323a-a5a7-54305eb70010 | -3.7661 | -47.5727 | 2025-10-26 13:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 132.2 |
| eb933ba9-3e99-38c2-b2c7-991055cf851f | -17.3158 | -43.6674 | 2025-10-26 13:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 173.8 |
| c8a2f62e-8366-3116-b2bb-c122fdcbd340 | -4.8933 | -43.2349 | 2025-10-26 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 207.0 |
| d3768b17-b272-3990-8190-1c050e9081b1 | -6.2567 | -41.8298 | 2025-10-26 13:50:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| 92c5cd77-4b49-3242-8ef6-b4ac77b35355 | -13.0315 | -47.2033 | 2025-10-26 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 3ab5bb8f-6eea-3a92-affd-20e07664b7ea | -17.4317 | -46.8608 | 2025-10-26 13:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 106.4 |
| c2b36afc-7a13-3304-9687-64cf2af4eb1b | -5.014 | -37.8416 | 2025-10-26 13:50:00 | GOES-19 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 128.0 |
| 195930e2-4d54-3056-a67b-cbcd79f0a60e | -12.3165 | -47.4855 | 2025-10-26 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| ad9e89fa-5206-3f1c-8db3-40265ef79cd6 | -4.8931 | -43.2582 | 2025-10-26 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| f24548b9-3501-3b33-8916-cf69d14d4ba0 | -6.2306 | -42.5463 | 2025-10-26 13:50:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 65.3 |
| b478d86a-85da-3e40-ba97-72c8081447a5 | -3.964 | -45.4173 | 2025-10-26 13:50:00 | GOES-19 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 92.2 |
| e071d421-2733-3c4b-8afa-f21f128db3ca | -3.7024 | -42.3892 | 2025-10-26 13:50:00 | GOES-19 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| b7b17264-9f53-3495-89d5-77ce32632e33 | -16.1901 | -45.0841 | 2025-10-26 13:50:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 246.1 |
| 63708ab1-72ce-3106-b46f-873b06208741 | -4.3239 | -41.7839 | 2025-10-26 13:50:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| f7f0e0dc-46bb-3ada-b8c0-2658fd695da0 | -11.7428 | -51.1897 | 2025-10-26 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.8 |
| f28e091c-1af0-3cfe-90db-712da2083ba1 | -3.9166 | -44.0097 | 2025-10-26 13:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 7c797af6-e8df-3b4e-923a-4fbc55c21d9c | -17.3165 | -43.643 | 2025-10-26 13:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 328.1 |
| 6fcefc45-e20b-3d26-be3f-992271257bf1 | -12.3169 | -47.4631 | 2025-10-26 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 126.8 |
| d0d1df50-7c4a-3c3f-9a61-74e02b1889bb | -13.2777 | -54.3882 | 2025-10-26 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 126.2 |
| 554b68ea-e6fc-3260-9fbd-e515c625e46e | -5.4676 | -37.8278 | 2025-10-26 13:50:00 | GOES-19 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 145.9 |
| 2e201783-5b3b-396c-b01a-fb143b16f5e1 | -4.3237 | -41.8078 | 2025-10-26 14:00:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| 79f9046a-9049-3872-b65f-7c8e3180fbc4 | -3.7024 | -42.3892 | 2025-10-26 14:00:00 | GOES-19 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 120.0 |
| 731a597f-d8cf-362f-b150-767e04438403 | -2.8994 | -42.3552 | 2025-10-26 14:00:00 | GOES-19 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 7f891470-30db-3a2a-95bf-4b47be286938 | -12.3165 | -47.4855 | 2025-10-26 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| ec5ec39b-acde-3d0f-9f94-4f1a0c8a62e9 | -16.1703 | -45.0881 | 2025-10-26 14:00:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 97.3 |
| caf81253-f4d9-37d9-9565-8a22cf1e77af | -13.8949 | -48.4364 | 2025-10-26 14:00:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 3863066b-ddf0-3930-87ec-754732142cce | -13.2482 | -47.9768 | 2025-10-26 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 6168e9c9-4312-3a9e-b97e-6cf1752d381c | -13.2777 | -54.3882 | 2025-10-26 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 144.9 |
| cc963916-27aa-38df-8ed5-b678197d243e | -6.7832 | -45.4121 | 2025-10-26 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 78b25690-e3f8-3760-8305-d28328b8a38a | -12.3169 | -47.4631 | 2025-10-26 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 121.3 |
| e148d4f6-36f3-3f3d-8c80-dd779155306a | -12.363 | -48.1238 | 2025-10-26 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 750e7c73-4350-380f-a5df-6e5fb63f7e76 | -3.6531 | -41.2705 | 2025-10-26 14:00:00 | GOES-19 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 85.5 |
| 099ce89b-d793-38cc-bcc1-c4a49d04e19b | -13.8945 | -48.4586 | 2025-10-26 14:00:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 8163c860-0519-39ba-854f-6a6f330baf04 | -6.9667 | -44.0246 | 2025-10-26 14:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 5544c486-a2b8-3207-aaba-a8cc8a77263a | -7.8138 | -43.9894 | 2025-10-26 14:00:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |


[Clique aqui para ver as próximas entradas](README59.md)
