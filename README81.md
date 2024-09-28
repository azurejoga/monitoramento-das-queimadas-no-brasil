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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78e3271e-b81f-3834-80a1-396c06016b71 | -15.67962 | -53.92039 | 2024-09-28 05:10:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2985faac-b092-330d-98ff-8a4b4692d760 | -15.67705 | -53.90819 | 2024-09-28 05:10:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f2d4643-0915-398a-9a7c-a6bdfe216c60 | -15.67654 | -53.91204 | 2024-09-28 05:10:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69a63ea7-268f-35cb-94bc-b14bf9313b82 | -15.67552 | -53.91982 | 2024-09-28 05:10:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 71e801b6-2f1e-36a1-8dfa-9fa9fd1d61f6 | -15.48787 | -53.38015 | 2024-09-28 05:10:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 20857630-b2d6-3070-9b79-20bbb9bdb8d0 | -15.48734 | -53.38436 | 2024-09-28 05:10:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 46aa0773-7aa7-308c-b25c-a1419fe638de | -9.46731 | -53.59457 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ec4f630-9ef4-32a5-a484-a92dba563720 | -9.46345 | -53.59401 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c47dcbb3-5ed9-35a7-8c0f-ab27e8cc14e0 | -9.23905 | -54.56628 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02a19c7c-fb89-3c4d-87be-e2b1cfabee2c | -9.2384 | -54.57058 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c918a7f-4fb7-3e17-b830-4517c4fe86a5 | -9.23541 | -54.56573 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31b4ea16-4959-35a2-9512-4a049ef1a38e | -9.23177 | -54.5652 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d52b1c83-a48a-3189-91ec-5bb152ceb5d1 | -9.17248 | -54.66545 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ff9f165-56c7-3a5c-b22b-89e34466405b | -9.17124 | -54.67392 | 2024-09-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0b3a961-c8eb-3671-978d-901ce3a65c5d | -9.17063 | -54.67804 | 2024-09-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dde93e85-3b2f-3496-aa29-53e3bda64ed8 | -9.16824 | -54.66918 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4b0d2e9-4568-391d-b771-7f33efc9b675 | -8.92917 | -54.74728 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a2fa919-55d8-3d86-8ecf-078900b8d1db | -8.92498 | -54.75084 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 910c1d0f-0e72-305f-af5f-2c8d7bcad8d7 | -8.92139 | -54.7503 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3101fc3b-d8c6-3962-bd3a-659137176794 | -8.91781 | -54.74971 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53a3bd5d-cfcc-3e55-a54b-560eea5c4857 | -8.91484 | -54.74494 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ec52515-e4f2-34b4-87c3-53cf69381654 | -8.79918 | -54.68304 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 684de2b5-9acc-3c5d-bfe7-7ebbfaba56b0 | -8.79856 | -54.68718 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1391e012-d082-3820-9791-ea87cb36f471 | -8.79559 | -54.6825 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05226279-35cd-3c9c-8847-3ec94db732f0 | -8.79496 | -54.68664 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a43150e-466b-3d0c-8b74-533923f396d5 | -8.79076 | -54.69019 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f37486a1-2e9a-3deb-8bc4-c44c40b446b6 | -8.78716 | -54.68962 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b69b411-0951-3d7c-b267-51abcfaa6360 | -8.75276 | -54.74787 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbb5c91c-7b3b-3f6b-80b2-ce6ca554ba72 | -8.74918 | -54.74731 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d56827ad-36b9-3947-84ef-08e9226f9cca | -8.61417 | -54.57878 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 320dddd8-2325-33ee-93e4-214e973a189c | -8.61273 | -54.58001 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f165cefd-8c34-3ae4-bdd4-578628063af0 | -8.61056 | -54.57824 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0c291f8-ebdc-3663-b16c-e088e38c6af5 | -8.60996 | -54.58239 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b4b329e-5123-3555-8230-9e9ae9a205d0 | -8.60912 | -54.57946 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65ba8594-0727-3643-85d0-a8194caafcfa | -8.60849 | -54.58361 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 743fccf0-6eb9-386b-9e56-32f55663c657 | -8.60696 | -54.57769 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8370e12-531b-30ea-8c33-c79bca95a051 | -8.60635 | -54.58186 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a6b3550-5a49-387d-aee5-950e75f3ab78 | -8.60551 | -54.57892 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 890a66b0-cd39-32ed-8abf-f875a9ae4bb4 | -8.55628 | -54.56283 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 40115e19-2f97-3b73-a068-6b08c70c3984 | -8.55566 | -54.56702 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a7799451-1602-3e4e-a453-1a648a8688a7 | -8.55503 | -54.57121 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2479c020-a55d-36fa-b637-4a1c671a6e62 | -8.55441 | -54.57542 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b014425b-9eb6-305a-8060-6617066876ce | -8.5508 | -54.57489 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cac916b6-0779-3ab9-8b60-03eb5381cd14 | -8.54719 | -54.57436 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 149cf251-2391-3679-9d5d-2eceaf7c3e12 | -8.53998 | -54.57325 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8dd050e4-4519-3811-8aa3-deedcf1030d7 | -8.53936 | -54.57747 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a33394b-1183-3a1b-9d3b-eaad409052cd | -8.53874 | -54.58165 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bb98ced-74de-3bd3-86c9-d3662e2529d4 | -8.53638 | -54.5727 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce0a1c80-01ec-3d81-b0ab-d56f62b205a0 | -8.53576 | -54.57691 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4517d3e0-f32c-34ac-b667-1a77f8c6709f | -8.53514 | -54.5811 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2811c2c8-a114-3999-85bc-5396c37d3031 | -8.5114 | -54.69206 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d146af5-db92-3330-a4e6-7bc262baa6b6 | -8.5108 | -54.69618 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e487a7f-4f19-3392-bb3d-223724fefe0d | -8.50332 | -54.57192 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e09aebb-01e6-3006-b975-b29ed13f0de0 | -8.50217 | -54.56923 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2965b36b-ba7a-3162-a25a-71779f82d075 | -8.50033 | -54.56722 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58be5ca8-28a0-3eb0-b579-9f0a5ead3591 | -8.44218 | -54.67473 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8a167d7-72b6-3d56-95fb-6f8c7602f609 | -8.43859 | -54.67421 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 521e5022-9167-34ff-9804-b6266087acc3 | -8.42723 | -54.67671 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb5cf3b9-67d6-348d-a5e7-ff27f9c80528 | -8.426 | -54.68496 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d1e527e-0b7e-313d-8087-0dbf1911ba2a | -8.42415 | -54.69735 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e72fb841-c0ac-3f37-be3f-f718acbe56f0 | -8.42293 | -54.70552 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f666695d-0140-3533-a315-19578aa1623c | -8.42233 | -54.70957 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05e302c0-ecc9-34a4-9ba2-5546f813e3ae | -8.4218 | -54.68853 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79611686-b76a-39fe-ac49-1a4a1b1361e0 | -8.42173 | -54.71364 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52768153-930c-3a11-9d7c-c099534c7bde | -8.42057 | -54.69681 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bbca27b-6817-3fc9-9b82-64225a5a5bfb | -8.41936 | -54.70498 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f04d797-2c7c-3978-9b2c-c37bb9c1de32 | -8.41875 | -54.70904 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5df9c41-5dc6-32e4-b502-5f5b4a486985 | -8.41815 | -54.7131 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7840ebfa-e7f1-3fc6-8dde-baa31167f739 | -8.41639 | -54.70034 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68559ef0-2a65-3ff0-a1ce-78377824af8f | -8.41281 | -54.69979 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d4a811b-ac84-3877-b9d9-3c13c757b9e7 | -8.335 | -54.76464 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4bdb4b14-13cb-39cf-a6bb-07aaf9e73c27 | -8.33144 | -54.7641 | 2024-09-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf32a081-4967-358a-91f2-da1dad31838e | -9.66017 | -53.53702 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a5b7ab57-c7ef-3bdf-baf1-b4b4fc718c0d | -9.63708 | -53.58828 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e093435-8bcb-3fd1-b240-329631dfa01d | -9.59464 | -54.25695 | 2024-09-28 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f22ee0ba-5b54-350b-acad-0f34967a5e2b | -9.59399 | -54.26138 | 2024-09-28 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfa1659c-09f2-38a8-98f2-18de8d011568 | -10.71269 | -54.1149 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efec7b7c-3d1f-321f-83fa-363e909becf1 | -10.35214 | -53.75569 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f52ec98a-261e-3c89-8c5f-5332219d4d5e | -10.35143 | -53.76056 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cef9eb2a-32af-3259-aac4-d53672feb131 | -10.34963 | -53.75783 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a77daf7e-5216-3273-a0ec-f432c37ff89b | -10.34895 | -53.76272 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 716a5c2b-6a38-3115-b832-c82dd68fea70 | -10.34756 | -53.76002 | 2024-09-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 455f3774-1892-3ec5-8f18-147dd33e4562 | -11.74275 | -54.5224 | 2024-09-28 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6032dbc-1b7a-3577-b920-530a48a9bc84 | -11.68114 | -54.44258 | 2024-09-28 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 24955f07-385d-38f3-84d0-75b63619de48 | -11.67087 | -54.4882 | 2024-09-28 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9bfe503-bf75-313a-a9db-bb98b93a003a | -11.66711 | -54.48761 | 2024-09-28 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9750038b-aa70-37b1-b701-4c6b242aa8a5 | -11.66335 | -54.48703 | 2024-09-28 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0c4a98a-e7da-36b1-8f92-3dc781a18439 | -11.65959 | -54.48643 | 2024-09-28 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 552ff0b9-b490-36dc-aecb-01adf5657bb4 | -11.65937 | -54.48477 | 2024-09-28 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52c70ce3-4a9f-3830-a3ba-c5b983e412b9 | -11.62343 | -54.57338 | 2024-09-28 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11124661-6d2b-3a09-a131-fbfded046dbf | -11.61969 | -54.57285 | 2024-09-28 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3be650b1-1040-3a7b-be7b-7203b7dfbf40 | -11.3892 | -55.18005 | 2024-09-28 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c20ba9e0-b7a5-3fd5-b5c9-3b0618b145fa | -11.28429 | -54.16397 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25389c19-7388-36b9-8494-7affcc463968 | -11.28047 | -54.16342 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e14ec7c9-c124-38d4-acc9-95ddf8187647 | -11.22836 | -53.87738 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9cc1ce3-d105-38c4-9ba1-c07de30fe042 | -11.21626 | -53.9356 | 2024-09-28 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5844d68a-27e6-39ba-8b1e-1d4ca20bdbf8 | -11.2142 | -54.76527 | 2024-09-28 05:10:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ce51fa13-bb67-3191-b850-5334472fea57 | -11.21179 | -54.75588 | 2024-09-28 05:10:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b0cd5107-12cf-3130-956c-afe0970eb95f | -11.21115 | -54.76032 | 2024-09-28 05:10:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 61c45e4b-244a-3694-9851-f052cfac6f0d | -11.21052 | -54.76473 | 2024-09-28 05:10:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |


[Clique aqui para ver as próximas entradas](README82.md)
