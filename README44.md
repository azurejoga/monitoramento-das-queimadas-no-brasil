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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d72f4f49-9719-3f6f-b2db-e2091031d34f | -13.3055 | -51.3235 | 2024-09-26 02:16:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 167.5 |
| f04c5b1c-6527-348a-b3cc-0464460e9950 | -13.3052 | -51.3449 | 2024-09-26 02:16:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 185.7 |
| 5180762d-4472-30fb-bd7a-bd800ba73c90 | -13.2867 | -51.3046 | 2024-09-26 02:16:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 372793cf-8d02-31ae-9430-a9ad75c753a1 | -13.2863 | -51.326 | 2024-09-26 02:16:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 208.7 |
| 48bb3cee-a811-3397-867d-2e7c1176f31a | -13.286 | -51.3473 | 2024-09-26 02:16:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 1138dbbd-a080-3ec0-8201-526e7c93e35b | -13.4993 | -61.2698 | 2024-09-26 02:16:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 79e81767-998e-3d6f-9860-a1d2f1f1693a | -14.4439 | -45.2555 | 2024-09-26 02:16:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| f2681ba0-caa3-369d-b9b0-b9aa4a4cbad1 | -14.5705 | -45.6973 | 2024-09-26 02:16:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 4bec524c-f86e-31b1-b391-548741c1ff28 | -14.8828 | -51.4777 | 2024-09-26 02:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 31.5 |
| c073d70f-468d-358f-80be-ae778e9a637c | -14.8824 | -51.4992 | 2024-09-26 02:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 65df1ac1-ba7c-3df3-b595-157a75e6b2f1 | -15.7676 | -49.9555 | 2024-09-26 02:16:35 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 73869c9a-f61a-39b3-84f7-7b67c2c35d3e | -16.0985 | -51.9896 | 2024-09-26 02:16:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 223.1 |
| 6b6ac433-9bd5-38b2-80c5-f9abf9b9ca87 | -16.098 | -52.0111 | 2024-09-26 02:16:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 009dd6cc-0ce5-3c8c-9941-f2c64cdc04ce | -16.118 | -51.9867 | 2024-09-26 02:16:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 142.3 |
| fb476ef9-affb-3ea5-bd16-95cd32b3fcf4 | -16.1176 | -52.0082 | 2024-09-26 02:16:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 125.1 |
| dd04068a-ad26-329e-b47a-eb38fa102f3d | -16.5735 | -56.0091 | 2024-09-26 02:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 47.9 |
| 4adcd4b2-59ee-3b81-b933-64af16f392cc | -16.8231 | -57.4994 | 2024-09-26 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.6 |
| be8ef2a8-4103-393d-b053-2261186a218b | -16.8036 | -57.5016 | 2024-09-26 02:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.0 |
| 6e4fe77b-f883-3f4e-90d6-38ea4e2397d2 | -19.9298 | -43.7711 | 2024-09-26 02:16:56 | GOES-16 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.0 |
| 94b6433e-4006-3b37-bfe1-beecb981224f | -19.929 | -43.7959 | 2024-09-26 02:16:56 | GOES-16 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.4 |
| fb5ed858-5f00-3c68-b2e5-9c644f72e87c | -20.6086 | -51.4762 | 2024-09-26 02:17:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 114.4 |
| d4454b46-9807-3bdd-8a89-0963f28a03ee | -20.608 | -51.4986 | 2024-09-26 02:17:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 321.9 |
| 5c0aafa2-88c8-3bee-84c2-aac530a41f7c | -20.6074 | -51.5209 | 2024-09-26 02:17:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 157.2 |
| 6da1c428-b418-30d3-bcf0-0ee3bad78969 | -20.5881 | -51.4802 | 2024-09-26 02:17:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.0 |
| a9c74503-09ae-38ea-bcb1-046a28b33820 | -20.5876 | -51.5026 | 2024-09-26 02:17:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.2 |
| 125b4693-7c84-3df1-8990-3bf90376657c | -20.6284 | -51.4945 | 2024-09-26 02:17:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.5 |
| 458807ac-27ec-3650-9aba-69e05db4e733 | -21.9583 | -48.5638 | 2024-09-26 02:17:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 67.1 |
| bfdc0ce6-ad79-30ba-87e1-ba2b55456e37 | -21.9381 | -48.5453 | 2024-09-26 02:17:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 112.9 |
| a35b66a3-d62f-3248-b0db-58ff1f545b78 | -21.9374 | -48.5688 | 2024-09-26 02:17:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 826ebd0c-693b-3c51-92d8-e17454ce4313 | -21.9173 | -48.5504 | 2024-09-26 02:17:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 53.7 |
| adf90b9d-695a-3200-b075-c9a926225d18 | -21.9166 | -48.5738 | 2024-09-26 02:17:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 54.9 |
| f0b04739-38ad-3323-a3e9-e1f7d099459c | -14.89558 | -57.98975 | 2024-09-26 02:19:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| caabfe58-4763-3fb6-8ff5-19963c4fbb67 | -14.90663 | -57.99229 | 2024-09-26 02:19:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 185.2 |
| 65a57a2a-6043-3750-8972-08335715c55d | -14.91175 | -57.98516 | 2024-09-26 02:19:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 155.2 |
| 5c90017b-442c-3256-99e4-4e482bedf20b | -14.94896 | -57.94422 | 2024-09-26 02:19:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 8e509437-44c0-31fb-a880-de260505a65c | -14.95402 | -57.93811 | 2024-09-26 02:19:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 11afcb3e-e355-3941-9b4a-92fc9e07783b | -6.96288 | -62.91758 | 2024-09-26 02:21:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 97649d22-8f9b-3e7a-a8d4-1e79ee89f0cf | -6.96622 | -62.93861 | 2024-09-26 02:21:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 20ee8cd8-0b1b-3363-a671-86db50cca4a7 | -7.29713 | -61.10585 | 2024-09-26 02:21:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.5 |
| ef9c7399-1fc6-3932-ae9a-181ee555f065 | -7.29924 | -61.11208 | 2024-09-26 02:21:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 0b83bc2e-0558-32ff-b4a2-e7dadb0a8a59 | -7.57381 | -62.79727 | 2024-09-26 02:21:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 84bd994b-3574-3b73-8ab8-169ced02f4a1 | -7.57695 | -62.80307 | 2024-09-26 02:21:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| d49c3376-21f5-3088-84f7-c071ea2d9782 | -7.58695 | -62.79519 | 2024-09-26 02:21:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 22.1 |
| d7c7153d-4f54-33a6-91a8-ac8ca514fed2 | -8.137 | -61.28997 | 2024-09-26 02:21:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 30.7 |
| f5dfd11f-cbc4-3fb8-845e-50054a07e3c7 | -8.1374 | -61.28405 | 2024-09-26 02:21:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 27.5 |
| d0349714-1b94-3ab5-ab1e-16ddf2d93cf8 | -8.16867 | -61.3944 | 2024-09-26 02:21:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 88a8f60b-146e-314c-8329-a5e875733279 | -8.16984 | -61.38831 | 2024-09-26 02:21:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 4e523927-8f52-311d-8003-ae38535470a3 | -8.67655 | -67.0071 | 2024-09-26 02:21:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3b0aa2cc-9fcf-351b-88e0-2ae2c77c6af3 | -8.686 | -67.00567 | 2024-09-26 02:21:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 3b85b2bd-bb2e-352f-8be0-e160c6505848 | -8.68751 | -67.01591 | 2024-09-26 02:21:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f2fcaef9-cc32-3077-ab15-86562ab9a69d | -8.69503 | -67.06683 | 2024-09-26 02:21:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 68a622cd-44ff-3733-b5c1-9ffab697cb23 | -8.69652 | -67.07699 | 2024-09-26 02:21:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 8b3aaab8-b70b-3b5d-8d43-ced0b8140a32 | -8.72675 | -67.02041 | 2024-09-26 02:21:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 62d94ec4-e7df-3a52-83b4-e93ce09c1fdc | -8.80324 | -67.04413 | 2024-09-26 02:21:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 61537862-96b0-3801-81a2-bdf7f1106634 | -8.92542 | -67.18443 | 2024-09-26 02:21:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 1319a63d-5014-3752-8985-46ed4b1208a9 | -8.93475 | -67.18304 | 2024-09-26 02:21:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 7b26de5f-e9ad-32b7-9066-f7b0c4d66ca9 | -9.0513 | -60.44121 | 2024-09-26 02:21:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 04f93c65-16c9-31df-877c-fb54422d7181 | -9.06677 | -61.36789 | 2024-09-26 02:21:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 27faf9ee-e4cf-3887-a317-e9e91852e393 | -9.08769 | -61.11635 | 2024-09-26 02:21:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 9ffaa4c9-d403-372c-98d2-08fc06cd8809 | -9.09211 | -61.14311 | 2024-09-26 02:21:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 85918a36-38a8-3dcb-af62-c70d766df126 | -9.09945 | -61.27732 | 2024-09-26 02:21:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 31d98159-1064-3ea3-a9da-bb18bb4db6a0 | -9.10563 | -61.33495 | 2024-09-26 02:21:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| bf4e0cc2-d1a4-35dc-b078-3cd787bac9ab | -9.10803 | -61.32902 | 2024-09-26 02:21:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 78b21daf-bf51-30ad-9188-995fd0587962 | -9.1097 | -61.36066 | 2024-09-26 02:21:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.0 |
| eaf430ce-1330-31a8-9671-29020aaaed06 | -9.11229 | -61.35471 | 2024-09-26 02:21:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| b31a89ed-06d1-3de6-bacf-4b05bd8f25ab | -9.11385 | -61.27489 | 2024-09-26 02:21:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 253dc967-c580-3f0f-ba09-cdecad0ccff9 | -9.12237 | -61.3266 | 2024-09-26 02:21:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 900df8ce-b9cc-38af-9046-99cd67957d69 | -9.1266 | -61.35228 | 2024-09-26 02:21:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 571a74c3-e58a-3cfe-8073-b95e2227bf6d | -9.1308 | -61.37785 | 2024-09-26 02:21:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| ab4a2982-30eb-34ef-af99-13f41d7df257 | -9.14419 | -66.16521 | 2024-09-26 02:21:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 63e1217e-e496-3c6b-b89c-f13681e2e8e8 | -9.50907 | -66.76218 | 2024-09-26 02:21:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 341c54df-bc0b-3382-8842-59c6c64cd134 | -9.64527 | -68.99926 | 2024-09-26 02:21:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c68d56ff-193c-3d80-83e5-1d840b4d343c | -9.81302 | -68.81683 | 2024-09-26 02:21:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fdd25f00-1c45-32f2-b4d7-2d465d88767c | -9.81428 | -68.82577 | 2024-09-26 02:21:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 548459ff-d125-3b5d-b93c-d6167d930817 | -9.94786 | -64.77451 | 2024-09-26 02:21:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 7d67b186-be34-3f4e-bac3-5610df63579f | -10.0574 | -68.58913 | 2024-09-26 02:21:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 17.3 |
| bd3a36df-e76a-3f61-91d2-5be2c0b0aada | -10.06627 | -68.58784 | 2024-09-26 02:21:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c158c712-8089-3b4a-baed-2c807f5f54cc | -10.07387 | -68.57755 | 2024-09-26 02:21:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 23a10aa9-ac2f-376b-9807-096a987ff0c4 | -10.08404 | -68.52101 | 2024-09-26 02:21:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3d541447-c04b-314b-a91e-f12adfe518e4 | -10.2519 | -68.26577 | 2024-09-26 02:21:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6fa2d48d-bb39-3764-9d92-12def5a92aab | -10.26135 | -67.94733 | 2024-09-26 02:21:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ff5532ff-fdf7-31c6-9f3b-ae92d047b9f8 | -10.29189 | -67.96504 | 2024-09-26 02:21:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f9b900b2-73c5-380e-998a-ff71fc69a527 | -10.31007 | -68.02796 | 2024-09-26 02:21:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e91a61df-7934-3851-85be-dcd7a374da3b | -10.38868 | -67.86897 | 2024-09-26 02:21:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 6cd7adbf-3a11-3095-bfd7-770d15c5accd | -10.39 | -67.8782 | 2024-09-26 02:21:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 66e0d937-f38d-3548-96a9-60d4526f53a3 | -10.39766 | -67.86764 | 2024-09-26 02:21:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 71149be6-ffc9-33d5-add2-375f54cf9026 | -10.39898 | -67.87686 | 2024-09-26 02:21:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 82c2380a-2d9b-3bff-bf7f-60c79c587505 | -10.52269 | -67.77686 | 2024-09-26 02:21:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 33904b1e-b655-3a33-970a-39f6bf8eebb9 | -10.53433 | -67.79411 | 2024-09-26 02:21:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cebbe308-ea62-3599-8de2-aea31cc27dcc | -10.60991 | -67.87077 | 2024-09-26 02:21:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4f00a5e1-be60-3a06-8b2d-b65bc919fb23 | -11.25493 | -65.28191 | 2024-09-26 02:21:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 22.3 |
| faa62ddf-7914-3c7e-ad70-9669d189d5dd | -11.25673 | -65.29385 | 2024-09-26 02:21:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 27f454ab-5b00-3c19-b3b4-ba5f9b3ca211 | -11.26507 | -65.28021 | 2024-09-26 02:21:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 5e27bf8d-d072-3100-8d06-75b02a62a5d9 | -11.26686 | -65.29224 | 2024-09-26 02:21:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 16afb655-c128-3f24-b835-72d2a7d583c3 | -11.9586 | -60.35735 | 2024-09-26 02:21:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 39856773-f380-3bb7-bb5f-18787f72aab2 | -11.96374 | -60.378 | 2024-09-26 02:21:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 23.5 |
| a1705954-2063-3e17-8a65-6e2443339004 | -12.2818 | -62.32715 | 2024-09-26 02:21:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 8bb7d002-f8f6-3e95-9e16-7e4ac9adaec5 | -12.28314 | -62.32036 | 2024-09-26 02:21:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 6b0de1d5-b3cc-3f27-b252-47a13c6fba9f | -12.29563 | -62.31832 | 2024-09-26 02:21:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 66466ff0-5e16-31f0-a7ef-4b79e1dd195f | -12.47162 | -64.04832 | 2024-09-26 02:21:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |


[Clique aqui para ver as próximas entradas](README45.md)
