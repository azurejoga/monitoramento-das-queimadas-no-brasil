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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d31a335-9cd3-379b-aaa4-b8060cea26e3 | -7.37977 | -47.43895 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f10bf8e9-ee40-3c8c-abeb-daa826db4c4d | -8.87642 | -47.96459 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd89eaba-08b3-39e2-bb90-18ee2bed8f7b | -7.8837 | -46.99269 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2981b89-9a25-3b94-a8be-f72dbe9efc80 | -5.43103 | -49.9936 | 2025-09-01 04:32:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7516bc1d-71d7-3347-9bdc-3ded846c9f98 | -6.30984 | -43.5155 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9c0bec8-adac-390b-83b6-d3405d149163 | -9.66134 | -48.35048 | 2025-09-01 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a3524e83-0417-3308-9ce4-8794b071613d | -7.93936 | -46.45118 | 2025-09-01 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 23e22557-b3a4-3ef3-8cc5-3a69fab4d36a | -6.33792 | -53.4292 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d442483b-b1ee-3602-b975-dacf3f920c61 | -6.50847 | -43.55504 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1c1421b-f1b9-3365-873d-c288a1bd9f01 | -6.79537 | -52.80442 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7ba0cbfc-a187-3791-857c-9ce39fb9ae83 | -7.09036 | -49.92585 | 2025-09-01 04:32:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22911443-84c3-342a-8ed2-6576659cbb1b | -6.8398 | -43.34452 | 2025-09-01 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6527008c-7aea-3a39-8097-29cfd3140f64 | -7.72742 | -50.2604 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9342a510-e25e-3fe0-91ae-c9e146426223 | -6.42503 | -43.96261 | 2025-09-01 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4382e63-bf05-3b80-9f5a-68d409c674be | -8.87528 | -47.95008 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5fe6ec6-05bd-3e86-8923-34ac3439dd8a | -6.64175 | -43.96226 | 2025-09-01 04:32:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9361b61-223e-332e-9c1e-54635c2832f6 | -9.00987 | -50.11549 | 2025-09-01 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 24c3cbc8-f90e-393b-a16f-b3366924c029 | -3.81328 | -48.95559 | 2025-09-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d92043ca-efa0-3010-bdcd-1ec6edf08138 | -7.07753 | -44.35877 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| dee14812-ebc8-320a-ae26-bc13ef8e507e | -9.6416 | -47.82243 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05ea98ad-1ad9-31f9-b25e-1ab81e048dd8 | -3.21359 | -46.82939 | 2025-09-01 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 621ce50b-2a9b-3e8c-a722-5cf223a6937b | -8.33726 | -47.43762 | 2025-09-01 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50955bd0-b945-386e-8381-36718a9a8bb6 | -11.04259 | -45.15192 | 2025-09-01 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 7074c069-9f53-34f3-8366-8c58c7df13fe | -6.9519 | -44.29585 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 094d5cd2-3588-3613-9356-cc1cadd3f4fb | -8.77922 | -46.10905 | 2025-09-01 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8490d29-261f-37d5-9f54-a5e22fa08329 | -3.00738 | -47.83491 | 2025-09-01 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ca30d139-584b-3831-b963-b5cbc4a59f70 | -7.09134 | -44.3427 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| c284a65a-721b-3929-9d06-5efb41f342ef | -7.45461 | -44.80838 | 2025-09-01 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3cd198e-9c06-3c37-8e01-fa5c313a855d | -6.1967 | -45.37767 | 2025-09-01 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 888f5585-d021-37b3-8793-7afadf585b23 | -7.72801 | -50.25675 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| daa3c6f8-a674-334a-82e6-d991d774c49c | -9.70792 | -47.04211 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d45875f-2dfc-303d-9325-5f962f2a3639 | -10.04958 | -48.10343 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7f6611fe-b390-314d-86a7-52076d771245 | -7.67304 | -42.66002 | 2025-09-01 04:32:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 547fefdc-262c-35a9-9fa2-51e33f483b18 | -9.82121 | -45.83809 | 2025-09-01 04:32:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19c4dd2e-d058-3493-a338-29ca708c1776 | -11.04324 | -45.14742 | 2025-09-01 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| f064dbd7-7812-3044-8cca-9b9c7b6b9597 | -6.8183 | -45.69747 | 2025-09-01 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| f6f248bd-106a-3f6d-bf6a-92ee8ed9fd1c | -10.04789 | -48.09237 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b25b5c6a-bff9-3d2d-999d-0e2b828f4458 | -7.63315 | -46.55196 | 2025-09-01 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc00bb0d-ed4a-3598-b940-631f33c3c5f4 | -8.82153 | -47.83736 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ff1e455-c5b3-3108-8504-5515ee2e7ff0 | -7.28167 | -60.66682 | 2025-09-01 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 378ce0f5-65db-3026-aed1-ec4624aeb8fa | -6.79846 | -52.81026 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d178f784-6fee-3e0a-85e3-4c5a6af4d9f0 | -6.82634 | -43.32691 | 2025-09-01 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 068ee2ae-2f31-3afb-b755-ee5b6b0f124b | -6.30855 | -43.78739 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01108ec6-6f65-370b-ba68-b0c077e718e7 | -9.22196 | -47.10991 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b6b7871-8114-3537-a0bc-a4877c0beed1 | -5.62141 | -42.6264 | 2025-09-01 04:32:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1a1b320e-cc2e-35db-ac1e-65209cd976fb | -6.86642 | -44.32218 | 2025-09-01 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b1b8454-0fc8-3393-9cfe-7fc57a4ed68d | -5.32863 | -42.86483 | 2025-09-01 04:32:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9792b5dc-ca1e-302c-ba2f-4394da260c47 | -6.8438 | -52.80747 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abab56e4-c1e6-3156-acf5-251c0361738b | -8.89023 | -47.96316 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0bb29327-88ac-3be0-84dd-6b78c4a5a4d7 | -6.27397 | -43.53274 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9c4ba7b-4349-3e48-9488-273486665b7b | -7.62799 | -44.03364 | 2025-09-01 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c914577d-61eb-3316-93cf-0a88bb50d52e | -8.76936 | -46.10371 | 2025-09-01 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1b4c505-91ea-355d-9cab-7bc3d2b58600 | -9.22252 | -47.1063 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ee87cb8-efa5-30d2-a203-e8ce683a79c5 | -7.39251 | -47.44453 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22248e59-88de-3f98-86d4-7f53966164c1 | -6.23957 | -43.39264 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed8cc235-ee11-3e50-91fb-cf273f2cdd52 | -3.62755 | -49.19402 | 2025-09-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc1ea9f2-2943-35e5-b9a6-f0da20b0ae80 | -6.24492 | -43.38346 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe8f4f2d-ec89-3193-9830-9d9ac886128c | -9.62892 | -47.8205 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c15ac6e-85c9-34bc-bd59-e9119af18bab | -11.03641 | -45.14182 | 2025-09-01 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 16aa89a2-2784-380d-95d8-f2079746b151 | -6.48984 | -44.07262 | 2025-09-01 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 166a3cd3-2c45-3d14-bcbb-e47d19e49f6a | -6.25146 | -43.91032 | 2025-09-01 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6629136b-5d78-3a00-9d8d-6dd544d2b885 | -7.08125 | -44.35929 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ae10cb24-a019-3f1a-b691-bd4d9b01ac11 | -6.29183 | -43.55749 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 28218ef9-e180-37bb-bc02-a78380983417 | -4.15768 | -46.78572 | 2025-09-01 04:32:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c5a9764-00ed-3672-a34d-72fa5b0433d5 | -8.44194 | -47.37417 | 2025-09-01 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28c69f89-7f8d-39a1-a366-b7f38a0fcd14 | -9.01267 | -50.1197 | 2025-09-01 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36c37316-3228-374b-ac52-9674033e8a2f | -6.089 | -43.19361 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.3 |
| df627a7d-7fcc-3e55-802e-787519389803 | -6.47924 | -56.00801 | 2025-09-01 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b229f33-e43a-337c-b1e5-2594b565fdda | -7.69586 | -46.71378 | 2025-09-01 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba140709-effa-3bf5-8245-a2cab25246e8 | -6.3137 | -43.51612 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3d6508b-622f-3c75-91b3-abc2e1ae5fb9 | -9.15411 | -47.94772 | 2025-09-01 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f8e39d4-a1a5-3a9c-999c-cd0165b0aa6c | -6.27635 | -43.55557 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0ccd168b-bcff-350a-af00-32b143ef01a3 | -5.79723 | -43.84639 | 2025-09-01 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 93f1db04-bdee-3a1d-a767-b7c39e166d86 | -6.43829 | -55.62203 | 2025-09-01 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ff80cfce-8613-367b-98c7-af0f0ad9553e | -6.19824 | -53.76349 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e44a3a7e-0deb-3547-93b1-da65b0274ff5 | -9.40394 | -48.19476 | 2025-09-01 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1745710c-31b6-3da0-bbd6-311263ae36a6 | -9.2404 | -47.05704 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c5a72c3-fb9d-34e2-9c1c-2eea1679efc2 | -6.41264 | -43.63111 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07d12fcc-0dd2-3407-b99c-53266ed6750b | -5.91557 | -43.44283 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa1d4c18-b0a7-3382-af2c-d8362fccad81 | -8.35783 | -52.53799 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c028b70-1660-39b1-bd4a-bc2a30378c2e | -6.82227 | -52.8143 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e545199d-16af-34f1-a59e-81f0280d2f9d | -7.87584 | -46.97684 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c17e66dc-30ee-3a3f-b9df-dbc7564e0027 | -5.40567 | -42.34278 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0afad5ad-44bb-3f61-a340-a9ece1755664 | -8.83899 | -47.48301 | 2025-09-01 04:32:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56dab441-2234-3e99-b6ce-65e7d7046294 | -5.83034 | -45.20044 | 2025-09-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb982557-56f3-35e2-9aec-c01d2e683743 | -6.76854 | -44.62435 | 2025-09-01 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b247a87-68ca-3278-ad0f-b3e3709f6765 | -8.32656 | -44.99647 | 2025-09-01 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e50052e2-e93f-3f68-8097-5f99d12e1786 | -6.74216 | -43.78325 | 2025-09-01 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0af6c86d-d229-392e-adb5-6df088709dc8 | -8.85003 | -52.02074 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75899570-1dfe-3853-88f6-5b754ca80545 | -10.66478 | -46.26117 | 2025-09-01 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d37b94b6-a2bf-3633-895c-25c61c82e378 | -6.33166 | -53.4328 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f837e01-2a74-3802-89a6-75a8236e118c | -6.54704 | -44.58181 | 2025-09-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 058349d2-fdee-3a28-a69e-5f6942098ce2 | -6.07251 | -43.43384 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c81d821f-372e-3757-81fa-656e8c50c734 | -8.47174 | -45.17585 | 2025-09-01 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e0d6df0b-8c85-37a6-b459-4a148ec37a77 | -9.12615 | -45.19543 | 2025-09-01 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3734c6d8-611d-3d54-bbea-fc71bbc4bd56 | -6.26555 | -43.53627 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 295b6d79-a9d9-3e6e-8a90-e1460a5aff86 | -10.04567 | -48.08474 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af62245e-7d56-3bae-b5a3-d8a318bb2de3 | -10.02574 | -48.36543 | 2025-09-01 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1c3fdd6-f934-358d-9c70-9f64a9d7a051 | -8.44528 | -47.3747 | 2025-09-01 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8042eed-23ef-330e-b56b-e7b365aa7bf2 | -8.47237 | -45.1716 | 2025-09-01 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README57.md)
