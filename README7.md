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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23073e4a-de67-36c4-a361-9fd885258d9f | -18.98994 | -48.42211 | 2025-07-27 03:49:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06c8fbb9-f235-3bfa-af4f-2cc4c0ec36fb | -26.02106 | -49.00755 | 2025-07-27 03:49:00 | NPP-375D | GARUVA | SANTA CATARINA | Brasil | 4205803 | 42 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| d91cc2ab-145c-32f1-91d6-529f6d46f35c | -26.01872 | -48.97614 | 2025-07-27 03:49:00 | NPP-375D | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 24fc133e-6a40-3711-a9a3-6f1135f80d52 | -26.01768 | -48.97613 | 2025-07-27 03:49:00 | NPP-375D | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 91261847-786d-3f7b-b2f8-cfc253bd5097 | -18.20703 | -44.62135 | 2025-07-27 03:49:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c7bfc51-2a68-36d4-8390-a68577e0616e | -18.98529 | -48.41678 | 2025-07-27 03:49:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59606db9-94ad-3011-8e20-ab8cc0b1cfef | -19.39079 | -44.3231 | 2025-07-27 03:49:00 | NPP-375D | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8b3f9ad-0026-3cc3-8694-d67bb4d5404f | -18.39472 | -44.18708 | 2025-07-27 03:49:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a5c1827-665a-35da-a3c1-f15c1fbf1119 | -26.01532 | -48.96777 | 2025-07-27 03:49:00 | NPP-375D | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1bd5355e-2004-3c0f-b396-3c4180904f4f | -26.01676 | -48.96119 | 2025-07-27 03:49:00 | NPP-375D | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 517cebc6-f187-3e73-8058-e309e6e7cd1d | -19.77745 | -40.07263 | 2025-07-27 03:49:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 64bafaee-c531-31cd-843f-1e58eff0c9df | -18.39253 | -44.18818 | 2025-07-27 03:49:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 919a9ca2-da52-3292-a74e-be569706955e | -26.01734 | -49.00646 | 2025-07-27 03:49:00 | NPP-375D | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d5d2c61f-6cb8-31e0-ad44-f001a815ffe6 | -26.01711 | -48.98349 | 2025-07-27 03:49:00 | NPP-375D | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1f009640-69e9-3f76-a57e-763362311b39 | -26.02213 | -48.98451 | 2025-07-27 03:49:00 | NPP-375D | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1af04f7f-9c93-3f95-9977-77d60f88f00b | -26.02072 | -48.96273 | 2025-07-27 03:49:00 | NPP-375D | GARUVA | SANTA CATARINA | Brasil | 4205803 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 789d5ce4-9fc9-3207-87d6-9eb3fc6c9273 | -18.81541 | -44.46619 | 2025-07-27 03:49:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dcf08d6f-4972-3ca8-b2fd-5a21e0efd0ad | -26.02163 | -48.96284 | 2025-07-27 03:49:00 | NPP-375D | GARUVA | SANTA CATARINA | Brasil | 4205803 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 86287439-e5a1-3973-b3a4-db76491fbf5b | -26.02103 | -48.98449 | 2025-07-27 03:49:00 | NPP-375D | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| df37ca8f-5213-37ec-91b2-a2809f1d658b | -18.39334 | -44.18386 | 2025-07-27 03:49:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5167ae14-3ca2-3b9d-8284-d0e3d522a426 | -6.6574 | -58.8661 | 2025-07-27 03:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 13dd364d-b85e-35cd-b860-043f4d0f61ba | -18.0027 | -53.1584 | 2025-07-27 03:50:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 5ad9f797-a61c-3e31-abe9-82a342f8f9a4 | -6.639 | -58.8475 | 2025-07-27 03:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 4d9ca611-7042-3a83-be30-f0359c57ba8e | -17.9828 | -53.1615 | 2025-07-27 03:50:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 35.0 |
| b1096d0e-2ac0-3441-a6c2-ecb63025224e | -18.0023 | -53.1799 | 2025-07-27 03:50:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 3dbe5430-09ce-3c92-a3fa-cf91ccff62d0 | -6.6575 | -58.8468 | 2025-07-27 03:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 96b4efad-704f-38ab-a5f7-09baefca5d14 | -6.6389 | -58.8669 | 2025-07-27 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| b7bdee88-085d-37a5-8ed2-24fdfd238ee3 | -6.6575 | -58.8468 | 2025-07-27 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| edf50155-7f1d-3a9b-9e0d-576a408e22d3 | -18.0027 | -53.1584 | 2025-07-27 04:00:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 41.6 |
| ed5e334e-7181-3783-b274-32d9bd68cdb8 | -6.6206 | -58.8483 | 2025-07-27 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 47660608-d698-318b-987a-01e9740c554e | -6.6389 | -58.8669 | 2025-07-27 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 60d4aafd-facb-38b4-bd9c-228679630de8 | -18.0023 | -53.1799 | 2025-07-27 04:00:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 44.3 |
| ef7c3f60-0772-39d7-9762-ce5ff961aee8 | -6.639 | -58.8475 | 2025-07-27 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 7f76eaa3-77a4-3e57-a6d8-92d7187b00a6 | -6.06192 | -42.9371 | 2025-07-27 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b15adb18-c4af-34dd-8bb4-9363d02a0406 | -6.02396 | -44.03614 | 2025-07-27 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb3bb0c7-9c2c-3ec1-807d-a43c7d4160a8 | -3.58533 | -47.52175 | 2025-07-27 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 829a1250-7d08-3518-83a0-e783cc36d181 | -6.55371 | -41.51287 | 2025-07-27 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3e606c34-4a84-322f-a53e-286a377625da | -6.52794 | -43.34806 | 2025-07-27 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb813874-103e-3187-ac68-ff84b0a7d610 | -6.66137 | -36.41627 | 2025-07-27 04:06:00 | NOAA-20 | NOVA PALMEIRA | PARAÍBA | Brasil | 2510303 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2f96d895-8e78-3b09-b88e-260de47826dc | -6.01381 | -44.05443 | 2025-07-27 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6446bb07-7adb-3ba7-9fe2-d4061c81a333 | -5.18341 | -44.956 | 2025-07-27 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 40384cd9-f8d9-3dc3-844a-1e5ed7882dbf | -6.70314 | -43.07215 | 2025-07-27 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc1c8657-8dd0-3667-b97c-290768de1919 | -6.41466 | -41.14339 | 2025-07-27 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 52e8705a-3218-3dc3-a274-080c820c0a7f | -7.01005 | -42.34407 | 2025-07-27 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bfae7ef7-cce1-391b-b5aa-6fe27ea03c56 | -7.29015 | -43.08122 | 2025-07-27 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5d2f9344-ce53-32d1-a264-90c8c773b1fd | -6.88918 | -43.10555 | 2025-07-27 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7035f94-ccf3-3ccf-ac9b-82a56948748e | -4.06969 | -42.53841 | 2025-07-27 04:06:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 319c08c6-85e9-3526-bda2-3d3b3b3fa8d7 | -2.7416 | -48.68491 | 2025-07-27 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd00dea6-f626-3054-8a33-e60bf79bf504 | -2.73925 | -48.68379 | 2025-07-27 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 24d20a0a-114f-3bda-aac5-f87ce8b4c5e4 | -4.10635 | -48.2068 | 2025-07-27 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 58dc5460-1cd9-3497-b2e8-4f00a6e60474 | -6.42582 | -44.08586 | 2025-07-27 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 219019b8-0781-337e-a7ec-49829937ac96 | -4.06353 | -42.53377 | 2025-07-27 04:06:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 58847af2-677d-3bae-9cb7-7bc149abe936 | -6.24506 | -44.05795 | 2025-07-27 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9b090f9-011f-30c6-b444-451cac1e144f | -5.60146 | -45.08026 | 2025-07-27 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ca8574d5-4881-342a-ae3e-1f3d2970a499 | -7.2868 | -43.08068 | 2025-07-27 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 312934c1-696a-3185-950c-4751869f96ec | -3.36433 | -49.17043 | 2025-07-27 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0824d356-9956-31cb-8bcb-93853f480fd6 | -6.56471 | -41.50753 | 2025-07-27 04:06:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3e00b541-deb9-3e2c-ac7d-37a23f565e66 | -4.1091 | -47.93135 | 2025-07-27 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 8bd2dbac-362a-3317-8d6d-e83b06bfb692 | -4.10901 | -47.96018 | 2025-07-27 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 27a6bdcb-ed9d-36a9-97ab-f851bd3499da | -3.92393 | -42.41286 | 2025-07-27 04:06:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c3a11326-3bcc-3d82-9e48-ddd2f94c2d0c | -6.69978 | -43.07159 | 2025-07-27 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f2b6668-a1dc-350a-a402-c3b021747c25 | -6.56369 | -36.59903 | 2025-07-27 04:06:00 | NOAA-20 | CARNAÚBA DOS DANTAS | RIO GRANDE DO NORTE | Brasil | 2402402 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c37d0a50-002a-33f5-99f9-54717003861f | -4.95725 | -43.73246 | 2025-07-27 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 20e7332d-a923-34f8-b1ee-84331d7aa27a | -6.86874 | -43.52241 | 2025-07-27 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83994ff0-232f-35a1-83b0-f78c0c4ec57a | -6.87965 | -44.01523 | 2025-07-27 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 402f6bde-f7c1-3b41-82ef-d597c28269dc | -4.11017 | -48.21262 | 2025-07-27 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f86b7f6-9d64-35f6-b455-b7dc9a80c698 | -6.88861 | -43.10914 | 2025-07-27 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9780f9a-2194-3062-808a-f9d560c8e082 | -7.29293 | -43.08533 | 2025-07-27 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1df0867d-6cb9-3e03-98fe-c7486ca1da81 | -7.09583 | -44.04533 | 2025-07-27 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19e37a8b-c977-3866-9908-4c459adcdee6 | -4.07642 | -42.53948 | 2025-07-27 04:06:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cbc1202e-2cd9-3611-88bc-ec9b416697be | -5.60323 | -45.07801 | 2025-07-27 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21d14497-edd8-33ec-ac7f-b8007e917092 | -6.8791 | -44.19323 | 2025-07-27 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 278e79f6-c0c6-3362-a1dd-ff9c0f5a9de4 | -5.67383 | -42.795 | 2025-07-27 04:06:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2f85a029-f634-3269-9d9d-79c2976504c4 | -6.59588 | -41.78434 | 2025-07-27 04:06:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1d5f1d42-b604-3a46-8d9c-0f22f869ce86 | -6.24157 | -44.05745 | 2025-07-27 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 975739ff-d2e6-3e09-9e3c-46f3401ce3d7 | -5.74416 | -43.94933 | 2025-07-27 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 21ff6f15-d094-313e-bd84-4cae2c3059ec | -6.42904 | -41.15981 | 2025-07-27 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c953c68d-4dac-3ce2-81ae-2ff78bac098d | -2.25761 | -48.35421 | 2025-07-27 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d3411c1-e67e-35fd-b19d-5a7a953f7205 | -6.90736 | -44.21761 | 2025-07-27 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27ff8abf-57b0-321a-9761-90206fd42660 | -6.48749 | -43.49225 | 2025-07-27 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 415ce4c2-5e9a-3c1d-ba0c-4f61d2691e32 | -7.02752 | -42.10502 | 2025-07-27 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 64acae70-4068-364d-a4f3-c548aecfbcdd | -4.10835 | -47.93589 | 2025-07-27 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 969cff3e-2d7e-362c-9484-eef41ec41143 | -6.39241 | -43.69024 | 2025-07-27 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf509587-b489-3120-b3aa-060f948e2bfc | -5.72637 | -44.50467 | 2025-07-27 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb22f571-e0af-3aa0-9160-dc46746c3979 | -6.01031 | -44.05392 | 2025-07-27 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3656e3ab-8fd2-3813-8caf-7658fb1a1f87 | -2.90223 | -48.24783 | 2025-07-27 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5dc47a5d-4f42-3349-8bb3-89a71e578eb3 | -4.07026 | -42.53483 | 2025-07-27 04:06:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a477ed27-588d-38de-9358-03606a830c1d | -4.07305 | -42.53894 | 2025-07-27 04:06:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 600c7755-70c2-3d9f-9c5c-5061b648dd1d | -5.7454 | -43.94162 | 2025-07-27 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27b5e2f0-5fe8-38aa-a77a-cb478cbf63a6 | -3.56924 | -49.50538 | 2025-07-27 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f42d3c9e-bbfc-317c-93d1-4471babc0271 | -7.18204 | -43.95033 | 2025-07-27 04:06:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5f305cf6-f1dc-3961-b91b-b61379cac238 | -3.42629 | -49.47865 | 2025-07-27 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d71fefc-9b96-35ed-a117-c5c4a1469047 | -5.67662 | -42.79911 | 2025-07-27 04:06:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| ef7bf061-bfd9-39c1-a4cc-f449ac0d6be6 | -6.43199 | -43.53282 | 2025-07-27 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2bb7478-d453-3784-ae30-a8efcc3eb7ca | -4.10943 | -48.21018 | 2025-07-27 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13ab55e0-33ce-3a98-bb01-998e5a618a44 | -6.05391 | -42.93198 | 2025-07-27 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9590c0fd-6abb-369e-8168-6515c811b949 | -6.89519 | -44.80546 | 2025-07-27 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41b3cf6c-4289-3922-8dda-41cd28689533 | -6.41135 | -41.14288 | 2025-07-27 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 25416465-c0ef-3d5f-ba81-a82c8412e3d5 | -5.57249 | -39.25683 | 2025-07-27 04:06:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fbed5ea8-ca24-3b28-a540-a5479dfd8638 | -6.66932 | -43.97103 | 2025-07-27 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README8.md)
