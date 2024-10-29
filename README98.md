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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a33f1b0-3eb0-36bf-b9ea-ece5fd496d12 | -3.0864 | -53.81384 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e54a2a9-60c5-3774-b494-19e3b9918716 | -3.08565 | -53.81894 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c9e6209-62cf-3827-8481-86b2890e19a1 | -3.04072 | -53.79454 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e55abbba-ce3d-3874-a09a-848064a36f5a | -3.03593 | -53.79371 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 384be0ed-bdcf-3dc0-9411-95d09f0a087e | -2.95554 | -53.87292 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6395c4c1-c1a0-31f7-ba48-39d73f8b71a4 | -2.95549 | -53.87057 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e806f8f-8582-357e-bcdd-6ebaf6fca7df | -2.95471 | -53.87561 | 2024-10-29 05:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01148650-6cdb-3cdc-a07b-4ba86500853c | -2.941 | -53.70861 | 2024-10-29 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2eaf290e-58a2-3944-84ee-ecd2b025ee34 | -2.27971 | -53.77408 | 2024-10-29 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98058e48-6c66-3ff0-bec9-5e465a6af621 | -2.27417 | -53.77847 | 2024-10-29 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 05c7f71d-2d74-3ba9-a16d-d09461a00a2f | -2.27263 | -53.78856 | 2024-10-29 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dba0957c-7d44-345b-855a-f85d6a4691c9 | -2.24857 | -53.72224 | 2024-10-29 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9cc45a8-b1d5-3dee-8d13-43ae29559515 | -2.2478 | -53.72739 | 2024-10-29 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75e488d7-1b55-3485-9aa7-65e8d718c90e | -3.33267 | -54.80318 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0cc2dae2-e2d0-305f-909e-533b21decbc2 | -3.33199 | -54.80763 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 571c7710-5c7d-3d3c-8d1a-4dd7896c1f3f | -3.3025 | -54.69714 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27a0e463-5fb3-3afd-ba16-aa00c7ba1097 | -2.99313 | -54.53932 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41401526-f21c-3790-9408-56d4fbb398e1 | -2.97762 | -54.51812 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 682185e3-f1fe-3ba0-bf31-bd9d1d8ffae5 | -2.9731 | -54.515 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a0caf48c-3ad3-3331-979e-aa02b22f6091 | -2.97307 | -54.51732 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 129b6468-9eba-3ee4-b8d5-9e0c458d454d | -3.63714 | -54.68398 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25947b9c-ee0d-317f-b2df-ec1d0f460c1a | -2.97238 | -54.52198 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 732fc1f4-8b7d-3482-a5d0-39a572b7e927 | -2.97238 | -54.51965 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a169abc9-1e2e-3ab3-8a6a-922833178a96 | -2.96852 | -54.51646 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df52e9f6-20ce-30e8-954e-36b1d7373ee3 | -2.96783 | -54.51883 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2cdd8457-d866-3e41-bc15-d25f41f28fd6 | -2.78019 | -54.73524 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9908711e-9a58-341e-8cfb-ec4455d86753 | -2.77569 | -54.73466 | 2024-10-29 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7d96042-361f-383a-aef5-7901c6e36747 | -2.68292 | -54.96134 | 2024-10-29 05:25:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6632533f-a28f-3374-a16e-28537a593476 | -2.68235 | -54.9628 | 2024-10-29 05:25:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc95a3f7-c4ca-30d7-8107-1be17c5803a3 | -2.68226 | -54.96558 | 2024-10-29 05:25:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b03b6f9a-8be5-3a20-bf88-90a0435406d4 | -2.38727 | -54.66054 | 2024-10-29 05:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 83f740ad-1e4c-3b3d-b330-6050e75d952c | -2.38658 | -54.665 | 2024-10-29 05:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8a649a92-7043-303c-8a02-dac423908594 | -2.16135 | -54.6356 | 2024-10-29 05:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 541b6afc-53e2-36e9-a43a-dc64dcbc524d | -2.15688 | -54.63492 | 2024-10-29 05:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c0a9e5f-100f-311b-ba2a-5bb778789665 | -2.1217 | -54.80422 | 2024-10-29 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 16403780-d838-3d60-a7cc-a4ed54a5a2b9 | -3.70401 | -54.42682 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 17648e5b-56ba-3c57-b064-ddf7f19fa983 | -3.69067 | -54.26043 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 189305fb-18cf-31aa-9092-e46321bd9ab8 | -3.68994 | -54.26536 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9de42bbd-7152-394c-804a-41ef1f38f0bf | -3.66255 | -54.51374 | 2024-10-29 05:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 726983d3-0e9c-3896-ac55-3644b3bc0b27 | -2.44871 | -48.77769 | 2024-10-29 05:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4d54501-fcd9-31ca-9027-9f0a3dc02da7 | -2.44523 | -48.76905 | 2024-10-29 05:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2cdaf5b5-6678-37c1-8db5-aef571817647 | -2.44435 | -48.77477 | 2024-10-29 05:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b43eb759-9a07-3dfe-83ae-b2844a09ec78 | -2.44291 | -48.77106 | 2024-10-29 05:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48e40a8d-09dd-3199-aa06-55dd9cab3d67 | -2.40363 | -48.5489 | 2024-10-29 05:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6227ea31-b955-3804-bd17-a9cc586a8098 | -2.40275 | -48.55477 | 2024-10-29 05:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4bef6f09-e396-330e-9803-8982fa76f0fc | -2.39605 | -48.55374 | 2024-10-29 05:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95046935-a7c7-36c3-bbff-d5719c155683 | -2.19442 | -48.83511 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d9e3665-200a-30c9-9b48-acc4c0ab81ea | -2.97122 | -48.05574 | 2024-10-29 05:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 874d17f6-fa82-3d30-8147-441048cb65ce | -2.97026 | -48.0577 | 2024-10-29 05:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 01a870b3-889a-3e82-af16-52bc70d2efda | -2.97022 | -48.06234 | 2024-10-29 05:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f673e7cc-213a-364d-9e38-990bdc3eddbc | -2.96932 | -48.06427 | 2024-10-29 05:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b2cc2018-97e2-30e1-8410-7eb8d53ff019 | -2.37308 | -47.67335 | 2024-10-29 05:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a85c13a2-3330-34aa-a203-5771dccf089a | -2.37155 | -47.66789 | 2024-10-29 05:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce773768-7789-3c47-9800-522fc756006c | -2.36604 | -47.6722 | 2024-10-29 05:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df630b20-1b02-361f-a45c-0d07ce10b938 | -2.36353 | -47.67343 | 2024-10-29 05:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8d8cbb7-c8d6-3292-9225-b6e86813d3d4 | -3.93544 | -48.35249 | 2024-10-29 05:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f1a302c6-95cb-376a-bb6e-9f6f5387ab04 | -3.9285 | -48.35162 | 2024-10-29 05:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 802bfc6c-92ff-3b31-8752-8949d800231e | -3.92162 | -48.35032 | 2024-10-29 05:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eecfc8aa-3f80-32e5-934e-5a06bc384d8c | 0.0795 | -49.87557 | 2024-10-29 05:25:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd90e5e0-020e-324c-ab54-ffff155c6eae | 0.08547 | -49.87465 | 2024-10-29 05:25:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c38c71bc-c227-32d8-aac5-5a497ffbf24c | -2.10181 | -49.6955 | 2024-10-29 05:25:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c3bbb765-5197-3246-bbf3-7cd5cf88c1d4 | -2.10055 | -49.69357 | 2024-10-29 05:25:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c976412a-f738-36ae-aa62-ed0d8d42a5bf | -2.09982 | -49.69846 | 2024-10-29 05:25:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0a112add-5a31-37e1-89c3-208ee8cb3762 | -2.09558 | -49.69457 | 2024-10-29 05:25:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 93c53b14-ae93-3798-b72a-14c21e2d89dd | -3.4206 | -50.34348 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a711e44-3b75-3fa6-a169-82b7d8fac266 | -3.35961 | -50.1628 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 616e9454-8cd8-3a5e-b72f-289049478a45 | -3.35418 | -50.15693 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0548165-588f-3222-9fb6-6e3468214790 | -3.35346 | -50.1618 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 187b0149-c157-3d40-9dc5-f63c754a1d25 | -3.32742 | -49.91828 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecaa33f5-c5b0-327f-a555-981c9f8bcf9e | -3.32511 | -49.92092 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4975170-6455-3f67-a09c-6c87bcf312c3 | -3.31918 | -50.30969 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8509be36-341f-36be-a0bb-0f5cdc6c4f52 | -2.83235 | -49.23679 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75df49b7-6c3a-34a9-a822-4b4735704054 | -2.83155 | -49.2422 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dd1eedf3-991c-340b-bc4f-097c67fbff2b | -2.82666 | -49.23045 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f0a96aab-2b97-3428-9c73-b701afd18e96 | -2.82587 | -49.23583 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 0789f192-4a99-3374-8617-2492f7819c77 | -2.82508 | -49.24124 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 5d96e0a1-92ed-3a7c-b212-4e216e7626f3 | -2.81939 | -49.23491 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8369ad99-54bf-3554-bcbc-7cf0ab440c29 | -2.8186 | -49.24028 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| f3398084-91ac-376b-ab57-372c6ad11f20 | -2.81452 | -49.22302 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| caf26bf6-7db7-3f52-b760-e688f952741b | -2.81371 | -49.22858 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e36b0306-c5ee-3cd8-a463-87a32220f203 | -2.81361 | -49.22544 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c664e91c-9c57-305d-8922-d3ca7a66bd53 | -2.81276 | -49.23095 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1505a28-f9f2-30df-8a85-4811f8fd835a | -2.80804 | -49.22207 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 309f6750-b945-3d67-b4bd-06a2a9f9d029 | -2.80796 | -49.21907 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 735b2770-9329-3100-81aa-3f618806321c | -2.80724 | -49.22757 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7cce4014-66c5-3e2c-b749-3d7ce3af1253 | -2.80713 | -49.22453 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 26ebfb68-3dc7-389d-b42a-6029a561d9bd | -2.8063 | -49.22995 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2c5c912-7c66-3cd2-a788-11969f67c081 | -2.65774 | -49.25177 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 4080833d-6c78-3d73-b3ac-32acc26ca2f8 | -2.65735 | -49.25067 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2c20cce4-dfb7-3b79-82df-f50860099278 | -2.65697 | -49.25712 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| d21aec6d-5e0f-3156-a768-2d06b810c049 | -2.65654 | -49.25605 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 5de1da11-dcbf-3aef-b853-16729f76a234 | -2.6562 | -49.26245 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| d6732957-3c44-3947-b8f6-d5dd702b13c4 | -2.65574 | -49.26134 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| c1300b8c-a20d-3be2-a713-c5057befe6ee | -2.5739 | -49.1442 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 73a84b87-ee9a-3357-aa13-ee1c41bdcc84 | -2.5569 | -49.16693 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7d25be7f-cb64-330f-9fc5-1422b09bf898 | -2.43757 | -49.03408 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6afa4053-6f0e-3257-a005-1ff4e02bec18 | -2.43675 | -49.03954 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c01fe0cf-a15f-38aa-b243-30e24380d910 | -2.34219 | -48.91544 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 80344b55-7c46-34cc-80c1-fbc03d1436b2 | -2.34136 | -48.92099 | 2024-10-29 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9948f930-8b81-33a6-9a5f-78eaf5efb4d1 | -3.0705 | -50.50875 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README99.md)
