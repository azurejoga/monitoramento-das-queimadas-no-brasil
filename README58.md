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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9086dad3-c89b-35ab-b6a4-37827b3ad646 | -3.2774 | -53.6585 | 2024-12-04 05:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 4cfd2e9d-ed30-3319-bb55-49ad1ab38e94 | -3.127 | -54.6063 | 2024-12-04 05:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 142.0 |
| d0296579-f0fe-3dae-a5f8-f01777e2f3d9 | -2.8196 | -53.0629 | 2024-12-04 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 89c48b65-501b-3ccd-a7a6-80bcdfdd8702 | -1.7545 | -52.6159 | 2024-12-04 05:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| dcb57976-4a20-371b-bc0d-0a9cefe38396 | -2.8197 | -53.0425 | 2024-12-04 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 0cf0d822-87b5-3931-b257-c35935f1573c | -3.259 | -53.6388 | 2024-12-04 05:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 634694a6-874e-3d5d-bc65-a4a8da34333e | -1.7544 | -52.6363 | 2024-12-04 05:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 4f0af37d-53cf-3a24-8a80-069eab6dbb43 | -3.1086 | -54.6068 | 2024-12-04 05:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 9b968da2-1f46-3812-a470-06e3fad251d0 | -3.1086 | -54.6068 | 2024-12-04 05:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 4068011f-a4a6-3ac4-ba74-0a0983b93310 | -1.7544 | -52.6363 | 2024-12-04 05:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| fcd136b5-6853-3e7d-81a9-be7a267a1733 | -1.7545 | -52.6159 | 2024-12-04 05:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| b62970b0-d201-3351-97b3-cf532ba46b95 | -3.2774 | -53.6585 | 2024-12-04 05:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 58b35d7e-49c3-3720-ac69-5204df1e89f5 | -1.7728 | -52.636 | 2024-12-04 05:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 7b40c448-3181-3284-a57a-b7d67f5f994f | -2.8196 | -53.0629 | 2024-12-04 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| e25f0b0e-f6fa-36da-a9b7-841b0de772d3 | -1.7361 | -52.6162 | 2024-12-04 05:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 342d8d19-5fea-348a-85de-6629d27277ab | -3.259 | -53.6388 | 2024-12-04 05:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| f5ceca06-215b-3b65-a074-512ddc16fa0e | -3.259 | -53.659 | 2024-12-04 05:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 272847aa-fd90-3235-bf19-defe57d18970 | -4.1223 | -43.9299 | 2024-12-04 05:40:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 97db2383-ecc6-36d8-8584-cfabb64ab2b0 | -3.127 | -54.6063 | 2024-12-04 05:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 167.5 |
| 0a0af537-cfcd-358e-ac72-57f380b0fde8 | -3.1086 | -54.6268 | 2024-12-04 05:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 51c4abaa-3ade-3e35-9a5c-24f8c0ddef2d | -2.8197 | -53.0425 | 2024-12-04 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 733bed1a-aba9-34fd-81b0-19ed7b22f6a3 | -3.1269 | -54.6463 | 2024-12-04 05:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| e50d9f18-ea0a-30b2-8d1b-bee4111f6ce7 | -3.1269 | -54.6263 | 2024-12-04 05:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 250.5 |
| 25cc2792-e31f-3007-bf22-8f4d17614676 | -3.29538 | -53.67092 | 2024-12-04 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d92bcbcb-503e-31b9-9d18-47a22bf00e7d | -3.12125 | -54.60202 | 2024-12-04 05:44:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| d18b1af4-7a8c-3147-b417-0710e078b702 | -1.07395 | -53.45021 | 2024-12-04 05:44:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b6500a3f-baa7-3308-b4d1-379f9f6dc407 | -2.04317 | -51.20055 | 2024-12-04 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6cf1b67f-6194-38a9-afe2-96c7f86e5e31 | -3.25821 | -53.65413 | 2024-12-04 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 748e0b98-80bd-37c2-ba59-47c134d70123 | -3.48036 | -53.79951 | 2024-12-04 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 122c629e-d06c-3638-a72d-0fc518c81e12 | -5.57429 | -45.14708 | 2024-12-04 05:44:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 8c8a337c-6b74-3b73-b1f3-4ccf1e2b0f6b | -2.23752 | -53.69156 | 2024-12-04 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 172f7b8e-84d9-3955-9452-107ccc5fa7b2 | -3.12973 | -54.61597 | 2024-12-04 05:44:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 8d8f68e6-c0d9-32e6-9dae-2fbd104fc0e0 | -1.76199 | -52.63709 | 2024-12-04 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 8d81b7f0-87a7-375d-9f83-a8f724424b31 | -3.41732 | -50.17376 | 2024-12-04 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6bf36895-dfc3-364a-b3bb-e2cc0002992c | -2.51689 | -51.80732 | 2024-12-04 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ab965410-c242-34dd-b792-2051a559403f | -2.94669 | -51.4096 | 2024-12-04 05:44:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0cdd4bd6-eead-333d-a4d9-cdf52e22ac73 | -3.33529 | -51.2057 | 2024-12-04 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cda11fe3-9edd-3ff9-899c-c7e68a23f288 | -3.24174 | -50.41646 | 2024-12-04 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 18631edd-7143-3454-9c41-80889537501e | -3.2632 | -53.62194 | 2024-12-04 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| e494cc65-2bdf-3f74-8ac9-7a9fb8665d3d | -2.87039 | -54.03779 | 2024-12-04 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2b7ace97-e3d3-3c4e-be0d-635ab24c85f5 | -3.19736 | -50.65272 | 2024-12-04 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 17aa2a95-ab99-347f-ac8b-c72701ef7d04 | -3.06044 | -53.27205 | 2024-12-04 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ebdbac89-40d8-34f7-9468-5998ec845f87 | -3.08445 | -53.37099 | 2024-12-04 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9555fddd-326c-39e0-b5fb-da5182be07bf | -3.09699 | -53.28785 | 2024-12-04 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0f8c200a-6294-3f2d-ab82-04ba27ca876c | -2.79615 | -53.05809 | 2024-12-04 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 70dab360-a10b-3f34-8e6e-d8ff9e6492c5 | -2.81502 | -53.06084 | 2024-12-04 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 775927ff-b702-31a4-9646-4ce5fc9ab580 | -2.63272 | -45.72808 | 2024-12-04 05:44:00 | AQUA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |
| be7c41ef-3d7a-31cc-8af8-db21662d82bf | -2.72816 | -51.8136 | 2024-12-04 05:44:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c28755d3-d8fb-3539-badb-2f93b874224e | -1.96567 | -51.53568 | 2024-12-04 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 93fad7d1-2f3e-37f2-804c-106be87c433d | -1.37715 | -53.54763 | 2024-12-04 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d1e58a5e-88b7-3541-866a-2c606b5ff9c6 | -2.90356 | -51.81482 | 2024-12-04 05:44:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 84d6f61c-9602-3cb1-8846-05cab4941945 | -1.68048 | -52.50798 | 2024-12-04 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 00cd649f-b346-3227-bd5b-553e180b307d | -2.80868 | -53.03926 | 2024-12-04 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 39822e86-6771-3b52-a1d6-3d03abc489dd | -3.36967 | -51.05471 | 2024-12-04 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3ada9f45-9f1d-3432-80ce-a05f1d7c6394 | -0.84737 | -52.7068 | 2024-12-04 05:44:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 07bfd248-f4f7-3669-8f8f-d60d2c571fff | -2.09196 | -46.57909 | 2024-12-04 05:44:00 | AQUA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 70212c2a-14a9-3ae7-9080-5230ba993856 | -3.53285 | -50.38667 | 2024-12-04 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e467ed08-61c8-3bbd-a6d3-9658a7631e11 | -3.81272 | -51.65643 | 2024-12-04 05:44:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0edd967c-ee8e-3c94-b228-d222d07426fa | -3.06203 | -53.26169 | 2024-12-04 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 67713fc1-b07e-30c0-a318-f587400426f1 | -2.7977 | -53.04798 | 2024-12-04 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e48f1434-a0dc-3fda-9ebf-7b7866f7b710 | -3.11668 | -53.97603 | 2024-12-04 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e2aeafee-850e-3a4a-a1b3-47da82150643 | -3.81138 | -51.66533 | 2024-12-04 05:44:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e3bf7626-b47e-3c1a-9623-220bfafb91f5 | -1.61161 | -53.82259 | 2024-12-04 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ceb8ccf7-6822-38f4-b1e0-1ab3a5293dfd | -4.26731 | -50.84719 | 2024-12-04 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 39ae5f9f-7077-30df-9c5b-830215d264ad | -1.66149 | -52.75822 | 2024-12-04 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 61497547-ace5-323e-b3e7-edac9f5a0994 | -4.26579 | -50.67594 | 2024-12-04 05:44:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f92cf8e2-a845-3ecb-a391-60d4320988e2 | -2.46262 | -53.6243 | 2024-12-04 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2db04e56-f2ad-3168-92bf-2d7fd0835604 | -2.54391 | -53.41505 | 2024-12-04 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 41736df7-0ad4-3c18-9307-0ab3d7e3974e | -3.9756 | -50.50956 | 2024-12-04 05:44:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| af781dc8-1fd3-3032-a9e7-7b57f33ca76c | -1.74162 | -52.60725 | 2024-12-04 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| be5a6675-24ae-3f11-8b9a-8838a0b7aaee | -2.86388 | -54.01338 | 2024-12-04 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ce7389b3-b0c6-3327-a1ee-1d9f9f060675 | -2.57723 | -53.67046 | 2024-12-04 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 93515a6b-46d3-34f7-8864-75d90fd6f808 | -2.79455 | -54.13841 | 2024-12-04 05:44:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 993544a4-e679-3641-8e20-94bdeae6270f | -2.09781 | -46.57361 | 2024-12-04 05:44:00 | AQUA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7f19a8c0-095b-3b34-8c51-fdbe1a8f7890 | -1.87417 | -53.30623 | 2024-12-04 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8daa90e6-8631-3097-a165-9b45e5cfa2a6 | -1.7635 | -52.62721 | 2024-12-04 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 9fb98ae7-5345-3e5a-a753-1dbe108436bf | -3.2485 | -53.65269 | 2024-12-04 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 35aaec65-31b3-3c72-9411-581eb5620ed9 | -3.25251 | -50.60372 | 2024-12-04 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 56e9d257-f303-3299-93a0-93a4066460a0 | -3.19999 | -50.63516 | 2024-12-04 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 27989826-14af-30d0-8d2c-69dc26ed1a9c | -1.7079 | -52.4523 | 2024-12-04 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 895645d7-e733-302a-9f59-fcaf81bd6866 | -2.22763 | -53.69015 | 2024-12-04 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1bfdb58a-d379-3501-91a3-3250b6f6ef8a | -3.10431 | -54.05559 | 2024-12-04 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 6c971c22-0114-3fad-862f-9866a7af3848 | -1.65208 | -52.75684 | 2024-12-04 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 05635d5d-da87-35d8-8305-97596262abef | -1.75265 | -52.63572 | 2024-12-04 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| b7dfd88d-b631-3f51-adf6-04f4b91a645e | -3.33908 | -49.76437 | 2024-12-04 05:44:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7d0d2af3-1232-33e4-8494-02d614aa4711 | -1.73229 | -52.60588 | 2024-12-04 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6adb4cf0-18fa-347e-a247-ba83c1d7542e | -3.19868 | -50.64394 | 2024-12-04 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| c0303744-017e-3044-8023-0fc4138ebddb | -3.09793 | -53.08997 | 2024-12-04 05:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 93315ad9-1059-3ebe-9e87-9ea5ba54bfa6 | -3.57417 | -50.29974 | 2024-12-04 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 282a01aa-de2c-39a1-b8fb-3d844f904b8c | -2.57044 | -54.79491 | 2024-12-04 05:44:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| a10dd1db-83bf-32f2-a43c-f90d7c68bbdd | -1.74483 | -52.62447 | 2024-12-04 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7f95df9b-928f-382a-b32d-bbbd6023add6 | -1.75567 | -52.61597 | 2024-12-04 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5671ece3-d3dc-3b53-a532-9c03664d0062 | -2.693 | -51.86413 | 2024-12-04 05:44:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 21b91dd7-20ae-335b-a739-cfcecdeacf27 | -1.58289 | -52.24439 | 2024-12-04 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 34839b32-5023-39a0-8e70-b1d98522ae7e | -3.32455 | -53.54424 | 2024-12-04 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3684ee08-60ad-3160-8cfa-4c381b59cffc | -3.84937 | -52.15268 | 2024-12-04 05:44:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 94c7bef6-320b-317c-beca-8c3fcabab605 | -3.58419 | -50.53608 | 2024-12-04 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 983319e6-1c74-38df-919d-b3016d221e24 | -3.48218 | -49.98214 | 2024-12-04 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| aff8cf8b-a0e2-36d0-ae99-5b446027b55d | -3.06242 | -54.05545 | 2024-12-04 05:44:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d340d893-7c7c-3f4b-8d50-a3262dbe36f3 | -1.64506 | -52.37786 | 2024-12-04 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |


[Clique aqui para ver as próximas entradas](README59.md)
