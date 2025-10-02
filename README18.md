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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56d4d837-78b7-3fee-8c07-27b9e84d6aaf | -3.17464 | -42.95736 | 2025-10-02 04:00:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9326fd55-2494-3399-a0c8-77d49e8e599b | -5.32951 | -43.76279 | 2025-10-02 04:00:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 03aa7ac7-a0ff-31de-923d-a5861ee2ff1f | -3.48471 | -50.09092 | 2025-10-02 04:00:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c2bb242-3ac3-3166-92e8-d2d9048d3954 | -5.34082 | -43.7646 | 2025-10-02 04:00:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 3f6262ad-dd3e-3e5c-94d9-50d42a0d02c2 | -3.22478 | -47.12827 | 2025-10-02 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9eaa490-a0b7-3d8e-ba2a-7ef3e3e7b4a4 | -5.33026 | -43.75819 | 2025-10-02 04:00:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9414a3a3-25b0-317e-ac1f-1fa2a5b9a4a5 | -5.4885 | -42.75756 | 2025-10-02 04:00:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 4e65cc2a-a9bf-316e-b29e-27e5e3205194 | -5.3378 | -43.75939 | 2025-10-02 04:00:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 87c2566b-7ec9-34e4-8472-17061817a91f | -5.69898 | -42.69005 | 2025-10-02 04:00:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| fe521f29-7a19-35c3-936a-3f3807156b6f | -5.24615 | -42.97894 | 2025-10-02 04:00:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 93579b80-c502-3de1-aac3-fba3d23cf3ae | -4.14221 | -44.40371 | 2025-10-02 04:00:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82b7f030-ba99-3cab-86ee-ce4ae7b756c0 | -4.25366 | -48.55935 | 2025-10-02 04:00:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8ddd880-a092-3b4e-bbc5-74e8f1ef54ec | -5.34475 | -42.65717 | 2025-10-02 04:00:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8c77b2ae-42be-3653-87c9-3e3f077b6023 | -5.70449 | -42.83653 | 2025-10-02 04:00:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 0ce714db-4357-3f08-90ca-d3c87d762ace | -3.34701 | -43.19184 | 2025-10-02 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| aba92a33-9faa-3167-97ca-f62c90b6bd9d | -2.92647 | -48.29924 | 2025-10-02 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b5064ef0-9c24-310a-8f8c-ad86d2dcbe0d | -3.09537 | -47.016 | 2025-10-02 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1fcc6df1-b757-3d9b-a7ae-43f8ced1c572 | -3.45954 | -50.0957 | 2025-10-02 04:00:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b284e3b9-94ae-3abc-b19a-b721232f5667 | -5.41248 | -41.32079 | 2025-10-02 04:00:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0b6ce3bf-850d-32c4-a741-a0ad99cf6bea | -3.76229 | -44.92162 | 2025-10-02 04:00:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45929144-9a8c-3bbc-a79b-a982ffcdf48b | -4.25893 | -48.56038 | 2025-10-02 04:00:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24972719-4576-3f78-b950-080218d3848b | -5.0555 | -40.95321 | 2025-10-02 04:00:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d8a18d64-7ed8-30d5-a11d-534a87949bf0 | -3.80284 | -51.31609 | 2025-10-02 04:00:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dfca7094-836b-394c-af3c-8dca329d980d | -4.62338 | -49.36987 | 2025-10-02 04:00:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5015f97f-31bc-3250-8171-5ccec3b08194 | -5.40741 | -41.33103 | 2025-10-02 04:00:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1b3f69fc-9a3a-33b6-8641-94a878742430 | -5.27433 | -42.87247 | 2025-10-02 04:00:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2c4618a6-f6ad-388c-b90f-4f448b84cbad | -3.68472 | -49.05244 | 2025-10-02 04:00:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ecbe29ff-e555-30b0-a504-b04516c017d8 | -2.92536 | -48.30586 | 2025-10-02 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 649f8f10-31cd-3ac9-ba4e-2ba73e757937 | -2.96201 | -48.59885 | 2025-10-02 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f2096f41-13e3-3ad3-8aad-10388eedb2a2 | -5.80784 | -42.84786 | 2025-10-02 04:00:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2ec4673c-b6a9-3b67-be51-774ee92785e6 | -3.81777 | -47.58492 | 2025-10-02 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 542c034f-86ac-350b-bc50-d7a3b5528f8b | -5.33555 | -43.77325 | 2025-10-02 04:00:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7a4be33c-2d3c-3f54-bd1d-83c6199efead | -5.79413 | -42.77454 | 2025-10-02 04:00:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c0b0f7e5-e929-3272-b7c0-6cdb0fe5aa3b | -5.48785 | -42.76164 | 2025-10-02 04:00:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 76fe3b51-6598-37d0-a520-91ec1c2822fb | -5.46097 | -42.83718 | 2025-10-02 04:00:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bcc4184b-9f86-3108-bba8-81ab7aee97d3 | -3.92547 | -41.57165 | 2025-10-02 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 580221be-8904-3394-8cd1-4326f8bec5c2 | -5.18327 | -41.24022 | 2025-10-02 04:00:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9271ea6f-5b19-3f48-80ca-1f753c59332c | -3.16741 | -42.97886 | 2025-10-02 04:00:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83d85169-0a02-3f7a-b97f-d862d37c4652 | -4.97284 | -37.95548 | 2025-10-02 04:00:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d03a665a-5095-3fd3-9c11-1dd16068906a | -3.87961 | -42.51588 | 2025-10-02 04:00:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7e1fc13d-b02d-36ab-9c2f-17da1570b987 | -4.44693 | -43.23529 | 2025-10-02 04:00:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d86f2556-b7c6-36bf-a772-772cf010840c | -5.73193 | -42.88636 | 2025-10-02 04:00:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 46cc7038-1744-3de9-98e5-56337971b260 | -5.55131 | -41.57787 | 2025-10-02 04:00:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 32c1b7d7-7deb-3273-9b4d-ccd5ca152636 | -5.39405 | -37.70585 | 2025-10-02 04:00:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 180e2126-859c-3106-9c16-aba87d1bdcdc | -2.9626 | -48.59536 | 2025-10-02 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 194dfb6c-23df-3bf1-8882-88f0942b89e0 | -3.81326 | -47.58125 | 2025-10-02 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4eedb8f0-c86e-305a-8a07-c19513bbe55f | -4.1098 | -47.93271 | 2025-10-02 04:00:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6044ae54-03da-35a4-b946-954a5a3f486b | -3.09789 | -47.00893 | 2025-10-02 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5659e61a-a400-3dba-b1b1-bccb3f0e6365 | -3.2768 | -43.53137 | 2025-10-02 04:00:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a757d67f-1632-3b83-9517-d85ca4d3552f | -5.26444 | -42.77386 | 2025-10-02 04:00:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5819200c-12dc-3ce3-a269-4629cf003f7d | -5.45964 | -42.84541 | 2025-10-02 04:00:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f6607cb1-884c-33f2-b03c-3d90d56ebac4 | -5.71716 | -42.82604 | 2025-10-02 04:00:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dcc422d9-8ef1-3d2d-9664-7aeff0732d27 | -4.05518 | -49.07711 | 2025-10-02 04:00:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67814c56-10eb-3568-ba3f-5ddf7fa54a79 | -5.1799 | -41.23969 | 2025-10-02 04:00:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6bfb536b-566e-389f-8ed5-81fa6087b659 | -4.26518 | -48.55164 | 2025-10-02 04:00:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52487e9d-046e-37ba-8949-7d6564cc4ba0 | -4.45064 | -43.23588 | 2025-10-02 04:00:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d5c27415-e6fd-3215-a196-4e5888d0c448 | -5.41133 | -41.32806 | 2025-10-02 04:00:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| fd849bae-32ae-393d-9c23-c25b0e9ca345 | -5.33253 | -43.76802 | 2025-10-02 04:00:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 92f7da84-82f3-3afb-a4d0-d54f513ab126 | -3.90015 | -49.08652 | 2025-10-02 04:00:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8db1b4e0-f7fe-325e-b15c-742bc4672238 | -4.25293 | -48.55963 | 2025-10-02 04:00:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1da8c9fa-5cb6-3681-86d5-a1ef5a2aaf93 | -5.41291 | -37.69724 | 2025-10-02 04:00:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3661a5de-9b29-3aed-8d2e-a6fbe7b657d0 | -3.62405 | -42.77431 | 2025-10-02 04:00:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a2638a98-ce92-38cd-b84a-ef27b5fa2d37 | -3.92143 | -41.57484 | 2025-10-02 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7c8b21b0-ac3a-31a7-8f3a-eeaf99401856 | -3.09703 | -47.01427 | 2025-10-02 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| b63d5d4f-abb8-33de-ba94-f411e08dd16f | -5.1827 | -41.24379 | 2025-10-02 04:00:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c0666a25-ffff-329d-8341-7cbc2a876f44 | -5.40906 | -41.34243 | 2025-10-02 04:00:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 3e6cb5cc-8cb5-3213-91de-99a06ce6806c | -2.27229 | -47.85192 | 2025-10-02 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3a53c4dc-035f-34f8-b3f8-491d92a0ae5e | -3.87603 | -42.51532 | 2025-10-02 04:00:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 76e61e6d-63f3-372b-9cf4-0635bed46efd | -3.46692 | -50.08823 | 2025-10-02 04:00:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b1ae02f4-2650-36a1-829d-697b73489c07 | -3.85054 | -38.56507 | 2025-10-02 04:00:00 | NOAA-21 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ed45e52f-fdc1-3d27-b5a2-023a53ba444f | -5.24548 | -42.98312 | 2025-10-02 04:00:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 51a81d27-1ddf-3206-80b5-e6cf33efebd9 | -3.93009 | -41.5647 | 2025-10-02 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9d845c0a-b355-3021-8e16-30805b95adeb | -4.00597 | -43.27216 | 2025-10-02 04:00:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78a0181f-84b0-3bad-bd7f-13c676d05fde | -3.69971 | -49.56659 | 2025-10-02 04:00:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b5b9a225-2f36-3810-aa3f-2713d456c45d | -5.46031 | -42.84129 | 2025-10-02 04:00:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 742d59fa-66d8-376c-a218-4d698cf645c0 | -5.7617 | -42.92886 | 2025-10-02 04:00:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 3d57b0f1-1f26-3691-b4f8-98ed9fa55a8b | -5.05215 | -40.95275 | 2025-10-02 04:00:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 75df635d-3aa5-33a5-9820-a7d67e500454 | -5.46389 | -42.84186 | 2025-10-02 04:00:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a0d31a34-cc72-3beb-be4e-769cfd363966 | -3.09051 | -47.0153 | 2025-10-02 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| aea6e633-6f60-3e91-bd6c-820e459e22d7 | -4.48209 | -47.67475 | 2025-10-02 04:00:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05400eb0-901e-33e2-87f9-3bad5adc52fb | -4.05416 | -49.08039 | 2025-10-02 04:00:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 193d068d-d8b0-366e-bee0-96ee9121de96 | -5.90063 | -38.48138 | 2025-10-02 04:00:00 | NOAA-21 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 726c62b1-d0b1-3c2b-b602-edbbc003e2b7 | -4.80745 | -38.58106 | 2025-10-02 04:00:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a115a1a9-9235-391d-9868-7c3dda2ff495 | -3.68533 | -49.04882 | 2025-10-02 04:00:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4eaa040-be87-320b-867c-568cae9ea1b1 | -4.83413 | -43.51012 | 2025-10-02 04:00:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2e4e56b5-25b6-3b21-8050-458a0aa52c41 | -5.33178 | -43.77265 | 2025-10-02 04:00:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 52bdd428-4864-3f3b-9554-1dab2d768e8d | -5.69543 | -42.68954 | 2025-10-02 04:00:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 07ec2e14-a9cb-344b-951d-1bfc1fec2225 | -3.46619 | -50.09242 | 2025-10-02 04:00:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cfde9c90-636e-38db-8f7e-b0ea687ef91f | -3.69904 | -49.57055 | 2025-10-02 04:00:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ace0cc38-7ec6-3d1e-a5d7-7ab2e89a5d20 | -5.75742 | -42.86515 | 2025-10-02 04:00:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 75210242-e306-39dc-9a65-a38479b852ad | -5.23651 | -45.20307 | 2025-10-02 04:00:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 86a5f8f3-c1f0-38ba-a152-bb3f9a3ab077 | -3.87178 | -42.51888 | 2025-10-02 04:00:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| e3486c0a-deb3-3062-8c82-1441d6cef1c1 | -3.52093 | -44.03801 | 2025-10-02 04:00:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a96917a-bb02-3ed6-877f-d0620c32474d | -3.09302 | -47.00828 | 2025-10-02 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 8ea3cf37-6b3f-3f6f-b1e2-cb19f8d75b37 | -4.26003 | -48.55367 | 2025-10-02 04:00:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 706f9e2b-81b1-3351-bfb9-e0439e310d08 | -5.71804 | -42.68459 | 2025-10-02 04:00:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fe393291-0030-334a-95a4-b7e3d32309ce | -3.0914 | -47.01004 | 2025-10-02 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 66b4028b-50d6-319e-998c-c0c65c8d617d | -4.57853 | -43.96663 | 2025-10-02 04:00:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d0037a04-4494-3869-9375-d3b6bf637ce9 | -5.64401 | -42.78109 | 2025-10-02 04:00:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| f03f1926-43a8-3fc6-a042-fa82ed39fae2 | -4.36681 | -43.0101 | 2025-10-02 04:00:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README19.md)
