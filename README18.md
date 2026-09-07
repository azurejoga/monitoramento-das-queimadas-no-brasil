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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd42b8de-c25e-38bd-a4a7-f52d9cd449ab | -3.41347 | -54.7734 | 2026-09-07 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4faaa435-a779-3526-b4a1-48663e511279 | -3.13624 | -60.63652 | 2026-09-07 05:01:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e9e3725a-090a-3232-90f7-93fc2de8441b | -3.79705 | -55.87881 | 2026-09-07 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76deb249-2875-3621-b4e6-90d9ce0bfe79 | -2.62825 | -46.77525 | 2026-09-07 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3faf92ba-6a20-350d-899e-ae8f32b2c5b6 | -3.14775 | -60.66397 | 2026-09-07 05:01:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b67a4c85-2322-3687-b482-fb08cca87ff2 | -2.71308 | -59.76713 | 2026-09-07 05:01:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba854a63-0111-3b36-a941-f7b371f3afb0 | -3.14723 | -60.66712 | 2026-09-07 05:01:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 51ce3062-5477-3bc4-b797-2a4f37b31888 | -3.14253 | -60.66311 | 2026-09-07 05:01:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| f73e6492-83bf-326f-b1df-f1f452c721e8 | -4.08003 | -48.95203 | 2026-09-07 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| eb60baf3-ee45-3042-bf41-468ab06a66ce | -1.62184 | -55.16846 | 2026-09-07 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13452a44-adeb-3a34-a33c-176e73076c4c | -4.02978 | -52.06896 | 2026-09-07 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7c6c5df-f728-3a34-99f3-176815e5cc9d | -1.20457 | -55.72045 | 2026-09-07 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a5f51eb0-68c9-3edd-b75e-7e9aeec40bbb | -4.032 | -52.07639 | 2026-09-07 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0dc50762-cf6c-32fc-8834-a6f3b1315e41 | -3.62785 | -54.60646 | 2026-09-07 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f89d355-8847-3d30-8dab-8d74fbe3a134 | -3.67581 | -48.91362 | 2026-09-07 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ce69f0b-8b8d-34cd-9128-b01d61f2d140 | -3.42236 | -59.64818 | 2026-09-07 05:01:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 20d81ae2-5ccb-332f-a5cb-8913bdfbea6a | -2.0242 | -52.1068 | 2026-09-07 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad07d347-ba0a-3c6b-8b2a-c0763c8ba890 | -3.06024 | -51.25023 | 2026-09-07 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad9714db-876c-3e05-9fe8-f8574c219413 | -2.62726 | -59.39778 | 2026-09-07 05:01:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5311819b-64ad-37fb-bd92-15cd226129e3 | -4.35159 | -48.97759 | 2026-09-07 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 22fb981b-0180-3fc1-b098-6b3c0ee01f0a | -2.86093 | -50.45941 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2f562d6-64f4-3298-a5eb-47b53fbc14f1 | -1.49511 | -54.81834 | 2026-09-07 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96adf7a0-8276-344f-8464-2388212c0c4c | -3.7858 | -55.87701 | 2026-09-07 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e75c6cfc-88a3-3972-a8f7-a0c34e959b75 | -1.49376 | -54.82679 | 2026-09-07 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35604dc1-c4c0-37d7-b88a-6f15661f24c0 | -4.2152 | -48.56006 | 2026-09-07 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75f76004-4d06-3854-b035-7c2daf69dbd5 | -2.6323 | -46.77585 | 2026-09-07 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 86fbcba6-b6e2-3dd1-92dc-d2a6731f9eeb | -4.11187 | -49.05944 | 2026-09-07 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7113f44c-b750-3b7f-a34a-f89548dd8242 | -1.86277 | -47.98103 | 2026-09-07 05:01:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 532b7bbb-ce79-39a8-bfe2-4ee313d44244 | -3.80988 | -55.89476 | 2026-09-07 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d9c0aa1-513f-33e9-bbb9-61a6451084dd | -2.45341 | -57.91298 | 2026-09-07 05:01:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd79437c-8bed-36a2-9298-167609c56d4e | -2.30329 | -48.58823 | 2026-09-07 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 496eae03-922c-3544-bf96-9774e946e007 | -2.73649 | -58.1889 | 2026-09-07 05:01:00 | NPP-375D | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa2ae066-455b-3d03-85c0-babe96f5756b | -2.55884 | -54.74519 | 2026-09-07 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d35bee27-7da1-3448-acbf-73fb8a9540d5 | -1.90093 | -58.24434 | 2026-09-07 05:01:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2e6460f-7226-3a5e-a52c-e489a7bf524a | -2.55705 | -59.444 | 2026-09-07 05:01:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 00dcedcd-9e89-3b47-a508-eaec153e330b | -3.14196 | -60.63423 | 2026-09-07 05:01:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0f2e848-6b09-3573-80ea-c13b75384a16 | -3.38166 | -59.41944 | 2026-09-07 05:01:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 791f4c82-b802-34ba-b31b-df32bb9507f7 | -4.3486 | -48.97285 | 2026-09-07 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc272482-4c6b-38ba-b3ea-9c68b912ceaf | -3.5752 | -55.59777 | 2026-09-07 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a64d6ab-cb37-33d8-ba9c-4bde06f3314a | -3.37212 | -59.41788 | 2026-09-07 05:01:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69ec974a-45d6-3b81-ad1c-3cca1a674e74 | -4.10825 | -49.05889 | 2026-09-07 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e463049-ef3a-307c-9d24-d1076bd0b801 | -2.8694 | -50.4497 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 079e653d-e54c-36b1-89d6-312b4560d741 | -2.0884 | -49.53246 | 2026-09-07 05:01:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f7f98bc-28f1-3129-aaa3-55444d961f39 | 0.21491 | -51.28749 | 2026-09-07 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a8d3f4f-3ad6-3af7-abc0-2f223387f7cc | -3.49347 | -50.60867 | 2026-09-07 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb399fc6-1a5c-3919-bc3c-348418d209d7 | -2.82 | -46.71225 | 2026-09-07 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bf02995-f3c1-371c-85a9-a968aed23ecb | -4.03623 | -50.87094 | 2026-09-07 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5083c50f-3976-3d96-aa89-bd07631add68 | -4.12805 | -54.41391 | 2026-09-07 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f277f292-fd13-38c9-9c3b-4c0cff6770f1 | -3.38083 | -59.42455 | 2026-09-07 05:01:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b01d2e1e-74d0-368b-a2b8-4b0c68fb0022 | -1.20304 | -55.72998 | 2026-09-07 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4943e4b2-3f46-38f1-adef-7397ebd9bc9e | -3.62176 | -54.60262 | 2026-09-07 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76e4473e-432f-38f6-8b9d-a5a2065b3acd | -4.34795 | -48.97704 | 2026-09-07 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 38e9fb23-ed4a-3f32-9cbb-8b3edb561cd8 | -2.63636 | -46.77647 | 2026-09-07 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 97a3a201-56e6-3c40-acd7-b433e166e3b2 | -2.30094 | -48.57935 | 2026-09-07 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33efc194-b8bf-3924-8401-5516539f5b42 | -1.56572 | -55.24801 | 2026-09-07 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4feb8f23-2474-3264-b761-bb0779587027 | -3.36667 | -59.51202 | 2026-09-07 05:01:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13790b06-3cd7-3097-807d-07dae00a0be1 | -4.3786 | -44.392 | 2026-09-07 05:01:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 48481da1-ef7b-31e2-bf19-54f2d8efac63 | -2.63745 | -46.76942 | 2026-09-07 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| c6d1bc1d-925b-30d4-a740-98dbf59b9486 | -4.5935 | -50.98664 | 2026-09-07 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a66a3295-9651-3dec-99a0-7e07be5daaf9 | -2.86773 | -50.43839 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f6f30b0-7f64-3188-bf8a-09de8b0e09b4 | 2.51724 | -51.29016 | 2026-09-07 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 67015598-92c0-363f-a943-6fd5ad8c6da4 | -4.04241 | -50.87556 | 2026-09-07 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 478f9f78-9470-3adc-b85b-85d5a137dace | -4.59461 | -50.97954 | 2026-09-07 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71a63452-2470-39a9-a245-1918c23b1df2 | -2.87723 | -50.4505 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf478253-f181-3ff6-8b74-f6e62ecaad53 | -2.86545 | -50.45276 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fb84261-e0e3-3be6-9beb-710c8469243f | -2.96022 | -48.70182 | 2026-09-07 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e0b7d5a-e5d7-379a-866e-1223c08a768b | -2.87165 | -50.45741 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9277b5a6-acf7-33f9-916b-6e0bcd4c4a24 | -2.87222 | -50.45382 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01d6e93e-b555-3b8f-8ce2-0b50e7971a06 | -2.87835 | -50.4433 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 3db3cfde-c71a-3cd5-b3a7-690caebba4fc | -4.51858 | -46.40866 | 2026-09-07 05:01:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79ea6c03-b0e3-339e-afaf-7ecf82b94297 | -4.03848 | -50.8786 | 2026-09-07 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1902c600-de94-34ef-9632-454cec1edddf | -3.26815 | -57.87529 | 2026-09-07 05:01:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 318f944c-f780-3841-abd0-0ef2a9eb1e63 | -3.50023 | -50.60973 | 2026-09-07 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51968f48-3d32-3316-812d-4dde64af3afb | -3.81261 | -52.35322 | 2026-09-07 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69252f25-3730-3fa7-a9e1-8ede45c26604 | 0.21768 | -51.28354 | 2026-09-07 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cb38a60-0d67-31aa-b7ae-295f9abda5e5 | -4.104 | -49.06249 | 2026-09-07 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a777c98-66a4-32ef-bffa-68fa4a194e99 | -4.12457 | -54.41341 | 2026-09-07 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2e87d05-e1f6-3bc7-b4c7-2536676eecf6 | 0.21878 | -51.29042 | 2026-09-07 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a90d57e6-54b1-3f9f-bf11-5d6807220dd8 | -3.34063 | -53.40508 | 2026-09-07 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d63e9a37-9267-3b26-bfc1-ab9364779535 | -2.86997 | -50.44611 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6216d836-0309-3185-800f-8096c0c55567 | -2.88342 | -50.43304 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5a534654-4181-3099-9ba1-0aa7a51b189e | -2.87919 | -50.34412 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aedeada0-dae4-3d86-8afa-3b4fd147bb43 | -4.21824 | -48.56501 | 2026-09-07 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 45c9e3d1-45bf-3346-9f5d-ae79e68ed808 | -2.87903 | -50.43278 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7946bc46-1307-366e-beae-7945537855e4 | 1.95022 | -50.87371 | 2026-09-07 05:01:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d5cf7e8-5b70-3f22-8bd9-93101a393156 | -4.11527 | -49.08537 | 2026-09-07 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e5670d57-01b1-312b-9bce-e18ff661b906 | -1.86766 | -47.98025 | 2026-09-07 05:01:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24abe8d4-8d42-386e-92ff-b91c58e89049 | 0.58652 | -54.21244 | 2026-09-07 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 616154f7-1443-3e12-87fe-5983899bb1f8 | -2.87976 | -50.3405 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39dbdd44-cfcf-3d9c-8f37-3b774839644c | -3.08893 | -61.06981 | 2026-09-07 05:01:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cb71f00-b9c4-3a2c-97e5-51182181eb11 | -1.63256 | -55.12549 | 2026-09-07 05:01:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64a53bd0-e591-373c-a3a7-6279945a59be | -3.38725 | -59.4151 | 2026-09-07 05:01:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bbe3bd2f-d222-3e2d-841f-80de21070a43 | -2.87891 | -50.4397 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| e2ef0cf2-4069-3099-87db-3c700b9c3bd6 | -3.15622 | -50.82657 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98238bb2-a998-3314-88f1-69ac48f7328f | -2.86488 | -50.45635 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c49819a-8981-3d83-be1b-fe1b9e7940d7 | -1.2374 | -54.10446 | 2026-09-07 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2863fe88-9147-3274-b937-daa61d754d4b | -2.87054 | -50.44252 | 2026-09-07 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45de06b5-693d-357e-a811-efcdaadbd441 | 0.21437 | -51.28405 | 2026-09-07 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdbe90cf-8421-329a-b371-52d91d197278 | -3.33725 | -53.40454 | 2026-09-07 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97f264c5-98cd-3846-87eb-0af0b9b7e284 | -4.03255 | -52.07294 | 2026-09-07 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README19.md)
