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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 714234c7-483c-3fac-88e1-8e8a99737b6e | -10.1058 | -36.1748 | 2026-02-02 00:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 118.5 |
| ee6a123a-746e-3df7-aad9-ac3c7eb98778 | -10.0865 | -36.1782 | 2026-02-02 00:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 107.0 |
| d3d9a91e-1407-385b-b172-23fcd004673c | 4.354 | -60.3789 | 2026-02-02 00:10:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 96506081-3056-3230-9896-01844b6463f7 | 4.0784 | -60.6894 | 2026-02-02 00:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 79142d19-bea1-3b3d-a286-31970bc40593 | 3.4202 | -60.6647 | 2026-02-02 00:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 9138c4fd-4fd9-360f-bc28-ec2a9b9e0f4d | 4.3723 | -60.3785 | 2026-02-02 00:20:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 27.8 |
| edc616ec-d995-332f-8f12-c22e13af6a26 | 4.354 | -60.3789 | 2026-02-02 00:20:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 1e1a6b42-b1ee-3480-b7ff-bdfc713c3de8 | -6.0486 | -48.10715 | 2026-02-02 00:28:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3ba7047f-4ae7-37f8-95da-7308fb50ea62 | 4.354 | -60.3789 | 2026-02-02 00:30:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 31.8 |
| f05d25bb-1212-30b3-8c4c-7820ca3344af | -3.15644 | -48.14777 | 2026-02-02 00:30:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d735c2f3-b8c2-3621-82a1-6349c0d60ab2 | -3.14634 | -48.14927 | 2026-02-02 00:30:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 6227922f-bedc-3285-b63b-e41c5a562fe0 | -3.14467 | -48.1374 | 2026-02-02 00:30:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f38a8f73-fd9d-3675-8853-f9b8b482847a | 4.06904 | -60.68083 | 2026-02-02 00:32:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 77fa3943-489f-37da-a760-e24480d6640b | 3.4202 | -60.6647 | 2026-02-02 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 30.7 |
| d6560389-ca72-3ab9-95da-f86b6b02092d | 4.354 | -60.3789 | 2026-02-02 00:50:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 337ba744-ad69-3e51-abf7-b55ff33cbfe0 | 3.4202 | -60.6647 | 2026-02-02 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 2dd88223-b99c-3aa2-914e-06ea3469c15a | 3.4202 | -60.6647 | 2026-02-02 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 43c1253c-49d5-32b0-b4fc-170db07ef2db | -10.0478 | -36.1852 | 2026-02-02 01:50:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 90.2 |
| 590ce56d-9913-3292-9210-7400c6d96b9e | -10.0672 | -36.1817 | 2026-02-02 01:50:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 84.6 |
| f4fcdb2b-7737-3f11-b332-7baa25f4b215 | -9.56957 | -37.39063 | 2026-02-02 03:06:00 | NOAA-20 | SÃO JOSÉ DA TAPERA | ALAGOAS | Brasil | 2708402 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5dc06a1f-cc4a-3c77-b9c3-97d325254986 | -7.47643 | -35.1434 | 2026-02-02 03:06:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c546f218-2f07-3ed6-a447-8eda36fffdde | -7.47517 | -35.14326 | 2026-02-02 03:06:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8f1ce5f2-6079-395f-84e6-175d63e88816 | -8.99292 | -35.23849 | 2026-02-02 03:06:00 | NOAA-20 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3d43095a-edec-3aac-8371-4cd0bf174c66 | -7.47116 | -35.14239 | 2026-02-02 03:06:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 819f7118-2ca7-39d6-8431-a3d0ba190546 | -7.47578 | -35.13994 | 2026-02-02 03:06:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e370ff7a-e50d-3af8-b671-01d25b8cdd49 | -7.47701 | -35.14009 | 2026-02-02 03:06:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9610daab-2a14-33c6-8700-1c74f56f883b | -8.99234 | -35.24163 | 2026-02-02 03:06:00 | NOAA-20 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f378242a-6951-3e97-af36-39c7f2336eab | -1.52143 | -45.92185 | 2026-02-02 03:53:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a6169324-5bf5-32bb-8be2-62dfc72fd8e0 | -1.5219 | -45.91886 | 2026-02-02 03:53:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f4869d83-fd94-3b26-8257-d8d86bf50b16 | -3.05299 | -48.46512 | 2026-02-02 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a34eec9d-a8c8-3d0b-b284-df5748736567 | -10.18179 | -39.04953 | 2026-02-02 03:55:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3031df8a-378a-3ec3-8bc5-24ba45eebe10 | -7.69915 | -35.03809 | 2026-02-02 03:55:00 | NOAA-21 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ee08080e-4de5-3fb8-a22b-4c1187ea1a2e | -7.47811 | -35.13948 | 2026-02-02 03:55:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d572d50d-fc6f-36c6-871f-143d89719097 | -5.23865 | -40.87257 | 2026-02-02 03:55:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6796017a-3405-30ef-ab58-9a32dd866b96 | -2.6295 | -42.74207 | 2026-02-02 03:55:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cc8fca01-25c9-35f8-9d88-ca007b9f53aa | -3.06649 | -40.11156 | 2026-02-02 03:55:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 716d6f3c-ad1f-3709-9c91-f30d746fc429 | -6.58146 | -38.54948 | 2026-02-02 03:55:00 | NOAA-21 | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dca4cc4c-8c78-38af-9eb7-33e38ac17ec9 | -8.71124 | -38.64056 | 2026-02-02 03:55:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 296e3f5c-1b49-3495-90ff-12bf4c9a13e9 | -6.74089 | -37.98732 | 2026-02-02 03:55:00 | NOAA-21 | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9bffb017-9560-322d-80d5-4c1a9cba57cf | -5.43849 | -38.56916 | 2026-02-02 03:55:00 | NOAA-21 | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9898eb83-24be-39ce-af48-fb700666fd67 | -4.92296 | -37.42472 | 2026-02-02 03:55:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ba19f081-eca7-3942-807e-16c643ed9fff | -7.47376 | -35.1433 | 2026-02-02 03:55:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| aa674d5b-4623-3609-8e03-80ac7cad0dcd | -3.2748 | -42.38532 | 2026-02-02 03:55:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| bb4c0b7a-49fe-37db-b8fe-41e51afc4fd4 | -9.81476 | -38.10105 | 2026-02-02 03:55:00 | NOAA-21 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b25b982b-1e8d-316f-be78-47768c22e499 | -7.88735 | -37.37135 | 2026-02-02 03:55:00 | NOAA-21 | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 79e6124c-6d3d-3003-bb40-c6486368e09d | -3.97949 | -40.91561 | 2026-02-02 03:55:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e44d8e73-ff1c-399d-a1a2-2ae35b769189 | -10.74018 | -37.06282 | 2026-02-02 03:55:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| eafd182a-d152-347d-9efe-3d9e011a02dd | -7.73943 | -34.95897 | 2026-02-02 03:55:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| fd92d97c-16e5-3678-8e5a-7ab4ec057d72 | -6.22649 | -35.62811 | 2026-02-02 03:55:00 | NOAA-21 | SERRINHA | RIO GRANDE DO NORTE | Brasil | 2413508 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a0e973d0-33c8-3b24-b234-f365a73da1fc | -6.43368 | -35.26361 | 2026-02-02 03:55:00 | NOAA-21 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1c37572c-d84d-312d-bcf7-a0b039ff7c8f | -8.24753 | -35.96022 | 2026-02-02 03:55:00 | NOAA-21 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cf325cc3-e1a2-382d-ba50-9d140cf0fc22 | -6.04395 | -40.32231 | 2026-02-02 03:55:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7b625231-d91e-30b1-9d07-9af93b5daa2d | -5.53346 | -43.68899 | 2026-02-02 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd89814a-f1c3-3f67-85c4-258acdedac69 | -7.94922 | -36.80954 | 2026-02-02 03:55:00 | NOAA-21 | CAMALAÚ | PARAÍBA | Brasil | 2503902 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| af3461f2-e7c3-3111-b6a6-cff71b7d1a02 | -5.3631 | -38.59199 | 2026-02-02 03:55:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5b1ca27c-b4f2-331a-a8de-8a2c8438bad4 | -5.23514 | -40.87203 | 2026-02-02 03:55:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e3fd2f06-6cc7-3890-b117-fdbc286b4a51 | -8.99546 | -35.24075 | 2026-02-02 03:55:00 | NOAA-21 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 9e2082e3-3a31-3af7-93f6-1229b27e6279 | -8.99611 | -35.23622 | 2026-02-02 03:55:00 | NOAA-21 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 9c8baad5-ee7a-32e9-b43c-728ed8142f75 | -9.81421 | -38.1046 | 2026-02-02 03:55:00 | NOAA-21 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b00636a4-b2de-37be-aff7-566f518f0aa4 | -9.56978 | -37.38639 | 2026-02-02 03:55:00 | NOAA-21 | SÃO JOSÉ DA TAPERA | ALAGOAS | Brasil | 2708402 | 27 | 33 | nan | nan | nan | Caatinga | 0.2 |
| b5ee5d33-ac44-374a-b4c4-747da79babb1 | -6.7442 | -37.98783 | 2026-02-02 03:55:00 | NOAA-21 | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 70c24006-801a-3d08-b7fc-152656b7a443 | -6.875 | -35.24171 | 2026-02-02 03:55:00 | NOAA-21 | CUITÉ DE MAMANGUAPE | PARAÍBA | Brasil | 2505238 | 25 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 80c57a98-0b8d-3873-be91-35338596bb1c | -7.47713 | -35.1415 | 2026-02-02 03:55:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4a631299-b111-3bb9-af14-fed92ef2a08f | -5.09384 | -37.55124 | 2026-02-02 03:55:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.4 |
| bcd1449e-e466-3c48-a103-66103b026dde | -5.87707 | -39.69017 | 2026-02-02 03:55:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4d580349-ae34-3efd-b737-a092ed349816 | -6.87137 | -35.24113 | 2026-02-02 03:55:00 | NOAA-21 | CUITÉ DE MAMANGUAPE | PARAÍBA | Brasil | 2505238 | 25 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 3deb1460-6bed-377a-8ea1-09bedcafc4a4 | -4.50204 | -42.4217 | 2026-02-02 03:55:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5ee803b5-f3ec-3640-8cab-6c0ed0189571 | -4.24123 | -45.18602 | 2026-02-02 03:55:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eed554e9-caf0-325c-8fc5-098992e3bd46 | -5.43519 | -38.56865 | 2026-02-02 03:55:00 | NOAA-21 | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 375d6e6d-9279-3c0e-bb76-c0d4dc14ca5f | -8.99173 | -35.24019 | 2026-02-02 03:55:00 | NOAA-21 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| e2ad7d75-691e-3473-95ac-1a4887c62ca5 | -9.33414 | -36.19894 | 2026-02-02 03:55:00 | NOAA-21 | VIÇOSA | ALAGOAS | Brasil | 2709400 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c72e7017-fe78-36fa-b94d-f0f16f482c1e | -3.0671 | -40.10772 | 2026-02-02 03:55:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9900df69-8c06-303e-9dbd-bcfade50d2d4 | -3.07057 | -40.10827 | 2026-02-02 03:55:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 703d27c2-0737-30c2-9562-1fc4559391a2 | -8.71454 | -38.64108 | 2026-02-02 03:55:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e9743d07-d6cb-3822-886d-b0b7fbe2ee14 | -14.90022 | -39.02987 | 2026-02-02 03:57:00 | NOAA-21 | ILHÉUS | BAHIA | Brasil | 2913606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 85d63ef3-a2a6-3932-b7fe-bd82639bb4cb | -14.08707 | -47.20205 | 2026-02-02 03:57:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 60cd240f-8218-3c25-bcd6-22351511ebe0 | -24.3095 | -49.75349 | 2026-02-02 04:01:00 | NOAA-21 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65ea872c-6759-3008-9256-579e00f1f170 | -24.30915 | -49.75564 | 2026-02-02 04:01:00 | NOAA-21 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b02e7ee9-65f9-30b2-b846-7fc54853ae29 | -28.63684 | -50.46569 | 2026-02-02 04:01:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ece30f20-ac1a-3413-a9ca-564cc1fd52f4 | -3.06704 | -40.11177 | 2026-02-02 04:23:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4076f066-c141-32fe-b363-77315a113f4a | -3.27319 | -42.3843 | 2026-02-02 04:23:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d90e6a2c-2b70-3f42-84f2-f5209ff3fff7 | -1.5027 | -46.03033 | 2026-02-02 04:23:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 89087ac2-fdb1-356f-87a7-1a48a888b8a1 | -2.43236 | -46.92018 | 2026-02-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 630e89d2-cca7-3a6a-8549-5a770746622d | -2.42288 | -47.14444 | 2026-02-02 04:23:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecfc0594-8ca8-3cb2-ae93-5fcbc7e0981a | -2.39841 | -44.87256 | 2026-02-02 04:23:00 | NPP-375D | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10c31972-176f-37cb-ac6f-d91226fdc4e8 | -2.60886 | -44.20659 | 2026-02-02 04:23:00 | NPP-375D | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42abc125-0b56-38a3-a049-85645bdaa898 | -2.42242 | -47.14708 | 2026-02-02 04:23:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc06a71b-fc4b-30fc-844b-ee4457ceff46 | -9.98168 | -36.28519 | 2026-02-02 04:25:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4a33fb63-ba5f-375b-bc03-f7b1ef9f8aa1 | -6.74393 | -37.98841 | 2026-02-02 04:25:00 | NPP-375D | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5a5bf523-c23b-336e-a5f3-e29aafaea714 | -5.59813 | -45.37025 | 2026-02-02 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2bb35370-422c-3a5f-b7db-ef980920ea79 | -3.15156 | -48.14223 | 2026-02-02 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bc58ab6c-b68e-3384-951d-9f3f56504ddf | -3.98096 | -40.91362 | 2026-02-02 04:25:00 | NPP-375D | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c6c70932-613d-321d-9ea1-cbad8c9c1e0a | -3.14774 | -48.14162 | 2026-02-02 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 21f5cd9f-0dda-36aa-b28c-5bede3c3a759 | -9.9871 | -36.28591 | 2026-02-02 04:25:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6f85853c-2a7d-3b4b-a058-c044d20d10eb | -9.98555 | -36.28838 | 2026-02-02 04:25:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 69534d73-5197-3da5-ad30-a304c1c49565 | -5.09088 | -37.54935 | 2026-02-02 04:25:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1c6d57f8-9f59-3b13-9e91-34fad01601db | -3.1508 | -48.14687 | 2026-02-02 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| eb9b34f5-b046-38f6-9f68-67313bb59afd | -5.36032 | -38.59345 | 2026-02-02 04:25:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0c46ffe1-9e69-3074-8489-1aaae612b0cf | -6.11173 | -46.5865 | 2026-02-02 04:25:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e31813f-c61d-3400-821b-5637add0589b | -3.14699 | -48.14624 | 2026-02-02 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README2.md)
