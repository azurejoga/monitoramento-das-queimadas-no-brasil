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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 731b1b79-994c-37b6-b198-4d2751a18f28 | -3.41856 | -59.22648 | 2026-09-11 05:27:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14bee627-11e3-3b87-a16c-ea6cc2df2d97 | -6.96042 | -59.74939 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b0a59ec-435d-303f-ad03-55ee703aed6d | -3.73493 | -61.75572 | 2026-09-11 05:27:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f46ad79b-346e-3760-9b5e-66007be294ea | -6.82376 | -58.98922 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98bd26ef-c8b1-3015-bcad-ffe19f605c44 | -6.85482 | -55.75352 | 2026-09-11 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e053da22-db9b-3627-a24f-17e2a229c9b1 | -4.47496 | -54.89246 | 2026-09-11 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f08edbe5-55d5-3f3b-b666-561ac94f5786 | -2.85834 | -49.54056 | 2026-09-11 05:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d14e5531-052c-38bb-852a-551ad43c67fd | -6.20502 | -55.27565 | 2026-09-11 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6e8abccc-bc27-369a-9320-98ae7ad27d69 | -3.55092 | -48.18182 | 2026-09-11 05:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5e9ae2b-e0d8-32d9-a9fd-65200c5771b6 | -6.76698 | -59.43249 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23110c26-8abb-377c-9312-7f3f65fd8f02 | -6.76754 | -59.42902 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6edb77ad-5e1e-35a3-a097-26fda66a437e | -2.94294 | -50.47136 | 2026-09-11 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab3df62b-46ec-3480-be22-f63a41d649ca | -5.97598 | -57.78308 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95f0942e-ee76-3afc-8579-d1483fce5d66 | -2.54926 | -56.28566 | 2026-09-11 05:27:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cb6cba7-984b-38b9-b6af-47d7f31ce3d8 | -5.853 | -53.86689 | 2026-09-11 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91699b02-f54c-3a14-ab75-1e941f9852b8 | -3.37418 | -50.74948 | 2026-09-11 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ed274c36-bbc1-3b22-bcbe-ee8eec3af0e9 | -2.72862 | -57.62978 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f8a29585-66b4-38b6-aaea-6075c259b75c | -6.19892 | -55.26551 | 2026-09-11 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42ac8842-c36b-3690-8e17-b03a459be452 | -4.29869 | -49.10523 | 2026-09-11 05:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3af1478d-3e05-3edc-8ea6-7f19a31689da | -3.53312 | -48.18286 | 2026-09-11 05:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9d5d710-335a-3022-901e-df1067981ddf | -6.77086 | -59.42954 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a5f2544-e0dd-3bc6-8076-37af348b9260 | -2.73415 | -57.61642 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 555eb2e0-f7fd-3aef-ae94-873ad9ca8340 | -6.11058 | -57.63579 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d954ded-2fe7-3707-b782-59fae8769870 | -5.97543 | -57.76472 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 49df0243-a678-3dab-8fd9-5069d88c2f3b | -2.71749 | -57.61382 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5cb3f1b7-dfa0-3d4e-af49-511e5d24910c | -6.19756 | -55.27448 | 2026-09-11 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 040d44ee-3454-3f2e-a4f4-f40185f8eb00 | -2.69177 | -57.51722 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ed8c393-6daa-385d-9f9d-d89cebec88a9 | -2.73469 | -57.61295 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09730391-5c1b-3d4d-baf0-e47cf7417b29 | -3.06912 | -51.33709 | 2026-09-11 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e5455d82-8230-33ff-9b2a-d229bee1dd8b | -6.50599 | -58.38928 | 2026-09-11 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be635e74-8366-31dc-baac-57e41228cca0 | -2.74742 | -60.23678 | 2026-09-11 05:27:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54790bfa-a190-3fcd-b641-bf25db3e68d4 | -3.40228 | -54.07772 | 2026-09-11 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9e00291-cb3d-341a-908d-d0dec69b5d96 | -4.52619 | -54.96239 | 2026-09-11 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4437b5ea-054c-3860-9cc3-441d9a0528fb | -6.12502 | -45.11024 | 2026-09-11 05:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3a00dc04-18bb-309e-a996-50e0a6f60f8a | -2.56102 | -58.06687 | 2026-09-11 05:27:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 405defbd-7012-342b-b329-7f02e6794809 | -6.24075 | -51.68745 | 2026-09-11 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 58a9af73-589a-3529-9d5a-a6b99501a746 | -8.62701 | -47.4092 | 2026-09-11 05:27:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 103f0c51-1ecc-315e-b880-1f653c6b77c5 | -2.73473 | -57.63429 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 602ad876-1447-353c-ac59-bfe0ce24c7c2 | -4.53801 | -54.95973 | 2026-09-11 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ac797cde-5604-31c0-8143-0705bac18cfd | -3.37338 | -50.7547 | 2026-09-11 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c9202767-d96a-3b22-a624-05937f9a7b12 | -1.77702 | -54.94279 | 2026-09-11 05:27:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a715c89a-25bd-3d8e-b147-ecf0bb7df7cc | -3.98515 | -56.09118 | 2026-09-11 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c3bc622-b412-32b1-bc15-08b2b066a639 | -8.63209 | -47.42077 | 2026-09-11 05:27:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 0a5c7304-d48f-369f-91a7-2791500bf3ec | -7.93116 | -49.73246 | 2026-09-11 05:27:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94d8f9b5-1eba-3a77-90a9-443f6caf7d3f | -6.76672 | -58.62019 | 2026-09-11 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e87cfe28-5a10-36a0-8e3c-db167a09d407 | -6.19518 | -55.26496 | 2026-09-11 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6614faf7-77e6-3892-a6ae-c40854de78c3 | -3.251 | -50.81909 | 2026-09-11 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c8d684d5-37b5-37d4-9a03-c33c65f812c8 | -6.69146 | -59.13912 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65b7ea96-99dd-33f5-a6e7-554cb9c1cd90 | -6.18672 | -57.75388 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8736dd1-842a-39d4-9812-edbfa8baf7a0 | -3.03641 | -59.16606 | 2026-09-11 05:27:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da2d6d94-325c-37a2-aed3-ea1299ac5f30 | -3.37017 | -50.74348 | 2026-09-11 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 320a9932-e9e1-38ee-b14e-632f2b62f90d | -6.05835 | -57.79242 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 927495a4-68d7-3593-b277-8438e7803f56 | -4.83122 | -55.76596 | 2026-09-11 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de265ee9-7c85-35bf-a998-dc79559bd49a | -6.18447 | -57.72421 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f450feaf-8b87-36a4-9ea1-f5ebaf523370 | -6.50321 | -58.38525 | 2026-09-11 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 766b87c6-e53b-39f7-a46d-10aad2e33d20 | -1.77639 | -54.9469 | 2026-09-11 05:27:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a17fec04-9e16-33f3-ab7d-ba8ab1d57254 | -6.95986 | -59.75289 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc3fa655-db03-31d7-8d79-9ab0ab566961 | -4.36099 | -47.78291 | 2026-09-11 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b726b36c-7c3c-3ff0-a4bf-6c538747ffb5 | -7.93151 | -49.73308 | 2026-09-11 05:27:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef55df79-2095-3ee6-a9ff-6e3465e5f714 | -3.37179 | -50.76509 | 2026-09-11 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 664e2c91-072d-32e6-831d-f2b374b61f28 | -6.50266 | -58.38875 | 2026-09-11 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 604836e8-c548-3013-9c66-96bd167f7e83 | -2.67898 | -57.51165 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 09260fd0-52a1-3eda-9275-e7c29d19781f | -5.28006 | -55.96546 | 2026-09-11 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 465f7edb-d6e2-3b11-902c-e262ed561152 | -2.67953 | -57.50818 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a58ef75e-7a85-30ca-aa2f-a439566413fd | -4.4528 | -55.44054 | 2026-09-11 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5fbcdde-8e1e-3b46-ab45-a0624dcaa745 | -4.52379 | -54.95323 | 2026-09-11 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c21fb62d-2181-3ffc-8318-276893b617aa | -5.98441 | -57.72959 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c0053a6-3b5c-3f4d-b1db-e00c369ca561 | -6.1322 | -45.11126 | 2026-09-11 05:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dbaa3ee5-79e3-3864-94cf-6c9db40eb677 | -6.19144 | -55.26442 | 2026-09-11 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d72fd646-938f-3e74-93fe-8dea4b99f85a | -2.53148 | -59.55254 | 2026-09-11 05:27:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0be017ef-31a8-346b-9887-aa60974643ed | -6.18503 | -57.74264 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de19048b-c32e-3c42-8b68-c2efc9c2790f | -4.36404 | -47.78114 | 2026-09-11 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 015f9534-80e8-30d1-9bd2-2b015539e7d3 | -4.36165 | -47.77843 | 2026-09-11 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b553ad4a-1f55-38da-bd08-396ed80b6233 | -3.53371 | -48.17888 | 2026-09-11 05:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 19cefcfb-111b-3b56-a97c-946c04bc9881 | -3.09343 | -51.29084 | 2026-09-11 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad2beb50-5481-3182-8266-7567b6a6a544 | -4.36763 | -47.77932 | 2026-09-11 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6340719c-ffda-31e5-a325-45e12cb61570 | -2.73748 | -57.61694 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e4097d1-c597-3300-9a1f-cf029d5056e0 | -2.69232 | -57.51374 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dac26869-2dd7-363b-9e79-e33fc9e4ed66 | -4.29372 | -49.10091 | 2026-09-11 05:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f08c1e28-6c45-3958-97c4-a68fcdaf88d3 | -6.50431 | -58.37825 | 2026-09-11 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 902d5fda-22ec-33b1-81fd-b3bb31c1ef23 | -3.15928 | -58.64631 | 2026-09-11 05:27:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfd95926-e260-3d43-b4f2-67a623ff67e9 | -2.74026 | -57.62093 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 740bdd25-050a-3a66-8ccb-884386535bc5 | -6.20062 | -55.27956 | 2026-09-11 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb7143f6-a811-3a41-baf5-e69ab07843b1 | -2.92201 | -54.11102 | 2026-09-11 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2da1abd4-c66a-3dfd-8dac-1b5b72a8bccf | -4.53732 | -54.96417 | 2026-09-11 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4207abdb-2e3f-337a-b6bb-bb913303acd0 | -4.8631 | -56.00357 | 2026-09-11 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6e732bd-5d25-3d66-a746-38979506085f | -6.40616 | -54.96871 | 2026-09-11 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b97953d1-0096-3a4e-90e3-7e08fb22b7dc | -3.0642 | -49.52209 | 2026-09-11 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d334f14-d78c-3e9a-ac44-12b63f808751 | -4.86479 | -56.01629 | 2026-09-11 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3a8c2be-6a7d-3540-9e81-ea11f66a85d0 | -4.55806 | -47.76229 | 2026-09-11 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51a6f86d-eedb-3472-86f2-611c08999ead | 0.30266 | -60.43733 | 2026-09-11 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6266c6fe-ffbe-3b87-9d96-cab451b6447e | -2.71804 | -57.61034 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4455d9c5-8fe8-36a5-a244-affb9a46dddb | -6.2524 | -57.78186 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6960a241-bb25-354d-8b29-25575f9f30f5 | -2.93316 | -50.46994 | 2026-09-11 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44c23417-6fbf-3622-8bbe-962b04480b29 | -5.97487 | -57.7683 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| af29effb-fa04-3468-8775-eb7b4b8798b1 | -4.2992 | -49.1017 | 2026-09-11 05:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a1913bb5-15e5-30fa-9983-ee9dee3e5292 | -3.42191 | -59.22701 | 2026-09-11 05:27:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee41ee8c-ce1a-3a71-83b4-71fa93b2fc44 | -6.10661 | -57.66098 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c3911f2b-de3e-3c18-a1c1-76b418f615b2 | -5.38305 | -46.30132 | 2026-09-11 05:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98b9972b-a8b5-3894-85d6-d69b74a3fa31 | -3.3388 | -59.43818 | 2026-09-11 05:27:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README26.md)
