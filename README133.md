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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c95f83a-6f4f-3715-b747-456590acb894 | -9.4168 | -51.4636 | 2024-09-27 11:46:00 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 1744ab2d-d893-3063-b357-59468b3bba1b | -9.417 | -51.4426 | 2024-09-27 11:46:00 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 165.4 |
| f43ec7f4-6bff-39cc-8f11-7761c74c2f89 | -10.0136 | -53.467 | 2024-09-27 11:46:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 161.4 |
| 48732c78-d1e2-3f6b-95e9-8d3db23bdb9d | -10.0139 | -53.4464 | 2024-09-27 11:46:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 444.8 |
| 3c58b087-c737-3b89-89df-41c40dc4ddb4 | -10.0134 | -53.4875 | 2024-09-27 11:46:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| a17aadd5-4c59-3195-a92b-03b3be0d6663 | -10.0322 | -53.4859 | 2024-09-27 11:46:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 337.6 |
| c6703cae-2518-33a7-8387-31c0fbe9cb82 | -10.0324 | -53.4654 | 2024-09-27 11:46:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 712.0 |
| 26c8e8a3-b73b-3d0d-b7ab-160e2f263ec4 | -10.6438 | -45.9544 | 2024-09-27 11:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 60d17552-8f49-3ff3-8c12-168b04b0731b | -10.6434 | -45.9772 | 2024-09-27 11:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 155.3 |
| ef973902-7905-3dc6-8b2e-6811a1c0c14b | -10.8143 | -46.0005 | 2024-09-27 11:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 245.0 |
| 15206d60-241a-3624-9f59-d71a3c043236 | -10.8334 | -45.998 | 2024-09-27 11:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 283.8 |
| a0ba39fa-599e-3a98-b237-586625d9381f | -10.8337 | -45.9753 | 2024-09-27 11:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.4 |
| c7a1ee70-b5a6-3005-8c48-a288ec6c647a | -10.8146 | -45.9778 | 2024-09-27 11:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.4 |
| e9f3df98-ddd3-3dbc-9b64-7744df44f1b9 | -11.2025 | -45.5616 | 2024-09-27 11:46:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 183.8 |
| 26148230-3cb5-3661-aac6-3bd9f81c61a1 | -11.0976 | -46.1446 | 2024-09-27 11:46:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| e2888868-2952-3acc-aa9a-64925de35f3a | -11.0972 | -46.1673 | 2024-09-27 11:46:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 189.2 |
| d0045f6b-9d7a-3e75-9110-d9408f0070c2 | -11.2695 | -46.1216 | 2024-09-27 11:46:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 86eef3a8-0ac6-329a-bbb2-effdc9056809 | -11.6605 | -44.5041 | 2024-09-27 11:46:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 7eec07c1-ae29-324b-af2e-a0ee0984c010 | -12.2367 | -45.5045 | 2024-09-27 11:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 6bf2bcb0-c5c2-30d2-81d3-f935a9fd2d41 | -12.2666 | -50.5317 | 2024-09-27 11:46:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| a300c715-de6f-3ca2-a692-58877e1267f6 | -14.7114 | -45.4863 | 2024-09-27 11:46:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 17959e9e-1736-393a-9613-bbc1c6f2853a | -14.7305 | -45.5061 | 2024-09-27 11:46:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 255.4 |
| a9d3ea10-c72a-35be-b3b9-90e3693c7972 | -14.9026 | -51.4534 | 2024-09-27 11:46:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 984f7454-7649-3fdb-b66d-04dac1b3726c | -9.417 | -51.4426 | 2024-09-27 11:56:01 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 142.0 |
| 1543cf1b-0e38-3080-9590-ebe7589b8422 | -9.4168 | -51.4636 | 2024-09-27 11:56:01 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 0003f9f6-f99d-36f9-89b2-5a234009d809 | -9.4356 | -51.4619 | 2024-09-27 11:56:01 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| baaa8b23-b26b-3824-bdf2-77287219ee8b | -10.0324 | -53.4654 | 2024-09-27 11:56:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 659.8 |
| 219a1c09-8302-3b90-9203-6ce387f12b62 | -10.0136 | -53.467 | 2024-09-27 11:56:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 263.0 |
| 564d173f-1424-3902-9b9b-5f6171611223 | -10.0139 | -53.4464 | 2024-09-27 11:56:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 513.0 |
| f31276a5-fe0f-327f-8585-59a25f9a0ffb | -10.0134 | -53.4875 | 2024-09-27 11:56:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 121.0 |
| dd4ea501-3aa3-345f-9dd7-af73571504cc | -10.0322 | -53.4859 | 2024-09-27 11:56:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 299.2 |
| 1776b523-a353-3316-bc67-4aa4858e2e19 | -10.0513 | -53.4638 | 2024-09-27 11:56:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 48ef9cdd-1715-36ca-9262-b24009914d2e | -10.6639 | -45.8838 | 2024-09-27 11:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| a1116a9a-63b2-3d35-b292-20775cbaa806 | -10.6452 | -45.8635 | 2024-09-27 11:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| a469c9f4-f991-3b20-a665-2653069956d9 | -10.624 | -46.0023 | 2024-09-27 11:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 242.5 |
| 138f818c-ec71-3004-afc9-29b396fc6c99 | -10.6643 | -45.861 | 2024-09-27 11:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 8fbddeb0-b707-3be0-a040-e45c43f41a84 | -10.6244 | -45.9796 | 2024-09-27 11:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 8d8227ba-45b4-3576-b07e-e0dbdf6e47f4 | -10.8334 | -45.998 | 2024-09-27 11:56:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 282.9 |
| 57d12eba-73fc-3a1b-8f44-9422c36d3a28 | -10.8337 | -45.9753 | 2024-09-27 11:56:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 160.4 |
| 094568ce-3936-3048-a362-914b0084250b | -10.8143 | -46.0005 | 2024-09-27 11:56:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 171.9 |
| ce0a2250-7b7c-3cf2-b8bb-f32bc745fdac | -10.8146 | -45.9778 | 2024-09-27 11:56:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 7d283a2d-d1be-37ac-b079-2412ef9fce35 | -11.2504 | -46.1242 | 2024-09-27 11:56:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 2af7b62c-cd21-35fb-923c-38969fc3fe5e | -11.2025 | -45.5616 | 2024-09-27 11:56:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 173.1 |
| 76899981-a374-3fde-b624-7a861aad5999 | -11.2029 | -45.5387 | 2024-09-27 11:56:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 9101e80d-6338-3ee5-8786-de8b1b216f6c | -11.2217 | -45.559 | 2024-09-27 11:56:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 695761c6-779f-36c6-ae10-03b57f1ddadf | -11.6605 | -44.5041 | 2024-09-27 11:56:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 5772b18a-18c5-3fc0-b037-079e2782d994 | -13.235 | -45.6245 | 2024-09-27 11:56:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 5dc4ffce-d21f-328d-8659-ab197b402aab | -13.2156 | -45.6276 | 2024-09-27 11:56:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 7c9d4925-26c6-3b91-b63d-47a49f760d35 | -13.2152 | -45.6507 | 2024-09-27 11:56:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 321de441-4ea7-32fa-91e4-ff56a3a409b8 | -14.7119 | -45.463 | 2024-09-27 11:56:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 2e4f05a7-a9f8-34d0-b1d3-95908dce5846 | -14.7114 | -45.4863 | 2024-09-27 11:56:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 056f0c9f-c949-3ca5-9630-a2ff4856f0f5 | -14.7305 | -45.5061 | 2024-09-27 11:56:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 179.1 |
| 58969a7a-ed70-303c-a87b-f35948dbbdac | -14.8832 | -51.4561 | 2024-09-27 11:56:31 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 1b095f6a-2ea9-3c31-b4bc-488ceb1d63d5 | -14.9026 | -51.4534 | 2024-09-27 11:56:31 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 76a6dcd0-c37b-3b2e-a832-4170df5ba874 | -18.0553 | -44.3645 | 2024-09-27 11:56:47 | GOES-16 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 424620ae-1bee-3d80-aebb-a01f9cbbbc0a | -10.83 | -46.0 | 2024-09-27 12:04:23 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8594a6bb-e5a1-35ef-8516-a7ec3d5671ff | -10.01 | -53.48 | 2024-09-27 12:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee85c2d9-1ee5-389e-999f-31305fddda6f | -10.01 | -53.41 | 2024-09-27 12:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f059fc2c-eca6-398a-bad1-e0f7781e2115 | -10.04 | -53.48 | 2024-09-27 12:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e54d994f-c5b8-356e-998a-c3da5ad2dfd1 | -10.04 | -53.42 | 2024-09-27 12:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8c364483-8b43-3e11-8424-397f67fd1033 | -9.4168 | -51.4636 | 2024-09-27 12:06:01 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 152.1 |
| 6d8f012b-9da8-3cc7-a95b-720de34532a1 | -9.417 | -51.4426 | 2024-09-27 12:06:01 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 263.3 |
| 045e948e-8eac-3d9f-8ffc-68b6179c9b55 | -10.0134 | -53.4875 | 2024-09-27 12:06:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| dea0fd24-8648-3937-b9d8-87e253af8a7e | -10.0513 | -53.4638 | 2024-09-27 12:06:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 03757de9-ffe5-31fe-8bad-9e2f1793da08 | -10.0136 | -53.467 | 2024-09-27 12:06:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 207.2 |
| 4fe73b6a-ea75-3baa-a6c0-0c824ddcca16 | -10.0139 | -53.4464 | 2024-09-27 12:06:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 600.3 |
| 1a381163-741c-3af8-b1cf-c0fcca4d8e42 | -10.0324 | -53.4654 | 2024-09-27 12:06:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 718.6 |
| d33f1d10-3977-37bf-b736-94886abf0f23 | -10.0322 | -53.4859 | 2024-09-27 12:06:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 231.6 |
| 219d250f-911b-31f6-a267-9a5d78f507a0 | -10.8143 | -46.0005 | 2024-09-27 12:06:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 243.8 |
| f0ea6d5a-e13b-3687-90fe-2af8302e1624 | -10.8146 | -45.9778 | 2024-09-27 12:06:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 184.1 |
| 402d2a10-ca56-3c6e-9445-0be0b7e128ad | -10.8337 | -45.9753 | 2024-09-27 12:06:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 296.4 |
| 4aa1c511-1047-33c6-923b-b1c2864caa4b | -10.8334 | -45.998 | 2024-09-27 12:06:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 383.4 |
| 21171f5a-2d05-35ba-8135-9e9cbfba2022 | -11.2029 | -45.5387 | 2024-09-27 12:06:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 2c2f81e4-3dce-3465-a856-d285110e49b7 | -11.0969 | -46.19 | 2024-09-27 12:06:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| c24fd449-3802-3c4a-9a35-622fc69988e5 | -11.0976 | -46.1446 | 2024-09-27 12:06:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| fd190fb1-d9e0-3cab-a614-3ad560161fd3 | -11.2217 | -45.559 | 2024-09-27 12:06:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| ccfe4a49-0c92-3941-8209-4ed88eceb225 | -11.0972 | -46.1673 | 2024-09-27 12:06:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 217.1 |
| 9ff19632-1860-3796-b922-fdebaa16b44c | -11.2025 | -45.5616 | 2024-09-27 12:06:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 234.2 |
| ce6417e1-b3e8-37f3-be5d-c898bdc0a07e | -11.333 | -46.9024 | 2024-09-27 12:06:11 | GOES-16 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 4ad1a23c-0f5f-3fd3-9d62-63db1979f0e0 | -11.6605 | -44.5041 | 2024-09-27 12:06:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 192.9 |
| df4c1c1e-18e6-3471-be57-3a11a6995f3d | -12.2371 | -45.4815 | 2024-09-27 12:06:16 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 339844dd-a78c-3c74-80b4-ee49c307dacb | -13.2156 | -45.6276 | 2024-09-27 12:06:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 39d24d15-e3dc-3f41-be3b-64ca013f55f5 | -13.235 | -45.6245 | 2024-09-27 12:06:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 162.1 |
| b0bbd580-035e-3d6e-b31d-508cd41b4618 | -13.2152 | -45.6507 | 2024-09-27 12:06:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 118.9 |
| a413bf59-cebc-3de9-97a7-5e1378c28fd8 | -14.8832 | -51.4561 | 2024-09-27 12:06:31 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.4 |
| ba8e229c-4dd5-31cf-a014-ce36a78348a8 | -14.9026 | -51.4534 | 2024-09-27 12:06:31 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 168.6 |
| aa3967b1-bc46-3d7c-a9e5-c7a2604de6c5 | -18.0553 | -44.3645 | 2024-09-27 12:06:47 | GOES-16 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 7c73f3e6-d024-34a5-b69e-97cab4e66289 | -9.4168 | -51.4636 | 2024-09-27 12:16:01 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| a2a16e0d-ffc7-31eb-a5b0-474ee7690d8f | -10.3167 | -46.2216 | 2024-09-27 12:16:05 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 8501a2a5-5792-33d7-ac85-69c8ef1e474d | -10.6643 | -45.861 | 2024-09-27 12:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 799da0b0-8537-3009-a967-d80cefa923ac | -10.6639 | -45.8838 | 2024-09-27 12:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 968ecbc1-0882-39b0-a502-0964d81f693c | -10.8146 | -45.9778 | 2024-09-27 12:16:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 3ae22447-155e-37f0-aba8-297929129c90 | -10.8337 | -45.9753 | 2024-09-27 12:16:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 247.4 |
| 46c652ad-1868-3370-8a52-dd044b84132e | -10.8143 | -46.0005 | 2024-09-27 12:16:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 200.6 |
| 1b85ee3c-1cac-3345-a254-07dc4555e26f | -10.8334 | -45.998 | 2024-09-27 12:16:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 373.6 |
| e03dcc45-7ae9-389d-974b-ab6e796d2c8b | -11.0976 | -46.1446 | 2024-09-27 12:16:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 178.7 |
| f1c55c7f-62d0-3c0e-9f52-1a5eabde398a | -11.116 | -46.1875 | 2024-09-27 12:16:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 760bade6-dc85-3607-9d8f-fecbec5271d7 | -11.2217 | -45.559 | 2024-09-27 12:16:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 176.7 |
| 83bdf8d3-f9f8-3746-800e-febdd0db20e7 | -11.2025 | -45.5616 | 2024-09-27 12:16:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 331.8 |
| 045b7131-3c48-3a3c-8148-fd5216ab8f06 | -11.2029 | -45.5387 | 2024-09-27 12:16:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.4 |


[Clique aqui para ver as próximas entradas](README134.md)
