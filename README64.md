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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e78a5041-2908-3c4d-89d1-51b53e1bcbcd | -2.88235 | -50.74268 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 07ea9a85-13f2-39f2-b5da-72acbed34558 | -2.88184 | -50.74571 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 68f2a6db-e867-36d0-b01d-f8e3d5360c70 | -2.88133 | -50.74876 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7645171d-132c-3e7f-8b5a-457fa0bd236e | -2.88082 | -50.7518 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b4ad0ff0-b62f-3361-bfb9-336dcb1119f0 | -2.8808 | -50.7363 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f2ef4d55-a3bb-3f21-8030-f0b75aed3a4f | -2.88032 | -50.73933 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 79e0010a-6311-301d-8d18-33776ce6a487 | -2.8803 | -50.75485 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 97d6c9e9-c66b-3b70-ba49-48895c64cdf8 | -2.87983 | -50.74235 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9e865e30-0399-3910-8ab8-358148cf53f6 | -2.87935 | -50.74538 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| af63bf62-c1b2-36d3-b068-c3ec8c656329 | -2.87886 | -50.74844 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6fe7917c-d416-3180-90bd-e5a506218c08 | -2.87837 | -50.7515 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2b08bcdc-468b-3df6-bf93-e89f8cd717e7 | -2.87824 | -50.73579 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4c6215d0-6c1e-353d-8d51-af91f28c1017 | -2.87788 | -50.75454 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e1bc0014-d785-3cc9-84ef-68378abd05a9 | -2.87773 | -50.73881 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1cc35204-b7de-3a66-ae5a-bcb4fdba425f | -2.87723 | -50.74183 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2c35dfce-8ea3-3618-a403-adcc97c77937 | -2.87672 | -50.74486 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 37748123-cacb-3ee2-abb3-0b168f095423 | -2.8762 | -50.74789 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a83c49f1-1d13-3c4f-968e-811b286ecf32 | -2.87569 | -50.75094 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7cbf4fec-d7a4-36b9-b869-d19f7f2296a7 | -2.8752 | -50.73845 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 28d3dea1-a8d0-3867-a0bc-57b04960cd5b | -2.87518 | -50.75399 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 858278f0-b62b-3888-bc88-095b5d0cf0a6 | -2.87471 | -50.74148 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9c634a69-17df-34a3-be9c-fbae2baea42b | -2.87422 | -50.74453 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8754fd8d-3415-3007-84b0-e15b5fdd1c91 | -2.87373 | -50.74757 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| caa845e5-fcc2-3a49-8e67-cec3babff622 | -2.87324 | -50.7506 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b3687c17-ec5e-3e90-9e2e-92a1be10cadb | -2.87275 | -50.75365 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3dad8530-8801-331a-b3e6-be3080268feb | -2.87262 | -50.73793 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 58dabe93-17f1-3d9d-9cce-9607cbfef6a5 | -2.87211 | -50.74096 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5d1afe7e-6f1a-34db-b7bc-d85f49aec7da | -2.87159 | -50.74401 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5ea02c3e-cf6a-3a13-b7ca-4c3e41d28e2c | -2.87108 | -50.74704 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c97d76af-f627-3d49-94d2-e91c20d96f34 | -2.87057 | -50.75007 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6117545b-eaaa-3990-8c9f-72f4eb66f91b | -2.87008 | -50.73756 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5be72035-7360-3200-9a63-ed13dc2c2b66 | -2.87006 | -50.75311 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 81907732-994e-32be-8fda-1c01e06bc49b | -2.86959 | -50.7406 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4a930ef0-5727-3601-b6c7-9f3c78cb9bd8 | -2.86954 | -50.75616 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 00e77c7d-8364-3640-83a2-e88e8fec991d | -2.8691 | -50.74366 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bc480915-a39d-3aef-ab21-16a1d6973d3d | -2.86861 | -50.7467 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0b70c20b-9412-304f-a6f4-4b71748eb3ed | -2.86812 | -50.74975 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4ea57727-c4d6-3308-97ae-fb1ccaaf1ebd | -2.86762 | -50.7528 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| db352858-3267-3232-a53e-f54b0c586ad7 | -2.8675 | -50.73708 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9a5ae5c5-e2ec-3236-9fae-f159a6c896f7 | -2.86713 | -50.75586 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3d1aa4bb-2dbf-324d-8965-ca6774ad54ad | -2.86698 | -50.74011 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d8f15ebe-f6da-3bae-97cb-3ab667dce324 | -2.86647 | -50.74315 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 139a61f9-a031-30f8-87ea-109651d99716 | -2.86596 | -50.74619 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7bf49888-fb7a-37c1-a746-27f85dd93b70 | -2.86544 | -50.74923 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c5abb14f-86c4-3af2-8392-598aa32c5cb0 | -2.86495 | -50.73671 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c4f1d03f-9f98-3b78-b532-83338a26df96 | -2.86492 | -50.75229 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3a858626-c87a-39dc-ba42-c12768c63079 | -2.86446 | -50.73975 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c4b8d779-496d-30ac-8636-1c35d5a22541 | -2.86441 | -50.75533 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a627ea9a-411e-377d-b27c-bc0163f4f194 | -2.86397 | -50.74279 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| df73c0cb-a158-3488-bad4-4530fa04fb6e | -2.86348 | -50.74584 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b3eae6e0-ad2c-3b46-adc3-7be2d983e37f | -2.86299 | -50.7489 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0ccfbead-c31a-3283-b278-dc4d2c548dbf | -2.86249 | -50.75196 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cd267afb-cd4d-379e-96ba-704114f365cf | -2.862 | -50.75502 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b77e396c-7f96-3b5f-99bc-747a56c333ff | -2.85983 | -50.73587 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c490446d-4919-307a-bb2f-aeb388c68612 | -2.85934 | -50.7389 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 212a88db-468e-3333-9ddb-c64b51e76430 | -2.85885 | -50.74194 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bca9f522-d1e2-3c3d-bebb-11a40ea410df | -2.85836 | -50.74497 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eb8bb7b7-493b-30cb-9f59-67529dceaa0b | -2.85786 | -50.74802 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1c4956ae-b0c1-38eb-abfc-d427dfd43e66 | -2.85737 | -50.75108 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| aff5b84f-8bb1-34cb-b837-c765d2e4e5bc | -2.85687 | -50.75414 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f710306a-e044-3839-9264-4a48a2377c61 | -2.85421 | -50.73807 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 46995f7f-d76e-320c-8225-9c568a4cec11 | -2.85372 | -50.74109 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9deb00cd-d46f-367c-a930-6183b2c5f8bb | -2.85323 | -50.74411 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f6a1ee45-d162-390f-b7d2-574b33e6531d | -2.85274 | -50.74716 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e66ae015-d464-3f2b-b222-258efb588538 | -2.85224 | -50.75021 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2abca224-6280-3348-afc8-7641a9890324 | -2.85174 | -50.75327 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 82e29cef-8c22-3cf6-8122-bb03a0270b09 | -2.84908 | -50.73722 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3aeed158-2a4d-3382-b7b4-c7c4fce55617 | -2.84859 | -50.74026 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6225a04d-237c-386e-849f-64bb02d2c0f4 | -2.8481 | -50.74329 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c18bbae3-ed25-3fbb-8444-59b007358e3b | -2.8476 | -50.74633 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 134ac786-1efa-3fdf-80ee-15c3ced9de8e | -2.84711 | -50.74936 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 37e37293-b424-3e31-8322-d3fffae4f475 | -2.84662 | -50.7524 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c0af928c-5a25-3f3d-9c26-f269f0180464 | -2.84396 | -50.73639 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4b33705-b560-3901-90bf-dfde9f10424f | -2.84346 | -50.73941 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5c0fbeea-71e1-38ea-b553-94642cf6d6b7 | -2.84297 | -50.74244 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 786261ea-fb3d-3f14-8def-ea2afa5ce692 | -2.84248 | -50.74546 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 33e70561-066c-3ae6-9ced-89e6db1ad685 | -2.84198 | -50.7485 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67007668-cfdd-3786-954e-a793542ab585 | -2.84149 | -50.75154 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 747d99bc-a4c4-3df2-95fb-34b2a1bfe13e | -2.84099 | -50.7546 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5df092c2-7aa7-30b0-b92b-7e3d33ed15b0 | -2.83735 | -50.74458 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7061a06-7b9c-3c9b-84f1-4e44002901ad | -2.83686 | -50.74761 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64739ca1-53e1-3103-8aa7-ead9fc9d5b73 | -2.83636 | -50.75068 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 333af0af-8f7f-3351-a941-feb7a9ae01c0 | -2.83586 | -50.75373 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e91fa534-97a0-3286-9446-19e12b2215da | -2.88596 | -50.78402 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22012d81-d71a-360a-83b1-f0717d450736 | -2.88545 | -50.78708 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a98f9c1-ed3f-31ae-b687-2ec1fc7bdeda | -2.88492 | -50.75873 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d841a8b3-12c1-3ef9-9615-7e8a34bb65b0 | -2.88441 | -50.79327 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e4d8965-f4dd-392b-af9e-34b884fd87eb | -2.88441 | -50.76178 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b4a39c8-08f9-3526-ab69-80bf82eba7af | -2.8839 | -50.79636 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2ee06a1-98eb-3c0e-9936-0304684ef11b | -2.88339 | -50.79937 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d30e3127-c988-31ff-9858-27daa70c83d3 | -2.88082 | -50.78317 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e93b832b-f237-3e0f-8bd5-599ad0701e19 | -2.88031 | -50.78624 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61d3c441-a179-3edd-806b-0c68791ab49c | -2.87979 | -50.78933 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78c0350c-ede1-31ae-9ba6-7f5d8aa0c037 | -2.87979 | -50.75789 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 07a5876d-858b-3d78-9567-30f89f7757fc | -2.87928 | -50.76092 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 691700db-a640-3163-81d0-d055f12a79ad | -2.87927 | -50.7924 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f7cb4fd-0f13-3187-952e-89fd55d7e527 | -2.87877 | -50.76398 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 363601f5-8781-37c9-918a-a46dea08dec2 | -2.87825 | -50.7985 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed26db65-6d01-30fd-a6ad-d03788155ae8 | -2.87739 | -50.7576 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fbc5e177-6615-3253-8bb8-f78627e87f39 | -2.87724 | -50.80453 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README65.md)
