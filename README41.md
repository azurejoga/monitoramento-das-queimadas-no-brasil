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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 389cfad2-4955-3424-8a98-58b45a1e4b2e | -2.62496 | -47.9901 | 2024-10-12 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3e97a800-188d-386d-9596-2cd5aac034c2 | -2.62428 | -48.48502 | 2024-10-12 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da566988-5067-35db-b755-009a6dbfc7c0 | -2.62219 | -47.98497 | 2024-10-12 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 884db732-815e-3432-b1e2-c2db54831c53 | -2.41576 | -48.45601 | 2024-10-12 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e6557e2-4ac5-3075-b34a-54694677f335 | -2.18555 | -48.25146 | 2024-10-12 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdb756a2-e6a8-38a0-a350-f33609beddb3 | -2.12733 | -48.37898 | 2024-10-12 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d59d051f-05cc-304c-a712-99dd2ab25bd2 | -3.45668 | -47.66231 | 2024-10-12 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a5492bb4-0e2a-3dca-89d3-199d5e85fec2 | -3.45591 | -47.66697 | 2024-10-12 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1cf64b76-ab8b-3815-931e-0f56d56ae5fd | -1.59658 | -53.35146 | 2024-10-12 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8c59465d-2af7-3e56-93b1-c8c6b0197124 | -1.58982 | -53.35014 | 2024-10-12 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e7f3b112-a23a-3d3e-8f8a-d7cd6deef7dd | -2.96119 | -54.12928 | 2024-10-12 04:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a5793bd-5987-3628-8d8a-7150f7fc2ecc | -2.96091 | -54.12415 | 2024-10-12 04:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 25988bee-75c0-34a8-ae9b-a1bbf285dff2 | -2.95976 | -54.13064 | 2024-10-12 04:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 66db2293-2d70-381a-ab95-333835f1527b | -2.95425 | -54.12789 | 2024-10-12 04:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 430fad5f-23ed-3fdb-9263-c2b100146164 | -2.78934 | -54.01612 | 2024-10-12 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0cf6e4c4-c00c-3ed6-b35f-904ea1de051d | -2.78841 | -54.01734 | 2024-10-12 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00cea3c5-f98c-3134-93c8-fe59c8daa97d | -2.78826 | -54.0226 | 2024-10-12 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 975883ed-83be-3c89-88fb-52ae53fd7727 | -2.78729 | -54.0238 | 2024-10-12 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33085ec2-d9d6-3768-9648-162d236599c5 | -1.89493 | -54.42944 | 2024-10-12 04:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f7a76d5d-d107-3527-abb7-270971948683 | -1.89376 | -54.43661 | 2024-10-12 04:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4f28eb49-3aa5-334e-b5d7-3b2dd283269e | -1.88998 | -54.42957 | 2024-10-12 04:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 314b755f-1f32-3229-8b16-03418d08ff51 | -1.88875 | -54.4368 | 2024-10-12 04:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 27156f5f-f3f9-3d90-9883-54285959a5b5 | -1.88774 | -54.42822 | 2024-10-12 04:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 54781707-74c1-356b-b0bd-e0263b9842fb | -1.88655 | -54.43547 | 2024-10-12 04:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4355fe79-1586-3f69-9793-1ee494a183e9 | -1.88277 | -54.42847 | 2024-10-12 04:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a73a6e32-851f-37a0-8c04-9cad1960d2a2 | -1.88155 | -54.43562 | 2024-10-12 04:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8464d14c-c42f-32ae-8ee2-b33df1222e19 | -1.88053 | -54.42711 | 2024-10-12 04:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 44718696-f052-3b73-aa48-361184aef2f8 | -1.88033 | -54.44278 | 2024-10-12 04:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| aac62a1a-7c37-39e9-9fa9-3a80074208ab | -1.87819 | -54.44138 | 2024-10-12 04:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| cd62e215-c85b-3692-a5dc-72c58d2c1b49 | -1.87436 | -54.4344 | 2024-10-12 04:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2f4a6e76-d159-364d-bcc2-a3f242cf3567 | -1.87314 | -54.44155 | 2024-10-12 04:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a6b055ad-278a-3e2c-8ef6-1a87a9e95fc6 | -1.87217 | -54.43298 | 2024-10-12 04:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd694bab-522c-3be9-926d-da6c1e9766ed | -1.87099 | -54.44015 | 2024-10-12 04:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dab8e31-5975-3413-8657-a25790c1d06f | -2.20132 | -48.84863 | 2024-10-12 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 26fb28b7-ba36-3f47-b10b-67c22c1707a4 | -2.19628 | -48.84779 | 2024-10-12 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b6a72ec9-c2da-3c0c-8fa2-ef6a7aad192a | -1.086 | -48.85648 | 2024-10-12 04:04:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 121761a5-2db1-3608-8e0d-d8fe0dc3f567 | -1.08137 | -48.85257 | 2024-10-12 04:04:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 905f9b90-08cd-34a9-a876-62b4f91d3bc6 | -3.45052 | -50.16475 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1079cad-3094-39e1-b822-7d83a12dacf9 | -3.44993 | -50.1684 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06306a8f-947d-3050-a2f6-14694b0be7c4 | -3.44706 | -50.16482 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79118ab1-716e-3a5b-8ea2-142581805f4d | -3.44645 | -50.16841 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0117ef14-f24f-3acf-8479-08779061d951 | -3.44511 | -50.16385 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9043e583-a381-3146-80f9-d91dce92c46f | -3.44453 | -50.16746 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d170bee-7531-318f-9489-ba8a06a22646 | -3.44104 | -50.16749 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ca99f97-efe0-3ede-bb00-511083420d98 | -3.43912 | -50.16656 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 225823da-e9e1-3995-9777-fd0d060396e1 | -3.34241 | -50.14647 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e4151ac-c72e-38a2-9b3d-9317a0a07795 | -3.34028 | -50.14814 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 94a15341-3005-3af8-be4a-0b6bcf4b5321 | -3.33699 | -50.14564 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60036475-4b9e-3351-ac4e-9108616c0315 | -3.33641 | -50.14898 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eca0e55d-3d87-36a7-9d08-77f087481d7f | -3.33488 | -50.14717 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c9e5c8d-1fce-3a98-9080-b054c8648fdd | -3.33434 | -50.15052 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55f1c383-de93-3ca8-90ab-6d0501c11e90 | -3.5225 | -49.72256 | 2024-10-12 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd0d57ab-ca06-31b1-ad88-4e46c2f2e488 | -3.52209 | -49.72476 | 2024-10-12 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b682dc19-e9f5-3593-963b-a6f903d4cc15 | -3.52195 | -49.72581 | 2024-10-12 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 667c018d-94fb-3aa5-9580-8892cf965e24 | -3.51726 | -49.72173 | 2024-10-12 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e27dee8-d2e9-3e91-b7ff-87636d15b98b | -3.51684 | -49.72392 | 2024-10-12 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c1e5d3f-3e44-35fc-912d-aec5f21c6d0f | -3.3351 | -49.13344 | 2024-10-12 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0b92acc-c5df-337d-9441-7275266ac2d4 | -3.33006 | -49.1325 | 2024-10-12 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 798afd58-f740-3ca6-b830-94c4a88cb593 | -3.32958 | -49.13539 | 2024-10-12 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a13a9f57-aa77-36eb-92c3-9b6d529ac562 | -2.83318 | -49.52769 | 2024-10-12 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8cd41bfa-2994-3e63-9e88-3823f4dfe73a | -2.83265 | -49.53085 | 2024-10-12 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f6691e4a-e1a1-3cd0-9619-41727fb25bf7 | -2.83158 | -49.53731 | 2024-10-12 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3972b809-a67f-31ac-b9d1-be2706a2bf8c | -2.82741 | -49.53006 | 2024-10-12 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 096a2ba0-ddda-3a15-b11f-7c418bc11b68 | -2.82687 | -49.53328 | 2024-10-12 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d257eded-4c7b-3211-950b-c6366b57cdb9 | -2.73475 | -49.53738 | 2024-10-12 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afcb42d7-e400-3017-a66a-1b80cce39074 | -2.73422 | -49.54062 | 2024-10-12 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41a3a78f-2001-3638-aaca-c6bbf9bc64e7 | -2.73092 | -49.16115 | 2024-10-12 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0094940b-eb56-32b2-992a-2ad29b1600ba | -2.72581 | -49.1603 | 2024-10-12 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ba05538-73d9-301a-994b-3a01afd37590 | -2.72228 | -49.48289 | 2024-10-12 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f45b647-b9b3-39db-a3ef-0087cd948325 | -2.72174 | -49.4861 | 2024-10-12 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ec6c3cd-8cd3-34fe-808c-b36f0eab3020 | -2.71812 | -49.47563 | 2024-10-12 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8d789ce-d414-399f-9817-c73297bf7c31 | -2.71759 | -49.47883 | 2024-10-12 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 432f9e01-c92e-3b33-b3f7-24e5da9da509 | -2.71706 | -49.48201 | 2024-10-12 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e4d5b7d-193d-3453-a8d3-253cee0b32a3 | -2.59367 | -49.80624 | 2024-10-12 04:04:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d697c00-802d-39d0-9c47-244ac6405b4d | -3.70427 | -50.11393 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| baa8319c-bec6-375c-b8de-b01a2cae79f3 | -3.7037 | -50.1173 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d2970bd8-bcb1-3c12-b14a-0776d94a702f | -3.70313 | -50.12067 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b442de37-286e-322e-b1e4-4f6122f624e0 | -3.70256 | -50.12407 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| eeb9d101-f6ac-3546-80ee-8adc757082b3 | -3.69889 | -50.11311 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 042d9c41-a1ea-3a0f-b101-cc6c643dc473 | -3.69833 | -50.11644 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5b4d1a7d-d4ab-3619-9dd1-ef84a134113d | -3.69777 | -50.11975 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c66d6987-b6a7-3938-8f66-417118841299 | -3.6972 | -50.12309 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7ca357ba-1aa5-3c5a-a4dd-93e07b35d845 | -3.69663 | -50.12646 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d0969b90-fa86-3719-b3a9-dd9b4985f857 | -3.69296 | -50.11553 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b172acd5-0f57-3560-bd8c-009949f7ce19 | -3.6924 | -50.11883 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e9178f7-501a-38e1-8a75-aad40b85fd8c | -3.69184 | -50.12217 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c69ed224-d1f1-383e-8018-960522a90871 | -3.68646 | -50.1213 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88b94409-fa04-3448-b601-aaec53869751 | -3.57699 | -50.56673 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e67314b9-e6d9-340f-bd74-a14b6b124453 | -3.57639 | -50.57036 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f2409817-512f-3fe1-a73f-878fc00fc22a | -3.57632 | -50.56694 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 455150c2-7c23-306b-8a33-3bdfdd65df14 | -3.5758 | -50.57397 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 649df05e-79f3-33ec-80ab-97ff165cc5e8 | -3.5757 | -50.57056 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7d1337c7-7210-3283-94ed-48b2102962c6 | -3.57508 | -50.57416 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8c10f8c4-4eea-37ec-b319-798e87a8489d | -3.57088 | -50.56926 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c58a523e-1708-3b6b-8e13-f639f37814a2 | -3.57028 | -50.57286 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0aac41f4-6773-3a8a-9b9d-506c4b4895bf | -3.28688 | -50.95223 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 281462d5-13ee-3bcd-b1db-072bca3fa781 | -3.28116 | -50.95131 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f7a94d14-d9d1-3506-aaf0-d0caf157bbfb | -3.28051 | -50.95525 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4dc7aaf4-bc99-359f-8887-f9db66c266c7 | -3.27612 | -50.94635 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c67bdf14-8e3f-366e-9e0c-cd38c724ef8d | -3.27546 | -50.95029 | 2024-10-12 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README42.md)
