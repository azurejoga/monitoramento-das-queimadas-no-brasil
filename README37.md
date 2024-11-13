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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22b33b44-cd42-33d6-8c19-e3ad16aa4aa6 | -2.16339 | -50.65234 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 348728ad-a56f-31b8-b6cf-1c62102d9a80 | -1.9358 | -51.40844 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29f68951-1d08-3cf3-b3df-fd689508153d | -3.37268 | -51.64593 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5008d2b6-9863-3c64-80fd-67ea85b4cadd | -4.11205 | -51.10359 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63abb51d-1474-3438-bf6f-bda115f75b46 | -3.44042 | -50.30544 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 342baf5a-12da-358c-9a8f-91fa5debda76 | -2.47937 | -53.97885 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f38cd485-c667-3afc-90c2-6659157df511 | -1.8483 | -55.52402 | 2024-11-13 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ce0c27d-7cfd-3ea6-bd95-ac814e39ea4b | -2.24615 | -53.75266 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2259b85e-cdf7-3c23-b065-239aefdcb7f6 | -2.25222 | -53.75711 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1c9b58e-e164-3763-ad3e-6151efb946dd | -2.9976 | -51.45929 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| acef834b-4dfc-3e22-9ca9-a65d45119782 | -1.39464 | -51.43653 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f59a335b-2767-367d-8e32-2dfdc9a3acbd | -2.56451 | -53.97855 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec84f94d-6180-35da-bd39-07ed202a1a1e | -2.56859 | -54.03915 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4897968-c6bc-3f20-8d8a-4a5ee8a3d7e4 | -3.27966 | -53.66855 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e35e182b-98ea-3f98-92ee-10bf89c82785 | -4.2713 | -48.19922 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c68c4c74-2fd2-3c39-b1d7-756fe4c4c953 | -3.0361 | -51.10154 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4123bee3-af8e-3862-96fc-b2f857e46066 | -2.4639 | -53.68791 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc6bbe7c-af23-3353-8ff0-92d26d885217 | -0.68991 | -52.7362 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5707be6-bf82-3d80-8721-d9343ab4ae8c | -2.10121 | -48.29536 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b52ac7f2-0e0e-31a2-b4b7-819033b5176c | -2.67361 | -54.26078 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fe7f5fc-ec1c-398d-b7ac-e503558cc533 | -1.88658 | -54.20186 | 2024-11-13 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 04350f36-edc4-3840-8881-6e070c955fda | -2.56736 | -54.00366 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 84554418-ae38-3193-819c-2026f661f718 | -2.87245 | -47.9139 | 2024-11-13 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0bfb1f9-ffae-33bf-bef0-199dadfbb124 | -1.34286 | -51.42905 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbe49846-6151-32c7-be0e-b421ffd18662 | -1.6537 | -47.47455 | 2024-11-13 04:57:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d99fd0a1-bd0f-31ac-a23d-a53d07b383ec | -2.2509 | -49.33028 | 2024-11-13 04:57:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 45efeeed-1e1b-312e-8ad7-e53d22b39c59 | -3.10659 | -56.62313 | 2024-11-13 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| baf13d72-4357-368c-9206-2ac07790ea7d | -3.06453 | -50.33654 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4b1ccf79-35ca-37f1-b4e6-377f4c2a3a9a | -3.57619 | -54.64459 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f412972-b289-3a8a-a92f-0ff5bcf2c1bf | -2.7881 | -51.75146 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f401f424-43c3-36ed-8d76-5a82b324496a | -2.25053 | -53.7463 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 84bf4728-4046-32d3-b6b6-628ef6e709d3 | -0.38131 | -51.74692 | 2024-11-13 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc22ab79-9fd0-3d58-9eb1-7bd5e305bdba | -2.98751 | -51.34616 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1f1df95-ca4c-3020-8c79-7d67b360ea2d | -1.62779 | -52.65607 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da3aa453-dd9a-3a96-9fcc-524e985e0aad | -3.07753 | -50.32882 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7d9f2a8-98e1-3266-96b0-31d454cd2617 | -1.54385 | -52.21166 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcfba38d-a9c0-32d6-885e-1ac9a030b2aa | -2.76564 | -54.04152 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98511bef-6b88-3225-b298-7e4a20194aab | -3.95398 | -48.18148 | 2024-11-13 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2de450f5-b614-31c4-b24c-296544723361 | -2.05308 | -52.08324 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f961ff56-f091-3768-84d4-5f9ca73fea09 | -1.33435 | -51.41647 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a29331a5-b821-34ae-aec7-b3eb4f65bfd6 | -3.06322 | -50.34499 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f0400455-8280-3f41-a400-cb84669592fc | -3.02613 | -48.04515 | 2024-11-13 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee88e919-e4fb-3157-b29a-9afe9b87d716 | -2.37296 | -48.51347 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5be905b0-38ea-37fd-855d-3984b8be45f3 | -2.57658 | -48.1267 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1d75192-b510-344f-af52-7e34c622ae67 | -2.93545 | -48.31956 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f8b76154-05ad-3f17-8087-d3cf02f4803f | -1.3212 | -54.63823 | 2024-11-13 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e010ea4-ed2b-3406-af1c-7d51ddba7ca5 | -2.57092 | -48.4387 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48bc3072-6668-3724-9182-f480584298ab | -2.63319 | -51.89248 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c01c7e00-2d24-3613-80df-d133758f5050 | -1.55755 | -51.85818 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 104b5fa0-ef78-30b0-a7bd-6dfdb5ca6131 | -2.45509 | -48.59375 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1946f35-5fbb-3bb8-8d6c-9d55f953724b | -3.30035 | -53.12224 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58132a2d-396d-3df0-8a3b-566cf24a2bad | -1.42617 | -52.2469 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73ca5bfa-4048-3191-bd52-00286ef40ada | -4.21958 | -46.45004 | 2024-11-13 04:57:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 492db2f1-0e5b-33b4-b05f-7254f85495ac | -2.04393 | -53.95676 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| cd7cb35d-1209-3992-803f-347b6b4881bf | -3.14252 | -45.97979 | 2024-11-13 04:57:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e418b2ca-cfcb-30e1-87fc-d22c8de3284b | -4.41107 | -49.72738 | 2024-11-13 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b5f1498-7bfe-3d7b-86eb-2bb8b10a63a0 | -2.192 | -48.38513 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df6dd3cc-c992-377a-9931-e292bebb4393 | -2.16155 | -50.52594 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3429195-5b8e-3542-bf2d-53eaf4355542 | -3.25388 | -50.39711 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ef17c83f-04cb-3bfd-9f7d-9b5abb7b0663 | -4.29631 | -48.59716 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14c65720-f0d6-3f5d-9239-4e716d3d45f2 | 0.91209 | -51.94873 | 2024-11-13 04:57:00 | NOAA-21 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c15012d-ce71-3fde-b0fc-1975c65cd0e3 | -2.59445 | -54.24488 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9927e6ff-04c9-30da-bd5c-ff8e2b97218e | -2.59531 | -48.19792 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d5689a6-e15f-3487-b836-38107fa799c8 | -4.6627 | -47.42876 | 2024-11-13 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| e886084c-7c61-3d85-824f-675ffe86306f | -2.71415 | -57.34912 | 2024-11-13 04:57:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4096229-63b4-3282-8395-95f11eb14414 | -4.42463 | -45.9481 | 2024-11-13 04:57:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c7e0ddb0-ec8b-315d-a054-53a5df859b25 | -1.62354 | -52.22372 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18dbb698-9bda-383d-acdb-418bce64b58b | -4.30399 | -48.60213 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e942f53-4b91-3d80-b2b0-eaa69e5166e4 | -1.66358 | -51.35284 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19536c59-6264-31c3-acb9-0c6e4dc7645c | -2.84324 | -48.67726 | 2024-11-13 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 589f0219-c43f-3d54-b2e5-9492f3931f10 | -1.41676 | -51.11355 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b1c34af0-da89-35f6-b133-fa0d47d6e86a | -2.52821 | -47.24795 | 2024-11-13 04:57:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4baae8d8-228e-3428-a308-91bacea68653 | -4.52235 | -48.92916 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47c890d0-3be2-3ffc-8dc3-a71082101305 | -3.47225 | -51.66032 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 012b68ef-cef3-3e8b-9665-9fb01340b869 | -1.67958 | -53.82922 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a22800e-57f7-3867-be61-8283dd039cba | -1.13687 | -54.1018 | 2024-11-13 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49f4861f-2c9f-33e3-8378-9c7bbbe38ca3 | -3.14875 | -54.48494 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 9ab3498d-d8ad-3f6d-b46e-dbbc3d9d969f | -3.1177 | -53.70602 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2fb97438-33f6-35bc-bc11-159eca2ca850 | 0.90672 | -50.14118 | 2024-11-13 04:57:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c289f70-dc3a-33c3-843e-d381d7279c7a | -2.25276 | -53.75367 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d07da801-18bf-3433-856f-e3a7743cdf56 | -2.25316 | -50.51805 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 251f946e-b9d3-3bda-946e-1063e6669b55 | -2.73014 | -54.13846 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a53f1a11-7522-3f90-a98c-5a4ef6f285ce | -3.02796 | -50.96798 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2e75a27-c328-3c0c-91d0-7f4c2734c700 | -2.46548 | -48.5914 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c64ec8e-8b05-35d1-99cb-7c261ee70abe | -3.6193 | -51.36461 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d67fff7-6a66-36d4-94ee-3130691be2b0 | -2.45652 | -50.37099 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c704237-f04a-3516-bd91-c1707e23abb9 | -2.81915 | -54.09277 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08b8676d-7b1f-364b-9e7e-54ae827b8cb8 | 0.7282 | -52.01318 | 2024-11-13 04:57:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d120badf-f379-388e-9d6d-f10b71b1e103 | -3.103 | -54.30016 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b909c91d-238c-3845-afdb-ee69482c29ca | -2.55965 | -49.11368 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b54fc67c-a9e0-3c2b-befa-da083deb6e09 | -2.17656 | -50.61346 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a83d576-504d-3a7d-abd1-880130d2e050 | -2.76902 | -54.73746 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b1b1e69f-35fb-347b-84a4-ac0a32f5ca4e | -2.35975 | -53.67888 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 982191c1-cf5e-3c0a-bd02-b0fe7f6b422f | -3.89145 | -53.43359 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42090cbd-eee3-34f3-a0d7-83706e99f81b | -2.48247 | -54.06763 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae21ddce-56d0-3dd6-bea0-b39cb00ddf5a | -5.97471 | -45.35987 | 2024-11-13 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f19da37-c977-3623-9e16-8c3c7034611a | 1.1114 | -59.19118 | 2024-11-13 04:57:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 04bd39a5-57e1-37ca-be57-758fd9c97e32 | -0.97694 | -51.72544 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f4a688e8-90a6-383c-bd15-005f63f06340 | -2.58013 | -54.03033 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea913899-391b-3205-b3aa-75cbcbe22a9b | -2.19253 | -48.38158 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README38.md)
