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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1499c3d-d507-3103-a456-3009ddb1e35e | -1.3271 | -55.8475 | 2024-11-30 01:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 6554d79b-6f1c-3fad-8ced-344371169937 | -6.07214 | -48.03604 | 2024-11-30 01:30:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 214.3 |
| 169fcd09-bcbb-3777-9043-697c039d10ce | -6.08283 | -48.06429 | 2024-11-30 01:30:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 194.8 |
| 4ceea68b-f33b-3bc6-9379-bc7082cb5165 | -6.57801 | -51.11539 | 2024-11-30 01:30:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 5cebfe00-48b4-3a07-b51c-4bb346794c5a | -8.14144 | -54.85204 | 2024-11-30 01:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e325cfb6-331c-3920-a285-f611c99882a7 | -6.07683 | -48.02808 | 2024-11-30 01:30:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 8ed7b376-871b-31e1-af57-ce04859ad3cb | -10.18616 | -59.52763 | 2024-11-30 01:30:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ade66bba-8810-3df3-b1d2-e52969cce96d | -6.07788 | -48.07207 | 2024-11-30 01:30:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 711dbd48-c62e-348e-933b-043354402c6a | -6.08874 | -48.03313 | 2024-11-30 01:30:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 38.6 |
| ddf83320-d5b8-3351-8b10-f6036ab180c5 | -1.49735 | -54.94309 | 2024-11-30 01:32:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 86155e67-76fc-3c9e-a7db-9896a071ab36 | -3.40182 | -50.66098 | 2024-11-30 01:32:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 006a4f0c-8c6c-34a4-8009-a47c25df773d | -2.57126 | -51.83531 | 2024-11-30 01:32:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| c54bf177-573f-3996-9c2e-3f5a9371d16f | -2.60371 | -53.9912 | 2024-11-30 01:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 6503e6f7-0225-3539-8891-95f20653234c | -1.66181 | -54.23817 | 2024-11-30 01:32:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4da8b4e5-c940-39a2-b317-398cd4087f41 | -3.11659 | -53.81282 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 24d5f2de-2340-3e68-992a-a0a10848ab9a | -3.1084 | -53.10696 | 2024-11-30 01:32:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 09c7622f-4f25-3142-b8e5-a8d9eb52832f | -1.49913 | -54.95564 | 2024-11-30 01:32:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| b559dff4-fba5-39ea-b5dd-c7ec9104f3e1 | -3.40571 | -53.03799 | 2024-11-30 01:32:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| a8ba148b-206c-3eb1-9538-9cc5089a1b82 | -2.59266 | -53.99278 | 2024-11-30 01:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 39a9fb33-6af5-3f4f-af7e-c4fdd441d8cc | -3.11513 | -53.10036 | 2024-11-30 01:32:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ae40fa95-8c8b-36a0-93a0-d2d4a424eb29 | -3.23814 | -53.9271 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| e9697f33-223f-3bfb-8ea4-785e3a5af07d | -3.19019 | -54.33326 | 2024-11-30 01:32:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| a47c736b-7870-351c-ab0f-350a3be07c74 | -2.52022 | -48.49175 | 2024-11-30 01:32:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| b490e583-f75b-3e44-a508-fc47a0df9539 | -3.49954 | -53.82785 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| fdc74b77-c838-3a8c-89a6-76bd87aa9065 | 0.98587 | -50.13133 | 2024-11-30 01:32:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 25.4 |
| eec17b4e-db8e-3403-8e41-442a74ef9e2e | -3.15992 | -53.24127 | 2024-11-30 01:32:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 49fea4c6-ce2f-3bba-86ec-3e7736338941 | -1.27095 | -54.56459 | 2024-11-30 01:32:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| e8c57ce7-1e86-3032-8d3e-695775851b0f | -2.89503 | -54.17107 | 2024-11-30 01:32:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8a774c56-a31b-398b-802c-c1eef1847ad9 | 1.19422 | -56.00879 | 2024-11-30 01:32:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2050d250-e73c-3d61-b8af-b7b544bafb88 | -3.25407 | -53.64775 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 716d73e8-8e76-3029-b991-a3c6acaf37bd | -1.3305 | -55.85929 | 2024-11-30 01:32:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ea49f0b5-b9cc-3e0f-bc2e-74a5210fe59e | -4.11028 | -54.41281 | 2024-11-30 01:32:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b37afac5-c431-30a3-90fa-1d7574779884 | -3.35975 | -49.77518 | 2024-11-30 01:32:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 0a188eea-34c9-36ba-a6d5-d7314de00451 | -1.62137 | -53.87529 | 2024-11-30 01:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e69b3f3c-075f-3bd3-81e6-67c4725bb8a9 | -3.25194 | -53.63297 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 149.8 |
| 6951799b-69c0-3435-bb7b-669418748203 | -2.62111 | -54.2075 | 2024-11-30 01:32:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| fccbfdf1-3be0-3673-80fd-4d6f44bf3392 | -2.61026 | -54.2091 | 2024-11-30 01:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 67fb98e4-96cd-3757-8f9c-7791e0bc87d2 | -3.49448 | -53.80651 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 05f5a15e-78b2-35d2-858f-e1805f7c65fd | -3.35537 | -49.74534 | 2024-11-30 01:32:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| a6b54157-2887-302f-afcc-1cb99733e901 | -3.3009 | -51.10806 | 2024-11-30 01:32:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 5f90ffff-7f74-3c3e-b1f0-96b6aeecf8c3 | -3.14334 | -53.83125 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 3f0e31a4-fd64-3418-93f3-907d08224223 | 1.20227 | -55.95031 | 2024-11-30 01:32:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d2a8c165-cffc-31cc-b945-5ec072509a1b | -3.92739 | -53.85486 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 04f01026-e985-38d9-ae11-f54f40c08775 | -3.82446 | -50.13874 | 2024-11-30 01:32:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| f07e284f-4681-3117-b1d4-fab3c159fc22 | -3.08565 | -51.41413 | 2024-11-30 01:32:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 770cb3d2-e24a-3d57-bcb5-e4e0623017e4 | -2.91968 | -54.2633 | 2024-11-30 01:32:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 1388589b-c0b6-323e-b041-4027b3bcbb68 | -1.60782 | -55.43824 | 2024-11-30 01:32:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1750303d-219d-32f0-a5d4-79ccb187f3ab | -2.02971 | -50.78195 | 2024-11-30 01:32:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 5aeafea6-ca9a-3ad8-834e-6b0b3cee575e | -3.60324 | -49.98651 | 2024-11-30 01:32:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 9faafca8-159b-3bb0-a23a-098898ca9541 | -3.23492 | -53.91923 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 36c8745b-f884-3595-b044-122064c4e5f0 | -1.99691 | -52.10997 | 2024-11-30 01:32:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 18f0b703-5d32-36b2-ad87-592bcc70c6aa | -1.43775 | -55.24612 | 2024-11-30 01:32:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 5c94c013-52cc-34a0-aba8-f11080beba07 | -3.48432 | -53.80131 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 1ee8c8a0-6073-3f8e-aed5-c244a52f8130 | -2.98398 | -53.29534 | 2024-11-30 01:32:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 81107346-c889-32fc-b82a-c7bfefbc8653 | -1.35875 | -55.18948 | 2024-11-30 01:32:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| abbe1d35-ce77-3e9c-904b-2dc9c7b1c194 | -2.51424 | -48.45301 | 2024-11-30 01:32:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| f81b0918-cc25-31ac-aec9-d13c94383680 | -2.36543 | -55.87602 | 2024-11-30 01:32:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4cc281d0-aeb6-32b5-986a-2efef56d6315 | -0.99727 | -51.72549 | 2024-11-30 01:32:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 16.1 |
| aaadbac0-1825-3188-96a5-8984de53084d | -2.57463 | -51.84042 | 2024-11-30 01:32:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| fbba949a-d748-36bf-85d3-109b7c898971 | -3.3781 | -50.82304 | 2024-11-30 01:32:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 1469ad73-2125-315c-a725-2d65cfc8860b | 1.19055 | -55.96056 | 2024-11-30 01:32:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 38f0c41b-e3c0-3e76-9671-5dbb73bed299 | -3.44194 | -59.2886 | 2024-11-30 01:32:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 7b3c4ef6-492d-3818-9173-fb60b665c161 | -1.19723 | -53.87534 | 2024-11-30 01:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| e06250d4-29eb-3337-9bc8-312b6fd9ee98 | -3.07636 | -50.32967 | 2024-11-30 01:32:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| babcf481-1f41-3101-9a02-cfaf9747a14f | -3.22661 | -54.17307 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 21c14ce4-2c27-3460-8a69-0925b6882869 | -3.30687 | -54.16874 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 0f481d1d-9497-3672-83a9-72ef616ddebd | -3.42741 | -53.88721 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 6713a48d-5aea-319b-a899-a762c02e4777 | -2.90373 | -54.78152 | 2024-11-30 01:32:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| eb884d4c-5333-3aab-b5c6-5bfcd8e06689 | -3.46036 | -53.88243 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| bf0b33f6-4cec-3e0f-9e50-96c27cd7fd90 | -1.7043 | -52.44011 | 2024-11-30 01:32:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 64fcfac5-5522-3c09-819f-4cc9dfae5986 | 1.21566 | -55.92817 | 2024-11-30 01:32:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 664b9cf1-5e6a-3b77-acbd-f776da27952d | -2.37648 | -54.32376 | 2024-11-30 01:32:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 17f69d29-5287-33ca-951b-128cc819b026 | -1.24742 | -54.55414 | 2024-11-30 01:32:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 77541ea8-ea75-3496-80b8-721d91281272 | -2.62497 | -51.74127 | 2024-11-30 01:32:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 974d9e52-cfad-3f6e-815e-108d7d2d3831 | -1.63263 | -53.87316 | 2024-11-30 01:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 8c0b420e-ca13-3db3-8628-674ae3aeb507 | -3.25887 | -51.61901 | 2024-11-30 01:32:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| a42c611a-127b-3bc6-bc2b-e15668ce7f99 | -2.51204 | -48.46048 | 2024-11-30 01:32:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| c20874b1-42f5-3278-8fc8-6d742d724650 | -3.78564 | -58.97775 | 2024-11-30 01:32:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| beb42ae3-a8b4-3921-aee5-09a54e42a1e4 | -3.48341 | -53.80795 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 160.7 |
| d3d9540f-cfba-30ab-8f0e-c191a874f3a4 | -3.76967 | -50.17493 | 2024-11-30 01:32:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| defe106f-a49e-3178-8ca2-9dfa4a0d4f0f | -2.76808 | -55.32703 | 2024-11-30 01:32:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e7fd22f6-7f91-39bb-907e-8b02f2b4f1fa | 1.71442 | -55.79622 | 2024-11-30 01:32:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 2e01e0a2-6b8d-3e3f-ae42-9c3167e7e3a7 | -2.57613 | -55.99504 | 2024-11-30 01:32:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bbfed506-6e76-3fce-af3c-e00c6e2e50b4 | -2.62802 | -51.76247 | 2024-11-30 01:32:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 4d7f6d4a-d8e0-3039-8973-2c05005cd047 | -2.62545 | -54.21423 | 2024-11-30 01:32:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 83072840-7843-3792-a565-36f1d1826f03 | -3.15441 | -53.82951 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 45fd286f-a0b5-3aa3-962f-ce04850bd9fd | -2.44684 | -53.62129 | 2024-11-30 01:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 2c9d89d1-195e-3e23-be3f-db0348907229 | -1.00414 | -51.73092 | 2024-11-30 01:32:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 6fb1c0c9-3507-3a8f-bd83-1f80a175a8e1 | -2.03065 | -52.07853 | 2024-11-30 01:32:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 7ca854ab-c844-39be-aa2a-dc6dac52c321 | -3.72743 | -54.23189 | 2024-11-30 01:32:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 3f95ac0b-d445-3155-9bc1-695a0eb8f62b | -2.33201 | -54.49907 | 2024-11-30 01:32:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 284b169a-2eb1-3dbe-9595-2cc0ce6b332f | -1.35031 | -54.63119 | 2024-11-30 01:32:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b5c470fe-70a1-3f85-9fb1-3cd27a060fab | -2.60089 | -53.98363 | 2024-11-30 01:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 32af3d4b-05bc-3f41-902d-991477755ee1 | -1.44124 | -55.12225 | 2024-11-30 01:32:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e01f200b-d414-307c-b8b4-c8a51712696f | -1.09504 | -53.40192 | 2024-11-30 01:32:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 4500192f-72f0-3894-82ff-dc848808587f | -3.48541 | -53.82198 | 2024-11-30 01:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 347807d4-b5e0-33b4-9bda-f55826da8251 | 1.21403 | -55.93993 | 2024-11-30 01:32:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| be37d83c-f330-3719-9c19-b573f04cc494 | 0.97838 | -50.13564 | 2024-11-30 01:32:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 27.2 |
| ea129a7f-8abe-3886-9398-918016212711 | 0.93938 | -50.76261 | 2024-11-30 01:32:00 | TERRA_M-M | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 0193acd3-6ff6-3ad2-bb87-2e211ccb7b55 | -3.11961 | -53.26915 | 2024-11-30 01:32:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |


[Clique aqui para ver as próximas entradas](README8.md)
