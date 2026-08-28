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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 368c4a74-23e0-31f7-bb5f-b6764aa1c288 | -12.31182 | -50.56566 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 89fb6fbf-55bc-35f1-bec1-781193001609 | -10.46447 | -46.18573 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 63cc92d1-0e5e-3245-bc4a-03c4a4f44040 | -11.83149 | -47.22076 | 2026-08-28 16:07:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| eb8d7246-f778-374e-858c-42b9730f98a9 | -12.31971 | -50.57194 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| e7e43aa0-3eb7-3f64-af28-ea2197f5e585 | -9.62963 | -45.735 | 2026-08-28 16:07:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6856a2b0-115c-348d-9088-32a3cde569c0 | -12.03427 | -47.18214 | 2026-08-28 16:07:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1c1dccad-e5f4-3f70-b76b-9d7cb30f664c | -1.19541 | -50.05063 | 2026-08-28 16:07:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cf07aa2e-2bd5-3e4b-bb30-a9b6590dbd72 | -1.57957 | -47.74513 | 2026-08-28 16:07:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 9ffbb8e2-b008-3d37-ad6d-0ba78b166c95 | -10.91085 | -46.62296 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7bce8c7d-c410-3062-9114-049e8b0bba89 | -10.02339 | -45.63119 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 45258b77-f83c-3511-9a2b-4cd15328acd1 | -12.06077 | -47.158 | 2026-08-28 16:07:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 3882447b-e59e-3433-8518-ce7096d5d8bb | -11.84993 | -47.2207 | 2026-08-28 16:07:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a1c56e83-175a-30e7-9d90-5ddf5a592da2 | -10.01296 | -46.4076 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 52051285-6c36-35f3-9694-0cf6dafa5e2b | -2.99514 | -48.95343 | 2026-08-28 16:07:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 84986bbe-ea64-3a9d-81c2-89a1bb6ff4a6 | -11.07141 | -47.1204 | 2026-08-28 16:07:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9b8d39ef-1bdc-3036-9e4c-63c147b37e41 | -10.32755 | -46.75256 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ebfecca3-f91a-38fb-a933-fbc21d578743 | -10.92267 | -46.62188 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 763722b2-9d32-3260-b92a-a42279c0fc74 | -11.76915 | -47.64882 | 2026-08-28 16:07:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b63d873b-bae4-3c51-829d-13551a3cd6f2 | -2.01282 | -48.34215 | 2026-08-28 16:07:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 323fc511-b0e4-31e1-b51e-626b08108d82 | -10.63781 | -45.22216 | 2026-08-28 16:07:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f7d62905-39e5-31e3-9b03-33a3c68bd7bc | -11.82103 | -47.22419 | 2026-08-28 16:07:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| e9fcb4e4-03b7-3b99-936e-9131e9f77c04 | -9.88684 | -46.34105 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bcc9d8e0-cfc9-339b-9acf-2a75ec95d13e | -12.0805 | -47.17646 | 2026-08-28 16:07:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| eb221133-1918-3392-8892-03332303bfdb | -10.9168 | -46.6259 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| be0a95f4-3c7b-3416-bf09-688afd4ed919 | -1.73999 | -44.84534 | 2026-08-28 16:07:00 | NOAA-20 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 418bb77a-3189-3cd1-8dbc-da5714932cc7 | -10.47458 | -46.18058 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 56d59ff0-295e-3932-b09e-d14ad55e8410 | -9.66784 | -45.12986 | 2026-08-28 16:07:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5b67b198-fba2-3a8f-98b8-2d215174546d | -3.08215 | -43.6372 | 2026-08-28 16:07:00 | NOAA-20 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 22de3b35-0ba7-3387-a373-df85908ac210 | -11.0823 | -47.11496 | 2026-08-28 16:07:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1272bfe2-d205-3fb2-b116-04370734212d | -10.91172 | -46.62347 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7ace39e9-ae10-3720-bb8c-abc05464eb72 | -3.22447 | -48.60947 | 2026-08-28 16:07:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2f42c12b-ba04-31b9-96b9-fb9f7daf6b7e | -4.84897 | -45.39437 | 2026-08-28 16:07:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| e7bfb203-d874-3902-aa14-6abf5b20842e | -10.53933 | -46.26483 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 37bb5051-ec16-30a4-834d-fd8e9d4ebc84 | -3.9318 | -44.90315 | 2026-08-28 16:07:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 1fba6042-3d1d-3e69-a971-b56f77d14511 | -10.54475 | -46.10425 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7f39d64f-84a4-3213-875c-58e3b83878d7 | -12.259 | -50.54295 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| e5fd4226-343c-3a83-85fe-0fcedd00afaa | -1.08213 | -47.93667 | 2026-08-28 16:07:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a0054d6-9b31-3226-a342-11cd78448546 | -11.84415 | -47.22143 | 2026-08-28 16:07:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 064ab261-6b58-383f-b512-d018512f790d | -10.34617 | -50.38537 | 2026-08-28 16:07:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| aed7e0f2-35bc-3f09-96e9-ec1984eac949 | -10.09239 | -46.97824 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d2bc9ba3-6c76-38b1-bba5-55161fc0a48e | -5.57734 | -47.45417 | 2026-08-28 16:07:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8213317d-09d3-3c9f-a492-caec65c05e43 | -10.53751 | -46.26435 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d49426a5-7ef8-3ed4-bdb9-193bb5d40847 | -2.73002 | -47.05182 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 97c5346a-f5a3-3fae-a350-2e22dbea6fd0 | 2.51541 | -50.85019 | 2026-08-28 16:09:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0b7efeec-7f61-3f31-9fc1-a6262791a217 | 2.52136 | -50.85113 | 2026-08-28 16:09:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 55f9c486-9ec3-3afb-8f56-90b882268d26 | -9.0278 | -69.569 | 2026-08-28 16:10:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 58.6 |
| aa7d179d-69c2-3cde-bcda-60d8519a2387 | -9.9706 | -53.9624 | 2026-08-28 16:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 208169e2-3a06-3a1f-a862-34cf287f0a4b | -8.6694 | -49.5369 | 2026-08-28 16:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 10e6b8f5-dc5f-353b-8941-fa58c2b8a698 | -10.7839 | -50.6346 | 2026-08-28 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 2924f13c-dfb2-385d-96ca-1f5d346c82c9 | -10.7791 | -53.9752 | 2026-08-28 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| f40b0d7d-9d63-31c0-8a43-1127231853a9 | -8.5971 | -54.7553 | 2026-08-28 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 27feab96-3f9f-3da1-9dd1-fd982796d6bf | -6.9872 | -59.2582 | 2026-08-28 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| bcae8f7c-884a-38ac-8297-a77896166552 | -10.7649 | -50.6366 | 2026-08-28 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| de88b990-71ee-3428-9320-f6cb1e3c00cf | -14.2302 | -45.2472 | 2026-08-28 16:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| ba060f07-5383-3658-a81e-7cb6daf09532 | -6.5322 | -55.2577 | 2026-08-28 16:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| aa615545-dcd2-3bcb-a864-372d0f21e08d | -8.3902 | -62.7152 | 2026-08-28 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 0b8179d2-396d-3737-94ff-6be5e70f320a | -6.7105 | -45.1917 | 2026-08-28 16:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 333355c7-2126-3752-84ab-b784f7991cd0 | -14.4444 | -53.3806 | 2026-08-28 16:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 144.2 |
| e34e3e08-2f66-3336-b524-d8318af00581 | -11.1452 | -45.5694 | 2026-08-28 16:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 1e1b51ec-36bd-3ecc-ae29-7bcb3aecf8d2 | -10.8422 | -50.5219 | 2026-08-28 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| e1f12c4b-0361-3520-9234-0105ce7ed83e | -10.7603 | -53.9769 | 2026-08-28 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| a36f6d3d-728b-31e3-86bd-601d2585f2fb | -5.9995 | -57.8444 | 2026-08-28 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 21e79c55-c10c-3693-b973-81fcde753881 | -15.2478 | -53.8666 | 2026-08-28 16:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 44daf21f-52b6-34a1-a7ab-538d85ad2bb5 | -10.9364 | -50.5545 | 2026-08-28 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 0e413405-7e8b-37b6-8ca6-ca8a445709e7 | -7.0057 | -59.2575 | 2026-08-28 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| b30301ec-161c-3580-aab0-8c36148eb1cd | -6.6357 | -45.1752 | 2026-08-28 16:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 5974370c-cb1a-3fe4-a7cc-37a255ecd186 | -7.263 | -49.864 | 2026-08-28 16:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| f6faf2be-146c-36d6-82ab-79bb75707abc | -8.3716 | -62.7349 | 2026-08-28 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 0addc91d-9936-36ce-b5c9-459b15a79db6 | -6.2676 | -53.3768 | 2026-08-28 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 9ee3673f-f841-32d4-b689-f22712d55cd7 | -6.018 | -57.8242 | 2026-08-28 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| d5d6b660-f48f-3254-86f3-1520e0fbefaf | -11.697 | -54.5876 | 2026-08-28 16:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 68034328-3e14-3597-ba9b-290af595ed16 | -11.6411 | -46.7265 | 2026-08-28 16:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 62852d37-3650-3d3b-93ad-582eed542dca | -10.7598 | -54.0179 | 2026-08-28 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 41836427-715a-34fa-a505-be61b7780787 | -6.7451 | -59.6533 | 2026-08-28 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| a3bd5667-9271-38dc-a761-5826099019d1 | -10.8996 | -46.6216 | 2026-08-28 16:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 3d90ae4b-7e50-3593-b4e2-7c4c39d81496 | -6.641 | -58.4987 | 2026-08-28 16:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 4727fabc-b5b6-3db6-92de-a5f2f0bc6ba7 | -8.3718 | -62.697 | 2026-08-28 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.6 |
| d7ae9ead-ec22-3e85-9637-80f9122ccf2d | -3.2901 | -61.5747 | 2026-08-28 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| f58d5e18-e49d-39fd-88d9-3654d066f99f | -10.76 | -53.9974 | 2026-08-28 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| b5d4c01a-93e0-3fc3-a845-7a44517b6346 | -10.7789 | -53.9958 | 2026-08-28 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| a10259bf-f484-36cb-9b39-580c2c9f0405 | -6.137 | -53.5259 | 2026-08-28 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 1ac34d0e-6c62-38c3-a00d-f8b40e56efd1 | -11.1922 | -51.2284 | 2026-08-28 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| f076bc6d-2988-3666-9c44-8fee1a5bbed8 | -10.5601 | -50.4022 | 2026-08-28 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 2cd40ec4-8ff6-3868-9a87-31af8563f4a8 | -9.0462 | -69.587 | 2026-08-28 16:10:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 46.8 |
| b492e098-f2ae-3534-9479-390d9f9938f6 | -6.6359 | -45.1525 | 2026-08-28 16:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 3dda71a3-1d6d-3eff-b3df-52bc59f8b742 | -9.89 | -45.87 | 2026-08-28 16:15:00 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 91a54afd-8cda-34bc-9a21-b00deaa1b822 | -12.33 | -50.58 | 2026-08-28 16:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 65ad743f-2554-34da-8db2-54ee39878528 | -8.07 | -45.83 | 2026-08-28 16:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b94e9e8-af2d-3a3a-baf8-7306cb5221ee | -10.8028 | -50.6326 | 2026-08-28 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| b613de92-0f62-31a8-8ccb-e3b091193328 | -8.5971 | -54.7553 | 2026-08-28 16:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 031451db-28d1-31f0-a23b-0b6e75e36893 | -12.3999 | -48.2073 | 2026-08-28 16:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 98fa5cdc-5cc2-39ba-8cf0-056708e3233e | -10.7787 | -54.0163 | 2026-08-28 16:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| d9b754b3-7874-3e18-8abd-1a5d8e53f352 | -6.695 | -58.7291 | 2026-08-28 16:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 151f77aa-da68-3c22-b54a-dd51b49acf54 | -5.9996 | -57.8249 | 2026-08-28 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| b3446322-f4a5-3b2c-905f-7ae63a90f886 | -12.2281 | -50.5578 | 2026-08-28 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 5bec61aa-f782-33f7-ac0c-1f630daa8348 | -10.7649 | -50.6366 | 2026-08-28 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| c181a12b-19e1-3ff9-92e3-287395a428f7 | -6.1473 | -57.78 | 2026-08-28 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| cf48ab12-2057-3140-b6f7-2e939f5dbc40 | -11.1452 | -45.5694 | 2026-08-28 16:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 215.4 |
| 07e552b0-ae31-3c66-abe0-07140b0c9ad5 | -6.1284 | -57.8588 | 2026-08-28 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 00ddef0a-3d76-3ba2-a432-4adea3b84e4e | 1.51 | -55.9638 | 2026-08-28 16:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |


[Clique aqui para ver as próximas entradas](README101.md)
