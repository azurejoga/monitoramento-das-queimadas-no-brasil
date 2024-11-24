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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ac6004b-5dd7-38c9-a862-65891ad0b907 | -3.18713 | -54.77652 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 201b7879-4753-3e54-9544-5552c08ed04f | -2.58075 | -49.22392 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 32f2357b-4e79-3f46-a241-24621616b13d | -2.19963 | -49.11137 | 2024-11-24 04:53:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4653093e-7216-3711-862d-8741d191f13a | -3.81765 | -51.99906 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e8127d5-04de-3860-b9c3-7951eb7b2c93 | -5.10937 | -43.15133 | 2024-11-24 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4c734d24-4f32-3375-9620-b0768655e730 | -2.70525 | -46.11254 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e6b8267-69b7-36ce-9e38-9e639c732fe2 | -1.75212 | -54.51762 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0d8585d3-0ed5-3478-9425-6491ed6703fd | -3.85269 | -50.42937 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 568a3bd5-c2df-3feb-b4b6-c639b60be7d2 | -2.70821 | -46.26291 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 900097c1-10f8-3750-bf72-416e3295a0bf | -2.41257 | -50.35376 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 045291c7-c91a-3c0f-be3c-87e943a5c904 | -1.19623 | -51.77128 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| af44fb61-8e16-3622-946c-b1a7731b269c | -3.78479 | -52.29668 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6282b132-9009-3a9c-aded-55d4e8271fe1 | -0.97751 | -51.71281 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 24321ea5-c8aa-3a34-90f9-3eb04a53ce85 | -3.58695 | -52.23434 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0b2d683-62ac-39ef-b49e-fc3994ecd554 | -1.45215 | -54.51241 | 2024-11-24 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fc6897b5-48fe-3379-bc5c-1669be72bee5 | -3.97335 | -50.55626 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b941629e-d93b-3be1-b0c0-7084ac6b6b64 | -3.0244 | -54.0521 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c238d63-bd75-397e-8e17-a7eaa282f9c0 | -1.22164 | -53.68462 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d6a72c72-199d-387c-9fa3-904a0459e12a | -2.01959 | -51.18198 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a19cf5e-93cc-30ab-8af7-e58ec4e6f075 | -4.02328 | -53.81479 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28d98267-aba9-3b45-a1c7-5b1250db02c8 | -3.05003 | -52.75352 | 2024-11-24 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28439de0-03f3-37d4-aa3b-345d9190199a | -3.17278 | -45.29985 | 2024-11-24 04:53:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 377d22e6-7ba5-3926-a0ff-fddea99b2295 | -3.46736 | -50.01398 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b074627-4d55-3bd0-9387-b0f37d459060 | -1.96532 | -48.7048 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c69c126-caed-366b-b7de-3ba74e7c5ec8 | -4.48917 | -48.11403 | 2024-11-24 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7513768d-061e-35e5-b1af-16dbe7a319f5 | -3.23256 | -53.9333 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e88ea89a-8b9a-3256-b352-496f46eaa3fb | -3.3367 | -53.33465 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a951997-4dd0-301f-81f1-8211145ddf3c | -1.60362 | -47.13961 | 2024-11-24 04:53:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5c90e19-54ad-3290-90d0-8f755be839f3 | -3.3917 | -50.3264 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 665d2c2b-b27a-3e08-86d9-79609d891ead | -0.05111 | -51.74347 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9923f22d-95bc-3333-85ed-3a82e7e0bb04 | -1.22931 | -53.36695 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 798837e8-911c-387b-b8e5-e6b9e6b057ee | -1.39911 | -54.50402 | 2024-11-24 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a6546545-0366-3b60-b876-2032cc088755 | -1.9924 | -53.29367 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4479b9f7-1273-389b-ae1b-c5157bba6ece | -2.1737 | -53.6354 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b04af4ee-810f-301d-bd4b-67a7e2654a77 | -1.89658 | -54.59151 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1ab9682-478c-3780-b8ad-c674bee23d9f | -1.89492 | -50.95596 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b007920e-1f58-346f-a0df-ec1d076ed8c5 | -2.75091 | -51.88148 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1567ffd8-d2bf-3fee-b892-ee7604a51c25 | -2.22055 | -46.39304 | 2024-11-24 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2d247761-0a8b-3ec1-a8ef-cad82b048ff0 | -3.63211 | -52.24835 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c38c714-159b-3c55-b352-c8081cdf8f97 | -3.47197 | -49.93725 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 892bc671-9472-3a6b-898f-543136f31260 | -2.70839 | -46.29053 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0b95ffca-a5f8-3dd6-b4bd-d2f3d0044a04 | -1.52233 | -51.62225 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bec8b6ee-0b37-3d76-8f63-6b037db29ec2 | -1.65653 | -52.70233 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4ba34e7-ef41-3d69-9ecf-29b7fb189c5d | -3.66849 | -51.73259 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28d8cbb3-93cf-34d2-8c89-3e9f1bc29e7a | -3.2389 | -54.22652 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fec1bdd-b552-3869-8770-1ebe7117325a | -2.37168 | -50.38427 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc282fd5-5fb9-3c78-abee-2ea81ca7eb79 | -1.7423 | -52.37094 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3187cae-cbab-3926-b3a3-4cf0e75f9720 | -2.5957 | -46.85462 | 2024-11-24 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4a98ce7-f256-329d-bcb4-8ed9eeef43a9 | -2.85633 | -43.56006 | 2024-11-24 04:53:00 | NOAA-21 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 722b07a7-a117-3d11-8985-d6f67647f4e9 | -1.9604 | -49.5316 | 2024-11-24 04:53:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b239b6da-295b-3410-8876-e51aef2f84eb | -4.73442 | -46.50866 | 2024-11-24 04:53:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d33174b-cae6-39d4-9850-0aa583e24c89 | -2.69863 | -51.36545 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec9410ad-4a04-335f-85ab-7e665a1a3ea0 | -2.82104 | -54.00612 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45712753-11b6-3e50-8367-503c7fa23fb1 | -3.41423 | -52.81705 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40f2fba0-0823-3885-a443-6afe3797464e | -2.17117 | -53.7852 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b7ed268-e65e-3f59-a495-51e7a69f2858 | -4.03212 | -54.18504 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 293b3dcc-3c72-358f-bb96-e1f8f64f110b | -3.22915 | -53.93276 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ac09c31-3d27-30c4-a437-6472b8cf2e70 | -3.47825 | -51.99517 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f3ed840a-5cf1-304e-8508-8d858ba609c1 | -2.6457 | -46.85513 | 2024-11-24 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c9d0a602-e2a3-36b3-8430-7a4ce19532f7 | 0.72037 | -51.47483 | 2024-11-24 04:53:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3418c30f-5a88-337a-b9a7-f54e683becaa | -2.46448 | -49.03902 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f119242f-9b88-300d-9d3d-843338ab0f60 | -2.38043 | -49.85203 | 2024-11-24 04:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ef23aa6-b346-321e-afcb-babda4a38fbc | -0.92363 | -53.10202 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 804e5cbc-616f-3dd1-8073-ec4f7b771294 | -2.28858 | -47.3097 | 2024-11-24 04:53:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 088e3710-2440-34b0-8c41-83a2dcd580c5 | -2.95973 | -53.92889 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f84a7c5d-424f-3b4c-ae75-1c604c5a0f68 | -1.82065 | -46.6354 | 2024-11-24 04:53:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4d075a75-d7b7-3cda-bdaf-aaecc2f24932 | -3.17223 | -45.29716 | 2024-11-24 04:53:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 029cfa60-2eae-3234-a2ce-f8b55920a7a6 | -1.19465 | -51.93684 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 124707af-b6a8-3240-8d1d-1c3e70fcf119 | -3.25395 | -49.7885 | 2024-11-24 04:53:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e0951fc-3a32-3e0c-b418-38f41980e93d | -1.19769 | -55.69584 | 2024-11-24 04:53:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 433fdad9-e8e6-3682-862e-e6cf28889913 | -2.10573 | -50.18115 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfcdc7b8-cb06-3498-9a51-60f4d705c59a | -1.66597 | -52.70736 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81aff9cc-6058-3047-b586-288858e426ec | -3.24339 | -54.24258 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e690b25c-982e-3ed4-bf6b-650288ee9b5c | -0.95993 | -51.71713 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 096fdd51-1c97-3acd-ad2a-84f11b613ed9 | -3.02431 | -51.37002 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d859010-def0-35f8-9152-d5cd6ff02c76 | -2.62406 | -51.80206 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cfcc0b5-98cf-3e69-b84b-3b985669da5e | -3.13584 | -52.98742 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1a3145a3-18ed-3aec-afe8-9524ec8e7ea5 | -0.90943 | -51.73745 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0da35b7-2c5d-37d4-8cf9-ea3bbaa681b3 | -3.68854 | -50.21914 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38a7b1e5-62e4-396b-8d2e-81b4a7840202 | -2.07274 | -52.04232 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b5d8d49-7ea7-3d18-8dcc-4a3798e3c21b | -1.73717 | -52.7297 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c25d096d-b610-36e9-a95e-531fa723ff1c | -3.58884 | -50.52792 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 962141cc-d3bf-36d2-a901-9cb0042ec07c | -3.8287 | -52.40965 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a11d7809-9e2d-3877-b86f-ad43b00783f5 | -3.54228 | -50.18966 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2721b2a0-d91a-35ee-a5ae-f59c790a5f7e | -2.92115 | -50.32674 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad7b9e8e-3418-3700-96a0-0f160b9fd828 | -3.04364 | -54.39785 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3419dd10-fcf6-3988-97e9-cafe1209d3fd | -2.8451 | -53.98708 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 95c1f35a-0c58-3939-92c8-8bd67b8df2cc | -2.11409 | -50.12646 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b835566-7eff-3a22-85a2-a537cb1c3cfd | -3.32903 | -54.16798 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b2f5487-0218-30cb-89e9-a245260365a4 | -3.31604 | -53.29166 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68f2ccec-b8a8-3be1-abef-772d9b8244ef | -2.21363 | -50.87646 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8aa1f135-231f-3878-9856-b9886caa0ed8 | -3.51151 | -50.5499 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f097f40-1308-386d-8e93-88ef74969510 | -1.98917 | -48.5503 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01b6afcc-b86e-3f7f-b5ed-7013542b3747 | -4.51829 | -45.72459 | 2024-11-24 04:53:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ff6c399-5570-3455-9078-9db13fc68a42 | -5.10911 | -49.1343 | 2024-11-24 04:53:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf804442-a71a-33c5-8ab6-c020279a79c3 | -3.26201 | -53.26524 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf434510-286d-350f-8193-baeb929ace77 | -3.89312 | -50.07282 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b39cb002-267a-3710-9325-3a5938fe002c | -1.25766 | -51.74989 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9b53e4ec-83d6-30c8-9434-713cdf596475 | -3.06724 | -53.22806 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a51926f-c636-3107-a202-7bf2a10e0250 | -0.98081 | -51.71331 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README56.md)
