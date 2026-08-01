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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97a370ed-6588-3eee-9148-f218a6042bbe | -3.72829 | -49.27262 | 2026-08-01 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2c89874-0cbc-31d3-8d10-8a5475c94fba | -5.5597 | -43.9664 | 2026-08-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 187447e9-2d96-34cb-ac34-88a218631e7e | -7.24834 | -42.13547 | 2026-08-01 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| a4d0e6c0-d03c-383f-bcb0-c0e24970c536 | -3.85545 | -44.09858 | 2026-08-01 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f85f1c0-a91a-34c7-80d6-e7e0a0b71531 | -6.76467 | -41.00415 | 2026-08-01 04:19:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 655814d4-e83f-302a-a5a5-3a8d931d29b0 | -4.61089 | -49.05542 | 2026-08-01 04:19:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 957fa44f-97b3-3363-9d92-97c2f3d4c33d | -4.52593 | -38.54881 | 2026-08-01 04:19:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 3d577bda-f1c2-341f-a059-2fd0bad0c84f | -5.448 | -43.5885 | 2026-08-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ddf87e1d-22d8-315e-aa76-24c921d95264 | -3.51506 | -48.88876 | 2026-08-01 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fec723ea-8f28-35cb-89b0-17b997e7936e | -7.23988 | -43.431 | 2026-08-01 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 384fa092-2ce1-3369-97e1-81f0cff87999 | -7.23794 | -44.37098 | 2026-08-01 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14b3cbb3-974e-3c8d-a0dd-caf2ced5aea2 | -5.01359 | -38.67356 | 2026-08-01 04:19:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b3edc99f-797a-3f1b-937a-325614b01569 | -4.36705 | -47.76999 | 2026-08-01 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 396bb85d-cf65-394d-99de-bed6d2eaf362 | -5.55917 | -43.96986 | 2026-08-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 54631c39-9c6d-3468-a2a4-c1c99e12bc11 | -6.87698 | -44.78938 | 2026-08-01 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 911388d1-ec2d-3d60-9ddb-ea961c2652ca | -7.23762 | -43.42324 | 2026-08-01 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ae9390a4-4ae3-37bd-add4-d141f17af726 | -3.11733 | -47.91318 | 2026-08-01 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c3b002bb-3f56-3e7e-98c1-646122a5bd10 | -6.76332 | -41.01309 | 2026-08-01 04:19:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 98f46ca3-29b8-3b13-b91d-d72f92f1bbd8 | -4.27159 | -48.19644 | 2026-08-01 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| acda8fdb-7467-3b22-b412-abf447c2a611 | -4.62428 | -47.4071 | 2026-08-01 04:19:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea3d56a7-509f-3c43-aaa9-509f45f749c1 | -8.34526 | -45.98859 | 2026-08-01 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9bc1abf2-263e-385b-9cd1-c3574a68ab8d | -6.27452 | -41.87223 | 2026-08-01 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 98f266e0-7570-3ddb-b8e3-073dc8cbccdd | -7.50852 | -45.83706 | 2026-08-01 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6149a9c2-0370-3ef2-af77-100654b144f4 | -6.56145 | -55.16652 | 2026-08-01 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0aa8fa5a-6f25-32b5-8ae7-53c5cd37bb8b | -5.641 | -47.10867 | 2026-08-01 04:19:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23b79369-c62d-3184-a162-8e18f866fdd2 | -6.42833 | -42.82224 | 2026-08-01 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a125fef6-faed-3217-9b1d-d97e9e08bb5e | -0.99299 | -48.08345 | 2026-08-01 04:19:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cce10402-8a6e-338b-a0e4-8cf18c847a9c | -6.76265 | -41.01756 | 2026-08-01 04:19:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3b875ff3-a6c3-32ba-a6c0-5f10690a71c4 | -7.54763 | -43.99289 | 2026-08-01 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ac5b25c-c05a-3f8f-92bf-8be99566a2af | -5.55496 | -43.97289 | 2026-08-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36b4b623-65b5-3bad-aaf4-b7555845a343 | -3.85322 | -44.0912 | 2026-08-01 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0726fe64-f8df-3444-9d6e-99b5703dcf5f | -7.62354 | -38.80048 | 2026-08-01 04:19:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5e3d7501-f014-3c51-b7cd-e445f7e1cf2e | -6.42797 | -43.71507 | 2026-08-01 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3e302b7-760e-3fc2-9aa1-79a36b16ef9b | -6.60991 | -44.66921 | 2026-08-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 765d07a9-0cf7-3da2-9967-c4a91e89502d | -6.64823 | -43.91817 | 2026-08-01 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0cc1a622-f1e6-3c46-a0ae-f2afcee38ae5 | -2.89065 | -48.01873 | 2026-08-01 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a05df8ae-89af-3b36-a10a-49bb5851a069 | -6.27391 | -41.87625 | 2026-08-01 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 0622da14-61fe-35c3-8fc8-3b70b3f2a1ed | -7.55484 | -43.99038 | 2026-08-01 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 836bda3e-9e9b-376b-85a2-0646105e042a | -7.34036 | -43.00364 | 2026-08-01 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7ee4b345-1b6c-35a9-94ce-b9f3acbf81b9 | -8.31872 | -44.78994 | 2026-08-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8efbf0d1-beb5-3edd-a3ea-d15913bff04b | -8.31818 | -44.79342 | 2026-08-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32a95acb-9cc3-34c5-8b27-9d199227c560 | -3.43016 | -49.02136 | 2026-08-01 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ae3b44b-0d15-3d6b-a836-db4b2f27196f | -8.43786 | -45.61635 | 2026-08-01 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d562aa22-33e4-3ce9-afe8-5593b29646e8 | -3.48395 | -47.6866 | 2026-08-01 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7293cb8d-2bda-322d-baec-2e4898d7d3d2 | -4.36775 | -47.76564 | 2026-08-01 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 1a55f710-f127-3b54-862e-ce900441a750 | -3.85598 | -44.09514 | 2026-08-01 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29eec7a8-632c-3011-8a59-47d43ea72465 | -6.84095 | -42.89867 | 2026-08-01 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 519c7593-0d78-302e-a6b2-ed34deb1000d | -6.56114 | -41.84245 | 2026-08-01 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 743d4d72-a98f-313a-b899-794d9e9a6b95 | -7.19902 | -42.96364 | 2026-08-01 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b67a9057-a4e7-3877-9c6e-cca2bbb58a87 | -5.55549 | -43.96943 | 2026-08-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e8f74ca4-056a-32b6-b68f-854a5a0806de | -6.2308 | -38.26028 | 2026-08-01 04:19:00 | NOAA-21 | RAFAEL FERNANDES | RIO GRANDE DO NORTE | Brasil | 2410504 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8e805cfc-faf4-31f5-85a0-f66d448ed3e0 | -3.67877 | -49.47814 | 2026-08-01 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70807792-c62c-303c-9e91-d0367c8f5920 | -7.32754 | -42.99463 | 2026-08-01 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 51be0bc4-fbf3-3a61-b981-94ba797ba576 | -4.2571 | -38.03171 | 2026-08-01 04:19:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 81.3 |
| a0bd24d4-3d02-3314-a038-c80564732516 | -4.65654 | -42.43666 | 2026-08-01 04:19:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4dc61ce3-1126-316b-8102-0117dab6d5a5 | -6.79044 | -41.83373 | 2026-08-01 04:19:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 553e3e16-00bb-3459-9c17-8c6009fad28b | -5.76287 | -47.34278 | 2026-08-01 04:19:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| aa33cd8f-96f0-3fa9-a8f3-a2c007c8651a | -7.23424 | -43.42271 | 2026-08-01 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c7e7af18-56ce-3056-bf4c-c7782e78693a | -7.64516 | -45.05301 | 2026-08-01 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e676d74d-b5e9-3176-beca-16eec8ec2cbb | -7.649 | -45.05006 | 2026-08-01 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f575363-ac95-36a8-9c00-4790f5c6e98f | -4.2761 | -48.1925 | 2026-08-01 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d94c55e-0258-3c1e-b833-87bc9a8e82de | -7.19218 | -42.9626 | 2026-08-01 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 11b71def-b907-3414-82f3-4138bc7ec6de | -3.03685 | -48.41176 | 2026-08-01 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8def436f-be0b-328f-b237-19481cefae52 | -4.64276 | -43.12233 | 2026-08-01 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fd45eeb-584d-3f4e-baa5-679f45d33bdf | -3.42559 | -49.02427 | 2026-08-01 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35c83258-2f7d-3a99-8e49-584824eff3c0 | -6.79523 | -41.82607 | 2026-08-01 04:19:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4a0b7f2b-f89c-31ba-8a1f-fe4bc2187d2d | -7.23032 | -43.42581 | 2026-08-01 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2c835026-250b-3349-a900-b3cb03f4f18a | -5.31648 | -47.48219 | 2026-08-01 04:19:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 76ed181f-a32d-3eb3-a8cd-df9ee2009268 | -2.60155 | -47.34308 | 2026-08-01 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a115d6d5-1b49-32ea-b553-a7a42003f43b | -7.77635 | -44.07545 | 2026-08-01 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d7d8380-09d9-370f-87b7-519dd1c764d5 | -6.42464 | -43.71454 | 2026-08-01 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 038d3726-65b6-37f0-acdd-44d00ccf95af | -7.49506 | -46.11729 | 2026-08-01 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 79bf5c1b-42ba-322c-86c9-51d880bddc80 | -6.52071 | -42.76737 | 2026-08-01 04:19:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9cc33e64-0ac8-383e-8d67-dcaa1e7bdd67 | -6.7646 | -41.01558 | 2026-08-01 04:19:00 | NOAA-21 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0a74e1d4-41a3-391d-846a-f3093e53ffe2 | -5.55863 | -43.97333 | 2026-08-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d02b980a-5d16-39cb-92af-ee5e2f250da0 | -5.75625 | -43.26715 | 2026-08-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b5869ac6-caa4-326d-b405-dd953ca7a281 | -6.41343 | -42.45942 | 2026-08-01 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 228277a4-ce2f-3665-8242-f258fab2dc7b | -3.84608 | -44.09362 | 2026-08-01 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 632f024c-666f-3fb5-9d8d-3c53e9ccf51f | -5.545 | -45.79689 | 2026-08-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78847249-95b2-3f28-a37a-c37c7a67ff7f | -7.50464 | -45.84005 | 2026-08-01 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| fb14f810-4c25-3655-925c-056318285e37 | -8.34858 | -45.98911 | 2026-08-01 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cbe5cba8-a6be-3eb2-88c0-c19d7ae53358 | -7.77303 | -44.0749 | 2026-08-01 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b22eed59-19df-3fa8-8cc8-9427dabbf3cf | -7.66445 | -45.05957 | 2026-08-01 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd26dd7b-fec8-3f6e-a24b-729b99cfed7a | -3.11053 | -47.90751 | 2026-08-01 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 80f0931e-67a5-34aa-89db-9878dc9f4e78 | -6.67305 | -42.57085 | 2026-08-01 04:19:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e549af19-2581-3189-a3c4-e57c119529cb | -6.5528 | -41.8741 | 2026-08-01 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ea9680c8-ecd3-3428-b449-bdb27ca27614 | -5.93396 | -46.35339 | 2026-08-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c444dd03-1845-3085-a620-11d91b7971e2 | -5.04198 | -43.26652 | 2026-08-01 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16a8dc3f-cd54-336a-a34b-064592ac0c71 | -4.65313 | -42.43613 | 2026-08-01 04:19:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8744774d-4cda-3567-88b6-034b600d4eff | -7.50131 | -45.83953 | 2026-08-01 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fb8bc122-53f3-3293-81ed-f7deee977c16 | -6.6066 | -44.6687 | 2026-08-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d4813fd-aa8a-36f5-8ae9-59c00833fbe7 | -6.84116 | -43.28499 | 2026-08-01 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| eb3cb36f-f08c-34bc-b180-dd92e9048505 | -6.54275 | -41.84372 | 2026-08-01 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d991f1ee-eed4-3ceb-9ef6-4b7a47f574f9 | -6.27806 | -41.87281 | 2026-08-01 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 3299fe94-b511-3989-b1a6-fcb67a792352 | -7.62523 | -38.79848 | 2026-08-01 04:19:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f024a8c0-98df-3a71-9341-af8e212d726f | -8.34193 | -45.98807 | 2026-08-01 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f1c2863-3d4b-312b-b4d8-a400678f357d | -7.32464 | -46.81829 | 2026-08-01 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| af8dd2c9-3d7c-3525-a497-bd19b8805329 | -6.6521 | -43.91519 | 2026-08-01 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2a9162e8-ca81-3453-98fe-fae227ca1341 | -3.84554 | -44.09705 | 2026-08-01 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3c70dd5-e417-316a-992e-cbd847823f97 | -7.22503 | -43.55025 | 2026-08-01 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README11.md)
