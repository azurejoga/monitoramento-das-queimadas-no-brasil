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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ba77acf-c4c1-3f3c-9e26-780a8fe59f49 | -18.02542 | -54.37622 | 2026-07-10 00:18:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 19.4 |
| f4d14e2e-e493-3ee4-b288-83c1ed4d7896 | -17.54179 | -54.00806 | 2026-07-10 00:18:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 2ae7f8d3-f528-3713-972e-f556e3dbbd8f | -18.02216 | -54.3489 | 2026-07-10 00:18:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f6ca5256-da7e-392e-8b84-704f86312083 | -21.7668 | -56.30679 | 2026-07-10 00:18:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 43.6 |
| ec26154c-a487-3710-a7a3-f5d792dd58c7 | -18.02378 | -54.36246 | 2026-07-10 00:18:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 110.4 |
| d3d3d15c-2b41-388e-89f4-c9742ba6dde2 | -22.92012 | -49.21186 | 2026-07-10 00:18:00 | TERRA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 73dff063-d8c8-36e1-aa1d-28605612c836 | -17.54029 | -53.99518 | 2026-07-10 00:18:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c702c3d4-c990-372b-88d4-9a2db315bb60 | -18.0344 | -54.36113 | 2026-07-10 00:18:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 15.1 |
| c156fd36-41de-306d-b2ab-c71e8ba99cb3 | -17.40086 | -47.33554 | 2026-07-10 00:18:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2bfd4cc5-d878-3232-b733-18178bb52d1e | -21.45642 | -48.685 | 2026-07-10 00:18:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b973cb3c-eb8c-361c-8623-9a6a53ea2a4a | -23.56306 | -47.5147 | 2026-07-10 00:18:00 | TERRA_M-M | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.6 |
| ebaabe93-ad94-3f41-b260-95ac97de0fad | -23.60545 | -53.01425 | 2026-07-10 00:18:00 | TERRA_M-M | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 191.5 |
| a8b08712-088a-3db3-acb2-b80007a604b7 | -12.5003 | -43.7621 | 2026-07-10 00:20:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 8b9fb9b9-4efd-32e8-a949-63f9aa225a20 | -8.4987 | -48.0594 | 2026-07-10 00:20:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 155bd0e4-8e46-333f-95c8-aedb260ddef8 | -18.0381 | -54.3681 | 2026-07-10 00:20:00 | GOES-19 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 381c992d-d73b-3a98-8b7f-863e1bdb069e | -10.1478 | -50.167 | 2026-07-10 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 1d7519cb-0840-3cd0-aa70-24104f611516 | -8.0367 | -47.4219 | 2026-07-10 00:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 1c8c5e28-dbb6-3910-a8dd-43b61d4195cd | -4.3402 | -47.7645 | 2026-07-10 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 1b817dc0-e3ce-3d09-b889-0545c5715ab7 | -12.3561 | -47.413 | 2026-07-10 00:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 8a901a6c-b2f2-3e0f-9922-7d29c67ce6e8 | -10.60441 | -46.56468 | 2026-07-10 00:20:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 97464aab-768e-3697-b599-f1c604a7a581 | -10.69703 | -49.60231 | 2026-07-10 00:20:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b9266085-7ef3-3197-a2ff-b11b8d59ba2f | -8.03377 | -47.42739 | 2026-07-10 00:20:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 33.4 |
| a76ffadb-5bcf-3943-8530-21d897527bfa | -8.13568 | -47.86363 | 2026-07-10 00:20:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c27e05f2-2e56-3830-8e78-2af52af2910b | -10.60543 | -46.55385 | 2026-07-10 00:20:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| ad4cbdbd-b6ce-3bda-a19a-fd59dc5aa111 | -8.12276 | -47.87205 | 2026-07-10 00:20:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 1fb65b12-71f6-3669-b7e5-ff6631abbb1c | -10.14022 | -50.16659 | 2026-07-10 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 2ad89fa3-9adb-33cc-aa06-da46bd96a7e0 | -11.85225 | -48.24872 | 2026-07-10 00:20:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 52cd09a4-6c5d-3417-aaba-d265bef1a671 | -10.14799 | -50.15557 | 2026-07-10 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| cf2a7b43-77df-3c38-b01f-1ab780056ae0 | -9.57168 | -49.09867 | 2026-07-10 00:20:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8adf66b4-56c9-3b83-a020-4edbeebfbccd | -10.60785 | -46.56973 | 2026-07-10 00:20:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| ccf1d9ff-369c-302c-a236-80dc85b002f5 | -10.40252 | -49.44005 | 2026-07-10 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 571ff7b0-737c-3f37-924a-4a10f2ae0b20 | -6.58871 | -51.69793 | 2026-07-10 00:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| ba734459-f852-3118-a8a9-766a8c400025 | -8.13782 | -47.87753 | 2026-07-10 00:20:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| b9d33448-76ed-3c93-bbd8-4c6ee7fee6e7 | -10.69848 | -49.61245 | 2026-07-10 00:20:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 95d28beb-9253-3296-acc3-c74aee4c07b6 | -9.2667 | -47.28464 | 2026-07-10 00:20:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 151180b1-3d9c-3e45-852c-0176248ba839 | -10.14659 | -50.1459 | 2026-07-10 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 65fa26ae-175b-3790-8505-2f18f9f94ca5 | -12.46211 | -49.58587 | 2026-07-10 00:20:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 06300170-c8fb-3860-a4a7-fed952839022 | -8.71761 | -47.83581 | 2026-07-10 00:20:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 018acd11-1a63-3717-9bdd-4c053f830642 | -11.27575 | -55.78217 | 2026-07-10 00:20:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ed1eeb4f-d526-3b13-b4e1-52f3ac09eac8 | -11.83053 | -48.24017 | 2026-07-10 00:20:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0cd8bfec-06d1-3f87-a6ea-9796995aff86 | -11.27738 | -55.79544 | 2026-07-10 00:20:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 319523cf-ca83-38a8-9c36-347c55181d8d | -8.03146 | -47.41199 | 2026-07-10 00:20:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 255fb900-3033-30d7-baf0-3e8edc9ea39a | -12.35136 | -47.42102 | 2026-07-10 00:20:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 9f1544bf-2fbe-3bf9-b4a7-c106433e7bc5 | -12.6994 | -45.46305 | 2026-07-10 00:20:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 22717084-5312-3889-a9dc-6d0810f4e4c5 | -9.16501 | -50.88601 | 2026-07-10 00:20:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a9854299-1ad7-31ed-99c7-330641b91a60 | -9.16631 | -50.89522 | 2026-07-10 00:20:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 0cd78326-6501-3e61-ba36-9959b918c9fc | -13.37121 | -54.36702 | 2026-07-10 00:20:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 66fb137e-4cdf-3300-8b80-49d5dd6d1578 | -10.32889 | -50.06677 | 2026-07-10 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 93485e15-04a4-361e-902c-fc82852eb4ea | -11.84053 | -48.23867 | 2026-07-10 00:20:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a4870c92-4eb5-3573-830b-74df9252307d | -12.45149 | -49.57753 | 2026-07-10 00:20:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 35.1 |
| aff04f60-3649-38cf-be3c-09843dfb1b02 | -10.38244 | -52.15848 | 2026-07-10 00:20:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a0c297d2-25fe-3c39-b2ea-6b155b43fde6 | -8.49802 | -48.0676 | 2026-07-10 00:20:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 4ba9005b-f870-35ba-b41a-a587dbf739b2 | -9.5733 | -49.10971 | 2026-07-10 00:20:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0042b7c4-1141-3901-bde9-2a701e367c9e | -10.14161 | -50.17624 | 2026-07-10 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 723f0dbf-053a-3b26-bc64-8bc37364565a | -8.13569 | -47.88428 | 2026-07-10 00:20:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 246b3879-e96c-391f-8a65-657132fddb8b | -7.90875 | -55.42634 | 2026-07-10 00:20:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| e90ddcfd-43ef-37be-a409-1eeb9390f3f2 | -12.49649 | -43.75945 | 2026-07-10 00:20:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 5271746c-7c05-3bde-b518-3f34c516b19b | -8.72843 | -47.83424 | 2026-07-10 00:20:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 74eb4081-88b8-3ea6-9802-ab66943d4927 | -14.15022 | -52.88345 | 2026-07-10 00:20:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 2a65e879-6df9-3312-8bcc-2a44439a46ef | -10.13605 | -50.19326 | 2026-07-10 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 9b2a52c7-2d57-3616-a764-90e1688ec0a1 | -5.46746 | -45.42029 | 2026-07-10 00:20:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 7dacdaed-41fb-3946-9c5c-3163eb9e698a | -12.35985 | -47.40628 | 2026-07-10 00:20:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 687dd0af-8551-36b1-98b7-f441115ea184 | -9.80361 | -53.32026 | 2026-07-10 00:20:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6c6dedf7-6acf-328d-887b-f00820d67bda | -10.13468 | -50.18362 | 2026-07-10 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 1588ec57-3b64-3895-ad90-5e2383d9a303 | -13.30556 | -43.73112 | 2026-07-10 00:20:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| b31c5e46-c643-37ca-9ce2-1e7997691778 | -13.37271 | -54.37864 | 2026-07-10 00:20:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 3f8120fe-adde-3755-9c25-259a5021f46b | -8.13365 | -47.87037 | 2026-07-10 00:20:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| f1be3fe9-f3f6-3b9e-89cf-5fa612aa86e0 | -10.85684 | -45.04645 | 2026-07-10 00:20:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 25.7 |
| e19835ab-7d6c-3815-805f-6d83e207856f | -12.37175 | -47.8862 | 2026-07-10 00:20:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5e3d1980-a854-359f-a53e-b29a7726a8a4 | -10.14301 | -50.18587 | 2026-07-10 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 67c03f86-1b7a-3380-bfba-4dc9afd6de84 | -13.31927 | -43.72865 | 2026-07-10 00:20:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 61e1d233-4eb0-398e-b297-5fcf1fe61474 | -10.15576 | -50.14453 | 2026-07-10 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4630632b-ee8e-39fa-a7d1-9d19ec599463 | -12.5006 | -43.78374 | 2026-07-10 00:20:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 94759a08-feeb-3079-bab9-b9d45978b7d2 | -10.98817 | -49.39814 | 2026-07-10 00:20:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| eb722436-9dbf-3c0b-b0d2-eb186024582b | -10.13332 | -50.17397 | 2026-07-10 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 61d6ba90-05f8-3695-b991-140d39477383 | -12.66867 | -48.22833 | 2026-07-10 00:20:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e9c72121-752a-3429-987f-86a8e717a322 | -10.68767 | -49.60371 | 2026-07-10 00:20:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 38295902-2b82-3545-b566-78eec4207ca7 | -10.15716 | -50.15419 | 2026-07-10 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 80fd1cd1-c59b-3e4b-a0a9-2df2720964a1 | -6.66854 | -47.52594 | 2026-07-10 00:20:00 | TERRA_M-M | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 12bba919-c5ef-33a8-b645-b6b116406979 | -13.37264 | -54.37279 | 2026-07-10 00:20:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 6605f3ee-b4b3-30b4-a321-81534cc4f11f | -12.36184 | -47.41925 | 2026-07-10 00:20:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 29.7 |
| a83222f9-23b5-31bf-ada3-8acfe0ec5a47 | -12.71152 | -45.46107 | 2026-07-10 00:20:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 01ecdd2d-f689-32f2-8785-50c683e76799 | -7.90828 | -55.4327 | 2026-07-10 00:20:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 001f38b6-9831-30e3-8d18-636f4a0ad37f | -9.269 | -47.29946 | 2026-07-10 00:20:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 26076be7-535c-3e89-b4b1-ea3ea27c2cc7 | -10.40404 | -49.45033 | 2026-07-10 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 04aa2d0c-4aa0-3571-9d67-0b783a4aa6b5 | -13.36128 | -54.36837 | 2026-07-10 00:20:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 2d69484d-e2dd-3c1e-9fc7-898b1aae16e6 | -12.37355 | -47.89827 | 2026-07-10 00:20:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| db916e9e-6df7-3dbf-9b25-59bb880da3e9 | -5.4624 | -45.42632 | 2026-07-10 00:20:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 571087fc-e2da-3eb6-a71c-244ed8ac1daf | -10.32749 | -50.05706 | 2026-07-10 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| b4943cf8-99c1-39f4-8672-979ef6094be7 | -10.83041 | -49.38173 | 2026-07-10 00:20:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| df5ee401-4989-3b77-a7cc-6ef56c9a1a13 | -12.45293 | -49.58734 | 2026-07-10 00:20:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 1342029e-474d-31a3-8c90-3738ab522375 | -11.47994 | -52.92265 | 2026-07-10 00:20:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9a2576ce-83d7-30a2-944c-d7cb1b1887de | -8.50871 | -48.06607 | 2026-07-10 00:20:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| f6e24a5a-6ac1-36c6-92a2-21eb259bc3f9 | -9.56074 | -48.67667 | 2026-07-10 00:20:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| db5517e1-143b-334c-8a15-64814e8c314c | -10.68912 | -49.61382 | 2026-07-10 00:20:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7652f42d-663c-3df9-b499-af98055b74f0 | -12.34936 | -47.40804 | 2026-07-10 00:20:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| a0b37e9a-32f9-3e4e-9ce8-bf30e01607c1 | -4.33704 | -47.76238 | 2026-07-10 00:22:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 7ee078ea-f78f-3125-ba3a-e03d5b755a31 | -4.94685 | -48.24892 | 2026-07-10 00:22:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 80506e92-93ba-3506-ae72-828b5d43bc8f | -4.1583 | -54.99171 | 2026-07-10 00:22:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 09faa106-e0af-3742-a1d8-fd9654885b8e | -2.80103 | -48.58987 | 2026-07-10 00:22:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |


[Clique aqui para ver as próximas entradas](README3.md)
