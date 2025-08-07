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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be3a6f81-a936-343f-958c-7ae35219a191 | -9.0685 | -45.0579 | 2025-08-07 05:48:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ef925d86-139f-3e91-9da5-e16f932934a8 | -11.75818 | -48.18683 | 2025-08-07 05:48:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| b87a3ab5-72fa-3321-b420-f394560bff85 | -12.70479 | -46.38745 | 2025-08-07 05:48:00 | AQUA_M-M | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 2bf2ed09-8f3d-38c1-9167-7637d78ce9c4 | -10.6348 | -44.76368 | 2025-08-07 05:48:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 02387cbf-87e3-3515-bff7-593e8bd5cb59 | -10.639 | -44.73449 | 2025-08-07 05:48:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 5331f004-0534-392d-8b19-18c30d05126d | -10.64538 | -44.75529 | 2025-08-07 05:48:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6d28b090-09c1-3dd7-9b52-adc47089e425 | -10.43905 | -44.39462 | 2025-08-07 05:48:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 152ea1cb-8788-35c1-9372-c8518079baea | -9.64945 | -43.84928 | 2025-08-07 05:48:00 | AQUA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 0e318b8d-894f-3c8e-81d5-059f5ac1c11a | -10.62562 | -44.76236 | 2025-08-07 05:48:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 41.2 |
| e61cfa40-6154-3c2e-b1f7-b51134ff5d7b | -10.6376 | -44.74422 | 2025-08-07 05:48:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 169.2 |
| faec8884-f95a-36fe-9db7-62a75ad41381 | -9.46401 | -40.38806 | 2025-08-07 05:48:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 30.8 |
| 6f106d70-c01b-3160-b556-c5467c5428fc | -10.79526 | -46.49139 | 2025-08-07 05:48:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8ff548c0-aa48-386b-bf17-02d58a58083e | -12.70346 | -46.39648 | 2025-08-07 05:48:00 | AQUA_M-M | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e23f8d4f-8688-3c75-97a1-d2a41e5d6b85 | -12.71497 | -46.37973 | 2025-08-07 05:48:00 | AQUA_M-M | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a80c1aee-373c-3ba2-9c17-a3d71ca66dc6 | -9.46398 | -40.36247 | 2025-08-07 05:48:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 30.7 |
| 5bef7e11-bf11-3439-9013-4d1f9aacee56 | -8.51981 | -43.29336 | 2025-08-07 05:48:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| ca1c65c5-aa2b-34a4-ab15-c667a4145133 | -10.6438 | -44.7645 | 2025-08-07 05:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 6a646437-f348-3707-ac10-79eba55d9279 | -8.9213 | -60.7489 | 2025-08-07 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 8859d818-7165-381a-98c9-1dd696350e01 | -10.625 | -44.7439 | 2025-08-07 05:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 8d6ba941-af5f-3840-82ae-feb4ffb93c48 | -10.6441 | -44.7413 | 2025-08-07 05:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 196.4 |
| 9cea0317-96ee-391e-a43a-b12df90ad9ac | -8.9215 | -60.7297 | 2025-08-07 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| f80b2e26-1bad-3246-832c-495a41b2e73c | -10.6247 | -44.767 | 2025-08-07 05:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 40a6a754-2336-3d6f-b7a9-fd08aaf2a15c | -15.74154 | -43.39679 | 2025-08-07 05:50:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 056ec774-cc7a-32a9-a654-97058048c310 | -15.74743 | -43.38907 | 2025-08-07 05:50:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 47.0 |
| b0297c0a-ee75-3b57-a15d-f6bcc2eb3354 | -15.74339 | -43.38288 | 2025-08-07 05:50:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 2f66b6c8-b977-385e-8c2b-a0a248b38af7 | -10.625 | -44.7439 | 2025-08-07 06:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 3de4e53a-c62f-3056-b4c0-c4bea3be827f | -8.9213 | -60.7489 | 2025-08-07 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| e40f42cc-0303-3706-9a46-c42d4e534ab2 | -10.6438 | -44.7645 | 2025-08-07 06:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| cfc222bd-56fa-3962-81ca-ff63bc6ebee1 | -10.6441 | -44.7413 | 2025-08-07 06:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 3a136470-259b-3e61-bd0a-24410e2a84cb | -10.6441 | -44.7413 | 2025-08-07 06:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 140.7 |
| ff591458-6e28-31a0-a43a-64a9dd22cfbc | -8.9215 | -60.7297 | 2025-08-07 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 95109031-2334-38cf-9c51-3fa26d9cab7f | -10.6438 | -44.7645 | 2025-08-07 06:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 93c30cb5-829b-37df-af7d-4f07b2dfc2fa | -7.4074 | -60.0108 | 2025-08-07 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| bc0d45a3-eb43-3937-bf02-08a34af2c5f2 | -8.9213 | -60.7489 | 2025-08-07 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 2dd9a780-1430-3111-aa3a-12551cbb2ca7 | -10.625 | -44.7439 | 2025-08-07 06:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 14ac20f7-76e0-3d9f-bb85-ef98a619f2d6 | -8.9213 | -60.7489 | 2025-08-07 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 5d651e0a-e8c2-31b9-aeaf-04e587996f7a | -10.6438 | -44.7645 | 2025-08-07 06:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 4934dc29-503c-3ad4-9bc3-b93a42139319 | -10.6441 | -44.7413 | 2025-08-07 06:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 111.2 |
| e641bbea-eb10-34ef-b734-afe3abf4395f | -10.6247 | -44.767 | 2025-08-07 06:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 56.2 |
| c0ef1930-8eaa-3c2c-b9ca-452387440c60 | -10.625 | -44.7439 | 2025-08-07 06:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 54.8 |
| d865e276-1444-3e08-a6e6-fd9fd21895ab | -5.8218 | -46.2258 | 2025-08-07 06:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 8012b88d-e7a5-350d-b8dc-f823fa62482b | -7.4074 | -60.0108 | 2025-08-07 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| c2325449-299c-3f72-806a-35c7f6c14c0b | -10.6438 | -44.7645 | 2025-08-07 06:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 524c5747-ab5e-37b7-871d-5a0f5e7711e1 | -10.6441 | -44.7413 | 2025-08-07 06:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 140.6 |
| b0b992e3-ade6-3b4d-98cc-9d114c7d770d | -8.9213 | -60.7489 | 2025-08-07 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 92517545-2a5b-3b4c-8327-4d2a0cb7497f | -6.0784 | -44.6961 | 2025-08-07 06:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 437b5b1c-6913-36ad-b785-d31386bad1dd | -7.4074 | -60.0108 | 2025-08-07 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| b7a47a55-5f41-3969-85f5-a3403de303d1 | -5.8218 | -46.2258 | 2025-08-07 06:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| ae486868-05e4-366a-9449-3e702e6b771a | -8.9213 | -60.7489 | 2025-08-07 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 0314cff7-857c-3481-9a8c-a0d1e80bd38c | -10.6438 | -44.7645 | 2025-08-07 06:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 225c2219-df1c-3a27-99cf-42d960a4d566 | -6.0784 | -44.6961 | 2025-08-07 06:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 7345d377-d42c-38f8-909a-d542e4ec70d5 | -10.6441 | -44.7413 | 2025-08-07 06:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 58e04e69-b835-38d1-84f3-d241d178d2de | -10.625 | -44.7439 | 2025-08-07 06:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 61.3 |
| a9ccd637-3947-3bcd-9e4c-92010889f1b1 | -10.625 | -44.7439 | 2025-08-07 06:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 58.4 |
| f5a8eb84-5e20-39da-9490-2961fc75e869 | -6.0784 | -44.6961 | 2025-08-07 06:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| eedab046-137c-3c6b-9e43-36087ca0bd97 | -10.6441 | -44.7413 | 2025-08-07 06:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 7b61903c-7a14-357c-ade3-bc52d76dc952 | -8.9213 | -60.7489 | 2025-08-07 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| d8b47152-8120-3eda-a68f-3d36773b7308 | -10.6438 | -44.7645 | 2025-08-07 06:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 0f0cb2f9-f06d-3f8a-9118-37bd14650be0 | -10.6438 | -44.7645 | 2025-08-07 07:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 2a82bc84-47cb-3b6d-825d-3c72e55d5e70 | -8.9213 | -60.7489 | 2025-08-07 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 55f4e53d-5e0b-3880-9a65-1a9f7fc6d453 | -6.0784 | -44.6961 | 2025-08-07 07:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 63cfcaea-f411-3cd7-b337-5375279c1992 | -10.625 | -44.7439 | 2025-08-07 07:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 8c167be6-8021-3c11-bb7c-1a8c3869d291 | -10.6441 | -44.7413 | 2025-08-07 07:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 68b666b0-7e3c-359b-b85e-e1cd0c821dc0 | -7.4074 | -60.0108 | 2025-08-07 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 7454c821-7672-3b37-a383-2d962480d72c | -10.6438 | -44.7645 | 2025-08-07 07:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 17317cf4-28cc-3da6-9d2a-9b0ce6df777e | -8.9213 | -60.7489 | 2025-08-07 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 1a34ad1d-ba2b-3465-9843-52296f222b6f | -10.625 | -44.7439 | 2025-08-07 07:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 50.0 |
| d3f1a43a-5cf5-389c-a60f-4a1e431a5a25 | -6.0784 | -44.6961 | 2025-08-07 07:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 55c2c210-167a-3343-af79-e0f6c0d9849b | -10.6441 | -44.7413 | 2025-08-07 07:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 5b6e8641-7eee-37e1-af8b-049e4ef4e25a | -6.0784 | -44.6961 | 2025-08-07 07:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 956ccad0-c373-3064-af5d-711316459124 | -10.6441 | -44.7413 | 2025-08-07 07:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 599ee220-1321-3f2b-bdfd-05bacea300d4 | -10.6438 | -44.7645 | 2025-08-07 07:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 93fb6021-0ad0-358d-a75f-79984f93dc6c | -8.9213 | -60.7489 | 2025-08-07 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| e62cfb6d-e04c-3c18-a5e2-3e2421cd56b8 | -8.91341 | -60.74936 | 2025-08-07 07:26:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 709caf98-6dbe-3140-99a7-ea2ad43c45d6 | -8.9266 | -60.74664 | 2025-08-07 07:26:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 37.0 |
| e15d5032-913d-3754-8f94-a223ad782be1 | -8.9095 | -60.74478 | 2025-08-07 07:26:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 37.3 |
| ef69f411-465a-3ca5-bc49-376893ce9eca | -10.6438 | -44.7645 | 2025-08-07 07:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 54.5 |
| cb600370-7579-3be1-bd76-001b1d95afa6 | -8.9215 | -60.7297 | 2025-08-07 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| e799fb51-8f0c-3aa8-a322-c281b7bd8a60 | -8.9213 | -60.7489 | 2025-08-07 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| f430afd1-8569-3b45-9ccd-ebbecd2e93c7 | -10.6441 | -44.7413 | 2025-08-07 07:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 54da0f47-37d1-33bf-a2cc-8ae66a72e3c2 | -10.6441 | -44.7413 | 2025-08-07 07:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 094b3a1d-052e-321a-aa08-bfd6a4f6dc4d | -8.9213 | -60.7489 | 2025-08-07 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 86561be5-e285-3a30-9838-da0da225ffa1 | -6.0784 | -44.6961 | 2025-08-07 07:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 9467730e-81d1-3ddd-bb37-9cab72416e78 | -8.9213 | -60.7489 | 2025-08-07 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| b65e30d4-3e5d-3d27-beec-ed3eb81ad810 | -10.6441 | -44.7413 | 2025-08-07 07:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 46f95a18-9794-3802-9193-124b20234424 | -10.625 | -44.7439 | 2025-08-07 07:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 2349be3a-e578-3833-b559-7e0ad4f41f17 | -10.6438 | -44.7645 | 2025-08-07 07:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 7261a5e1-9c0b-379d-b53d-36a3e3ebc763 | -8.9213 | -60.7489 | 2025-08-07 08:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 1cb376a3-1800-36b8-b359-b49af46d4c33 | -10.6441 | -44.7413 | 2025-08-07 08:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 9c914896-52b2-3e09-8358-1e3a09805ddd | -8.9213 | -60.7489 | 2025-08-07 08:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 89d6c085-8b93-31e8-8c0f-4f3495248595 | -8.9213 | -60.7489 | 2025-08-07 08:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| d0567773-47f5-37af-bd74-d38e94e9ac6e | -8.9213 | -60.7489 | 2025-08-07 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 635a6b13-4bb0-35e7-b4b8-2a7a1a80e270 | -6.0786 | -44.6733 | 2025-08-07 08:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 2fb92895-e088-3de8-890b-490f8160a638 | -6.0784 | -44.6961 | 2025-08-07 08:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 3663a709-0e0b-374f-a732-fbbc64e12378 | -10.6441 | -44.7413 | 2025-08-07 08:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 62.5 |
| f4d6d95c-598b-348b-9461-64252f3b9074 | -8.9213 | -60.7489 | 2025-08-07 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 8d9e37a6-4cab-3b33-bdc2-a07d7cb2642e | -8.9213 | -60.7489 | 2025-08-07 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 41cd87e7-6cea-3afa-b167-5ad9e5701ca0 | -8.9213 | -60.7489 | 2025-08-07 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 75406e6b-80aa-32e7-8560-e6569d2ddc9f | -8.9213 | -60.7489 | 2025-08-07 09:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| dab5a807-ba38-38a3-9c22-41ddacacb380 | -8.9213 | -60.7489 | 2025-08-07 09:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |


[Clique aqui para ver as próximas entradas](README28.md)
