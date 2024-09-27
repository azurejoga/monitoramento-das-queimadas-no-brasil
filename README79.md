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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a0e8151-f3e5-3d8b-876f-b8ac24efad0d | -8.67753 | -54.81046 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ad47f6e-486f-3f55-b12d-279b214a09ed | -9.4668 | -53.58847 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab3983a7-76f4-33e3-897b-541015f8f7bd | -9.46315 | -53.58785 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 212456ce-691e-3141-ad51-feea63ab470e | -9.45413 | -53.57465 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f153345-7444-3248-80f5-6becf1a6b11f | -8.61926 | -53.64726 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e3529ec-19de-3878-b6ef-122a4402640a | -8.61851 | -53.65173 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9a6e0bc-9e48-38be-bbbd-c044c1521f32 | -8.61109 | -53.6505 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9bfff40-035d-3328-b04c-47686d4ac008 | -8.58088 | -53.33673 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6424fd46-16a5-3a5e-b3ac-809201d9be1a | -8.57803 | -53.35395 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de46fd1e-33e4-3dc4-8db2-576b582e95ce | -8.57724 | -53.33607 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4ca03290-4182-3679-8faf-9c1e42ed9881 | -8.57511 | -53.34897 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36f267c2-2653-3cdb-8beb-13335560b876 | -8.57437 | -53.3534 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9214f644-4f23-33d9-bed3-6159c4af223b | -8.57219 | -53.34394 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| db7c7fe1-1761-313a-8384-4a61384af3f6 | -8.57146 | -53.34835 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| df7f4a4a-128d-3eaf-b74f-ad9781c86f1e | -10.46897 | -54.21671 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b55191a-91db-3a1a-b4a6-bd5765f41ff5 | -10.4682 | -54.22126 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00f0f2aa-8dd6-3192-bdde-e13b1d9db4e6 | -10.46709 | -53.83014 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1c60572-6f3a-34ea-99df-e4860448f001 | -10.46637 | -53.83445 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4abc7556-4697-3368-8b06-5da1258ba690 | -10.43348 | -53.69594 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8e7f754-911b-3e7b-b2f3-9a296247e291 | -10.41604 | -53.71063 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5ccdef3-8b12-35cc-9d91-036206bec820 | -10.4159 | -53.70773 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c328f10-d0c4-37fe-b1e3-c91769f51e7d | -10.41457 | -53.71926 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| de4da158-5feb-35f2-8898-78c1c0d6c547 | -10.41226 | -53.70713 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aef4c70a-becb-362e-92b1-2c6d89c047d5 | -10.41096 | -53.6966 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f2622dc9-5d36-32e0-8436-cffc57e7cb60 | -10.41074 | -53.6937 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d6e48210-ea5c-3b9f-9bc7-8bf96557c703 | -10.41004 | -53.69797 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ce3bdce-6462-389c-bdaa-37e959436077 | -10.4095 | -53.70515 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5028ff35-1cca-34ff-ab6d-6522e0a0324d | -10.40933 | -53.70225 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25163514-ebf0-37cb-b0d6-35b5e4e0fcfa | -10.40862 | -53.70654 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 394f0622-6841-380d-abce-bd5b52e580d2 | -10.40656 | -53.72234 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b06745c4-1562-3f5c-8c7f-9b8d33791a9e | -10.40578 | -53.72376 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 450373a2-6378-3614-a335-0c6594df859d | -10.39196 | -53.71692 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7aac220-6cc3-3e2c-9d26-865d2d4cb1c2 | -10.38903 | -53.71202 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30a37c41-9c0b-330f-aa15-b7656c8cd320 | -10.38832 | -53.7163 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60730957-5030-3fa8-a3cd-164a7c67780a | -10.38317 | -53.70229 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6cd5771-e0a9-33dd-9216-bea57c2bc25f | -10.37609 | -53.76743 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c64d6ac-4a55-3e1a-9830-ab1d840c5c9b | -10.37537 | -53.77173 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b15572b3-5f5b-30f7-87a3-c89c9dc9b55a | -10.37465 | -53.77604 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 095d4770-2c1c-3a92-ac9f-774c6c9e6c81 | -10.37394 | -53.78036 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d3a26cf5-cba3-378f-88ee-183480bd0f7c | -10.3725 | -53.78901 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 86c23291-8a4b-3a41-830f-c1b215f6be06 | -10.37178 | -53.79333 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 08db1b0c-b3d9-39f9-8269-17ed389c44ab | -10.37101 | -53.77541 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d42176ac-fa11-3cc3-ba78-246f1bc8fe74 | -10.37029 | -53.77972 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 28c57a9a-a1ec-3675-b376-c8e24d536a5d | -10.36957 | -53.78407 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f5fa4cb2-dd60-366b-af59-7f1eef8afd05 | -10.36884 | -53.7884 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b585e9fb-741f-3ade-bca1-d5741bc64a27 | -10.36812 | -53.79272 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 60cf74cb-8229-3706-9cee-bfe7326893b1 | -10.36736 | -53.7748 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ac7a45a-6e38-3e1e-9dec-f157e00b8aa1 | -10.36664 | -53.77913 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 79cb47bf-c2d5-3795-8e6e-f39621d3c249 | -10.36591 | -53.78346 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d21529b0-ca10-3c0a-b977-294c42abd4ff | -10.36519 | -53.78779 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| aa3ef9b7-bc1c-3392-a01d-636b1fac85e2 | -10.36447 | -53.79212 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| af6a1b2b-a643-392d-b9c6-9ca6cf9654ca | -10.36298 | -53.77854 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 517d9cf2-388e-3808-8375-2eea7d5f8f19 | -10.36226 | -53.78285 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f03b206c-7dcf-3b6c-80b7-643fbc29f0c5 | -10.36154 | -53.78717 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| fcab56a2-112a-348f-aa57-20d768db7138 | -10.36081 | -53.79152 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 54f40f95-24cf-33b3-8378-0a832a19adf3 | -10.35933 | -53.77795 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ecbf7ff-4110-383b-a9aa-abebe96a69a2 | -10.35861 | -53.78226 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 429ca357-cf2a-3e46-a941-9200903562f1 | -10.35857 | -53.76005 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cad362db-1697-35b0-a6ca-2e3e4522e46b | -10.35789 | -53.78658 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4fe8ada8-4800-3648-b97a-650aa8a13a7d | -10.35492 | -53.75943 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8ff387c-1b37-3f83-8b4d-a6b7fd45cbf9 | -10.35128 | -53.7588 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 408f1d82-5d64-3bde-abb2-20e110893dc6 | -10.35056 | -53.7631 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce34a7b3-5fba-3435-9c67-61c29f980247 | -10.23736 | -53.96955 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4975840-0583-3e97-bba0-4aa166c1ee97 | -10.23053 | -54.12536 | 2024-09-27 04:40:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 166ad635-8f78-338b-b0b3-b15047cd7d25 | -10.22853 | -54.12402 | 2024-09-27 04:40:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 97f61200-1bc6-39a8-b314-8b6396e0178c | -10.22756 | -54.12017 | 2024-09-27 04:40:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 404c280d-56c2-3cf3-b64a-68354c2ed5fc | -10.22681 | -54.12473 | 2024-09-27 04:40:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 731c5644-1e60-35be-a681-a25c78f6809b | -10.22459 | -54.11499 | 2024-09-27 04:40:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 314ad913-cad8-38fd-ac10-929fc6002b73 | -10.22383 | -54.11955 | 2024-09-27 04:40:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cbe86fd2-f55d-36c1-ab34-c343b5e5019a | -10.22308 | -54.12411 | 2024-09-27 04:40:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7f6098ce-3365-3665-8321-fafa137b0403 | -10.20977 | -54.08914 | 2024-09-27 04:40:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a86c7cbe-29f1-3b19-bfde-cf8727ee9d4c | -10.20903 | -54.09356 | 2024-09-27 04:40:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23614a4b-249b-3093-a09d-82a07e45a7da | -10.11963 | -54.19057 | 2024-09-27 04:40:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 86c445aa-604d-392a-ad07-426c1aa84b1c | -10.11893 | -54.18785 | 2024-09-27 04:40:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a047ae5f-cb11-3398-a6d2-321540563e3a | -10.62406 | -54.83772 | 2024-09-27 04:40:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a552b2f3-a717-3303-b578-f79fb497acfd | -9.72731 | -53.60334 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1240ca87-7d3e-36d3-8ce4-87b03b4b0c07 | -9.66764 | -53.53207 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ad5df45-8bf1-3191-809a-632d197c8bea | -9.66694 | -53.53634 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95382987-c8cc-340c-b968-381811c6a64c | -9.66401 | -53.53148 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe1501a9-f285-3197-a6a1-5560ac5d5638 | -9.66331 | -53.53573 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da1b2f27-797b-319f-89e6-aed7cfc50387 | -9.66037 | -53.53085 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e775b874-0a9c-3dc8-acdd-2e495f56bdbf | -9.8184 | -54.10732 | 2024-09-27 04:40:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ccaf0315-1451-365e-a174-3ca6c236c041 | -9.81466 | -54.1067 | 2024-09-27 04:40:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1edaae19-3439-36da-ad8f-225417ae788a | -9.66678 | -54.24238 | 2024-09-27 04:40:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d4c6bf4-2a17-3277-a856-ddc430719c73 | -9.6665 | -54.24483 | 2024-09-27 04:40:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b55e0207-b48b-3223-a79b-3e5f8620f2b9 | -9.59473 | -54.25439 | 2024-09-27 04:40:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 075a9cb2-7fc3-3994-b5ff-91cd0580e98b | -9.59393 | -54.25909 | 2024-09-27 04:40:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96abad6d-761a-3dd7-8a43-116bcf4ff973 | -9.59093 | -54.25383 | 2024-09-27 04:40:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf022dbd-7b64-3939-9882-3e7ff6c2227a | -9.58754 | -54.20531 | 2024-09-27 04:40:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 13007aab-4797-39be-a1a3-e88c318b4cfb | -9.4642 | -54.56771 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15e057c7-b9f3-36e5-b7df-7effd482e91c | -9.46113 | -54.56232 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2143b25-0aec-37f8-a342-57dbd6f66580 | -10.62365 | -54.60915 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26784ca4-611c-36f8-99a6-58b56fd8b83d | -10.61983 | -54.60854 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 717557fe-cc42-3c87-a438-fe8ee0e3b87b | -10.38649 | -54.49651 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1a267bf-e954-39d1-bbea-513a6189b821 | -10.38634 | -54.49415 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cbd970d9-6ab5-3f1d-ae14-79887b0f51c3 | -10.1811 | -54.62539 | 2024-09-27 04:40:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2bc0c421-8eb7-3ff5-ba77-7acd39ec999b | -10.17726 | -54.62473 | 2024-09-27 04:40:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fe97d6b-cae6-332a-9014-3b738457f643 | -11.23994 | -54.78161 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 56b8276b-e204-303f-9cdb-76cc8aa52fcc | -11.23613 | -54.78092 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| abf3eb8c-d472-3d7d-bfd0-b19e19c72871 | -11.23233 | -54.78022 | 2024-09-27 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |


[Clique aqui para ver as próximas entradas](README80.md)
