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
| 41480fe7-d20a-3d30-9ea4-f2e11eaee8dc | -17.7807 | -40.0182 | 2025-02-07 00:00:00 | GOES-16 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 112.1 |
| dcc6beb2-f9f9-37d5-b30e-4463feee7ff9 | -6.3353 | -43.360802 | 2025-02-07 00:31:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9782bd02-142d-3fff-9620-156e7eb6fd41 | -6.3371 | -43.3685 | 2025-02-07 00:31:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d52b489-d379-3430-9889-b90020f8b44b | -7.059 | -44.387199 | 2025-02-07 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dcebd967-2ab8-33c7-a1e2-c3ba75a53644 | -17.4716 | -40.860802 | 2025-02-07 00:31:00 | METOP-C | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a0725394-5532-3a89-be45-3ee6b2932e97 | -11.5831 | -47.615898 | 2025-02-07 00:31:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cfb6bb47-87bf-301b-95df-e8c304bd813c | -17.469801 | -40.852901 | 2025-02-07 00:31:00 | METOP-C | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ce371bad-777a-39f5-addb-a42302f8a542 | -6.3523 | -43.3895 | 2025-02-07 00:31:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb6bf627-3262-3646-ab15-b881573c8f10 | -7.0606 | -44.394299 | 2025-02-07 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f6ba97a3-5a42-36ba-89f7-e808dcbb6a3e | -14.1938 | -43.655399 | 2025-02-07 00:31:00 | METOP-C | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 059adb1f-0b34-33bc-843f-7d046d472e98 | -14.3494 | -44.116001 | 2025-02-07 00:31:00 | METOP-C | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| f9105f65-2987-3e42-a50c-6e5f3233c61c | -14.1922 | -43.648399 | 2025-02-07 00:31:00 | METOP-C | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6d207024-d087-3934-8bcc-7914ea23723f | -10.007 | -48.4837 | 2025-02-07 00:31:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3c1afb9-38f7-33a0-9664-89d02f10b003 | -10.0088 | -48.492199 | 2025-02-07 00:31:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 65e846e6-9bd6-3ae7-b17b-780405e38172 | -7.0688 | -44.384998 | 2025-02-07 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f25a7b4-3569-35b4-b25e-cdbd3a24bb44 | -6.3505 | -43.381699 | 2025-02-07 00:31:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c67d1281-5d49-3241-b5de-8e378a88c61d | -11.5849 | -47.624001 | 2025-02-07 00:31:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 379c6806-f547-311b-8c34-e7e0c9b737de | -14.3462 | -44.101898 | 2025-02-07 00:31:00 | METOP-C | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| af21dbde-09fe-3183-b49e-15e25588d73a | -8.9549 | -44.243198 | 2025-02-07 00:31:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 624d3e10-60d9-3c33-bdba-0252aecdc6a1 | -11.9696 | -44.666401 | 2025-02-07 00:31:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5e56fc5a-b787-3609-942a-c8ef7fd88a33 | -14.3478 | -44.109001 | 2025-02-07 00:31:00 | METOP-C | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| e6d197c9-000c-3748-92dd-09d0cacd733c | -8.9533 | -44.236099 | 2025-02-07 00:31:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a3dd7d33-f38c-3834-aa93-fcbe0238cdce | -22.67662 | -42.85625 | 2025-02-07 03:08:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| c0d65b00-0325-3fe4-a19b-287982d1be75 | -22.67517 | -42.86205 | 2025-02-07 03:08:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 224bb7e9-6146-32f8-8a0a-f0d84f732098 | -22.676 | -42.85804 | 2025-02-07 03:08:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 17fbc672-2e23-35f2-9bea-75a0987f56cd | -22.7805 | -43.04351 | 2025-02-07 03:10:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 8a6fe196-a53a-3d10-b18c-88393c8c4e66 | -14.33644 | -44.11863 | 2025-02-07 03:32:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 273a694c-fc3e-3a40-98e5-f0846e1d379a | -11.88099 | -44.22054 | 2025-02-07 03:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b52e699f-2ca0-3154-b70b-cfc24d8b715f | -10.8049 | -44.5136 | 2025-02-07 03:32:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5bac2d0-d97f-3f0a-9970-80850bd1847d | -8.94199 | -44.24055 | 2025-02-07 03:32:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39007e13-73db-3053-9229-20ca816521eb | -14.33989 | -44.11774 | 2025-02-07 03:32:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| faca41df-5492-38ea-8e79-b719d9e113a0 | -12.74413 | -44.83364 | 2025-02-07 03:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| bfdbb32f-1218-305a-b2bb-330493df6bc9 | -12.7432 | -44.83823 | 2025-02-07 03:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8ecedf10-7389-3aac-9da6-e9725c0dd7ca | -8.94107 | -44.24545 | 2025-02-07 03:32:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21415f5c-c2e2-3c3a-a58c-8e97e760a346 | -16.53273 | -40.05146 | 2025-02-07 03:32:00 | NPP-375D | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f8f2f581-9fe4-39fa-9595-b062d9ae1846 | -11.88685 | -44.22171 | 2025-02-07 03:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 768d4db1-47f9-3245-a72e-450464c13ff9 | -8.93581 | -44.23942 | 2025-02-07 03:32:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e45eb16-2d83-32ed-b742-8ee67d006e6e | -9.6267 | -41.83578 | 2025-02-07 03:32:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5e71bdd9-4153-3e90-bd53-f04d4de95c92 | -13.36483 | -43.83221 | 2025-02-07 03:32:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dab8055a-ace3-3d78-a4bb-b6833a81d103 | -14.3372 | -44.11483 | 2025-02-07 03:32:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 743ddcce-e766-3f22-a186-61af0c7ec74c | -20.2026 | -46.67782 | 2025-02-07 03:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d422b833-0e60-33c4-a693-c4afd8bde022 | -20.19996 | -46.66254 | 2025-02-07 03:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a35aae8c-e965-3f56-8624-d04cbc002173 | -22.67653 | -42.85749 | 2025-02-07 03:34:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 8745cc62-d44d-3bd9-80fc-2f584784fb99 | -20.19792 | -46.6715 | 2025-02-07 03:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc04d1c6-1663-33c3-8ffa-b1ef486206de | -21.62792 | -43.46746 | 2025-02-07 03:34:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| eae9e6ef-55dc-35ce-8c6d-99061f885c5c | -20.19839 | -46.67614 | 2025-02-07 03:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1fddafe-c968-3a3f-9f15-98297eb5475e | -20.41744 | -43.55442 | 2025-02-07 03:34:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 30fcb276-77ed-31aa-879f-c9a68d5cb1d4 | -18.80763 | -40.15891 | 2025-02-07 03:34:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2887399d-2818-3d69-a0c6-a45e7c190975 | -17.76778 | -39.77363 | 2025-02-07 03:34:00 | NPP-375D | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 5c53fcd7-eea9-369b-8e34-d8ba64bb0d8d | -20.20358 | -46.67355 | 2025-02-07 03:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b82eae93-42b0-3cff-8caf-9881e6904fa7 | -22.53736 | -48.81266 | 2025-02-07 03:34:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cfaaafd9-b5e2-3cad-aa5a-f9a93a927293 | -22.78007 | -43.04504 | 2025-02-07 03:34:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 2cacffcf-0f37-39eb-92b4-6d1af7882674 | -20.19936 | -46.67176 | 2025-02-07 03:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b009719b-c79f-3a8d-b5b6-a04a8de233b7 | -18.80816 | -40.16013 | 2025-02-07 03:34:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 45a4edcb-3957-3f21-9d30-aab0b1bfb5c1 | -20.19893 | -46.66704 | 2025-02-07 03:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb2f7fe9-2929-306f-b635-2d88e564f229 | -17.51038 | -39.72432 | 2025-02-07 03:34:00 | NPP-375D | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 59769888-1c2e-3d9d-a560-a3b99024d309 | -20.49362 | -44.14933 | 2025-02-07 03:34:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1b4e2a53-bc65-3182-8aec-4521fcd2f5f3 | -19.22057 | -40.16137 | 2025-02-07 03:34:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 34a0429a-ed14-3e25-aa5c-5f54c134f2fa | -11.35745 | -48.0147 | 2025-02-07 03:53:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd214299-bf9e-392e-80fe-0e4558657575 | -5.9103 | -45.40252 | 2025-02-07 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb2373e1-0bf1-39b1-b1fd-b886c3c38a29 | -9.98657 | -48.08322 | 2025-02-07 03:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d6327e8-a750-35fd-af2f-5b2e3dcfee5f | -11.58122 | -47.62455 | 2025-02-07 03:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81e930f5-2b6b-3c43-8943-4928fde02acc | -12.48868 | -43.78989 | 2025-02-07 03:53:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3aacbd77-9860-36a9-b6c1-68693b1f602f | -12.59744 | -45.0561 | 2025-02-07 03:53:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f1c4953-b43b-3083-891b-55f9a99ce681 | -10.3371 | -47.90385 | 2025-02-07 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 510af6d0-f3bc-306d-a611-082cf3637741 | -6.32264 | -43.36737 | 2025-02-07 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a151bdc7-662e-3686-ae23-39575abdae2a | -12.48866 | -43.78706 | 2025-02-07 03:53:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef9e1a81-f05d-374d-971b-cde0e896a466 | -11.57335 | -47.62657 | 2025-02-07 03:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 901b8690-0ee8-321b-b1da-436664c9948f | -9.98506 | -48.08489 | 2025-02-07 03:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c6e992f-f91e-3573-83c1-7bbb03e0c352 | -6.22646 | -44.82586 | 2025-02-07 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3721b0c-a441-389a-b59d-05ce6e705427 | -11.57436 | -47.62109 | 2025-02-07 03:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac2c3c71-c184-3055-bc8f-50699bb79c80 | -9.98079 | -48.08547 | 2025-02-07 03:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a4394c0-e037-33b6-9fe3-63feb26c882c | -6.32206 | -43.3709 | 2025-02-07 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 339075b0-f725-3347-af46-a511346a1ea4 | -9.62699 | -41.83551 | 2025-02-07 03:53:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8969d871-b4f7-3db8-81f5-e69fb3b22cd1 | -11.88325 | -44.2224 | 2025-02-07 03:53:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d180f1c4-8f97-342d-abd6-f7e75a53f869 | -6.34382 | -43.38899 | 2025-02-07 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a8e6afe-1d6c-3a5a-852b-8ba0115b5f81 | -10.80618 | -44.51432 | 2025-02-07 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1900c5d4-bcf5-3754-aa78-9b023d5c1b76 | -9.98598 | -48.08634 | 2025-02-07 03:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e345403b-a3ae-314c-850e-a14d3f7af704 | -12.1085 | -44.74012 | 2025-02-07 03:53:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 77b33923-e7f7-35bd-b2eb-fa53439ef317 | -12.49242 | -43.78775 | 2025-02-07 03:53:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 087b2516-8dc8-3587-b793-9db8dbee0cc2 | -8.94354 | -44.24079 | 2025-02-07 03:53:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a85f45b0-78fb-33b9-9e7f-1037a9cb8ce5 | -6.38471 | -43.67053 | 2025-02-07 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7cfbaad-17ed-39d4-bce3-997cff7c69df | -6.33068 | -43.36866 | 2025-02-07 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fad96cb3-98a1-39d9-9939-6541d4263d86 | -6.98235 | -40.43256 | 2025-02-07 03:53:00 | NOAA-20 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cdd61cce-8c1f-3bf6-a4d0-7b3580d7598c | -6.3398 | -43.38834 | 2025-02-07 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d71eb429-a79c-37cd-9336-764dcc31cede | -11.88424 | -44.21939 | 2025-02-07 03:53:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf36bada-e7e3-381c-87ea-1fb533e7fb91 | -8.93946 | -44.24009 | 2025-02-07 03:53:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11af4fea-1cf9-3a9a-af78-0a02d8d43ac2 | -12.49324 | -43.78595 | 2025-02-07 03:53:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56d2153b-0f13-3324-a751-49de2d974990 | -10.65548 | -44.49369 | 2025-02-07 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c98b4c39-f4be-3a38-85cb-9894720a929a | -10.4872 | -47.39206 | 2025-02-07 03:53:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 423fb206-6fcb-3172-aafa-0f568d7decc8 | -11.57635 | -47.62356 | 2025-02-07 03:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc0e226a-0b8c-33fc-a8fb-d7c8c8f3e093 | -10.34017 | -47.90345 | 2025-02-07 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 627da285-a7e5-3c56-9daf-743df2f878b4 | -11.95896 | -44.66751 | 2025-02-07 03:53:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 261a51fa-3c49-3801-b395-aa78ad83a14a | -6.33009 | -43.3722 | 2025-02-07 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b41dfa8-3544-3dba-ac76-c9532772c5cc | -9.27126 | -47.91302 | 2025-02-07 03:53:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48bca68d-c236-3ab7-91ba-2daa7ac7e8ec | -11.57922 | -47.62208 | 2025-02-07 03:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da7f09d8-4baf-3c40-b531-8b893e3e183a | -10.34077 | -47.90028 | 2025-02-07 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 338ee5c5-2780-3c1a-ae66-1c22c1972401 | -10.3422 | -47.90469 | 2025-02-07 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4f60f77-0f4e-3b7d-9ba9-00095dfce3a1 | -11.88336 | -44.22436 | 2025-02-07 03:53:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfd10c63-99bb-3f1d-98d4-691f7ee9cce9 | -11.35801 | -48.01169 | 2025-02-07 03:53:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README2.md)
