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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee10c79a-5630-3116-9c56-3e162433ab7d | -2.82064 | -48.60646 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 22f6241d-40fa-3278-bcc4-e4e4bef90cd9 | -2.81937 | -48.60033 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 71fd6d35-6ae0-3c78-8be6-f3c522dc16ce | -2.81572 | -48.60572 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| da1db475-c8ce-37bf-995f-c44632e3f83c | -2.81425 | -48.68422 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d288b825-c74f-3bdc-982f-abf47a5b696b | -2.81345 | -48.68967 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 0ddce836-878a-38fc-808f-edd6ad02d5f9 | -2.81265 | -48.69512 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 8f69566a-9220-3a76-9a79-930d58ca6ce5 | -2.81155 | -48.68343 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 1d7234a4-6b82-3b61-a7c9-ea4a24b43b4a | -2.81071 | -48.68887 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| c9ddef6f-d6cc-3a58-ac14-b24d1ad5e022 | -2.80987 | -48.69431 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 46060f1e-29b3-3240-9536-dbed16c7fb34 | -2.80777 | -48.69436 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 83fa2484-9096-3459-a79f-a3b2b4df5b83 | -2.80582 | -48.68811 | 2024-10-06 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 7a3a8f67-2a4e-345d-b52a-82a7d0146d25 | -2.20471 | -48.15918 | 2024-10-06 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07209b06-f7a6-3f49-8c92-fcc303b44a50 | -2.16136 | -48.82646 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f95e2541-1112-3934-aa89-cb2c672c537b | -4.73516 | -48.83209 | 2024-10-06 05:10:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81cdf3a3-ea7a-3328-a23d-2dccaf8b2f55 | -4.73475 | -48.83495 | 2024-10-06 05:10:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cfb39a0e-1f35-3af3-8877-0424a68831ed | -4.39362 | -48.71229 | 2024-10-06 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ccb15f66-7bdb-333f-951b-9bc4e5db3297 | -4.3932 | -48.71511 | 2024-10-06 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e72125a2-63c9-32f7-9fe3-bdc185bf7702 | -4.38902 | -48.70887 | 2024-10-06 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3800a169-d58b-3f82-8035-4b27a99c0ab8 | -4.38862 | -48.71158 | 2024-10-06 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b9c6f35-9911-3fd6-8000-af4d43b78cd8 | -4.28056 | -48.64452 | 2024-10-06 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80f242aa-869f-3b21-949a-393be60600e3 | -4.28013 | -48.6474 | 2024-10-06 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a6f32ef-7dc4-3674-903e-f4e1c433cec7 | -4.27975 | -48.06935 | 2024-10-06 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8dca98d4-01e1-345e-8929-e3fa338d3959 | -4.27922 | -48.06802 | 2024-10-06 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f07ce7c9-cc11-35f3-9e57-0e1b1b4d6121 | -4.16277 | -48.60951 | 2024-10-06 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a645c4a-c4c8-3bb2-8177-d57ac1a480be | -4.15818 | -48.60585 | 2024-10-06 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c0a5102-5732-39e1-aa16-5cae8fc2ef95 | -4.10542 | -49.06756 | 2024-10-06 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 706348b9-88cc-3712-be04-53e3d9c89717 | -4.09485 | -48.2662 | 2024-10-06 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 335009b3-2358-303f-87f4-f111c54d45a9 | -4.09441 | -48.26925 | 2024-10-06 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 18e66abd-c1d5-3dd2-97ce-5f9942b175b5 | -4.07652 | -47.94917 | 2024-10-06 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5991ffd-147a-39a9-ace7-d7b79a402089 | -4.07605 | -47.95235 | 2024-10-06 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0983324-3bd5-3d1f-ab2a-fb58aa3093c5 | -3.90961 | -48.3469 | 2024-10-06 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1dc37d59-fb37-394a-954d-6e5e84c6828a | -3.90918 | -48.34982 | 2024-10-06 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 63e7a076-ec43-304d-a137-91b86662753a | -3.90449 | -48.34635 | 2024-10-06 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0a999ff1-350f-37ab-9606-ca4e507b145f | -3.90407 | -48.34922 | 2024-10-06 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 16442a35-c4d2-37b2-a115-7ff39756fc5f | -3.90364 | -48.35208 | 2024-10-06 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1e049756-41ac-3633-8b22-bf825b56982b | -3.90321 | -48.35497 | 2024-10-06 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 178bfcff-6430-31be-b977-9accb9ef66b0 | -3.89941 | -48.34554 | 2024-10-06 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df4b0d56-21de-3973-ad9e-8aace07124ee | -2.14019 | -48.90262 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 483fe862-33bd-3b84-acac-5e511bbea5dd | -1.42129 | -49.3765 | 2024-10-06 05:10:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1e1f3f11-8d42-3113-8516-07e70d63baab | -1.04609 | -48.70536 | 2024-10-06 05:10:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1edd26c1-c82d-3a33-b4c5-88c832abf052 | -1.04213 | -48.69951 | 2024-10-06 05:10:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00bf7f50-683f-36ae-8e97-491627bef3b9 | -1.04133 | -48.70463 | 2024-10-06 05:10:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f344ec9f-c453-35c4-abeb-e60f5cdb0d67 | -1.03739 | -48.69876 | 2024-10-06 05:10:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b1826f6-5c6b-3b73-9b0a-2ecabd0543bd | -3.31773 | -50.45562 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f63351e0-e7cc-3d63-9c1e-8256e204b12d | -3.31711 | -50.45974 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 94084549-2c8f-3bf2-b433-067b7e760b1a | -3.3165 | -50.46389 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 19e3e839-7143-3716-a4ee-c424985c13a2 | -3.31587 | -50.46813 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 004f4e94-ff10-331b-ae9c-6d8c64b45e40 | -3.31462 | -50.44651 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 389e10f5-78d2-3f08-b282-c1b2b9ff1f61 | -3.31399 | -50.45076 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01457e43-fbdf-3dba-8f83-df7921229512 | -3.31336 | -50.45499 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fb3957c4-bfca-3cec-b244-184061e86b2d | -3.31275 | -50.4591 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4fcd4abb-2e7b-3a25-83f4-dc3672db8ce8 | -3.31214 | -50.46322 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bb8f2a18-b534-37fa-a52e-787b82a62de4 | -3.31152 | -50.46743 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 904a55ef-6fbe-38dd-b694-435a83a55e0f | -3.30964 | -50.45004 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 55550ecd-a298-3bbf-a1d2-e775144a759c | -3.30901 | -50.45425 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 58bacaf4-b4c1-3007-aa86-cc131482d90d | -3.3084 | -50.45838 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cd715dc0-3598-3610-8110-8d53fc6b839d | -3.30779 | -50.46252 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e073d537-2f90-3848-9f4b-ec340186d948 | -3.30717 | -50.46674 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d49e0beb-53a6-367c-9f73-b7781c801c59 | -3.30655 | -50.47095 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c1fb677f-38c4-3c1d-9e86-850275fd9885 | -3.30528 | -50.44932 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 41b8a46b-43e8-3cb7-8bff-5d519fb1ead3 | -3.30467 | -50.45349 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47fb8ea0-5114-375e-b0b6-e64fd6cd7a4b | -3.30405 | -50.45765 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b991cca5-4875-37f5-9170-3a0805da607f | -3.30344 | -50.46182 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| da9059ab-d163-3d2e-8c8f-25246dcb594a | -3.30282 | -50.46605 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 846818fa-f938-3ad3-bf1f-bee2406de773 | -3.3022 | -50.47028 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0ecf36db-aba9-39d3-b4cf-5830b0243048 | -3.30031 | -50.45282 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 752bc11b-8f5f-320d-956a-2a6d4218bd33 | -3.2997 | -50.45699 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7788cfe2-9120-3692-a133-4578d85e5155 | -3.29909 | -50.46114 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4aa08a7d-90fc-3a6f-91a2-6cd1938078bb | -3.29595 | -50.45215 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2dc921b3-e2e2-3cce-b090-08a814be1e49 | -3.29541 | -50.44865 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e955e5c-92fc-3efa-87b8-dc9560c4debe | -3.29534 | -50.45636 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1db382ea-c9fa-3afc-b0b7-3153ce0f610c | -3.29475 | -50.45291 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4febe736-9246-3692-a84b-fa95d5c7d2ae | -3.29411 | -50.45708 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0cac446-8203-36d1-bcd9-332d46819433 | -3.2916 | -50.45147 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c349032e-39d6-3c6b-8779-2e7cbae1269f | -3.29098 | -50.45569 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf0beb55-25ed-33ba-8f7e-6c937d60f4a7 | -3.2904 | -50.45222 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a1f80d8-b96f-3a5a-969e-1d54291d5f33 | -3.29037 | -50.45987 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c11de439-f199-3d6f-a9ec-9d4d823fb60a | -3.28975 | -50.45644 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 421b64ac-7ced-392d-bda7-6e1e1e569f29 | -3.28911 | -50.46062 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 07da722b-ad7b-35be-a8e8-8df32f08390d | -3.28724 | -50.45078 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3335e76-6fef-38a8-b9ab-55f0e4d6692e | -3.28662 | -50.45503 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 867a00e3-c420-37aa-8400-7fadd6a49290 | -3.28604 | -50.45156 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1ccd0bdc-9b9a-38f8-a786-606fb1e16271 | -3.21513 | -50.44909 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 86f6e4df-ce86-3b8f-8199-fe4ce3584ca6 | -3.00471 | -49.80814 | 2024-10-06 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 83a84f3a-a1b4-3d51-91cf-589fc8ea2df2 | -2.87695 | -49.47255 | 2024-10-06 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f365efa2-640b-37b8-9b78-eeb4e230325a | -2.80256 | -49.62185 | 2024-10-06 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0573e742-3ff9-3b34-b73d-f284e9f1e746 | -3.38772 | -49.24948 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61688c6b-7cb2-3f44-8cd1-e4995024d3bb | -3.38697 | -49.25458 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d6b026b-dabd-3b9d-9c64-107f67b0002a | -3.32527 | -49.13935 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a525ff0-38d4-3e58-916f-872ba9044ca4 | -3.3245 | -49.14451 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df4b2555-f320-3222-a32f-52c4e2e6e375 | -3.32049 | -49.13861 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b62f7a0-4aa5-3fa5-8918-ee9fbb6bcf5c | -3.31973 | -49.14377 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0483ddfa-2066-3937-b68c-9720b78420d2 | -3.27678 | -49.13712 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9a84d948-c03b-3da0-8e21-870bfd08358e | -3.27659 | -49.13602 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cc08c55d-d04b-37ca-b40b-f0865a63253d | -3.27603 | -49.14225 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b31e8ce3-e032-38fe-8411-686ea1680832 | -3.2758 | -49.14115 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8d115b0c-1260-35c7-9d20-85b72ea526a8 | -3.27502 | -49.14625 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb2eea7c-e83b-3bd9-968e-c9f0a9bb49fc | -3.27351 | -49.12597 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| be2274e3-4fbf-34f5-98c7-e30ea2773d74 | -3.27341 | -49.1249 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| db70d1fc-a690-3b71-a921-9c0001bdc84e | -3.27261 | -49.1301 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |


[Clique aqui para ver as próximas entradas](README98.md)
