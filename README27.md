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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64986936-70f5-3fce-b99d-289ddf9f5f6d | -3.90043 | -40.93586 | 2024-12-03 04:06:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 604c2243-e57c-39d8-9179-a143e7049acc | -4.0319 | -46.93695 | 2024-12-03 04:06:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e728fb62-b1d4-3af6-8eb6-61ae146b78c3 | -4.04127 | -46.82616 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74b2b53f-b860-350e-8f55-4ea8ecc24665 | -2.33664 | -45.8981 | 2024-12-03 04:06:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55452ed3-8d06-3837-b86c-241e232fa5de | -2.4735 | -46.54662 | 2024-12-03 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fe17f56-f960-3dc2-a949-5ec54de74037 | -5.11688 | -43.2117 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 44200b05-7fb9-368d-a01d-04fc62b03198 | -4.06261 | -44.87758 | 2024-12-03 04:06:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 010b5386-e4f3-36ce-a714-068ec56906d7 | -5.11043 | -43.215 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 0a4967a8-6c9b-3acc-9594-3e4a73881800 | -3.5335 | -45.25775 | 2024-12-03 04:06:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3f32f3f-5449-3e84-a9e9-222124b882bb | -3.31721 | -42.78833 | 2024-12-03 04:06:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1857d80-bf66-34b3-9551-805498b06156 | -4.93399 | -43.77861 | 2024-12-03 04:06:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cbefe89d-2113-3e5a-9d7a-590b59cf203d | -3.1052 | -53.22785 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ac67950-cdb5-3b03-9e4e-b8a11f288944 | -5.80859 | -46.48487 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6640eb7e-10b9-36cb-ba49-c56d83ea8465 | -3.25973 | -53.34466 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1f5a8d0f-22ce-3ffe-b566-41a4f0eb5fda | -5.11566 | -43.20429 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fcd43984-44a3-3580-8573-98ff3485e520 | -2.73347 | -45.20708 | 2024-12-03 04:06:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74333e5e-fb28-37c4-ba4a-57d60e92250b | -3.08648 | -53.37315 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8bcfa2df-c979-3bc3-af93-33c35056ece3 | -3.54655 | -50.18106 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e8b05565-c1f2-3942-b99d-440e436cc78a | -4.16065 | -48.58545 | 2024-12-03 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 71a1de4b-a338-3533-bc93-5b002ce24479 | -2.75262 | -46.12786 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c956e75-54d8-3c3a-b76f-eb960a2e9baf | -2.68023 | -46.60237 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75280057-d5e4-35a4-8c7b-c46727b0dd56 | -2.67826 | -46.61459 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec486ab1-6912-3b8a-a00f-6aaf44da892b | -1.08572 | -53.46252 | 2024-12-03 04:06:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| d45ce3e8-5e7d-3868-b9ff-b52d2e87c94e | -2.68388 | -46.60715 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7ae558f-a4e6-3b48-a936-80d030b11cd7 | -1.07913 | -53.45585 | 2024-12-03 04:06:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 368886c7-a92d-31fd-9ef8-fde1bf20bbfd | -3.35094 | -51.2192 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 19fd8454-8d9e-30e1-8492-21a1e2da4e40 | -1.94411 | -45.55311 | 2024-12-03 04:06:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d8ec33a-8ccc-319c-a5a9-45d14bfb1aa1 | -3.54475 | -50.19157 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f13d2c39-d110-3db3-94df-211d63be9155 | -5.11507 | -43.20805 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 89a574e1-c375-3e15-9ced-667a1239dd77 | -2.20447 | -53.77847 | 2024-12-03 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ea48279e-5ac4-3e94-b910-9eb92e6b3cb8 | -3.5523 | -51.4607 | 2024-12-03 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 466a6810-1b0a-3731-b239-a8c300fabc50 | -5.38828 | -46.36329 | 2024-12-03 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7c311ce-7b34-3717-96d6-058a8d2e7aa3 | -4.80681 | -45.00166 | 2024-12-03 04:06:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5c344d6-6a94-3242-92ed-e73d88745cb1 | -3.341 | -46.06052 | 2024-12-03 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 03517858-934d-301a-8366-816f9ca49b52 | -1.95198 | -53.34605 | 2024-12-03 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23dc5252-9238-3a68-9bc9-2c4d976b7fa4 | -6.1162 | -43.96827 | 2024-12-03 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 581d561a-9df5-3b96-88ab-22394c9d6cde | -3.70125 | -51.82508 | 2024-12-03 04:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2bbeb437-9833-3ee6-900e-05d0af344246 | -2.85506 | -45.83098 | 2024-12-03 04:06:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2819b387-3495-36d8-9e67-720fc241d028 | -3.29561 | -53.66796 | 2024-12-03 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 26c567c7-b596-375c-a894-96547e488660 | -3.54769 | -50.1744 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0f8f945f-6880-37e2-9017-b877572ff9dd | -4.09648 | -47.4248 | 2024-12-03 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f1ad86f-2c25-3e22-9198-1250d4ab39ef | -2.85468 | -45.39505 | 2024-12-03 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 052a4d5a-b765-3477-b7b5-4a559b8be46c | -2.68454 | -46.60308 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59841d67-325a-3199-b526-a0e7e450a92b | -2.72561 | -45.20583 | 2024-12-03 04:06:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 52f45040-fdb9-325d-88b2-29358aeb1dd5 | -5.5959 | -42.93025 | 2024-12-03 04:06:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3a835249-76e9-3307-82d0-57a2bb6ce2ad | -4.01174 | -47.0056 | 2024-12-03 04:06:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88b0b88b-ea9f-3209-8dc6-a117c5186a30 | -5.11388 | -43.21555 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 3aa30607-f06e-3a82-8ef1-03ecb5d06518 | -2.21008 | -53.77824 | 2024-12-03 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d697c9b5-199c-3a6d-9a4b-6a0ab61b91ba | -3.6483 | -52.63589 | 2024-12-03 04:06:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3d3f453-95ee-3271-9d86-f3af0733faa2 | -2.6882 | -46.60785 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0281ebfc-4e6d-389e-8d90-cff5ca9c60f8 | -3.19744 | -46.36604 | 2024-12-03 04:06:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 420ca6a3-bc71-34e8-b134-de153729f272 | -5.11627 | -43.21545 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| e3bdbeb3-ff4f-39c0-8b9e-d2d97be16d3d | -5.38524 | -42.95769 | 2024-12-03 04:06:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7a142cb6-73f8-323c-babc-811dbc11a157 | -2.81115 | -53.06068 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db90d54a-c51e-3322-a353-d11c2546d9c0 | -3.34537 | -51.21231 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fecdc3c8-cb14-3e9a-b5a5-a601cc32cdde | -2.22044 | -45.56507 | 2024-12-03 04:06:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1c10196-ef36-3b7f-bcdd-876828fb3062 | -4.34705 | -43.75166 | 2024-12-03 04:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae2682f2-1cea-3e1d-868c-c0d6ed48065a | -4.93816 | -43.77523 | 2024-12-03 04:06:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e8463222-88d0-3adc-a881-9cf3a87186e3 | -3.9666 | -46.62506 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1a8d3c84-de84-38be-9599-1857bb57800f | -2.85809 | -45.83077 | 2024-12-03 04:06:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d62f2e22-858c-31cf-9268-4bb26f8a1d79 | -3.34214 | -46.05339 | 2024-12-03 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f2383f85-7f4e-3c81-8f5c-b0e6a1bcf18f | -3.12328 | -45.99294 | 2024-12-03 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 934eafe1-c294-3b9a-8e99-264d9b07d035 | -2.95693 | -39.96227 | 2024-12-03 04:06:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e8e027e4-74c5-3b48-bbd4-c6efc8a05f6e | -3.10132 | -53.23002 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ad6762c0-f34c-3e70-8ce9-625e32e1cec8 | -3.54975 | -51.45311 | 2024-12-03 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0369d6b9-5956-3ff1-8c6d-555a4e2d4da0 | -4.04777 | -47.00309 | 2024-12-03 04:06:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a53e794-0b03-3bc2-9e41-7a03c79da679 | -3.45506 | -44.92838 | 2024-12-03 04:06:00 | NPP-375D | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7557cc06-af8b-3fc1-92f9-092ac812f716 | -4.05608 | -46.81625 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5404892-40db-33a3-af42-3d23651f572d | -6.12162 | -43.95714 | 2024-12-03 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ff27005-c155-3840-a676-02c912231a75 | -4.74589 | -45.11398 | 2024-12-03 04:06:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e9ed3416-02eb-3cbe-8dab-7c6ad19dc37e | -3.70309 | -51.82347 | 2024-12-03 04:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 533752a1-47b5-3fb1-9ff1-0fe74f4cc44b | -2.65835 | -46.12088 | 2024-12-03 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f15ecfd6-8d38-31d4-af66-885b100b3be6 | -2.88388 | -45.44151 | 2024-12-03 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 142c3c3e-65bf-3f10-a217-81346af9a1e7 | -2.73221 | -45.20858 | 2024-12-03 04:06:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0ac59f75-3e66-3394-8b80-a9a62470758f | -4.56221 | -46.6268 | 2024-12-03 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22c79e9f-a743-3354-8de0-9ebe673f538a | -5.48272 | -46.34616 | 2024-12-03 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acd753e2-ce5e-3188-8755-23450e093a86 | -5.27872 | -45.45309 | 2024-12-03 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f8e4128-6784-3ea2-bc09-b7f21468736d | -2.85071 | -45.39442 | 2024-12-03 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 40e773b6-a27f-3b3d-af8b-cab0a5b1d84e | -2.59515 | -46.27169 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ce03023-4c37-3fa7-a601-a97bd10515b8 | -3.28353 | -50.33367 | 2024-12-03 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ec01c0ad-9539-3f04-904b-ad89c4f48061 | -4.48171 | -47.73296 | 2024-12-03 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20b9861d-5b42-3751-8fc7-54b9f1ff566b | -5.11221 | -43.21867 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 760d9ddf-db28-30b2-acd6-748faf6a7d9a | -3.90567 | -46.65582 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6067f945-29eb-3d31-bff5-0c8df3750277 | -3.20226 | -46.36286 | 2024-12-03 04:06:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54a1f690-5062-349a-b00b-fd5fc3dce154 | -2.75679 | -46.12851 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 538a61b2-d0d8-3a26-97fd-23a5e56e9ce0 | -5.54337 | -43.8969 | 2024-12-03 04:06:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b053432c-36c8-3cfe-9821-ce211ae3949f | -3.5464 | -51.4597 | 2024-12-03 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 835f28db-68de-369b-9d89-5af13e143e29 | -2.85098 | -45.83031 | 2024-12-03 04:06:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 12198b67-4c7b-3dfc-abfa-cb1437f89909 | -5.48676 | -46.3469 | 2024-12-03 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff3b9abd-0cb5-3e02-9137-bc968b25357e | -6.11972 | -43.96885 | 2024-12-03 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aee8c9f2-a320-3500-89bf-e45c9a4d140a | -3.37199 | -45.84064 | 2024-12-03 04:06:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 647abb09-f5e3-3db5-ba50-e45449692fc6 | -5.38865 | -42.95824 | 2024-12-03 04:06:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 67441547-a896-3a6f-99f4-63b909e38a01 | -3.97145 | -47.25018 | 2024-12-03 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fcfd974-0ca8-30d6-8aa4-59fd241dfaef | -2.67693 | -46.62278 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ed3033e7-89d2-3984-8ee8-74e2fa8850ca | -3.25408 | -53.66572 | 2024-12-03 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 681d95f4-5222-3b40-9788-a04918b3ac65 | -5.12155 | -43.20475 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b42c3838-a5fd-3505-bfc4-e0645cc91c6b | -3.95688 | -46.50053 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 09b65756-baa3-3dfe-877f-5e4fa1a9e297 | -5.8374 | -44.01905 | 2024-12-03 04:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa46d011-6cfa-3207-93c6-db3d114b9193 | -1.75445 | -52.79058 | 2024-12-03 04:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 687c3a1a-93fa-3f74-805b-e52ab0549186 | -4.74896 | -45.11907 | 2024-12-03 04:06:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README28.md)
