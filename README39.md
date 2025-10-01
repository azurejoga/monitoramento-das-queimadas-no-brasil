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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 649091cf-6fbe-3f7a-8dfe-5e5897fd7010 | -5.90424 | -42.92607 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 70604eeb-1cd7-3f7a-95b9-72160e726735 | -3.94322 | -41.59108 | 2025-10-01 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b9394e7a-b7f4-3125-a6d5-1d0f98f74d11 | -6.46031 | -43.93379 | 2025-10-01 04:19:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 01931ee7-d8d0-3737-aa15-6407621cfa7c | -5.76496 | -42.86822 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2c0efd32-e546-3713-95e9-95f9a9b45086 | -6.26186 | -43.65588 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 040300ed-6836-37cd-9bb3-b90bdb1f054a | -7.48374 | -47.26966 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b159a02a-32c0-35b6-b04b-ac6bd0492d2a | -9.93948 | -43.65397 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6ae4a1a-ce90-31ff-b8d4-ddd9035f7f49 | -8.89548 | -45.03319 | 2025-10-01 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7be7206-19a0-3b34-b7ed-f8a6bc1502b9 | -5.62301 | -43.23077 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 4934728b-c377-377c-bc65-320903ca9545 | -2.51773 | -44.11952 | 2025-10-01 04:19:00 | NOAA-21 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c3336045-0ae1-3d56-bce6-28899571d666 | -9.77733 | -46.2228 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70b909a6-9b48-32a3-b975-e011f9e2752d | -6.37918 | -45.6049 | 2025-10-01 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a630f027-9494-350d-a2b6-3b4e689375a4 | -6.27438 | -44.0586 | 2025-10-01 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f1e3f4a-4fe8-304b-9b47-0ea31f9b5689 | -9.92819 | -43.68277 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 012a8302-0c0d-3753-b2ac-f0def1fc27a6 | -5.90079 | -43.92204 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2ee83bd4-d01f-38a7-9c02-a4bf9c5d91ed | -5.94734 | -45.86094 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 201e2b11-1591-37e5-bf53-f66e53d838e2 | -6.73114 | -49.64013 | 2025-10-01 04:19:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57ae1fb6-b1eb-3352-9e85-7c23e6788416 | -6.83057 | -42.99053 | 2025-10-01 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| bc57d94a-f29d-3011-9712-b1139488ae9c | -9.26335 | -45.68598 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98ede6a7-a40e-3ba6-9fcf-cca228cebe4c | -2.63772 | -48.03877 | 2025-10-01 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56b0def2-7bba-3711-a949-213d0dd4b50b | -6.05043 | -43.61542 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7a089e4a-f3fb-3dd0-a8f4-eb5efd027c22 | -5.89061 | -42.50762 | 2025-10-01 04:19:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fb89c0a8-1d6e-37fe-a4a6-d1e642888ece | -5.91675 | -43.90665 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad740245-1b8a-37bf-8743-6a20db164ce9 | -9.35137 | -40.51789 | 2025-10-01 04:19:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| de95031c-2406-321f-bd1b-d908ef83b150 | -6.3098 | -43.47831 | 2025-10-01 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed25886f-c5b9-36b9-83b3-92f2b8747aa1 | -5.32291 | -43.32631 | 2025-10-01 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7df6bb74-6b14-3768-bfd4-a1f31f0ce95d | -9.93714 | -43.62302 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3cb38fa6-617a-315d-ab08-e423ae8c8c41 | -6.79319 | -45.61353 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 12420a69-3366-308e-8da1-ef3b76049a97 | -5.77469 | -43.30848 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 048ca80e-21cb-37ba-8aa1-72d8a209027c | -5.90249 | -43.93296 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddf36f27-7c7f-3ea9-a470-d983e0dfa651 | -6.26907 | -43.65337 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44de49be-940f-35a2-bef6-a339f4ef49a5 | -5.17986 | -41.24228 | 2025-10-01 04:19:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 92568a95-9271-37f7-b9bb-27df4bd84e07 | -5.06234 | -45.60107 | 2025-10-01 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee0ddc67-da06-3630-b559-0ef280562e91 | -6.11168 | -43.44041 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fbe4067e-0208-35e2-98f6-b1bf492abdb8 | -5.8872 | -43.68036 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c15f8e3e-20ab-3b39-a009-287ea6e581cf | -7.05261 | -46.42484 | 2025-10-01 04:19:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 184eba6c-db23-3eac-870c-0cd0fdf9b727 | -8.55502 | -44.73027 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f80deb4d-9a54-3b13-86dc-cab74d044c87 | -9.276 | -45.69154 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a446971-2dc2-3af2-b745-cf987f86fa0a | -5.91019 | -43.92705 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b3a6367-bdcf-3b24-960d-d74427679e76 | -6.35403 | -45.89267 | 2025-10-01 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80149943-8516-3244-8a3d-b6f4d48f03f1 | -6.8683 | -45.6325 | 2025-10-01 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ded8953c-aefa-3f4b-b3f5-fda9116b99e4 | -5.61855 | -43.89887 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e1349796-ba1d-3afc-bfcd-ca720257d1ad | -5.4451 | -44.64144 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a39a1ec3-ac3a-34d5-9dc0-7f67d863ac52 | -4.62632 | -43.54138 | 2025-10-01 04:19:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 52995b7b-49e5-3890-8b6d-55de67bd9375 | -6.5759 | -43.4464 | 2025-10-01 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 41e49917-1c3c-3eab-95b2-ee8f2959c5a7 | -8.55839 | -44.75217 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 39978189-fdcc-38a2-b4fe-a7ef79852da1 | -6.5795 | -51.6779 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84a795e8-8a28-3060-b39a-0dcf6683935a | -8.89899 | -46.62556 | 2025-10-01 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 419db441-8218-39ae-b2a8-5451d1c13973 | -3.08938 | -48.48941 | 2025-10-01 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7de7ba8-01e4-3835-bbbe-3f5550c09a75 | -9.92992 | -43.69447 | 2025-10-01 04:19:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cc1dda64-6fa6-3e1e-a361-4bac7a42974d | -5.95681 | -45.86607 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 544ab2a0-6521-3f3a-af44-9a018204fb4d | -5.67904 | -42.62905 | 2025-10-01 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 56c411f1-288e-33a1-bf48-064ff13d0499 | -7.6335 | -45.44211 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b4e2ac7-8fea-31e4-b49b-652464bbb242 | -6.12248 | -43.21502 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 24719075-f53b-38d1-a34c-e90384474cec | -9.4156 | -47.33838 | 2025-10-01 04:19:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1548f6eb-7b50-39f5-a3df-4ee16b48d3fa | -3.50873 | -53.45301 | 2025-10-01 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 551ff113-f9d1-354b-9b09-b32f5d5e5115 | -5.24405 | -42.90765 | 2025-10-01 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 79fc477e-b550-3f91-99d4-28cd262ec6da | -4.58384 | -45.61577 | 2025-10-01 04:19:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0803f274-7213-3cb5-99b6-53e83245d245 | -7.16474 | -50.54236 | 2025-10-01 04:19:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a52e2c9-f376-3e23-a31d-2ed3d70f515d | -8.55279 | -44.72281 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c829661-e087-37c6-8b37-0e42689708a6 | -7.01836 | -44.45903 | 2025-10-01 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 640ff4b6-affd-3ab8-9e84-b63f456d3959 | -7.04982 | -46.4207 | 2025-10-01 04:19:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0f62d34-bacb-3a9d-9a4c-ed0855c976f5 | -5.31989 | -42.77418 | 2025-10-01 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fe8153d6-9c42-3f06-aeaf-dcb8354feaa7 | -8.72273 | -47.98823 | 2025-10-01 04:19:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8fb0c6d1-8ca4-3cb0-82c4-a8ec05873150 | -3.50815 | -53.45653 | 2025-10-01 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d907b3ea-789c-3d9e-a151-42c22ecef0a4 | -8.5826 | -44.7488 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d7fdbaa7-39f3-3b54-bbb5-8e66565d1dce | -9.80231 | -45.93649 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ed78664-6420-3db5-8403-3627d5de51c9 | -8.68031 | -40.9521 | 2025-10-01 04:19:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 22c8948a-10c7-3d06-9a4b-2301f8e96184 | -5.94344 | -45.86395 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17e1b7e6-1772-37fc-9feb-29bc9da821cf | -3.93568 | -41.56979 | 2025-10-01 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a71fb846-bb6b-32fd-9efe-27109f691dab | -5.76382 | -42.92036 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e95d991b-d023-3148-b7f7-d96e75a9fdf0 | -5.95347 | -45.86553 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cd0817e4-0d02-3fd3-a43a-f0e8ec78af5e | -5.79148 | -43.06501 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 48426e34-349c-360e-b551-5c8938f73a07 | -5.93948 | -45.91072 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc6d294b-2497-322f-8fbf-40c7769dce60 | -2.2465 | -47.88583 | 2025-10-01 04:19:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8ffb287c-f1e6-396b-9bc2-bb25dac3ad1b | -5.95459 | -45.85844 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de273643-6826-3406-98ed-a88f05975c7a | -6.42905 | -43.07298 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4a4ef5d3-9599-36bd-bcd7-68fbe63a4ec2 | -8.53465 | -44.70567 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6f485ddc-e4a1-3603-80a7-461ca7979cdc | -5.85731 | -50.06781 | 2025-10-01 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f498b096-53cb-3e6f-91c5-a9893fe215af | -9.93724 | -43.66891 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 76da8b48-7873-3256-b7e4-274d7d8019d3 | -5.38615 | -42.87029 | 2025-10-01 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7066e0f8-14a6-391d-aded-7c71fca94ab2 | -6.11744 | -43.22535 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2cc492c5-4835-3459-abbd-c8b8ad9fbae6 | -6.08423 | -42.47876 | 2025-10-01 04:19:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5b7b9acf-4ada-38de-8446-fc4a2996c568 | -7.79001 | -42.50615 | 2025-10-01 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| f658b406-eda3-32a7-a10f-707eea0c9aff | -8.54559 | -44.67885 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21ffbead-4369-3c1f-bfbd-415b33ea87f4 | -5.38741 | -43.59159 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 26cd6162-5a0a-31fd-989d-7ca3879d4261 | -5.33062 | -42.77212 | 2025-10-01 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 22863805-6ce2-3b64-83ee-14056512ec05 | -6.0871 | -42.43636 | 2025-10-01 04:19:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 683ea17f-d465-383a-8b2a-4cb4abada635 | -6.10503 | -43.46127 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ceeb291-7241-383e-8907-742785aba7bd | -3.82879 | -52.04261 | 2025-10-01 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b28c5f6-fe67-3e2c-a32d-fbd7ef39abee | -5.64741 | -41.24325 | 2025-10-01 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b43bb598-99cd-36e8-8b44-809757252e46 | -6.66508 | -41.39842 | 2025-10-01 04:19:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ea201539-25ec-3264-9b17-cd2e9af69e4b | -3.46793 | -50.09068 | 2025-10-01 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 33f93310-d4e0-3b6c-b6c8-62c0f89b9642 | -5.82218 | -42.45168 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ec2c5950-112b-3553-8133-e08d74f0b9fd | -8.2995 | -50.76744 | 2025-10-01 04:19:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6c7db298-f25e-3754-add5-01b8ab24ab0b | -7.55495 | -46.28128 | 2025-10-01 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c1e856e4-968f-3e0b-96e8-510a15fdb4e3 | -5.4039 | -43.24045 | 2025-10-01 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 099a22e2-dbdf-3190-8c93-fa33ebd3cf98 | -3.25461 | -50.12162 | 2025-10-01 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 651c5f9c-5cfe-31f4-817e-567f92f5d576 | -4.15861 | -40.00528 | 2025-10-01 04:19:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0eb53ffa-a283-3832-bbb8-cdb872861c90 | -5.63818 | -43.90548 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |


[Clique aqui para ver as próximas entradas](README40.md)
