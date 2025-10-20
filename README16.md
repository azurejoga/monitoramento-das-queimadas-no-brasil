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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39b5d882-2775-3d01-b35b-661ec37a40ed | 0.86112 | -51.12366 | 2025-10-20 05:01:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f5964d3-a402-3b10-8bd8-ed3455bfba4c | 1.78386 | -55.70216 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc7e2dfb-56df-3b10-9176-b1eeb743c4d6 | -2.87558 | -50.72247 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e5b207a-4bdd-33f2-aec0-2d9dd994f637 | -2.8732 | -50.71246 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3fa6f98-e6b2-362a-8c59-1d079391b901 | -2.56666 | -49.11439 | 2025-10-20 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77a54a99-bace-3d61-a57e-5ce2db04edba | -2.8763 | -50.71776 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bb3c8d4-e756-36ae-9620-af51b9b76d75 | -2.86887 | -50.74073 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 732ba148-ef1a-3960-ac87-dffef3955154 | 1.78442 | -55.7058 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 810e737b-f43e-3429-9568-b7c0acba777f | -2.25326 | -51.91502 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 8dc1e27d-dc8e-35db-a014-7f0d9b58077a | -2.66076 | -49.37552 | 2025-10-20 05:01:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe9961e6-0cdd-3039-a82e-679ba6f21a68 | -2.25451 | -51.90696 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 3bd6d557-689d-335a-a6fb-c3c9c5a72108 | 2.0203 | -55.73357 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94aaad21-b06a-3d75-baad-930e3fbab90e | -3.14723 | -49.51587 | 2025-10-20 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e1ca58f-901d-37e3-8492-73c6d338cd53 | 1.71769 | -55.95726 | 2025-10-20 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b8445b12-e861-3f84-b85d-6a778f0142ae | 1.08155 | -51.30339 | 2025-10-20 05:01:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bab01c30-e565-3f32-a658-310e3cf01163 | -2.96972 | -49.22775 | 2025-10-20 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8221d8ec-60de-33e3-830a-9f8e69324187 | -2.86815 | -50.74543 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87791f51-dcb9-3ded-a9a8-ea95e2d44647 | 1.74818 | -55.72605 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bec9590d-3e11-30de-890c-910e00599e87 | -1.01816 | -48.95927 | 2025-10-20 05:01:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13be4a8f-9a63-3d40-90de-c2c7c4bae3f1 | -2.88012 | -50.71835 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c03a5ad-9141-35c9-8351-a862ca224f8e | -2.86578 | -50.73543 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 377d8b7d-5e5c-345c-9cd8-914a82580d6b | -3.21742 | -50.21869 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91ff67a7-8026-3716-adc6-1ce41033589e | -2.87486 | -50.72717 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35f73132-e1fb-3752-b226-a3d6f325baa2 | 1.79688 | -55.69643 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 975de256-2441-300e-8f04-438f9b47441c | -3.60574 | -51.1227 | 2025-10-20 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ad10954-bade-3728-b5bd-c836765db0da | 1.70969 | -55.76944 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27bba4e0-4b58-376d-bf24-53d762ddea26 | 0.86953 | -51.13068 | 2025-10-20 05:01:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e059c53b-d636-3c6f-836a-728e5223f0d0 | -3.19627 | -53.076 | 2025-10-20 05:01:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c45ac42e-4be4-3176-9e49-3dc0c7e1cf55 | -2.91248 | -52.71238 | 2025-10-20 05:01:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 472d1158-bb4b-3d14-9cf9-6d9cb416dd7c | -2.86196 | -50.73484 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| efcbfcc4-f42a-3372-b7d7-802d6d1b8324 | -2.85753 | -54.09008 | 2025-10-20 05:01:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19e670cc-2d4d-3558-95bc-d892bd4a9c31 | -3.51761 | -49.93425 | 2025-10-20 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8efe15ab-b823-3f89-a897-6ae1bd6237c7 | 2.06739 | -55.7226 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0fcb4f2-ee2c-3c0b-8df2-60dbe26579ec | -2.25033 | -51.91044 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e8c51457-93a5-32f3-bdf9-c5d107e8e1e0 | 1.71311 | -55.97344 | 2025-10-20 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e2350b8-0afe-322d-95ce-695282146129 | -3.24569 | -50.02795 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 220a21f5-ed1c-374f-bdb2-8d6a8e9a15a7 | -0.35468 | -50.37004 | 2025-10-20 05:01:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f3fd698-5575-341e-a1e2-7d1ee553dfec | -2.86124 | -50.73955 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ca2aa59a-379b-3e53-b78a-4286a78fb644 | -3.59796 | -41.65726 | 2025-10-20 05:01:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 4f3ac117-5f23-3c0d-849b-0795346e5911 | 1.73687 | -55.74275 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98faa1e9-4460-3f0f-b6a3-97aeaff4a26a | 1.74761 | -55.72239 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e017277-8845-3714-992c-c37b1ad4eeeb | -1.48969 | -48.68104 | 2025-10-20 05:01:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edb6b1c3-1d3a-3d2d-8a82-b3b1ee073095 | 0.0694 | -51.15746 | 2025-10-20 05:01:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11344710-e134-3d86-9257-86609d959d52 | 0.87516 | -51.25761 | 2025-10-20 05:01:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e6e3df00-11c0-322a-9364-08e7a26bfa42 | -2.86434 | -50.74484 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3983d00-f044-31e6-87e3-403e4ac895e2 | -1.97764 | -50.81146 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f9c5317-68df-3666-9947-4be36851f19f | -2.27393 | -51.92233 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fd52a12f-72ec-3490-899b-9023afffaf7f | -3.42829 | -49.48418 | 2025-10-20 05:01:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8c09578-b391-32e3-bdb5-f3ea0f157b6b | 1.75101 | -55.72187 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0942500e-aee9-3242-bbef-b4c6c649f889 | 1.73991 | -55.91961 | 2025-10-20 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c1ee75f-55e5-3a67-abfd-c29a8773f5b5 | 2.04245 | -55.76412 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b42d8c40-75ec-328c-8b52-d8373eb89e39 | -1.97694 | -50.81598 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4adb0243-f07f-3af5-90dd-909d8d87948f | 0.87018 | -51.13472 | 2025-10-20 05:01:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a7497f6-c05d-3e2c-882f-55f7644f4e91 | -4.49902 | -43.66294 | 2025-10-20 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34fc13a1-b4ac-3bec-8325-47846ccf5748 | -1.09117 | -54.13596 | 2025-10-20 05:01:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bd6df3a0-d237-3cb6-ac2f-d26a5866c3d1 | 2.05319 | -55.72093 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b065783-0f11-33ab-8e6a-d677a9f2136c | 1.78782 | -55.70528 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c82083ba-f797-31e6-a6bd-44cd720b95ba | -2.85815 | -50.73424 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 457886ab-faf5-30ac-9844-72aad34d2d1b | -2.39948 | -57.17826 | 2025-10-20 05:01:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cae92cc4-7043-3726-b822-e91369ee940e | 1.67026 | -55.96852 | 2025-10-20 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0257fe6-46bd-38f0-84d3-be5f89060473 | -3.42354 | -49.48733 | 2025-10-20 05:01:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3f1e338-a2f3-347e-b41a-db6f675c3da1 | 1.81499 | -55.67875 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e882a57f-fb38-38ef-8ccc-764908c93a45 | -1.48876 | -48.67991 | 2025-10-20 05:01:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33ac6b03-d515-305d-955b-c27590258731 | -2.30643 | -50.53642 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2569c59-8ee5-321a-9115-a97bcb36cff8 | -3.19968 | -53.07654 | 2025-10-20 05:01:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ab0fb3e-866a-3f83-9a8d-f29c2f463be3 | -3.42103 | -49.48564 | 2025-10-20 05:01:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67c2802d-18b4-3171-aeb4-9e9e2baa18c6 | 1.79632 | -55.69279 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| d06d1989-f7e6-37f6-a70c-41697c1c660e | -3.59719 | -41.65397 | 2025-10-20 05:01:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a13f64a9-70f6-397f-aac9-5acfe1826478 | 1.79065 | -55.70111 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a861a07e-825a-38cc-80b6-e11d68fa5fc1 | -3.13487 | -52.99826 | 2025-10-20 05:01:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3d4664b-a84e-3a57-bab3-c272bc8c3e4b | 1.76345 | -55.71249 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36532438-bf7e-37a8-b132-886a41756e1c | 1.72567 | -55.94081 | 2025-10-20 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 394d8a3f-eda7-3f80-b3f5-df3c53847496 | -4.83177 | -42.75337 | 2025-10-20 05:01:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2846f6c2-8cb6-37c2-a02b-c30adec55d92 | -2.56607 | -49.11829 | 2025-10-20 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a45df2b8-1432-3b1b-a4f2-9412929d52a6 | -3.42412 | -49.48355 | 2025-10-20 05:01:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d28a729-efab-3087-af97-c9f968c4eba4 | -3.42158 | -49.48184 | 2025-10-20 05:01:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fdfcc65-7cc0-3708-bbf5-083ca6ceaebf | 1.8229 | -55.66261 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a3000a0-94ed-35ca-88eb-643f727c5bbb | 1.78159 | -55.70998 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ae87dcf-6d1e-3c65-b99c-e78bfc577b31 | 1.74275 | -55.91536 | 2025-10-20 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8e2a5e69-1e74-32f2-be2e-60c7e355d1bb | 0.98026 | -51.14309 | 2025-10-20 05:01:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08e92f6f-f8fb-3a2a-a099-42348f9124d8 | -2.80177 | -51.34936 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bb6b1ad-9eb2-39bf-86fe-04d303f6fe5c | -2.87248 | -50.71717 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dca0f37c-2290-36d1-b946-793c36788cfc | -3.33239 | -50.22823 | 2025-10-20 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca7f17f1-b4be-3e08-ab36-f51ada539217 | 1.77985 | -55.70625 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0583fa56-5a0c-34a6-ab78-3c79d7cc2c62 | -3.52167 | -49.93483 | 2025-10-20 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e987ea41-a891-3382-a629-c44bf5cb86a6 | 0.97024 | -51.1488 | 2025-10-20 05:01:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8cb547d3-7c7c-3e5b-a8d4-11cadc2ad558 | 2.03505 | -55.71626 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ae647b6-bb5c-3404-8fbc-1438666de65a | 1.72054 | -55.95302 | 2025-10-20 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 301ccbcf-0d4a-3a44-a219-208bef24abe6 | -1.09171 | -54.13253 | 2025-10-20 05:01:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 69a48ae1-82b1-363b-a081-194bec73e99e | -3.4252 | -49.48628 | 2025-10-20 05:01:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b706765-e6e8-30de-be33-38a0c5f9035a | 1.68628 | -55.98134 | 2025-10-20 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ee45d03-a379-367e-a8e0-05bde1637ec2 | 1.73348 | -55.74329 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72b2a4d6-557e-37f2-9266-cb08d109b666 | -2.25388 | -51.911 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f475d1a2-c112-32ab-aa82-35b0fde58579 | -0.3544 | -50.36802 | 2025-10-20 05:01:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c90181ef-2e11-3d69-93f6-f41c9e3eeece | 1.82573 | -55.65844 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72eac3f1-2c14-349b-bf6a-058e47c190ab | -3.01886 | -52.35835 | 2025-10-20 05:01:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9ab9212f-4f0b-3c27-bdd8-6f112235cd8f | -4.82982 | -42.74655 | 2025-10-20 05:04:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 51f9700e-0473-3de1-ac15-0d9d905c2a79 | -4.83729 | -45.80038 | 2025-10-20 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c2b6adb-d8cc-3979-8341-618e3fc57ec2 | -4.97097 | -49.3848 | 2025-10-20 05:04:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f5552fc-6bee-3427-81f2-c1db5edf58cf | -3.84631 | -51.40004 | 2025-10-20 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README17.md)
