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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a99da66f-4e6e-34e6-adec-38c4cf655e31 | -15.9591 | -59.3887 | 2025-09-22 13:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| c7f5a0d8-45fa-3498-8733-d4f46a9da8a6 | -11.6446 | -44.32 | 2025-09-22 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 7794482c-6bbe-3771-850a-92e6bde4edca | -13.925 | -44.0819 | 2025-09-22 13:00:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| cedf6845-cee9-3584-863d-3c3b4d7406f9 | -12.4186 | -45.0153 | 2025-09-22 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| d5175421-abf0-3426-a8ee-29dc787d0def | -14.9895 | -44.4022 | 2025-09-22 13:00:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 5564c818-772e-3a94-8295-a5f8e9346f8f | -8.2803 | -44.3801 | 2025-09-22 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 2b252299-4966-3ead-ae63-15d3b52b0d22 | -14.9699 | -44.406 | 2025-09-22 13:00:00 | GOES-19 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 7cf166ad-2677-355f-bda9-1a7d1038b79c | -14.4721 | -44.8532 | 2025-09-22 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 243.6 |
| e7953983-6280-37c2-8e7a-af27e6da9edc | -12.4554 | -45.1022 | 2025-09-22 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 149.4 |
| c6941e48-e9bb-317c-a095-b222b2fb26ad | -8.5185 | -44.9291 | 2025-09-22 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| ae3b1cd4-1056-366b-bbd1-8c0c1c3b8c78 | -11.2153 | -49.6008 | 2025-09-22 13:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| d7710fab-a8fe-3528-bb7f-94a06a88cece | -12.7153 | -47.6972 | 2025-09-22 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 959b871c-2016-3ad1-9de2-423e287ba147 | -10.3378 | -46.0835 | 2025-09-22 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| e2ad38ef-4f89-3798-a510-5c15e83da6dd | -5.5773 | -42.1255 | 2025-09-22 13:10:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| 8becf6f0-a563-3b8e-8d6a-55efdd37d44d | -12.6093 | -45.1012 | 2025-09-22 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| e18aa505-732f-3c91-bd8e-43b652af8cba | -12.4186 | -45.0153 | 2025-09-22 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 16bc3605-09a0-3ee0-99e8-e29ea631dd3e | -8.5185 | -44.9291 | 2025-09-22 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 812e968e-59e3-373d-a1d9-2ca66fe75cf8 | -11.6442 | -44.3434 | 2025-09-22 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 120.9 |
| cca1ff01-67af-378a-90d3-d4d07f0ccdba | -12.3592 | -44.0915 | 2025-09-22 13:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 110.1 |
| b9722b47-f662-32bc-ac1f-f41a58405b7b | -12.455 | -45.1254 | 2025-09-22 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 6df35e79-a3dc-354a-a340-09b279cc3717 | -12.0767 | -44.8131 | 2025-09-22 13:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 5e4b6364-50cd-324c-aad6-9e36703fc2dc | -12.4182 | -45.0385 | 2025-09-22 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 7e102f9d-9824-37f7-a556-4415f8193ed4 | -15.7652 | -59.4072 | 2025-09-22 13:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 109066a3-d4ff-366c-9591-9330a9cbb2a5 | -14.8484 | -45.4613 | 2025-09-22 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 6bb5e833-6b64-3c18-9696-8a2451d7dcee | -11.6446 | -44.32 | 2025-09-22 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| d98f3a7d-c016-3012-80b3-210157658c0b | -12.0771 | -44.7898 | 2025-09-22 13:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 2d82fd9e-a1c8-36e5-819f-c620db60a212 | -12.4361 | -45.1052 | 2025-09-22 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 89b909a1-4c2c-36f7-8004-1cddebf9a9d3 | -14.9895 | -44.4022 | 2025-09-22 13:10:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 113.7 |
| d87429be-43c2-3c80-b5d3-e690b96d6d78 | -14.4721 | -44.8532 | 2025-09-22 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 72be0202-edda-3d2d-99ec-37268ea630eb | -8.2803 | -44.3801 | 2025-09-22 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 248.1 |
| 1a2d4d18-399e-30b7-9d78-264e8a5eda8a | -13.925 | -44.0819 | 2025-09-22 13:10:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 5e688054-42c2-3b4a-b698-6805e0cb6817 | -8.2614 | -44.3821 | 2025-09-22 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 619bf64e-b380-3a13-9f99-7285231003a3 | -14.8479 | -45.4846 | 2025-09-22 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 8594db5c-c380-3538-9e98-74a0b8db10a6 | -12.4554 | -45.1022 | 2025-09-22 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 211.3 |
| 498c8198-81d1-390e-9952-2e6abe282a3c | -12.0963 | -44.7868 | 2025-09-22 13:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 7f455bc2-c1c1-3e5d-9bde-2d1be6c6ced9 | -12.1156 | -44.7839 | 2025-09-22 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 05c8b012-8234-3b8c-a347-96e29513a66c | -14.9699 | -44.406 | 2025-09-22 13:10:00 | GOES-19 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 78.0 |
| add0f80e-75a2-39a4-8f8c-896789bada4e | -12.4357 | -45.1284 | 2025-09-22 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 8ff98b50-bac5-341c-a43f-58b0e398cf2d | -14.8675 | -45.481 | 2025-09-22 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| fb046580-8c82-3191-8b5b-db104b525832 | -11.6442 | -44.3434 | 2025-09-22 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 171.8 |
| 27a1e049-8748-3841-9a21-3f553bf64f20 | -14.4917 | -44.8496 | 2025-09-22 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| f73645f0-3e5f-39bd-8c8a-6d9d84d7a64a | -12.4545 | -45.1486 | 2025-09-22 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 1e01dcbf-68e5-31cb-a507-b8c0e54b9d39 | -12.3592 | -44.0915 | 2025-09-22 13:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 1a841b01-df7e-3c42-a8d7-d47fba6b9503 | -11.6446 | -44.32 | 2025-09-22 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 72af2ef3-2f32-36ae-9f29-5a42633b56c1 | -12.455 | -45.1254 | 2025-09-22 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| ed6dcad5-89f1-38b7-8333-c9e95a53913e | -11.1193 | -49.6765 | 2025-09-22 13:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 93ece905-9043-30a4-891c-3e05082ee466 | -8.2803 | -44.3801 | 2025-09-22 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 87e515e9-780e-3adf-949a-a41e4ce7688a | -12.4554 | -45.1022 | 2025-09-22 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 31817ff3-ac8c-3478-847b-1d49c5f6581e | -14.9895 | -44.4022 | 2025-09-22 13:20:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 17b6d294-6a9c-39f0-9129-a85e47c6071a | -12.7153 | -47.6972 | 2025-09-22 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 9d7c5b39-4acc-3f0f-8753-613d85d80efc | -11.4674 | -43.5248 | 2025-09-22 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| ba9f970a-49fd-38bf-a366-e713c5189904 | -15.9591 | -59.3887 | 2025-09-22 13:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 71b42e33-b256-3831-9e9e-2ba153dec903 | -12.4186 | -45.0153 | 2025-09-22 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| d284ecfb-f7fa-3c62-93d8-220b2a14f9ed | -14.4721 | -44.8532 | 2025-09-22 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 212.6 |
| 654aa3f0-d177-39d6-9185-dd1feb8ed656 | -12.0767 | -44.8131 | 2025-09-22 13:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 224c405c-daee-3491-8c73-3ab59a6a3392 | -14.9699 | -44.406 | 2025-09-22 13:20:00 | GOES-19 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 103fa087-6129-3901-b70a-815763711486 | -12.0963 | -44.7868 | 2025-09-22 13:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 133.6 |
| fe9ad00d-d8ec-35e7-b7fc-b8cd981ce80a | -11.2153 | -49.6008 | 2025-09-22 13:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| fd2dee3a-990f-3b68-b5ee-16d2570dc045 | -12.7149 | -47.7195 | 2025-09-22 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| b9f6a2c7-efad-3021-9914-39224dc54120 | -15.9594 | -59.3687 | 2025-09-22 13:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 107.2 |
| e6bdd5f3-a801-363d-bc2f-f20c349739e1 | -12.4182 | -45.0385 | 2025-09-22 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 3b1dd155-7147-3c78-be95-8c36281d996c | -13.925 | -44.0819 | 2025-09-22 13:20:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 1a76a3d8-100e-3c09-9f77-b232a67a8c97 | -12.1156 | -44.7839 | 2025-09-22 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 7a9e8093-cd62-349b-b9c8-366f8e4ee2b5 | -11.1 | -49.7003 | 2025-09-22 13:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 82864bd7-56d3-3934-a2d3-2c2e09c3a4b2 | -5.5773 | -42.1255 | 2025-09-22 13:20:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 86.8 |
| b3e439b0-5d4f-349a-a085-c1ca29040171 | -14.989 | -44.4259 | 2025-09-22 13:20:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 5fc45408-6d13-39fd-936d-e6c23825bb67 | -14.2613 | -44.7041 | 2025-09-22 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 2b051f1b-3615-343d-b4ac-478c6929ca45 | -12.4357 | -45.1284 | 2025-09-22 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| df639928-8e36-3bb9-8183-616f624ae4d8 | -8.5185 | -44.9291 | 2025-09-22 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 2b47644d-d521-334e-8954-2f9a3daca118 | -12.4353 | -45.1515 | 2025-09-22 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| d1b44c49-4504-3e25-994f-a2d229917e2b | -12.0771 | -44.7898 | 2025-09-22 13:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| e54d656d-f82b-307c-bf90-5a58f4d11a77 | -12.405 | -44.7156 | 2025-09-22 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| ee9cc52c-4a9a-3480-bbe0-832e27861562 | -5.5585 | -42.1269 | 2025-09-22 13:20:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 76.2 |
| 6fb39290-ddab-305c-b12e-8bd7e033d3bf | -12.0767 | -44.8131 | 2025-09-22 13:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| dce8a60d-9d4e-30e3-a171-00002a1c1754 | -8.2936 | -44.8154 | 2025-09-22 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 69.9 |
| d8bd54e1-539a-3e0d-83c8-c09078cd4f1e | -14.9699 | -44.406 | 2025-09-22 13:30:00 | GOES-19 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 130.9 |
| ff0ffb7c-d99c-3d6b-b637-dcfd96c17c61 | -12.3592 | -44.0915 | 2025-09-22 13:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 930ab288-0ef3-3c3b-a15b-143a1bfae62b | -12.0963 | -44.7868 | 2025-09-22 13:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 6873cf65-30de-3c90-9379-0de6c08a5a68 | -5.5585 | -42.1269 | 2025-09-22 13:30:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 79.6 |
| 82deef13-d51f-3d08-84ae-aa434044c1f4 | -8.2748 | -44.8174 | 2025-09-22 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 31d935ee-7f58-32e9-b03c-3dbb369981fa | -18.5983 | -45.0287 | 2025-09-22 13:30:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 168.5 |
| f41f69c1-1b9b-32de-9c44-3f886351ed8f | -12.1156 | -44.7839 | 2025-09-22 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 3285b74a-a8de-3563-aebd-eb8e9908bc50 | -11.2306 | -46.1722 | 2025-09-22 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| c973f772-7573-398b-b99c-d3b2e9137eb1 | -12.7149 | -47.7195 | 2025-09-22 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 91359e21-fa7e-3543-b786-4edfd815ed4c | -14.4721 | -44.8532 | 2025-09-22 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 169.9 |
| d6b35020-b1af-3cc5-8cba-8f3d7a5825a5 | -12.7337 | -47.7391 | 2025-09-22 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| d7496c07-0be2-32a1-86fa-d25c79f3e877 | -11.467 | -43.5485 | 2025-09-22 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 1f042276-9ecf-324b-997d-2fa2c1c645ff | -11.6446 | -44.32 | 2025-09-22 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 133.4 |
| e47f9882-b2dd-30c0-8072-cb8a4b48993c | -11.7687 | -44.8826 | 2025-09-22 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 48f6a0cd-20ef-3047-b034-29b3a19e65b5 | -12.7153 | -47.6972 | 2025-09-22 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 590fe3c0-7d93-3b9b-8a8e-4a539419d451 | -11.2153 | -49.6008 | 2025-09-22 13:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 85d5ab64-8f02-30d2-a3fc-050e419a4414 | -11.7682 | -44.9059 | 2025-09-22 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 0529e129-3f55-3680-85af-5f545a9ac004 | -8.5185 | -44.9291 | 2025-09-22 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 106.7 |
| cfec00bb-a969-32de-867b-1053d92abe58 | -5.5583 | -42.1507 | 2025-09-22 13:30:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 82.8 |
| 3d8b189a-945a-3580-be12-3ec4945f1634 | -11.6442 | -44.3434 | 2025-09-22 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 235d49db-6c5a-3b17-9776-d1d5b772e63f | -14.989 | -44.4259 | 2025-09-22 13:30:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 6a44c41d-2443-3b57-a815-989e620482c6 | -5.5771 | -42.1493 | 2025-09-22 13:30:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 84.7 |
| c2d391a2-0ba0-3664-b616-0e26b3219de4 | -8.2803 | -44.3801 | 2025-09-22 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 1705c44c-48cb-3ae1-84d4-a9dab68eb98e | -12.0771 | -44.7898 | 2025-09-22 13:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 499d5582-0d8f-36ac-a739-2f7de16db339 | -10.3572 | -46.0585 | 2025-09-22 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |


[Clique aqui para ver as próximas entradas](README46.md)
