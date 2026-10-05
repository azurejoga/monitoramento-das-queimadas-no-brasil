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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1981c6d2-1396-3c17-a708-ce4fd27d5ba9 | -7.45412 | -63.55683 | 2026-10-05 01:17:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 18a91e98-7452-3bfc-b91c-beb20d43b25f | -7.4482 | -64.42523 | 2026-10-05 01:17:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 01cef1c9-e6bd-384d-8e94-2745214cdbc0 | -7.45644 | -63.57219 | 2026-10-05 01:17:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 21dddea5-bf36-3928-acff-4669a4868174 | -7.44504 | -63.57395 | 2026-10-05 01:17:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 18f3e2ae-fa9b-319f-87d4-05b69787e28e | -8.2719 | -71.12542 | 2026-10-05 01:17:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 82d10964-6abf-3a19-a413-f59af2980125 | 0.44526 | -60.53345 | 2026-10-05 01:17:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 49.5 |
| c62274ef-d8cd-38c3-931b-b9cfc70ba7f0 | -7.44271 | -63.55859 | 2026-10-05 01:17:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 0119ceae-93fe-3735-ae2d-a720655626c8 | -7.43131 | -63.56035 | 2026-10-05 01:17:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 22.8 |
| eb365414-634c-3cf5-afad-b5771d1ff963 | -7.4443 | -64.43161 | 2026-10-05 01:17:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5a32fad0-2435-33a2-9317-97848f18f7bb | -7.43365 | -63.5757 | 2026-10-05 01:17:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| c6ac8849-9609-3bc8-9aa3-e5d0ea73a611 | 0.45042 | -60.53926 | 2026-10-05 01:17:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 803df90b-612b-3a82-9860-bdb1be5c2e66 | -7.35491 | -72.60989 | 2026-10-05 01:17:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 1b1d53b9-045c-332f-ad6c-5bad0b7d241d | -7.4626 | -63.5583 | 2026-10-05 01:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 5c363f5b-0554-3d12-b591-e1676bf93f2b | -6.914 | -43.6816 | 2026-10-05 01:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 58f2a80e-c0be-3198-b90b-ccbc8f62cd35 | -3.8756 | -55.8184 | 2026-10-05 01:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| a0c921fe-f2c9-3b06-a5eb-73cd62e97337 | -3.0548 | -54.2277 | 2026-10-05 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 4a4a077d-1a98-31dd-8f3a-d603db21cf51 | -7.4441 | -63.5777 | 2026-10-05 01:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 3b83ab32-e80e-3401-b81f-f23303f07f4b | -6.0075 | -53.5122 | 2026-10-05 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| d28d30f2-a4d6-3de1-a5d0-e6329a579779 | -6.2159 | -52.8285 | 2026-10-05 01:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| d638356d-722b-3f39-8dda-1df758e1323f | -6.9328 | -43.6799 | 2026-10-05 01:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 0312459c-77dc-3ab2-89b8-4822b71466dc | 3.1097 | -60.6133 | 2026-10-05 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.5 |
| ed82001d-5794-38a1-befb-fa08c4ff20b4 | -3.8448 | -50.3063 | 2026-10-05 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 6b87c79a-6753-3363-a893-45e784f72115 | -2.6859 | -49.0325 | 2026-10-05 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| ed9e1c87-f2d4-34b8-928b-3762d1c2484d | -9.1613 | -68.2568 | 2026-10-05 01:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 97eabed5-0ca5-317b-8165-e377b730fb52 | 1.8583 | -55.8018 | 2026-10-05 01:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 030fe4b4-3db1-38f9-956b-2e9c9dc776ff | -2.9082 | -54.0907 | 2026-10-05 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| e476dce5-1bba-3cb7-890c-0a90537fcc83 | -7.4442 | -63.5589 | 2026-10-05 01:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 96c57795-08f7-3c40-905c-2686a08ef37d | -6.2529 | -52.847 | 2026-10-05 01:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 9efd0aeb-2876-3063-97bb-13be410626f2 | 3.1098 | -60.5943 | 2026-10-05 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 24fe3a27-a366-3df4-b6d0-b56ed16e7570 | -3.5128 | -54.6162 | 2026-10-05 01:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 45bcda95-0029-3fef-8430-b5eb63386789 | 1.8583 | -55.7821 | 2026-10-05 01:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 667caa55-306e-3e43-96d0-caebaf9d7756 | 1.8766 | -55.8016 | 2026-10-05 01:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 0ffed865-e0f0-3cf1-859b-280a6bc1c9ce | -3.8447 | -50.3273 | 2026-10-05 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 12ab3783-496b-3461-ab03-7dda7ade630e | -6.8952 | -43.6833 | 2026-10-05 01:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 3d60f5b1-ceb2-3090-b4ca-0cf534b1c844 | 1.8766 | -55.7819 | 2026-10-05 01:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| e871f540-7574-320e-9677-09ad2d089110 | -5.9882 | -53.635 | 2026-10-05 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 8e9bd8d8-1567-3420-9e2a-bf06fac6b286 | -6.1974 | -52.8295 | 2026-10-05 01:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| bb86314b-d6db-30c9-903b-9a099ccd4e6b | 3.10719 | -60.61774 | 2026-10-05 01:20:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 150.2 |
| b8c8b8c6-e80c-3214-a6cb-3e453f4eda1b | 3.10508 | -60.61027 | 2026-10-05 01:20:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 134.7 |
| b147943c-d13a-3313-93fe-4975b350f6e4 | -7.4626 | -63.5583 | 2026-10-05 01:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| e87d4eef-326c-3b05-abe1-98612a7a30b6 | -3.7665 | -55.5445 | 2026-10-05 01:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| d3279851-ada1-32d0-9673-454c60f1fd38 | 1.8766 | -55.8016 | 2026-10-05 01:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 0781d92b-8111-3aeb-b859-5aa14070724d | -5.9882 | -53.635 | 2026-10-05 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| adc240e4-0de1-3fc6-97dc-2252b06dab77 | 1.8583 | -55.7821 | 2026-10-05 01:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| e414898c-639d-376a-984f-f1ec2eebbdd5 | -10.8951 | -57.0942 | 2026-10-05 01:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 075c2144-d2f8-38db-85d6-ffd0355829b3 | -3.9218 | -49.6918 | 2026-10-05 01:30:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 0bc103f3-3166-30c1-9d5a-013c245ffe74 | -3.8448 | -50.3063 | 2026-10-05 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 51294d88-ac0d-3629-a818-332749df023e | 3.1098 | -60.5943 | 2026-10-05 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 5d65a597-19f3-3be5-ab4a-c145f59c57f1 | -6.0067 | -53.634 | 2026-10-05 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 880cb4ca-eb4e-3c42-899d-c37ef8b190d4 | -6.8952 | -43.6833 | 2026-10-05 01:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 36d90a16-0724-3369-a655-83ee4dac53e0 | -6.914 | -43.6816 | 2026-10-05 01:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 90.1 |
| a03a170d-0104-3cb2-b805-d4f56fe4d103 | -2.6859 | -49.0325 | 2026-10-05 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 6419f863-d9eb-33a5-b6f4-38d7e5ea0fc2 | 1.8766 | -55.7819 | 2026-10-05 01:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 59f6acd2-cf5f-3675-9749-3905f26d0de4 | -2.9082 | -54.0907 | 2026-10-05 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 9b0903bd-cf8a-3d93-8ce3-c9dc113a01b2 | -3.9859 | -55.8152 | 2026-10-05 01:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 50306610-679d-372b-be1f-3eef63a65620 | -3.5128 | -54.6162 | 2026-10-05 01:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 9b7a88de-3e68-32ab-b668-95e3937a02e3 | -6.2529 | -52.847 | 2026-10-05 01:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 427de107-19dc-371e-8b40-4407025733c9 | -3.9217 | -49.713 | 2026-10-05 01:30:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| dcce3042-ead7-31ae-9ca9-c9ab08930394 | -3.3335 | -53.3941 | 2026-10-05 01:30:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 41428ea4-8598-30d6-91da-166c2cdf7b54 | -6.1974 | -52.8295 | 2026-10-05 01:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| d1d7e66b-8396-30cc-b800-e015864043ec | 3.0916 | -60.5757 | 2026-10-05 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 0e6e2a43-e8f7-3f06-8b9d-1779bf4761f9 | -6.2159 | -52.8285 | 2026-10-05 01:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 8668184f-43a2-3638-8087-d0030bf2527d | 1.8583 | -55.8018 | 2026-10-05 01:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| b3b86539-2bee-3c7a-94bc-852f8fa237c7 | 3.1097 | -60.6323 | 2026-10-05 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 3d91632d-2f90-3757-84de-ef180a91b9f6 | -3.8447 | -50.3273 | 2026-10-05 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| aecbd718-37c1-3e2e-98fa-e9f57f4ccb3a | -7.4442 | -63.5589 | 2026-10-05 01:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 117.9 |
| fa6753da-483d-38ce-a993-7fb2aa73c4a8 | -6.0075 | -53.5122 | 2026-10-05 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| e6d0163c-f308-3468-bedf-5519a0148cd6 | -3.9032 | -49.7137 | 2026-10-05 01:30:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 15507b81-ede4-3a6f-a3e8-d06215a6ef48 | 3.1097 | -60.6133 | 2026-10-05 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 117.5 |
| fa1cc6c6-56a2-3495-a165-ef0881f4a5aa | 3.1097 | -60.6133 | 2026-10-05 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 7ca1896d-8dae-3251-a2bd-c3b5c12982ec | 1.8766 | -55.8016 | 2026-10-05 01:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 5d31bc5a-5837-306e-ad72-32ed9f4dea26 | -6.0075 | -53.5122 | 2026-10-05 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 1c285275-297e-3206-b4bc-d442e0638506 | -3.8448 | -50.3063 | 2026-10-05 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| f7b09541-58d1-3154-8c0b-780ef8ffc7cb | -5.9882 | -53.635 | 2026-10-05 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 55e0a6f2-7cd3-329c-a682-54f595ff8760 | -3.3335 | -53.3941 | 2026-10-05 01:40:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 3d822b41-6b9c-314e-a9bb-e9994f2c9155 | -6.0067 | -53.634 | 2026-10-05 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| ad1337ae-bab3-36c6-8765-cb33251939a3 | -10.8951 | -57.0942 | 2026-10-05 01:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| d83698a5-5b37-3ded-9def-aacb5881c33b | -2.6859 | -49.0325 | 2026-10-05 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 045a2850-7a76-366a-b66b-76eced5c04da | -6.1781 | -52.9328 | 2026-10-05 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 064b3a64-da59-3776-8805-91de985d2477 | -3.7665 | -55.5445 | 2026-10-05 01:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 2bd44b62-021a-332b-983a-d6730b87714c | -3.9032 | -49.7137 | 2026-10-05 01:40:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 280ef233-5c44-3daa-8f4c-a9ec3292cd6a | -6.2159 | -52.8285 | 2026-10-05 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| a6e6cf3b-f67b-388f-81aa-91654d8a74a4 | -3.8447 | -50.3273 | 2026-10-05 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 452cb9b0-2949-3c0c-b8ab-a60cc9c8ebef | 1.8583 | -55.8018 | 2026-10-05 01:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 508ae1cb-37e7-3128-b2fd-8e84dfaf2460 | 1.7303 | -55.6456 | 2026-10-05 01:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 13c1ce87-d208-33ad-bf55-a39ecb8953ba | -3.9217 | -49.713 | 2026-10-05 01:40:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 5fb2ca1e-5a91-39d0-9a78-ba1eea6527fe | -2.9082 | -54.0907 | 2026-10-05 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| e5b1a24c-4257-3497-a7c3-161399659a02 | -7.4442 | -63.5589 | 2026-10-05 01:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 116.6 |
| eb2dc24b-7a1d-3b67-b147-e353544d5597 | -6.914 | -43.6816 | 2026-10-05 01:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 910e52d2-1aed-3e94-8398-5ac0b3a5cd7d | 3.1097 | -60.6323 | 2026-10-05 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 1300ca5b-4002-3054-a8db-8b7856f0aa45 | -3.7481 | -55.545 | 2026-10-05 01:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| a935c640-e0e5-37db-8572-fc9057260249 | -3.0548 | -54.2277 | 2026-10-05 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 6047f5a7-5f7e-3da7-8531-f5a0f6b9a523 | -3.5128 | -54.6162 | 2026-10-05 01:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 9c229f93-8f4d-3cac-be52-cfd969be1a08 | -6.8952 | -43.6833 | 2026-10-05 01:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 27717d40-c2ba-3075-a3f7-670615535b6f | -6.1974 | -52.8295 | 2026-10-05 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| dfd5fd53-e60f-374f-98e8-586eb0c0e787 | -3.5128 | -54.6162 | 2026-10-05 01:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 8d0a34f6-bc90-3886-a0a0-fb609ba7e810 | -6.0075 | -53.5122 | 2026-10-05 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 00b74184-fa3f-3fc4-8454-116a683b4d9c | -2.9082 | -54.0907 | 2026-10-05 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 5751195e-7950-3e3b-8fb9-326e8bb65218 | -3.9217 | -49.713 | 2026-10-05 01:50:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 01a057bf-ab9c-3817-a6c4-e78c29567e16 | -3.9032 | -49.7137 | 2026-10-05 01:50:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |


[Clique aqui para ver as próximas entradas](README8.md)
