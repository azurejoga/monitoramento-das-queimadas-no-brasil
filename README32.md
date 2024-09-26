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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d4378e2-ee06-3141-8502-c36b57c6f740 | -9.086 | -61.1245 | 2024-09-26 01:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| e000b6a5-bac9-3709-b99a-1755d454832b | -9.1046 | -61.1237 | 2024-09-26 01:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 7c650eaa-585e-3527-91b0-f09d1f31b4a1 | -9.1349 | -65.564 | 2024-09-26 01:15:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| df855581-d5b4-3809-93ae-d0a3e6caf93c | -9.1535 | -65.5634 | 2024-09-26 01:15:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 0a5538b8-71ad-32ad-a3d0-58e09865df21 | -9.3571 | -65.6315 | 2024-09-26 01:16:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| e85a5e63-e5c7-3ad3-be14-c59f22866334 | -9.6015 | -50.1566 | 2024-09-26 01:16:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 126.9 |
| 92d97048-532f-379d-b553-85e931a2be3e | -9.6018 | -50.1352 | 2024-09-26 01:16:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| e932f1e6-e3d3-3d5c-82bb-274d696c2e4c | -9.6147 | -57.7765 | 2024-09-26 01:16:01 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 30.6 |
| f07e9c1c-348c-390a-8091-c7b04bf61a7d | -9.6149 | -57.7568 | 2024-09-26 01:16:01 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| a7cd7488-b230-3699-a09a-508da003b818 | -9.8083 | -68.8152 | 2024-09-26 01:16:03 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 0333143f-7882-3e2a-941f-f6d34f042a2c | -10.3713 | -58.9056 | 2024-09-26 01:16:05 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| cb730ddb-aa41-3e76-ad1b-41a8ae878c1c | -10.3882 | -67.8737 | 2024-09-26 01:16:06 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 62.8 |
| b01c3d17-aa20-3178-a6e9-49e914be26db | -10.9107 | -57.411 | 2024-09-26 01:16:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| a5a767df-8c7d-305a-bbf7-2fdf8aa20869 | -10.9928 | -44.415 | 2024-09-26 01:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| af6e372b-98ac-3020-9766-57e7fd1ccd55 | -10.8915 | -57.4521 | 2024-09-26 01:16:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| dec92937-1bd0-354e-a153-bd8f8c6f3852 | -10.8917 | -57.4322 | 2024-09-26 01:16:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 655e11e6-da10-39af-a709-6da64bdce73f | -10.9264 | -54.2692 | 2024-09-26 01:16:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 4bd01f69-852e-3fc8-b00d-d54c6b609d02 | -10.9105 | -57.4308 | 2024-09-26 01:16:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 132.9 |
| ba54bf11-85ef-336c-9bdb-34ff9b1735c8 | -11.1354 | -46.1623 | 2024-09-26 01:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 5c7e73ae-b8a0-36f8-911e-c6c529bc47d3 | -11.2034 | -54.7752 | 2024-09-26 01:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 0d01d36b-1813-31b7-81fa-21bde35c3897 | -11.2599 | -65.299 | 2024-09-26 01:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 364fbe81-79d0-3b2e-b8cf-32eb60182422 | -11.26 | -65.2801 | 2024-09-26 01:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 82.4 |
| f41ecb97-7e9a-3d88-a514-aab761c7f4a5 | -11.955 | -60.363 | 2024-09-26 01:16:14 | GOES-16 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 340d78c6-6086-3d1d-996d-dba7ad382076 | -12.2367 | -45.5045 | 2024-09-26 01:16:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 88fb59b1-2457-30eb-a881-492865bc7f5b | -12.2371 | -45.4815 | 2024-09-26 01:16:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 6d076cb3-1797-37f1-846d-fb605ee6fb1e | -12.5085 | -53.498 | 2024-09-26 01:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 90d73410-a77a-3f7b-8967-b6481fcde1e8 | -12.5276 | -53.496 | 2024-09-26 01:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 122.8 |
| 5d8deca0-6621-3dc0-b6ec-55ce9cad5ecc | -12.8411 | -62.6874 | 2024-09-26 01:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 64aa21b8-43ba-3198-afcf-8c9dab015ebf | -12.822 | -62.7078 | 2024-09-26 01:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 62281cbb-cdc2-39fd-a156-0ec3d8984189 | -12.841 | -62.7067 | 2024-09-26 01:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 146.6 |
| bcfe9d87-b93c-3384-a0b3-8914413abfd0 | -12.8222 | -62.6886 | 2024-09-26 01:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 41.8 |
| f7903b1e-597a-3f9b-82cd-29d41f821959 | -13.0295 | -57.2985 | 2024-09-26 01:16:20 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 9ae607bf-8398-3c24-8d4f-71f3931cc393 | -14.4439 | -45.2555 | 2024-09-26 01:16:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 38009f25-0545-3550-8d65-5ca441408890 | -14.4444 | -45.2321 | 2024-09-26 01:16:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 13087771-f176-3797-bc4c-ffd6d95b1c82 | -14.4634 | -45.252 | 2024-09-26 01:16:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 248df9de-eece-38e1-8dec-a3c3c91138b6 | -14.4639 | -45.2286 | 2024-09-26 01:16:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 6313ee22-469a-34f3-9eef-50c83d0a5a43 | -14.9544 | -57.9413 | 2024-09-26 01:16:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 95778413-cf9c-3617-a04b-58f748f3ea79 | -14.9541 | -57.9615 | 2024-09-26 01:16:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 41.4 |
| f8c10d39-aa44-3e15-b17c-d24a5e1425e5 | -16.9726 | -57.9514 | 2024-09-26 01:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.0 |
| 2ac3c825-1051-3293-83aa-c76503d034a2 | -17.0995 | -56.1504 | 2024-09-26 01:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.9 |
| 0789ff69-6554-3eb3-8247-8d69673aeaa1 | -16.9925 | -57.9288 | 2024-09-26 01:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.1 |
| 41041504-41d1-3cc7-bb7e-29967d13f741 | -16.9922 | -57.9492 | 2024-09-26 01:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.2 |
| a83e2da7-f37f-34d4-9b33-9d24bfbd1041 | -16.9729 | -57.931 | 2024-09-26 01:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.2 |
| 4de745b3-2c25-358f-80b8-6071d96eb5f8 | -19.929 | -43.7959 | 2024-09-26 01:16:56 | GOES-16 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 54.6 |
| 30e97bd4-d045-3ebd-8bf8-2f4ce98a488a | -20.4197 | -41.8798 | 2024-09-26 01:16:58 | GOES-16 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 102.0 |
| dc471e0b-4b2e-34b4-b683-1b76c60a4483 | -20.4206 | -41.8541 | 2024-09-26 01:16:58 | GOES-16 | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.2 |
| a51ab417-a90a-3403-bec4-8221c55085c3 | -20.5876 | -51.5026 | 2024-09-26 01:17:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.1 |
| f78bb70b-884e-3d75-a186-86d40fde06e0 | -20.6074 | -51.5209 | 2024-09-26 01:17:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.8 |
| 1e71920c-0d1f-3f9f-8092-6a310b256c26 | -20.608 | -51.4986 | 2024-09-26 01:17:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 256.6 |
| ffe45b14-e639-3999-9811-05ea360ba22b | -20.6086 | -51.4762 | 2024-09-26 01:17:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.0 |
| 06b6a4b0-a06a-3386-a59e-1298ca631be6 | -21.9374 | -48.5688 | 2024-09-26 01:17:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 598b4ada-0537-3122-9bd0-3a098a8ae2bb | -21.9381 | -48.5453 | 2024-09-26 01:17:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 7bdaab18-09c9-38fc-b0de-8c8ccd80f2c5 | -1.0553 | -53.3553 | 2024-09-26 01:25:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 345eac19-ad2c-301e-8cf4-519f3f11e128 | -2.6601 | -57.5507 | 2024-09-26 01:25:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 1f3f6f07-0625-3ba2-81c6-342b95d7aad9 | -2.6785 | -57.531 | 2024-09-26 01:25:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| e16dc428-dcd6-3c53-8fde-6ce6091b46e1 | -2.6968 | -57.5307 | 2024-09-26 01:25:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 63ab39bd-4a89-35c5-b0c6-ec1051ab961d | -3.3158 | -53.2122 | 2024-09-26 01:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 7b4fc366-124e-38ff-9e85-ce701ca22c25 | -3.3342 | -53.2117 | 2024-09-26 01:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| e12b421d-8402-31fc-8f87-cb8cdc8f012b | -3.3505 | -53.7775 | 2024-09-26 01:25:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| f21c4bc2-220b-32e2-93ff-437c6a01406a | -3.5673 | -50.3794 | 2024-09-26 01:25:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 20f73d95-8088-355e-8b6a-4a9018b424b0 | -3.7281 | -47.7483 | 2024-09-26 01:25:27 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| fdc74a73-68b0-3968-abce-13997eb29a3f | -3.7282 | -47.7266 | 2024-09-26 01:25:27 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 234.6 |
| 6fec3af3-b207-3eed-8607-7c2c86f6a8c4 | -3.8008 | -41.5989 | 2024-09-26 01:25:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 70.6 |
| 626a4d91-69bf-3bae-8c5b-e3fecd9bd486 | -3.801 | -41.575 | 2024-09-26 01:25:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 47.2 |
| f55fc755-7775-376b-88c3-22a519eac154 | -3.9208 | -46.4459 | 2024-09-26 01:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 74.6 |
| db2d02a2-a949-3204-bcdb-578b56875df8 | -6.7839 | -59.3245 | 2024-09-26 01:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| a1c8e6fb-1b10-3ef5-9b1e-7c6eaf868339 | -6.784 | -59.3052 | 2024-09-26 01:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 308fffad-a57d-3fbd-b76e-eb28c96ad67c | -6.8024 | -59.3044 | 2024-09-26 01:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 3dae9ae9-14dc-3252-a003-c73ec6d4aab3 | -6.9305 | -63.1241 | 2024-09-26 01:25:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 2c3994a0-3352-3e83-8d62-5212ae6fb1b7 | -6.9306 | -63.1053 | 2024-09-26 01:25:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| d7e1275a-de93-3dc4-adba-b450654bf418 | -6.9489 | -63.1236 | 2024-09-26 01:25:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| e48da2b3-a01b-30dc-9b7b-746a15628928 | -6.949 | -63.1048 | 2024-09-26 01:25:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 48dcf294-416a-39fe-9492-fcc6516f2dba | -7.2905 | -61.106 | 2024-09-26 01:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| e6a8957d-ab95-35cf-ab15-59dac8ad10f9 | -7.3636 | -55.5334 | 2024-09-26 01:25:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 08d20b17-72b8-32cb-bd1f-168a466e9ad5 | -7.3637 | -55.5134 | 2024-09-26 01:25:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 299.6 |
| c1bc5a4c-c935-39fe-9dae-c1493766ca03 | -7.3639 | -55.4935 | 2024-09-26 01:25:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 218.7 |
| c5c4598a-33b3-3216-b7cf-626ad193733f | -7.3821 | -55.5324 | 2024-09-26 01:25:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| b52673bf-dac6-3352-9a84-9ae6fb25b944 | -7.3823 | -55.5124 | 2024-09-26 01:25:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 203.4 |
| ed2401f6-4b02-31ae-8feb-054694434e1a | -7.3824 | -55.4924 | 2024-09-26 01:25:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 159.5 |
| ca047bc4-a25f-3a50-a1fb-b61c2004567e | -7.797 | -54.7263 | 2024-09-26 01:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 1e03611f-3fd2-3c27-8ba7-1e1a461f8536 | -7.8154 | -54.7453 | 2024-09-26 01:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| a409d44c-0c14-3eb2-a1ba-244d0bb5b7e9 | -7.8156 | -54.7252 | 2024-09-26 01:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 73bb2d9c-e2a0-3fe5-bf66-42c8fd6c245e | -8.3155 | -54.9956 | 2024-09-26 01:25:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 47081e5e-b297-3103-b535-85221aa31334 | -8.7087 | -54.7881 | 2024-09-26 01:25:56 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| d5227d23-7d54-35b0-89fc-9ecf7cb1e378 | -8.8098 | -58.2172 | 2024-09-26 01:25:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 1c92073f-7214-3546-b755-147f8f8547b5 | -8.9244 | -67.1889 | 2024-09-26 01:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 350914c6-b000-34b5-b740-05df2b5d5cf4 | -9.086 | -61.1245 | 2024-09-26 01:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 051e23e4-ba21-3f59-9794-80995aab91a9 | -9.1035 | -61.2769 | 2024-09-26 01:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 61c9d3b1-4e9a-3bc3-8bbe-15669f06086f | -9.1046 | -61.1237 | 2024-09-26 01:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 35eeeac6-906a-355f-a391-e89144e33072 | -9.1349 | -65.564 | 2024-09-26 01:25:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 60ea8801-a020-3858-9df5-cb96cdf06119 | -9.135 | -65.5453 | 2024-09-26 01:25:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| f01b9751-0171-3417-9248-0ae676714bc5 | -9.1535 | -65.5634 | 2024-09-26 01:25:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| ea81f238-fa31-39a1-bc95-9d965d84a02d | -9.3571 | -65.6315 | 2024-09-26 01:26:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 78af6ba5-6217-35e8-b2ad-de50bfda756f | -9.6015 | -50.1566 | 2024-09-26 01:26:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 10932948-f2ea-3fb6-a3b8-03aa69ba2484 | -9.6147 | -57.7765 | 2024-09-26 01:26:01 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 29686bfe-0c6b-3c7c-ab69-718361878976 | -9.6149 | -57.7568 | 2024-09-26 01:26:01 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 34419ae8-52d8-3879-9bf9-69832078d586 | -9.8083 | -68.8152 | 2024-09-26 01:26:03 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 46.3 |
| ba009df0-a5e3-3884-8192-6610a620d5f4 | -10.3713 | -58.9056 | 2024-09-26 01:26:05 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| add5f69a-a232-3bd0-a99e-0dcc1f5d099b | -10.3882 | -67.8737 | 2024-09-26 01:26:06 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 134f0c24-271e-3a60-b68b-a7be1e9096b9 | -10.9928 | -44.415 | 2024-09-26 01:26:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |


[Clique aqui para ver as próximas entradas](README33.md)
