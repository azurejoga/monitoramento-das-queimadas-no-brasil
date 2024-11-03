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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 872e3bfc-f55c-30e9-950b-66980ca41d4b | -5.36572 | -46.44484 | 2024-11-03 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 497352ac-9c61-3d25-beec-0da89947a97b | -5.22223 | -46.73009 | 2024-11-03 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1409310c-c07c-357b-a8f9-3d24c14c2106 | -5.22153 | -46.7347 | 2024-11-03 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45b95040-6212-3a42-9b03-3fdaaa822a85 | -7.89816 | -47.35626 | 2024-11-03 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d2159a8-0eab-3f32-8af1-acdecef495c2 | -7.76597 | -48.23891 | 2024-11-03 04:46:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 426ac456-1d7b-3027-a061-cc7f5b6652a1 | -7.75039 | -48.24495 | 2024-11-03 04:46:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 430722e3-800c-318f-bcdf-bdc004d73783 | -7.74979 | -48.2491 | 2024-11-03 04:46:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a22d8e1-9f30-3413-9917-f9b1668caf12 | -7.65282 | -47.60601 | 2024-11-03 04:46:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d970bd62-84da-3a09-8c0f-58b768e6250e | -9.33491 | -47.83112 | 2024-11-03 04:46:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 108ec8d6-5786-3d3f-ad9f-d88a24d76b14 | -9.33426 | -47.8357 | 2024-11-03 04:46:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ccea4539-d344-375f-83de-b5b523eb8b83 | -9.02302 | -47.84728 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3167309f-5134-367d-81e6-b8a3577bf418 | -8.83884 | -47.72771 | 2024-11-03 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 24da932e-0429-366d-9a1c-b8ed2bbe53c5 | -8.83819 | -47.73221 | 2024-11-03 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 800620ab-fbf1-310f-937a-cdbbb1f552f1 | -8.71987 | -48.00717 | 2024-11-03 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90098fbf-80c2-3084-86ac-149cc72b1f47 | -8.71923 | -48.01153 | 2024-11-03 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e8a8395-6f0f-3efe-b17f-cd556bb85aea | -8.71619 | -48.00665 | 2024-11-03 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 32fe484e-99ba-363b-9923-6a2f7349ed16 | -8.71555 | -48.01101 | 2024-11-03 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| a4fafe38-feb1-3a20-b275-d4442d2f7c3a | -8.71491 | -48.01535 | 2024-11-03 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 6c5e56cf-2f91-3dbc-8a93-a80373412ecb | -8.68323 | -47.97471 | 2024-11-03 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3254189d-1c46-3837-921a-229c9a984b24 | -8.65375 | -47.82359 | 2024-11-03 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a55f576-4128-3c3c-8e1c-0cc279197d02 | -8.65309 | -47.82806 | 2024-11-03 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 478dc9dc-b10f-39e8-be6c-92ea45f7201c | -8.65004 | -47.82301 | 2024-11-03 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 702f711f-9220-3d5e-aa55-2d93a6d72d1f | -3.42733 | -48.82316 | 2024-11-03 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fa6f16b7-5378-30af-a9a0-c6efebc84007 | -3.35073 | -49.06061 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d649cb89-9e67-3411-ba8d-24232d33c02e | -3.49331 | -48.23155 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23b7e946-305b-3410-ad03-27ebe7bf5438 | -3.06614 | -47.99765 | 2024-11-03 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f6a28cb0-1f55-3575-82f6-d4e6bcdef5c7 | -3.0539 | -48.0541 | 2024-11-03 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 755dfe6a-090c-3794-967a-358bc9da45f7 | -3.03314 | -48.07417 | 2024-11-03 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6e0da81-64c9-3f9a-acf7-55b777003b65 | -3.02231 | -47.93629 | 2024-11-03 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aebb1a69-53c8-30fe-9f53-98b5df2d99db | -2.93112 | -48.30404 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2bd51368-cfa8-3958-acda-ed93af8f1312 | -2.93054 | -48.30774 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24506029-d2c4-39ab-8c60-708822d795b6 | -2.92713 | -48.30722 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93fe5ba2-b5a0-3c03-bb12-82af4667f4d4 | -2.92371 | -48.30669 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ae9b5fc-0f99-331a-97ce-9cb711a75042 | -2.92029 | -48.30617 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7cff0d0-3db6-38b1-af08-9bd3b89e77ba | -2.91687 | -48.30564 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a5efe91-3b65-3973-922d-aecefdf823d0 | -2.91651 | -48.05695 | 2024-11-03 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 253e86a1-9b37-3590-a863-2f113ef5be40 | -2.91593 | -48.06071 | 2024-11-03 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe6d8e5a-8077-3660-a93c-c9797ac4b1a8 | -2.86177 | -48.45909 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4913d0c-9f27-39be-8a84-ed3c4319fe2a | -2.86065 | -48.46642 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da893f57-742f-3464-b28e-5efe11706269 | -2.86008 | -48.47008 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 998672a1-0a87-3a5f-b490-363db9747344 | -2.85894 | -48.45491 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ee5056c-946a-3622-b32e-a7a1e595ee23 | -2.85842 | -47.81875 | 2024-11-03 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d149c63b-0038-311e-8b5a-6352535ff78e | -2.85837 | -48.45857 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f3c55cb-ee69-3d64-ae55-d14aea8bf4d0 | -2.85783 | -47.82259 | 2024-11-03 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f83b16a8-8707-3e97-b670-1bd627821318 | -2.85642 | -48.24314 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9355030b-773f-3723-b0a8-f1b70a609f3f | -2.84818 | -48.45701 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b6baee9-f53d-314e-b3fb-4fed32c22f78 | -2.84761 | -48.46067 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8f7e0d1-bcf8-325d-8e60-f210996a07e7 | -2.84194 | -48.4523 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e710e479-b92b-34ec-a5e3-b8b595ae1bdd | -2.83966 | -48.44445 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 411b6765-eb56-395d-a7d3-0f9536712011 | -2.8391 | -48.44812 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ad5b37d-3bd8-3c66-ad7b-faa37dcd36be | -2.83854 | -48.45179 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e6acbcc-e5ad-3bac-8313-3d693971b7f2 | -2.83738 | -48.43662 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8744a08e-6014-3673-8ad5-a0674e7f8b8f | -2.83682 | -48.44028 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6c0dbc1-800d-3e83-8554-3f1187c19d91 | -2.83626 | -48.44394 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1929b9b-562a-3146-820e-b8c23dc53023 | -2.8357 | -48.4476 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b5af092-ccf5-3217-867a-333bac86759e | -2.83453 | -48.43244 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 849d4936-2893-369c-9487-ee6f3c5a04c3 | -2.83397 | -48.4361 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f32f1fb0-7bce-31a5-aaf6-5b644187d844 | -2.83342 | -48.43976 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b2823de-5550-3abd-bced-29fba3b3bb0b | -2.82915 | -48.34956 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a911a36-430f-3f92-b184-e728c54dfcf0 | -2.82858 | -48.35324 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dc1296c-545d-34a8-8e11-4c8060c73502 | -2.82801 | -48.3569 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b17a1de-302e-3cac-bda3-f09f8ca6396c | -2.82744 | -48.36056 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13864edf-307c-30a2-be79-2dd2362c1515 | -2.82717 | -48.43506 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b24800c-9afe-3f77-afc7-eb310366cb36 | -2.82661 | -48.43872 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dcfee85c-39d9-373b-8e41-31d51db20835 | -2.82382 | -48.45701 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67cf0aa6-2903-3817-a157-2ac91c2dbf46 | -2.82326 | -48.46067 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 740f61df-753e-3b38-b8b5-54e4e109b6c0 | -2.81986 | -48.46015 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9cff7eb-1a36-304b-866a-42d16327e672 | -2.81931 | -48.46381 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6242f157-547d-33d3-b7b9-ee9824b624d6 | -2.81646 | -48.45962 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d824760-10ba-3704-80d6-42b98461c257 | -2.81591 | -48.46328 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f026a472-7c72-3b15-9010-0a05cb43cde8 | -2.7945 | -48.27996 | 2024-11-03 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13924867-5d27-3103-af08-50092539b1d6 | -3.34738 | -49.0601 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6e182121-62e2-36a4-808a-2e6c2727dc7b | -3.20278 | -48.65618 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9008b8f8-f8cb-3ffe-8859-c2af7984e329 | -3.20222 | -48.65981 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da3ce76c-3e27-3e63-b986-93c400a9f7d8 | -3.1994 | -48.65566 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a03725d-5989-3d8a-bd3f-aa6bca195826 | -3.15693 | -48.57096 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f1ca121-43de-3f93-b30b-ea2df234489d | -3.15637 | -48.5746 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25f1163a-ff5f-3aec-a31f-822ffad6fcb6 | -3.1541 | -48.56678 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 064d7650-465d-360c-8244-14d312b77311 | -3.15354 | -48.57044 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c820a586-61bb-3a3c-98d6-20a5a8ac1c4c | -3.15298 | -48.57408 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83de3c38-fa0f-3b2d-82af-e17b23f1dc0f | -3.1507 | -48.56626 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 54df07a5-57a9-32ac-b340-a7721a2ba526 | -3.15014 | -48.56992 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 3320342f-cca0-3df4-a197-8a0305da6bd3 | -3.14958 | -48.57356 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| f4c61672-ebcb-389f-a04d-fdaf3a47e41a | -3.14903 | -48.5772 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e95c4f6-09d3-3997-b5b8-9532821df89b | -3.14731 | -48.56573 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| a749a1ff-7950-3042-afcc-ddb7288056c1 | -3.14675 | -48.56939 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| f586e50e-c639-37a5-9cda-8390dc702f50 | -3.14619 | -48.57304 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 5d175db5-0bb9-36f6-8d33-3a380782c184 | -3.14391 | -48.56522 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13186a21-99f9-36aa-903b-96dff9d23329 | -3.14335 | -48.56886 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3387249e-112d-3f17-9f7f-c2d24a18b318 | -3.11173 | -48.65372 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09b102c1-9b3f-34db-a85e-621c401b907f | -2.98173 | -48.63359 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92c42d1b-1ea3-3454-a5a9-4fd1fdb43502 | -2.97778 | -48.63669 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 455e911c-d118-3611-8d00-28e8b1da430a | -2.97722 | -48.64031 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5514e03-b059-3889-846f-2c08cce65253 | -2.97108 | -48.72438 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8f28ae8-83a8-3938-b0bd-c5fd70f38e78 | -2.96771 | -48.72387 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d01f8815-ca1b-3cd5-863b-b7644abea236 | -2.96657 | -48.70895 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f10eacfb-0de0-353c-8fe1-1b90ed6ad095 | -2.96489 | -48.71975 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a97fa63-c78b-336b-83eb-666c15115f0a | -2.96434 | -48.72335 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb4489d9-b15b-3e96-895e-94c6f8ec3faf | -2.9632 | -48.70842 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67faa0bf-b548-3779-93c5-51c84049e50a | -2.95748 | -48.6336 | 2024-11-03 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README38.md)
