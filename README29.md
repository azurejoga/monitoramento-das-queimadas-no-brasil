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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d308304f-b6a3-301a-bd89-d337b39edf1b | -3.32322 | -51.65837 | 2024-11-16 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f2e7392-5fcb-3b51-b0ee-eb2a129df6e6 | -2.6652 | -46.18727 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2af2182-a78b-3966-ad4d-7cea89b7b211 | -2.65517 | -46.1857 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0fcf9fa-8104-36d9-b135-ea9eb8ffced5 | -4.37795 | -45.62825 | 2024-11-16 04:23:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0c0250e-c7c5-30a3-8a87-04b1884d3f88 | -4.44311 | -45.46836 | 2024-11-16 04:23:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef92912f-6690-3a1a-be30-faf92b1ce052 | -3.76021 | -50.78545 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 066e16fe-6956-3275-b10d-9295299e4f98 | -4.00033 | -46.49707 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2c4ed61-bc68-34dd-8bca-525fe3ec76aa | -3.03678 | -47.97428 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5ddf80f-0593-3d74-9061-1b57d8038434 | -4.1349 | -49.36565 | 2024-11-16 04:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 78975438-ec4d-359b-a34b-52c40fad820f | -3.40878 | -42.38787 | 2024-11-16 04:23:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 73912014-8b13-35db-a27c-d2101d2d49f4 | -3.18427 | -46.53506 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a1baae8-60f2-302b-ab50-5747f409c9de | -1.13301 | -54.16779 | 2024-11-16 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71bdf163-9ecb-3dba-97aa-264907ee0475 | -3.73927 | -45.65875 | 2024-11-16 04:23:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 48.1 |
| d195d863-6718-3705-8f94-8370a6776969 | -1.33371 | -47.68344 | 2024-11-16 04:23:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8e8d55c-ab38-3ede-b900-2a320700b191 | -3.23259 | -45.37764 | 2024-11-16 04:23:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 128dbe50-1074-342d-b7f7-037dc2bd0236 | -2.50816 | -46.3895 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 540f0441-c58d-3d8a-9bb5-c83b10df242b | -4.0073 | -44.34072 | 2024-11-16 04:23:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 946115ed-b836-337c-b05b-ec262bd4247e | -4.35904 | -45.87276 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83309846-4063-3196-8954-1adb11c7de0d | -2.55741 | -54.03992 | 2024-11-16 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74c3cfcb-7ddf-36c1-aa31-a74b9119d73d | -3.76254 | -50.7972 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 386e7211-2f06-3171-a303-0adb04ffc33b | -1.12438 | -48.37854 | 2024-11-16 04:23:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 640335ec-a899-3131-bee9-ce32c703b9c9 | -2.23166 | -53.61111 | 2024-11-16 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| eec1dc7f-8981-3587-b5e6-7c8144ded1b0 | -2.242 | -46.83694 | 2024-11-16 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddb32e67-558c-3e86-b035-bd20a4eb1563 | -3.51894 | -44.71665 | 2024-11-16 04:23:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 1a4fcb2f-3bda-3310-a99a-d635c43edb4b | -4.72853 | -43.25255 | 2024-11-16 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d92b082d-44d7-353c-9b74-e65616264e2e | -2.55079 | -46.89222 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d508de84-8b03-3a67-ac08-daebf50f448d | -5.67182 | -35.63974 | 2024-11-16 04:23:00 | NPP-375D | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 67797480-ae21-3c57-b7f8-f3a1dac41649 | -3.65147 | -49.94253 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 30ccba75-70b5-3485-a0a6-944ea131efb8 | -3.73486 | -45.66514 | 2024-11-16 04:23:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0536df70-09bb-3dd5-98ab-03f16e738862 | -3.75902 | -50.79288 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bb61be3d-1747-3b3d-ab83-f822466f7af3 | -2.51407 | -47.47576 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc89d36b-ecf6-3add-a8f5-6fd91e8cb03d | -5.23719 | -44.91465 | 2024-11-16 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d94873c4-c68f-313c-8470-31b387bc5e63 | -2.17514 | -46.43966 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f9b8e32-7d37-34f6-b72b-49839bf76b2c | -2.55215 | -54.03926 | 2024-11-16 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 525910bc-87c5-3b50-82d2-53e3a9f142da | -3.87959 | -45.0257 | 2024-11-16 04:23:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 309c111d-07c3-3fc7-a603-143756870c0d | -3.575 | -45.67141 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da00db8c-944d-35ad-82f5-9bc0987ffbc3 | -3.98943 | -45.85695 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e16e2ecc-5db4-3da0-8a73-cefd93495d8c | -0.81024 | -49.51799 | 2024-11-16 04:23:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f41e2cb2-d09f-3736-945f-2105cef91bcb | -3.55896 | -51.64606 | 2024-11-16 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 646d0e87-11ae-31d1-b13c-8c10bebfbc04 | -3.01499 | -47.97486 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fa9779b-0440-3e3e-b436-6a50ce057aa9 | -1.2284 | -53.70779 | 2024-11-16 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3c58aae-770b-3f46-8eb4-b9c7c2c50217 | -3.95905 | -46.71435 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8deb7cb7-8e78-354f-9023-9b466fd923a2 | -2.17909 | -48.7489 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a100c82-7206-3c91-9ff6-0bb46f263d80 | -2.66016 | -46.17572 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4a1d758a-6c7a-3ee3-8399-7b5a6bb57a46 | -3.97081 | -46.70533 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6920a124-0e67-3a1d-ad73-5392d7d03114 | -3.96295 | -49.99477 | 2024-11-16 04:23:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 447c88f2-ac71-3db4-836a-2258564db294 | -4.81479 | -42.91878 | 2024-11-16 04:23:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc57558b-7742-3b08-a0e0-1302e37727a3 | -3.91591 | -45.8526 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1bf13db-290e-3348-955b-5a53b156aaa2 | -3.19936 | -45.54551 | 2024-11-16 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| ff10d888-278e-3046-b3f6-7545b96d0ebe | -2.88207 | -40.38884 | 2024-11-16 04:23:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fee2cf4f-f33c-3e45-b584-d90abe9ff1fe | -4.61367 | -44.39669 | 2024-11-16 04:23:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25e2ae75-4c24-3109-97c0-f3db25db8e2c | -2.94116 | -48.3246 | 2024-11-16 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3a20d9c7-dd2a-36a0-a1b1-fd90f27595a8 | -4.13533 | -43.92421 | 2024-11-16 04:23:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7817c8e1-61e4-32eb-a269-48e26a3c6644 | -3.0343 | -47.99002 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61740f31-027b-3649-98de-9cace779f7ac | -2.09683 | -46.58479 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c43d54ae-aef6-36f8-8482-845ff890ca29 | -2.22072 | -47.21065 | 2024-11-16 04:23:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8de11fb-ea5f-307d-bcd1-d997098c3783 | -2.78174 | -48.57727 | 2024-11-16 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2304be7b-61ee-3229-82b5-beff5963d200 | -2.04603 | -53.95428 | 2024-11-16 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1aacbc6f-d360-3c36-9bf0-5cfb49f152a3 | -2.62732 | -46.1885 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b49c83a1-9328-3202-b5e9-01717c4622c9 | -2.95508 | -48.00981 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d84003c-b929-3321-a47d-147517f5da42 | -3.72937 | -45.66083 | 2024-11-16 04:23:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fded8f8f-7722-356e-bf54-c7849ec9c64a | -2.63819 | -46.82752 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6099a699-91f8-3575-91cd-250672540be7 | -4.81897 | -42.91527 | 2024-11-16 04:23:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f77b0aa8-39d9-3003-9c93-906e68a8fc48 | -2.08655 | -50.47997 | 2024-11-16 04:23:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fc017b9-b4fb-39ca-b0d6-5b149c36e993 | -3.73541 | -45.66169 | 2024-11-16 04:23:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 48.1 |
| e57fb5c8-d960-3c5b-92ed-9d4fed2c57db | -4.74214 | -44.08652 | 2024-11-16 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06318dd9-1475-34dd-8436-182bfbba539c | -2.1339 | -48.76087 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2da1f6d8-c68d-3f3f-bff5-7dba146565a7 | -2.79246 | -46.64521 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adc3556f-b567-3569-bf40-a0217d3cd9b6 | -3.97361 | -46.70938 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c2c6c06-36e1-3c68-a7bc-0727cde5060f | -2.05477 | -48.8978 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5be2bb3-49f6-359f-a22a-d70c802631bd | -2.74007 | -48.55777 | 2024-11-16 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7505133a-fe7f-339b-871a-f9fa6ed75ada | -3.24468 | -46.43595 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8ceb245-a608-39d8-b4f5-d0adb6792ee8 | -3.28397 | -45.50278 | 2024-11-16 04:23:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 17.3 |
| aaf77d21-2bf5-33c1-9a60-71d0617c7d35 | -3.72659 | -45.65686 | 2024-11-16 04:23:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48f2021f-504f-31d2-a5a4-3099788731af | -2.14036 | -46.39781 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb88b628-9407-3228-8ebd-e44f77daed77 | -2.67039 | -46.84387 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89736717-2bef-3c9e-8d00-3a3470a324be | -3.7663 | -43.24677 | 2024-11-16 04:23:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c8620d6-183e-36f8-9c49-e8ae216c3a6d | -4.01868 | -44.00003 | 2024-11-16 04:23:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f06e9e75-9d5c-3ee9-8952-7572230a82e0 | -4.83536 | -44.54064 | 2024-11-16 04:23:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2d97dc1-7b58-36b8-934c-27ee0cdaef69 | -3.18763 | -46.53558 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8434467d-07bd-3cec-a2eb-fe2a5ad3ca19 | -3.50119 | -42.0045 | 2024-11-16 04:23:00 | NPP-375D | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bacd8d8e-3b73-31b2-9f1b-ec37e00d0dcd | -4.00117 | -46.18958 | 2024-11-16 04:23:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23a77e37-8e56-346c-a2ed-7f12d969f8b0 | -2.22116 | -46.35599 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f2ab34f-ae6b-3e43-ad98-4c1fa118a824 | -3.98182 | -43.72088 | 2024-11-16 04:23:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd93c7ea-37a2-3809-8ff8-58f023fc65e6 | -2.66185 | -46.18674 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0a3dcc4-897f-352d-98ed-06d627be42c9 | -1.69881 | -50.20241 | 2024-11-16 04:23:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 711926d1-25c7-37e1-99fc-8872416f0353 | -4.21442 | -50.69651 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6facd14-f863-31b2-b493-92a71a920f69 | -3.91298 | -49.03763 | 2024-11-16 04:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9514a2e7-c6f6-3778-8518-36cda706266f | -1.33017 | -47.68288 | 2024-11-16 04:23:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba12dc6f-f67e-3258-bc9f-ef28165730e8 | -2.7781 | -48.57669 | 2024-11-16 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9d74c474-2421-3b1a-a857-f61858ac9e77 | -4.10304 | -46.88984 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b361f6ab-cf89-3507-b4e7-0c5b4dbd1032 | -1.63917 | -48.51738 | 2024-11-16 04:23:00 | NPP-375D | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 788b43af-683c-3286-8824-0847ef4edd64 | -2.09774 | -46.3327 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c972063-2621-3e32-96cd-ccec44bf636b | -2.65737 | -46.17169 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e4e0c11-fb40-368e-a27c-7934939f9534 | -3.98867 | -43.72195 | 2024-11-16 04:23:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6edf351d-1b86-33e8-bc1e-4c4f8dbc18df | -2.74304 | -48.56252 | 2024-11-16 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df5fbb5d-792a-3b56-88be-85ef0a44a3ef | -3.97808 | -46.70286 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7bddfe7-8ee5-350b-ad9e-b375721a6cc5 | -3.57967 | -50.51388 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adf5e81a-b62e-3154-828c-77099929c77c | -2.63981 | -46.534 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acb0daa7-870c-3183-bee4-9dcd5feada31 | -2.31035 | -48.46932 | 2024-11-16 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README30.md)
