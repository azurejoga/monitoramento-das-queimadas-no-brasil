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
| 70fad844-22bc-3200-9d3e-7679e2ee20b2 | -17.1182 | -42.8844 | 2025-03-10 00:30:00 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 901f6fa6-d156-3c3d-8863-2857105ab01b | -22.899 | -43.75326 | 2025-03-10 00:35:00 | TERRA_M-M | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 09592bd0-37b8-33d6-b73e-21dcef088e99 | -22.80602 | -42.47208 | 2025-03-10 00:35:00 | TERRA_M-M | RIO BONITO | RIO DE JANEIRO | Brasil | 3304300 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 768f59ec-496c-3e88-8b44-ef93d0e25994 | -18.02089 | -43.28807 | 2025-03-10 00:35:00 | TERRA_M-M | SÃO GONÇALO DO RIO PRETO | MINAS GERAIS | Brasil | 3125507 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b57195da-6b7c-371c-b14c-7dba7e32fd79 | -17.12637 | -42.89792 | 2025-03-10 00:35:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0a37fd67-5571-3353-8b1a-16ca065e7264 | -23.5148 | -50.9252 | 2025-03-10 00:35:00 | TERRA_M-M | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 21.2 |
| 692f2127-a004-38cd-b07d-843c0656f10f | -19.45001 | -44.91806 | 2025-03-10 00:35:00 | TERRA_M-M | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 67453c6e-0902-3570-bf9b-c41126fbbb1e | -17.11738 | -42.89936 | 2025-03-10 00:35:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| bc8c885a-5e52-3192-8cec-bd4cf729603b | -17.12496 | -42.88824 | 2025-03-10 00:35:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a4b7e7d2-4462-33bd-b1fb-2a79de2fdc97 | -17.11597 | -42.88969 | 2025-03-10 00:35:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 13950259-6f69-328a-a91a-a13e71ded1f7 | -22.76716 | -41.93902 | 2025-03-10 00:35:00 | TERRA_M-M | ARMAÇÃO DOS BÚZIOS | RIO DE JANEIRO | Brasil | 3300233 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 7cbdfdc8-2168-3cb2-89ef-5edeb0bbd4be | -22.76858 | -41.94875 | 2025-03-10 00:35:00 | TERRA_M-M | ARMAÇÃO DOS BÚZIOS | RIO DE JANEIRO | Brasil | 3300233 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 6132d1e8-69de-36dd-bdba-08a9357fdafb | -17.1322 | -42.907001 | 2025-03-10 00:36:00 | METOP-B | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2bbb0952-1eac-3a40-91dc-8cb5b67a8fa5 | -21.623699 | -48.751499 | 2025-03-10 00:36:00 | METOP-B | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bc3a7ec4-570b-3dbd-85eb-77f2e8dda918 | -21.622101 | -48.744099 | 2025-03-10 00:36:00 | METOP-B | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 22229ddd-fa92-3bfb-82f6-64a849e3b26f | -17.118999 | -42.895699 | 2025-03-10 00:36:00 | METOP-B | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4d27cd73-b090-3817-b8f8-0d5d6c412cdc | -24.0196 | -51.078098 | 2025-03-10 00:36:00 | METOP-B | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f8e9738c-c672-31be-b3b0-e9f87acba13c | -17.1287 | -42.893002 | 2025-03-10 00:36:00 | METOP-B | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 792e8f02-212e-3b54-8c94-21b67b905da7 | -24.0179 | -51.0695 | 2025-03-10 00:36:00 | METOP-B | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b076d11e-4edf-373e-93f0-b9a49e45378b | -17.125 | -42.878899 | 2025-03-10 00:36:00 | METOP-B | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e0904dd0-7850-3e2c-82d9-1ff9163c48a0 | -14.56022 | -46.72419 | 2025-03-10 00:37:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8672b1f2-bf41-3d4f-b0ce-b1e1143551f1 | -14.56955 | -46.72289 | 2025-03-10 00:37:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c20c5f99-2573-35fb-96ae-3f05e5fb2ad0 | -14.20264 | -45.76917 | 2025-03-10 00:37:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c3b8ca7c-e929-32ba-9897-37936dd1914f | -17.1182 | -42.8844 | 2025-03-10 00:50:00 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 27d72c22-76b2-3921-84b4-6d9690e254ee | -17.1182 | -42.8844 | 2025-03-10 01:00:00 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 79.9 |
| b82cf91e-55a8-38da-8524-097406011a5e | -17.1182 | -42.8844 | 2025-03-10 01:20:00 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 84d9946d-ba4a-3288-a5c5-25f2e52b3c25 | -21.631399 | -48.742001 | 2025-03-10 01:28:00 | METOP-C | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ef616486-23a9-399d-ad5f-cf40f9da2f60 | -21.641001 | -48.738899 | 2025-03-10 01:28:00 | METOP-C | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| dab80053-c056-3f63-9834-a7b0b732b9fe | -17.1182 | -42.8844 | 2025-03-10 01:30:00 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 0cc2d7ad-f7c5-368c-91b1-973b579a0806 | -11.64206 | -37.78913 | 2025-03-10 03:23:00 | NOAA-21 | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 146c486d-0572-301b-8161-5fc7620e478d | -11.64132 | -37.7933 | 2025-03-10 03:23:00 | NOAA-21 | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7765eed1-76b9-3730-9124-68e5bf8f84b4 | -17.12334 | -42.89913 | 2025-03-10 03:25:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 45ceef65-329f-3bdc-8cfc-777bbf4bc886 | -14.22542 | -41.60098 | 2025-03-10 03:25:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3045a00d-a2dd-317e-a676-421febf60ec6 | -17.11787 | -42.89819 | 2025-03-10 03:25:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4c2e1fd1-a257-3060-b647-82da0f2e6e0b | -17.12402 | -42.89577 | 2025-03-10 03:25:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 65a6b3dc-76d3-3d59-b30c-98638ef17e7c | -17.11943 | -42.89679 | 2025-03-10 03:25:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cb3305e8-4950-3af2-b416-8bb7093f8f43 | -17.11868 | -42.90032 | 2025-03-10 03:25:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 3a7bf35e-83c8-31c9-ad21-1002dc336beb | -17.12488 | -42.89779 | 2025-03-10 03:25:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 481c492b-6a99-3e5d-b322-cd5798b00a8d | -19.83124 | -40.11425 | 2025-03-10 03:28:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e49c7382-6732-344e-815b-0f593d74ee79 | -22.80897 | -42.47106 | 2025-03-10 03:28:00 | NOAA-21 | RIO BONITO | RIO DE JANEIRO | Brasil | 3304300 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 71411fd5-3cf7-326f-84df-50e9ee5355e0 | -19.4508 | -44.91593 | 2025-03-10 03:28:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 322a4baf-b656-327c-99ea-f4bd0425cc3d | -22.93688 | -42.97184 | 2025-03-10 03:28:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| fe86fd66-9f15-32ea-b4bf-54019b629fe3 | -22.6731 | -42.85867 | 2025-03-10 03:28:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 6fe4d7f2-9790-39dc-9891-7db55ac7c4e3 | -22.76718 | -41.94119 | 2025-03-10 03:28:00 | NOAA-21 | ARMAÇÃO DOS BÚZIOS | RIO DE JANEIRO | Brasil | 3300233 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| da4523ea-4287-384c-8efc-ee0eda7a5962 | -19.71655 | -40.35341 | 2025-03-10 03:28:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| cdf2daaa-1858-31b9-af44-6fd8ead1d6b0 | -20.50163 | -42.21194 | 2025-03-10 03:28:00 | NOAA-21 | ORIZÂNIA | MINAS GERAIS | Brasil | 3145877 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c64c303e-16bb-3870-b666-eda1995c8a2d | -22.77175 | -41.94226 | 2025-03-10 03:28:00 | NOAA-21 | ARMAÇÃO DOS BÚZIOS | RIO DE JANEIRO | Brasil | 3300233 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 7db2079b-7296-375d-8e57-d33a75c4ff01 | -19.83555 | -40.11515 | 2025-03-10 03:28:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 008ed740-61ce-3af5-93eb-1ac2f770ad9b | -22.77284 | -41.94018 | 2025-03-10 03:28:00 | NOAA-21 | ARMAÇÃO DOS BÚZIOS | RIO DE JANEIRO | Brasil | 3300233 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| e78ade8c-6fa0-3bf7-8741-1e595e6561a4 | -22.76827 | -41.93912 | 2025-03-10 03:28:00 | NOAA-21 | ARMAÇÃO DOS BÚZIOS | RIO DE JANEIRO | Brasil | 3300233 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 03f2e8f4-77e8-3cc4-9866-340c93666638 | -14.22706 | -41.59712 | 2025-03-10 03:49:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 57b8d5f7-ba67-3621-96fb-450e19ce13f8 | -9.34108 | -43.08695 | 2025-03-10 03:49:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 375c8d38-acd3-3853-9467-0e3278771a7a | -14.22633 | -41.60143 | 2025-03-10 03:49:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8a69ed1b-f479-391a-86e3-db564a9e014b | -12.22639 | -38.14429 | 2025-03-10 03:49:00 | NPP-375D | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5291ef55-64e9-3bd7-8ca5-1fd6d069a2dc | -12.49651 | -45.52244 | 2025-03-10 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b425e760-4594-369f-a73d-9b0c5c7ffdcc | -11.64231 | -37.79346 | 2025-03-10 03:49:00 | NPP-375D | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 522ff380-7e1d-3135-8b07-e24e10faef2f | -12.498 | -45.52486 | 2025-03-10 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39a8efc5-119e-314a-ab83-edcefd4ee607 | -14.20496 | -45.76385 | 2025-03-10 03:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bb212ad6-1077-36ff-8f5b-c6d6d0efb071 | -9.34527 | -43.08767 | 2025-03-10 03:49:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bf8ac834-63e7-30fb-aab0-26d521cb4deb | -14.20035 | -45.76295 | 2025-03-10 03:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7511ee97-c4a0-3ee7-8733-afb181cb1eb8 | -11.64286 | -37.78994 | 2025-03-10 03:49:00 | NPP-375D | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 54531fed-a59f-3f41-80fb-91fcfb45bee1 | -14.56143 | -46.71954 | 2025-03-10 03:51:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d05cd3d-f928-3c03-81b3-8e9623dab98e | -20.07547 | -44.22422 | 2025-03-10 03:51:00 | NPP-375D | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 54540026-f5e4-375a-824d-e3c6f1863e4c | -17.12138 | -42.89946 | 2025-03-10 03:51:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 20a7eb0b-6de7-3415-8e91-847124e1fe9f | -22.67434 | -42.8586 | 2025-03-10 03:51:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 859c5663-1a0f-3460-bc58-83becfa1d2fd | -20.90121 | -43.82038 | 2025-03-10 03:51:00 | NPP-375D | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 64f789cc-6399-351e-b56a-37e92ecc69b3 | -19.7185 | -40.35522 | 2025-03-10 03:51:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 62009755-2fa9-3fcf-aecb-7291ea9dea1a | -18.4882 | -48.37415 | 2025-03-10 03:51:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0ee5b59-72c4-3087-87e2-9cc1cac4e4a5 | -17.75187 | -42.89371 | 2025-03-10 03:51:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64526134-85af-35d1-baaf-0827a483bab9 | -18.04076 | -39.92563 | 2025-03-10 03:51:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 427dab7a-12a6-3c06-8f17-7aaf17580ba4 | -19.44811 | -44.91605 | 2025-03-10 03:51:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95ee3098-1c1f-385f-a002-575a73178e2e | -19.83221 | -40.11463 | 2025-03-10 03:51:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3f35d666-0524-3ef9-bbba-9de3aa99b038 | -17.12216 | -42.89506 | 2025-03-10 03:51:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6c7f28c2-8424-3927-b6c5-118bf1344b44 | -22.77039 | -41.93941 | 2025-03-10 03:51:00 | NPP-375D | ARMAÇÃO DOS BÚZIOS | RIO DE JANEIRO | Brasil | 3300233 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 76e044fa-e239-3f5d-b69e-64100540c33c | -17.78115 | -42.80979 | 2025-03-10 03:51:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dffef243-6e7b-315e-8dfa-bc27e67aa157 | -16.68289 | -43.88376 | 2025-03-10 03:51:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73b0f6f8-4a8b-3c59-9e00-ea33659d9ec6 | -15.08058 | -48.94706 | 2025-03-10 03:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5058118e-02b0-3a9e-b358-7b43fc541d17 | -17.82018 | -43.612 | 2025-03-10 03:51:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fd03e45-1661-351b-a4e8-d6003a0cbc99 | -21.65742 | -41.32639 | 2025-03-10 03:51:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 806aeaa0-7e6f-389d-a85d-88130d67c2e1 | -19.45144 | -44.91451 | 2025-03-10 03:51:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8bebe736-a205-3e05-a25f-f1e5edaba590 | -16.55795 | -43.20961 | 2025-03-10 03:51:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2241f3b7-a352-3c20-8620-957442a9cb56 | -18.02492 | -43.29 | 2025-03-10 03:51:00 | NPP-375D | FELÍCIO DOS SANTOS | MINAS GERAIS | Brasil | 3125408 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1420a2c1-0c77-3ea1-a32d-185ecadd1ea5 | -19.44747 | -44.9136 | 2025-03-10 03:51:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de6dc945-f2c8-3ec9-81dd-874a0c922879 | -22.75708 | -41.95675 | 2025-03-10 03:51:00 | NPP-375D | ARMAÇÃO DOS BÚZIOS | RIO DE JANEIRO | Brasil | 3300233 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f9fe78c2-cabc-3088-b944-d452d2a93df6 | -22.77376 | -41.94006 | 2025-03-10 03:51:00 | NPP-375D | ARMAÇÃO DOS BÚZIOS | RIO DE JANEIRO | Brasil | 3300233 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| a319ee0e-cae0-3a0b-84b0-f7875bec61c6 | -17.09515 | -43.80392 | 2025-03-10 03:51:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 208bc484-cdbd-317e-aae0-42f0da2b55af | -19.83279 | -40.11096 | 2025-03-10 03:51:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 047493cd-c5a0-3484-afe6-f17c5fbb4532 | -14.5663 | -46.72056 | 2025-03-10 03:51:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64bb7879-8743-3655-8371-53333261cc79 | -19.45491 | -44.31596 | 2025-03-10 03:51:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42c6c3ea-76ae-3e90-9e17-eae9051b0f57 | -16.75207 | -41.35551 | 2025-03-10 03:51:00 | NPP-375D | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d522680f-f9cb-32fd-b217-23d1cece4682 | -15.56981 | -47.85526 | 2025-03-10 03:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a1dbf24-6cce-39b4-b1e5-a01816dab26f | -20.41676 | -43.55322 | 2025-03-10 03:51:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7b055fa7-f18a-3fbc-a4fb-93b151e68c96 | -15.07693 | -48.94696 | 2025-03-10 03:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c5339c4-7191-3754-8971-c1dc5b336f10 | -18.02121 | -43.28928 | 2025-03-10 03:51:00 | NPP-375D | SÃO GONÇALO DO RIO PRETO | MINAS GERAIS | Brasil | 3125507 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c816f58-8e8a-3664-832f-29e69d7da667 | -24.01694 | -51.07403 | 2025-03-10 03:53:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1aa919f7-1919-388e-aba5-53249a7f5eb0 | -25.79052 | -51.09505 | 2025-03-10 03:53:00 | NPP-375D | CRUZ MACHADO | PARANÁ | Brasil | 4106803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e962f7f1-8321-31fe-a55e-3f1630b6fdf8 | -23.18072 | -45.88504 | 2025-03-10 03:53:00 | NPP-375D | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 61dc9e85-e8e5-3619-acb9-9bfce1545957 | -25.79557 | -51.09673 | 2025-03-10 03:53:00 | NPP-375D | CRUZ MACHADO | PARANÁ | Brasil | 4106803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a4441076-a0e7-3dfd-a0e2-7c5388ce2b98 | -22.80178 | -42.46444 | 2025-03-10 03:53:00 | NPP-375D | RIO BONITO | RIO DE JANEIRO | Brasil | 3304300 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ca952041-8b62-3af2-be78-34473b76f5dc | -23.17942 | -45.88283 | 2025-03-10 03:53:00 | NPP-375D | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |


[Clique aqui para ver as próximas entradas](README2.md)
