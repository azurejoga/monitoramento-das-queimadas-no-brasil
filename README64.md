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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6624a010-b766-32d7-bd79-ba03bcffc6d1 | -9.40858 | -60.52541 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cd50c9eb-b5ff-338f-b263-dba78fa363f7 | -9.49422 | -60.54278 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d81e1a5a-3f8a-3f3c-a9aa-fc5dfdee52d2 | -9.13935 | -65.27548 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c4b30db-e428-399e-b977-51d3857c06dd | -9.15709 | -60.78144 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b879e00-e267-3512-9426-0405b294f2de | -8.95038 | -65.94521 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0d47153e-6d27-3a3c-b17b-d0a92bfff810 | -9.63561 | -59.64289 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2995997-d848-3460-a71a-1077d85a71df | -7.29216 | -57.63824 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96b97ca6-d976-34b8-91be-5e49cc2aff12 | -6.63355 | -58.54536 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74abdc8d-7433-3e7f-823b-c332a8ca9444 | -7.53691 | -61.38282 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b89432c3-6f93-3b8a-b05c-26d0823762e5 | -6.84076 | -58.96106 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9aa4f13e-c286-3125-b014-826d62bb9eef | -8.95472 | -65.97205 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e3ddb4ce-83ef-3b52-96bf-4161690e5af6 | -9.17853 | -59.45621 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91e3b56a-b442-3a33-b0b3-4475458c6df4 | -9.4046 | -62.49372 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b570b48-7d61-36ca-a0cb-1944b5c63878 | -11.13443 | -46.34379 | 2025-08-27 05:18:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9c4670cb-3745-32fe-ba20-70b394f55850 | -9.64222 | -59.64394 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10641a6c-b726-3680-b661-21ee111fdb50 | -7.49986 | -64.58926 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4e7c257-a183-3676-a3d8-97576e1787f8 | -9.41024 | -60.53649 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 66b47197-9bc4-32c6-abf3-b768260de513 | -9.00515 | -65.39838 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98f78806-78f7-368a-af1e-e7700d4f9c0a | -10.31688 | -46.80341 | 2025-08-27 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 43ba9a13-da07-3070-8685-f6e47569c877 | -9.25275 | -59.61045 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d06a2bc1-4433-30f5-822e-256368dcf951 | -9.25441 | -56.90453 | 2025-08-27 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33932124-e12e-31c0-b8e0-7a04f5a42562 | -6.69431 | -58.54769 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1032d752-845e-3129-ad18-3d921d0955d2 | -6.77024 | -59.67322 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c47d65e-aeaa-385c-a25e-cb83c91a46f3 | -6.82153 | -58.97577 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f74bcfdc-6ce7-3684-8030-fecaea9a507b | -9.28579 | -56.91348 | 2025-08-27 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d16b243f-d954-3afe-8c75-89a8726b7320 | -8.85399 | -62.4431 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff7b1e21-4ba7-3b4d-939b-e167541d8181 | -9.18753 | -60.80088 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e365cb6-44fe-3857-b2ba-68f163903931 | -8.99679 | -65.39693 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e12e9ac3-ce25-3649-af28-b1ea1fed3182 | -11.31533 | -55.21501 | 2025-08-27 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6fe8111-5816-3d2c-8df8-392252e79997 | -9.40415 | -60.53191 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d694dfe0-4f34-39c6-bdcd-2e26896967f2 | -8.95471 | -64.13327 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3a92cfb2-8045-303b-a992-cd4b4bcddd0c | -9.22921 | -59.67442 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c580251-cd88-367e-a644-db246a7395b5 | -9.413 | -60.54053 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bf7a3d3a-d2ad-3a05-b1d0-33331211af46 | -9.40591 | -62.48575 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd9753c8-1b5e-3df1-9b28-a3d830827353 | -9.13871 | -65.27924 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f6c2887-b0be-3728-b8d4-e69e93a1a88c | -9.08777 | -65.72585 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb5b83da-558d-38a5-aa73-7bbb5628e900 | -9.18623 | -59.45029 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 545bfb06-ab89-3994-8738-f2621e67727e | -10.27549 | -64.50253 | 2025-08-27 05:18:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40f3a28b-9b14-3fa3-ac80-a45dfb99a0e6 | -8.63511 | -62.65026 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5ddcb39-3131-3177-99fe-f7372a6a0fd7 | -5.45219 | -60.15683 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a4b6b50-3516-30a1-ba3a-c9673b3cff99 | -9.41247 | -60.50084 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f079b59c-ad60-33e0-89d6-1d76b8d3c826 | -9.23002 | -60.92089 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4430eebc-22cc-39fd-91d2-54127cd78edc | -8.92143 | -65.93166 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 42ffb87f-14b6-3186-9378-76a01dcdcfb6 | -10.27936 | -64.5032 | 2025-08-27 05:18:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c319814-b607-34bf-969b-ee40b77b22de | -8.89741 | -60.76489 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f5cd224-f4ca-3dca-a5cb-a8ba301c1860 | -6.68599 | -58.53569 | 2025-08-27 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06ee58f2-ac84-398d-95e3-d6713eb79af1 | -9.17319 | -59.51244 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e635f52d-f23d-3aa0-99aa-86f1a323c9dd | -9.40583 | -60.49978 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| f255ba78-1b0f-3500-93cf-6e52b73f36c5 | -9.79789 | -64.24797 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 508b9420-4bef-3ae3-b3c8-3b503f6de959 | -6.81215 | -58.97077 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6618638-ae11-3512-88e7-d7fd68ae1221 | -9.23059 | -60.91733 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93b11eba-70d8-3d6d-bc94-03392d4dbd2c | -9.01884 | -65.69289 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc1bd011-7903-3f7b-b3bd-83f5a072e42b | -10.40602 | -64.39772 | 2025-08-27 05:18:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7008979c-ca6a-39ea-a72e-6088b307cad0 | -6.61686 | -59.95511 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 424f1cee-b0bd-384a-bf50-1152bc08a4cd | -6.81492 | -58.97474 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8121564e-6faa-3e8b-b8fe-d2837b1c526a | -9.03872 | -65.72978 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01801343-07c4-3e47-a321-f8772aa9087b | -8.85974 | -62.45229 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8f86105-2b23-3536-a2c6-9fdc63651af1 | -10.2449 | -59.66151 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7dea1fc-cdb2-3ea1-a97b-dfab91e6279e | -9.7987 | -64.24315 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31b4f214-c3a9-3dc0-9f85-a2d446fc6446 | -10.79306 | -47.0618 | 2025-08-27 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| b3095eca-ff97-3b5f-a9ac-ed88f97d363e | -10.09992 | -62.90179 | 2025-08-27 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9d7d4a35-7c93-3281-832d-7639454e56b7 | -9.41688 | -60.53754 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 03e280dc-ae9b-3af0-842d-6ec3c4b52d9f | -8.90188 | -60.75832 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c86edee-d516-3fa3-bd8c-49f4cd1886c5 | -10.09569 | -62.90527 | 2025-08-27 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 27d25851-910d-37d3-9b3b-d385501bbfd7 | -9.64276 | -59.64046 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8400ac87-88da-3712-a606-9c6de3629e64 | -6.25363 | -60.01582 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cec38ac5-8137-3faa-b819-b821d4e4830a | -12.7706 | -48.17224 | 2025-08-27 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b5037e2e-2c6b-3150-82be-bb8eab1be4f0 | -9.80174 | -64.24863 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0caf152-e609-3d49-9ee5-90da32cf2e54 | -8.93734 | -65.94302 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 7c071d52-a126-3623-85fb-cf1b40a486c9 | -9.25501 | -56.90044 | 2025-08-27 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ca301f5-f649-3672-b44f-1598887d5976 | -7.54593 | -63.83859 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d6407c50-d602-36fb-b49c-7ac9fb7a80ae | -5.31196 | -60.20358 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4f098a1-0be4-30ee-b8ff-930e1c67bcbb | -6.94029 | -59.56495 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 277547e4-eace-38ec-ae04-873e28b1bbf1 | -6.81762 | -58.95745 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1d4e839-6a3a-3802-a8ac-b7cd7956f050 | -6.24587 | -60.0218 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f0db7ba-d04d-3c98-b473-d1c8bba8046c | -9.23728 | -60.9184 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2950ffa-460d-3648-855f-1476acdf5679 | -7.39896 | -64.34899 | 2025-08-27 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8008658d-36e3-3e89-869c-53cd2f39dd59 | -6.24254 | -60.02127 | 2025-08-27 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa44faa4-9841-3b3c-97b3-3a7ec16245f2 | -7.16784 | -59.73987 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46467b31-56b6-3a88-8beb-c6aaa3cedefd | -11.80986 | -46.80226 | 2025-08-27 05:18:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba9193d8-531a-3962-9f0c-74203e55cc53 | -10.40547 | -57.70114 | 2025-08-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af38cc9e-39ef-36f5-b96a-d9140cd38b04 | -8.93592 | -65.9254 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb6eec7b-79fe-34ac-99e8-fcccac19b96a | -9.63723 | -59.63245 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d9ff1e75-1205-3cea-8618-c5b940f20ef4 | -9.13521 | -65.27479 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56fdf141-fc60-3892-b107-7ddaaa833b72 | -7.27308 | -57.67261 | 2025-08-27 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7915f82b-8cc8-355e-9c82-d6f32bf601ff | -6.79388 | -59.63076 | 2025-08-27 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5fdd2287-1e42-3a53-ab86-a29fd1b743e5 | -11.30527 | -55.11161 | 2025-08-27 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2587726-1e8c-357a-b1a9-484a2881efcd | -9.22668 | -60.92035 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 201a14b4-d933-3b0c-a216-b6ba62352c7c | -9.41633 | -60.51945 | 2025-08-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36fd1d11-abff-3433-8905-ea9ceeeab969 | -8.85686 | -62.44769 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edd174de-3819-3d5c-84f1-2951037f3565 | -8.65787 | -67.26409 | 2025-08-27 05:18:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 662d3d2c-18a6-332d-af36-a0eae79d8e06 | -8.86105 | -62.44427 | 2025-08-27 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 773a1dc0-7359-3bac-b6f7-5a1ed2b7eb62 | -7.7459 | -67.15262 | 2025-08-27 05:18:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a6ecf18-3774-3087-891e-b5c242c7130f | -8.53845 | -62.66515 | 2025-08-27 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec8372dc-25ef-396b-95d8-8949ae28c5a4 | -8.9511 | -65.94101 | 2025-08-27 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f48160df-c389-3dda-a082-0b7a4c47fec4 | -9.17162 | -59.54422 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d27a0980-dab4-3c4f-a614-1bed378281f2 | -9.17486 | -60.79885 | 2025-08-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24699c9e-a2ed-3696-a5dc-d42e13a1d94b | -8.23828 | -61.4556 | 2025-08-27 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 079ddd42-d5e1-3254-95af-ed82092b5a5f | -10.27328 | -64.49207 | 2025-08-27 05:18:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c9827def-28c3-3de7-b4a3-86857ab87c46 | -10.79165 | -47.07412 | 2025-08-27 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |


[Clique aqui para ver as próximas entradas](README65.md)
