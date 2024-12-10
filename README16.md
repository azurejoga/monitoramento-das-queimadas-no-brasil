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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4305192a-1a67-3ad3-831e-8d2dda038a39 | -14.53018 | -45.48236 | 2024-12-10 03:59:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f00b824e-cc08-33d1-af2c-c86be6327567 | -12.24729 | -52.44769 | 2024-12-10 03:59:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 186ef161-65e9-37e6-9592-c15de7466530 | -13.10152 | -43.32304 | 2024-12-10 03:59:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 131a12ed-43e7-3409-aec9-61f45bc3a776 | -8.86827 | -47.67689 | 2024-12-10 03:59:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d18e74fe-6bd3-346b-959d-2b6497549187 | -13.93897 | -44.35854 | 2024-12-10 03:59:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 992ab2e9-50fe-381f-aa4f-2c32686b53f5 | -9.16262 | -49.5009 | 2024-12-10 03:59:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e91a062a-d4c8-3089-a839-7dcb6fc808d0 | -12.92259 | -47.8904 | 2024-12-10 03:59:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64999721-84ee-325b-9ce5-eed9d70cf66a | -11.41312 | -54.32616 | 2024-12-10 03:59:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7d0b7d09-2076-328b-98b8-ef9308c257fb | -8.97044 | -47.08549 | 2024-12-10 03:59:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f9ee03c-c6f7-354f-b539-103806fb01a9 | -11.63276 | -48.02811 | 2024-12-10 03:59:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ee96130-49e2-3e30-bfd0-c5b3a50c8985 | -14.29168 | -43.94006 | 2024-12-10 03:59:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77d6e2de-8917-3457-8dba-a8496f073ee8 | -8.97174 | -47.08811 | 2024-12-10 03:59:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 256652b8-2a52-307a-a02d-6610ef284cd3 | -12.04012 | -44.44575 | 2024-12-10 03:59:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4fb1c7e0-caee-3ffb-b45e-9d6a958065ca | -10.44072 | -44.88968 | 2024-12-10 03:59:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 601162b4-af87-3b5b-aa5b-35578c0cfae6 | -9.93439 | -36.44846 | 2024-12-10 03:59:00 | NOAA-20 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c4ae9e2b-7a5e-3bfa-9bf9-86e0d794bac6 | -11.74952 | -41.14199 | 2024-12-10 03:59:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 77aa5ba6-de1a-3644-b481-0e233c07f357 | -8.97493 | -47.08629 | 2024-12-10 03:59:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c7d4106-2f45-3f09-ada0-ca678696e3e5 | -10.82348 | -44.3662 | 2024-12-10 03:59:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b116ebb5-a4aa-3cca-97bb-2d05899c7560 | -10.43993 | -44.89444 | 2024-12-10 03:59:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97a85988-9e4a-3f86-bd2c-f12424fa7f4b | -10.37238 | -36.3796 | 2024-12-10 03:59:00 | NOAA-20 | PIAÇABUÇU | ALAGOAS | Brasil | 2706802 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 08fb751f-7633-37bc-969a-88cd337728d8 | -14.53097 | -45.47781 | 2024-12-10 03:59:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c123e2e-1aff-3ef0-9a12-fd465e58f3a9 | -12.56961 | -51.30961 | 2024-12-10 03:59:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61ee787d-0779-39fa-b423-31409b29ba77 | -13.93967 | -44.35442 | 2024-12-10 03:59:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa30ea54-9ebf-3784-824d-3b5de82893c9 | -7.98317 | -50.68355 | 2024-12-10 03:59:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 06a2a807-419a-38a7-a44b-011b35a3fb2c | -10.44375 | -44.89505 | 2024-12-10 03:59:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 116de68a-e91c-3224-80c5-2f2b608f48e4 | -11.36478 | -43.90553 | 2024-12-10 03:59:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6bf2a5fb-bae5-30ef-83a0-ff589b9dfc25 | -13.94321 | -44.35507 | 2024-12-10 03:59:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d878fa36-eda6-39bb-b73d-77ec919be6e2 | -12.3674 | -54.17016 | 2024-12-10 03:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2751092d-699c-322b-98bf-c12a59abea98 | -9.10379 | -43.19601 | 2024-12-10 03:59:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a4a8fa71-22f8-3521-a3e4-99645e9524ad | -10.87595 | -44.3416 | 2024-12-10 03:59:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff6a5423-ba92-3039-b243-f46dc23558f4 | -10.02131 | -53.75559 | 2024-12-10 03:59:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a55711ee-6a9a-3b20-a571-73147e27ba29 | -12.7809 | -38.49789 | 2024-12-10 03:59:00 | NOAA-20 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c80cba7d-8c57-39a8-8d31-edbf4b801cdc | -10.45578 | -36.79752 | 2024-12-10 03:59:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 06bd81cf-ed57-33bf-a450-72869da27dbe | -12.24546 | -52.45682 | 2024-12-10 03:59:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 313b5511-6a83-3e6f-858b-36402dc5cc5f | -12.71628 | -43.95187 | 2024-12-10 03:59:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23653959-4016-3f85-ae17-a15fccafbe74 | -13.10494 | -43.32364 | 2024-12-10 03:59:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c481015d-7982-31d2-83d1-49f9f0b333aa | -13.10279 | -43.31544 | 2024-12-10 03:59:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 363b0680-8af8-37fb-8d4b-1100ec22159a | -10.89945 | -45.06445 | 2024-12-10 03:59:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c11c8b3-39f2-3ef5-b480-d45cd7e9c9b2 | -12.2413 | -52.44637 | 2024-12-10 03:59:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d1efba4-4d6c-32f9-ad17-67eea18d78c2 | -10.45022 | -36.7828 | 2024-12-10 03:59:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2d556eb2-e8f6-3a54-aaaf-99e32d05b61c | -10.45776 | -36.78371 | 2024-12-10 03:59:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| dd103cea-ced3-3c22-8fd8-f382834fd6f5 | -13.10215 | -43.31924 | 2024-12-10 03:59:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6baf2bb1-9a53-3048-93d4-42f429e769cb | -12.85396 | -43.82204 | 2024-12-10 03:59:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc64f1e8-a694-3761-a571-f0e8e1bf0918 | -13.0816 | -44.00027 | 2024-12-10 03:59:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3c01bd0-6431-36a6-8e10-e83644593732 | -13.40084 | -43.91303 | 2024-12-10 03:59:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6353233f-5f2e-3a4b-9b4f-3491d228f30b | -11.87333 | -43.72313 | 2024-12-10 03:59:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 00cbd766-4110-3200-bafd-46cbfb30dfe2 | -13.10558 | -43.31982 | 2024-12-10 03:59:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c8b48818-df6a-3a03-a68a-fa3748f77d7a | -13.0609 | -38.92834 | 2024-12-10 03:59:00 | NOAA-20 | JAGUARIPE | BAHIA | Brasil | 2917805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2a557817-9212-3cd2-8279-290d5097420f | -14.53389 | -45.48307 | 2024-12-10 03:59:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfc2a891-f199-3672-818a-c5e1acc3a3e0 | -13.06438 | -38.92887 | 2024-12-10 03:59:00 | NOAA-20 | JAGUARIPE | BAHIA | Brasil | 2917805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d6249080-adb6-31db-99f9-9f86e2e05097 | -10.50294 | -44.93183 | 2024-12-10 03:59:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a66d5cc0-a61a-3b73-a30a-c0ebdd1d18ca | -9.19891 | -49.48064 | 2024-12-10 03:59:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18a1c626-0ef4-36e0-8e93-e4f22170c97a | -10.69368 | -40.98905 | 2024-12-10 03:59:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8e861bc8-fc85-3c61-93bf-de8c42964684 | -9.25644 | -40.38986 | 2024-12-10 03:59:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 40b53996-4db4-31ac-aa4a-d8f5d7fc058b | -13.94251 | -44.35919 | 2024-12-10 03:59:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 90d1ca9c-47da-3031-affd-c567ec74a5c3 | -12.85401 | -51.93353 | 2024-12-10 03:59:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8cc67b80-567e-316c-915c-b2a0eaab7e5c | -8.86221 | -47.66745 | 2024-12-10 03:59:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79dac120-78b3-3aa8-9500-dcb2cb235d72 | -13.12189 | -39.81165 | 2024-12-10 03:59:00 | NOAA-20 | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3df2346d-7b30-3f92-898f-4c09f674ffea | -12.36616 | -54.17618 | 2024-12-10 03:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 14ccb05b-0fe5-3674-b048-b54327770cb7 | -12.20379 | -43.69849 | 2024-12-10 03:59:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a70046e5-de06-3ab0-be71-6326c0b04b52 | -7.97084 | -50.68536 | 2024-12-10 03:59:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1a2bb19-7461-3d7f-9210-0ee33a1eb831 | -12.16961 | -44.05442 | 2024-12-10 03:59:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1e38e474-dde9-3a22-a70a-1f2c0b9e6cd3 | -9.70356 | -36.17815 | 2024-12-10 03:59:00 | NOAA-20 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a6e13697-357f-364a-95b0-37529b1389a8 | -12.23946 | -52.45552 | 2024-12-10 03:59:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4ae5456-5e2b-3e72-a0ca-968c97cec70b | -11.633 | -48.02534 | 2024-12-10 03:59:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18bf5956-bbef-3bca-a575-47808ec327ea | -12.07445 | -48.40101 | 2024-12-10 03:59:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0609840-a767-3018-b1d1-de8f4d202323 | -10.46087 | -36.78874 | 2024-12-10 03:59:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 42524752-aa28-37b0-b1c0-73fada406726 | -12.3705 | -54.17165 | 2024-12-10 03:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ea016459-38a7-30f1-853e-8f6bd73695a2 | -12.3686 | -54.1643 | 2024-12-10 03:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bdc13306-5926-3738-8c17-88bc501fc110 | -10.45523 | -44.88952 | 2024-12-10 03:59:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f61458f2-126b-3eae-a19d-abc97f6e04fd | -13.83342 | -41.79452 | 2024-12-10 03:59:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6b6015eb-c24a-3826-b3a9-3d03c26122cd | -13.62497 | -44.37049 | 2024-12-10 03:59:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98c2c797-e8d6-3e05-8b2f-180ee4533444 | -9.84062 | -48.57273 | 2024-12-10 03:59:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 41e9b95d-4558-32b3-a8ad-ceed2c7d1cee | -12.85463 | -43.81807 | 2024-12-10 03:59:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 584af07d-0e5b-3f52-a7d4-c80e9bb4368e | -10.45061 | -44.89353 | 2024-12-10 03:59:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b21cc83b-143d-34fd-b531-bc96000c4e43 | -12.36263 | -54.17607 | 2024-12-10 03:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c71c9af3-8768-3656-be10-09124e024832 | -13.06263 | -38.9166 | 2024-12-10 03:59:00 | NOAA-20 | JAGUARIPE | BAHIA | Brasil | 2917805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f7179f2c-0ae2-3bb0-a6a6-3ec398c91cf7 | -8.86359 | -47.676 | 2024-12-10 03:59:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d3a9c8ce-6453-3c7d-8398-345c3d088688 | -8.86509 | -47.67816 | 2024-12-10 03:59:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2714695f-2c53-3809-8c18-2ba92fc6c7dc | -11.36716 | -43.90495 | 2024-12-10 03:59:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 346d6e6e-3703-32d9-8554-1a7f0a547fc8 | -10.24033 | -36.49417 | 2024-12-10 03:59:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 82e52531-a871-3da8-bc4b-b9ad4b425de2 | -10.4571 | -36.78828 | 2024-12-10 03:59:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 017eb156-00b3-3266-a83c-45b4bbed20cf | -12.6553 | -43.83853 | 2024-12-10 03:59:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68180311-df5d-361c-801b-0b1f80e9e10c | -8.71274 | -44.00986 | 2024-12-10 03:59:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d091477c-e7ce-39fc-961a-825a6ee42092 | -9.19423 | -49.47647 | 2024-12-10 03:59:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51b19a28-c81e-311a-bd06-0dbcfc6aa95e | -10.45142 | -44.88883 | 2024-12-10 03:59:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6003cbaf-92c7-3f94-b276-64c329d60c1f | -12.37298 | -54.16001 | 2024-12-10 03:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3a538345-3e38-3b93-becb-f686ae525484 | -10.02804 | -53.75705 | 2024-12-10 03:59:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7f986e6a-6dd9-32ff-9d6e-b0c799ee12d7 | -8.85891 | -47.67513 | 2024-12-10 03:59:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f5d57f4-8178-333c-8299-7cf8a015fea8 | -11.83674 | -43.72512 | 2024-12-10 03:59:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82de6e1f-67e3-3c8a-aa64-b8a19e034acb | -14.82328 | -43.82109 | 2024-12-10 03:59:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03839499-abdd-3c0d-859a-e5a960ca4a89 | -12.3639 | -54.17008 | 2024-12-10 03:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 735dcd05-f840-3801-87c7-8b1d66a89aa5 | -11.17251 | -40.36198 | 2024-12-10 03:59:00 | NOAA-20 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 784bcf11-0e8c-3f4b-b07a-c3435cf681e0 | -13.11852 | -39.8111 | 2024-12-10 03:59:00 | NOAA-20 | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8de39545-d988-355b-b503-cd131d5cf6f9 | -13.06148 | -38.92442 | 2024-12-10 03:59:00 | NOAA-20 | JAGUARIPE | BAHIA | Brasil | 2917805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e7a3b975-ed23-345f-ab87-6eaf034f90f4 | -8.85977 | -47.67019 | 2024-12-10 03:59:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3ebaf585-18b3-33da-9037-d717bd2906ea | -8.97705 | -47.08436 | 2024-12-10 03:59:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dcd3f357-756e-3126-b9ec-c6b0b1b457f9 | -7.97587 | -50.69067 | 2024-12-10 03:59:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 352ea6f7-c945-3b6a-acde-f948fe38dade | -14.15526 | -43.72049 | 2024-12-10 03:59:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02971ddf-f9f6-3997-be08-d89925b26ed3 | -10.44299 | -44.89222 | 2024-12-10 03:59:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README17.md)
