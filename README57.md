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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec93f6a9-84ad-3cff-8b37-cd352ae853b4 | -2.48937 | -48.05065 | 2024-10-27 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59cfa47f-d2b5-3f57-8693-b499b0bc3337 | -2.4888 | -48.05444 | 2024-10-27 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b82ab848-763b-31b0-9fe2-8b46f0919ab5 | -2.3683 | -47.67088 | 2024-10-27 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ab62df1-b842-3785-9935-358751346ae3 | -2.36828 | -47.6675 | 2024-10-27 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1c44861-d479-3d92-beb3-7df33ce8b636 | -2.36766 | -47.67151 | 2024-10-27 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e45ef54f-35cd-335b-87cb-5ec8958cc91d | -2.36253 | -47.66989 | 2024-10-27 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6efb3d5-858d-375e-a83f-0b2268a8be80 | -2.3619 | -47.67055 | 2024-10-27 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97471c7a-42e7-3089-bdb6-0d341441cf91 | -2.15778 | -48.45338 | 2024-10-27 05:16:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e31e601b-62f5-3e15-bccd-1dd5381faa5a | -2.10198 | -48.55461 | 2024-10-27 05:16:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c747a32a-ad97-33ae-a5a3-50e9a8f1d93f | -4.95558 | -48.64487 | 2024-10-27 05:16:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 286da5ed-3c32-3a60-8679-5e5e0fb7ad9b | -4.95505 | -48.64863 | 2024-10-27 05:16:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5294b928-05cc-3a2b-9736-7e3c0dc1e409 | -4.30101 | -48.65026 | 2024-10-27 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4a38605-bb3c-333d-a4e2-9976fa37bedf | -4.30049 | -48.65388 | 2024-10-27 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 875dd034-db24-3c8a-9daf-d8b061f7dad4 | -4.29594 | -48.64593 | 2024-10-27 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5281452-d217-34d3-8211-4242f4705062 | -3.93727 | -48.36269 | 2024-10-27 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6dab3914-d39c-327c-88a7-734b07094543 | -3.92811 | -48.34622 | 2024-10-27 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3eb6aa1-c5c0-36fe-8f95-eb40a1907f70 | -4.57982 | -48.02785 | 2024-10-27 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 464b71ce-d069-35a4-99b0-8bc093896b8b | -4.57499 | -48.02167 | 2024-10-27 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d18b9dfb-fbb6-34b7-afde-257d8b88d273 | -4.57456 | -48.02291 | 2024-10-27 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f084197f-c955-3de7-a526-81fac66ea5ee | -4.57399 | -48.02695 | 2024-10-27 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 163311e1-99e3-3572-9c77-2e7578c6237c | -4.57381 | -48.0297 | 2024-10-27 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 24901245-5248-382a-b58e-6e3d590c0230 | -4.57344 | -48.0309 | 2024-10-27 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 152aee46-c80a-31f8-9dc5-a601be77a432 | -4.57324 | -48.03355 | 2024-10-27 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 006b8026-6af0-3691-bc7e-02266c58c533 | -4.5729 | -48.03473 | 2024-10-27 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55657747-84a6-30ac-b8d8-c0573a755563 | -5.70692 | -49.31099 | 2024-10-27 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 062b4157-dba9-3bac-83a6-49924faada70 | -5.52116 | -49.49771 | 2024-10-27 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 07039594-9a94-30cd-a7ea-d291c6b4ed57 | -5.51893 | -49.49648 | 2024-10-27 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67360ccb-d4cf-3201-8666-370a54ca01a6 | -5.51846 | -49.4999 | 2024-10-27 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c0369d2-0fd4-386a-a863-31b46e03d917 | -2.47494 | -49.105 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 31cd8ac7-6898-34bf-b207-eb939656b6b6 | -2.47476 | -49.10571 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ff26fca6-f32e-3696-abce-9ca0733a06d2 | -2.47444 | -49.10821 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f83bae25-69d3-30c3-8184-e3018ad25819 | -2.47429 | -49.10891 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b38c2383-65f8-3bda-824a-e646d7fff28c | -2.47395 | -49.11139 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8d883a28-168c-33f9-85a4-1bbf491e9d54 | -2.46968 | -49.10416 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f665c1b-4bc0-38d8-894d-3788b2f6d827 | -2.46951 | -49.10486 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c7986db-101c-3347-9446-cbf630bfd899 | -2.46919 | -49.10737 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f06214de-5cff-3a84-8d4d-cf58cf0f097b | -2.46904 | -49.10809 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0032c286-c60b-3edb-b813-292eb1686fb5 | -2.42582 | -48.89206 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 999148f8-e43c-3d01-8b8b-b6deace1d43d | -2.41502 | -49.21665 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f85e8b9e-bacc-3a4a-a57e-9a12c7e16c44 | -2.41083 | -49.13784 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 922e195b-594d-3a75-87c9-906fa721aec0 | -2.41035 | -49.14104 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99a2ca0a-ab37-3f62-9416-675694731294 | -2.41028 | -49.21264 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a3b43a8-73f9-38cf-870c-82ddc6ed1368 | -2.40981 | -49.21579 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f4dccab-60cc-3c4a-9a3e-93df8fa240c2 | -2.39556 | -49.82038 | 2024-10-27 05:16:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 74b8b3d9-01a1-33d5-814d-1eeee731d196 | -2.39514 | -49.82322 | 2024-10-27 05:16:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c92a0ded-09b8-3555-bbd0-5c2a65edb86f | -2.38528 | -49.37843 | 2024-10-27 05:16:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fbaf7d3a-4de2-3cb5-a0eb-a610c4a9d4d8 | -2.38481 | -49.38153 | 2024-10-27 05:16:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 08a81f8e-eb54-303f-afc6-1b6a32c64632 | -2.8499 | -49.25621 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6993ea97-84f6-3837-bb15-cb3ab94c0dc9 | -2.84612 | -49.24574 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f80f215-1a39-3b07-8b61-233f54200492 | -2.84563 | -49.24896 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc0f8328-2015-3b58-a6d4-6e8e5d65a63b | -2.84515 | -49.2522 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f870c1d9-7f64-3459-8b3b-0bf2e4309874 | -2.84466 | -49.25543 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c2a06f44-b5d2-3347-9208-dba02f355946 | -2.84418 | -49.25867 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e697b0d4-7b10-3c6d-8a0c-d9f2dce2daf0 | -2.84369 | -49.26189 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 98b39e1f-b4ef-3dcc-a60b-61a120a3972b | -2.84183 | -49.23857 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0306867f-ae59-3b89-a2d2-3eebd14cd739 | -2.84136 | -49.24176 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f22316c-6de8-38a8-a31e-36047d465fab | -2.84088 | -49.24497 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63e74b86-4db3-3826-955c-a1152d569efe | -2.84039 | -49.24819 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d07c1253-5d53-3056-905c-f783514cf7e6 | -2.83991 | -49.25143 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 17cc1f2a-ba8a-3e8e-a4f5-3790fa4cd3b2 | -2.83942 | -49.25465 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e0cd8263-95ab-31e1-9e19-c384e12dff28 | -2.83894 | -49.25788 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 82d5ac19-0c42-3cf4-88e1-d1943b31ae86 | -2.83846 | -49.26108 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 11a512c5-1bb9-3c18-a760-2263369f05d9 | -2.83659 | -49.23777 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38aa8306-0db3-3bac-b338-4b2080a8ff97 | -2.83611 | -49.24097 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99147d00-488a-3058-b722-d812238b30ef | -2.83563 | -49.24418 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a42cb697-40ee-3a1a-ad46-91bc2a4ebe4e | -2.83515 | -49.2474 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f89aa41d-0989-318f-a109-81965b79ffda | -2.83467 | -49.2506 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5ca389b3-a00e-3ea4-8549-5614ac45e592 | -2.83419 | -49.25383 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 638a5fac-7101-33a8-a527-76a8b60786c8 | -2.83371 | -49.25704 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6893556-082d-3837-be81-e63a5029d42a | -2.83323 | -49.26025 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6e8e129-f154-3adc-a574-34ae2a70f6ed | -2.83088 | -49.24015 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac3f54de-3dc8-3506-bfd3-4bd6a236cf0b | -2.8304 | -49.24337 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0d404335-51f5-366e-ae2f-3e9df3111b90 | -2.82992 | -49.24658 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9d83b6ee-5567-33a2-b73d-2f7a39fdc7f4 | -2.82944 | -49.24978 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7c90d082-811d-3382-9fe9-73c1a603b49a | -2.82896 | -49.25297 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 921ee945-95ed-3be8-8f55-af0d46871b16 | -2.82848 | -49.25618 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4db4466-d217-3ea7-96f5-81018f04532b | -2.82516 | -49.24255 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67324cfb-bab0-3b33-8639-d25f329b2655 | -2.82468 | -49.24575 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11fa2e0d-27b1-35bc-8716-c6a83b31dc4f | -2.8242 | -49.24895 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a41e8c7d-2030-3745-8990-cc6062de8870 | -2.70624 | -49.32021 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 86a8c3a5-0846-33bb-9f4a-d15db0186460 | -2.7015 | -49.3163 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| aa7d8e3c-4803-3083-ac13-2df43a46c249 | -2.70104 | -49.31942 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3a96e049-e7c3-335c-88ce-9b487a5e73a3 | -2.69265 | -49.75665 | 2024-10-27 05:16:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bcdf8ee-3877-35ac-96a0-fa5c1847703b | -2.6919 | -49.75521 | 2024-10-27 05:16:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f03e2888-00ba-342c-a82f-96c99154cd60 | -2.64313 | -49.23672 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8bc1099-4afc-37b5-88f4-23c23216dc30 | -2.64265 | -49.23992 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4c160151-828b-3e05-adb6-dfff876ebd5c | -2.63839 | -49.23272 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91a9c7a7-0f0a-3014-b2f0-a4796029fb9e | -2.63791 | -49.23592 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19cc3f7f-b5b5-327f-a393-5c5caa1af89f | -2.63742 | -49.23912 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| da770a27-012b-3d32-ab53-55af00a4c8be | -2.63694 | -49.2423 | 2024-10-27 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9d339a1d-bd69-31bb-92fa-b688e077fc8e | -2.58231 | -49.77272 | 2024-10-27 05:16:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| efec8f50-e999-3364-b0bd-ccf832301a56 | -2.58187 | -49.7756 | 2024-10-27 05:16:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 812e2095-e364-37f2-93de-2d99e3cf5adc | -2.58158 | -49.77528 | 2024-10-27 05:16:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 95901876-bda5-3866-aed9-47466e808aae | -3.48192 | -49.59076 | 2024-10-27 05:16:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c53f286f-ef82-3846-9a7e-9284afd9a6f9 | -3.47674 | -49.59008 | 2024-10-27 05:16:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 906fccd9-92f6-3a69-ae8e-f0d59df4700c | -3.33605 | -50.11481 | 2024-10-27 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e9c66211-ad1b-3dd0-944e-0714f3d99e27 | -3.33563 | -50.11765 | 2024-10-27 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f804c018-ba52-3c52-8f25-14cb46fe2f3d | -3.33106 | -50.11414 | 2024-10-27 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8526bca3-1b5f-315b-89db-4084252c7748 | -3.32943 | -50.09063 | 2024-10-27 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2948815-7ae1-3d21-b4d1-68139d71b4ca | -3.32902 | -50.09345 | 2024-10-27 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README58.md)
