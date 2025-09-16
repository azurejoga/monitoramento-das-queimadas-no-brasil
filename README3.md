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
| 963f589a-2947-3ed3-8919-281e0e603b90 | -8.121 | -48.2681 | 2025-09-16 01:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 42546539-31af-3eb7-bc89-931c19570dff | -3.212 | -47.1357 | 2025-09-16 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 28f7ed35-0926-3adb-9730-a16f049d7b40 | -16.019 | -59.2628 | 2025-09-16 01:10:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| ed244240-fcdd-334f-9483-706ce52009e9 | -15.9996 | -59.2647 | 2025-09-16 01:10:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 2faa85a9-57b1-3523-84fc-d89f21047780 | -12.7433 | -47.2009 | 2025-09-16 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| c069b4b1-d791-3be2-84af-64ccb5db8f0b | -8.12857 | -48.29114 | 2025-09-16 01:11:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| dd2be1fc-7bfb-32d2-a1e9-0b98aa6e00a7 | -10.00345 | -64.91273 | 2025-09-16 01:11:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 13.0 |
| fa505e3a-bc79-33b5-b687-d1f91e264f01 | -7.13447 | -48.00843 | 2025-09-16 01:11:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 976801de-b865-39e8-b96f-c1db793c59ee | -7.56012 | -50.4565 | 2025-09-16 01:11:00 | TERRA_M-M | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| e5c655c1-aa17-3af9-ad88-af5642b036fe | -10.36837 | -61.25248 | 2025-09-16 01:11:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| d33b509e-9da7-35a3-b853-bf5d485054e2 | -7.70757 | -49.56641 | 2025-09-16 01:11:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| a33e4b79-3cb5-3d1b-b96b-995e17b7e70a | -7.40766 | -49.99087 | 2025-09-16 01:11:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| b4ca4d42-2741-3731-afcf-ea110f72e13a | -9.30779 | -65.58348 | 2025-09-16 01:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 0b3ea16f-c9d3-3cab-b77e-a180899416db | -10.36993 | -61.26453 | 2025-09-16 01:11:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 66692546-bbe4-3420-a588-6d90b04e7407 | -4.57734 | -56.24834 | 2025-09-16 01:11:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e7c424eb-2019-3d28-93ea-52ac1868ab20 | -7.95328 | -63.67727 | 2025-09-16 01:11:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 8f26341b-03f6-3bbb-8b6f-2792bd2d485c | -8.12253 | -48.25385 | 2025-09-16 01:11:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 8bef2292-d1d3-3a00-ab13-c01886e6eba8 | -7.40843 | -49.99753 | 2025-09-16 01:11:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 5dd4c634-7f8b-3312-a5d1-d989f2dbbd2d | -7.47091 | -63.77008 | 2025-09-16 01:11:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 53248f54-235b-3028-9f94-d520ca99c4ab | -7.12924 | -47.96249 | 2025-09-16 01:11:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| ff3f4e3e-1b78-3860-a44b-2d8fc20bb2d4 | -8.11674 | -48.28821 | 2025-09-16 01:11:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 6c411e96-00e6-3d0a-92e7-0d94b32b56f1 | -7.48495 | -63.78533 | 2025-09-16 01:11:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 64e7e2d4-5210-35eb-b1a5-1f57fce238ae | -7.55709 | -50.46255 | 2025-09-16 01:11:00 | TERRA_M-M | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 0cda5178-93f0-375e-99f9-c1b43852dcef | -3.74488 | -49.03812 | 2025-09-16 01:11:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 5d264ae4-ab11-3d59-b3f3-93f182913819 | -7.47306 | -63.78683 | 2025-09-16 01:11:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 01bcdf5d-7481-3485-8f89-dbd05ecba63b | -7.13613 | -48.00301 | 2025-09-16 01:11:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| c7ff3cfd-1029-3f8c-a6c0-19406117b9dc | -8.70473 | -49.41456 | 2025-09-16 01:11:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 380256df-570f-3678-858c-6c142554e9ea | -9.7449 | -55.36642 | 2025-09-16 01:11:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 06f1c6fc-3d9a-3c00-9112-3016934d6178 | -9.74641 | -55.37681 | 2025-09-16 01:11:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 40e5e1b6-adad-3278-9ae3-63fd035c4014 | -8.65279 | -64.20989 | 2025-09-16 01:11:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 40b7b997-dbff-3aa4-8bd7-0edd26a74d80 | -7.70434 | -49.56033 | 2025-09-16 01:11:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 48ebe509-c846-33c3-9281-e628053a6455 | -10.35816 | -61.25382 | 2025-09-16 01:11:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d7084661-4ef7-37a4-82b4-45c8f08ef4e7 | -3.74191 | -49.04578 | 2025-09-16 01:11:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 09927970-a79c-3693-9ba0-51626c3e2482 | -9.4949 | -60.49611 | 2025-09-16 01:11:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2bf8b928-423c-3c39-9cfd-0b69d5ed132d | -7.12783 | -47.96778 | 2025-09-16 01:11:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 5e3c4400-afe3-34c9-b3d1-027cc75417c9 | -10.7201 | -44.7541 | 2025-09-16 01:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 8657dedd-3d49-3d75-a993-9a67f56660c1 | -14.9181 | -51.6657 | 2025-09-16 01:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| b4a14e4f-595a-30ec-9b6b-6e8891d72bf8 | -8.5947 | -46.3471 | 2025-09-16 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| b3ff03c6-43a1-3527-b4b7-3abc14f4a1f8 | -7.4315 | -46.1663 | 2025-09-16 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| bea37584-ff98-317e-be83-ba02520f5836 | -10.7392 | -44.7515 | 2025-09-16 01:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 9c2aad8b-a1e4-3d1e-b316-b9eebe6731d9 | -7.48 | -63.7829 | 2025-09-16 01:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 9b8b3325-5654-326e-b94b-5f35bd88e249 | -12.7682 | -47.9568 | 2025-09-16 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| f0e70611-b4f8-313c-b531-0b70be16793a | -7.4503 | -46.1647 | 2025-09-16 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 7066ed06-c07f-3377-aeaa-f0ec0e9798ef | -3.212 | -47.1357 | 2025-09-16 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| b56fc8c1-46c8-374e-951d-4277b0e65bec | -15.8371 | -53.4741 | 2025-09-16 01:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 5c4a0162-3b48-3ad6-901e-d88511dfa9c4 | -13.2027 | -47.3126 | 2025-09-16 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| e166b10c-342b-3034-96ee-36579b437600 | -11.1299 | -45.3426 | 2025-09-16 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 20cc6c9f-3c98-3f64-bd6d-62017d75a432 | -15.7793 | -53.4397 | 2025-09-16 01:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| c497df8f-3c5f-3706-8027-2a5766718951 | -13.2031 | -47.29 | 2025-09-16 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 5e2fd1ae-2edc-3362-887c-09854912c57d | -8.121 | -48.2681 | 2025-09-16 01:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 11b37a5c-7512-32a8-9bae-a0e3a66448de | -14.8991 | -51.6469 | 2025-09-16 01:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 590a0be5-c4c8-3e31-a606-f009f5ed2aee | -14.9185 | -51.6442 | 2025-09-16 01:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 5064842b-df87-39e0-9299-8ac5b7327ec5 | -12.6729 | -47.9258 | 2025-09-16 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| db4dbf70-fc93-3a32-a9c6-d41a8f5c1a4e | -10.7392 | -44.7515 | 2025-09-16 01:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| ca61cbde-3e5c-3269-8adb-c0d5ab06ef03 | -10.7201 | -44.7541 | 2025-09-16 01:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 515a5c69-8c27-3472-88d6-93b4ed6f6ff5 | -8.121 | -48.2681 | 2025-09-16 01:30:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 94edfd98-5323-3826-8d6c-cdf70aebdc1c | -14.9181 | -51.6657 | 2025-09-16 01:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 114.6 |
| e7e0de4b-9168-325d-932e-05d90ff5d685 | -13.2031 | -47.29 | 2025-09-16 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| bdf43ec2-7895-3eb1-9a78-33065c1d5a74 | -12.7682 | -47.9568 | 2025-09-16 01:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 194.7 |
| 8b5f67f6-66cb-3612-963f-9fe198d2aa6f | -3.8197 | -41.5739 | 2025-09-16 01:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 58.3 |
| a60ca9d7-d0cb-3c16-9d17-b26fd7486982 | -14.9185 | -51.6442 | 2025-09-16 01:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 0a5785de-dbd9-377b-8083-e7c2ac0355d9 | -9.7495 | -55.379 | 2025-09-16 01:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 4d2c1e23-aa91-3fdd-b50f-fde1a2beac4a | -3.212 | -47.1357 | 2025-09-16 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| fdec6d1d-17b3-3fe6-9fb1-9adc3ad989ef | -12.7875 | -47.9541 | 2025-09-16 01:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| f2467d9e-9084-38f5-ad8c-c3614a07b0d6 | -7.4503 | -46.1647 | 2025-09-16 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 0044eda6-de49-3386-8733-d74a2639a7ed | -7.48 | -63.7829 | 2025-09-16 01:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 2ac31dfe-1e6b-367b-b68d-3e87a49ebf54 | -3.2121 | -47.1138 | 2025-09-16 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 9e4c9a40-f7cb-31c2-8bb1-f82c2e273e50 | -7.1318 | -47.9801 | 2025-09-16 01:30:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 75b7602d-453f-38b2-8973-05dee2cc7f31 | -9.0674 | -44.8455 | 2025-09-16 01:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 76c787ca-68ef-3ae5-9ea1-7bcb96db7aef | -10.7115 | -46.488 | 2025-09-16 01:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| a32ecb15-909d-3ca7-88a3-2e88e34a316c | -14.861 | -51.6094 | 2025-09-16 01:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 1d4de951-59b9-3e44-992b-81aa03f0b167 | -12.7682 | -47.9568 | 2025-09-16 01:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 9e76f40d-696e-3156-b9d4-f68a9660cabf | -9.0485 | -44.8477 | 2025-09-16 01:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 1b402a21-7af2-3f95-a8ff-21015f5c41e7 | -14.8801 | -51.6282 | 2025-09-16 01:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 0c7c0309-823f-3e22-926d-1a3f1b30cc12 | -10.7306 | -46.4856 | 2025-09-16 01:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 358bce7c-4cc5-3da5-9b92-07e0e6cb4442 | -11.1299 | -45.3426 | 2025-09-16 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 9259e950-e52b-32e8-9c41-783ae6ae1ffc | -14.8412 | -51.6336 | 2025-09-16 01:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 8dbadf5d-b219-364e-bbe4-71549ba5000a | -9.7495 | -55.379 | 2025-09-16 01:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 2be54034-48b2-305b-9ae9-4a57a9384156 | -7.4503 | -46.1647 | 2025-09-16 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 4ce570a7-4000-3131-8316-8926e3705c5d | -9.0488 | -44.8247 | 2025-09-16 01:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 104.0 |
| e5ec166b-2cb9-39e6-b78b-f801b5509f95 | -14.8606 | -51.6309 | 2025-09-16 01:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 872aa9a6-9315-3fce-b190-28c1d656d338 | -8.121 | -48.2681 | 2025-09-16 01:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 33d10f4d-a431-38e7-9b1c-119440e6e299 | -3.212 | -47.1357 | 2025-09-16 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| e19bbaba-8be2-38d3-9d5f-c5f378ed1e33 | -13.2031 | -47.29 | 2025-09-16 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| f00d67ce-4eb3-3dc6-a743-ab2948fa270b | -14.8214 | -51.6577 | 2025-09-16 01:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 99976197-09c0-308a-a432-69438a70ae40 | -10.7201 | -44.7541 | 2025-09-16 01:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 288d1aea-0adf-3f57-988c-382dc0349f74 | -10.7833 | -50.6772 | 2025-09-16 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 491df36f-ad89-354a-904f-48e93c2fcc55 | -12.7875 | -47.9541 | 2025-09-16 01:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 766947a5-103b-3737-8b5e-695440a11ae0 | -11.1299 | -45.3426 | 2025-09-16 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 790c8cdc-474c-3cb9-89fb-404412819f7b | -13.2031 | -47.29 | 2025-09-16 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| efdc6b31-8c02-3a27-801b-e7feceeece3b | -14.8214 | -51.6577 | 2025-09-16 01:50:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 9269cf6e-bc68-3b6a-b821-a03b49d43445 | -12.7682 | -47.9568 | 2025-09-16 01:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 113.3 |
| a137a03a-a630-34f8-b63d-298f315eb648 | -9.0485 | -44.8477 | 2025-09-16 01:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 3cbce63c-a3cf-33f6-926e-ad3aababa95e | -3.212 | -47.1357 | 2025-09-16 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 945827cf-b9e2-3c9e-9843-459a5436efb6 | -10.802 | -50.6965 | 2025-09-16 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 919085eb-7355-3dfd-956a-9acd0b14260e | -9.7495 | -55.379 | 2025-09-16 01:50:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 8a8a5d0b-85d4-372c-b217-652e50f785d6 | -7.4503 | -46.1647 | 2025-09-16 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 160e9f87-0c6e-3be7-ae12-d998f4816858 | -10.7115 | -46.488 | 2025-09-16 01:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 9d3f0ca9-146f-3419-a531-af78ce6a1e18 | -9.0488 | -44.8247 | 2025-09-16 01:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 1879e68d-c4ca-3c9a-b74b-8fe06bc9e74d | -17.081 | -45.8162 | 2025-09-16 01:50:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 76.7 |


[Clique aqui para ver as próximas entradas](README4.md)
