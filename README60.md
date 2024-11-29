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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4986dc5f-71c1-3235-b987-fdae0ecf32b1 | -2.62261 | -48.16666 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 590d46c2-53ff-3935-b7d0-89a0314e7e12 | -3.57332 | -53.02311 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 2325cd06-6c86-38cf-8251-22748eda90a6 | -1.0914 | -53.36559 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8d064f6-2dd4-329a-b9b2-492041fc426a | -0.33868 | -50.03384 | 2024-11-29 04:57:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a92d0aad-4c9d-3817-9525-939ff0f01cf7 | -2.64233 | -54.28214 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55cc0455-edbc-3e12-93a8-ef127e69ccd2 | -1.08586 | -53.35772 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e07758c0-ebc5-37f6-a1e3-ae318520b520 | -3.32502 | -46.69931 | 2024-11-29 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8653361c-0778-3bae-8cfc-354013ec3719 | -2.66965 | -48.79082 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f275adba-eda3-3eb8-a753-ea1e33615cb7 | -3.223 | -53.82996 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee4e7794-6dc7-3650-bb09-84886473d0c9 | -1.53692 | -52.66766 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e52f2a2e-1974-3d57-84a2-12a5edaeaf98 | -2.65283 | -54.06087 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5bc121a5-fd79-34b6-9b26-145c0c7642a2 | -1.62486 | -53.87155 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9efbad5-3688-3607-a434-2ab9d4d8984d | -2.61857 | -52.53544 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1333379a-5859-3d49-be29-32fff3debfa5 | -3.05034 | -53.71835 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eef84bb6-5306-38d0-bb31-71dc78bd2650 | -2.32101 | -50.68117 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e91d72f-84f5-3ac5-b068-2265e89a5a83 | -2.78253 | -48.10631 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8018598d-bb14-389a-b835-faab8dea1cd5 | -3.82601 | -46.53907 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 78c17ce9-3dfc-365e-8175-0def81ba3ae3 | -1.36334 | -52.53753 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a75125ed-809b-33c2-8c21-dd69fcad14bd | -3.24492 | -50.77606 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 423105f8-e36c-323e-b269-7b357cb5d8e0 | -1.18904 | -53.87399 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a01c40c-9857-34e3-85dd-f211c533eb89 | -0.02314 | -49.63513 | 2024-11-29 04:57:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4d0aedc-00f6-35ff-ac8b-931681436d65 | -2.5012 | -52.15532 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f0fe98b-8640-3778-b73d-802047806322 | -3.61405 | -54.74479 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffc91319-667e-3050-bafb-a6733c7b0d28 | -1.10582 | -54.1446 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d50da097-d596-3e8e-bbfb-7c2fd0c2ee11 | -1.26773 | -55.74316 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dccbba1c-0d40-305d-8071-2c8a896ca005 | -2.42204 | -47.60323 | 2024-11-29 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0ddc249-bc9d-3f8c-adfb-f57838051f12 | -1.20771 | -53.55568 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e5c5ac2-be52-37aa-8d4d-6910753170f7 | -2.77039 | -53.98377 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fe7b3d65-e30f-38f7-9ea4-3c67a5d26805 | -2.98659 | -51.32983 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b8ced86-6eb7-3dc0-8a4d-adf3482d2605 | -2.01895 | -52.08114 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5b9ec83-5b4f-324b-9622-6ebf63780a49 | 1.25877 | -55.91228 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe29cc2a-bcc4-35c5-a6a4-84b6f51ce971 | -1.44173 | -55.21401 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 301111fc-6eb7-38c3-a02c-cc9d0d328b44 | -1.68149 | -52.52637 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f2d844d9-cc37-3552-a08c-3a39d2f24b26 | -2.67195 | -49.86951 | 2024-11-29 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9783d98-04c0-311c-a5dd-06f8141623c2 | -3.50254 | -50.46554 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd2391b1-ed88-30ca-a69a-36b77a4e5b67 | -1.07222 | -53.38018 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e37470d-d6dd-3f17-91bc-e6ab0564eb96 | -1.56571 | -55.78771 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f09c3b78-f2b4-3853-a97e-2c7b6b0fa5b6 | -1.30249 | -52.53527 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 372dd050-75ad-324e-ab34-90bb258759c0 | -2.26009 | -53.67899 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1b96d6b1-3bd4-37be-8288-f35db6faf4ca | -2.61759 | -54.06954 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c7536a09-356a-3ea8-8c06-9dccaa9fc4f6 | -1.10702 | -51.73649 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e9639002-6d95-35db-af3d-f84fb0759e06 | -2.64712 | -47.12798 | 2024-11-29 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4a274222-f10b-33f9-934c-852514c7b840 | -1.57028 | -51.2364 | 2024-11-29 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3cc3c879-e9d8-39f9-9feb-27da7cc16dac | -2.90298 | -54.18151 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d9d30c3-5e06-30c4-8055-73e48090a169 | -3.15384 | -51.34285 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0cab3652-b1cd-3173-91d9-200b9df480ab | -3.4152 | -54.90459 | 2024-11-29 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f214d24-61e4-3233-8f50-a29800291236 | -2.79216 | -53.97736 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| faa8d20b-8e78-3013-b458-de99bb5738a4 | -2.44619 | -53.96831 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd359907-36c0-3ac0-9e77-a57ca6148e0f | -1.24264 | -53.35804 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35cc4940-4333-3a4d-9063-f8e9f007fe98 | -2.87046 | -48.09944 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ef06e41-1d4c-3cde-b586-63a45e2af757 | -3.09146 | -54.13008 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bfc6dbc-d3ba-37ad-a606-3956006175cf | -1.25911 | -52.72698 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9d06218-6d28-3658-b64c-a358e16d522c | -2.0398 | -45.69828 | 2024-11-29 04:57:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd07620a-c008-377f-9483-43026ee3bd14 | -2.19252 | -50.57693 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1eb1b89f-917e-348a-9be1-31b8df9aa68d | -2.79461 | -54.04821 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c8c9fa6-fa26-33f2-97dc-7d38e61f34cc | -3.48815 | -53.98441 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d3bd2e7-908e-356c-ac2b-45a07ed9d605 | -3.66079 | -54.42434 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70bdf0f0-ca6d-3923-b373-9a4ea253ec43 | -3.24364 | -53.63271 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6faa60d6-01a7-39fb-aec6-dcf1370ad7c7 | -1.15352 | -53.62113 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86ef3b37-025d-330b-8e6a-55ef9a9c583a | -2.45605 | -53.6883 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3ab3ea8-3c56-3ddc-bb70-9bb50253f1c2 | -1.64737 | -52.74483 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 28baf98b-ec03-3ccc-b85f-26526d044b7d | -3.04406 | -48.52174 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00fbfa6d-2be1-3a25-8787-d64f58a6ada2 | 1.86039 | -55.80993 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f7704d85-e827-3d99-a6f0-fe828493e077 | -2.83561 | -54.111 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2d00028-db89-3cfc-8aa5-54cd5db01b26 | -3.78966 | -54.62262 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d58b3c83-f5c6-3a78-b416-654d78392d4f | -1.34726 | -51.96745 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c20266d7-3db3-3f91-8807-59afacb473ea | -1.15701 | -53.40387 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ed121fd-3d38-3ca7-81b4-21d4472f93ea | -4.05866 | -46.68502 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b196c57e-d7a0-3067-8d34-30bfc5f04fa9 | -2.26749 | -53.47988 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 505ad0db-2a12-3bbc-803f-eb856a22c0b8 | 1.97657 | -60.91615 | 2024-11-29 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dea3a271-b7db-391e-a622-0c2c2e384fe2 | -2.80313 | -54.12365 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2aca493e-d1ab-3edd-ae66-dc26f7cec932 | -2.99158 | -53.354 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ee0e068-e3bb-352d-8557-f958c8349314 | -1.21828 | -54.18732 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0c75a43a-0e64-3014-b1a3-1ef8e36a6e06 | -2.01243 | -51.19474 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4be79821-5e51-3c5c-b5ab-f07aaf9061a3 | -2.88695 | -46.83823 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a4f24fe-40ab-37be-90ca-ef391668e933 | -3.38694 | -50.11479 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 83450872-9ee3-3859-9bfa-e2e6b703252d | -2.88312 | -54.00552 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 061c3f97-e1e0-34ea-ba63-b9db6ddb449b | -4.65714 | -46.54742 | 2024-11-29 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e194611-3e5a-3a2b-8153-c4d6ad83fa48 | -5.71859 | -43.83649 | 2024-11-29 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9491a32c-f521-38fb-842d-bc27e3a7a48f | -2.36481 | -53.86066 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b0d011c-ade2-3b98-a400-16646184bde0 | -3.16197 | -50.58479 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1db17b7-0cf3-35ea-8933-e3985220eca4 | -3.10077 | -53.80699 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbadb965-041f-3ec5-adb0-3ef68416182f | -1.63179 | -52.71411 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 64e5bd65-d08c-3d06-94ca-eec85d35bcd5 | -2.7335 | -54.13333 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fb50ccef-21d4-37d9-a676-2ff0ebe716ba | -2.5384 | -54.05367 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 945a7984-4774-36a8-8686-96693ba79efe | -1.68851 | -52.45963 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 87b164ba-99b8-35a9-8e9d-68b08dcf7380 | -2.46926 | -53.69033 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 328ae7ab-466b-31e4-9c93-7a3b79fd40cb | -3.19874 | -46.56886 | 2024-11-29 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 429ee60f-6d54-34fc-a3a1-29283f90d839 | -3.47045 | -50.5297 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 293ba16a-a8c3-3461-b014-ed91be57c172 | -2.29921 | -51.98857 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6ed826f3-844e-3177-ab7e-c95d727a3a4a | -1.03276 | -53.54622 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0af18ef-a5ea-39fc-bcc1-be6b194fdc8b | -1.78686 | -52.74562 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab325ad1-f9ea-3d35-82c0-587edb7ecff3 | -3.44113 | -54.06869 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 502b951a-9073-3cf6-a0b4-51eec233cff5 | -1.21925 | -53.55109 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aa1590d5-9e69-3126-81d0-e8329acf9f9c | -3.1133 | -53.27058 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 02eec179-ac8e-359b-a72c-718ff2cb5b6c | -2.19612 | -48.3432 | 2024-11-29 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f6ff663-bd8f-3da5-a1da-8c1946427401 | -2.82764 | -54.59666 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e299527d-eda2-3a9a-a4b0-6c4420038f00 | -2.88813 | -51.58638 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb535833-63e2-3961-951f-03303f57892b | -1.10256 | -53.40239 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6aae22f9-954b-3827-8974-f0581fc74026 | -1.6887 | -48.20051 | 2024-11-29 04:57:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README61.md)
