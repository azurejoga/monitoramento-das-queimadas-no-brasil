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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ba9da0d-0991-37e3-82a4-9f30a7c0a889 | -7.13573 | -42.65507 | 2024-10-09 03:21:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4d5fed7f-7a28-37ea-9d98-1aaa4adfc259 | -7.13031 | -42.64858 | 2024-10-09 03:21:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ed7d6a86-58f2-3af2-a110-2f28ae005a03 | -7.12931 | -42.65398 | 2024-10-09 03:21:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a978f660-2153-3c96-8871-65d7fbb17903 | -7.12391 | -42.6474 | 2024-10-09 03:21:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 194eb265-c022-339c-9ecc-d6323fbd04f1 | -7.12291 | -42.65281 | 2024-10-09 03:21:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c2a95300-524d-3f5c-80a3-d9fc78e40da9 | -7.10239 | -42.62095 | 2024-10-09 03:21:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ecb74abc-b7a7-3110-8845-20105d688083 | -7.10053 | -42.62315 | 2024-10-09 03:21:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ef075bf6-56b5-3330-861e-093138af78b6 | -7.09942 | -42.63676 | 2024-10-09 03:21:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6b756d9b-3662-3929-a631-b0c13be0aa85 | -7.095 | -42.62509 | 2024-10-09 03:21:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9fd05721-0c79-3fa7-9104-e8650064ba44 | -7.09402 | -42.63031 | 2024-10-09 03:21:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8022b651-8910-33f4-84c3-48a5b5bf463e | -7.09317 | -42.62727 | 2024-10-09 03:21:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 22304b0f-4e8b-357f-a92b-ef4da03a8b03 | -6.8377 | -42.81956 | 2024-10-09 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c82019da-d0e9-336f-a498-9b2c3a057a5c | -6.83691 | -42.82209 | 2024-10-09 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a253aa3a-f4f4-3d21-8914-cac37048bb9f | -6.83674 | -42.82487 | 2024-10-09 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d960e610-e95c-394d-8ca1-dfc5554c8c99 | -6.48088 | -41.9593 | 2024-10-09 03:21:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b38e961d-c6b1-366a-a1ce-d765b1211f61 | -6.47997 | -41.96428 | 2024-10-09 03:21:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 13765eea-374b-3f30-a5ee-3fe16783058a | -6.44192 | -42.93477 | 2024-10-09 03:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0fd5b492-be87-34d2-afde-3dde8bfa726b | -6.43723 | -38.83734 | 2024-10-09 03:21:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 848da6a5-9370-3bdb-bdaa-03c1ac15cf37 | -6.43667 | -38.84064 | 2024-10-09 03:21:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4bdf556a-5b9e-37ca-b2cf-6658e3dcd472 | -6.43315 | -38.83076 | 2024-10-09 03:21:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5dfe286a-0f56-3503-b758-a8f566741147 | -6.31505 | -43.38539 | 2024-10-09 03:21:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d5d1e5c-e53b-3806-ada1-09939f8fa034 | -6.31086 | -43.38034 | 2024-10-09 03:21:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1817b8b2-5d9a-3197-b768-bafa81046e01 | -6.30972 | -43.38639 | 2024-10-09 03:21:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 967c080c-8ae1-3832-bbfa-591e353edd43 | -6.3094 | -43.37793 | 2024-10-09 03:21:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2bfb4164-976f-3ecd-bb25-55a62abc012c | -6.30831 | -43.38398 | 2024-10-09 03:21:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 639eaffc-69c9-3547-8ca5-b5fe66f8e6a6 | -6.18118 | -42.60561 | 2024-10-09 03:21:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| eccbbaa3-02f7-37dd-ac3f-146fd71dae75 | -6.18015 | -42.6113 | 2024-10-09 03:21:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ddb9cd23-b3d3-3315-82fa-78a601746743 | -6.16464 | -43.7079 | 2024-10-09 03:21:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 844b89ef-1158-3943-a506-0e2fe14c3a9a | -6.16404 | -43.70718 | 2024-10-09 03:21:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ef64b932-bc5d-3e0d-a293-8f0354c180ed | -6.16348 | -43.71437 | 2024-10-09 03:21:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 856258bb-8b43-3475-86ea-0b1f3af220a7 | -6.16283 | -43.71368 | 2024-10-09 03:21:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 81efef69-d063-3ad8-8781-ceaad5f8347d | -5.97121 | -43.36323 | 2024-10-09 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 70ed71e5-32b3-32e0-8b50-51f1d932b47b | -5.97018 | -43.36889 | 2024-10-09 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c4ee3dbd-115f-3085-8f48-bde7b7433bd4 | -5.96336 | -43.36775 | 2024-10-09 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d842202d-bbc9-3494-8f4d-9535ee6e390b | -5.85014 | -43.75313 | 2024-10-09 03:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ee778aa-2cc4-31d6-8899-a9a5a4b8ba0d | -5.84316 | -43.75195 | 2024-10-09 03:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4b09218-5209-3067-b2c4-98a914e6e901 | -5.81749 | -43.2365 | 2024-10-09 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9c75493-cc95-3e21-ac82-147815a0f8f8 | -5.81585 | -43.23587 | 2024-10-09 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1111987-287c-3259-87d0-20cb275f0ee7 | -5.81475 | -43.24201 | 2024-10-09 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 465d9a3b-cca1-33d2-813e-36e9aebcfc1d | -5.81075 | -43.23516 | 2024-10-09 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd60404e-fd18-3052-aa45-f5fe8c567767 | -5.58577 | -43.25912 | 2024-10-09 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f3429354-aad3-31b7-9c9b-b2c3a655ba8a | -5.5846 | -43.25879 | 2024-10-09 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9a167312-34ef-3e47-bbbc-eb8a193ebfd5 | -5.57895 | -43.25807 | 2024-10-09 03:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cfce2483-b4ae-3eb9-84ca-3b5b08b8736a | -5.57777 | -43.2577 | 2024-10-09 03:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fc751465-6efd-389f-8867-cfcaed3bcf51 | -5.54585 | -42.93453 | 2024-10-09 03:21:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f2fadd0e-5e72-37e0-bde5-378a5f1cf442 | -5.49906 | -42.79264 | 2024-10-09 03:21:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 26004e9f-58eb-3425-942e-2d507d8820d7 | -5.49349 | -42.78563 | 2024-10-09 03:21:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 771104a7-6c64-3c75-921c-1944982a8a03 | -5.23315 | -43.81579 | 2024-10-09 03:21:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c3294444-549c-3cab-8e28-441ea456daaf | -5.23185 | -43.82277 | 2024-10-09 03:21:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b7c48374-22b1-3865-abe9-04628d62b359 | -5.22884 | -43.81575 | 2024-10-09 03:21:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 809754ab-3962-3b60-9658-9c1d79931ade | -5.22758 | -43.82273 | 2024-10-09 03:21:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a91e60f1-6478-3104-af1a-5d160f61a7b1 | -5.22619 | -39.93551 | 2024-10-09 03:21:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 483f2003-b264-3af1-805c-74822813e7ab | -5.22049 | -43.82161 | 2024-10-09 03:21:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef113655-2ca0-36c6-bdf0-e820b6cdad90 | -5.1661 | -38.09047 | 2024-10-09 03:21:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a561a7d5-6765-35d4-b893-c7021e03f6f0 | -18.58122 | -40.75789 | 2024-10-09 03:23:00 | NOAA-20 | VILA PAVÃO | ESPÍRITO SANTO | Brasil | 3205150 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f6bbb5f4-cec3-3b5e-afa4-f2a5fc5df3bf | -18.57891 | -40.75562 | 2024-10-09 03:23:00 | NOAA-20 | VILA PAVÃO | ESPÍRITO SANTO | Brasil | 3205150 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 06afa84c-66c0-3a19-bcdc-c5d3082a8fe0 | -18.44053 | -41.15704 | 2024-10-09 03:23:00 | NOAA-20 | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| b5cb11c9-c981-3d2f-ba00-59be10df0dc9 | -18.2469 | -42.23422 | 2024-10-09 03:23:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| dae6a727-bdb5-3bf1-86c4-35dbcad0e10c | -18.24623 | -42.23744 | 2024-10-09 03:23:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3f9df918-00dc-3e95-85f1-48ce8b395d1b | -18.24121 | -42.23584 | 2024-10-09 03:23:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9d3a3ca5-2e48-3ef0-8100-8e5de8db557d | -18.23976 | -42.9535 | 2024-10-09 03:23:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 86d33b3a-f227-330b-aae9-2123920393d7 | -18.23897 | -42.9573 | 2024-10-09 03:23:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 47bd6cd9-3f09-35c7-9d4d-4753e1e01ab0 | -18.23531 | -42.94797 | 2024-10-09 03:23:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7df65aab-c040-3f3e-8981-cdf9c8ef02e3 | -18.23446 | -42.95206 | 2024-10-09 03:23:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5af38bcb-a272-3c62-8b00-1f8a35f6d25f | -18.22914 | -42.95071 | 2024-10-09 03:23:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bd9897d0-b74a-3a77-b70c-f21cce0dc4eb | -18.18524 | -42.58549 | 2024-10-09 03:23:00 | NOAA-20 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 20a0e518-1f47-35b0-84a3-c5175c750d18 | -18.18454 | -42.5889 | 2024-10-09 03:23:00 | NOAA-20 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 270a870d-d28b-30e1-aad4-98664871965c | -18.1039 | -42.58121 | 2024-10-09 03:23:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 72789c96-173d-3191-bc41-6e38b380d6dc | -18.10316 | -42.58466 | 2024-10-09 03:23:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 973eee9a-92ae-3bf8-b58e-6de6048a8dcd | -18.09836 | -42.34783 | 2024-10-09 03:23:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 8f8b429d-bbc9-3ab3-8927-92646436e6ce | -18.06015 | -42.10957 | 2024-10-09 03:23:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 142493bc-1e4c-3cd4-8729-ee7f9b56b931 | -18.0595 | -42.11271 | 2024-10-09 03:23:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 87bb7e6a-8f84-3ab1-86a1-48e41e78e036 | -18.0073 | -42.13309 | 2024-10-09 03:23:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 87c3c6de-0b68-3d8b-8a9d-cf63fd6bb8c1 | -18.00657 | -42.13663 | 2024-10-09 03:23:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 5d5f604d-5adb-3dec-aa15-f40f32498689 | -18.00585 | -42.14006 | 2024-10-09 03:23:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| b3632c43-b445-3ef3-90f7-151d46a52470 | -17.89716 | -41.43603 | 2024-10-09 03:23:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f4e7dbd6-421d-39fa-9012-067d755a5066 | -17.89585 | -41.43399 | 2024-10-09 03:23:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6738a15e-9805-334d-8e1e-af772b6cbe95 | -17.89579 | -41.44271 | 2024-10-09 03:23:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 34c320e6-bea1-3d5a-9d1a-e0f9ce9e38b7 | -17.89462 | -41.44019 | 2024-10-09 03:23:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8978f0cd-eeeb-3dfa-8ba3-80250948d999 | -17.89326 | -41.44704 | 2024-10-09 03:23:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3da96020-5081-345a-9467-49ead661a6c1 | -17.89081 | -41.43367 | 2024-10-09 03:23:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| dd2ca5cf-43ec-33e4-ae2b-f8acf7cfb3ff | -17.87695 | -43.2922 | 2024-10-09 03:23:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0b9e2212-3cb2-3170-ac19-0a2091fe30d7 | -17.87624 | -43.29551 | 2024-10-09 03:23:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0b55aeb2-d894-36eb-a1b4-15a0a0a59afc | -17.87547 | -43.2991 | 2024-10-09 03:23:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 46298588-29d4-3663-a04d-b31b37b058ee | -17.87134 | -43.29145 | 2024-10-09 03:23:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6a2cd06e-efe7-3ed2-9103-49681e7902b4 | -17.86675 | -43.28596 | 2024-10-09 03:23:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54324978-934e-30a4-b67e-35272ca564a5 | -17.59823 | -44.5056 | 2024-10-09 03:23:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 224a4b03-1c56-3721-8ff1-4bcf52d22599 | -17.59512 | -44.50143 | 2024-10-09 03:23:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a7657b3a-0294-3a0c-9fa8-833d8bf1655a | -17.59389 | -44.507 | 2024-10-09 03:23:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ec1434db-29b6-3022-b266-0c2589579865 | -17.59225 | -44.50437 | 2024-10-09 03:23:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2e4e6a2f-cfee-3944-b9f1-e8bb16913dcd | -17.59101 | -44.51017 | 2024-10-09 03:23:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7c7ff0ee-5f69-3d01-9284-40db56ddf71f | -17.39237 | -43.42753 | 2024-10-09 03:23:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38a571ac-accb-3455-a4ba-ba1fedd98e23 | -17.39155 | -43.43148 | 2024-10-09 03:23:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3997c0af-8e7f-3c0b-a450-ddf3581c3966 | -17.38993 | -43.42545 | 2024-10-09 03:23:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03081f79-f515-3c7b-bdc9-a18f5456e99e | -17.38908 | -43.42937 | 2024-10-09 03:23:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 460486ef-c302-3d24-a61a-9d120175981d | -17.09925 | -41.19935 | 2024-10-09 03:23:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4d2d3ee0-ec12-3b05-8378-654f96a9fef2 | -17.09769 | -41.19843 | 2024-10-09 03:23:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7e6e8a0d-c288-3d1e-b5a6-ff8dc70151d8 | -16.65571 | -42.22566 | 2024-10-09 03:23:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a2b0e87-4663-3346-8b48-fd2f29502dff | -16.65428 | -42.22633 | 2024-10-09 03:23:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a26c81f0-b89d-3862-ac85-7481e649bcb7 | -16.65043 | -42.22456 | 2024-10-09 03:23:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README60.md)
