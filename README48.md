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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6dca02f4-600b-33cd-bca9-708579c03782 | -2.98388 | -51.0321 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5461b037-5f98-324e-b1f6-16ac2e8f47ac | -2.98327 | -51.03594 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de7f0931-a32b-32ec-ab81-79732cc3a6f4 | -3.72098 | -50.71669 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 391690a7-bad4-3c5d-9582-e8832c7d56c6 | -3.72037 | -50.7207 | 2024-10-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ddb5178a-5dad-33e0-ac9c-9dae15eff65c | -3.2772 | -50.66166 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 297973d2-2d56-357b-9cc3-3962e33a1473 | -3.27659 | -50.66565 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57142ad0-b47f-3f57-be28-5afde1890653 | -3.27365 | -50.6611 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d4ad047-532b-3e0a-9e2c-b48e5e380833 | -3.27304 | -50.66509 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da5a6118-886f-37e3-ad7c-636bbd4d12e2 | -3.26949 | -50.66454 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a890f1c-9e31-31f5-8757-44578afb07ec | -2.90073 | -50.70999 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9c92f17-d7d1-3969-86a6-7b1c9c074879 | -2.40719 | -50.43948 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6a7039a-889d-337b-868b-bdc66e819845 | -2.40364 | -50.43894 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8aab26a4-0941-31f7-b995-d583c3f17b3a | -3.54832 | -51.52186 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5fda15da-849f-3d16-abca-2fcd22f7b96d | -3.54489 | -51.52132 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e851685-10ab-3430-aa24-7c081ca0deb9 | -3.54125 | -51.38654 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0b8bece2-0183-3e7e-bc1b-f7e1298d402b | -3.53639 | -51.48571 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ac6345b-1c21-3955-9e56-c4949b970b6c | -3.51215 | -51.59622 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53cdb2a2-a8ea-3ff5-8d6a-c3c923da263f | -3.50873 | -51.5957 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5dae45cd-4b64-3f95-8ce2-f5320c5aec85 | -3.4744 | -51.20983 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0ae7655-c914-3773-b9db-0d0cc9d7d4bf | -3.4738 | -51.21366 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57209078-525a-31db-bcad-da7f7f097ff3 | -3.3874 | -51.42898 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac2468a3-f687-31bc-8441-39e974e5c321 | -3.36792 | -51.50988 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96530eee-fcc5-304f-92e8-1f24ef009551 | -3.27067 | -51.61694 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3ad20c3f-3b61-3f70-993f-55eb472dbab5 | -3.23561 | -51.27988 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13e82ca6-4b51-36e2-aaaf-e3b14a2acb7d | -3.23502 | -51.28368 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 250b934b-bb03-33be-81f8-5e5dce30a4ea | -3.23216 | -51.27935 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed6bcfcf-9736-3bf8-9e99-6b34d7b6f65b | -3.21757 | -51.35043 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c96212c-57dd-3de8-9873-67d7a3d04aa1 | -3.1798 | -51.25201 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3a0c613-77fe-3e4e-a261-251af3cf0154 | -3.17921 | -51.25581 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8520cd15-db51-3f2a-b147-cb0e2733e586 | -3.17634 | -51.25148 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9b69d43b-5212-375a-8e67-1321b7dc4bc9 | -3.17576 | -51.25528 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| be003614-e5ed-3765-a4e6-a7dd29a1d276 | -3.16688 | -51.25025 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2fdb6c6-5ffd-3afa-8c71-7a064aedfdfe | -3.16628 | -51.25404 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8d24a26-68ec-3f5c-bfde-2ca6953868e4 | -3.16598 | -51.24985 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5efdc99f-9d93-3303-be6e-134cbcb51e2d | -3.1654 | -51.25364 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3df48857-021c-350d-87c3-c1e627e1bc42 | -3.16283 | -51.25348 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 068ee24b-62ac-3dbf-b82f-ba327e774f62 | -3.14687 | -51.35512 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76ed41bd-f56c-38f3-ae47-0226b2da0952 | -3.14296 | -51.49202 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6340ec75-3083-3574-a445-bf14b4692d64 | -3.12739 | -51.3445 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b0fabfe7-b542-308e-ad11-5998033a88d3 | -3.12681 | -51.34823 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4e99f1eb-43d2-35bf-b2d4-e671306ab612 | -3.12395 | -51.34399 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e07a0cbd-3f79-33d1-9857-ecd3a8b5be20 | -3.12336 | -51.34772 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a05b1584-7eab-33dd-8de3-34e097efebcc | -3.11135 | -51.33437 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10dea7a5-17eb-3af9-8a21-b2b4a6eccb00 | -3.11077 | -51.3381 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 068054c6-00ad-38ca-8b38-788f6f93f1a0 | -3.09031 | -51.21927 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eabbff17-d7e0-334c-959a-fc14b82bc8ef | -3.08972 | -51.22305 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5b78053-68bd-3be1-a0ef-883c743453f7 | -3.08744 | -51.21492 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85b557e9-b03e-3f7d-a20a-8b0e3f762ccf | -3.08685 | -51.21873 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c0b451f-4b11-34d1-a938-ce5ac9e8e908 | -3.08627 | -51.22253 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebca3001-ced4-398c-be71-ec61617ee4a0 | -3.08456 | -51.21059 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5b0b5d2-938c-349c-9a3e-e54abddcc044 | -3.08398 | -51.21439 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee11ffed-4f83-39fa-a903-7146761d8f9b | -3.08339 | -51.2182 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c10166f9-a81d-34f3-9c26-c3217cc7a72e | -3.08052 | -51.21387 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 841dc792-64bc-34e2-8775-e24489bfd374 | -3.07993 | -51.21768 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8619c730-8c05-3ae8-9a1c-ee13b8ea471b | -3.07648 | -51.21714 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c11d8ec-31e6-36df-8b6d-ea90163e38f3 | -3.0753 | -51.24789 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5490797a-c3f6-3003-9566-f79a89a92959 | -3.07472 | -51.25167 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7e7b72b-24b0-3950-9fc2-881fbef5078a | -3.04481 | -51.33613 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2207d1a-0d0d-3cdf-a7eb-b12209eb48e9 | -3.04422 | -51.33556 | 2024-10-20 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df51bfdd-9a26-3ee4-90ec-1ccd3e46ab50 | -3.43271 | -52.06143 | 2024-10-20 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9f352daf-5cf6-3796-82fb-a8fa65aee837 | -3.37337 | -52.13288 | 2024-10-20 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b042743-ab8c-332e-9bd9-ffa3ee3f8488 | -3.3183 | -52.12091 | 2024-10-20 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 059a5bb3-3690-3fc7-bafc-29677fc77dd6 | -3.39162 | -50.66981 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d30fa77e-8d4c-31c2-b630-8b2d66d91d95 | -3.38867 | -50.66527 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| d1e7899b-42fe-314f-aca0-62e32356c23e | -3.38807 | -50.66924 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 882aa15b-2f18-38b7-a2cd-3ac4300ce00b | -3.38746 | -50.67324 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 88077bd9-7481-3856-8eb2-2689e64a2d21 | -3.38685 | -50.67726 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e86bc3c4-dd47-324f-a33b-ae7e995b8d9c | -3.38512 | -50.6647 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 480885e8-1ef8-3a0e-b6e1-6acfc8349bf2 | -3.38452 | -50.66868 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 502d0667-fe9a-3a62-94c6-b920c5f32bd0 | -3.38391 | -50.67268 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| c38a2f92-b063-3edb-b3e6-93725bf5d174 | -3.38157 | -50.66414 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8da5779-5836-302c-a53a-98a8c4a09550 | -3.38097 | -50.66813 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f4d2472-b31f-3668-bcf9-27f8ac7230e2 | -3.38036 | -50.67212 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24c93a95-6219-3fbf-953a-a61833287a48 | -2.45876 | -50.99751 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8cb24ecf-d8bb-3dc9-b594-257f21f0337a | -2.45059 | -51.36901 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6e9b4a35-c263-305e-87fb-e8a8ac9fd13f | -2.39587 | -51.80789 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64e6a43b-06cf-3366-845e-9aa2036e5892 | -2.3925 | -51.80737 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 870c50d4-8aa4-3e45-a0e6-6b6322391291 | -2.27038 | -51.24379 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6773ab6f-c54f-34d7-a58a-396a8a3ea780 | -2.26637 | -51.24697 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d8cf325-9110-3129-a137-695c94421d59 | -2.26294 | -51.24643 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0131f23e-13bd-30cd-bd1e-922147c4104b | -2.21979 | -51.88705 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67a3b3c3-7853-3aad-84e3-50eed5fc25da | -2.85204 | -51.28762 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8285a480-d07f-3116-8834-724ccdaadb81 | -2.85146 | -51.29137 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9ac2a4b-886e-38de-a135-b50da3ddf8db | -2.8486 | -51.28708 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51a1a375-93e1-39ad-a721-adf789177efa | -2.83884 | -51.30478 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3c53db3-e56a-3d39-bb81-c03a5ddda4dc | -2.83597 | -51.3005 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bbee403-ac23-30c4-804e-ca2e3bb41d66 | -2.8354 | -51.30424 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fe92512-8691-3a11-8b35-001ad93562ba | -2.83483 | -51.30799 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 307950d6-24d0-3fc2-b734-06f2a8f0aa8d | -2.83296 | -51.30123 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f098ab5-084f-3188-92d0-e4e51e0b34d7 | -2.83254 | -51.29996 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb1a412e-3124-3795-bfe8-5c890d4f113d | -2.83237 | -51.30496 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5d3310c-f8f3-37d7-88c8-6096ba224545 | -2.83196 | -51.3037 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcc18276-d64a-3998-bafe-def27d4b1295 | -2.82617 | -51.27715 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 835bbcb4-d933-3f00-b7f4-8c396e55ded1 | -2.81903 | -51.345 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89b0e2b4-f5fb-3835-8a4a-512dbff8933e | -2.81845 | -51.34872 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ef9b407-00c9-3e8b-9901-ea829670c5e5 | -2.81619 | -51.34074 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d10782ca-cdaa-3971-bbad-c92c60570aaa | -2.8156 | -51.34447 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0190627-2716-3660-8a87-0ab1f4ad81e4 | -2.81502 | -51.34819 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ab32131-61c9-3b2d-b474-26d4ad4b401e | -2.81275 | -51.34021 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf2ade7d-a047-3341-bae5-ca39b2d167bf | -2.81217 | -51.34394 | 2024-10-20 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README49.md)
