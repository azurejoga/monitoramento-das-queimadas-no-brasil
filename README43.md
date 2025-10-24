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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d9a9164-095a-3eaf-a7ed-00b3cc8f90ff | -6.31175 | -41.86232 | 2025-10-24 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5d7640a3-daf4-34e1-9ff7-02a4dcf26159 | -4.24834 | -48.12867 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92d27391-46c8-32a7-99f7-e027f77e9954 | -8.66276 | -44.78027 | 2025-10-24 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b84ec75-64b9-370d-8690-bdb6890930fc | -5.65519 | -45.95547 | 2025-10-24 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5e913af5-a67c-30b4-9a36-40fdf28fa403 | -3.16063 | -49.16534 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b16f5e4-91af-369b-bc62-a38a0a0b46e7 | -8.11943 | -47.39059 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b2a44ef-c671-3c09-b133-c7c65883284f | -5.22853 | -50.82175 | 2025-10-24 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fc93ca7-14aa-3e93-a26c-b8bed6f628fd | -9.47313 | -47.7654 | 2025-10-24 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85f11407-8297-3f6e-a72c-766b1d282cbc | -8.61277 | -44.81343 | 2025-10-24 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4e7c827a-a6d3-333e-ac82-1b1d474fbcfb | -6.93196 | -45.16304 | 2025-10-24 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9b23c3e-0d31-39ea-9c33-515ca04859d3 | -8.64505 | -44.78892 | 2025-10-24 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a047c5c1-503e-3f9d-8b88-e3394ab84af1 | -6.44484 | -43.81865 | 2025-10-24 04:38:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 43912dbc-0a55-3997-88f7-97219128722e | -4.30028 | -43.22365 | 2025-10-24 04:38:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f6c7c4b-75e9-3ae5-9e79-ce477d69df73 | -3.02482 | -49.48576 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39438a92-4b7d-3cd2-ab2f-d8c1395d125c | -9.3261 | -48.48211 | 2025-10-24 04:38:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 949f100a-01fc-316c-9ca6-df4bd35284ca | -9.97527 | -47.73727 | 2025-10-24 04:38:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33b17351-6786-35df-a8ac-88f83e39db45 | -4.21045 | -48.60739 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 58a0990b-5049-36b1-a6ed-749c4af6cf01 | -2.86008 | -50.74505 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bbb3dbf-880b-3db7-b6ce-d8d96179789e | -5.75663 | -46.68389 | 2025-10-24 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e98cc55c-3ecd-3ff4-90f8-7d46f5220c10 | -4.90592 | -43.21842 | 2025-10-24 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77d8ddf8-8a67-39a7-80e7-d8f1b7bb9834 | -8.11677 | -47.04852 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8199caa-bf16-3bc8-a641-1d5f96253dfb | -3.01649 | -49.4522 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd74e422-7118-31a8-bcce-50dc18f1ccce | -6.90505 | -51.17247 | 2025-10-24 04:38:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6635cc92-91fe-322d-b23d-cf51a68382b7 | -3.84059 | -49.93479 | 2025-10-24 04:38:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1957813d-ffeb-3ce3-a735-fc453b6d34fc | -9.60789 | -46.91334 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ee44c004-0d51-39af-bc66-3462d368c28c | -3.13484 | -49.52126 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 7dacc012-75b5-3daa-b1f0-fc830648a703 | -5.3774 | -50.90103 | 2025-10-24 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ff04f9cb-6ca8-3aca-9192-38261271f5d2 | -3.14161 | -50.16327 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6f473be6-c328-3b3e-87fe-99f6908adb30 | -2.80018 | -51.35119 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f53bc7b-722d-38f2-8e23-f0748425cc69 | -8.32684 | -46.78301 | 2025-10-24 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e326756-1e33-3dea-abdd-806889f8fdc1 | -2.81474 | -49.13873 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 51d2ae91-9204-3211-abea-d4b9f4529ff7 | -8.35065 | -46.17454 | 2025-10-24 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd6c527d-be22-372a-9c7a-87dd6580fe64 | -3.7858 | -43.90462 | 2025-10-24 04:38:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5d544d3-7cfc-3f01-8e9c-c7a03f6bd3f7 | -9.5965 | -46.91578 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6fa78995-9552-3001-8fc7-c0c13d213d99 | -10.00987 | -47.10041 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d569d31-520c-3eaf-96b8-00fcd2e37b3b | -8.46894 | -45.56167 | 2025-10-24 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 632fe98f-bcd0-300b-8ad3-fcff70fb269f | -8.61679 | -44.81398 | 2025-10-24 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ddf0b3fe-5727-350f-aa9d-0de398bde4e9 | -6.30418 | -41.88171 | 2025-10-24 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ae46f1db-2b0e-36f3-89eb-699c15aa506b | -6.13014 | -41.7295 | 2025-10-24 04:38:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8e136bd9-61d0-36ea-92a4-5b0553a137e4 | -6.30892 | -41.88239 | 2025-10-24 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 37a7f4b8-ad0e-3862-b2b4-b6a5953c6905 | -4.28714 | -40.70351 | 2025-10-24 04:38:00 | NOAA-20 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 24be392d-6430-3551-8d4d-7b5c0ace85a8 | -4.19751 | -48.36531 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68ffe147-fab2-3574-9707-ff70555e7809 | -6.10224 | -48.19852 | 2025-10-24 04:38:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76eda88e-1062-30f7-8c20-6df459776956 | -3.51422 | -45.83641 | 2025-10-24 04:38:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11f1d1ae-bbaf-3691-adc5-603026e026f6 | -5.86736 | -51.12592 | 2025-10-24 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a85207c2-c35f-31cd-9d7f-59e1cc65c945 | -3.48059 | -50.08329 | 2025-10-24 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 690a3fb0-c05a-3b97-96b7-a24cfec52ac2 | -9.19991 | -44.54075 | 2025-10-24 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5699e588-08f7-3571-a625-2a0526ed1d05 | -5.54905 | -41.35224 | 2025-10-24 04:38:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9b4c623e-f22f-39c3-8b71-8e863d4f55a0 | -8.32366 | -46.25405 | 2025-10-24 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 34317b3b-3540-30b5-87bf-43522345dc6c | -7.47382 | -48.39634 | 2025-10-24 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9efa5702-a8fb-3924-8a51-00cc28078f15 | -10.02308 | -47.08549 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d6f1ee33-38ee-3621-80f4-cc3ebe35522b | -3.85478 | -52.1032 | 2025-10-24 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e95ed1a-02bc-399c-8e14-1b70d2811ce8 | -4.27695 | -48.33528 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| caada51b-f4d0-3b0a-b2e3-33e6a409940d | -7.77768 | -45.40368 | 2025-10-24 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd5e2710-ab21-3375-8264-97ef9534ea3c | -10.5199 | -44.16666 | 2025-10-24 04:38:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cb461ac-9531-35a3-81a5-6cfbdbfe29ea | -3.94265 | -48.08448 | 2025-10-24 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c28763b-0573-3eac-aaa0-384383277027 | -4.8521 | -48.56728 | 2025-10-24 04:38:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f615147c-6fb0-30db-a577-ae10481499fc | -9.36879 | -50.81373 | 2025-10-24 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3658340a-60f2-382e-a2d1-c25925407681 | -7.138 | -45.04492 | 2025-10-24 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f428891a-307c-3d4b-a930-923eaf9744bb | -2.80369 | -49.14408 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 296baac0-3119-396f-91ce-b4a7a80ed911 | -5.77347 | -53.45961 | 2025-10-24 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8673b37-4687-33cb-8815-9205669cf82c | -11.04858 | -45.40533 | 2025-10-24 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b4331013-b80c-3969-beea-378218dceafd | -3.02426 | -49.48926 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f85516a-1bb8-34a3-bd4a-0b6b49e590f2 | -4.70113 | -46.44318 | 2025-10-24 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fd4e9ee-b366-3b13-832f-c9d4ae9bc89e | -9.09264 | -46.53352 | 2025-10-24 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 389c2bb9-e2c6-321d-82f2-421b5d5ed3a6 | -6.81334 | -45.46727 | 2025-10-24 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0154fe6-a28b-3a60-a6b1-ea8e7116e7c0 | -9.23747 | -45.58836 | 2025-10-24 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22a766fd-20cd-33c7-890c-f2f95c3f4ee3 | -7.55594 | -47.36636 | 2025-10-24 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e6c8ca96-46f8-3aea-8fbb-b443bf3c4599 | -3.5301 | -50.32391 | 2025-10-24 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4aae34d4-5f3e-3542-acdc-8953a5d68203 | -2.07211 | -54.22544 | 2025-10-24 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f61fb1f-1a89-3b76-b66a-0f4f078e3448 | -9.6061 | -46.9099 | 2025-10-24 04:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| b6336986-733b-34fc-bc75-4a4726d1c7de | -12.8235 | -50.94751 | 2025-10-24 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a33f0b41-366a-3bcd-8afc-34b41695194f | -13.19838 | -47.76215 | 2025-10-24 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 394f4822-5524-3071-90be-6eee87b29ab5 | -14.42929 | -50.95357 | 2025-10-24 04:40:00 | NOAA-20 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 81c73094-ea6e-3b2b-bfd1-20f8a6d3e881 | -12.7301 | -46.94917 | 2025-10-24 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff5e0229-d3c6-387d-9cbe-dec3a4903c44 | -12.03226 | -46.93213 | 2025-10-24 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54e0c1a8-27da-3f8b-a3ee-f45cc0088e5e | -11.66269 | -48.46698 | 2025-10-24 04:40:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| beeaf4cc-2638-3541-b55d-181eff0ccb50 | -17.31323 | -43.60172 | 2025-10-24 04:40:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e4c5a87b-b8d3-3468-bdc5-2630b8623af3 | -17.3722 | -52.02009 | 2025-10-24 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2612ce0-85bf-3ceb-a177-5d3de6041d06 | -11.48267 | -54.01134 | 2025-10-24 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35ac1215-c30b-3b1d-8277-77eb2761ccab | -11.36065 | -55.12717 | 2025-10-24 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a15ea684-13bc-3dae-8e6d-3c1f696aa2a7 | -15.60476 | -48.05251 | 2025-10-24 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e6dc2be-ee5e-3d75-bb5d-55a9ea505178 | -12.95568 | -48.49883 | 2025-10-24 04:40:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc7ba6e9-1560-3486-a055-030c35b832bb | -14.38308 | -51.52504 | 2025-10-24 04:40:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f17a457b-0c19-3bba-b476-68cdf234dc3b | -15.31564 | -47.85678 | 2025-10-24 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2eadd1b-6cce-3870-8db8-60232f06fb30 | -12.77032 | -47.37249 | 2025-10-24 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8413c682-4e8d-3a7e-924b-0ad802351339 | -15.83703 | -49.09034 | 2025-10-24 04:40:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a721ffa7-344e-34a7-b0e3-db56038e2fe6 | -15.61058 | -45.91791 | 2025-10-24 04:40:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0ecab402-3cff-3680-84be-3055fc101a4d | -13.35565 | -47.9674 | 2025-10-24 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 19d6e7f5-1fe3-3804-ab12-c1ac388bd78e | -12.03046 | -46.9186 | 2025-10-24 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b44cd49-25a7-3a9b-9582-d0d4356ed875 | -12.94245 | -46.54353 | 2025-10-24 04:40:00 | NOAA-20 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5cc31240-99da-35ac-b040-f0ccaa5bfc2c | -16.25148 | -46.78595 | 2025-10-24 04:40:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e911932-875c-3aef-9ad0-5fea5afdfc8c | -12.88756 | -43.43169 | 2025-10-24 04:40:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ba03b67-2767-3707-8ead-6d876823383b | -12.47307 | -54.45779 | 2025-10-24 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0112ac61-990f-3dba-ac8b-376346151ba8 | -17.09807 | -46.19315 | 2025-10-24 04:40:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a6d5756-c407-30bc-b629-37a47aab5249 | -16.67119 | -52.13443 | 2025-10-24 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63c4e6e3-c933-31b7-a705-df23a6746fce | -15.60694 | -45.91372 | 2025-10-24 04:40:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41fb9435-afda-33a8-a8e0-1885b0bd650d | -16.3108 | -46.57499 | 2025-10-24 04:40:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6298bae-787c-3502-a403-aae5c388dbe4 | -14.76753 | -49.29463 | 2025-10-24 04:40:00 | NOAA-20 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4823c8b6-3347-37ee-9d06-955ead3a5a9a | -15.83301 | -49.09351 | 2025-10-24 04:40:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README44.md)
