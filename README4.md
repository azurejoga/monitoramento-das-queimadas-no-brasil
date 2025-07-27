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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56e891f9-bf09-3853-9895-98e18927728a | -6.42132 | -41.15059 | 2025-07-27 03:45:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b88db788-3eef-3261-94f6-c1da70a87e34 | -8.17118 | -43.19151 | 2025-07-27 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 92264aba-9f6e-383c-ab9a-df0180162c14 | -2.89968 | -48.24972 | 2025-07-27 03:45:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c261c43-2744-38d9-aadd-d30f63ee232b | -6.86889 | -43.68873 | 2025-07-27 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d0440fec-079b-3b4f-9899-babff99d7ab3 | -6.99047 | -45.62106 | 2025-07-27 03:45:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ccacfec1-dd02-3058-9cb5-9abfaad3b302 | -5.6046 | -45.08285 | 2025-07-27 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9d724dcb-2442-3b30-8980-f5c5c0498f64 | -2.90689 | -48.25086 | 2025-07-27 03:45:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a42705a8-a101-3f8b-bf9f-4cc1e1bf4723 | -4.61603 | -43.32083 | 2025-07-27 03:45:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9168b57-3086-310f-a492-fc9b65639500 | -8.29841 | -45.00894 | 2025-07-27 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1dedf83e-6c33-3099-9077-102120396f20 | -8.3026 | -45.00957 | 2025-07-27 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e46475dd-833e-33f8-8b0c-6175d58e3005 | -8.01276 | -48.1771 | 2025-07-27 03:45:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e76bae01-1a79-367b-adcd-71de6c0ad2d5 | -9.66213 | -40.59353 | 2025-07-27 03:45:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 6a7d82f7-9713-32a6-a435-bc112152b973 | -4.10234 | -48.21171 | 2025-07-27 03:45:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 801a7319-2335-3465-83f1-7eef9e866dbc | -6.4292 | -41.15644 | 2025-07-27 03:45:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 78f6a752-cd19-3062-aab5-f81546a1e000 | -4.10973 | -47.9313 | 2025-07-27 03:45:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ceeec64f-3708-317e-8ea1-0f1109424974 | -7.17185 | -38.43814 | 2025-07-27 03:45:00 | NPP-375D | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 74ef2a5c-dc71-3134-8094-40918c66e5cc | -5.74257 | -43.9513 | 2025-07-27 03:45:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 126e1a8d-e39e-386d-8544-b89da89f0017 | -7.917 | -43.10021 | 2025-07-27 03:45:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6bc167a1-5a80-3596-b419-efd3e3962977 | -8.1728 | -43.20432 | 2025-07-27 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 77d495e5-cf9a-3080-8311-cc09fcd0611f | -7.09542 | -44.0511 | 2025-07-27 03:45:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce3a5611-8102-31f8-8578-b100c0c5387d | -6.89672 | -43.12556 | 2025-07-27 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d8e466d-31e9-3df1-9387-3d8c3611149a | -9.03542 | -45.39751 | 2025-07-27 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c513cfa3-afd8-393c-adc1-c12ddda49786 | -9.57584 | -43.86988 | 2025-07-27 03:45:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7b4ede0f-7696-3080-abbe-9d7db6197111 | -6.89129 | -44.81011 | 2025-07-27 03:45:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24604454-3adb-371c-9955-198f69d955c4 | -6.70449 | -43.06886 | 2025-07-27 03:45:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34269b5c-a29a-30ba-9988-1e8e61c8de48 | -5.78593 | -43.60982 | 2025-07-27 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c3c08f26-aa70-3596-8d52-3a55d4c82258 | -6.70128 | -43.06995 | 2025-07-27 03:45:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0ac21b36-e231-30e4-beb0-39f8f6182d0e | -5.60358 | -45.08231 | 2025-07-27 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f8bb3f8d-102f-3ae2-b718-63d541674a70 | -6.86721 | -43.52068 | 2025-07-27 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a5ab3bdb-4d84-314f-bcb7-1bb072471aff | -8.17184 | -43.20959 | 2025-07-27 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a5bcbffd-ae50-3c25-9282-d9f42c2d6dd6 | -7.10421 | -44.91652 | 2025-07-27 03:45:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c669418-bd13-399a-8b4b-39907bbf1ecd | -5.74029 | -43.96439 | 2025-07-27 03:45:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f7ea9a1-badb-3a81-84f7-0075e71bff5a | -5.18631 | -44.95825 | 2025-07-27 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94081e76-9cf3-394e-9d16-763e32fd1948 | -5.18551 | -44.95599 | 2025-07-27 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| df77c974-325c-377a-8a25-11519d13de04 | -6.63891 | -43.04001 | 2025-07-27 03:45:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e658ccfd-ed0f-3776-afb8-7b38c2356e0a | -6.55509 | -41.49868 | 2025-07-27 03:45:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3b3f6d9b-5c49-3b88-9761-db0c9ddf8279 | -6.00936 | -44.04997 | 2025-07-27 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93034ec4-9c78-3386-9e22-836379ae78ac | -6.86835 | -43.69178 | 2025-07-27 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b0dcd9c1-0636-3789-beb6-603504e2ad89 | -3.13686 | -47.01623 | 2025-07-27 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9994e52-8e8a-3a87-9456-97a9c32c7d09 | -4.06389 | -42.5387 | 2025-07-27 03:45:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d67d83c1-e1a7-3914-8968-2aada7924c02 | -4.10369 | -48.20419 | 2025-07-27 03:45:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30cd6663-3343-3f55-a0d1-043e67889b34 | -8.01049 | -48.17017 | 2025-07-27 03:45:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c09fa692-5ecb-3c6a-ba58-1903b70b3eb3 | -6.52933 | -43.34668 | 2025-07-27 03:45:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a736fc14-33af-3f68-91a6-c52f587b38a6 | -3.13269 | -47.01564 | 2025-07-27 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 631e5eac-4317-3fe6-abc1-43346224738e | -7.29199 | -43.08757 | 2025-07-27 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 23f02360-95c3-3812-ad34-1e63ef3ecb0b | -5.78182 | -43.60298 | 2025-07-27 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55f4151b-6c81-34ae-b7a5-d3147b84c799 | -6.52839 | -43.34712 | 2025-07-27 03:45:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d035f74d-3d67-3f45-9339-7fdc18c0b67d | -3.92186 | -42.41167 | 2025-07-27 03:45:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a07a602b-45f4-3440-a1e9-feb42563f04b | -9.12689 | -45.87357 | 2025-07-27 03:45:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2332df80-ecde-33cf-af14-046f9e868c82 | -5.74313 | -43.94807 | 2025-07-27 03:45:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65d760e7-020c-3549-b531-adeb75cec331 | -8.28759 | -45.00683 | 2025-07-27 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5a64dcba-217f-39b3-b476-8d8a9b31ea2a | -5.67898 | -42.79971 | 2025-07-27 03:45:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2c5dcacb-5785-3c74-9b1b-3fa9cbde1d01 | -5.67598 | -42.80068 | 2025-07-27 03:45:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 583e4dc5-2251-3c1a-a9eb-10400e7b49bd | -6.63402 | -43.03913 | 2025-07-27 03:45:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bfe3a43-27fb-344a-8797-e43ab2f06194 | -6.8667 | -43.52357 | 2025-07-27 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cdf7a71b-51f1-332e-afbb-8205af04c745 | -4.13209 | -47.64907 | 2025-07-27 03:45:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e2f3db2f-1c2f-3007-b484-152b14e6593f | -7.28808 | -43.08134 | 2025-07-27 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9a4a164c-e8bc-3134-b2c3-de3558a5fdb9 | -4.11046 | -47.93362 | 2025-07-27 03:45:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 283746fb-4ab4-3156-8c71-47aab31edfdf | -4.06481 | -42.53318 | 2025-07-27 03:45:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5adb2523-9034-3a40-b5aa-b6459c63665e | -7.53122 | -42.41858 | 2025-07-27 03:45:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 827de172-408c-3808-94a6-0aaacd143811 | -9.13322 | -45.87104 | 2025-07-27 03:45:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a232208-bd2a-310c-aba3-9b7969e09a62 | -8.30761 | -42.21741 | 2025-07-27 03:45:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ca01e1c4-82d0-3cfc-8821-0ec70f4f3dd7 | -4.07376 | -42.54037 | 2025-07-27 03:45:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| bb571f2a-2014-373d-8bd4-326dcb92fb50 | -5.78078 | -43.60889 | 2025-07-27 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 27941a8b-c297-3765-a119-c41c990169fe | -4.10344 | -47.93281 | 2025-07-27 03:45:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 79a50f61-c30a-3b70-91f5-e96b1aa89e67 | -8.29363 | -45.00447 | 2025-07-27 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37665e1c-ae9b-32e3-8764-b710a55bcc6f | -8.00722 | -48.17004 | 2025-07-27 03:45:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b78c665-1759-3671-a12d-be7c0fe4140b | -9.03471 | -45.40134 | 2025-07-27 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88868991-c282-3f15-af68-047ba04ad61b | -7.10494 | -44.91242 | 2025-07-27 03:45:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3524f677-de6e-36ec-8e13-9fde96b31d78 | -8.17323 | -43.20827 | 2025-07-27 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 860327ab-4e49-3fbf-8376-6835d9e80873 | -6.22493 | -44.52495 | 2025-07-27 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ccd11b9-293a-3461-849c-a6f7ec057f01 | -6.99098 | -45.61941 | 2025-07-27 03:45:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f511d6e6-0759-353f-9ebb-f251a9e4c352 | -4.61656 | -43.31778 | 2025-07-27 03:45:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de9e54e8-8742-38c6-ac3a-2fb86b3abe8d | -8.30382 | -45.00998 | 2025-07-27 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 960924b4-e77b-3c4f-8d28-027118870be0 | -9.66608 | -40.59423 | 2025-07-27 03:45:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 0565ecef-6dab-352b-9e82-1631bc602e40 | -6.00876 | -44.05335 | 2025-07-27 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5903f418-5d9e-3754-825c-5c042f13028b | -4.09895 | -48.20684 | 2025-07-27 03:45:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b991db2-105f-3192-b6ae-9d81fb5088ae | -5.7813 | -43.60594 | 2025-07-27 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 02254695-fb06-33e0-ab8c-3834826160c6 | -6.89703 | -43.11265 | 2025-07-27 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67090dff-da2c-3525-ba93-222862a1cabb | -9.5768 | -43.87261 | 2025-07-27 03:45:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4ac72886-53b1-3ad6-8a5b-5a1fb1a5f216 | -6.88818 | -43.10553 | 2025-07-27 03:45:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49732efc-1384-33f8-be32-6a65b81fed36 | -6.86378 | -43.68793 | 2025-07-27 03:45:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0b4877c0-f79f-3161-bb0c-7bfec98bff0e | -8.29178 | -45.00744 | 2025-07-27 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e72dd4c-5fc8-3e06-b36f-5f5f40a04cf0 | -4.06975 | -42.534 | 2025-07-27 03:45:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a25c615e-bf36-33b3-b668-21bf58587320 | -3.12351 | -47.01384 | 2025-07-27 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbb3ef2d-cfd9-3818-8b54-6fabb9acb0c7 | -5.67695 | -42.79513 | 2025-07-27 03:45:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| b8534226-2e40-3487-8533-f5fd0d1acde5 | -6.99921 | -42.34685 | 2025-07-27 03:45:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c58f1d85-6460-36b6-ab61-3141b294b305 | -8.17507 | -43.19771 | 2025-07-27 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 414da8a1-21c7-357b-aed7-9dd05e5d460b | -8.30986 | -45.00762 | 2025-07-27 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 245e712f-3b33-3e4b-a27c-81e636564915 | -5.78645 | -43.60685 | 2025-07-27 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e3aa1448-36ec-302f-a30e-a780c764ab9f | -4.03615 | -42.5227 | 2025-07-27 03:45:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 4a81564f-d9df-33e4-88ef-a82efee1dd95 | -6.24453 | -44.05923 | 2025-07-27 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b22dcf2-7d72-3507-944b-3216e560f06b | -6.59821 | -41.78308 | 2025-07-27 03:45:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5110b8d7-87bd-31b8-8c2f-ed9e18520ad0 | -4.7582 | -38.47919 | 2025-07-27 03:45:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bac8eb53-b678-3b69-900a-e8bde521abd6 | -9.56103 | -40.64852 | 2025-07-27 03:45:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0d4486f1-ff3e-3c5a-a3ff-74f4e49753a3 | -8.17026 | -43.1968 | 2025-07-27 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 96dab6a5-8ea3-31bd-8530-9d4c56e00b86 | -4.1016 | -47.93653 | 2025-07-27 03:45:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 55d1aad8-77ba-3073-b9de-0c9cf762f15f | -4.06883 | -42.53951 | 2025-07-27 03:45:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| eaee1b3a-145c-3d9c-a809-eb086adac9eb | -8.00933 | -48.17612 | 2025-07-27 03:45:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f0703d4-0234-3193-b0d2-ce78089f958b | -8.17415 | -43.20298 | 2025-07-27 03:45:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |


[Clique aqui para ver as próximas entradas](README5.md)
