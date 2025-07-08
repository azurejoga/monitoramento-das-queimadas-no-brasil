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
| 82e3087d-764f-3dfa-8ae6-c11a531fc273 | -10.6299 | -49.4504 | 2025-07-08 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 4cba8a7a-0bbf-3dbc-9965-2ac69e6674af | -10.6296 | -49.472 | 2025-07-08 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 90a58081-5a33-378b-b7f2-e94966b40c1d | -10.6486 | -49.47 | 2025-07-08 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| b0e19258-2c25-374f-86dc-efe225353c78 | -10.6489 | -49.4483 | 2025-07-08 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 23e58edb-f1e9-3c3b-8ec4-a12854b7b583 | -10.6299 | -49.4504 | 2025-07-08 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 8f1df842-2e15-3493-b6ec-5316643ce3ee | -7.2594 | -43.0881 | 2025-07-08 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 134.6 |
| ca1f969f-4d25-3b94-a627-5d9b11a0be8d | -7.2597 | -43.0645 | 2025-07-08 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 107.6 |
| f6e73b74-1d46-3c4d-9369-b1f7b49175ee | -10.6486 | -49.47 | 2025-07-08 01:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| a328581a-b36b-36e0-9fa9-b179b699dfcb | -7.2023 | -43.1406 | 2025-07-08 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 496e975b-19a7-30e5-98c4-c15bf5a67077 | -10.6296 | -49.472 | 2025-07-08 01:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 43bd8856-cfee-33d2-afbe-326cc6f31eec | -7.2597 | -43.0645 | 2025-07-08 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.2 |
| 1ff09b05-87ac-36f3-acc4-4a99b20a99af | -7.2594 | -43.0881 | 2025-07-08 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.1 |
| e437f19d-c3f1-3616-b08b-253d80ed7955 | -10.6299 | -49.4504 | 2025-07-08 01:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| f10ef80b-2fc3-3049-b7f2-49b0090bb27b | -10.6489 | -49.4483 | 2025-07-08 01:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 6137d347-164a-347f-8e5e-df6e1d7ed664 | -10.6299 | -49.4504 | 2025-07-08 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 54f6192c-604f-3a1e-bca6-4db76462e377 | -7.2597 | -43.0645 | 2025-07-08 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 084ec2da-d349-3620-bafe-75cc1521b060 | -11.4393 | -45.1154 | 2025-07-08 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 1002eb0a-ec46-368d-9c0f-7308549befc2 | -11.4201 | -45.1181 | 2025-07-08 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 3d6e8c9c-4ebd-3d07-8ba9-8164aa18b53a | -10.6486 | -49.47 | 2025-07-08 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 872a869c-3e2c-3fec-8c92-d8a544a4f157 | -11.4397 | -45.0923 | 2025-07-08 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 034823e4-09ba-3a65-acfe-6dd4c43ef016 | -11.4205 | -45.095 | 2025-07-08 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| da381528-c997-3a09-9d69-42e4f9742d3b | -10.6489 | -49.4483 | 2025-07-08 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 984be84f-0a62-350a-9f25-b65cc8d4f1a0 | -7.2594 | -43.0881 | 2025-07-08 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.8 |
| a15b4253-6c7b-3a7a-b901-233b069fc17f | -7.2594 | -43.0881 | 2025-07-08 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| 544a0acd-70d8-36d4-afe7-178a49433acb | -11.4393 | -45.1154 | 2025-07-08 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 7250cbde-b587-34a9-9dd4-8548dd68b345 | -10.6299 | -49.4504 | 2025-07-08 02:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 9e2fda15-8a1b-3fb9-875a-95731fce81fe | -11.4205 | -45.095 | 2025-07-08 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 69378107-62c2-3c1d-8bc0-8abba65c870e | -10.6489 | -49.4483 | 2025-07-08 02:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| d3d49863-bf62-3ac6-933a-171153612857 | -10.6486 | -49.47 | 2025-07-08 02:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 5a8a76ca-ebab-380e-a249-4bcfdab55870 | -11.4397 | -45.0923 | 2025-07-08 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| a5555dbd-458a-3b78-a220-105487196fca | -11.4201 | -45.1181 | 2025-07-08 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| d9a11b1c-834b-3774-a71c-bae23ce1f86d | -11.4397 | -45.0923 | 2025-07-08 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 118.4 |
| c88f3736-427d-37e5-a4d8-bce3324252ad | -7.2594 | -43.0881 | 2025-07-08 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| 316a84d1-566f-3451-878a-1a9cb20229e0 | -10.6486 | -49.47 | 2025-07-08 02:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| f273f0b3-8bf0-39a8-af79-22fdcd8c61fa | -10.9811 | -45.1104 | 2025-07-08 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| f79e10b7-e914-34ba-8c71-25f9fb85a1e5 | -10.6296 | -49.472 | 2025-07-08 02:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| a2f45fca-aa02-320b-a48b-7c95af5f3d8e | -10.6489 | -49.4483 | 2025-07-08 02:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 66d02cda-5902-3667-99b7-82f3097d3596 | -11.4205 | -45.095 | 2025-07-08 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| c7cdb174-911d-3397-aa68-e1ac3d13e537 | -10.6299 | -49.4504 | 2025-07-08 02:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| f290cab3-3b1f-3892-a53a-6e69434ae985 | -11.4393 | -45.1154 | 2025-07-08 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 97d5106e-c1ee-3b64-ad8c-ca9f7ff3e66b | -10.6299 | -49.4504 | 2025-07-08 02:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| a799da3a-0813-3697-baa1-5a6ba5bce5b9 | -11.4201 | -45.1181 | 2025-07-08 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| e64c4875-142f-3c95-b517-3963d724d2af | -10.6489 | -49.4483 | 2025-07-08 02:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 9b200eda-67a9-3249-afec-a2bd48f2cd67 | -10.6486 | -49.47 | 2025-07-08 02:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 96f06d87-315c-3b5f-8ffa-4a0f640bcb5b | -11.4393 | -45.1154 | 2025-07-08 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 25aa3f9b-91a1-3231-a29c-993b5688e67f | -7.2594 | -43.0881 | 2025-07-08 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.5 |
| 009c31d5-a769-390b-a2a7-0932c228aec7 | -11.4397 | -45.0923 | 2025-07-08 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| c2801a2c-5bc3-33d6-ba0f-0f9377a9954f | -7.2597 | -43.0645 | 2025-07-08 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.7 |
| 4e517c41-beb9-3e95-a391-b94ff3950ede | -11.4205 | -45.095 | 2025-07-08 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 016f6dfd-eafd-33d9-b6f7-267fd2f54f52 | -10.9811 | -45.1104 | 2025-07-08 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 80e9975e-6967-3c25-96d7-61f96bdad70c | -11.4205 | -45.095 | 2025-07-08 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| e2681cc4-4a14-3376-ac16-e1c49c0caa24 | -10.6489 | -49.4483 | 2025-07-08 02:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| e93face0-773b-3101-b5d5-0feb0ee9dafa | -10.6486 | -49.47 | 2025-07-08 02:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 236aed41-ab8e-37e5-bd12-d93f0570f278 | -11.4393 | -45.1154 | 2025-07-08 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 70c799c2-7467-33be-8865-e1832172b7c2 | -11.4201 | -45.1181 | 2025-07-08 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| b8b5b03c-b729-33f1-be24-d203e3d81690 | -10.6299 | -49.4504 | 2025-07-08 02:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| b13a12a1-8fa4-3c35-9c37-b333ff2ff791 | -11.4397 | -45.0923 | 2025-07-08 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 60cd7c23-a705-3536-baba-12f11fe21904 | -11.4393 | -45.1154 | 2025-07-08 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| e18515b6-7c70-36cf-9729-b2b4c23aca1d | -10.6299 | -49.4504 | 2025-07-08 02:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| f6898846-ced5-309e-b036-155a7ead5d79 | -11.4201 | -45.1181 | 2025-07-08 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| e7293bbe-e197-32f2-9f13-6c887e4afde5 | -10.6486 | -49.47 | 2025-07-08 02:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| a26f4b69-7318-37b5-b46b-319f04dd72e2 | -10.6489 | -49.4483 | 2025-07-08 02:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| a03081dd-5453-3e48-9006-55f4b88ca402 | -11.4397 | -45.0923 | 2025-07-08 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 615d4f57-1147-3840-957c-fd905d8c1bb9 | -11.4205 | -45.095 | 2025-07-08 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 87667af4-15f5-3aa7-8317-b91f5c21512c | -10.6299 | -49.4504 | 2025-07-08 02:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| f1661f73-5aa1-3f90-8e3e-ceccade103b6 | -11.4397 | -45.0923 | 2025-07-08 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 3cc31e90-9fb3-3294-b0e5-8d4ae03820b6 | -11.4201 | -45.1181 | 2025-07-08 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 5356aa9a-c13a-30ae-904e-6ab881ce0042 | -10.6486 | -49.47 | 2025-07-08 02:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 8304eea7-5312-3edb-867e-a20f21f992e4 | -11.4393 | -45.1154 | 2025-07-08 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 313dbff2-1b09-381b-9164-3c5a2035b4ea | -11.4205 | -45.095 | 2025-07-08 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 7cf4b15c-9549-3539-963d-b37c71e258c9 | -10.6489 | -49.4483 | 2025-07-08 02:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| af882b7f-ff27-3bed-99ec-26523999c847 | -11.4397 | -45.0923 | 2025-07-08 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 536824bf-86e5-3111-a234-0682fac75638 | -10.6486 | -49.47 | 2025-07-08 03:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 7024eb0d-be85-334a-b0b3-8484b9e96733 | -11.4205 | -45.095 | 2025-07-08 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 134.7 |
| b701a212-4517-3a4e-8e9e-ec822a33b0a9 | -10.6489 | -49.4483 | 2025-07-08 03:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 38704c32-c3fa-34ac-9a89-09a1c2dd2325 | -9.2255 | -48.6 | 2025-07-08 03:00:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| af453841-d708-337c-92ea-c8875d3668fd | -11.4393 | -45.1154 | 2025-07-08 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 8a009d56-64c5-38ac-a828-fbe0bb383293 | -10.6299 | -49.4504 | 2025-07-08 03:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 9a803438-6d97-3cae-b1fe-d523e4a49596 | -11.4201 | -45.1181 | 2025-07-08 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| bcc2dab1-534d-3f2e-8a73-56180aa7f157 | -17.89035 | -39.79092 | 2025-07-08 03:04:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6b4f3c36-56a7-3168-aeff-b2242d7e5f16 | -17.88482 | -39.79092 | 2025-07-08 03:04:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8aa1a2ab-fd30-3d94-87c8-45787403c5f4 | -17.8913 | -39.79257 | 2025-07-08 03:04:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 153fe3e5-50c1-36c6-aa2c-a4d1d8589d8e | -11.4205 | -45.095 | 2025-07-08 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 9d222a3e-bd12-3644-adb4-5fc663347996 | -10.6489 | -49.4483 | 2025-07-08 03:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| d8b68a6a-07dd-3ef9-81e6-9f530561555e | -10.6486 | -49.47 | 2025-07-08 03:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| f296fa32-c5dd-3390-a9e5-5fa4e91e733b | -11.4393 | -45.1154 | 2025-07-08 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| bd595e5f-c1e2-3e7c-887b-972001a14da3 | -21.4127 | -51.1569 | 2025-07-08 03:10:00 | GOES-19 | FLÓRIDA PAULISTA | SÃO PAULO | Brasil | 3516002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 103.3 |
| e395ac8d-45df-3aa2-9dae-a82e13528fb7 | -11.4397 | -45.0923 | 2025-07-08 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 6c4819a1-7053-3f35-ba7e-36f2a9fb7c79 | -10.6299 | -49.4504 | 2025-07-08 03:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 2de6cc39-6258-388d-a3a8-3d5d9fc1cff1 | -11.4201 | -45.1181 | 2025-07-08 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| dd57e18d-7f82-3748-9260-fa4db605dbcf | -10.6299 | -49.4504 | 2025-07-08 03:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| c39d1d2e-2c82-30bf-a994-2af7468b1e5f | -11.4393 | -45.1154 | 2025-07-08 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 2d515a48-723c-306b-9e0e-f12309580d5d | -11.4205 | -45.095 | 2025-07-08 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| bf8fce1c-36f1-3b09-be9e-2905e76440a0 | -11.4397 | -45.0923 | 2025-07-08 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 916b3d8f-bd2b-3278-b96e-d5f1e341c5a4 | -11.4201 | -45.1181 | 2025-07-08 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 9d93360f-d810-36e1-b230-339b7539400f | -10.6486 | -49.47 | 2025-07-08 03:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| ed6f191c-93f7-3be2-8274-92538a29dcda | -10.6489 | -49.4483 | 2025-07-08 03:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 02dae888-c0e1-3149-9214-b5257a385347 | -7.27341 | -44.64225 | 2025-07-08 03:21:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cf6ae017-507f-381c-aaeb-aa9f065b8f5d | -7.24999 | -43.0755 | 2025-07-08 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| b6d0c41d-f4d6-367f-a4f2-aa31bed5016e | -5.83479 | -44.10765 | 2025-07-08 03:21:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README4.md)
