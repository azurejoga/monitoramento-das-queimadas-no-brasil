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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f5612d4-0839-3019-aa2e-a392ccd16f0f | -3.82405 | -48.96479 | 2024-10-26 04:42:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efd0a58a-62be-3ad8-9662-993ce55cdfa7 | -3.82123 | -48.96068 | 2024-10-26 04:42:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 435ea717-1e85-3bd1-bc66-b7565b3e79c8 | -3.82068 | -48.96428 | 2024-10-26 04:42:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 021b30b4-8f9f-3ce4-84ad-f70035fb1333 | -3.00508 | -50.48728 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c9884dca-e2e3-39a5-ba49-98fe8c981688 | -0.57645 | -49.50971 | 2024-10-26 04:42:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab4b704d-afae-3730-a01d-75eb40ebecda | -0.57315 | -49.5092 | 2024-10-26 04:42:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f13c0703-91e3-36e8-8c80-b7e132ea67e2 | -0.74152 | -48.63062 | 2024-10-26 04:42:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfd8ed57-d994-3fba-bd4a-60770a003e46 | -0.2292 | -48.79846 | 2024-10-26 04:42:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ce84173-77ca-390b-a162-7555d948c45e | -2.12859 | -49.27464 | 2024-10-26 04:42:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cb96b3e-6ab9-3ab5-8088-6da27a620a46 | -2.05083 | -49.48952 | 2024-10-26 04:42:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a836e542-0c72-301e-93ff-e5b828cef0fd | -2.23078 | -49.14411 | 2024-10-26 04:42:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 250f398b-0cd4-3d22-b8a3-a0b25b6dcc39 | -2.18569 | -48.84187 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c12df572-5cd8-34f9-b646-418fddc2f730 | -2.18514 | -48.84541 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8085b99d-588c-3641-9291-399c1012a049 | -2.18234 | -48.84135 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6329767-3129-335f-b85b-8cc6c7bdd88c | -3.64543 | -49.30487 | 2024-10-26 04:42:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cfeba49c-3f9f-335b-85c6-f11f30fcf5c3 | -3.64488 | -49.3084 | 2024-10-26 04:42:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 86d36980-6cd4-3a0d-bfa4-1cd3f44753cb | -3.54739 | -50.30143 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d078bda8-4c33-3186-9b59-0a1690fa880b | -3.54685 | -50.30486 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd70a8a7-a373-3800-9506-8496f0156d3d | -3.54301 | -50.30778 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e623a5f-4b88-3523-ab12-976d41d4898a | -3.50943 | -50.47844 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60b984bf-7743-35d4-8ece-1aceb2f0d56c | -3.50609 | -50.28445 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53992652-f3ef-3c10-9369-b630fff78db8 | -3.4814 | -50.48463 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a8d8ead7-93a2-32ab-9529-76000f83537f | -3.43292 | -50.25243 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 113e8198-4cd2-35a2-bc4f-ca40929c319d | -3.42961 | -50.25192 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d516151-8445-3ab8-8aed-261ff5c23442 | -3.42631 | -50.25141 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a9a4f23-6ec0-3b5d-bdd9-c9476167738f | -3.42333 | -50.35648 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb56297a-18a7-334c-bbec-0ef00ea05d2d | -3.41902 | -50.38394 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8dcf1440-fe94-3820-a7da-a4d6ece6fa42 | -3.38002 | -50.2231 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7bbe1efa-2e6b-3243-9ee7-b6474fbabf4a | -3.37766 | -50.34585 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32daf54c-d09a-30cf-8fc9-6716529bc7e3 | -3.37672 | -50.22259 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8a8c066c-fc53-3af5-b85d-c5589130b5c4 | -3.3767 | -50.39494 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01e14ccf-4eb2-32be-9d5a-293b98466e3f | -3.36432 | -50.30157 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dda04956-e0aa-38ff-84ed-dbbd33da7d75 | -3.30402 | -50.01374 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b70691c-a11a-3cb4-ab51-c4d805c161d7 | -3.26831 | -50.13137 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c727fb68-b43e-3ae3-bd71-33f7d2bf950a | -3.258 | -50.60828 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c154fa4b-54f2-3ce1-8562-24a61b58bb52 | -3.25698 | -50.2035 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3eefa1c-5dfa-311f-94c2-e089c537e590 | -3.25367 | -50.20299 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 339b3ad4-fded-342f-91b1-1190c33ffe5f | -3.24983 | -50.20591 | 2024-10-26 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad2cc943-4c81-3ab5-a14d-b059f9bd4f70 | -3.24923 | -50.18822 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 825cfd01-f712-3d4d-8e5c-48c4d8a98d62 | -3.23272 | -50.18566 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d0d98859-c581-3c33-9a06-ba27051ec418 | -3.23218 | -50.18909 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a2dd1eaa-cf60-319d-b4af-a943e3936158 | -3.23164 | -50.19253 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 068265d7-4045-3df9-856a-f2b687c343b5 | -3.22167 | -50.16987 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ec9ffa5-e3a0-3474-abe2-9743c8fa4ca6 | -3.21783 | -50.17279 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc5091ff-006a-39ba-89b6-6054a3ea0e9b | -3.21507 | -50.16884 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ecb433e9-2462-358a-a9f0-2cdd53bfb693 | -3.17807 | -50.29673 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9193a9e6-35ea-318b-8d62-d6f9a63ae109 | -3.17477 | -50.29622 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb16caec-107a-38fe-9fd0-c447e1ac3dd4 | -3.16404 | -50.38597 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21c4b3b0-9c1e-33c0-9be1-d2c4fd91fae6 | -3.15876 | -50.46252 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9638538b-f304-35cc-aa1f-8199f4b120f7 | -3.15546 | -50.462 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99f7fa12-724a-37ae-8694-48f36705cba4 | -3.15492 | -50.46544 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e0cd4d2-a985-3793-97a5-14dadcc9b8f0 | -3.15216 | -50.46149 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea9107a5-abf0-3864-85e7-fa9e540fe72c | -3.14718 | -50.45016 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74d07f16-ec39-31b5-95a9-7bc011a5431c | -3.14664 | -50.45359 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a8ce595-686c-3458-8552-c089c6fd44be | -3.1461 | -50.45702 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87178eaa-bf8b-3812-bcc3-4a77fd0a7a14 | -3.14334 | -50.45308 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa1fb388-9304-307f-870e-6b4e97658347 | -3.07369 | -50.50513 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae76f77e-2d95-325a-9f16-513e3ce8a699 | -3.07147 | -50.49775 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c41bc11a-839c-35ac-a6d1-2ca8b93ed652 | -3.07093 | -50.50118 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd252b6a-97f8-3de0-9e78-cf3da2e9d79b | -3.06985 | -50.50805 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65a16c7b-ffed-3600-acef-d0f8dfc6142a | -3.06817 | -50.49723 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce957105-bac8-3740-817c-60237cce1a5c | -3.03742 | -50.5206 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 450b332c-1483-3994-a548-7981b5ea2daa | -3.01587 | -50.48557 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 5a004167-fb84-30f3-aa17-2e0c0808cee4 | -3.01311 | -50.48162 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 7cc43fc7-791c-3c3f-9a40-47c08e801951 | -3.01257 | -50.48506 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| b9af1d88-9d45-31e8-bd59-498e8e7ae63d | -3.01202 | -50.48849 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ea6644a1-1265-356c-950a-4f069081074a | -3.00872 | -50.48798 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7d89baf9-9893-388b-ab14-96ef099a579d | -3.00231 | -50.48333 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 8fa75f91-45f4-36db-8a55-1cfe929e6743 | -3.00177 | -50.48676 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a63e4176-d79f-330f-aa2c-cad5a0a75b9d | -2.99901 | -50.48281 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7404c370-8cf5-3499-8a3c-0633390b7fbb | -2.99463 | -50.48917 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 05df0e4b-2533-3aa6-a547-fc957591e1de | -2.99241 | -50.48178 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 02d61ad0-2fed-39ef-9483-9d564eda2114 | -2.99187 | -50.48522 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fdd68b74-e2c1-303d-a109-5b6df96e30ca | -2.98745 | -50.29815 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b35a1fc-116b-3be3-b40c-aa989c1675e1 | -2.98193 | -50.29026 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c873b18-5107-383a-b7b0-9ebe0108d64b | -2.96911 | -50.41483 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba1af2a5-77e7-38e9-bc78-d771a30c8ef0 | -2.96694 | -50.42856 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51a00e73-5a76-3349-8f41-aa97ffec709d | -2.96526 | -50.41774 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59f8de4f-e199-3a21-9cd8-9823cb0cf412 | -2.96472 | -50.42118 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89447e3d-a1fa-3fe1-9207-6a1939c2fbf8 | -2.96418 | -50.42461 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d00376f2-5d47-32f3-a10e-c039ed09da54 | -2.96088 | -50.4241 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fbeb3152-52a0-3bee-8b60-d5a1506037cb | -2.95704 | -50.42702 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fc515376-f104-31ea-a42b-7d22f9e80dd8 | -2.9565 | -50.43045 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 896e3584-6221-3c21-88cb-664eb511055d | -2.95566 | -50.52181 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c965410b-c3d4-32f4-a15a-d690f7f35948 | -2.95512 | -50.52525 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c26a96b-68f2-3e08-b8e3-021acfa74f27 | -2.95458 | -50.52868 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02152d33-3380-3ae7-89c4-7d9c987c9782 | -2.95428 | -50.42307 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e78d9361-c4d6-3af2-bcb5-d7887c33b800 | -2.9532 | -50.42994 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2043c313-fe5d-3720-b895-1e8395ddc9ee | -2.95236 | -50.52129 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a975842e-1592-3d75-91d9-c37d291860b4 | -2.95127 | -50.52817 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9edd5a6-68c9-35af-aa2e-8804a1928071 | -2.95098 | -50.42256 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 32a3deed-ef04-3ef3-bee8-19bc51b27f12 | -2.89533 | -50.40704 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b2eeacf-f450-3eee-9e93-67ea10ea6010 | -2.87956 | -50.46436 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e59f3727-9fac-386a-bd4a-f11506cb939b | -2.87902 | -50.4678 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08c6f874-68e6-362d-9dd7-aa91871b1d44 | -2.8766 | -50.39709 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58f67580-08e6-3b13-b17e-d1c1ac916fa1 | -3.22942 | -50.18515 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 93586d43-e9c9-321a-9124-4505ad00d85a | -3.22888 | -50.18858 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fd06ab9c-624a-3ada-b4f2-1ae925c0f780 | -3.22113 | -50.1733 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c65515f-31d1-354a-935f-7468830e3b25 | -3.21837 | -50.16935 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7444522d-c4d6-3aa3-b45d-ef444c651818 | -3.21453 | -50.17228 | 2024-10-26 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README66.md)
