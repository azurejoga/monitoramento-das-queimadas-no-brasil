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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c4b82e8-6cce-3b68-9861-1ebdb5613927 | -10.74294 | -44.75122 | 2025-10-30 03:36:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 908eee35-170d-3fb8-8ddb-6c4fed567bf1 | -6.99096 | -46.23283 | 2025-10-30 03:36:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e7a1f181-319b-3463-85cc-e9f04ccc10b2 | -6.12959 | -41.70479 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1f8714d0-ab92-3562-9a6d-b1346c567add | -6.12378 | -41.85828 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f5e86cf4-66c2-34b3-8f18-3a1ea8917c5a | -8.32865 | -47.93893 | 2025-10-30 03:36:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 889b2e4f-7927-322f-99bf-25d165355353 | -7.65325 | -42.24546 | 2025-10-30 03:36:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b2b2ccdb-f845-3299-a665-e710d4adc695 | -10.85701 | -47.86827 | 2025-10-30 03:36:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ae3acad9-9a20-3e2f-a8b7-fdf78aefefa6 | -8.26584 | -43.92479 | 2025-10-30 03:36:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0572b009-cf08-3cbd-bab1-6a9fcbdf8260 | -7.46881 | -38.55697 | 2025-10-30 03:36:00 | NOAA-21 | CONCEIÇÃO | PARAÍBA | Brasil | 2504405 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 63aaeaf5-6122-33f5-8b22-881f2507236a | -7.29211 | -45.66585 | 2025-10-30 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3256ca0b-19e0-34e0-86f5-d5506c18c6a7 | -7.92472 | -45.64524 | 2025-10-30 03:36:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7d98a6af-f62f-3023-b3b5-2b05b63aaab9 | -6.1351 | -41.7028 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cca8bf27-4d23-3c9d-a727-d531dec96507 | -6.99524 | -39.13809 | 2025-10-30 03:36:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 7703696c-804c-3e8e-b912-ee6a0cf8cdc6 | -9.81481 | -47.57794 | 2025-10-30 03:36:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6ac4066d-7ac9-3b75-b24f-414a4fffb5de | -11.18083 | -45.2168 | 2025-10-30 03:36:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 61808c24-d363-3218-8b85-5c886683f0cb | -10.33322 | -47.09154 | 2025-10-30 03:36:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2226839d-1b0f-319d-9a36-fc2ead08f07d | -9.80592 | -47.58147 | 2025-10-30 03:36:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4e4f02ff-7f11-3c52-8d4b-c62c4b2db656 | -7.14552 | -40.46136 | 2025-10-30 03:36:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 88f86623-079f-33f0-a34c-cf8e6ad59098 | -10.65316 | -39.93352 | 2025-10-30 03:36:00 | NOAA-21 | ITIÚBA | BAHIA | Brasil | 2917003 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ecd21e4d-0a41-3298-8678-bba38efcf9c2 | -9.88339 | -47.44926 | 2025-10-30 03:36:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c36a3dff-9e9d-3438-93e0-4fcbcf4c8e74 | -10.76867 | -44.73947 | 2025-10-30 03:36:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d82ca162-08d1-3deb-8937-8484b120dab1 | -11.52897 | -44.96751 | 2025-10-30 03:36:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e902f62e-928c-38ca-8edf-8df2c282c51d | -10.25152 | -43.95711 | 2025-10-30 03:36:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 72e6ad1d-0fc1-3953-8ae3-83afd762e7ea | -7.59253 | -45.84953 | 2025-10-30 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b28bde3a-fc5a-3626-9305-12fd8377d439 | -6.13366 | -41.68134 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 76e48afb-4421-37c0-9ff3-90669dfe3257 | -7.62811 | -43.58378 | 2025-10-30 03:36:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 55f4743d-4b0d-3d6d-b62f-17e9752e7ff6 | -7.15466 | -44.70785 | 2025-10-30 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0afb516d-d2a2-3497-8920-6664216356dd | -7.15551 | -44.70316 | 2025-10-30 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42ab6662-ebf2-3d62-a519-b7022d6c2435 | -10.04367 | -36.14973 | 2025-10-30 03:36:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| c00ce0f3-99da-30a9-95d3-8cd9e8fb8a20 | -6.13406 | -41.70876 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d222b33f-5383-3f27-93cf-9776cae4367b | -10.04768 | -36.14657 | 2025-10-30 03:36:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5365e59e-23ce-309e-a825-c3d3cca1f610 | -10.48816 | -45.04055 | 2025-10-30 03:36:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ec39e594-b1a2-3430-a98d-7c2f492380d8 | -7.3321 | -38.85407 | 2025-10-30 03:36:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e158f1c3-55e1-33bd-bd13-f12c6b9073ed | -10.28152 | -44.58036 | 2025-10-30 03:36:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5eb294ed-80fe-3125-9b8e-26abd9d1f1cd | -7.6205 | -43.59413 | 2025-10-30 03:36:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb10fa20-717f-3d56-90e1-d302bf6f893b | -6.11854 | -41.7089 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 452e165f-cd1a-3c34-8505-ba37ea5bfd46 | -7.79164 | -46.42578 | 2025-10-30 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ae2a3954-73d8-3de5-a86a-1ac8b4cf4960 | -11.06929 | -47.53666 | 2025-10-30 03:36:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aeaf2c6d-02ff-372c-b638-0f168b16a62b | -7.62323 | -43.57918 | 2025-10-30 03:36:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9b795664-5a2a-3564-8b18-242cb63c7bb5 | -7.32357 | -42.48275 | 2025-10-30 03:36:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 10eb89af-8929-315d-9ced-683161ead894 | -8.70372 | -47.98213 | 2025-10-30 03:36:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c73da645-6243-3e90-8677-734e7e94c9aa | -6.52465 | -46.9082 | 2025-10-30 03:36:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6101f3cc-94ed-3223-a639-4d12d21ff09b | -7.38589 | -43.01001 | 2025-10-30 03:36:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0af35e97-993e-371f-88a5-32328108ddd9 | -11.17438 | -45.21904 | 2025-10-30 03:36:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e6f666f-a857-3465-845e-e3495e7ca42b | -9.88165 | -47.44783 | 2025-10-30 03:36:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 01149839-844b-39c7-ae02-d43114082f3c | -6.51773 | -46.90702 | 2025-10-30 03:36:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| cfd600ff-00b7-3514-b2e3-d3422d2fa0d0 | -9.31954 | -43.09263 | 2025-10-30 03:36:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9e58f0da-6ff4-3015-8e54-6b25bb24897a | -10.8834 | -45.07587 | 2025-10-30 03:36:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4c7653f4-7c3f-3d3d-9752-45c3bcfa6e3d | -7.28339 | -45.66303 | 2025-10-30 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc423851-65ce-3f3a-adbf-6058f39aa5c2 | -7.62897 | -43.6105 | 2025-10-30 03:36:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8cf42cd8-4994-3a1a-905a-55d3e450aae4 | -9.88838 | -47.44925 | 2025-10-30 03:36:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 12bfd475-b4cc-3c2c-bbbf-800d1ae105ae | -6.71166 | -38.21512 | 2025-10-30 03:36:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1d6e1468-8ecc-3997-85ba-f74fe713fdf6 | -7.40262 | -43.93869 | 2025-10-30 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5fbc07d1-b541-363a-a140-843057e7d73a | -10.47228 | -44.08355 | 2025-10-30 03:36:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d906655-5c2b-3f3b-b5f8-de2469c8f772 | -9.9042 | -47.9141 | 2025-10-30 03:36:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a873362a-f213-350f-b96d-4b69cb5deb39 | -7.46824 | -38.56038 | 2025-10-30 03:36:00 | NOAA-21 | CONCEIÇÃO | PARAÍBA | Brasil | 2504405 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7eaf3e8f-695e-307d-a15c-f3c8e3ce1360 | -6.14108 | -41.69804 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| aed30f60-a23b-32c1-bada-ad0f96a967cc | -7.32711 | -42.493 | 2025-10-30 03:36:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f42b481c-2b4a-37ac-8448-9838480d6ec7 | -7.62254 | -43.58296 | 2025-10-30 03:36:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a44a1cc2-1e1b-3886-b048-a624ebd3ad57 | -6.08498 | -41.78215 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7046ef1c-109a-3373-8afb-ce506986322d | -6.14364 | -41.56489 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 78332941-9655-3c40-be01-bf101931c455 | -6.52393 | -46.90952 | 2025-10-30 03:36:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0d802ae2-cd26-32e8-9611-1f3d704467d9 | -6.10956 | -42.43884 | 2025-10-30 03:36:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 4d66b190-6eab-39ee-9f9d-4cde2e5aefce | -6.85682 | -46.29166 | 2025-10-30 03:36:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a6dfe7eb-6d97-3415-b0c1-f71d6b2579d0 | -10.67808 | -48.04522 | 2025-10-30 03:36:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| afdd0591-cd03-3bf2-86ae-7db859df6aa3 | -5.41562 | -46.01369 | 2025-10-30 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7bc914f9-1a0b-3f5e-b2d9-423cc2dec2a4 | -6.1382 | -41.56676 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 41e090b7-7fb5-3f25-b45a-cc5cbcc6a18a | -9.90788 | -44.90535 | 2025-10-30 03:36:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 579467c6-f895-3561-ab18-5983adb358ad | -5.43104 | -45.34275 | 2025-10-30 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 7f91eb13-f609-36ba-a32d-1b6290d6af85 | -8.31717 | -45.37234 | 2025-10-30 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 27c6cccf-6f6a-31eb-8852-ca50ee95bee0 | -7.61768 | -43.5782 | 2025-10-30 03:36:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 497422e4-b8bc-3482-8f59-020c9229cd42 | -7.54413 | -44.04323 | 2025-10-30 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ae72dfe-499b-36b4-b5f1-3a62669a574e | -10.76378 | -44.73444 | 2025-10-30 03:36:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c5cb0a5-56dc-3b71-8a4f-388aa6f84ce5 | -9.81942 | -47.58478 | 2025-10-30 03:36:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0daa1553-6b41-3341-bd85-04a79235b7c7 | -6.19116 | -41.58593 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 56add0e5-209f-391b-8842-8b360728bb55 | -7.38526 | -43.01347 | 2025-10-30 03:36:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c03d7f76-020d-3a9f-a3d7-7c5808c5aaa1 | -7.95571 | -46.72879 | 2025-10-30 03:36:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a6aae0c6-ce4b-3420-b895-4c65cbe369c5 | -10.76779 | -47.88839 | 2025-10-30 03:36:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0b953c03-09a7-31e1-bd4f-ca714d659b63 | -10.75636 | -44.74249 | 2025-10-30 03:36:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be5bd4fa-66f3-31cf-9333-2e8848d4b284 | -9.84832 | -47.69015 | 2025-10-30 03:36:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 06e34cee-0775-3f4b-9afd-6f966a777b05 | -7.07647 | -44.93183 | 2025-10-30 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 34b82396-cc9f-3d96-ba38-773f6b0413fd | -10.28078 | -44.58431 | 2025-10-30 03:36:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cbaf29ec-296e-35c7-ba43-dd71fd635a30 | -7.38609 | -42.46868 | 2025-10-30 03:36:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8a57771a-b1cf-326c-ae0b-269637fa208e | -5.43291 | -45.33991 | 2025-10-30 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| c7f9a4df-d640-3c70-aa83-97a18b6cc2d2 | -9.9087 | -44.90101 | 2025-10-30 03:36:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c39993c4-725b-3ef0-80a0-51daee0d983c | -6.7086 | -38.20932 | 2025-10-30 03:36:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 376a4129-c26c-3023-a5e0-be9b69477735 | -6.85571 | -46.29746 | 2025-10-30 03:36:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4899ee77-4623-3766-aa8a-f26f0eb4d172 | -10.58484 | -36.84359 | 2025-10-30 03:36:00 | NOAA-21 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fdb9c35d-8b1a-33ca-85ec-f59c9a01ce6d | -7.08253 | -44.93311 | 2025-10-30 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3b84b002-70fe-3222-a748-0eb5e12facba | -7.96226 | -45.44424 | 2025-10-30 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 46fe5497-b77d-36d3-8a83-dc21f321f5f4 | -11.17502 | -45.21579 | 2025-10-30 03:36:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a3857cf-a2dc-3399-988b-4b1ab0799f40 | -10.36698 | -44.12751 | 2025-10-30 03:36:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b9ace74-0291-3686-96cd-2df9f4bfe19c | -8.33574 | -47.94041 | 2025-10-30 03:36:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a14fab8e-6f5c-3d42-abf6-91db36e74751 | -7.96166 | -46.71544 | 2025-10-30 03:36:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0f7028a0-ecb1-3731-b3e6-44efe510da87 | -6.17235 | -41.60606 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e6b2bc64-60be-3fe6-9cf0-281b3c1c21a4 | -6.36947 | -40.97252 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b372092b-40ed-317d-b47f-faadbc9ad057 | -11.9655 | -43.287 | 2025-10-30 03:36:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54f4f01a-507e-3b31-9e8a-ddbb1ee910ec | -9.84735 | -47.69692 | 2025-10-30 03:36:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 277e38bc-7bf1-326f-b77b-23d23a6dcbf2 | -7.62829 | -43.61425 | 2025-10-30 03:36:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 730191e3-2046-331c-8bbc-f013b383538d | -6.3135 | -42.10376 | 2025-10-30 03:36:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |


[Clique aqui para ver as próximas entradas](README16.md)
