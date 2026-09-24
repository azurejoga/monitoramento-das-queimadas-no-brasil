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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e946210-b27c-353e-a425-a993e724ab4a | -3.18258 | -48.01451 | 2026-09-24 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ba41eaea-0d8b-36e3-b366-f814e9344e64 | -6.26917 | -43.27317 | 2026-09-24 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 50df5242-e1e8-34b5-8e66-3b3d8d27d0e5 | -5.19741 | -44.69145 | 2026-09-24 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d03ab197-57bd-3c69-935b-86a6fd03cc7e | -8.51338 | -39.92093 | 2026-09-24 04:08:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 59394134-0b5b-3843-9804-78655474db57 | -7.46185 | -44.53808 | 2026-09-24 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e06cec8f-bfc4-3e76-9b7e-7fe9cafc883d | -3.04719 | -46.92565 | 2026-09-24 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c3d4e2ec-3fd2-37f1-943a-8b03ad006ade | -7.08076 | -45.61823 | 2026-09-24 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f298711f-e3b9-3979-ad12-bf896897e89f | -4.94297 | -46.03994 | 2026-09-24 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 195ff03c-07c7-39ab-b05c-8a8c89bc6d38 | -6.07562 | -44.87427 | 2026-09-24 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d3e0defe-0f55-35ae-bb2a-6776602bf230 | -6.63926 | -47.70378 | 2026-09-24 04:08:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac61efe3-8bbb-39a5-9cb8-c8f6222c2615 | -8.89906 | -46.81534 | 2026-09-24 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d130df84-2397-3a32-be77-9925cc29bf62 | -7.27344 | -45.53798 | 2026-09-24 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a390aca4-42f3-3a46-8540-e70d5b26b717 | -9.25481 | -46.248 | 2026-09-24 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b9deee6-dfbb-3906-8d68-6bcd79f14501 | -2.83032 | -46.70869 | 2026-09-24 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa61902f-e2fa-35e6-a351-64ac8e5b5ef9 | -3.18105 | -48.02393 | 2026-09-24 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0d94ce2f-9d04-321f-8c62-ba92dad4df3b | -3.23758 | -54.32577 | 2026-09-24 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3af0fc21-c266-337b-9a45-a21ab016fe3e | -7.0297 | -41.55033 | 2026-09-24 04:08:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 908452b2-e025-3011-b546-a1efc150fbc3 | -8.80577 | -37.12094 | 2026-09-24 04:08:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f6a3b876-efc4-3a94-b0e4-39a68a65a773 | -9.5404 | -45.36855 | 2026-09-24 04:08:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5f33f93c-bd17-3ff2-8344-458086fbf3ab | -1.02493 | -53.73303 | 2026-09-24 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5d938974-a163-3cb2-bda4-83a8bdc9c78d | -4.02333 | -52.06639 | 2026-09-24 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 183dc954-5ec0-3208-a750-d8e59e6a2cf0 | -5.57501 | -42.30159 | 2026-09-24 04:08:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4f7d23b0-6b13-371d-a9c9-39bdef069f10 | -5.29424 | -49.2877 | 2026-09-24 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b475ac17-8923-35b7-ab52-f6d23fab1aa0 | -6.65213 | -43.62709 | 2026-09-24 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d01a20a3-43ef-323d-8e24-087282f03af1 | -8.67919 | -36.33823 | 2026-09-24 04:08:00 | NOAA-21 | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 071a5b13-a9af-3a4b-813e-bad1d64333fd | -5.36246 | -47.72192 | 2026-09-24 04:08:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db2823fe-7c62-3700-9d4f-718b174c3a42 | -6.8565 | -45.54227 | 2026-09-24 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d28c660-19be-3125-8a37-ed3ba08d167f | -6.40595 | -46.20383 | 2026-09-24 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0fe9d5d5-2d41-3195-b79b-ddb523e57cd4 | -7.27083 | -46.79207 | 2026-09-24 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 39675370-9376-3e38-9bea-2f1dfeb8c75f | -6.60773 | -43.73026 | 2026-09-24 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e0d4db4-afd4-352c-afac-4d318f932b83 | -4.99734 | -45.55574 | 2026-09-24 04:08:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| b3b8b575-0f2f-39be-828a-afea6f7a78bd | -6.54592 | -43.08809 | 2026-09-24 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5a60e2a-c94a-30ba-8cf0-f4fa39307366 | -3.1537 | -54.60616 | 2026-09-24 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8baab378-2623-3d47-bef8-ff3f276ac603 | -6.65506 | -55.05522 | 2026-09-24 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3b0fae6d-a9f7-3c08-b9de-729881d3560c | -9.5332 | -46.49178 | 2026-09-24 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bd41a1c3-8df5-3bfb-a641-62383f48dea4 | -6.87999 | -43.74263 | 2026-09-24 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab5f3a5c-0630-31cd-8f51-0e1d9b98326a | -5.00189 | -45.55175 | 2026-09-24 04:08:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| dc3d2cea-febb-3532-b970-c44abee67db8 | -5.5739 | -42.30856 | 2026-09-24 04:08:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b0fed928-ef43-3fc7-9205-28d1179da992 | -6.77591 | -42.36771 | 2026-09-24 04:08:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| f5cd27ec-2107-3785-8f34-aef6609d40e8 | -8.73032 | -47.60682 | 2026-09-24 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9974a4d-3177-3e69-9f42-6c3c03036ce0 | -8.9047 | -45.90931 | 2026-09-24 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bcc45e34-2dd1-3e77-8e13-e3770014991b | -5.00705 | -44.63729 | 2026-09-24 04:08:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbf8636b-aae2-3c3b-a851-2e305831fe6e | -8.38769 | -46.29823 | 2026-09-24 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3ea84c93-6d8f-3895-889c-5ab8fc1a2a8c | -4.11142 | -51.08308 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d632a207-1687-36a4-a693-bcc85202eef8 | -5.84135 | -53.85569 | 2026-09-24 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf4f8f54-c091-3540-b2b1-c295cfb1b84a | -5.32956 | -48.98488 | 2026-09-24 04:08:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 209cfc16-c079-34fb-8538-cd5d81b713ce | -5.77243 | -45.09924 | 2026-09-24 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 2f4e30e4-2a69-3491-952c-38acb693e847 | -7.35223 | -42.05782 | 2026-09-24 04:08:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| af992d1d-01e9-3f3b-aacc-7ca080e03315 | -8.42386 | -45.84547 | 2026-09-24 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67a48527-9cbd-3bc1-a70d-82a428babe85 | -8.92134 | -43.875 | 2026-09-24 04:08:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f20788b0-a734-3d49-bcd1-e5c31fb5f73a | -5.98875 | -44.42392 | 2026-09-24 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02c19d8a-c9c0-3533-9670-1638571b10fc | -3.41906 | -54.00652 | 2026-09-24 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5b0afc7f-8d4d-3f7e-9628-988d74c6d733 | -8.4581 | -48.69413 | 2026-09-24 04:08:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 68f20035-6a98-3821-8947-70c58bf9e963 | -6.94124 | -42.09542 | 2026-09-24 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ba93f886-ff2a-3fd3-a9ce-683765c250e4 | -5.83684 | -52.01045 | 2026-09-24 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 053f2b45-616d-39af-ab17-5f0e856f40fd | -2.29927 | -47.88752 | 2026-09-24 04:08:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1252fa7c-6d51-336b-89c3-6c44d8e3de51 | -3.71789 | -49.04629 | 2026-09-24 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bf0a0f7b-ba18-306a-b654-9861807f9f75 | -6.64872 | -43.62655 | 2026-09-24 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe53a691-e22c-3ec8-a08e-7c5dec24075b | -6.00784 | -42.72925 | 2026-09-24 04:08:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 06e9bb8e-a899-3f23-966f-3bda67a9e80f | -3.06201 | -49.57253 | 2026-09-24 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5db6dc76-43c9-3e11-bc82-b8df8aed3fa0 | -8.30481 | -48.22506 | 2026-09-24 04:08:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88c1455e-09eb-3a2e-8575-4d481456ef5a | -8.26465 | -54.7692 | 2026-09-24 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| be7adf27-4961-3b89-a8a3-522c995c52e2 | -7.38768 | -44.81721 | 2026-09-24 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7433272-bca2-343a-a8f3-62c351bc9ef0 | -5.76571 | -45.30106 | 2026-09-24 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f6001c5-cc16-39e5-ac78-8ddab1c3ebd0 | -5.79375 | -49.18127 | 2026-09-24 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35719c72-2290-3a4a-a149-ecb2853b9450 | -5.84418 | -49.87996 | 2026-09-24 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c438f65-56fb-3d8a-8c16-997f821b6680 | -7.45367 | -47.17132 | 2026-09-24 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7130e2da-9c26-34ce-a0b3-582a5b8e4489 | -9.74394 | -41.87507 | 2026-09-24 04:08:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5be0fabd-4f6e-398c-ac27-49e06d9f0edb | -5.49946 | -49.02923 | 2026-09-24 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 330de023-cfba-3c14-b2a0-305c242a99e3 | -7.12822 | -41.72497 | 2026-09-24 04:08:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 85619d07-c2be-30c2-9da6-3352cbcfc07c | -9.12157 | -44.6955 | 2026-09-24 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 291552e4-8246-3671-b1a7-d8cd94b25043 | -2.64768 | -54.69339 | 2026-09-24 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 6a6a87d1-ba70-3ebe-98ff-3a935b8fd3d0 | -7.81118 | -38.86167 | 2026-09-24 04:08:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b04d1ed2-1f84-3b1f-a674-1bd63fd7d6d3 | -7.34573 | -39.31202 | 2026-09-24 04:08:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2a3a9d01-a8cb-311d-a3dc-4ff26887cd40 | -3.44551 | -50.09261 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2888e215-ce71-3f16-9e81-8703049bdf7e | -5.83165 | -43.06743 | 2026-09-24 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0f1a3026-569d-3ec9-b33b-f6c3cd374f15 | -2.64518 | -54.68633 | 2026-09-24 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| c658d6ba-dee7-3dd7-8327-b4593993edf5 | -7.39852 | -44.77304 | 2026-09-24 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 637573ae-b40c-3e22-8a9d-1ea12b27844f | -8.93201 | -45.95 | 2026-09-24 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42fb1ab0-479b-3552-893e-016f43b4f4ae | -7.14862 | -42.07543 | 2026-09-24 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a2ff8695-ffa9-35d4-a4fa-686fb8f13bb9 | -2.38688 | -48.52688 | 2026-09-24 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c3b79bf1-140d-32b8-b910-0c4d88cc821c | -4.75727 | -42.73669 | 2026-09-24 04:08:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| de6d944a-f612-303b-8122-4f9680e01186 | -6.51915 | -52.82267 | 2026-09-24 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4859b655-4c7e-3a9d-9d05-2989d113b52b | -5.38345 | -46.57296 | 2026-09-24 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 493c5ee8-4000-36c1-811c-286bb5e76567 | -7.40272 | -44.7696 | 2026-09-24 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 59c3aebd-ea7c-3231-a864-55d2161ba6f6 | -3.44239 | -50.07896 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7a2c51ae-88fc-311b-97ca-041a8da14072 | -6.71428 | -46.63372 | 2026-09-24 04:08:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03e30099-5cdc-334e-82c3-049398f35ce9 | -8.12704 | -54.82074 | 2026-09-24 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c3f90f97-8d14-3797-85d4-226555d5782d | -2.82609 | -46.70801 | 2026-09-24 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 62b2c7a3-d922-31c7-bd3e-a3abc5fe801a | -6.52751 | -51.50564 | 2026-09-24 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6178cfbf-f402-3f62-b8f0-15ed1b466510 | -5.75905 | -44.04951 | 2026-09-24 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b73fbc47-773a-3212-9c04-3c2c7ed48b65 | -1.024 | -53.7389 | 2026-09-24 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9740c7fe-eb57-32ce-a2a7-acbaa6738399 | -6.72258 | -44.15138 | 2026-09-24 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| b2e80b68-1c04-32a4-93e7-4d28bccc5c19 | -7.42955 | -49.86224 | 2026-09-24 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e2486f5e-5fc6-315a-9fe6-ae734c328679 | -3.26543 | -49.14661 | 2026-09-24 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1318ef7f-44c2-32e8-8907-5eae624ff2ef | -7.99135 | -38.33172 | 2026-09-24 04:08:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d7256621-d41e-3f12-a56a-ce917866a9bf | -7.19307 | -47.45524 | 2026-09-24 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 973c4b55-d8ba-343b-95d8-86ff66e30cd0 | -5.11328 | -43.7451 | 2026-09-24 04:08:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd7bd1be-706d-328d-ad3a-32d761d19f13 | -7.98316 | -44.97081 | 2026-09-24 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 905b98aa-2771-30d5-a41f-d817abdb8baa | -5.57445 | -42.30507 | 2026-09-24 04:08:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |


[Clique aqui para ver as próximas entradas](README33.md)
