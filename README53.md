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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf8775b1-d791-363a-99a9-286919eb5d41 | -5.9788 | -45.3621 | 2024-11-07 05:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 65dcf74c-a079-3121-98d5-c9a276544660 | -2.2845 | -53.8224 | 2024-11-07 05:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| d5079621-ad86-3acf-8bcb-29f2b248fe7b | -5.9975 | -45.3607 | 2024-11-07 05:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 09240084-8cce-3cf4-b371-10de9bb9f95c | -3.5863 | -50.2527 | 2024-11-07 05:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 18acd9bb-bfba-3810-8be6-2c776842a4a2 | -2.82 | -52.9613 | 2024-11-07 05:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 84d944a3-8978-3382-9c90-4737e2957d7c | -3.6602 | -50.2501 | 2024-11-07 05:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 749a2b2b-64db-3379-bfcd-c0ebf7fb5188 | -2.8537 | -48.6642 | 2024-11-07 05:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| d613612b-a1fb-3a1d-a287-026efc5c3771 | -2.9464 | -48.597 | 2024-11-07 05:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| ea342bd7-b2c8-3531-b01a-a62914a01efa | -8.3091 | -43.6112 | 2024-11-07 05:50:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 42acbee6-16e3-3d08-81ae-b9a9fa6b4880 | 0.68834 | -51.4371 | 2024-11-07 05:50:00 | AQUA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 959f3c43-bf4e-36ae-8cbe-8af58ffa692f | -2.66794 | -49.86893 | 2024-11-07 05:52:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| fd1d562f-2e06-33a4-a007-ab2bed4e92ef | -3.87989 | -52.37893 | 2024-11-07 05:52:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 16a62c2b-a376-39e1-a1a8-84b2cb4eb6c3 | -5.98287 | -45.37627 | 2024-11-07 05:52:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| e189b9ce-916c-331a-a2d8-db9509f0900a | -2.97293 | -53.86906 | 2024-11-07 05:52:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cb86efd9-14af-3d1b-8a95-6323b439944e | -3.67011 | -50.22722 | 2024-11-07 05:52:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 473a4a6b-1f46-3267-a677-d4f64f556458 | -1.53047 | -52.22217 | 2024-11-07 05:52:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b70100e7-d192-33c9-819b-b7304197318e | -1.45853 | -53.49684 | 2024-11-07 05:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ba3b92ae-6c06-39f9-97bf-2adcc9518bf2 | -2.23611 | -53.67496 | 2024-11-07 05:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 8d687a6d-18e3-3a7c-9a70-3fa44207199f | -2.67937 | -51.8227 | 2024-11-07 05:52:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a78f48d3-2262-39bc-9a8f-d55301eedf42 | -3.7117 | -48.9962 | 2024-11-07 05:52:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 20e93998-5df3-3832-8b79-50d13f216105 | -3.19532 | -50.58649 | 2024-11-07 05:52:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 67ee56b6-ecbc-3bb6-842d-5532394d569c | -3.33304 | -53.19017 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cc071cce-297b-364c-9dfb-7f6fb2dc2448 | -2.41564 | -47.78065 | 2024-11-07 05:52:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 3fddf0c4-c9b3-3dc0-a39e-c106349758e6 | -2.06475 | -53.26904 | 2024-11-07 05:52:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| de2c6724-9a27-368f-9bc1-f5e817a4b7fb | -1.52461 | -52.13999 | 2024-11-07 05:52:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9e9c052f-2dde-3eed-981c-e924cf6197c5 | -2.08429 | -52.04014 | 2024-11-07 05:52:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ae87ba30-3531-3ad2-982e-075a722ecea9 | -1.10385 | -54.19748 | 2024-11-07 05:52:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| aa29227b-f098-3b0c-927d-429aa64a2f59 | -2.66676 | -49.87344 | 2024-11-07 05:52:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 8c95d253-99c9-3648-896c-a86d7200fb14 | -1.39589 | -52.19021 | 2024-11-07 05:52:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 63b5b018-cfda-3881-b3f8-be211e6233af | -1.55045 | -52.27016 | 2024-11-07 05:52:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 1e3e1766-d9f1-3d6d-ac11-5a820d839383 | -4.99735 | -49.89051 | 2024-11-07 05:52:00 | AQUA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 75a3a955-6d00-3171-9679-24a3e028e6cd | -0.41019 | -51.56121 | 2024-11-07 05:52:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 15.0 |
| d01f164f-ef6c-3873-a80f-e325dc927584 | -2.8174 | -52.93416 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9e2f761b-86a2-3101-92b3-3ae72c59f4c5 | -1.55931 | -52.27144 | 2024-11-07 05:52:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ab6b0824-1382-3899-aab8-d8b8e4e0b330 | -2.81477 | -52.95173 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| e281e9fc-7102-38b6-bee2-83f6877f9ae0 | -0.41152 | -51.55223 | 2024-11-07 05:52:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6214960c-53a4-384e-b29b-4e93a48f6a04 | -3.70413 | -51.3836 | 2024-11-07 05:52:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7a4a508d-6d52-3461-a491-cea8952d74ee | -3.24665 | -53.39553 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 291ff232-8672-3546-b295-5cb51a68a40d | -3.58677 | -50.2321 | 2024-11-07 05:52:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 361a4079-96ad-3ac4-86eb-a637a09f638f | -3.66691 | -50.24924 | 2024-11-07 05:52:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 65d5eba9-4489-3eeb-946c-f24058f5a96e | -3.595 | -50.24429 | 2024-11-07 05:52:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 4b11a74f-eab3-396d-8c4d-76460b5a31a8 | -8.30853 | -43.62799 | 2024-11-07 05:52:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| a6a81dd2-4246-3f26-909b-2e9b176b27b8 | -2.28944 | -53.80856 | 2024-11-07 05:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 97f07592-e555-3735-af7c-d25dd0740819 | -2.88441 | -51.30802 | 2024-11-07 05:52:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ed14a84b-622e-3c39-9d3a-78d288562ebe | -3.03192 | -54.08685 | 2024-11-07 05:52:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6f8c88d7-4462-3c42-95af-ec94c8ae1603 | -3.70703 | -49.00237 | 2024-11-07 05:52:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 46ec1a32-3797-3fa7-b16b-2cf3576cc49a | -3.5982 | -50.22245 | 2024-11-07 05:52:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 1faafe90-95a7-3815-973e-ce9ba97fa5ad | -2.95433 | -48.58315 | 2024-11-07 05:52:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 7d53cf49-ea3b-3609-9efb-64fdd6913d8a | -2.84886 | -48.67507 | 2024-11-07 05:52:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| b323f9f5-8ecc-3312-a5ec-9512f95eab42 | -1.56063 | -52.26262 | 2024-11-07 05:52:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ffabf731-092d-3a6c-a723-9bd4327d056b | -2.78111 | -52.87504 | 2024-11-07 05:52:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 30c44afd-a466-38f3-b2d4-2df7f1e7b5e7 | -3.58518 | -50.24299 | 2024-11-07 05:52:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 541101be-a015-3563-af6f-886bddda46ee | -2.28187 | -53.79826 | 2024-11-07 05:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 09570ee9-6069-3d9f-92f0-5029e98bf577 | -5.98635 | -45.35276 | 2024-11-07 05:52:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 201.0 |
| 46fb3095-0f8f-322d-9430-b000aeaca090 | -3.01918 | -53.44003 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 01cfc723-2aef-3f6b-918a-b34aa93d5ac4 | -3.74414 | -50.06694 | 2024-11-07 05:52:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c97fa2a4-f456-369c-ad2c-8ab68376523e | -5.03147 | -46.83451 | 2024-11-07 05:52:00 | AQUA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 97930495-d13a-3492-bb59-381b82350649 | -3.25583 | -53.40361 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3b3176de-f016-301d-8313-bde097fe9bf1 | -3.04429 | -53.27265 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 90a05fbf-310a-31db-8267-663ee33f853f | -2.8236 | -52.95301 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 19065e0c-73ea-3b25-aa27-30b9b463afc5 | -2.7286 | -54.14415 | 2024-11-07 05:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 93e333f7-6c16-3b0b-82a5-6e949b969e6c | -3.24776 | -50.46091 | 2024-11-07 05:52:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 4882803b-3371-369c-b784-9905774c3b76 | -1.06452 | -53.66189 | 2024-11-07 05:52:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9381c6d0-695e-3471-a7c3-506935df5c54 | -4.08941 | -51.01208 | 2024-11-07 05:52:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 8487d6de-c6d0-36ee-bfbc-276321cb3c15 | -2.8508 | -48.6614 | 2024-11-07 05:52:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 04f5fd1d-4d4d-3238-b2cd-14251143c6ef | -3.21827 | -50.29888 | 2024-11-07 05:52:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c855ef09-d13c-33f1-acf8-87373a6dd6f5 | -1.19681 | -53.88872 | 2024-11-07 05:52:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 730f0d92-9091-3ec4-af86-8696099583f5 | -5.0295 | -46.83931 | 2024-11-07 05:52:00 | AQUA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 35fa6130-a42c-3ffb-8365-7f833e17b9b2 | -2.83901 | -52.91039 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5c76163f-4fec-37cd-a32b-50a295d42c2d | -1.39324 | -52.20787 | 2024-11-07 05:52:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0b05eb5a-7518-3076-9981-a076de65ab9f | -8.3094 | -43.61994 | 2024-11-07 05:52:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| e088cefb-fd24-3cfc-85ba-1eaad4769fd0 | -3.22693 | -53.10514 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7a9d9b0c-8d1f-3caf-8d37-d68afab3024e | -3.01165 | -53.42989 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 439444a0-a66c-36c3-ae72-07e5c6f0e981 | -2.95003 | -48.59125 | 2024-11-07 05:52:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 81243200-0dd8-33b9-afb6-5fe188708035 | -2.82229 | -52.96179 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| a6039513-8c20-3e8f-aa59-61c5b88e24c8 | -1.19545 | -53.89779 | 2024-11-07 05:52:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| e43cebc3-a81d-33fa-a45d-41afbdf2807d | -3.1172 | -51.29152 | 2024-11-07 05:52:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6fa3b87c-39e2-373a-b967-d2a1210f786f | -5.98262 | -45.38099 | 2024-11-07 05:52:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| fd701d8c-5390-3ec6-996f-94d01870c0c9 | -1.39456 | -52.19904 | 2024-11-07 05:52:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 33ab1723-0bca-3dfc-b487-ba7d9d4271f9 | -3.22657 | -50.37652 | 2024-11-07 05:52:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 4dde5446-ca1c-3c94-8ce7-35a620dddd83 | -4.04784 | -49.2621 | 2024-11-07 05:52:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b9abc669-9c64-3f52-b1d0-52500da4bd90 | -3.18577 | -50.58511 | 2024-11-07 05:52:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a224ea35-fb72-330f-bc27-6093710838c7 | -2.76511 | -53.22278 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 8aaddee8-9b23-39e9-92af-2af52cb21d46 | -2.82492 | -52.94423 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| ee176f71-927f-30e6-8713-8675080c549b | -2.58409 | -53.99903 | 2024-11-07 05:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e5c59e95-bb58-3bf4-80f4-a3ab8a270982 | -2.78994 | -52.87632 | 2024-11-07 05:52:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8c549257-2519-39c1-8c4c-a68042901037 | -2.84901 | -49.81973 | 2024-11-07 05:52:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0c4a19cd-bae0-351c-9cd6-7a006a83a1b7 | -1.28088 | -54.13331 | 2024-11-07 05:52:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2f26f229-5864-3150-bae0-484e04fad817 | -2.21018 | -53.72606 | 2024-11-07 05:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 3f20e145-25e0-34a2-ac29-c5cd1ccc55b2 | -2.21153 | -53.71711 | 2024-11-07 05:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 3e87ce14-f247-3300-9b48-546d1b20a6d3 | -3.64399 | -51.78922 | 2024-11-07 05:52:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f40cf42f-10ed-3f5f-9c16-ccc0f960faed | -2.85972 | -48.67657 | 2024-11-07 05:52:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 1bd6eaba-d9c8-311b-b62f-7123001bd5c4 | -3.0142 | -53.23233 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b8f0fd32-0d17-38e7-aec8-84b98df97ce3 | -4.05193 | -49.26953 | 2024-11-07 05:52:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 9730e4e3-b5d4-3a30-9117-611327f1701e | -2.1763 | -53.69711 | 2024-11-07 05:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a387a986-f98f-3d72-a72d-0663eb699524 | -2.24502 | -53.67625 | 2024-11-07 05:52:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 48e70a5e-588b-3dc4-b76f-6d6cac0dfe9d | -3.59659 | -50.23344 | 2024-11-07 05:52:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 298.8 |
| fd5fe851-c548-3d96-a991-e6d9000e926e | -2.61885 | -51.29907 | 2024-11-07 05:52:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 71b50303-891c-3af9-acea-89535ae36b60 | -3.23964 | -50.44905 | 2024-11-07 05:52:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| dd5406e3-438a-33cc-b81a-e4cdcdcd6a25 | -3.03545 | -53.27136 | 2024-11-07 05:52:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |


[Clique aqui para ver as próximas entradas](README54.md)
