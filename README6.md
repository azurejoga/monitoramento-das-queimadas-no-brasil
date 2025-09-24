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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5030906e-ae34-3abe-b780-e7fdd04b2f40 | -6.79626 | -41.76586 | 2025-09-24 04:00:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b325fb87-8768-3fb1-a531-3652f02b1cbf | -6.32075 | -43.62587 | 2025-09-24 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9357eab4-80f7-38c7-a689-f3e9ca2fd170 | -5.84696 | -42.64985 | 2025-09-24 04:00:00 | NOAA-20 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 4cc58d0d-75ef-369a-816d-7f5104129b84 | -7.25958 | -43.00365 | 2025-09-24 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d48ae4ee-42e6-336e-b176-7031177760df | -7.28478 | -41.86693 | 2025-09-24 04:00:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9d66aac5-cb97-39c3-a817-ebaa81190fe9 | -6.07059 | -44.08818 | 2025-09-24 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4b545ec9-18c3-39ed-8cd1-d7f1a5ea2cc2 | -5.68253 | -42.78863 | 2025-09-24 04:00:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4da02bd0-1456-3cb5-b750-164b7f96fdd7 | -6.00142 | -39.10108 | 2025-09-24 04:00:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b356cf66-9d78-3185-8ff5-50e376755068 | -5.42383 | -41.31285 | 2025-09-24 04:00:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e2271b43-b4e9-3ce4-9570-90ac1029726e | -5.63177 | -45.7277 | 2025-09-24 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4ff3403e-21d6-35d0-8b9d-58273b87b9e5 | -4.63522 | -43.18933 | 2025-09-24 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a39b4385-55a4-3131-a12a-3ebd295a5413 | -8.81632 | -43.08174 | 2025-09-24 04:00:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 56ea20e6-8aab-3344-84ed-42aab2dbe169 | -7.64631 | -45.21881 | 2025-09-24 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0932216-c74e-328f-a107-95e255bac9ac | -9.21055 | -43.13186 | 2025-09-24 04:00:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| faccc1e7-383e-3ba4-8362-a6a7dfe59407 | -7.76816 | -46.20212 | 2025-09-24 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 915cc31d-3c25-310b-b250-d6f78189142d | -3.14839 | -49.11675 | 2025-09-24 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e17d4d4-ec07-3bea-afe2-0abd442fc4d2 | -7.17484 | -42.24104 | 2025-09-24 04:00:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fcf939f0-550c-34b3-b3d2-629885304ac2 | -8.93906 | -40.61253 | 2025-09-24 04:00:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4d8ba4ae-031b-3fe9-8bd8-cf8f6662f2b3 | -6.15501 | -39.65829 | 2025-09-24 04:00:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 563fb76d-cc58-30fe-9eac-d9334f77e260 | -5.96807 | -44.12383 | 2025-09-24 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc1b05e1-3489-3f40-9feb-e36dfdad36b0 | -5.30538 | -42.75324 | 2025-09-24 04:00:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3bf8c161-4840-3d43-ae0e-3e01898792e0 | -7.28818 | -41.8675 | 2025-09-24 04:00:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 92918ae7-675d-3bbb-b4c5-a23c121f6498 | -7.94862 | -44.10683 | 2025-09-24 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5db5aa30-4d4f-339a-b401-fc74aa99a1f7 | -6.72842 | -42.73236 | 2025-09-24 04:00:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e3b9db84-f245-39d8-9bb3-be404640b571 | -8.81673 | -44.3452 | 2025-09-24 04:00:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5813cc1b-276b-3a45-9ec3-876852462579 | -7.28878 | -41.86378 | 2025-09-24 04:00:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 663705a2-b6a7-360f-9ce1-87594219a1bd | -5.17027 | -45.43163 | 2025-09-24 04:00:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| afe430b5-0171-315e-bab6-bc2cd1d9d3df | -5.76069 | -43.96699 | 2025-09-24 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32c4e9e4-0a84-3dba-9bdb-caccbdae9a55 | -3.62314 | -51.91157 | 2025-09-24 04:00:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d99a40b8-3411-32c8-b25e-6dab2ae50b4a | -3.39209 | -47.49546 | 2025-09-24 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00bcce0e-a96d-3108-a787-f5480f364dd9 | -5.77805 | -42.56125 | 2025-09-24 04:00:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a3da7d9a-aff7-3b78-b036-a451b74cc85c | -6.42041 | -43.08749 | 2025-09-24 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 57ee8de6-bf37-37b2-9922-9dd1e2c4c065 | -6.1996 | -37.62724 | 2025-09-24 04:00:00 | NOAA-20 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 632af295-cd7f-32e3-ad60-584a4529fec1 | -5.39196 | -42.28131 | 2025-09-24 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a5091f7a-7598-387a-a700-70ae13297c3a | -3.41188 | -52.68005 | 2025-09-24 04:00:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3e5f10be-78e9-36c5-a738-ce14f8180790 | -3.14777 | -49.12051 | 2025-09-24 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25a0b633-c1d8-3306-b2cb-2088937d8bb1 | -5.76837 | -42.57609 | 2025-09-24 04:00:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ac25eeca-c090-3b7e-93ea-d84ef6f1c8b9 | -4.30363 | -48.09711 | 2025-09-24 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e711c492-bee1-3db3-aabe-cf381b36907b | -5.64091 | -43.91578 | 2025-09-24 04:00:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 7ef0efac-d397-32ec-b0f0-79cb979ff363 | -3.81078 | -41.55378 | 2025-09-24 04:00:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 785bc195-e793-373a-a226-33b2be350b2c | -7.76887 | -46.19796 | 2025-09-24 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 52bed925-3d28-3fdb-be4d-28934d433c4b | -7.64691 | -45.21527 | 2025-09-24 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 002627a8-715c-3f7d-ae81-ad2aec74cc4a | -4.31448 | -48.09584 | 2025-09-24 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 699ead36-9263-321b-8175-63b1ba9481d1 | -6.42265 | -43.09653 | 2025-09-24 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 91678524-5cb2-3d57-9d20-5fa73cdaf439 | -5.73733 | -43.7989 | 2025-09-24 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 992a47e2-4bb3-3437-8326-ee5a27b2475b | -6.83675 | -43.17682 | 2025-09-24 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| e42657a4-1444-3f17-93e0-77142375fa85 | -7.95236 | -44.10749 | 2025-09-24 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b4981f2d-cf59-30bf-b543-206b58773a22 | -5.75189 | -42.56522 | 2025-09-24 04:00:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 614085f3-708b-3121-9dd0-1f93811a37cb | -6.07521 | -44.0841 | 2025-09-24 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9d1768d9-f5c8-3070-afbe-9637a1150d8d | -9.52449 | -40.41 | 2025-09-24 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bbd72033-9486-3d65-bacf-7e62afdbb653 | -4.07563 | -48.04485 | 2025-09-24 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1cd0d20-3566-3764-99da-408be4ac5146 | -8.34501 | -40.82394 | 2025-09-24 04:00:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 064e9ac4-6af1-32a0-a779-3868d983dd04 | -5.38971 | -42.27282 | 2025-09-24 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5a7c5738-b977-3160-8d69-01600630e675 | -8.78837 | -43.0321 | 2025-09-24 04:00:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 83fa05bd-a20f-3d3d-9e71-b82f4dd407da | -3.86599 | -40.35966 | 2025-09-24 04:00:00 | NOAA-20 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d743dc7b-55bf-3a52-8e79-62f3a5b5ae77 | -7.73915 | -42.95422 | 2025-09-24 04:00:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 816f1a58-0f82-3dc9-8baf-e41474c361b6 | -8.36852 | -44.70957 | 2025-09-24 04:00:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e80c0629-b248-3c73-a21f-36f030e36efa | -7.54997 | -43.9374 | 2025-09-24 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| efc9ff2a-6c55-305b-8b08-be82a9b34cd6 | -7.27299 | -42.98907 | 2025-09-24 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aba02d7d-0aca-366e-af16-f79e16d69c16 | -4.79458 | -43.54156 | 2025-09-24 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 807ed733-36a2-3d68-baa6-3f7a351f3462 | -5.6311 | -45.7317 | 2025-09-24 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cfac1e52-eb62-3125-8e2d-3d93b53469cd | -7.61 | -40.51009 | 2025-09-24 04:00:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6b1cb9c8-20be-3c76-b3f3-846c82ac8968 | -5.24636 | -43.72056 | 2025-09-24 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d6a83781-b1d4-37a5-99d4-b9d562ab40ab | -6.96468 | -38.58776 | 2025-09-24 04:00:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bdd826f7-36f6-32fa-b34c-51b332cefd08 | -6.06672 | -44.08772 | 2025-09-24 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e38f495d-e2f0-3149-b7ed-79ff722ddf62 | -5.73627 | -42.6166 | 2025-09-24 04:00:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 651c4796-6820-3a8d-81d9-c11a5c53904a | -4.74954 | -43.62499 | 2025-09-24 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fa9d7d41-a492-3793-b9bf-2daaf403dd04 | -6.56227 | -43.83221 | 2025-09-24 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9535d89d-e8d8-3c27-a72f-e36b7d03a2b8 | -5.91733 | -43.92911 | 2025-09-24 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1aeb53b0-cfd9-3fa2-a17a-b3dcc8b1cc7d | -6.42627 | -43.09713 | 2025-09-24 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4c3135dd-3db6-389c-9475-d8893c3b4364 | -5.64137 | -43.60599 | 2025-09-24 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ebec90e6-3df0-3f56-bd42-c85a2858c2cc | -5.30589 | -44.8134 | 2025-09-24 04:00:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b60942fb-abcd-3e94-a5b5-668566844c07 | -8.8423 | -46.18661 | 2025-09-24 04:00:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bdc893b-e9a6-3688-9dde-335c88550bb4 | -7.19946 | -46.674 | 2025-09-24 04:00:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b8e6dc6d-0fce-3f03-88f8-3fe59fe97314 | -4.7508 | -43.62243 | 2025-09-24 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3d14741-92bf-33e6-9716-de1edf049e0d | -7.85467 | -46.7788 | 2025-09-24 04:00:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 631354e5-38c0-3879-8f05-06a9cea23e15 | -6.18374 | -46.44049 | 2025-09-24 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9df8b62e-ab7c-3c35-848c-4583ebb4af18 | -4.29182 | -48.26406 | 2025-09-24 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e96b752e-ad0b-399b-9168-f56e09be4381 | -5.38556 | -42.27621 | 2025-09-24 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ade58bca-c854-3416-89a8-f589ef9343de | -5.23955 | -43.13886 | 2025-09-24 04:00:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a525b38a-4c14-3e82-bb5c-b05a3ad4fa1f | -5.78517 | -42.56229 | 2025-09-24 04:00:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f90e9615-365d-39c2-8845-806532aa0806 | -7.82256 | -47.86339 | 2025-09-24 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b3e5dfa-5085-30f4-b31d-08275950f185 | -7.77823 | -46.19478 | 2025-09-24 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9c3d68a9-2711-390e-ab56-ef3df1527ae8 | -4.79079 | -43.54092 | 2025-09-24 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 117604ee-daa8-3e8c-a2e0-67680e6bf81a | -3.62972 | -51.9132 | 2025-09-24 04:00:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b548a21-105c-32f6-bd01-ddbf18feb39b | -5.73352 | -43.79831 | 2025-09-24 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4e8de398-747d-3eb8-93a6-881a9d0e5657 | -3.64688 | -48.32529 | 2025-09-24 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97ae111d-2621-336f-89c3-d7bfc7f55ee1 | -5.88627 | -42.82692 | 2025-09-24 04:00:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 8e60dee7-b49d-3eb8-abb5-dc260887f433 | -7.82443 | -47.85664 | 2025-09-24 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 263da7e8-1d0f-3a7f-80db-7d7d77245bad | -5.91451 | -43.8524 | 2025-09-24 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 872a45f1-d059-30dc-a05d-020e6201eb7a | -8.79254 | -43.02874 | 2025-09-24 04:00:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 907efc59-8e14-3740-a874-e76df94a0125 | -6.89486 | -44.76936 | 2025-09-24 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 592eaa56-13ed-3736-b460-25110ddf8d33 | -5.30924 | -45.32467 | 2025-09-24 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b85c2db4-3f38-358a-ac5c-624ded6a094d | -7.52014 | -42.27566 | 2025-09-24 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 46bd21f1-f2ad-3851-9c17-79f1cf183fb4 | -4.16729 | -47.22924 | 2025-09-24 04:00:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aef5d1d0-086c-3dc1-a8c8-62a4639fa032 | -6.56218 | -43.83057 | 2025-09-24 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 04669eff-65c7-3172-97b7-2c8367411826 | -5.91753 | -43.85768 | 2025-09-24 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| edd58e33-7c9a-3ae9-bd24-54439fd1bd9b | -5.51999 | -44.21338 | 2025-09-24 04:00:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c475e83-ddc2-35f5-a5f1-3575be03a326 | -7.38012 | -47.04341 | 2025-09-24 04:00:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 53663c02-2ef0-3b2e-ad77-b9bf4f6cde06 | -4.64707 | -43.37582 | 2025-09-24 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README7.md)
