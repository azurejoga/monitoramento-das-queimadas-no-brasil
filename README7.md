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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 656654a1-ba8f-33dc-9c72-b3d50b6dd9c3 | -9.0799 | -65.4349 | 2025-08-31 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| e6325113-73cc-33b7-bfa4-e0e6ddbf22d3 | -14.5448 | -51.9943 | 2025-08-31 00:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 8775f7d7-b7f6-3f39-9930-ad3bae9281bf | -12.9192 | -56.9873 | 2025-08-31 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| bb9fb76c-d608-3977-af11-1a1ef651eac2 | -8.8337 | -66.7275 | 2025-08-31 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 49a6040b-221e-3de6-b5a8-b67f085a447c | -11.3116 | -43.6664 | 2025-08-31 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| e5fd7d0e-4032-3152-9d17-f4167b81109c | -13.4986 | -46.9517 | 2025-08-31 00:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| ca08626f-795d-331d-99be-6128d63f0f3d | -8.744 | -62.379 | 2025-08-31 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 713b958a-7324-36b8-9387-0230943b65de | -12.3287 | -45.7201 | 2025-08-31 00:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| ca63f38b-11d8-3f5c-b606-1df47cd87570 | -9.0613 | -65.4542 | 2025-08-31 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 134226ce-2fa7-3d59-a2e1-25259f432eaa | -13.3632 | -46.9727 | 2025-08-31 00:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 68.5 |
| ce20fe4d-cbfe-31d4-b12e-2c0a56ef5137 | -11.3112 | -43.69 | 2025-08-31 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 9e70e413-6a7f-366f-90fd-a49a8d0e31cf | -10.1359 | -58.0183 | 2025-08-31 00:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 904b9b83-d36d-3da5-95ce-821d281626e8 | -12.3095 | -45.723 | 2025-08-31 00:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |
| ac7a0ae5-22c4-372e-803a-0df982a20ccf | -18.6051 | -50.192 | 2025-08-31 00:40:00 | GOES-19 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 56.0 |
| 02a2f2d3-9cf2-383a-9300-fd267a75b6a3 | -19.0926 | -48.3106 | 2025-08-31 00:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 6de7116a-46f7-3fd0-b897-53ff6ac350c5 | -8.8522 | -66.727 | 2025-08-31 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| d0945206-1076-3fdc-9f59-9b04ebae49f3 | -11.3509 | -43.6133 | 2025-08-31 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 5320edbf-71f7-3580-b7ec-ca8e030b2bc0 | -9.0799 | -65.4536 | 2025-08-31 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 8d58d41f-970a-3f58-8578-ac1c883ae924 | -8.6487 | -62.8376 | 2025-08-31 00:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 1648645e-1501-3458-87b4-3ff77df5f150 | -11.3504 | -43.637 | 2025-08-31 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 47d0c7b5-d2a7-336f-a54f-34114b628090 | -14.5452 | -51.9729 | 2025-08-31 00:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 449a179a-b275-3292-b767-8d507b0fc3d0 | -11.3701 | -43.6104 | 2025-08-31 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 827570dd-a096-34d3-a469-0eefc943060d | -8.6673 | -62.8369 | 2025-08-31 00:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 63.3 |
| c4282318-bc29-3a22-a54f-feec1fa21599 | -10.3126 | -59.2023 | 2025-08-31 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 300576e8-0025-3635-8a25-68ec9bd05bdc | -19.1128 | -48.3063 | 2025-08-31 00:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 93.3 |
| d320d942-9b58-3029-a571-abe65a6750b4 | -9.0799 | -65.4349 | 2025-08-31 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 75331968-388e-3c1c-8fbe-20340fafd90a | -13.3636 | -46.95 | 2025-08-31 00:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 6e375f8b-1a4f-3d4a-9247-e6f2fff4eb39 | -12.9192 | -56.9873 | 2025-08-31 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 7ec1df4f-780d-3797-9be4-6c9ecf7c3f94 | -7.0951 | -44.3128 | 2025-08-31 00:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 74826fca-2b7b-31ca-8a54-91c329af9832 | -9.0799 | -65.4536 | 2025-08-31 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 2d77809a-2800-35af-9866-231548337b97 | -8.744 | -62.379 | 2025-08-31 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 3de8981c-a634-3bca-872b-edec54ad3f74 | -7.9732 | -46.4077 | 2025-08-31 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 647b8a74-3d16-37af-b086-b261ff4a0267 | -12.3291 | -45.6971 | 2025-08-31 00:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 824fc8dd-c86f-35ab-a064-2ec0c12325e3 | -11.3701 | -43.6104 | 2025-08-31 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| d5a64f77-aaa0-38c2-95dc-eb2ba1dc09cc | -11.3504 | -43.637 | 2025-08-31 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 52f7b609-973b-3f27-ad3b-9f7083a4d245 | -9.0614 | -65.4355 | 2025-08-31 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 0007b44b-1d63-332f-b1ef-a9fc2099b313 | -9.2745 | -67.6433 | 2025-08-31 00:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| ef061062-c566-332d-985d-14fdcd5ac06a | -8.6487 | -62.8376 | 2025-08-31 00:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 628b5ba9-0c33-3572-ba97-8b10e3ce40fc | -13.4986 | -46.9517 | 2025-08-31 00:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 82314c75-0733-3280-b154-f0d661692107 | -10.1359 | -58.0183 | 2025-08-31 00:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 730c7e69-96fb-396b-9776-cf0371f1956d | -7.1139 | -44.3111 | 2025-08-31 00:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 144.2 |
| d0bfee1f-6317-314d-afbc-e670c19c69a9 | -18.672 | -49.0793 | 2025-08-31 00:50:00 | GOES-19 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 64.5 |
| fd03c40f-4ce5-315c-8c41-378248f18ca8 | -7.908 | -63.0164 | 2025-08-31 00:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| ed3b5116-1fcb-35a6-a301-d308dd82af3c | -6.1853 | -43.3257 | 2025-08-31 00:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 2111f968-169a-3b63-aeb1-c8cf8d2b9cd2 | -7.0774 | -63.1948 | 2025-08-31 00:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 3c4fdf66-5cee-316c-b650-3348d888346f | -19.1134 | -48.2833 | 2025-08-31 00:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 8544ebe4-c0f3-3faa-bd64-5abe50b16f54 | -8.8522 | -66.727 | 2025-08-31 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 73508435-8e91-3edc-9b91-3e394f3e4ef7 | -12.3095 | -45.723 | 2025-08-31 00:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| ba63368e-64c4-329f-86fc-37962a5ee337 | -19.0926 | -48.3106 | 2025-08-31 00:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 7945efdc-8516-316b-a0c1-6a236258dcfc | -10.3313 | -59.2011 | 2025-08-31 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 8c6ab9a6-1537-3272-836f-fa8d17d768c1 | -16.2221 | -52.6778 | 2025-08-31 00:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 127.6 |
| b93805f2-d3d8-3eee-9a74-4542a0c9c246 | -14.5452 | -51.9729 | 2025-08-31 00:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| efcd68ef-1786-3976-b387-3fdfdddf60d8 | -8.8337 | -66.7275 | 2025-08-31 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 433bbcba-87f3-3495-9674-69dd09ea3b68 | -8.6673 | -62.8369 | 2025-08-31 00:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 63.8 |
| dab07a56-e93c-3fb8-b826-de3af1eb37fc | -13.3632 | -46.9727 | 2025-08-31 00:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.1 |
| a853310c-2c02-3c86-9de7-52b13850b12f | -16.2417 | -52.675 | 2025-08-31 00:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 0a168aee-2702-38af-91ec-d9ef5413c32e | -11.3509 | -43.6133 | 2025-08-31 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 1fb393d7-28a3-328b-9c49-9457681c6adc | -9.0613 | -65.4542 | 2025-08-31 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| d1902cd1-aa45-31df-a9bd-57e14ffa299b | -13.3443 | -46.953 | 2025-08-31 00:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 99.5 |
| cfbef9fa-29a8-3007-8940-7d967ed9402b | -8.7439 | -62.3979 | 2025-08-31 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 9e51ead3-551b-39d5-82d6-234d9dcc5d6c | -12.3099 | -45.7 | 2025-08-31 00:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| a1314154-2e4d-30f7-a6fd-b06b79f14bea | -14.5448 | -51.9943 | 2025-08-31 00:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| f0447f85-db8b-321a-8c18-f9374ac6fb62 | -12.0976 | -44.717 | 2025-08-31 00:50:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 139f02f8-c82b-3755-95aa-3c3d2fc503bd | -12.3287 | -45.7201 | 2025-08-31 00:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 99d17605-fb97-39e9-ab18-4e16f518da2a | -16.2217 | -52.6992 | 2025-08-31 00:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 92c6f033-3f84-3f8d-84f3-40c0a64eee11 | -3.8146 | -48.9515 | 2025-08-31 00:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| adf4d079-1623-3ee9-8d5f-9880cb0ccb1c | -13.4793 | -46.9547 | 2025-08-31 00:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 9a6996b9-5e15-3b7c-b527-3b92436f06b2 | -11.3116 | -43.6664 | 2025-08-31 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| ecdf2953-f20a-3637-9e28-2c9172e7b10e | -18.672 | -49.0793 | 2025-08-31 01:00:00 | GOES-19 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 59.4 |
| ef3293fe-48a0-3368-86f0-bd0b43abab34 | -12.0976 | -44.717 | 2025-08-31 01:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 5aed233f-dfaa-380e-b5f4-d395b87c9df6 | -9.0799 | -65.4536 | 2025-08-31 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 0ef63eb1-c989-3cb4-8c47-7f8cfe45884d | -16.2225 | -52.6565 | 2025-08-31 01:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 02daacf3-7229-3356-ad63-22eac83ce861 | -19.0932 | -48.2876 | 2025-08-31 01:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 2a7e99d4-da7e-30c7-af3d-2b3be8ae9bff | -13.4986 | -46.9517 | 2025-08-31 01:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 02ee664a-b7ed-3df0-9c04-d12cac46a678 | -13.3632 | -46.9727 | 2025-08-31 01:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| fe64d52a-2f3b-3c58-8e84-78d7c146c394 | -7.9265 | -63.0158 | 2025-08-31 01:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 03b14ace-00db-36d3-881e-62f62e1ec892 | -8.6538 | -61.9647 | 2025-08-31 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 28835b83-d6f8-3a9c-b677-3cb3a2168bd6 | -9.4497 | -62.3485 | 2025-08-31 01:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 9ef06e6e-f528-324c-9734-84906c68683f | -6.1665 | -43.3273 | 2025-08-31 01:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| f80d3bf9-17a0-347b-b0b9-d582eb1149f2 | -11.3509 | -43.6133 | 2025-08-31 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.1 |
| c9e6dfe2-6665-3edc-bc2c-ea2a9f21f95e | -10.6128 | -44.3284 | 2025-08-31 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 0b8940d0-701a-3af8-bda4-88a932dd71fb | -6.1853 | -43.3257 | 2025-08-31 01:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 666f5de8-42f3-376b-a1e6-f312b5781e3e | -9.0615 | -65.4169 | 2025-08-31 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 4bb85ab4-f9b2-38c9-a3f9-5e4f528bfca2 | -16.2217 | -52.6992 | 2025-08-31 01:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 2f365e97-b043-3a19-a865-b249a9f0d63c | -19.1128 | -48.3063 | 2025-08-31 01:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 0f19feed-cf3b-34f1-8803-4c473b426e47 | -16.2417 | -52.675 | 2025-08-31 01:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 909cedd9-a8d2-3a18-81de-cefd1d99e0b5 | -14.5448 | -51.9943 | 2025-08-31 01:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 78e34995-6419-3c04-98b7-0854349d2f27 | -9.0799 | -65.4349 | 2025-08-31 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| f4cb93ce-712b-33dd-bb51-850a191fc52b | -13.4793 | -46.9547 | 2025-08-31 01:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 6630c369-15f4-34ef-8c6a-bd2f0e7235b0 | -9.0614 | -65.4355 | 2025-08-31 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| d27a42a1-4cc4-384f-b8f4-01f0ee3ef1ae | -14.5452 | -51.9729 | 2025-08-31 01:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 14962158-c26b-38b8-ba7b-1c8ea46263c0 | -13.3636 | -46.95 | 2025-08-31 01:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 6d098add-d7b9-3395-8794-2798913c0920 | -3.8146 | -48.9515 | 2025-08-31 01:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| d023cd20-d12b-3272-9b7b-efffaf09b275 | -8.6487 | -62.8376 | 2025-08-31 01:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 49a7cc82-d8e3-3c21-8118-86b6dc6eb60c | -10.1359 | -58.0183 | 2025-08-31 01:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| b2695013-835a-3734-88a1-42d9a35e4152 | -7.0774 | -63.1948 | 2025-08-31 01:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| afbde15f-b009-3dcd-ac72-b700dc94db87 | -19.0926 | -48.3106 | 2025-08-31 01:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 1eb1f3c3-1c93-34c1-a92e-bcacb33f9560 | -16.2025 | -52.6807 | 2025-08-31 01:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 5f0b90fe-32b6-36b3-beb3-ee7692f046fa | -7.1139 | -44.3111 | 2025-08-31 01:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 1819139b-8ea3-3e4a-953d-e6a313a62333 | -11.8373 | -46.4287 | 2025-08-31 01:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |


[Clique aqui para ver as próximas entradas](README8.md)
