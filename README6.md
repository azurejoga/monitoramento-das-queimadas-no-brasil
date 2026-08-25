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
| 8bf14bfc-0601-3f89-b166-d2dccf194878 | -7.3287 | -64.660103 | 2026-08-25 00:32:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ebadd833-dfda-3348-86ea-8bcabe1b1ab2 | -6.1756 | -53.464001 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5283060e-f56b-3a0c-a82f-8d9ba3555147 | -4.6025 | -55.7309 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c64f92bb-df99-36a9-bb6b-89bf9620a3f1 | -6.8174 | -58.637798 | 2026-08-25 00:32:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d0aacf5e-3ed8-3279-ac30-b71d5f8459a4 | -14.9055 | -52.634701 | 2026-08-25 00:32:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2d1e676d-10a3-3d2b-bdfe-4c4371f8eecc | -12.1319 | -50.581799 | 2026-08-25 00:32:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 965e1f45-797e-3572-aa77-a29b6d4ebeb1 | -9.1697 | -58.316502 | 2026-08-25 00:32:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8bcb6d5d-0323-33f9-b923-90ae702061f9 | -16.5002 | -54.6628 | 2026-08-25 00:32:00 | METOP-B | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 559fb6ec-a544-3c59-bf1a-1f420228d7d7 | -5.9535 | -53.573101 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76b8125f-48ae-39ed-94f2-14101a5ff449 | -5.9498 | -53.5574 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61040680-3b6d-3204-9f6a-d0aad74bde60 | -8.605 | -54.708099 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e5f5fd2-e138-31a1-85b4-54625ee13acb | -5.7847 | -57.549999 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 711475e2-2df7-33de-b467-9b0bbc71258f | -3.5035 | -48.139801 | 2026-08-25 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c611749-8733-3cc8-80af-7f41045216f2 | -8.5665 | -55.266201 | 2026-08-25 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 994ad485-2e59-3e5b-83dd-608dba8b0056 | -6.5447 | -55.073299 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0ed32c4-3f00-3927-a56d-0d6a3f3e5324 | -6.335 | -54.741402 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3dd72728-9531-32a8-a2d3-cac21f06c7b0 | -6.5526 | -58.508301 | 2026-08-25 00:32:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 76a340fc-4537-3179-832f-6c3620527ac4 | -6.3269 | -54.750801 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db3ae475-9cb9-3066-a1c7-d58131564b2f | -3.6867 | -51.0886 | 2026-08-25 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc795720-65d7-3738-bb73-999c8f394837 | -5.7815 | -57.535801 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04970bb9-180b-348b-8bfa-c9ecc0b60638 | -11.1223 | -44.4468 | 2026-08-25 00:32:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4d35a078-2a9e-3def-bf1f-99e14329d3b2 | -6.1358 | -57.833401 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12fad0e5-7559-3765-b082-9c63d8dffdfd | -14.3982 | -52.9426 | 2026-08-25 00:32:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6dd3e214-1e15-3b3d-9466-411e960dda1e | -6.1232 | -57.730099 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50a54051-f7e6-37f2-8726-cc9f7c3bd69c | -6.9334 | -52.7752 | 2026-08-25 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2998be9-0ee6-3691-8147-7b2a12ef4ee4 | -9.0431 | -50.787601 | 2026-08-25 00:32:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d53624f4-84e1-3074-87c0-d89204bf0fd8 | -5.0111 | -56.1245 | 2026-08-25 00:32:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2310566f-4fce-3772-bd89-09c9be5c1e29 | -6.7965 | -59.573002 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f8d2accd-b8dc-34b4-a91f-3ab1ce330fe7 | -5.9736 | -57.612801 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f38d1e85-f549-3aba-a3bd-1afb91383faa | -7.2553 | -44.0476 | 2026-08-25 00:32:00 | METOP-B | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 68cfc13b-10fb-35df-873e-01ddc3302236 | -6.1755 | -57.6884 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eeea4931-4e40-3a84-8152-02b8554d47cc | -8.578 | -54.861599 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f902de40-3324-31c6-8c8c-e7499e7901ee | -5.9452 | -57.716599 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9738ed8-52e1-3d4d-83b8-c5d28ec03027 | -15.2393 | -52.787102 | 2026-08-25 00:32:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cdca241d-f8b2-360b-832d-418518af9878 | -6.1988 | -53.4753 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 938a981f-08f3-3552-8e02-f8e5947099ae | -8.2202 | -54.965099 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ed1dbc5-2952-37bc-8d08-4e8ddedfa71c | -14.2912 | -53.152 | 2026-08-25 00:32:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4cfb2e7c-679a-3e8b-851e-f53005dde445 | -5.9516 | -53.5653 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcf64a87-3f4c-38e3-af15-7be256c5edc1 | -7.2323 | -45.3181 | 2026-08-25 00:32:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 97087d6f-09b9-3cb9-941e-90466393b0ea | -12.7087 | -48.3741 | 2026-08-25 00:32:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e904517-d527-39b9-a3c7-974630aeb3e8 | -12.8565 | -48.4697 | 2026-08-25 00:32:00 | METOP-B | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0cde0936-32ef-3eff-be61-2b038e5dd601 | -8.5666 | -54.8568 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5650e810-7589-31d6-aec7-7976998100a3 | -6.5416 | -56.243301 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0c04b00-422d-3dd7-a1c2-452a0b0c2875 | -7.2228 | -45.807499 | 2026-08-25 00:32:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e20635ef-c479-3f1a-979b-42d640dd3e8f | -6.1326 | -57.818901 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb2d931a-24d4-32b2-9b32-727868f29e2e | -11.4041 | -44.500401 | 2026-08-25 00:32:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5aade5a1-47f4-3fb9-b2ae-72d4854f35ec | -8.6214 | -54.689602 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9869860c-a34f-3128-9bec-1baa931e01f8 | -10.0139 | -46.403099 | 2026-08-25 00:32:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ea6aabf9-732e-32ba-9bb7-1af6dc468a96 | -6.139 | -57.8479 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10072630-ff2a-3020-958b-933e98b52243 | -8.2199 | -55.009102 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88080857-a064-3b93-a7cb-eb53d01869bb | -8.5418 | -55.293598 | 2026-08-25 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3438000b-ea15-3c94-a473-637995405f3a | -12.8663 | -48.467098 | 2026-08-25 00:32:00 | METOP-B | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5671e567-2299-33ef-ba12-8dd5e6f92ad2 | -6.6145 | -53.177799 | 2026-08-25 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1186fac8-7a76-3ba3-8f2a-2bc2600a4ee5 | -6.1677 | -53.474098 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfcda9ef-f381-3062-ba0f-4c8a9192fe0b | -10.352 | -45.0392 | 2026-08-25 00:32:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7e34429e-bcec-39ca-9837-0e048580737a | -6.3253 | -54.743599 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46facb85-c4af-3fda-8fe6-1e6fb345e8ab | -10.9237 | -51.057201 | 2026-08-25 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0078740f-1989-384d-aeb5-f3e2b22bca67 | -6.8157 | -58.629902 | 2026-08-25 00:32:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 19a64f48-dec4-3769-939a-eb85bf02a08f | -6.5431 | -55.066299 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5998fc86-5ab2-3fe6-a466-3408246f78a2 | -6.1552 | -57.9207 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3807ad4b-4f78-3f14-b6f2-7e7ef1d64bbe | -6.2458 | -55.390301 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46d07700-bb80-3cb7-a2be-7a3c3ab85a43 | -12.1342 | -50.591301 | 2026-08-25 00:32:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5668039a-1ba2-3a04-a7da-c6e246cfba47 | -9.0407 | -50.7775 | 2026-08-25 00:32:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f76267b0-3b85-3e7f-9ce4-748fcabb32ce | -6.8057 | -59.6623 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c570f28a-48bb-300b-b398-09e5a87736b8 | -6.818 | -59.5774 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f4676914-1275-3e68-8bd7-55f9fa495bce | -6.2211 | -55.5998 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c2bedca-d2dc-31e8-bee5-597ff2d1ec1a | -7.2474 | -44.016998 | 2026-08-25 00:32:00 | METOP-B | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1df42f21-2af3-348d-9734-1f50f572116e | -16.373301 | -49.906799 | 2026-08-25 00:32:00 | METOP-B | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2e68ffd4-f303-3032-a84f-ce7cdf098a72 | -7.2611 | -45.3106 | 2026-08-25 00:32:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b2d186cd-773b-31e0-a1dc-6f164aafed67 | -6.1884 | -53.519199 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a26700f-4394-3377-ae76-7d9ad94ff011 | -4.2095 | -54.5495 | 2026-08-25 00:32:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff31cee7-cfec-39d6-a72b-9b77bb12859d | -6.4375 | -54.964401 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab59c0c4-662a-379e-8f81-c3d4dfed71f7 | -16.395 | -49.910999 | 2026-08-25 00:32:00 | METOP-B | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dd37029c-d77c-3f25-ac03-4984ce9485bf | -10.7882 | -50.922001 | 2026-08-25 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 65f7c57b-5b04-3698-8fad-c5a41b115c03 | -10.009 | -46.384102 | 2026-08-25 00:32:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b6b3688-ceb6-38f9-9090-faf48606e677 | -12.699 | -48.376598 | 2026-08-25 00:32:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cbe20159-f3d0-3a39-8247-20ddc1b01510 | -6.6341 | -58.458302 | 2026-08-25 00:32:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 80c8ccd6-a9e1-3830-8862-7016f0522f5b | -10.9388 | -51.033901 | 2026-08-25 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9d4ce68f-18fe-34ee-8d7a-94d33e39962d | -10.7763 | -50.914902 | 2026-08-25 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0b9cf5e7-ba99-3d84-bcd7-ad0c4c3cb62f | -6.751 | -59.646599 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2478e0dc-016e-397f-89fe-5f4fbc76d5c0 | -6.1787 | -55.4128 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82a884b5-8396-36a9-8de4-579afcdc960c | -4.9284 | -55.759602 | 2026-08-25 00:32:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2da68f8f-7f63-391a-903c-5de806ece8cc | -8.5277 | -54.821602 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6563bf9-cd17-33c3-8e39-f5be46d99c21 | -5.7929 | -57.540699 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91adada9-06c6-3c93-ad4e-c1ae93be047d | -12.8632 | -48.4547 | 2026-08-25 00:32:00 | METOP-B | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7365e43e-f1b6-3495-9cd7-bc26c6e17e80 | -10.7665 | -50.917301 | 2026-08-25 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 400b170b-154e-32d4-b811-0b23e557fb08 | -16.380899 | -49.8951 | 2026-08-25 00:32:00 | METOP-B | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 305e7031-e494-3f8e-8875-eaded0f1e2bc | -15.241 | -52.794399 | 2026-08-25 00:32:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c8f4d14b-afcf-311b-9e11-ae62a92579a6 | -7.0057 | -59.215698 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5fa48299-5c28-33f3-b9b1-f078a8bedf2e | -6.9353 | -52.7836 | 2026-08-25 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ec747a1-1f3b-3bd6-932d-50e3a0fd468f | -6.5349 | -55.0755 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f16619f-f360-32bf-9101-45e195414e51 | -16.4986 | -54.655602 | 2026-08-25 00:32:00 | METOP-B | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 728cdbdb-ddd1-3877-bfe2-e33d772cbb76 | -10.929 | -51.036201 | 2026-08-25 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0b2b3595-5628-39e0-8313-18dccd85a847 | -6.3366 | -54.748501 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5645b4c-3a98-39b4-8f5b-e6e811739827 | -6.2293 | -55.408699 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83a5c9bb-d6a7-3bec-a0e1-a96b3db08c55 | -7.0155 | -59.213501 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6a1eedb7-d455-3b2b-b92f-147ca79536fe | -4.9269 | -55.752701 | 2026-08-25 00:32:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1dd301e8-9e02-33d6-87a4-54db0066a558 | -6.8346 | -52.484501 | 2026-08-25 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f98d774-5d16-30ae-83c9-d0a09a79f32e | -6.1228 | -57.820999 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cadf3073-ec1a-39fa-b699-0a0a27337a68 | -10.8922 | -51.055 | 2026-08-25 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
