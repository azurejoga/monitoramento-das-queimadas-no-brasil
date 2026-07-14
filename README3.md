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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d855326-785c-391b-b08e-f1ad013afa29 | -10.75774 | -42.11037 | 2026-07-14 03:17:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4b6cd556-8bcc-3c19-a984-7d768d4d9aa8 | -9.40557 | -37.81915 | 2026-07-14 03:17:00 | NOAA-21 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5cd9e152-2426-3e47-8aff-9719fa364948 | -9.40608 | -37.81622 | 2026-07-14 03:17:00 | NOAA-21 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7246db95-8de1-30f8-9538-f500cb3b3ab1 | -6.49107 | -42.22807 | 2026-07-14 03:17:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9b859bc9-d20f-3a6e-8cd3-2a12afd283f8 | -9.40648 | -37.81464 | 2026-07-14 03:17:00 | NOAA-21 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c7cfcec7-72a6-3830-a86b-f9cfbd05a998 | -10.75695 | -42.10854 | 2026-07-14 03:17:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| abda6ac0-c5f6-3870-8c37-956b8baebda4 | -6.48547 | -42.21982 | 2026-07-14 03:17:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 5d72f4fa-0d79-3583-b427-deef6ea71c77 | -9.40594 | -37.81756 | 2026-07-14 03:17:00 | NOAA-21 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 01be4a8e-c5ec-315e-a433-42e582f975ce | -6.48291 | -42.23349 | 2026-07-14 03:17:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 26d1348d-f04a-3f33-87d8-b5896240b60c | -9.24096 | -40.50622 | 2026-07-14 03:17:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9ef9f8f9-04d9-305c-8fb5-195ec5119eb6 | -10.75589 | -42.11396 | 2026-07-14 03:17:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 71891d66-36d5-3f81-9b6c-c455b9aa907b | -6.4842 | -42.22657 | 2026-07-14 03:17:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| af3892c9-f0d7-324d-b3e1-4179e7c88ee2 | -9.40109 | -37.81527 | 2026-07-14 03:17:00 | NOAA-21 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7163c262-63bc-33c8-bcb1-2825690c1627 | -9.24406 | -40.50841 | 2026-07-14 03:17:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 5.2 |
| a8c1fcb1-7051-3d12-b29b-b69fb299031f | -21.56905 | -41.25472 | 2026-07-14 03:21:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9afa703b-5aeb-3718-a8f9-823f0f82a4fe | -21.57365 | -41.25706 | 2026-07-14 03:21:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ca471748-ae47-3256-a46f-588e4d87285e | -20.48488 | -45.67372 | 2026-07-14 03:21:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36fbfa05-9b75-315e-b505-07edbc695354 | -21.56869 | -41.25587 | 2026-07-14 03:21:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ef039f65-0ce4-32e3-8ac0-38a33a5a330b | -1.57341 | -47.7553 | 2026-07-14 04:10:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e161c939-9feb-3533-999b-274a744799a5 | -3.2214 | -43.36053 | 2026-07-14 04:10:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ed5804a-6741-3ccf-9997-7ff52f90d2a3 | -2.91106 | -40.3952 | 2026-07-14 04:10:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8bc138af-0427-3a8e-81e9-2487d9ca3146 | -3.55611 | -43.19653 | 2026-07-14 04:10:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7a77caa-3cc3-34e5-abd5-60084057dd64 | -4.14957 | -38.17034 | 2026-07-14 04:10:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 00a5cf7e-2aac-3aab-b1b6-79d0e31017ac | -3.95511 | -41.78496 | 2026-07-14 04:10:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f2189126-a564-3c7c-8188-f2c497495aca | -2.8056 | -48.59032 | 2026-07-14 04:10:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11f62071-3604-3738-a496-bc06b2b7651c | -3.69812 | -43.25355 | 2026-07-14 04:10:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d025a72-d932-317c-b312-af7e23004bba | -2.90775 | -40.39468 | 2026-07-14 04:10:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 753d93b8-8b89-3b4f-b72e-0f2bf804c892 | -3.43899 | -41.65325 | 2026-07-14 04:10:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bcc14b9c-9df1-3b81-a55a-53b2d6a6070e | -6.49587 | -42.22116 | 2026-07-14 04:12:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| e802fb83-061b-34a7-83b7-c4be3d56091a | -5.51907 | -45.96904 | 2026-07-14 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ff75b70-75b3-32e8-b9b7-1343f9c54239 | -7.77986 | -45.50383 | 2026-07-14 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3feb98eb-08ec-32cb-87b2-8e9ab321e834 | -3.15515 | -48.57856 | 2026-07-14 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4562a74-97c5-3727-9b34-01a3a147d626 | -5.52143 | -37.48717 | 2026-07-14 04:12:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ccce27fb-fc31-34e3-bc07-1e66d101b4fe | -4.37385 | -47.76824 | 2026-07-14 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8b09761d-1e12-3d63-b415-d23558f3073f | -7.29517 | -45.28241 | 2026-07-14 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4d93b78-34fc-39c6-aebe-3a799ff41227 | -8.73226 | -48.3281 | 2026-07-14 04:12:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76abc839-ba92-3b16-acf6-c145f26f55e6 | -7.7563 | -45.02951 | 2026-07-14 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 31b972c1-3f4e-3996-a053-ca27e79517d4 | -7.75989 | -45.0301 | 2026-07-14 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 3c5bc33a-212b-34b4-91de-4673dd20d66c | -6.67155 | -47.52235 | 2026-07-14 04:12:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7240365-8878-3194-9cee-5b2cdb9ff9c0 | -7.74622 | -45.02357 | 2026-07-14 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| adf5f0fc-0de9-36e9-a417-052e061a775d | -7.90647 | -48.26204 | 2026-07-14 04:12:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0df3ebb-82e7-3aa1-be26-7ee0f242fcde | -4.94393 | -48.24782 | 2026-07-14 04:12:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff6795ed-1278-3729-b04b-a0c856c9244a | -8.73152 | -48.33222 | 2026-07-14 04:12:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76e25f03-52df-3f69-965b-be8a2424ad49 | -6.67089 | -47.52631 | 2026-07-14 04:12:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 371036f5-a55e-37d2-a505-652ccbdd5290 | -7.68085 | -47.32833 | 2026-07-14 04:12:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee4448f2-97e7-3289-acc9-cc11c217d441 | -9.24115 | -40.50725 | 2026-07-14 04:12:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| da910ff0-f34a-3d36-90c4-1be232ab6bfe | -3.57743 | -49.20716 | 2026-07-14 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf847512-d017-3a87-a3db-dd452c941f0b | -5.82535 | -43.48111 | 2026-07-14 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb33a4e9-614b-368a-a99a-bf7584805f0a | -7.77619 | -45.50321 | 2026-07-14 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 34eaa612-4797-3cea-8f4a-33527b14a418 | -5.25495 | -42.66764 | 2026-07-14 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe715db5-1ee7-3b8d-9427-cd985ab22770 | -4.01602 | -48.05827 | 2026-07-14 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 060a0007-47b3-3b01-ba09-90cc5ccbe7b0 | -7.76847 | -45.03483 | 2026-07-14 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e5f5c5a-e2e2-30b3-8635-953415cb2140 | -8.8336 | -48.33358 | 2026-07-14 04:12:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e59dd801-cf0d-3301-b1e8-affdd0d87940 | -4.01083 | -48.06034 | 2026-07-14 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4af0f158-31b5-37e0-b20e-3d3296973dc2 | -7.76347 | -45.0307 | 2026-07-14 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35d03e64-7c9f-33d4-9d85-a8b640ccb8c4 | -5.91161 | -43.6215 | 2026-07-14 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| fd32a4d7-abaf-3468-8408-018064abd037 | -6.15506 | -42.90972 | 2026-07-14 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d3e63406-a8f1-31c6-8f6f-9d97c59fe241 | -7.90722 | -48.25778 | 2026-07-14 04:12:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47965f7b-812d-36e2-80fb-d4b484156fa6 | -7.01037 | -45.41795 | 2026-07-14 04:12:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0ba9f879-416d-3cbd-a354-5a89795c495f | -8.88624 | -48.50137 | 2026-07-14 04:12:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a679b85-a4c4-3571-a3a9-c28a149378e9 | -3.1514 | -48.57774 | 2026-07-14 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2db74d42-e3e6-3ee2-98c5-86bd52284bc6 | -4.47479 | -40.86393 | 2026-07-14 04:12:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5430f9fa-bff4-3380-b6ff-207175fe3057 | -9.24455 | -40.50778 | 2026-07-14 04:12:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4ccd4166-2395-396c-a38e-2bfc13bca8b7 | -7.7718 | -45.50693 | 2026-07-14 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a16f877d-6526-302d-ae62-bb61392dde12 | -8.59314 | -47.38937 | 2026-07-14 04:12:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ea5b38f-bbb7-3be7-95dc-d78f44e7981c | -5.82997 | -43.47422 | 2026-07-14 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 736645b0-65b1-39e9-abfb-fd74e7866316 | -7.01406 | -45.41861 | 2026-07-14 04:12:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5983e361-36c8-3c02-853b-1caffd5a7afa | -4.00602 | -48.06184 | 2026-07-14 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| be4913ad-af79-3ef6-a6c2-ff4ec82ea348 | -9.02929 | -44.256 | 2026-07-14 04:12:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdf2314e-fb0b-3741-84a1-bbf63d974a85 | -9.5551 | -40.33223 | 2026-07-14 04:12:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 7e32bc5e-ceab-31e6-bad2-d734718c006d | -9.40437 | -37.81309 | 2026-07-14 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fcd17306-9b04-3c4a-84ae-e4c0714ef618 | -4.01065 | -48.06234 | 2026-07-14 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 802580aa-cc14-3636-9f01-e921c9a365df | -5.3094 | -47.23961 | 2026-07-14 04:12:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7809596c-f0af-3d96-a644-6c43a34cfeaf | -5.911 | -43.62527 | 2026-07-14 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 291053a1-3254-3c79-b685-f791eef9ca78 | -5.30359 | -43.06293 | 2026-07-14 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc1cdbfe-0459-3bdb-86bd-ae7dc343d7f5 | -4.94355 | -48.25054 | 2026-07-14 04:12:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 068f609e-e56b-3487-94ba-5c08a6bf237d | -7.75271 | -45.02891 | 2026-07-14 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 07c64df4-f0ce-373f-9cb9-ad9ab69c5923 | -8.88551 | -48.50559 | 2026-07-14 04:12:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa8acd63-5b5e-3485-9ef5-131b7d60512d | -4.01142 | -48.05755 | 2026-07-14 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 97294768-ad60-3f28-b3c8-e0f2cc50dfa1 | -7.74981 | -45.02418 | 2026-07-14 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0ab04d3b-3afb-38b7-8ee8-5195be777f13 | -6.4847 | -42.22618 | 2026-07-14 04:12:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| ee70f786-484a-35ee-88ec-b98dc65e55d8 | -8.92984 | -38.22725 | 2026-07-14 04:12:00 | NOAA-20 | PETROLÂNDIA | PERNAMBUCO | Brasil | 2611002 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f512ba3a-bc19-3d1b-be7a-08083fddacb7 | -6.94705 | -43.70446 | 2026-07-14 04:12:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 566d167a-ee6c-3084-aebd-8a686dd6a6f6 | -7.09228 | -41.69565 | 2026-07-14 04:12:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bbe2f12b-a088-3db4-b529-931f682e476a | -5.82937 | -43.47793 | 2026-07-14 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f4a852e0-f7f5-391d-a144-058602b164ac | -5.30816 | -43.05615 | 2026-07-14 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7081f2e7-ad8c-3a6f-b7ce-a47c72edad9f | -5.93734 | -46.35326 | 2026-07-14 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b5aa66f3-bd71-38d5-a841-4cc736aa4a79 | -5.80068 | -43.63467 | 2026-07-14 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 323ec0d5-c180-319f-afd7-099203504df0 | -7.76639 | -45.03543 | 2026-07-14 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a72fa8a7-31b1-389e-9074-92e105f3c778 | -9.03333 | -44.25283 | 2026-07-14 04:12:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ac09a8b-d625-359c-81c9-79b598bea767 | -5.55638 | -43.96517 | 2026-07-14 04:12:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2c8afc5d-eef0-3200-9563-22ae03730afd | -7.0111 | -45.41356 | 2026-07-14 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a53d0b05-360c-33f5-8882-b5b7962f88dd | -3.15535 | -48.5839 | 2026-07-14 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcc701b0-3f32-3c14-9554-1230c41e38d1 | -6.48869 | -42.22359 | 2026-07-14 04:12:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| c31ee131-165f-32ef-9d69-8ca8f9225581 | -4.00537 | -48.06469 | 2026-07-14 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7383e493-d501-363d-aca6-b48f01a0f94c | -9.40365 | -37.81802 | 2026-07-14 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3dcb3373-8941-39ed-be44-dbb99aa6b8c1 | -8.73465 | -48.32936 | 2026-07-14 04:12:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e1e5a644-7eec-3c75-bdec-0d5e4b8a08c3 | -5.24275 | -44.93187 | 2026-07-14 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b88f35d8-4417-3daa-b0d1-9ae7d9fe3c43 | -6.15415 | -47.11939 | 2026-07-14 04:12:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 872d9969-e57e-3f11-ad14-de5f11bf5f4f | -5.30873 | -47.24364 | 2026-07-14 04:12:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README4.md)
