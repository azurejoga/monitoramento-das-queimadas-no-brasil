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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d111f2e8-117e-3ac0-847f-3f334ad9be67 | -5.93208 | -43.36518 | 2024-10-20 00:24:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 4d75fe8d-c80d-332b-9f18-59d09871672b | -5.94621 | -43.39668 | 2024-10-20 00:24:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 6235e622-c6c3-3718-b021-7566fcf1051f | -3.63202 | -45.85261 | 2024-10-20 00:24:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 7268dd5a-4411-3c26-a629-4e45047064d9 | -3.60715 | -47.51628 | 2024-10-20 00:24:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| a36541ea-6c23-3edd-9426-3ab76f6cd45f | -3.59926 | -50.57584 | 2024-10-20 00:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 4bf92def-6a02-3cfa-b64e-98b1db588198 | -3.557 | -50.32758 | 2024-10-20 00:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| db6245f2-425e-30d2-9f54-61549ee0e8f7 | -3.55263 | -50.29391 | 2024-10-20 00:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 275d58ce-4761-3a86-9f3a-b8a8ebe363ba | -3.54993 | -45.83965 | 2024-10-20 00:24:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 4c4a4281-364c-30f2-9afd-87c171c2af20 | -3.54949 | -50.33381 | 2024-10-20 00:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 4acf12dd-5e39-3d9a-a7a7-4ef3858d310b | -3.5479 | -45.82469 | 2024-10-20 00:24:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 784c6872-f55e-349a-a84f-9ae013774337 | -3.54489 | -50.3001 | 2024-10-20 00:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| d51e8186-a78b-3bc0-b9c7-25a358620f01 | -3.43468 | -44.24902 | 2024-10-20 00:24:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| c0d036ab-0e98-306d-af9f-892a14fdedfc | -3.39884 | -50.6869 | 2024-10-20 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| ab8df488-80a3-3b5f-9aa2-096fd77b3217 | -3.39398 | -50.65093 | 2024-10-20 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| f6c1a30c-092f-3999-87f7-922ac7fe2dd1 | -3.38776 | -50.68351 | 2024-10-20 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 162.0 |
| 138dbb41-7b44-3912-942a-b8f00be8ccfb | -3.38316 | -50.64737 | 2024-10-20 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| f4d75b17-7c80-3c2f-9ef9-9e5c4e11f85a | -3.38225 | -50.6893 | 2024-10-20 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 71d45c2e-791a-38a0-8642-0e4f17cb5462 | -3.37744 | -50.65339 | 2024-10-20 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| ed9ef313-53e2-32f2-8776-23e43b4a8a38 | -3.30336 | -44.48082 | 2024-10-20 00:24:00 | TERRA_M-M | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c5727bc3-41fd-3dc8-a7ac-0f3e03088a7a | -3.04647 | -51.02115 | 2024-10-20 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 8ab7f0cd-4970-38b4-9ae9-87036c36db7d | -3.04266 | -51.02832 | 2024-10-20 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 9e4bf77e-ba9c-3ba4-b70f-769dba78baf4 | -2.98101 | -47.91911 | 2024-10-20 00:24:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 0a3d6e2b-0012-3b32-948a-77b5d83a0591 | -2.78838 | -49.32866 | 2024-10-20 00:24:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 99edd1fd-70b2-304e-9a76-7d8cb8f1255e | -2.78833 | -49.32211 | 2024-10-20 00:24:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 141.3 |
| 4909defe-824c-3580-9d64-c9134fd33b7e | -2.7847 | -49.29469 | 2024-10-20 00:24:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 247.1 |
| 36ad702e-c55c-37e6-a836-45480779c7b1 | -2.78454 | -49.30126 | 2024-10-20 00:24:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 330.0 |
| 42725f9a-6cd3-30ff-9c76-a422ca18b48a | -2.77017 | -49.41583 | 2024-10-20 00:24:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| b96b1f85-ccb8-3733-acda-3944aa59f260 | -2.7695 | -49.40939 | 2024-10-20 00:24:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| dd5a9e64-57f8-32ee-b039-efd8bc0d2ff2 | -2.76095 | -45.36413 | 2024-10-20 00:24:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c2dafa54-7e6c-3735-81ef-8cc6f8ed3e58 | -2.65584 | -45.50818 | 2024-10-20 00:24:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 97ede020-8d65-34f2-93e8-a2c5e2d237cc | -2.6341 | -46.92316 | 2024-10-20 00:24:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 3948a10a-7600-3b7f-9640-21b0dc745583 | -2.63166 | -46.90576 | 2024-10-20 00:24:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| ceb832f1-8b56-35ab-91ed-9a8ec795c646 | -2.62615 | -46.91767 | 2024-10-20 00:24:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 6928a544-84e9-3de7-a875-27b586b2eb65 | -2.62384 | -46.90018 | 2024-10-20 00:24:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 9f8e2183-1c65-3ba8-853f-7b4aff4f15ef | -2.56243 | -47.06525 | 2024-10-20 00:24:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 00699d1c-541c-359e-a9ff-e849cf40b6a8 | -2.54534 | -47.12251 | 2024-10-20 00:24:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| cdbb54ea-3d40-397b-bdbe-5cf41cb2718c | -2.51833 | -47.48906 | 2024-10-20 00:24:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| ad8bc776-7b32-3209-8d86-987559e94857 | -2.51813 | -47.49547 | 2024-10-20 00:24:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 9d42f5de-741f-3674-85e7-c975c19a753b | -2.46053 | -47.83395 | 2024-10-20 00:24:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 233a610b-9076-3253-9ec7-ad5d0e4f7d37 | -2.43162 | -48.48949 | 2024-10-20 00:24:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 1a14eef3-5fde-3813-a5e6-c7245908ce70 | -2.41853 | -49.40287 | 2024-10-20 00:24:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 7f7497c5-598a-3e1c-857d-082501a4211e | -2.41833 | -49.39659 | 2024-10-20 00:24:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 2b66748c-6127-3af7-a1bb-02b90d74c288 | -5.92744 | -42.9656 | 2024-10-20 00:24:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| cd3c8513-706f-32ac-a787-60088180bfa6 | -2.36893 | -48.2951 | 2024-10-20 00:24:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 4ec2aff9-bd82-3885-b35f-e7f7988068c2 | -2.36312 | -48.29034 | 2024-10-20 00:24:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| c6b815c5-58df-3770-9cb8-9e7a9b6fef8a | -2.35094 | -46.05188 | 2024-10-20 00:24:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| cf6cf4b8-61b1-3509-acb2-f8a5aa660ecd | -2.34311 | -46.4984 | 2024-10-20 00:24:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ce8dc4b5-4a2c-3ca5-a17d-d9966e907557 | -2.31066 | -48.58321 | 2024-10-20 00:24:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 15763d56-15b9-3b25-a936-48c80b9149c9 | -2.30826 | -48.61411 | 2024-10-20 00:24:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| a8523c14-a3a7-3089-a608-2075c11a678b | -2.30494 | -48.5904 | 2024-10-20 00:24:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 245.3 |
| b1d79932-aba6-3c7d-80bb-952822d88300 | -2.30165 | -48.56687 | 2024-10-20 00:24:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| f7a1c228-eddf-323c-b5db-516057d39ae9 | -2.29993 | -48.60889 | 2024-10-20 00:24:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| c7017328-addb-34f2-9ebf-a59c2c831410 | -2.29681 | -48.58514 | 2024-10-20 00:24:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 308.6 |
| b00ee76c-9e36-39aa-9852-aaa6059853bf | -2.29109 | -48.59237 | 2024-10-20 00:24:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| c9463d52-b1ac-3005-97f6-cc9abdb6cabc | -2.27957 | -47.85021 | 2024-10-20 00:24:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 622e9a91-8a9d-3cec-819f-22f68810908c | -2.22716 | -50.45857 | 2024-10-20 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 474b03a7-bf22-33c5-8fed-1e23dd922704 | -2.21884 | -50.46651 | 2024-10-20 00:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 61ada8ed-c06b-379f-97b0-6cca97101354 | -2.21113 | -50.46084 | 2024-10-20 00:24:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| fa70f217-8bb5-3e58-b374-1c0dae23f3d0 | -2.20279 | -50.46867 | 2024-10-20 00:24:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 22bc407e-84a3-3168-8c90-b979aec0d85b | -2.19517 | -46.49831 | 2024-10-20 00:24:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| a6ad5d23-1a06-3be8-a412-2351a885f55b | -1.96582 | -45.59648 | 2024-10-20 00:24:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 1899ebec-c7c1-3b47-ab80-491714cb46b3 | -1.95502 | -45.59791 | 2024-10-20 00:24:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 9b247728-b320-3d5b-9065-af38ff5ef4e9 | -1.95315 | -45.58445 | 2024-10-20 00:24:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 2163e39c-f684-34c3-b215-1c6f13993eba | -1.35945 | -47.53385 | 2024-10-20 00:24:00 | TERRA_M-M | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 481a3883-0771-3c6e-9230-7e8f23ee8c2d | -5.92602 | -42.95515 | 2024-10-20 00:24:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| e03236ce-3a18-38ca-ac91-e3a328613c08 | -1.35778 | -47.53967 | 2024-10-20 00:24:00 | TERRA_M-M | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 97432564-4a98-379a-a156-44e98af72777 | -1.3551 | -47.52106 | 2024-10-20 00:24:00 | TERRA_M-M | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 8c917d9b-1a41-388b-9f33-7c206b445533 | -1.35691 | -47.51523 | 2024-10-20 00:24:00 | TERRA_M-M | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 36919a8e-740b-3a4a-8104-20a4056356aa | -9.81672 | -36.14528 | 2024-10-20 00:24:00 | TERRA_M-M | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| b640e4bc-4105-3f76-ac61-f79490246c83 | -7.87842 | -41.81443 | 2024-10-20 00:24:00 | TERRA_M-M | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| fe5bb398-d1ca-3481-a3aa-16f78e9166d3 | -7.04328 | -34.8839 | 2024-10-20 00:24:00 | TERRA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| 7bee7408-4d55-3ee8-8091-d839abb46395 | -7.03158 | -34.88603 | 2024-10-20 00:24:00 | TERRA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| e47af47a-7ff9-3ff0-a405-ce24bd953dd0 | -6.54258 | -43.04118 | 2024-10-20 00:24:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 65e5d130-4375-326a-b942-d9bfd1a5e928 | -6.04796 | -43.10261 | 2024-10-20 00:24:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8eafdda5-31c0-3e38-9709-7a4896af8c55 | -5.91791 | -42.96686 | 2024-10-20 00:24:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| fd7b3a1e-3046-311b-ba3d-effe39a16e6b | -5.9165 | -42.95647 | 2024-10-20 00:24:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 43.9 |
| ed51387b-c405-36e8-b022-dc5484a1fc0c | -5.85903 | -43.74109 | 2024-10-20 00:24:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7c14e754-1371-3f7e-b732-ba1c0121e47b | -5.72109 | -43.77722 | 2024-10-20 00:24:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 2ecdbddd-077f-32c6-a67e-7be478d85275 | -5.58938 | -42.93565 | 2024-10-20 00:24:00 | TERRA_M-M | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| f80d8be9-0652-39a2-81fa-2b529fa927d4 | -5.54441 | -43.90796 | 2024-10-20 00:24:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 3a88605e-c682-3384-9b45-b73854159110 | -5.54287 | -43.89633 | 2024-10-20 00:24:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d52e509b-1c80-36b9-83c0-fb3118371158 | -5.48964 | -43.34602 | 2024-10-20 00:24:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e59389d2-5b02-3f64-9e91-47780489bc2a | -5.48819 | -43.33528 | 2024-10-20 00:24:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3c876619-18ae-3eda-88ca-af388d94db12 | -5.47994 | -43.34737 | 2024-10-20 00:24:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5b652a22-fe5b-32ef-a9a9-7dcf7b0e8354 | -5.4785 | -43.33661 | 2024-10-20 00:24:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b8d91bf8-a1fe-36cd-bdf0-d5b59385a934 | -5.36643 | -43.57492 | 2024-10-20 00:24:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 233e4a85-9a6d-3d4e-bfef-a260c47d4856 | -5.36491 | -43.56376 | 2024-10-20 00:24:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fabe804b-6983-38e7-8c69-2683540bd224 | -5.35661 | -43.57625 | 2024-10-20 00:24:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6055dc0c-5431-393e-a294-d819a0dacc36 | -5.26899 | -43.98784 | 2024-10-20 00:24:00 | TERRA_M-M | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3c983c53-deb3-326b-8ec5-cc62b18a4a67 | -4.86171 | -43.24903 | 2024-10-20 00:24:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 09fc3cae-9eaa-3eed-ad84-8588e86fc5d3 | -4.82746 | -42.7425 | 2024-10-20 00:24:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a217ce13-0112-375d-9bf4-7c149031d9cc | -4.82614 | -42.73268 | 2024-10-20 00:24:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 47.5 |
| ecf21d21-52aa-30e9-ab56-6ed0f9772444 | -4.62916 | -43.35242 | 2024-10-20 00:24:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7214e742-4f6a-32eb-86f5-949dfcc9ba58 | -4.5848 | -43.98898 | 2024-10-20 00:24:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 72b8908d-4555-3856-a21c-26e94cc812d4 | -4.45712 | -42.91502 | 2024-10-20 00:24:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| d4f665a4-79e7-3deb-9cfa-226fefda2e5b | -4.45576 | -42.90519 | 2024-10-20 00:24:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 2310b308-59cd-3ee4-9d80-c74d585278d9 | -4.4544 | -42.89532 | 2024-10-20 00:24:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 92e1fcd2-77dd-3dff-9b1b-50e77309929f | -4.40921 | -43.0541 | 2024-10-20 00:24:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| afbeeb38-c5c7-39f0-96f5-9dcdcf80eca5 | -4.40787 | -43.0441 | 2024-10-20 00:24:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| dff65388-d290-3669-878d-d5568cab0cdf | -4.16036 | -43.36264 | 2024-10-20 00:24:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |


[Clique aqui para ver as próximas entradas](README7.md)
