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
| 74cfc6d0-7d42-3ab3-8903-621fdbbc8fbd | -11.54566 | -46.86203 | 2026-09-16 03:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d43b924-b7e5-352c-90c2-73915781ac7c | -8.54899 | -44.4966 | 2026-09-16 03:55:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b148de5e-43dd-3ed0-9445-fd932ea45b03 | -12.85506 | -44.39307 | 2026-09-16 03:55:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d392da70-5d52-34db-b025-53b18e24f9a6 | -13.2933 | -51.27222 | 2026-09-16 03:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 85bab0a4-1887-3724-810f-67cbc93463fa | -11.25536 | -43.45599 | 2026-09-16 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc3a3efc-0034-39e5-a19e-ffbd67304fb8 | -11.54515 | -46.86375 | 2026-09-16 03:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ee9578a3-f9a0-38fd-895c-e2139b82483e | -11.5509 | -46.86486 | 2026-09-16 03:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 94597106-a6bc-3d50-b5d0-974756094bc9 | -9.33917 | -44.39175 | 2026-09-16 03:55:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc49cf98-f819-364a-9d9e-7764f1fbfd24 | -11.89473 | -43.82056 | 2026-09-16 03:55:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| ec39d64f-8189-376a-bfa6-a44f51ba1a69 | -11.61632 | -46.95743 | 2026-09-16 03:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4bce05d5-6bfe-38ef-971b-1a811df18fc7 | -9.767 | -46.57759 | 2026-09-16 03:55:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 041e50dc-57ed-3936-a691-342d140be370 | -15.27036 | -42.80587 | 2026-09-16 03:55:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d014536-3058-35f6-be07-0fd285b7c487 | -10.78227 | -46.20373 | 2026-09-16 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5964326f-d14a-3e7b-bee2-079f23f0719f | -13.55971 | -43.53239 | 2026-09-16 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58121f51-1b63-37c5-8621-6888a81e9935 | -9.10427 | -45.73483 | 2026-09-16 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 23ed2ec5-b8f9-3112-9b78-0b3144ec9f9b | -9.22666 | -46.70513 | 2026-09-16 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c471bda3-d8f8-3e2c-8e82-823b116de2a7 | -11.89552 | -43.82328 | 2026-09-16 03:55:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 4cdf6490-fda5-3d3a-a0e8-57629d9a5223 | -9.33974 | -44.38869 | 2026-09-16 03:55:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf836a55-9180-3066-9ff9-793bee7a92a2 | -11.82926 | -37.57743 | 2026-09-16 03:55:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9f5e280f-13aa-30d9-bf84-e55673d0fe12 | -10.3704 | -45.12714 | 2026-09-16 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e6052029-36e3-35ae-ba15-e0bec438db7a | -10.31213 | -45.27164 | 2026-09-16 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d49fe829-406e-38cf-af66-29fb2b2ec9ba | -11.19754 | -42.815 | 2026-09-16 03:55:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7da1dcfb-6e54-3564-b2f6-e200e8df801e | -9.10986 | -45.73584 | 2026-09-16 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c8bd5ad5-8863-3d09-b25a-a41f617fad3a | -11.89197 | -43.83569 | 2026-09-16 03:55:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2cd401b4-af50-36ef-8a8d-5c4cf7617cc1 | -11.34496 | -47.31148 | 2026-09-16 03:55:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f75c99d2-ef42-3b6f-b7c7-c9e31c3cb541 | -9.78573 | -46.54337 | 2026-09-16 03:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6c8020a-27e2-368a-9319-fc942ae45236 | -12.52931 | -47.11932 | 2026-09-16 03:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 20334315-c3df-37de-b188-34442bc9a481 | -9.80392 | -48.92326 | 2026-09-16 03:55:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 951b2b2b-ec74-369a-8816-a0d25517592d | -15.64497 | -39.80469 | 2026-09-16 03:55:00 | NPP-375D | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f95b895c-e8e4-33f0-abf7-cf8d46335ff0 | -11.17663 | -42.8294 | 2026-09-16 03:55:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 571a2d42-a20b-3071-afa9-b803ea38f6da | -13.59052 | -47.91057 | 2026-09-16 03:55:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66ada58c-2deb-3121-98a8-b6c1ca564ef0 | -9.78035 | -46.54376 | 2026-09-16 03:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 31f85c2a-560c-32c5-90ef-cd5b3c8f84bd | -11.13371 | -40.48141 | 2026-09-16 03:55:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 4f0c7b23-c38a-3663-b162-011fcf13cbbe | -15.02763 | -41.46033 | 2026-09-16 03:55:00 | NPP-375D | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 928df233-4512-377f-9ae0-5a3881eb644f | -11.78985 | -46.58888 | 2026-09-16 03:55:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23b90426-44df-3c2a-bce2-be12a644b8cd | -14.22612 | -48.51869 | 2026-09-16 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4ff7feb2-6b05-387b-83b0-4f0d48034ff5 | -9.22884 | -46.7073 | 2026-09-16 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 984146a8-6a70-354a-a69e-674d8529ac86 | -10.83233 | -46.20036 | 2026-09-16 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ab994af-5e3d-3ba7-b072-902380134c5b | -9.5738 | -46.59067 | 2026-09-16 03:55:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c023c115-c608-36ac-a8e4-de50b85007af | -11.17743 | -42.82497 | 2026-09-16 03:55:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 511e7387-c864-34b7-ab6d-ec08825605a2 | -10.36978 | -45.13038 | 2026-09-16 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 94a99f7e-19fd-3538-b789-851dda8ae4b0 | -9.84227 | -48.35716 | 2026-09-16 03:55:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d1afc55-4f15-32ae-9458-abd24e4c15ac | -15.78958 | -41.80922 | 2026-09-16 03:55:00 | NPP-375D | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f54d21a6-6d97-3e75-a8af-1604694a3795 | -8.54389 | -44.49516 | 2026-09-16 03:55:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64efeabc-8a72-3f57-a276-9193c8407ec3 | -11.54011 | -46.85909 | 2026-09-16 03:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e008f02b-2bb7-387f-89e7-9b47148fd396 | -16.7895 | -39.46251 | 2026-09-16 03:55:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 14a5dc83-07b2-33b9-b7ca-bbd45b2121f1 | -12.52604 | -47.10577 | 2026-09-16 03:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a75902a3-6bd9-3fe0-abbc-7acbbdb7da40 | -10.82128 | -46.18105 | 2026-09-16 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 43fad6ba-4067-3a60-b2a3-7ad96789d5af | -9.09446 | -45.72563 | 2026-09-16 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 37334799-f460-3d7b-9c38-3b2ada38d1c3 | -11.20038 | -42.82471 | 2026-09-16 03:55:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 8165e268-2d08-3ff4-add6-1fb855901430 | -10.40902 | -48.66264 | 2026-09-16 03:55:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b1f8ae2-bab2-30a1-b352-4db6220147c7 | -15.89398 | -40.23199 | 2026-09-16 03:55:00 | NPP-375D | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| f983aaee-d012-3e91-9c38-a5493ea42e0c | -9.49283 | -45.44389 | 2026-09-16 03:55:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f9e9b593-4b5b-3ea1-9746-974c1610aad3 | -11.88729 | -43.83479 | 2026-09-16 03:55:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e06a9ba4-88ca-3ea4-894c-60580e75d532 | -13.59764 | -45.4651 | 2026-09-16 03:55:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b36f1deb-8dc4-31d0-8269-3a1ea577aea5 | -9.78538 | -46.54902 | 2026-09-16 03:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2386ddd3-2c8e-3c1d-b91b-46fb285a0205 | -10.4083 | -48.63918 | 2026-09-16 03:55:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6ce6176f-eff0-3fdf-b7d2-da7a3f4fa4a5 | -15.28451 | -42.79868 | 2026-09-16 03:55:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d10143f5-f6f8-30fc-b723-52586ecdb429 | -10.46308 | -44.95102 | 2026-09-16 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 10f5138d-aa69-36ae-8da2-bd7762fc0ced | -9.48748 | -45.44236 | 2026-09-16 03:55:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e78b074d-9923-36b7-9741-8cddd3bbd803 | -9.76765 | -46.57927 | 2026-09-16 03:55:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7ec9ba23-eb31-365c-b59c-ecaf55e6342e | -15.24736 | -49.11166 | 2026-09-16 03:55:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c36e3ff1-fa3a-3add-89ab-3760e146d592 | -12.71662 | -43.20801 | 2026-09-16 03:55:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c8c5e6bb-5ce8-3df6-a6f8-8b01c0e1c8e4 | -12.22164 | -47.13131 | 2026-09-16 03:55:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a88e112-db2c-393d-8dce-dcbd0ed99fcc | -10.4105 | -48.65548 | 2026-09-16 03:55:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 33743959-85d2-3ab3-bc82-cdb0923d7b81 | -11.7891 | -46.59277 | 2026-09-16 03:55:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7eb087c5-f9eb-3a40-8974-7d790712a2dd | -10.40726 | -48.64438 | 2026-09-16 03:55:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a76e4142-e578-3be7-9595-8cdd4b336af6 | -9.54871 | -45.42174 | 2026-09-16 03:55:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bffde842-34ed-3c2d-b892-9ae4bb714ee5 | -9.09937 | -45.73024 | 2026-09-16 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 556dd10d-6d21-3879-8515-4153ef9efdb0 | -10.45907 | -44.94381 | 2026-09-16 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54a651d4-a300-3bfe-85dc-39c2aee8bc25 | -10.60056 | -47.76444 | 2026-09-16 03:55:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d38e3c35-38d4-31ac-852c-91285d119db9 | -13.55494 | -43.50816 | 2026-09-16 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b59fdfa9-4113-3b40-95c2-34acd42926f1 | -11.16892 | -42.79602 | 2026-09-16 03:55:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5f5d52a3-e9ad-3408-9f93-4a0c72a187ee | -9.85781 | -49.82521 | 2026-09-16 03:55:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5a9a1afa-b119-37f8-93fe-e7dd0a49127e | -9.48819 | -45.43861 | 2026-09-16 03:55:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 545e4381-ef26-317e-a7ba-9735c3d8dfe4 | -10.78082 | -46.21134 | 2026-09-16 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ddc46d7-3aa6-3f0e-b897-c7d021f4d289 | -15.28565 | -42.81571 | 2026-09-16 03:55:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 92a70aad-9442-3536-9d13-ec58621a36b7 | -8.95424 | -44.39966 | 2026-09-16 03:55:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8443fb9c-4614-3853-b42e-d90c6b1d622c | -8.64824 | -44.45175 | 2026-09-16 03:55:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af331f62-b907-396f-9935-d073fb811067 | -9.78493 | -46.54747 | 2026-09-16 03:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e6deadc-52aa-376d-9ea4-3ee56edd804a | -12.17381 | -38.59868 | 2026-09-16 03:55:00 | NPP-375D | PEDRÃO | BAHIA | Brasil | 2924108 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cae89bfe-bfbc-3433-8c70-3c7d3c666dfa | -8.86126 | -44.90952 | 2026-09-16 03:55:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79153264-a582-3b6a-bbf9-1054b3d09243 | -11.34325 | -47.32032 | 2026-09-16 03:55:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d860b07-8e72-3122-a245-0f42e0cb3d2f | -12.49526 | -41.41348 | 2026-09-16 03:55:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c8a21acf-10a3-3a64-9346-39080c83a1ec | -12.55699 | -47.10059 | 2026-09-16 03:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a7514c75-0893-37cf-8ad1-78468ab21f89 | -12.53668 | -47.11229 | 2026-09-16 03:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a3f230f6-179b-3f31-8a37-bd0d8a491eaf | -14.66173 | -48.02008 | 2026-09-16 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e164662e-cc19-36d8-a038-93af32aa8c14 | -9.11612 | -45.7333 | 2026-09-16 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 88466981-07ef-39ca-ab46-968db22d2ede | -11.14131 | -40.48302 | 2026-09-16 03:55:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 544fd04b-bf3b-323b-9a5e-a40f09e18517 | -14.2266 | -48.51741 | 2026-09-16 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f3b4745-0f04-39c0-b85e-4f6227d4dfd8 | -10.37089 | -45.13115 | 2026-09-16 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ed293304-ddc3-3f2d-8a9b-7ae4c202ac31 | -11.13668 | -40.487 | 2026-09-16 03:55:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 5a197301-9ed4-3829-a8a3-36a997ca06de | -11.53935 | -46.86287 | 2026-09-16 03:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cd098656-a6c4-3c94-8136-d3782bdc4b47 | -12.54484 | -47.10115 | 2026-09-16 03:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85f5014c-72a2-35a0-a2b3-b9f06716820d | -10.7745 | -46.21411 | 2026-09-16 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8947cb94-a42a-388b-ac69-d3b00061e22d | -8.84088 | -45.86786 | 2026-09-16 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12c279cf-0b12-3a58-bbde-03c97fbafa7c | -13.59155 | -47.90545 | 2026-09-16 03:55:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ed989a5-a44f-3229-9ffe-7ca68e340d6d | -12.54564 | -47.09709 | 2026-09-16 03:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0dbe60ab-5212-399e-aa98-8338c540ebdf | -9.34031 | -44.38566 | 2026-09-16 03:55:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 114ff2dc-7344-306c-af4d-81ca77070638 | -9.76049 | -46.58 | 2026-09-16 03:55:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |


[Clique aqui para ver as próximas entradas](README17.md)
