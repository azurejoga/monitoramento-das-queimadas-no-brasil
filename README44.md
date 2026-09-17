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
| 27bb9dfb-1882-32fe-bf1a-8171926811d9 | -7.46231 | -46.8406 | 2026-09-17 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c5833354-3865-36bf-8958-55c92ac05015 | -9.17022 | -49.63633 | 2026-09-17 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7077428-d91b-36f9-87c0-ceeeeb9eb64e | -7.44608 | -45.29565 | 2026-09-17 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6753ce6c-68d8-3e0b-a367-0aee78a6a03d | -5.29361 | -43.63809 | 2026-09-17 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b5a16bc-5825-3781-b283-fe9c757abdde | -11.16358 | -42.7908 | 2026-09-17 04:40:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| b52576b5-c8bc-3125-b53e-cfae004c3faf | -5.54488 | -46.59639 | 2026-09-17 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb27b88d-3bff-39ab-9de0-c57b8f32d58a | -4.37528 | -55.03293 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0fa3445-b4e7-3341-a0d9-1d3a78271415 | -6.90123 | -59.03136 | 2026-09-17 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d143d20-9fd2-3f97-bf62-02254a12d1b4 | -7.94399 | -44.82974 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 147eff07-08d3-3774-8338-0e4e1870ef7c | -11.13885 | -49.04287 | 2026-09-17 04:40:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0592c988-bc58-35fe-bd6b-71fe45d9aad9 | -11.21393 | -49.94027 | 2026-09-17 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d28d18e-75f6-314b-9d0a-bd974d2a4c34 | -6.78135 | -48.66019 | 2026-09-17 04:40:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d10d38bc-c66a-341d-b59b-2f09d3e3581f | -11.88518 | -47.59009 | 2026-09-17 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77f7d1b3-60cd-3567-bb45-4de41b2b98b1 | -8.26917 | -42.17574 | 2026-09-17 04:40:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6dd2414d-8072-3b57-83df-f6ec7c510047 | -5.62077 | -45.2446 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9ae2f648-783e-3952-a239-2b1db14eda3b | -11.48172 | -45.76709 | 2026-09-17 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a915957d-63cf-3fae-8415-e31feb5f12ed | -5.65895 | -51.89322 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 748a2542-59a1-39f1-8501-adfbbe082d49 | -4.51221 | -54.96474 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ccae04aa-b642-33b8-a81c-8e382c31ecd1 | -7.97233 | -44.83413 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 943eb559-e268-3b67-911c-4029bbcd3bbf | -4.52544 | -55.66207 | 2026-09-17 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 862bb91a-1cc7-3115-b578-e5f78265fd1f | -8.78716 | -46.90901 | 2026-09-17 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 50136ab0-ec80-3baa-b0e7-b618dabcc555 | -9.47989 | -47.82867 | 2026-09-17 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8fd72a5-a901-3250-b198-8bebb93f9cce | -8.8709 | -45.88712 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e37171f0-2f33-3e06-ac92-ec13946e95c1 | -6.01235 | -46.64206 | 2026-09-17 04:40:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5dbcfcac-e302-3c2b-b050-ccbebb76b66c | -8.58423 | -44.56384 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fc47ec18-1a63-337f-bb46-08e254788bf5 | -9.86245 | -48.36794 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2605113-0b81-31f7-b13e-91aeee734f84 | -9.86217 | -46.76516 | 2026-09-17 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d8692b2-2684-37af-9f3c-0c13f6166b08 | -11.3543 | -44.02262 | 2026-09-17 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8804e50-25bc-3947-8703-1bb33b3f1739 | -7.08493 | -41.84679 | 2026-09-17 04:40:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 3c1cc7d8-356d-3bb3-a047-73e844a86ac4 | -8.3736 | -54.74076 | 2026-09-17 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6363d9b-0bad-37cc-af00-3b7c32f26a5a | -4.42035 | -55.50649 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 55b5deb3-73fe-3e0f-bac1-14c202d0e213 | -12.5006 | -45.91559 | 2026-09-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5e589a0-9f30-35ab-8ec9-d8ea98197a1d | -4.5387 | -54.93616 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e5d0fed9-3fdd-373e-a816-1ebb5cb8872c | -8.33258 | -51.31235 | 2026-09-17 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28a5cdb6-616d-3720-a2ab-6f63b2f27c0a | -10.3106 | -45.31906 | 2026-09-17 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 126fa0c3-263f-34ca-ae2f-20917ae1e5e2 | -9.11392 | -45.73431 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 7f897ee7-bb35-37f4-8135-8376d85b94fd | -11.13546 | -49.04233 | 2026-09-17 04:40:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fad00a50-e249-3569-a74c-e491b904f102 | -8.90839 | -43.88674 | 2026-09-17 04:40:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cb363bb6-edfe-3244-b504-c9604ceded05 | -11.59096 | -46.87295 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f699cce2-5286-3c76-8e35-af350a330763 | -9.62231 | -45.37009 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 13a1b31b-b6cf-36ec-936e-2de3f9d27579 | -7.9683 | -44.83338 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aee28284-c488-326b-8bf2-526554cf6c25 | -9.83841 | -48.36447 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc54e9a4-3c3e-3276-aac4-22696ef9ce32 | -8.25595 | -42.16315 | 2026-09-17 04:40:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 749d9327-9284-3c0a-8f98-da2eaa33c6b0 | -9.87449 | -48.38127 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1020e5ac-9193-3629-861b-4f860eeb3c5d | -7.99742 | -47.99923 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3598b05b-0a4f-3e8c-9a81-e74bc6999b38 | -8.77505 | -49.62067 | 2026-09-17 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8ce8f57-bb6d-3d8b-b44f-1dddac73f81d | -8.87866 | -62.39235 | 2026-09-17 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1e455ce-386d-318a-ac28-73cdb8066b30 | -4.45495 | -55.43571 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9af67014-c363-3d1d-a238-f7031c268502 | -10.50582 | -46.29161 | 2026-09-17 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 304995ac-b0f0-375e-95e4-af90d1a857d3 | -5.98509 | -46.62973 | 2026-09-17 04:40:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0252cf2-22bd-37af-8d85-541316aaff1a | -7.83242 | -50.23544 | 2026-09-17 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bad8c0eb-a4a7-369d-9d6c-2332dddd2698 | -6.78093 | -41.46796 | 2026-09-17 04:40:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1e62bb06-3a93-3fd4-befe-938bb6b60dae | -5.83732 | -52.09521 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 438961a3-f81b-3d1b-8a6e-1d8a671a14c4 | -12.31746 | -47.95854 | 2026-09-17 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 422dcb0f-b145-3b1c-a405-acece0e9468f | -4.49023 | -55.49364 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69581a3a-0f1e-3123-9e4c-5acb1155b52e | -5.32423 | -43.40299 | 2026-09-17 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a66eabb0-763d-3c22-8514-2ad68213b263 | -5.86438 | -51.9476 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9ac6bb7-ccaa-3452-8839-335563f1d9af | -9.61413 | -45.34051 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bc259846-21cd-3cea-9fef-2e57665d4b7b | -6.95863 | -42.58123 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4082829b-d2a9-36a3-8f7d-91666e2625c7 | -9.63429 | -46.0563 | 2026-09-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c44c94e3-f6ab-3b45-a8a3-b7ef639910c7 | -6.67964 | -43.65153 | 2026-09-17 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6ef845c5-cfef-3659-8461-e2040ab49230 | -11.57403 | -46.88448 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d255b473-0bc5-35b7-bb50-b438194058c9 | -11.89027 | -43.82257 | 2026-09-17 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f8c8a8ed-4979-36a0-a117-aca0e3165bc0 | -8.8625 | -46.98313 | 2026-09-17 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64308191-6cd2-3fb4-ae44-6bddd2824ffb | -8.37005 | -54.73806 | 2026-09-17 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a15d3123-f346-360b-96c2-60e0360c371e | -10.89695 | -48.36446 | 2026-09-17 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 22f91bcd-51b3-3064-af46-2215b8bb4d41 | -9.5174 | -43.13699 | 2026-09-17 04:40:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 594cdb52-8ef0-319e-8466-bdfa256d7830 | -7.27701 | -46.79939 | 2026-09-17 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10dc199d-1580-3cbb-8dee-169a989a8360 | -5.88919 | -52.09143 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 19ce5393-0eb4-3531-b89b-2a0ea34de3f5 | -12.14429 | -48.25463 | 2026-09-17 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f6255bd-32b4-3795-8a5d-b50676215034 | -10.11795 | -45.57468 | 2026-09-17 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 26b8e8a2-05b8-360d-872d-7f5e63811289 | -8.56647 | -44.47792 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96639db1-302e-38bc-9794-1e3dcff6e8d2 | -11.58465 | -46.89053 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d8002584-6c4b-3a88-8384-1e30bf96dc46 | -5.83443 | -52.09081 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8c78436a-95d2-31f4-b68b-4537520844c7 | -5.78791 | -47.24158 | 2026-09-17 04:40:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5bc2936-846c-367f-baee-31b3bce3c86d | -9.15961 | -49.99173 | 2026-09-17 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32a3d61d-e7df-3035-9d51-2c57ba59acce | -11.27647 | -43.47321 | 2026-09-17 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c5caae94-6ee2-3f49-97f0-a3b5d6c6676d | -5.77013 | -45.09846 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a6875a9b-f25f-3a54-b0a1-c51805d6ded9 | -5.99968 | -44.26151 | 2026-09-17 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57b6d343-57a6-3a54-971d-6b5dd592750e | -5.77259 | -45.10861 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 9b40b324-d4d5-3f8c-ad5d-9965beb2aef0 | -7.09233 | -43.47462 | 2026-09-17 04:40:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b8ee2cae-3718-3973-8221-1dcb4e74f697 | -8.48199 | -57.64033 | 2026-09-17 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| ec028a14-a3b4-3bf0-b7a9-0705a30db955 | -10.27866 | -48.27706 | 2026-09-17 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9e5f94a-e226-3b80-9fc6-000251690150 | -6.77366 | -42.77076 | 2026-09-17 04:40:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5d5b1b38-9411-3097-8e75-f8b8e4875aaa | -9.02253 | -61.00695 | 2026-09-17 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ede64824-c307-3da8-ab07-d1f55ab62cf0 | -9.86992 | -48.38834 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0926bcb4-a8a8-3c1b-b799-8a7bac63bb91 | -10.21539 | -43.18765 | 2026-09-17 04:40:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e7db4304-4241-3f3b-ac0d-8183984fb94a | -7.45701 | -46.16177 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84ba26e4-87d0-3f45-be05-d219bd98c507 | -7.85668 | -44.82851 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aeb06a62-7334-39ec-a1c4-ac0fb7967f8f | -5.56036 | -45.52161 | 2026-09-17 04:40:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6a51fb0-96d3-3551-b8a5-c7112b523ef2 | -7.38802 | -44.49898 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 915f8331-25c2-3b25-9b93-9f2a59d5a514 | -10.832 | -46.14248 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d768ab73-afc8-30a3-aa5f-f5eac0f60083 | -7.07813 | -42.09609 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0fa5903a-5020-3ddb-8c1c-9a53ecf7c374 | -6.66358 | -43.64096 | 2026-09-17 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c60a1a18-7318-38c9-baa5-76f0750582f3 | -8.37446 | -54.73571 | 2026-09-17 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 303d7abb-34e1-356d-a737-9f43f1e914db | -7.08737 | -43.57323 | 2026-09-17 04:40:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9cc82778-d642-31bd-99a2-faa188e57fec | -10.11105 | -45.5657 | 2026-09-17 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 256689bf-8cf7-308c-a830-c247a22b4a5c | -6.36794 | -58.28819 | 2026-09-17 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ece5fbc2-8820-39c4-9e97-27dbc7def6db | -7.85013 | -44.8163 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8924aef5-fc83-3d31-b7de-878643a619b5 | -11.21661 | -46.40134 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README45.md)
