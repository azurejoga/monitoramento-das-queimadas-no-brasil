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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4fefac6-c20e-3d72-a804-5d7c20e20e26 | -3.7942 | -48.8848 | 2024-10-21 00:38:46 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8da44635-2303-35fd-ab9f-e74c3d3904c0 | -3.7796 | -48.866001 | 2024-10-21 00:38:46 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0f8c951-1d34-3981-ba35-98be9ebc7871 | -3.7812 | -48.873001 | 2024-10-21 00:38:46 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe74fa42-1374-3606-afae-ed107b24e3e3 | -3.7828 | -48.879902 | 2024-10-21 00:38:46 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e446f3fa-5322-3564-9c69-273d33f4d9e7 | -4.25 | -51.045399 | 2024-10-21 00:38:46 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfbee396-a985-3cfc-bc98-20de26b21782 | -4.2516 | -51.052502 | 2024-10-21 00:38:46 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8c4fd11-9b8e-392b-8e27-df1283762592 | -4.2146 | -50.9795 | 2024-10-21 00:38:47 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f4ed206-dba9-36b6-8f7f-8af4be52fe2e | -4.2162 | -50.9865 | 2024-10-21 00:38:47 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce9d6556-2ffd-3c63-a7db-fbbf35b449d1 | -4.2177 | -50.9935 | 2024-10-21 00:38:47 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea50d3a3-b495-37e4-ba58-6bc1cbb54c4d | -2.8697 | -45.206299 | 2024-10-21 00:38:47 | METOP-B | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 933ce6e2-9c33-3fb9-a539-27cbe2b71b0e | -2.872 | -45.216599 | 2024-10-21 00:38:47 | METOP-B | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 094d70d8-d40b-3486-b1d4-7c82596ee580 | -2.8551 | -45.187901 | 2024-10-21 00:38:47 | METOP-B | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4678252a-0e23-37ed-aafe-a18b11ce3393 | -2.8575 | -45.1982 | 2024-10-21 00:38:47 | METOP-B | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f8b9f322-a4c7-3027-8a22-10990a5e2bb0 | -2.8599 | -45.208599 | 2024-10-21 00:38:47 | METOP-B | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4af1ed2e-ec8c-3c50-a178-690db1413b20 | -2.8622 | -45.218899 | 2024-10-21 00:38:47 | METOP-B | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8d923a7c-7ea3-36e1-b4f0-17d34bbf9ca8 | -2.8477 | -45.200401 | 2024-10-21 00:38:47 | METOP-B | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1795d760-22ce-3efe-babd-f291097c8a0d | -2.8501 | -45.2108 | 2024-10-21 00:38:47 | METOP-B | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b350f7e9-ea3d-3630-ad1b-ab95176e47e7 | -3.8745 | -49.741001 | 2024-10-21 00:38:48 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10dbdc65-d3cc-300d-af73-ce83bc49b337 | -3.8795 | -49.8545 | 2024-10-21 00:38:48 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1038f8e-0ffc-30da-acb1-d7b98632fc8b | -3.9025 | -49.956799 | 2024-10-21 00:38:48 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f85c4dd4-778d-3f12-b408-fbca9392b78c | -3.9041 | -49.9636 | 2024-10-21 00:38:48 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac7fc600-3a8d-3b51-8f8f-e3f0b8006f75 | -2.816 | -45.4646 | 2024-10-21 00:38:49 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 966a52e2-0aeb-3723-a203-3c8521c4812b | -2.8183 | -45.474602 | 2024-10-21 00:38:49 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 208e36d7-9425-3030-9a72-a203deef8a98 | -2.8206 | -45.484501 | 2024-10-21 00:38:49 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 66d545d8-3524-3830-a75a-83dbcfa643ce | -3.8467 | -49.983501 | 2024-10-21 00:38:49 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c2c65af-64a6-3303-a34f-8ea6bec16739 | -3.8483 | -49.990299 | 2024-10-21 00:38:49 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7de9cf7-83f9-3a89-80ef-729a392d9de2 | -4.0125 | -50.950699 | 2024-10-21 00:38:50 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 411f10d3-3bdf-3195-93e7-47ed7633da53 | -4.0141 | -50.9576 | 2024-10-21 00:38:50 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a90e6a9d-7dbd-33f9-ad43-3b6170200431 | -4.0168 | -51.0158 | 2024-10-21 00:38:50 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fbb5ea6-3d03-3d06-b76d-a956d23c6b0b | -4.007 | -51.018002 | 2024-10-21 00:38:50 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f7fe2c2-2483-3704-855f-3f64db82ba18 | -4.0086 | -51.025002 | 2024-10-21 00:38:50 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83da095b-eed1-3aa4-bf02-aa1c6fbf5af4 | -3.9827 | -51.001202 | 2024-10-21 00:38:50 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2341ea4-ae18-35c0-a4a4-86ff3cdbca86 | -3.9843 | -51.008202 | 2024-10-21 00:38:50 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f14469de-15c3-32fe-9085-690b0445e662 | -3.9859 | -51.015301 | 2024-10-21 00:38:50 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56f31343-d1f9-32c8-843e-c2d293089307 | -2.7663 | -45.784401 | 2024-10-21 00:38:51 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| af959bcc-07c6-39e8-b2d8-00b5d97c5a9e | -2.7685 | -45.793999 | 2024-10-21 00:38:51 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e2f52d9e-73ee-3bcb-a9a2-efc84f1234e0 | -2.7565 | -45.786701 | 2024-10-21 00:38:51 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| da9e407f-6d6b-37fe-a9dc-e458b1a6da68 | -2.7587 | -45.7962 | 2024-10-21 00:38:51 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4bd84326-7ff8-3b99-a131-ba763180ed35 | -3.738 | -50.186699 | 2024-10-21 00:38:51 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba86f390-75b4-3e4d-89c2-f71221e0d4a6 | -3.7808 | -50.652199 | 2024-10-21 00:38:52 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f09e1308-c8a5-359f-a46c-a24c564f98d0 | -3.8391 | -51.187801 | 2024-10-21 00:38:53 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85f3af61-0b68-3a25-8b1e-f4d1208f1629 | -3.8406 | -51.194901 | 2024-10-21 00:38:53 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccbf1367-410b-304b-a190-d5257425f4c5 | -3.6919 | -50.715302 | 2024-10-21 00:38:54 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32d3118e-023d-39b8-b2b3-794326709410 | -3.7743 | -51.128201 | 2024-10-21 00:38:54 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a75d14b-b9fd-341e-9c28-ebbe07c6eece | -3.7759 | -51.135201 | 2024-10-21 00:38:54 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e1faa38-a33e-3359-be3d-e23500647425 | -3.8008 | -51.292599 | 2024-10-21 00:38:54 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 425f153a-f1b2-3144-9d9c-3de3dc971f95 | -3.1751 | -48.609299 | 2024-10-21 00:38:55 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7038b827-7e30-3cbd-b8ca-29d35b83d346 | -3.1767 | -48.616402 | 2024-10-21 00:38:55 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 959f87fb-ff37-3049-8bca-04fa51253003 | -2.4732 | -45.5844 | 2024-10-21 00:38:55 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 66dbd20c-297c-33fe-9b4e-b683a8f7c8f5 | -3.5162 | -50.3004 | 2024-10-21 00:38:55 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ee707b1-3587-341f-8363-212ef2ddc9c2 | -3.5178 | -50.307201 | 2024-10-21 00:38:55 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15d5d946-43e9-3644-9a98-8a8af9df1e3a | -3.5064 | -50.302601 | 2024-10-21 00:38:56 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ab4e376-7546-3a26-9356-04e0ab8ca3a9 | -3.508 | -50.309399 | 2024-10-21 00:38:56 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9db05c3a-8877-3459-bf33-2027bf45cc83 | -3.5665 | -50.569599 | 2024-10-21 00:38:56 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 025a72cd-bb44-3ef1-870c-43d4ee42890d | -3.5681 | -50.5765 | 2024-10-21 00:38:56 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdfd5d18-bc75-3a0f-b97d-67d680dfd9ef | -3.5696 | -50.583401 | 2024-10-21 00:38:56 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f02f5174-797e-32ba-b7f5-7de4c4c5014c | -3.5933 | -50.780701 | 2024-10-21 00:38:56 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed9fc64e-6bb5-33e8-a23d-eb185dc59e59 | -3.5949 | -50.787601 | 2024-10-21 00:38:56 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c58d8c52-8976-3584-90c6-d46d24e9c7ec | -3.5835 | -50.782799 | 2024-10-21 00:38:56 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8db088dc-dfa7-31e7-ae87-b9ad7d3cd6ab | -3.5851 | -50.7897 | 2024-10-21 00:38:56 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e813675-2131-388a-b9a4-f895647c78a9 | -3.5866 | -50.7966 | 2024-10-21 00:38:56 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd75a411-4174-3483-a233-205df6ceadd0 | -3.3903 | -49.9702 | 2024-10-21 00:38:56 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fb3ebc9-a693-320a-b81f-3c0d62e266b6 | -3.3919 | -49.977001 | 2024-10-21 00:38:56 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 751c6acc-34ba-30c4-9f12-3548c09db3c0 | -4.2117 | -53.650299 | 2024-10-21 00:38:56 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ba24225-56ae-3925-a8b7-b3d7f5e8a9cc | -2.9299 | -47.9842 | 2024-10-21 00:38:56 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf825f10-6820-3a68-8e1e-ebce424b2d54 | -2.9316 | -47.991699 | 2024-10-21 00:38:56 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36f4d75b-f062-3beb-8d00-ac25a7fd51e8 | -2.9333 | -47.9991 | 2024-10-21 00:38:56 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5854fb3-368a-3e43-9d4d-be7d97395064 | -3.6846 | -51.325699 | 2024-10-21 00:38:56 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8a19df8-0b64-3b73-9dea-5ad1f6ca472b | -3.3577 | -49.734001 | 2024-10-21 00:38:56 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2981cfaf-8d65-3153-9c9f-aab9d41be85b | -2.9201 | -47.986401 | 2024-10-21 00:38:57 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 542dde42-87aa-3a49-a031-4562961c12e4 | -2.9218 | -47.9939 | 2024-10-21 00:38:57 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8ac35d4-89e3-371e-b547-0a52622c156e | -2.9235 | -48.001301 | 2024-10-21 00:38:57 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f79b5caf-4901-3efa-b1ac-ec7a01c695ce | -3.8024 | -51.8988 | 2024-10-21 00:38:57 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fba4615-1a2d-3dd3-9bde-1da8a62f4ceb | -3.8041 | -51.9062 | 2024-10-21 00:38:57 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adb68048-ed54-35e5-a65e-f2d7071b765c | -3.7599 | -51.800201 | 2024-10-21 00:38:57 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b14015c-3c38-34fb-89ba-8f49a819ae73 | -3.8265 | -52.191299 | 2024-10-21 00:38:57 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6127bf27-4638-3909-a696-15708c49ed41 | -3.869 | -52.382198 | 2024-10-21 00:38:57 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7fdfe6d-9c4e-3fbb-89c7-544e61b4348d | -3.3887 | -50.328602 | 2024-10-21 00:38:58 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33d23106-6c92-3449-b9fc-8953fe4aaef9 | -3.3168 | -50.101002 | 2024-10-21 00:38:58 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59df67cc-b1a9-3d3b-9c82-c1d5ff73126b | -3.351 | -50.3442 | 2024-10-21 00:38:58 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e08bf5e5-69b2-31fa-807d-34fa81983078 | -3.5526 | -51.287899 | 2024-10-21 00:38:58 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98e951e3-b944-3890-bbc1-a54c77dd6a86 | -3.762 | -52.3172 | 2024-10-21 00:38:59 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34dbe5d4-2580-3215-a420-8ba741b788d9 | -3.7522 | -52.319302 | 2024-10-21 00:38:59 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d96c9d5-793a-3f6d-bdd7-2a98a20dc71f | -3.7539 | -52.3269 | 2024-10-21 00:38:59 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 384005a5-9edd-32ea-b4a0-6dc2220ac877 | -3.4909 | -51.242298 | 2024-10-21 00:38:59 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e61ca5b4-2c3c-3f46-8092-e1366290af23 | -3.3516 | -50.667599 | 2024-10-21 00:38:59 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b67dae19-d31b-341f-ba55-1e93191c8a73 | -3.5096 | -51.3717 | 2024-10-21 00:38:59 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81c955e5-3b48-39fc-8950-ca265dc0d356 | -3.5112 | -51.378799 | 2024-10-21 00:38:59 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 951c56dd-5d08-34fa-b606-653f75fd9a26 | -3.5128 | -51.385899 | 2024-10-21 00:38:59 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a82925b-725c-3229-aabc-7610d1de4993 | -3.4738 | -51.3498 | 2024-10-21 00:39:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d422097d-a95f-3c5b-a8d1-5c024abd019c | -3.1697 | -50.362801 | 2024-10-21 00:39:01 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb03bd53-e310-3d83-a35d-de0d0c1a5481 | -3.326 | -51.058201 | 2024-10-21 00:39:01 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20948526-71ac-3361-a292-6c19fee9d2e6 | -3.4448 | -51.5881 | 2024-10-21 00:39:01 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27afd620-a51a-316b-9c35-7cc75f534d94 | -3.4464 | -51.595299 | 2024-10-21 00:39:01 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ff9bc0e-c1a8-3a16-8ac4-bcb221fca50d | -3.448 | -51.602501 | 2024-10-21 00:39:01 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43ae3839-7983-33cc-b831-b71d1add2f98 | -3.3668 | -51.240101 | 2024-10-21 00:39:01 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ab267e3-7362-3734-9c88-793e8c113723 | -2.7584 | -48.680099 | 2024-10-21 00:39:02 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b644aac-2716-320b-bf9c-862472a04b8a | -2.8975 | -49.339699 | 2024-10-21 00:39:02 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06d8c099-0293-3775-a07e-b280262b20f1 | -3.1206 | -50.373699 | 2024-10-21 00:39:02 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea7de31e-c469-38a7-a42c-fbe8f773f855 | -3.206 | -50.844501 | 2024-10-21 00:39:02 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
