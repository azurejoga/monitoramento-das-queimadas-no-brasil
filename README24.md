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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce2bab91-4ad2-3ab6-ace2-d837c5f129e5 | -17.6654 | -57.5645 | 2024-11-30 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.1 |
| a0c606cf-374b-3a93-95f0-e330d6ce3fe7 | -3.5875 | -50.0002 | 2024-11-30 04:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| edcc7b14-0820-3bdf-8316-ccfbf8d94002 | -6.8967 | -43.5436 | 2024-11-30 04:20:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 76702e40-fd04-34f2-83eb-afe97e7e9808 | -3.5876 | -49.9791 | 2024-11-30 04:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| d9bafab1-5895-394d-8542-7f26172d9c14 | -3.2591 | -53.6186 | 2024-11-30 04:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| b4fc033b-e0bb-3095-947c-7c739ac98303 | -6.9344 | -43.5401 | 2024-11-30 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 2b0366d4-859e-3619-a0ea-78283a7fda2f | -6.9153 | -43.5652 | 2024-11-30 04:30:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 0b3168a6-b2d0-3e68-8693-a72c48f19f2b | -1.6419 | -53.8529 | 2024-11-30 04:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 250eedce-0a32-3e16-86ee-e49ce674c040 | -1.0733 | -53.6378 | 2024-11-30 04:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 18672697-854f-3bd4-9f97-00c998cebe04 | -3.2406 | -53.6393 | 2024-11-30 04:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 9e08eb98-3718-36cb-b2f7-2453e87e5a22 | -3.6245 | -49.9777 | 2024-11-30 04:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| df3f7f78-eaee-3c7d-822a-4c2368b0e5ec | -3.4791 | -53.8142 | 2024-11-30 04:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 82a6deae-02da-3b77-826b-7ecb323385be | -3.6061 | -49.9784 | 2024-11-30 04:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 173.4 |
| 2a5dcd4f-7b0c-3cf8-b708-dd1250eebf4c | -3.5875 | -50.0002 | 2024-11-30 04:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| ad2fdddf-55e3-344f-81d8-b1b0fe712717 | -6.9158 | -43.5185 | 2024-11-30 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 29.9 |
| d8c01d75-f1de-330f-a574-3c6987c5c63e | -1.6419 | -53.8731 | 2024-11-30 04:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 122.0 |
| f8ed8ea6-0bf2-3db2-95a6-69e36c516719 | -6.8967 | -43.5436 | 2024-11-30 04:30:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 38f83122-e653-39bd-a10d-449335f69d17 | -6.9156 | -43.5418 | 2024-11-30 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 0554c62a-074e-3706-94a4-e98b71df631c | -3.259 | -53.6388 | 2024-11-30 04:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 0928f9db-bd4e-374a-94ff-f56f1584aeaa | -1.6938 | -46.7833 | 2024-11-30 04:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 10d54cd0-cb94-317c-a3a2-f916d8ab2fac | -3.606 | -49.9995 | 2024-11-30 04:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 4c956f9d-19d2-3d41-8b4f-dde1b7e93b7b | 0.63135 | -50.56792 | 2024-11-30 04:38:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49dd58c7-4409-3703-96cc-764a98dc1e65 | -0.09597 | -51.75274 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b64dc882-9186-337e-b0f1-f042811d27d8 | 1.19421 | -55.94768 | 2024-11-30 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 491b6990-5e86-304c-88ab-5524f1bf9ec1 | 0.98614 | -50.24912 | 2024-11-30 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46f0bfe9-7919-3d83-b3b0-5b1d88de62ff | -0.26466 | -51.4917 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 568c64ba-bb45-32e9-84dc-106dd4797858 | -0.26637 | -51.64648 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c24e87dd-ee6c-3795-bed1-3254e40a073e | 0.71686 | -51.46339 | 2024-11-30 04:38:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8eb663a8-a186-3088-8d3b-5c1f69103155 | 0.92974 | -50.27317 | 2024-11-30 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e15d3a3f-5f8e-3a6c-b4ff-a16ec48818ba | -0.2462 | -51.60883 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b2a5f92-b7a0-3dfa-b3d2-b61f341578d1 | 1.37881 | -50.94906 | 2024-11-30 04:38:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f605b4e2-8a9e-37dd-b3ed-75011b047201 | 0.72251 | -51.47555 | 2024-11-30 04:38:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f64b6077-6e74-34a7-9351-ececcbccfb2c | -0.19253 | -51.54187 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81d35019-54c5-3f2c-ba1e-c78c27089245 | -0.2571 | -51.61052 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb3dc160-2cb5-3661-a4a1-2a67f2baa7a7 | -0.1487 | -51.42017 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2fa79fd-23e2-368d-a3f0-f25e44d23f7f | 1.18609 | -55.96036 | 2024-11-30 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 29dfb186-c44e-3496-a8fe-96dad510553e | 0.98514 | -50.24906 | 2024-11-30 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb6bf3d3-9940-3a7b-a0e3-7e32c699ed8d | 0.97755 | -50.26203 | 2024-11-30 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| adb11406-62d8-3718-b734-726586d7820d | 1.10018 | -59.58772 | 2024-11-30 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 03be4f07-d878-35b0-9e8e-12e97706d89a | -0.02856 | -50.73655 | 2024-11-30 04:38:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e69e264-b897-3cc6-83b4-cce9b4066d6b | 0.88837 | -51.98668 | 2024-11-30 04:38:00 | NOAA-21 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 38c4e361-b7ea-302d-9988-dc9d58db840d | 1.38175 | -50.94445 | 2024-11-30 04:38:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c85445ed-e2fa-3f76-8e8c-d6c16c9eec9b | -0.10669 | -51.49059 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d8d3c16-7659-3968-935b-b9c80053eaa8 | 2.80878 | -51.08474 | 2024-11-30 04:38:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e96d1d3d-5e41-3c42-a64e-1a890010e5c2 | 0.94881 | -50.74835 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbadca39-f48d-33f2-8da1-2f79e1c18ef0 | 1.67511 | -50.66315 | 2024-11-30 04:38:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2a8db6e-fbfc-36f1-915f-90938df1969c | 0.03304 | -51.10207 | 2024-11-30 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fb95493-79c4-32dc-b898-7300a7d70fdb | -0.98663 | -47.88389 | 2024-11-30 04:38:00 | NOAA-21 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34b9dede-034e-38c1-813d-8f841160f2da | 0.95006 | -50.75624 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 917f9e6f-ebf4-3313-a60a-b1af2cd0d871 | -0.94189 | -47.56104 | 2024-11-30 04:38:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bbbe2840-ec21-3c7e-8bf9-969bd6c600bf | -0.09298 | -51.74791 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d73c7742-7f95-3936-a61d-623b07fd90dd | 0.27141 | -49.80529 | 2024-11-30 04:38:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2162cfb-5ba3-3751-bcd6-5c8011203d0c | 1.21221 | -55.93377 | 2024-11-30 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bee75fa9-6ec0-3d7e-8d09-069aa0f76e09 | 1.10095 | -59.59266 | 2024-11-30 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca93739e-48d5-3ab2-8f98-4031720ad3fd | 0.62846 | -50.57232 | 2024-11-30 04:38:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9193287c-9ccb-3de4-9617-60b0a88b916c | 0.99554 | -50.27071 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b63b9ce-df41-3d19-974a-f4eeb50bb0d0 | 1.28164 | -55.91426 | 2024-11-30 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a73a3b8-9bac-38f2-a035-b43f0ff5db26 | -0.05577 | -51.60323 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cea52e6d-e0e9-3c4f-9c98-eb7086540721 | -0.24595 | -51.44648 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f798fcf-9204-3865-9a74-ed871f708238 | 0.97812 | -50.06575 | 2024-11-30 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 614cdb3a-c6d0-33bd-b682-16ac66151b86 | -0.25347 | -51.60995 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88d2634b-3b98-379a-82d8-ace9c9b896f3 | -0.26181 | -48.6291 | 2024-11-30 04:38:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 217e64fe-4abc-342c-87e4-06b5d95318e2 | 0.94113 | -50.74547 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 714f874d-7513-34f3-b7c2-1ecd63a6a442 | -0.19616 | -51.54242 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5e69ae24-4a43-3c23-aa03-5fa295b938ea | 0.0466 | -51.70695 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 550f4ddf-eaef-3c3f-83b1-89248245f89d | 0.98862 | -50.27177 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb507a52-ee25-3332-ab2a-5429fce787c9 | 0.98804 | -50.26798 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e5478584-d8c5-36a2-bd97-d74cc874493c | 0.27479 | -49.80477 | 2024-11-30 04:38:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5654840e-b1bc-30c3-94d3-10b5a7a05790 | 0.92915 | -50.26939 | 2024-11-30 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 50d3b290-ee86-31e4-8042-5272d99b168f | 1.20815 | -55.94003 | 2024-11-30 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1b01e7c-073c-395d-8311-c6590d6b8a7b | -0.05361 | -50.82781 | 2024-11-30 04:38:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1927f559-632e-382d-af88-887af04f274b | 0.93698 | -50.74206 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cdcb3785-9db2-3335-b0ae-f6b2adb65965 | 0.06524 | -51.49145 | 2024-11-30 04:38:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 09d3cbe1-b612-3c48-8539-e5433a844c85 | -0.27331 | -51.62592 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c9873b0-200c-3331-982e-505a9611c3d9 | -1.30767 | -46.77568 | 2024-11-30 04:38:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47be1a3e-d422-3b7b-a589-f3d8395297ab | 0.93636 | -50.73811 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ff25962c-b7cb-3066-8d28-abc32fc5dcca | 0.99092 | -50.26366 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bba28e30-3ade-3768-a621-4afc1a69564e | 0.95068 | -50.76019 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ad2f435-44eb-3979-88d7-e782f81cb2d9 | 0.35294 | -50.66845 | 2024-11-30 04:38:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b1ef02c-16cb-392d-a1c6-f6de4770cc2c | -0.24984 | -51.60939 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cc916839-87eb-3ffb-bdd7-4be0d241e99a | 0.93989 | -50.73758 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 771f1c1c-9450-38f1-aabe-a508caed8561 | 1.18372 | -55.97764 | 2024-11-30 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| aa3931e9-4f7a-3f35-b12c-08bdb09ef5bf | -0.01899 | -49.63688 | 2024-11-30 04:38:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ab7f1ca-0401-37cf-bbf0-e50de0c9ea50 | 1.19506 | -55.95309 | 2024-11-30 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e2680477-4e6c-35ef-85bc-68371c4fdb3b | 0.97923 | -50.25017 | 2024-11-30 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ff2bdabf-6d97-3652-bc1d-354a9284343d | 0.97701 | -50.12707 | 2024-11-30 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f8301e4-9248-39b8-90ac-7e9870b155d8 | 1.28656 | -55.91348 | 2024-11-30 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1d56684-6fb3-324c-a8fb-f6d4166d5872 | -0.27265 | -51.63013 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9070cec0-febc-32ee-a237-9bb908fc458a | 0.89212 | -51.98602 | 2024-11-30 04:38:00 | NOAA-21 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8f64a58f-f31b-3be8-8d01-398953ef9369 | -0.26967 | -51.62536 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbd46cec-4d25-3591-8064-680c93821014 | -0.09912 | -51.27843 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ae1bb652-cf67-3dcf-9756-7bef48877067 | 0.20135 | -49.85356 | 2024-11-30 04:38:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c942625-19bb-3ac2-95d0-2cd31712c5f6 | 1.67573 | -50.66714 | 2024-11-30 04:38:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 912f5b85-24fd-3d32-b4ee-043eee3be9b5 | 0.94466 | -50.74494 | 2024-11-30 04:38:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5a99261-012e-37ee-a082-d677e9cd755e | 0.88768 | -51.9822 | 2024-11-30 04:38:00 | NOAA-21 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| edd08073-352d-3c32-9537-1a177ab6858f | 1.18695 | -55.9659 | 2024-11-30 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 595151ca-c2e4-32e7-a76d-3689b1e48fff | -0.38645 | -51.57318 | 2024-11-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4fdfd34-9eb6-322a-809a-002df65bfff9 | 0.97644 | -50.12333 | 2024-11-30 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b28c1629-2213-36cc-b530-8b12ff47a985 | 0.35583 | -50.66405 | 2024-11-30 04:38:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee313bb4-082d-35ac-ba6a-93ba1f7de1e0 | 1.35791 | -50.72144 | 2024-11-30 04:38:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README25.md)
