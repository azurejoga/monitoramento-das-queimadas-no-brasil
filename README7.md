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
| aeab1701-480a-318d-8587-581564ccf2ff | 1.856 | -55.8922 | 2024-11-25 01:01:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87763420-b0c2-3f18-a4af-1018b2e53de9 | -2.5904 | -54.048901 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 918b1e46-8c8b-3822-85b6-40743b91ddde | -1.9588 | -53.322102 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| faf78d0f-a465-3fde-a56e-40ec278b376d | -1.2253 | -51.7971 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bd29d54-c922-3475-8b8a-42b9177b789f | -2.7505 | -54.027401 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a3ea3d7-75a1-3ff1-a9a3-f0160f365ab9 | -1.8738 | -53.355999 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 707b947e-ac6e-3c13-81d0-2b6a9573632c | -0.9774 | -51.705399 | 2024-11-25 01:01:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 3ec24928-cf1b-3300-8532-97f2b85af00a | -20.255699 | -49.667301 | 2024-11-25 01:01:00 | METOP-C | AMÉRICO DE CAMPOS | SÃO PAULO | Brasil | 3501806 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8fa26ab0-1e9c-3f48-8a21-bd42bf9860b6 | -1.887 | -53.323299 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e8374ef-99dc-3a5b-8e20-5bc6bba599df | -2.8137 | -54.0779 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 416d8567-71aa-39e3-801b-b790af44688e | -1.7631 | -52.696602 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4286cfe-0b2c-31f6-bae3-ddd94d6f6414 | 1.8431 | -55.903702 | 2024-11-25 01:01:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2608ea75-b58b-36bd-8fef-21b7e15203ca | -4.6615 | -49.386398 | 2024-11-25 01:01:00 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57663cc5-d974-3a2f-8817-f26820e53864 | -3.5213 | -53.789799 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b19344c-f4e4-382c-a91b-33f79df29e86 | -0.2784 | -51.623199 | 2024-11-25 01:01:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 230f68e1-09a8-34ad-b159-eeeff079723a | -1.2923 | -51.730202 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8da5a9d-ae98-3c53-a402-1402aa70a67d | -3.4993 | -50.4492 | 2024-11-25 01:01:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13d24f60-1223-35e4-af8a-e490d406c3f6 | -2.5739 | -54.066898 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e489e19-86fb-37ab-8593-06a51ee4b382 | -2.7925 | -53.0 | 2024-11-25 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d9084c4-528f-30cf-96ea-6242197d6d57 | -4.0194 | -48.0723 | 2024-11-25 01:01:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cd40870-388b-3bc5-bb11-31aeba0dfc94 | -4.3162 | -45.889599 | 2024-11-25 01:01:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 75748c94-9bd8-31b5-ad8b-ebf1cd10d166 | -1.2317 | -51.735199 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b5ec69e-79a8-3343-a4e1-a92731a81fb9 | -2.1696 | -53.789101 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20a711ef-bbe6-3e1e-a46d-47c2cc2110ff | -2.8125 | -54.027901 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25fe3f87-7331-3def-8df4-844d6e37fc78 | -0.9578 | -51.7099 | 2024-11-25 01:01:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a2599cb0-3bc3-34b9-958c-8bcd83ca86cc | -1.0477 | -51.742001 | 2024-11-25 01:01:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 15f1cbd5-2f67-3adf-8cc6-9affcabd3789 | -2.244 | -53.6194 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 974189bb-69c0-3872-95f5-9e36ac9640ad | -2.5844 | -53.978199 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93caa9c6-1149-37bd-a2a4-cdf062414cd9 | -2.7893 | -54.061798 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa466631-5681-3bfa-a142-01e9eb922bed | -3.6543 | -50.230301 | 2024-11-25 01:01:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fabd6e9-35ae-3036-8c9d-20b810c25dfb | -1.1744 | -54.1278 | 2024-11-25 01:01:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5896e89-40ae-3e96-bbeb-cebce33e1bb9 | -2.8972 | -51.5811 | 2024-11-25 01:01:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54592eff-11ef-3180-b00d-26bd300d8cdb | -2.5797 | -53.9576 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cac1fd12-e13a-3e3e-913c-3d141f4ae6f3 | -2.8572 | -53.953098 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf344ce2-15fb-3911-b78b-2a808c2a1ad7 | -2.6198 | -54.042301 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df3c9fef-c12d-3ff1-8714-396089540c01 | -0.2451 | -51.612701 | 2024-11-25 01:01:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 960c043c-6266-3f05-b5eb-719f9691332e | -2.7599 | -54.068401 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b98b6c1-8aff-3130-bcf9-befab9abd9a7 | -2.7052 | -51.998199 | 2024-11-25 01:01:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbcdedf7-421d-3a37-ba1d-7ec4c4320d21 | -4.2582 | -48.729 | 2024-11-25 01:01:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b05f8632-f0aa-3f25-a83c-8027a82007bd | -3.6415 | -51.145199 | 2024-11-25 01:01:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c3db248-039e-3b39-baac-772892832ad7 | -2.8588 | -53.959999 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f78b6da-01ce-3d1c-9f1f-f39362a3f397 | -0.2765 | -51.6147 | 2024-11-25 01:01:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4f40b7f3-4207-38fc-b6c6-4ba3c8e05454 | 1.4137 | -55.886501 | 2024-11-25 01:01:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f047eff2-4c62-3e48-8701-a71fa6202d68 | -2.8184 | -54.0984 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb8681b0-1a3f-3a30-ab25-1eb9f14cc502 | -1.1281 | -53.612099 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26df376f-d565-34e5-bf02-231ff7e0d64d | -1.1087 | -53.3932 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9cf7e47-a8b7-3610-8c4f-5f9ca6af7c35 | -0.8211 | -51.608501 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07575ffc-c674-34c2-9553-d0b3679ef591 | -3.0713 | -50.955502 | 2024-11-25 01:01:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f1ba084-24e7-3b0f-856c-80f1c1b6ca62 | -2.6727 | -51.724701 | 2024-11-25 01:01:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 103400a2-24e8-3554-8919-c975bdac1c4d | -0.9695 | -51.7159 | 2024-11-25 01:01:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 5ac3e0d0-c8b0-3ee3-9799-c494863e6b5e | 1.8353 | -55.937698 | 2024-11-25 01:01:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bd5b1a3-4290-312a-ab77-ffaa82c80c49 | -2.7846 | -54.041302 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdeb69ec-9862-39a8-95c1-91e26fa8a7d5 | -1.0937 | -53.641998 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 166af0fa-5122-3cde-b6bc-0060e4e3f7a8 | -0.3527 | -51.5434 | 2024-11-25 01:01:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| dcaf924b-9bae-3d1d-a2c6-23629b155129 | -2.1746 | -53.766201 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a935dd7-b52f-31d6-9739-b96dd7564d29 | -2.8072 | -53.019199 | 2024-11-25 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11fe34e1-61eb-3dc1-91bb-7da8fe87ed45 | -2.7681 | -54.059299 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1b81696-9956-30a5-b200-8dfb3ec6abbf | -1.4797 | -51.960701 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1a0e8f6-fbb4-3a4c-87c9-3ddf4cec4ab7 | -1.2532 | -51.738998 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06900ef4-3d6a-323e-bab3-4690684f6616 | -2.928 | -51.758499 | 2024-11-25 01:01:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f56d8c20-fd37-36c8-8c0a-d1e92e690e57 | -2.9054 | -51.705399 | 2024-11-25 01:01:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 480d1a2b-1ece-3c63-9c97-9934f05cdf6d | 1.8348 | -55.894699 | 2024-11-25 01:01:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4143e1ae-07f3-3307-8dbb-4d6b69c4be4e | -3.0791 | -50.944698 | 2024-11-25 01:01:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78edffbe-4cdf-30af-b911-2ce1be4d8d70 | -1.2551 | -51.7472 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 545cf819-aef6-3178-a60b-e9c6af58af0e | -3.5193 | -53.826199 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 855f8a57-c380-371e-a365-537f0c77da36 | -2.2495 | -53.4641 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30f8dcf7-c83c-32c3-93c7-486d475bd88f | -3.7182 | -47.113899 | 2024-11-25 01:01:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| deab367d-7e9c-3689-8a04-f7bbe3c4ae85 | -2.8003 | -54.1096 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a26fe908-3afa-3b1e-b247-dfbfe160ec79 | -3.0362 | -54.013699 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1b0ccbc-2095-3b4f-a14e-8121dbcd7486 | -2.6162 | -54.251202 | 2024-11-25 01:01:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84930d8c-c097-32e5-8eda-191086c5748a | -2.7501 | -54.070599 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70e742ef-1e3e-3eea-bdf3-5469edf96aa9 | -3.5162 | -53.8125 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23480297-76ee-3d67-94cc-21dba5dcde4e | -1.6109 | -52.573898 | 2024-11-25 01:01:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 801bf815-a1e0-3335-b9b0-7ed2acba80a7 | -3.8018 | -51.169399 | 2024-11-25 01:01:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92553542-b121-355a-91a7-29d403870036 | -3.1116 | -53.982399 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e00648cb-0c5b-3b72-b388-bc52ccf104d5 | -3.5406 | -50.4492 | 2024-11-25 01:01:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 425db4a3-2aed-3b0c-9d3d-47771580970c | -1.0727 | -53.371201 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| babdbd5d-d76a-3a47-a947-aee9f2e63c59 | -3.5542 | -53.529202 | 2024-11-25 01:01:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93879801-74e1-3bf2-ab13-9aedf9c09e45 | -2.5919 | -54.055698 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4004aef0-051d-3d70-a76f-9c07eea57ced | -2.2424 | -53.6124 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d1d6150-2fac-3ac7-a685-dd94a8033e2f | 1.8544 | -55.899101 | 2024-11-25 01:01:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 040585a7-9fd1-3a4f-be2a-847bb7534506 | -0.2745 | -51.606098 | 2024-11-25 01:01:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 8730b0ef-aab1-3817-b061-78b163b551ec | -1.9604 | -53.329102 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc8579d9-2863-320e-a07c-aeedd9801805 | 1.8317 | -55.908298 | 2024-11-25 01:01:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1de4177a-ca50-3224-8583-2ebca868ee1e | -1.4858 | -52.522701 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37aafeec-9c5f-33b5-88e3-87c92e291c8c | -0.8192 | -51.600101 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4de1acb-02db-3b36-96f1-ef4cfc6586e2 | -4.2653 | -48.7155 | 2024-11-25 01:01:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 730404b4-a665-3153-94be-96154d3c8ba8 | -3.0606 | -53.222801 | 2024-11-25 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e260910a-0561-3108-b3bd-1d0172a3262e | -2.907 | -51.5788 | 2024-11-25 01:01:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5552cf0-6478-3d45-acb8-ad9b1a500e9b | -3.6458 | -51.3853 | 2024-11-25 01:01:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a3d88ce-e6d8-364e-8d91-fe7d68f08692 | -3.9497 | -47.995499 | 2024-11-25 01:01:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb25313c-b2d4-3667-870e-9a149bc686ce | -1.4487 | -52.451401 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7c92ce2-fc08-3099-bdf0-e0064ee2f604 | -1.2332 | -51.786701 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0aba03f5-d331-3291-8155-0867e12b0750 | -0.9499 | -51.720402 | 2024-11-25 01:01:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7ffa3ffe-325b-34e8-ae67-bf2de94fc7a5 | -3.5544 | -51.524399 | 2024-11-25 01:01:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fff5e36-4554-33d2-a2ee-ba928e0c8139 | -1.2428 | -53.393101 | 2024-11-25 01:01:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55f25eab-2119-387d-89af-47ea8ace1990 | -2.3291 | -53.8549 | 2024-11-25 01:01:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c70a8457-2c51-3c54-8244-2ffacec72cc1 | -1.2942 | -51.7384 | 2024-11-25 01:01:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1542287b-713a-3d56-8f6e-908809ae3492 | -3.25 | -53.283401 | 2024-11-25 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 536c6446-1b95-3d79-a0f2-a7861f38dca9 | -3.7091 | -52.412498 | 2024-11-25 01:01:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
