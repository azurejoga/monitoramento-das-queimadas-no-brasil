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
| 7b207c02-976f-3469-bdca-6db5bd0f6e21 | -5.98163 | -49.66304 | 2024-09-29 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3b0500b-30e0-3def-8a68-e285cacdbb2e | -5.98106 | -49.66681 | 2024-09-29 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dcebd3c6-4879-3301-be45-c1dc92c35390 | -5.97809 | -49.66255 | 2024-09-29 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 900f9c98-509f-3c66-b7ce-044f1505a8e7 | -5.97752 | -49.6663 | 2024-09-29 04:49:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 2ad7c108-ba76-3289-9813-eb3cafdaf936 | -5.8928 | -49.72543 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ec1345e-fd0b-3db9-ada9-cf3072c2b1d7 | -5.89214 | -49.7266 | 2024-09-29 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c540b25-942e-300c-848a-47bff3cbf1c8 | -6.20338 | -50.90833 | 2024-09-29 04:49:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1307e42-eb88-3c32-b7d9-0d6bbcb2dc79 | -6.2 | -50.9078 | 2024-09-29 04:49:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10be883a-177d-37e3-acf2-74c1e2b19d45 | -6.17972 | -50.90471 | 2024-09-29 04:49:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 567fced8-a78c-3dce-91c8-c46df2ff3af4 | -6.17916 | -50.90832 | 2024-09-29 04:49:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aeb2baa7-9bba-312d-8bda-0bb72cc089d0 | -7.85432 | -50.50222 | 2024-09-29 04:49:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 703ff953-d91e-3016-a1cd-292404b4309c | -7.81182 | -50.23006 | 2024-09-29 04:49:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67c0e5be-e71c-3f03-b4e6-cbcd6c6cb40b | -7.8085 | -51.19589 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c64f8632-41f8-3095-9bd9-e7a5ca631a6e | -7.54944 | -51.40058 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14f9a8e5-0d12-310f-9038-083cb00fba99 | -7.19371 | -51.16936 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0886b6fc-4d2a-3020-b13a-ad779488e43a | -7.18824 | -51.22798 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ee969a6-d5c0-3a1e-9e19-d4ff52a4aa6c | -7.1877 | -51.23153 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 87dc36a2-c6d1-3a4b-8a76-69f28a4ed838 | -7.18542 | -51.22383 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b35d973a-9ec6-3f56-9b84-41222b112cd0 | -7.1787 | -51.14485 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2dbcc40-5692-30db-ab24-6f070a0ed451 | -7.17591 | -51.20741 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55b67025-7edc-31d7-b566-8550a84e6e4d | -7.17588 | -51.14071 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e03ea15-37cd-3cfc-9322-b0d00a2c1a3b | -7.17531 | -51.14436 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4efba69f-535f-361e-9cd5-cc1b6fce1bd4 | -7.17475 | -51.14799 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91f1a462-fb0c-3d97-9dad-ddba184c120b | -7.17193 | -51.14387 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 785fe1c0-c8e0-31c0-97e1-ace95c9dec9c | -7.1426 | -51.1097 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30f5c3ed-f27b-3281-bf9a-500bc82b1835 | -7.13922 | -51.10918 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0d290fd-8285-364e-b239-e3821409f9ee | -7.12827 | -51.27016 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14af5756-5ef9-30c8-b140-e3c18e972ef4 | -7.12491 | -51.2696 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b68e4af0-5e48-3610-89c5-40c16c872a73 | -7.10993 | -51.1197 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| faf7a3bb-2829-3ea6-bb84-377277d5ac68 | -7.09626 | -51.25421 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec75af10-a83e-3c58-8e54-15201fe2e893 | -7.09572 | -51.25777 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a25d0cb9-247c-3e9c-a627-3968333b5e9a | -7.09236 | -51.25722 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb8185f6-4d21-3683-8854-6f34d6db7333 | -7.08954 | -51.25312 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09a9b621-dd8f-338f-978d-0a7a8966b093 | -7.08618 | -51.25258 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23f2a524-03d7-301f-b463-7dd9ae4af2c3 | -6.60824 | -51.03246 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a45dbbd3-1c94-38f6-bbff-d34e457e76dc | -6.60769 | -51.03607 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c04442e1-5717-3c3a-b623-c46433f545b5 | -6.5674 | -51.11867 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db9d2d2f-36e8-35b6-a818-36eee6bfdda5 | -6.56404 | -51.1181 | 2024-09-29 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e3a9dd7-173e-3911-aa73-234b04e4bad8 | -8.27369 | -51.01679 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19a323b6-383f-36c4-b8ff-1dcfcf0a2498 | -8.27075 | -50.8056 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e5a1fb3-90af-35ff-9c1a-f0a2861f9456 | -8.27019 | -50.80933 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46fd44cc-f3a4-322a-a571-c13bd3a4d2be | -8.26731 | -50.80504 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 859e3de6-5a70-360b-8e5d-ed777f42f4a5 | -8.26675 | -50.80877 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 721c7a8b-a64b-3b4c-93d9-6c975c8d17b4 | -8.26387 | -50.80448 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a57187c-7bcc-39af-a5d0-66c123ada2b1 | -8.20957 | -50.77323 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e448c3e-885a-356c-bd85-70503215b695 | -8.20612 | -50.77273 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3245fd23-2612-39fa-9097-a48fd5ca0ca9 | -8.20253 | -51.02496 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 218affa1-642b-30d2-8e02-edecac3e8dca | -8.11095 | -51.12108 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98c4f9b0-7c08-37ed-8efb-491d0ee85ea8 | -8.10811 | -51.11686 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77ee6a69-0f60-3039-ae19-f280ed204bdc | -8.0741 | -51.1115 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab21d98c-22ee-3e2b-8006-691f4f93934b | -8.0736 | -51.13787 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fb847e1-61ca-3fa2-a7d1-f3e775a55a76 | -8.07304 | -51.14153 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d12aa90a-2d59-3ab3-914f-840cd7ecedff | -8.07076 | -51.13365 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 330ce4a4-6b05-3f86-987b-18bb079ea580 | -8.06965 | -51.141 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 902ff2f7-f0ab-35ab-a968-731e5cf5d764 | -8.06847 | -51.12573 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 919daf37-210c-3f64-943c-a415b94d647e | -8.06792 | -51.12942 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cc56471-6ec3-3d9c-827c-ef4728ad7fc8 | -8.06774 | -51.12568 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a917a699-7b9d-30b3-a3e9-7db388030809 | -8.06718 | -51.12935 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83dd3521-03ca-3615-9e9b-35a738b07164 | -8.06151 | -51.14352 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49ed811c-10e4-3c62-b7cc-99ec9f89453b | -8.05754 | -51.14668 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb2beb66-1394-3c23-ad0d-bfad8bc01129 | -8.05697 | -51.15038 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ffc5971e-8d1f-3b99-ab66-2e3069a78df6 | -8.05415 | -51.14615 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a502a0a-b607-390b-964c-16067b45d04f | -8.05358 | -51.14982 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8dc52f02-f67f-32ca-b407-445423e374fe | -9.32917 | -51.14269 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0094abc-a2d9-380e-a8ad-4a5dd8108683 | -9.32574 | -51.14216 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45e7b6b6-7677-3966-9658-47e832cd533d | -9.32231 | -51.14162 | 2024-09-29 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ecd319a-eeb9-36a3-8eed-8e3ce931f760 | -9.30764 | -50.78073 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f8c8fae-96ba-3dbb-8b7d-ce9ab027759d | -8.74541 | -51.02222 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6836e782-a699-3b4a-96f1-866dded305fb | -8.73522 | -51.02108 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9fde223-bf9b-36f3-a45c-0a68bc04f6da | -8.7351 | -51.02083 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 180cd168-86c7-3e23-abde-a7d5480885d6 | -8.73179 | -51.02057 | 2024-09-29 04:49:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0feae089-adca-3155-b06b-b4d869fbb962 | -8.71929 | -51.0106 | 2024-09-29 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3117ce56-0cdb-30a5-9d34-7ceef40ac570 | -8.71871 | -51.01437 | 2024-09-29 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b767ab86-94dc-3f9c-9081-9a66006f4416 | -10.84836 | -51.06612 | 2024-09-29 04:49:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f49550ce-648e-39f5-88bd-504b52f86fd6 | -10.56948 | -51.10084 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7c97463-67c0-3084-b204-f3d442cf0a18 | -10.5676 | -51.10204 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd3aead8-04a5-34ac-9992-d9fac160a946 | -10.56601 | -51.10031 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0588e7f2-c1ea-3315-8f69-767ecfe1a1e5 | -10.56471 | -51.09764 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95a2cfaa-f6a6-339e-85ce-1965800435bb | -10.55428 | -51.09608 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c06030e1-f5a2-31e6-89bb-d1fc749a4b4a | -10.55081 | -51.09557 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 325339f6-dc5a-3cbf-abae-8a52b8f9045c | -10.54733 | -51.09506 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 847bc9f4-4017-3c02-bfc5-29691c88f9f4 | -10.54674 | -51.09893 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8303bc84-f1e9-3d86-8b4e-d0061ec6dd5a | -10.54385 | -51.09457 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9617f1a4-a32f-3ded-95fe-1fb3466876de | -10.54326 | -51.09845 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1ac6e0f-9c1e-3439-8393-5293f9b792ef | -10.54036 | -51.0941 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4cd6640b-f525-35bf-9b92-763a615c15f2 | -10.53978 | -51.09798 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a867ad6c-7c88-3081-a396-7afe2c2c1e1d | -10.53688 | -51.09362 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5479e29-befa-3107-8802-4f4450141aeb | -10.5334 | -51.09315 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1053d951-f9bc-3dbc-b5a6-6789eebd44ca | -10.52931 | -51.09669 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d9a07d7-77c2-3b1d-8603-4df3362249db | -10.52523 | -51.10018 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3251fac6-995a-3593-89f8-cc2e541f2796 | -10.52464 | -51.10413 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 033ca1de-1893-3fa1-9266-455d52ad0d67 | -10.5235 | -51.1117 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c833ef4f-a83a-37b0-9f9c-b862a50966ab | -10.52176 | -51.09967 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cdb08e57-fdb2-3a08-90ed-07c4b586bb18 | -10.52117 | -51.10361 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1008083a-715f-3032-9207-5bfb5c9bbbcd | -10.5206 | -51.1074 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80d06e94-98a3-302d-9149-ed3604968030 | -10.52003 | -51.11116 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e13b0292-e338-39c0-ab91-091620390fc0 | -10.51831 | -51.12268 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd01a684-61fe-346d-9762-48cc79f107bf | -10.51774 | -51.12649 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67fac02a-c7bc-34aa-9512-07632db4ffd6 | -10.51716 | -51.1303 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3b84a78-ed6a-3656-910b-89b78f936333 | -10.51659 | -51.13411 | 2024-09-29 04:49:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README48.md)
