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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0254128-2257-3157-84fe-1a639f3f26fa | -3.15714 | -50.43967 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5a02200e-5047-369e-ab6b-59da1afceff0 | -3.15606 | -50.44648 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cfde09dd-c841-3d8e-8c56-efaa30b0c29d | -3.15314 | -50.439 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c76ec3ac-bbe3-38ce-aed8-c99a143ad12e | -3.15205 | -50.44583 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| eeac0a36-eb84-3756-af79-35c1f0740a9b | -3.14914 | -50.43831 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 34008c93-1de3-3137-ae93-6a0977b87397 | -3.14748 | -50.44868 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2e1037d8-9ba2-33ba-82e9-6600349dd0c4 | -3.14458 | -50.44109 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7f1bc385-b43f-34ab-91a9-418086a45b9b | -3.14003 | -50.44389 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3ff40759-a8a2-3aad-9446-67c4962a6abb | -3.13878 | -50.42599 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d4153783-f550-3208-b125-c4cdaaad8bd1 | -3.13424 | -50.42871 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 70bcec3d-c680-3a06-9f9a-18145a721b78 | -3.09473 | -50.22588 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d9486c6-2257-326d-85c6-e72cee513b1e | -3.09393 | -50.23093 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b0dc3b9-86da-3e67-b0de-0202ef8ae0df | -3.02501 | -49.56033 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b668f15a-b515-3a26-bbb6-a34d043249e9 | -2.98705 | -49.53245 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b76d0483-d688-31cf-95b9-2b5957f46632 | -2.98703 | -49.53046 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1d243b98-4879-348f-a732-a024ccdec114 | -2.95884 | -49.20207 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f906e697-90e8-3d7d-93ca-38e9254a9bb1 | -2.91698 | -50.48329 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ef3ebe7-85f6-35f1-a749-1b6f24222608 | -2.90238 | -50.39434 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ad2e1b9-90b8-3dca-9219-0b192de3bd53 | -2.90182 | -50.39782 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7bdcbe03-23da-3c19-8ff6-12bf9986b234 | -2.89781 | -50.39717 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 209b13d0-b0f7-31c1-9555-d7fbca4f60c2 | -2.89724 | -50.40067 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0d65ea3-bba2-354f-a048-8c25950f449b | -2.89436 | -50.39304 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84809862-66d7-3a65-afc7-173b413f0cf9 | -2.84251 | -49.86971 | 2024-10-11 04:23:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01fb7f0b-0701-37f2-90de-f93ad9964f96 | -2.83304 | -49.52534 | 2024-10-11 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ae6fd12c-9d8c-3978-b9ea-9d273382e013 | -2.8323 | -49.52997 | 2024-10-11 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dbb90f66-75ab-3d6b-816c-bd6ccb9cf6eb | -2.8285 | -49.52937 | 2024-10-11 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 39b63eda-c39a-36d8-8d9e-8b8035ab8535 | -2.77441 | -49.23668 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b62c7eb-fb32-3ab8-9374-6f35ae5b9a4a | -2.77067 | -49.2361 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54dd7b6b-2ee1-3d55-bd08-f2c12b6a0eec | -2.75431 | -49.53391 | 2024-10-11 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ca328b6-76a2-3c52-8bf5-959908dc377e | -2.74141 | -49.54141 | 2024-10-11 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af93d46f-f9f8-3ae7-8875-746daf8a7942 | -2.7376 | -49.5408 | 2024-10-11 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| f662eb21-1066-30d4-8a41-a2ff7fcebf34 | -2.73379 | -49.54018 | 2024-10-11 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 3db0eb37-492f-3c6d-8562-2d570c1d0198 | -2.72468 | -49.54832 | 2024-10-11 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dceeb2e1-62df-3e15-a5f0-483061be6569 | -2.72236 | -49.53833 | 2024-10-11 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7f50f38-a2aa-3442-8a75-2bdb70221dd4 | -2.7107 | -49.44123 | 2024-10-11 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4b656ced-3872-3b64-91c7-37493dfbe159 | -2.61987 | -49.08321 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 878d52bb-d0cd-35d1-99f0-efd0865dee8c | -2.61389 | -49.78728 | 2024-10-11 04:23:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4a3842a3-6f62-32d1-a2d1-b22a01e8c392 | -2.5961 | -49.79929 | 2024-10-11 04:23:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c042ca5-d2b2-3d5a-aacb-757e239a855d | -2.59222 | -49.79867 | 2024-10-11 04:23:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42da56ca-dfc5-3f6e-94d3-ad35b1b60f55 | -2.57157 | -49.07551 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d00667e0-5c1b-3fb9-bfbd-a398bad95887 | -2.53345 | -49.71989 | 2024-10-11 04:23:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6e6d5fad-0c45-382d-babe-75a3d63afcc9 | -2.53226 | -49.71711 | 2024-10-11 04:23:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb3f2215-a68f-3ee3-81ad-b6411d03dd94 | -2.53184 | -49.026 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 401b82fe-fa10-3bf0-b73d-1ce68f88868c | -2.47249 | -50.24336 | 2024-10-11 04:23:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53c511a1-8d9a-3c16-bbd0-807d951971eb | -2.47193 | -50.24682 | 2024-10-11 04:23:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fa111143-5233-3243-bc86-4c0a7544afd3 | -2.46569 | -50.26004 | 2024-10-11 04:23:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7bbd132f-39a7-391c-abf5-9ae49aedadf9 | -2.46513 | -50.2635 | 2024-10-11 04:23:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 911f58c1-3ce7-3059-a1ba-ea76e708107f | -2.46169 | -50.25938 | 2024-10-11 04:23:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6cc0b349-6548-3125-8215-ce9ec032ace3 | -2.3904 | -50.41321 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10f32e71-810a-3862-ba93-9e6275d31f94 | -2.38636 | -50.41255 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99591ef2-bb56-361c-811b-2f85779c0365 | -2.3797 | -50.32451 | 2024-10-11 04:23:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39ac58b9-0580-3912-bfbf-6d9147c2bbfa | -2.37568 | -50.32387 | 2024-10-11 04:23:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cef726a4-f2e1-3ebc-8448-ad25a48181a5 | -2.37512 | -50.32738 | 2024-10-11 04:23:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f5450cf3-abc0-3ed9-afe2-4de1a3bd704b | -2.60228 | -48.95438 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2f75860-c14d-3949-920e-9b3b89b8a3e5 | -2.57717 | -48.94588 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e025912-906f-3331-ada0-3b2beedef261 | -2.57529 | -49.0761 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbe07e54-e754-3c03-beaa-8d636c432e4c | -2.39751 | -48.94818 | 2024-10-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d12d087b-81e8-352a-8d4e-613d6685d4ed | -4.43284 | -50.54644 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6607c579-236a-3818-ad9f-1239add932fa | -4.38933 | -49.82677 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33e9f90e-3e9d-31fe-8adc-b52103a92ed0 | -4.38553 | -49.82619 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2640d86f-12be-3920-8118-22b0a8a037f0 | -4.38478 | -49.83083 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef8d96ee-1d95-34ce-8d45-0784da677925 | -4.3825 | -49.821 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fd135911-b66b-327c-aa1c-5a24134a5b43 | -4.38174 | -49.82563 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 12617928-a2ee-3559-847b-8f8100b019b9 | -4.34639 | -50.50998 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7154e721-52d3-3a0e-9532-cf93b38c2e2a | -4.34522 | -50.51126 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d90a26d-37df-3643-a6ea-d4d265d2df0d | -4.34244 | -50.50932 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ef927820-7b82-3013-a988-b4de04c8fdce | -4.34127 | -50.5106 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19776122-8f2a-3c99-a7f3-c9754e3d8bd6 | -4.16947 | -49.77151 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4e3553c3-4375-354e-8848-cee92681637c | -4.14065 | -50.41502 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b9ea9d3-af79-313b-9a4c-5d3234c65c74 | -4.04091 | -50.38658 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50f56285-ec05-3dee-9834-52ecabf0023e | -4.04067 | -50.38329 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e887d94-f79c-345c-a60d-93795132af26 | -3.93098 | -49.66457 | 2024-10-11 04:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| daadcee1-5979-3c2b-9f98-3423593f8550 | -3.93028 | -49.66899 | 2024-10-11 04:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb4b9dc4-001b-3f75-956a-1c2e425f9f95 | -3.92957 | -49.67344 | 2024-10-11 04:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8cd6882-79eb-3d7e-bca9-f6ec12c05fe7 | -3.92792 | -49.65948 | 2024-10-11 04:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49d3a40d-990b-3f1e-b678-1a7770769484 | -3.9272 | -49.66397 | 2024-10-11 04:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b69a3bbc-40ed-31ff-86e2-cf2a9e68a277 | -3.9265 | -49.6684 | 2024-10-11 04:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88217f36-c643-35a3-8834-eebb76fe9510 | -3.92579 | -49.67285 | 2024-10-11 04:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc074181-cf15-3afa-83e2-92939975b3f7 | -3.92271 | -49.66786 | 2024-10-11 04:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f62ede1a-f3e5-31be-907c-8a9f68c56ce1 | -3.91914 | -49.6902 | 2024-10-11 04:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5596364-f569-304d-bad4-14c60bfc95ee | -3.91463 | -49.69415 | 2024-10-11 04:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aba5c32a-8139-3be7-b286-0ea731c688e4 | -3.91084 | -49.69355 | 2024-10-11 04:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dbc4d4cd-b2a6-300f-909c-fe2c657581b0 | -3.90705 | -49.69299 | 2024-10-11 04:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a7505352-656b-324e-8001-e919176e72eb | -3.75929 | -49.79085 | 2024-10-11 04:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2956704a-6a39-34ba-9510-beefc71021f1 | -3.68937 | -50.12399 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3d30e776-5538-3a1a-b9d2-a76642d93911 | -3.68627 | -50.1185 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2f124d13-62c4-3fa6-b04d-56176a87ba32 | -3.68236 | -50.11794 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8c20699b-90cc-3076-9c4c-8f12b8fb191b | -3.68156 | -50.12284 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 220b92aa-6ecf-34bb-8df3-d594d094d7eb | -3.65745 | -49.62981 | 2024-10-11 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5583b0ad-860c-370b-84a5-6bcbd22ce82a | -4.95011 | -49.76611 | 2024-10-11 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26d0b8b0-2c2d-3d3b-b02f-1466fa555b6d | -4.94636 | -49.76551 | 2024-10-11 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d156264a-ca02-3e6a-b219-90b749641ac4 | -4.90662 | -49.8665 | 2024-10-11 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0dd046c-261d-31a9-82c0-b49504074369 | -4.88697 | -49.91496 | 2024-10-11 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 889abed1-b76d-3c8e-b07f-e039a5e1f956 | -4.88668 | -49.91693 | 2024-10-11 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93a2488c-e5eb-3e0c-858a-54b528570f2d | -4.88621 | -49.91956 | 2024-10-11 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6eeadb3-86e3-3530-ad59-37fdbbe109f1 | -4.88318 | -49.91438 | 2024-10-11 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef97aa22-5cbf-3836-aeb7-160642e8fdf8 | -4.88289 | -49.91635 | 2024-10-11 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76f20a8c-0a9d-3660-b103-e09922ddbab2 | -4.8794 | -49.91381 | 2024-10-11 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25ad41cd-4fee-3494-8bff-bcce5c430939 | -4.8791 | -49.91577 | 2024-10-11 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a02b2a6-fd92-3090-b1c8-ab17bada63e0 | -4.84504 | -49.88634 | 2024-10-11 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README48.md)
