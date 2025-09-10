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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7827ea3d-9bb3-3d35-890c-bfee9d561cdb | -6.3974 | -43.50781 | 2025-09-10 03:21:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c945008f-3bfe-30aa-a699-a44b822fbae6 | -5.93966 | -42.78226 | 2025-09-10 03:21:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e8367e0c-e75b-3283-9d8a-ec96c4d49494 | -6.04963 | -43.1218 | 2025-09-10 03:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 06b8ec30-8456-350f-b3db-2354e3d38294 | -5.66968 | -43.35863 | 2025-09-10 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5328b525-0b9f-393a-8613-cc2f40d914bb | -5.6729 | -43.34862 | 2025-09-10 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1673f9c7-86d8-3a31-ab5d-02fe901b2da3 | -7.55529 | -44.66032 | 2025-09-10 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3b467f59-cbf6-3f09-89f1-646a3a300823 | -6.20513 | -43.35771 | 2025-09-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a4c3c602-2677-3c2f-acf5-002f6e5cfa18 | -4.54322 | -43.30751 | 2025-09-10 03:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bda07fbb-7933-3721-bb41-872fdf5b4af5 | -6.16406 | -43.38056 | 2025-09-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d666e3f3-206c-36f7-af15-0d84cc02fbc5 | -7.72144 | -35.13493 | 2025-09-10 03:21:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f4ed01cb-c900-3196-815e-69701cf985fb | -6.25792 | -43.41164 | 2025-09-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 8b062b3b-02bd-3a35-a09d-b5387a572617 | -4.09429 | -41.57402 | 2025-09-10 03:21:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| f66d153e-51ef-37db-9b33-55e453589f16 | -5.66893 | -43.89833 | 2025-09-10 03:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c314f35-2134-3529-b1f2-8539bd45c95c | -5.67061 | -43.36081 | 2025-09-10 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 57e9bef6-9547-32fe-81de-a52dba08c1ec | -6.05659 | -43.14193 | 2025-09-10 03:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4cff65cb-9484-389d-a487-9a8dca23be65 | -6.24329 | -43.41507 | 2025-09-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 72ad306c-43d7-309f-b264-c0a9fc772fe2 | -5.66282 | -43.35773 | 2025-09-10 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f2c5506e-e05f-3b86-a4f5-8c87e164e582 | -6.21007 | -43.35804 | 2025-09-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 18c0667f-53ba-3ef6-947f-4efbef8d86f7 | -6.19411 | -41.04644 | 2025-09-10 03:21:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 01eb262c-ef4f-3e75-b7b9-05d79fc3c905 | -5.67124 | -43.899 | 2025-09-10 03:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35a4823a-6b37-3cd6-8065-3c67ce146b61 | -7.25529 | -44.46288 | 2025-09-10 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d4dc8437-326e-3625-a0d4-6122c7eecd48 | -6.24106 | -43.42706 | 2025-09-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f13eb9d8-2c7d-35a3-9ab2-2b8972885b56 | -7.54685 | -44.6657 | 2025-09-10 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0b64ad63-bfdf-3aba-b4c6-460773271618 | -6.05401 | -43.13527 | 2025-09-10 03:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.2 |
| fe0eeb0a-75c6-3f23-a5c5-c538c806d957 | -5.79429 | -43.88645 | 2025-09-10 03:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b27e2490-58de-31b2-b3a0-ab135b624efb | -7.54381 | -44.66378 | 2025-09-10 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b4dae4f0-a25f-37ef-a197-e28493b59b1e | -5.66604 | -43.34771 | 2025-09-10 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e22a405d-bc37-383e-9d01-92e7e02f2c2f | -6.1821 | -41.05498 | 2025-09-10 03:21:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e439527a-e601-3375-9925-8cb14bc95611 | -6.20471 | -43.50883 | 2025-09-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1861f68d-1250-3c8f-84f9-dce360e48421 | -5.79146 | -43.89138 | 2025-09-10 03:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff59d708-af3b-3ca3-8b8f-e7c68b699173 | -6.31451 | -43.41892 | 2025-09-10 03:21:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6fe8387c-2c0d-315d-bf14-c21e33931002 | -6.05772 | -43.13559 | 2025-09-10 03:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ac024ea0-a398-3795-8ded-1f4161fe2f5f | -6.31976 | -43.41753 | 2025-09-10 03:21:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c240ba38-a0cb-3fc7-8d15-dfab8eae7aa5 | -6.15724 | -43.37959 | 2025-09-10 03:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b0d25216-1db5-349b-9424-53d5d8eab686 | -5.66062 | -43.90384 | 2025-09-10 03:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47cb0ae3-cd21-341e-8c21-db1da77a06db | -4.09781 | -41.57514 | 2025-09-10 03:21:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4f682d99-b8f3-3f33-b20d-43f0b02bfeed | -7.42511 | -40.08341 | 2025-09-10 03:21:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cb923222-ebc3-3746-9685-b6e46e2cca02 | -10.59773 | -43.30433 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39d058fc-6fef-3c87-905f-de25e00c9518 | -11.45084 | -43.62121 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 42230e37-a2b9-3b20-8497-239352b4e770 | -11.43477 | -43.58792 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d079911d-dbde-3419-b914-f6aa05ecda61 | -11.12088 | -45.12267 | 2025-09-10 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4cfbddb0-e087-3801-869a-94b46dfa05c7 | -11.45709 | -43.62269 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bb7d904f-135d-394e-a6be-991498abb87a | -12.01732 | -45.86129 | 2025-09-10 03:23:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b7edd1e-8065-39b4-8a28-28ddaf94e107 | -11.42327 | -43.58005 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca1f739c-7381-3f0a-a44a-a9fcea338f2b | -11.43816 | -43.6372 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c518883e-437d-38f6-8c55-81192e2c7699 | -11.41699 | -43.57877 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e248cbb-4fb1-31ad-b469-2ef98de621fa | -11.56651 | -44.66285 | 2025-09-10 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c425ccb4-0012-3a0d-82e1-c01b292372f8 | -11.41948 | -43.58251 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 112732a7-2834-3c5a-b148-94661c7e23e0 | -13.00022 | -45.21346 | 2025-09-10 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58ce6e06-e61a-38c7-adf9-ccfda9afd0d6 | -11.44565 | -43.6145 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0a3acf6-3988-3d8c-9678-ceee0a16a8b3 | -12.02585 | -45.85581 | 2025-09-10 03:23:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4826cbfa-5b8d-3fc3-bf28-f9edda668d00 | -13.14801 | -45.28708 | 2025-09-10 03:23:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2efb1c03-41eb-3964-a9aa-657a197c2bd5 | -11.42056 | -43.57727 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74decd5c-276e-3e36-90c6-2916cb4a13b3 | -13.00155 | -45.20734 | 2025-09-10 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4d2d355-4a81-39e7-bf25-a9551c218149 | -13.19099 | -45.2832 | 2025-09-10 03:23:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7b752f42-40a2-359d-a871-0114e83e41d7 | -11.42985 | -43.62774 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 12a0921f-43a5-3687-89c4-a404d295b112 | -11.56775 | -44.65687 | 2025-09-10 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f9ee2f8-0528-3770-83f4-a78953593827 | -13.53908 | -44.13951 | 2025-09-10 03:23:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56c7b7fc-9e82-3a58-b9e2-254926094082 | -11.42467 | -43.58908 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44ef7e09-0b5d-30a3-9ec0-d7f28fd3a810 | -11.4623 | -43.62928 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 552aeb69-5294-33b4-b91b-a3526bc0d5d4 | -12.13945 | -44.84075 | 2025-09-10 03:23:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fc26409-ca1c-3768-b60b-1e5b23cf3ee2 | -13.00502 | -45.21234 | 2025-09-10 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 38ac43e9-7721-3f2f-b4a4-0d24fce33015 | -13.78888 | -46.29248 | 2025-09-10 03:23:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7da2d9e6-628f-345e-b5b7-0e0ba9ba7c4d | -11.42849 | -43.58669 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef5c61e4-a1a8-3c8f-8481-dca65efc8dae | -13.78719 | -46.3001 | 2025-09-10 03:23:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fea1f4a8-eae0-3ec5-961d-3e4b1c3d42cb | -11.39266 | -43.53716 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f01203b7-bf8a-31b7-80ac-696f17ced850 | -13.19995 | -43.37778 | 2025-09-10 03:23:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 406905df-48ae-303e-9127-9f969e95efce | -14.59898 | -43.92867 | 2025-09-10 03:23:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0575e17a-2435-3c86-91a4-8c01caf00b1f | -11.43403 | -43.63942 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b85742d3-b89d-3231-9c20-b8337a819921 | -11.44127 | -43.62132 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4697b147-1f70-32d3-bbaa-5069dbf7e625 | -11.43272 | -43.59831 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f344a111-570f-3bc6-888b-bbd207edce95 | -13.14615 | -45.28664 | 2025-09-10 03:23:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f928023a-81c8-3143-bbd6-7cf963f98d78 | -14.598 | -43.9334 | 2025-09-10 03:23:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 49242743-e5e9-3e1b-8189-85bdbc519bb0 | -11.45502 | -43.6329 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| aef1adfe-f380-3d05-8c9d-2ce8ac6ea4fd | -11.87675 | -40.95154 | 2025-09-10 03:23:00 | NOAA-20 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1ef628b3-d820-3037-9c95-a591ca084e6f | -12.41489 | -44.71887 | 2025-09-10 03:23:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5a8354db-0cc5-3ff3-a4e6-8aaafbbc6b28 | -11.87609 | -40.95496 | 2025-09-10 03:23:00 | NOAA-20 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8b8b1528-721c-3eac-beec-0ee8940393b6 | -11.43375 | -43.59313 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c5de6343-0b9d-3458-9188-fa36699d0af8 | -11.44032 | -43.64072 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 410e6f8f-5bcc-33c6-9ac2-3c6778459728 | -11.43096 | -43.59032 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a12dd26a-3f39-32b0-b27b-f4dce7c0ae69 | -11.12134 | -45.11821 | 2025-09-10 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 032ff332-01c7-3f61-b4b6-c77dbf3c209a | -12.13815 | -44.84688 | 2025-09-10 03:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fccae18d-f9e6-3b66-a6a3-2c45569508e7 | -11.45605 | -43.62778 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c173b236-5a93-32c4-8381-b91152afbb27 | -11.4351 | -43.63418 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79429459-4598-3a37-b204-ba429e38b113 | -12.02215 | -45.8567 | 2025-09-10 03:23:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 99f2c42a-4095-3aa4-80c5-d5b544eca1c7 | -11.46125 | -43.63446 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 9192dda6-1374-363d-a091-e8159b41d7c4 | -11.43901 | -43.59956 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5add1bd4-3a6d-3549-87fb-a44e5938c804 | -11.4404 | -43.60814 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2016087f-a983-306d-891e-0e9129c0624b | -11.4362 | -43.59668 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 214e17c0-e8d3-32cc-90a0-25ff86b3ae4f | -13.79089 | -46.29807 | 2025-09-10 03:23:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 27644796-0039-31d8-9f0c-a57dae1a131f | -13.54012 | -44.13452 | 2025-09-10 03:23:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d212570-16d0-3e7a-981e-f347b847908f | -11.4446 | -43.61967 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c375d59-c56c-33ff-92c1-313ebd0cace8 | -13.1923 | -45.27705 | 2025-09-10 03:23:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c12980d2-79e8-3912-b16c-efd0b15fb036 | -13.82421 | -43.86724 | 2025-09-10 03:23:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79d3be0a-c6a2-357e-90ef-9f59b9394c18 | -11.46021 | -43.6396 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1aab6730-0e7f-3a3a-9a9c-b53b082c6111 | -11.41171 | -43.57247 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c483486-f3f8-3dcc-aeae-0e1b23dcf249 | -14.53353 | -42.48036 | 2025-09-10 03:23:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 69ae9c7f-f884-38b2-819f-b7c35eb411b3 | -11.42221 | -43.58539 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee6525d3-317b-3374-8435-c9e8c6a38693 | -11.4498 | -43.62632 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5b1bd6c8-3f4d-34d4-b114-677fabfe08f9 | -11.41427 | -43.57606 | 2025-09-10 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README16.md)
