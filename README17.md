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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04d707ee-4076-3e74-ad4a-88911c23bf0d | -4.7453 | -55.6478 | 2026-10-08 00:26:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b83e8d8-7328-30d5-885c-e6351bae80ea | -3.1095 | -53.789501 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee446f74-3b3a-3305-a4c5-59f5cc770eb6 | -6.2365 | -52.848701 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fad8a5fb-71f8-3f06-bed5-4f4661d9a410 | -7.3838 | -55.196999 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f14c2f5e-3284-35e8-81f4-efafd9f4680d | -9.8269 | -44.7826 | 2026-10-08 00:26:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 57450111-001c-3833-b7ba-ff338e30ac8d | -6.0438 | -52.7724 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0680698-ebcd-3176-941c-780459f8ab16 | -3.824 | -58.9967 | 2026-10-08 00:26:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 11018719-62b9-302b-b8d3-67b901cf895d | -4.9365 | -55.812 | 2026-10-08 00:26:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d982f0c-f8a8-38ae-b732-a011a9b89703 | -3.5322 | -59.487 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ca18c71-3587-3af0-b61d-66a591d16b6c | -6.7243 | -63.025101 | 2026-10-08 00:26:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8dec3433-e53e-3de9-9af4-69fda1d4eb86 | -6.7351 | -55.104698 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1535146-bd7c-3742-9662-88435b0873a7 | -7.4614 | -42.8363 | 2026-10-08 00:26:00 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e6b466f0-271c-3793-9089-d6956524e164 | -12.2024 | -57.124199 | 2026-10-08 00:26:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4cab4b07-f498-3853-9fa6-144f653c1c4d | -3.2821 | -54.049999 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5713c4db-79c2-3c02-a692-ad0e436feeef | -2.9913 | -54.769199 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b738ebe3-6b6d-37e8-be05-0495e5a25ef7 | -13.1772 | -54.319801 | 2026-10-08 00:26:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4c9bf7a2-4b9e-39d0-b68e-f83541252dac | -7.2311 | -55.112499 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ee836dc-e2bd-3e60-999b-4eccc353d548 | -4.1113 | -54.023899 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b5e3862-9744-39cf-8475-331c6e8645d9 | 3.5399 | -51.276001 | 2026-10-08 00:26:00 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 70db47eb-4283-3318-ae49-13ba06769546 | -8.7035 | -45.147701 | 2026-10-08 00:26:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 76f11b9b-5a2a-3608-be00-5ad4c11db4ec | -6.128 | -53.051701 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7c74bbc-b516-3b7a-aafb-0600662ce04c | -3.0773 | -54.283798 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb633dbc-2c92-3120-a4d1-954ff2876ff4 | -3.0582 | -54.244801 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4403f1f5-7c96-36d6-9bd2-33e8f0d7b919 | -3.0256 | -54.237598 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b60207ee-d443-3331-939d-60d37991eb04 | -7.1869 | -45.336601 | 2026-10-08 00:26:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13e3c05c-a479-3d56-893e-ec9101b1c1f5 | -7.8834 | -54.990002 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a44089a-264f-3317-a34e-ef74b639087c | -5.9689 | -55.362499 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a07da7a4-5b32-3a70-87e8-87a240071c80 | -5.8511 | -53.466599 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 607cab67-8551-3ca5-a8fb-7828ee80534b | -6.1182 | -53.053902 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3d90e9f-b13b-3d0f-8c4d-2ab0724489a4 | -3.5918 | -54.233799 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0b4e67a-ff0b-3c56-8a08-8f9485eb4db0 | -6.487 | -55.284599 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88e00f6d-42b3-323d-bc44-ceccc828c65c | 4.6904 | -60.562302 | 2026-10-08 00:26:00 | METOP-B | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 712a199f-b3c8-30b0-80ef-b224862b3dbf | -6.8069 | -55.287601 | 2026-10-08 00:26:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c6a8ed6-a421-32e3-9579-f4e2485e7cf4 | -3.4764 | -50.087299 | 2026-10-08 00:26:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3d81874-9ee2-3c69-b4bb-c3e11f85b4f6 | -3.2623 | -50.4076 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6b63dda-e49f-39f2-af21-c4d79e09de70 | -3.513 | -54.660301 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd52f029-1899-3a67-84ba-de12b8c0ef68 | -2.4985 | -56.056801 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 623df603-5a24-3e8c-85b4-78faa25dbaee | -2.1549 | -59.204498 | 2026-10-08 00:26:00 | METOP-B | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eb969630-16e8-3447-a28b-318a64b01af3 | -7.2048 | -55.132999 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e166e8f-0542-3d02-9eaa-da95dc37acc2 | 1.7563 | -55.566101 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0242d413-2393-3a61-89f5-2c748bc436c6 | 1.7176 | -55.600399 | 2026-10-08 00:26:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 303bdc06-161c-38ee-9e33-459eee0a9a05 | -3.0336 | -54.091 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a8846e1-6935-3f84-baf1-75d44e414856 | -3.4484 | -60.267601 | 2026-10-08 00:26:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd23ecc1-4071-3b84-b003-10dd40bec891 | -3.6193 | -55.496899 | 2026-10-08 00:26:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0f8a6dd-c98f-389d-a56b-76225f03158c | -3.1667 | -50.4398 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 776c75cc-7a99-34f2-889b-e40b68b526e9 | -2.8621 | -54.107601 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c25dd200-41a3-386c-89a7-71ae2f6a2da6 | -3.0113 | -54.037899 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab051da7-5fe1-3d98-b5de-c8e7f8f0a236 | -2.9614 | -54.1362 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f99aa96-3ad9-3aa3-a317-f3f40b3e0753 | -3.2698 | -54.678699 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e52135f-8164-3c85-a3f7-3cce8f9b7d59 | -2.7856 | -54.088299 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86a4d2d7-da58-3799-bd8d-5566f1a0d1a8 | -3.1352 | -54.3573 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b86f7ac-fdce-3269-812f-7a8fb74a8d90 | -2.8596 | -54.187901 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c71811f-b27c-3bd3-8f50-7e6b11831064 | -5.6796 | -53.483299 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9730a2a1-10c6-34f6-9805-9a927d80a387 | -6.0555 | -59.922699 | 2026-10-08 00:26:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d137c450-d1d5-3244-942b-c34d317ae99b | -3.1858 | -50.567001 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc2c01d6-111d-3301-af43-e5c4ab6c0798 | -3.1811 | -54.605499 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07eed899-6d8f-3256-bc53-af733d154191 | -3.53 | -59.477001 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 06d1c3cc-8f07-387c-9e81-42de67721ea3 | -2.981 | -54.131802 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43909cb4-7213-3ae1-a5f4-e4ae47fced5f | -2.853 | -54.2038 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe1f3310-85af-3c8d-b945-3c0fb6d43414 | -13.8108 | -52.7934 | 2026-10-08 00:26:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0a1a4472-8e8e-302c-b7d9-3d4642c50e45 | -3.5373 | -54.676399 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1459fa5-c69d-3261-8add-3c6e93a7fa73 | -6.094 | -53.492001 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45b84b7c-5b0d-375e-841f-25857c335871 | -3.6347 | -58.93 | 2026-10-08 00:26:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d160b473-666e-3b9c-8a7e-90ca6e92a785 | -3.0338 | -54.2285 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f045bfb-6212-393c-a487-1a9af566009c | -2.871 | -54.1926 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f5b0a48-bd7d-34e0-b836-b6a8e640fd8e | -3.8427 | -55.987 | 2026-10-08 00:26:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23df2ad7-14a1-3a1c-8eea-c361bd4c23f0 | -3.5397 | -50.094101 | 2026-10-08 00:26:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 583f4f3c-ca59-3514-afea-e55e7b4c82c7 | -2.9861 | -54.108898 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86bce974-fdc8-327d-92cb-2dd76e6adf26 | -3.4952 | -51.686199 | 2026-10-08 00:26:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 677f3d5f-e6b7-38ab-b442-2fa05719128a | -11.0928 | -44.0075 | 2026-10-08 00:26:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| afa6327e-7256-3379-a21d-8235ffb808b1 | -3.0548 | -53.911598 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db8f7e13-a9d1-3852-8b02-4c46a64a00f6 | -3.0459 | -57.486 | 2026-10-08 00:26:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b98244d7-097e-3ac9-a1bc-1de65b119834 | -3.1576 | -54.0923 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e3e5098-f01c-3974-aff6-65170e74022a | -6.1499 | -52.6502 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fce60d3-414f-3470-8f34-4cd4d1703605 | -2.8601 | -54.144299 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7203fec1-276f-3229-b402-71e8fc62e5d3 | -2.4608 | -56.072498 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7763384-9b45-3ed3-a098-df49a65bece2 | -3.1047 | -53.768501 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02edcb24-2902-361f-a15e-18598e34088c | -2.9464 | -54.161301 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5651a6c7-bb32-3937-aa99-b24024637939 | -4.9264 | -55.8587 | 2026-10-08 00:26:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b641b59b-88b1-321c-90be-edbf32580179 | -1.1215 | -54.115398 | 2026-10-08 00:26:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce132f24-2500-3a65-9a6b-dad19d9238e7 | -3.1978 | -50.574402 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 799db033-d044-3ec0-8adc-d200a981a117 | -11.3479 | -51.8773 | 2026-10-08 00:26:00 | METOP-B | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 01f3513d-f3cb-36af-b9de-090723ed20bd | -2.8412 | -54.061298 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e24d9fc1-2298-3e67-aa2d-b60a30fcde0e | -2.8643 | -54.2085 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26558ae8-8a5c-3076-bbc2-54a6827a3c4c | -3.5132 | -54.5242 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e6b7622-2228-34d9-9d9c-5ae4156b37ae | -2.9649 | -54.1064 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac9d1945-bb62-3b44-abc1-60353821d7a3 | -6.2577 | -52.851299 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1dfb1a8-6d1d-3f9e-8c98-cbcb386a2789 | -3.5927 | -54.556702 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 665ffc4e-1b06-31dd-b687-50094ca26fa5 | -9.8629 | -50.494999 | 2026-10-08 00:26:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a121117-a053-34d8-8df9-f09da4f898c1 | -5.2111 | -56.073101 | 2026-10-08 00:26:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd3181c9-e855-3b2b-8cd1-bb4190c3025c | -1.5197 | -54.507999 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f93d170f-2acc-3a51-b79a-7ddb84532452 | -3.0825 | -54.261002 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3ba0b5c-b8e8-3787-805f-daf451c52a51 | -4.9552 | -55.114101 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7eb02c6d-b175-3718-9229-979ac641f2a7 | -4.286 | -49.099998 | 2026-10-08 00:26:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1cd8bb7-dee1-3497-bbf0-6a751c8e26c2 | -3.0742 | -54.27 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6186900-005a-3d67-be8e-467dc3892897 | -3.5342 | -54.662701 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b26b015a-6e80-3174-bc3f-e4b11ff975db | -3.2997 | -54.082298 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75a50834-d801-30ea-82f7-f1ad71867ff5 | -3.0135 | -54.139 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 368339a8-087c-3665-9c1e-d61aea64d120 | -16.868799 | -40.612598 | 2026-10-08 00:26:00 | METOP-B | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ad5da743-6db9-3dab-b959-bcde99e8cbe2 | -3.3606 | -50.4767 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README18.md)
