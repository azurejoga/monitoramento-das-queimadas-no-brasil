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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 737deec9-69c1-3e64-b889-e6c63b8de146 | -4.4053 | -43.4978 | 2024-11-01 01:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 4458f5f5-e927-34dc-854f-4d34114b48c9 | -4.4054 | -43.4746 | 2024-11-01 01:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 324.9 |
| 7d18b0dc-8543-31e7-a12a-602fd02d2534 | -4.4056 | -43.4514 | 2024-11-01 01:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 20ac7b21-bd12-390b-bb2d-51f0e34fa1d2 | -4.4554 | -44.3477 | 2024-11-01 01:05:31 | GOES-16 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| d5f579eb-7d95-3573-b3ee-e3855e99ae5d | -4.4555 | -44.3248 | 2024-11-01 01:05:31 | GOES-16 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 123.9 |
| e8548f3d-e0cf-3cc2-a87b-9042e14c2713 | -4.9023 | -47.0577 | 2024-11-01 01:05:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 5e7835ff-4a17-3934-b75f-d456221689da | -4.9024 | -47.0357 | 2024-11-01 01:05:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 70.1 |
| a7af6c00-5241-3d3a-8090-74b9e5c55843 | -4.9209 | -47.0566 | 2024-11-01 01:05:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 91be3555-88cd-3e8a-8ffe-98625a0e74ee | -4.9211 | -47.0346 | 2024-11-01 01:05:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 8c2d67e4-47d1-3777-83df-b215dff013c4 | -6.1039 | -43.9824 | 2024-11-01 01:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 296a42dc-39a5-31ba-bfa1-9a15fb7d141b | -6.1041 | -43.9593 | 2024-11-01 01:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 184.0 |
| 92bdb8aa-3647-38cb-9d7b-9e3bb9f3751f | -6.1043 | -43.9362 | 2024-11-01 01:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| bf3eaff0-6da7-3e3d-9868-fe90887f5f0d | -6.1226 | -43.9809 | 2024-11-01 01:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 691e7e8a-f502-3e1c-9749-0ce7b1deb7d7 | -6.1229 | -43.9578 | 2024-11-01 01:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 170.1 |
| 8436ca9f-42a0-3451-831f-2c5bb26a92fe | -6.1231 | -43.9347 | 2024-11-01 01:05:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| b2999ba1-39e6-376a-bda8-871a1ead196a | -9.4391 | -40.3171 | 2024-11-01 01:05:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 117.2 |
| 6748c383-09ca-311e-996a-42b943551387 | -9.4582 | -40.3143 | 2024-11-01 01:05:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 121.0 |
| 690f1a80-d667-3788-848b-2fa5ff21dbc5 | -10.6819 | -65.002 | 2024-11-01 01:06:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 54802ab7-7749-346b-a392-6dd127fecfb4 | -10.682 | -64.9831 | 2024-11-01 01:06:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.2 |
| beb9a488-209a-31a1-8cbe-79beaab947a9 | -10.9811 | -45.1104 | 2024-11-01 01:06:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| c3ca0dd6-2a23-353f-8cd4-5cede9d317d7 | -16.9008 | -57.5313 | 2024-11-01 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.1 |
| 69c5f9f4-7b27-30b6-bbe2-dfeabb33cdf0 | -16.9012 | -57.5108 | 2024-11-01 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.6 |
| 037615d1-08b6-3a6e-b872-54be972b15e2 | -16.9204 | -57.5291 | 2024-11-01 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.6 |
| f92283a2-6d0c-38e9-8df3-d2ad59ee200c | -16.9207 | -57.5086 | 2024-11-01 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.2 |
| ea3544d2-a531-33ed-b17c-5455be39a88e | -17.6467 | -57.5051 | 2024-11-01 01:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.8 |
| 8d50e34c-d444-3868-bd2f-affc62c755d9 | -17.6664 | -57.5028 | 2024-11-01 01:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 138.9 |
| 4aac063b-5f82-3dd2-8566-82512fddf9ad | -17.7249 | -57.5368 | 2024-11-01 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.8 |
| 78b3de81-ba5c-3273-a9c2-cbec8e92aa67 | -0.6896 | -51.6847 | 2024-11-01 01:15:10 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 67.5 |
| a8bee6e6-aa22-3b92-acae-a348c8f046bf | -1.8654 | -52.3282 | 2024-11-01 01:15:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 9ee291ce-4bcb-3e2b-856a-34fae98b6061 | -1.8654 | -52.3077 | 2024-11-01 01:15:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 8a25dea4-5acd-35c7-b4cb-1c74105f9ecc | -2.1695 | -48.7252 | 2024-11-01 01:15:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| dc18f9e8-acda-366e-951b-baafd33d2021 | -2.188 | -48.7248 | 2024-11-01 01:15:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 110f2302-c7c1-327a-90f4-3f41fb8797ec | -3.0538 | -49.4895 | 2024-11-01 01:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 216.8 |
| ee764e47-83a1-325a-8dba-01c27a72096f | -3.0354 | -49.4688 | 2024-11-01 01:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 178.5 |
| 6a5fb1be-98d6-324b-9505-c33b312fa0ee | -3.0539 | -49.4683 | 2024-11-01 01:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 210.7 |
| e9164885-6348-33b4-a235-941084fb1316 | -3.0723 | -49.4889 | 2024-11-01 01:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 348c3a3c-a16e-3b88-b6da-ec36ee6415ab | -3.0723 | -49.4677 | 2024-11-01 01:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 0005306e-67d0-3b20-bec0-c87ada84782b | -3.0353 | -49.4901 | 2024-11-01 01:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 185.6 |
| 57c8b3d6-e78e-3173-851c-cda39b0b1673 | -3.5103 | -43.3127 | 2024-11-01 01:15:26 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 01958bc2-09d0-3e94-8113-94c009af1317 | -3.5446 | -47.3855 | 2024-11-01 01:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 19961db8-00cf-3bd0-9acd-45e80715c89d | -3.563 | -47.4066 | 2024-11-01 01:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| f40d89fe-51f1-3fd2-8f62-ba67515f20fd | -3.5631 | -47.3847 | 2024-11-01 01:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 313.4 |
| 792c7d46-5eb0-3373-9b4c-28ccf66b62a1 | -3.5632 | -47.3629 | 2024-11-01 01:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 121.7 |
| f0d84551-1749-3a21-a453-e4f84414c2f8 | -4.3866 | -43.4989 | 2024-11-01 01:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| a6b2b2e8-6543-3ac0-aae7-676058890a51 | -4.3867 | -43.4757 | 2024-11-01 01:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 243.3 |
| 4dd80b4c-7578-368a-86b4-7d7891e86b5e | -4.3869 | -43.4525 | 2024-11-01 01:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 27dc4d84-b1a8-3424-ab18-d1b35a313463 | -4.4053 | -43.4978 | 2024-11-01 01:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| b5bb706d-2e4a-39d2-8d7a-fa292257a59e | -4.4054 | -43.4746 | 2024-11-01 01:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 251.4 |
| 04841ab1-850d-3b38-8494-a6a158d17608 | -4.4056 | -43.4514 | 2024-11-01 01:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 7f25f0f4-9cf9-37b4-a9e4-94aa291d0292 | -4.4555 | -44.3248 | 2024-11-01 01:15:31 | GOES-16 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 74bf88df-b4f2-3c79-be16-74a756d873e9 | -4.9023 | -47.0577 | 2024-11-01 01:15:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 76.9 |
| bb3ff50f-9cdd-322b-ac4d-30dada0ac398 | -4.9024 | -47.0357 | 2024-11-01 01:15:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 80.1 |
| a6688502-8bca-34c4-a2e7-b3aa32378a90 | -6.1039 | -43.9824 | 2024-11-01 01:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| d4a10fd4-3b98-3522-b87e-9a04ab83a544 | -6.1041 | -43.9593 | 2024-11-01 01:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 126.2 |
| d73956ee-0c63-3b03-8958-4d9911cacf19 | -6.1226 | -43.9809 | 2024-11-01 01:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 7e9703d9-b489-3a3b-ad8f-9d6501af15d2 | -6.1229 | -43.9578 | 2024-11-01 01:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 172.1 |
| cd54940a-af67-32ce-b6aa-0a8c0f77f48d | -9.4387 | -40.3419 | 2024-11-01 01:15:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 201.7 |
| def3fd31-8802-35e1-abf9-365f29cfe429 | -9.4391 | -40.3171 | 2024-11-01 01:15:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 427.4 |
| 1ba67a5e-f358-37b2-b81f-e6bfa95e31fd | -9.4578 | -40.3392 | 2024-11-01 01:15:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 162.0 |
| 3bc3535c-9d3a-3de0-a227-2a3cd7c8219c | -9.4582 | -40.3143 | 2024-11-01 01:15:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 293.2 |
| affa721e-1ce1-32c2-8991-9de234cbb030 | -10.6819 | -65.002 | 2024-11-01 01:16:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 1025a787-440d-35e6-b398-730fc53f40d9 | -10.682 | -64.9831 | 2024-11-01 01:16:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 02fe81f1-8dbc-3bbb-9c1c-79fbd4265ac7 | -16.9012 | -57.5108 | 2024-11-01 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| eed614ab-b9cf-3e53-8995-36b89aeb5ca7 | -16.9207 | -57.5086 | 2024-11-01 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.2 |
| f64f4389-7d45-3167-b39a-c2db6b42e1f6 | -16.9008 | -57.5313 | 2024-11-01 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.9 |
| 8173b84d-f4b6-35dc-b3c0-783d66433075 | -17.6664 | -57.5028 | 2024-11-01 01:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 156.7 |
| b7c6e5ba-6763-30a7-9b93-dd9d914e9a4d | -0.6896 | -51.6847 | 2024-11-01 01:25:10 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 64.0 |
| b13091a9-c2b3-3666-82a0-aba61c0965f8 | -1.8654 | -52.3282 | 2024-11-01 01:25:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 9f2e35a3-a40c-327d-b038-1c0dabf7ef12 | -1.8654 | -52.3077 | 2024-11-01 01:25:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 3e44b504-614c-353b-95ec-4e6a30440690 | -2.1695 | -48.7252 | 2024-11-01 01:25:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| a8b40095-02b3-3ed2-8469-992580644cbe | -3.0539 | -49.4683 | 2024-11-01 01:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 258.0 |
| 02dbed4e-1f9e-3038-a12f-8793e019bc9d | -3.0353 | -49.4901 | 2024-11-01 01:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 215.5 |
| 19bce6ae-43d0-3bcb-a4a2-7b0e1461f2d0 | -3.0354 | -49.4688 | 2024-11-01 01:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 223.9 |
| 4d22000b-e107-3451-b870-c18fcf7e52f3 | -3.0538 | -49.4895 | 2024-11-01 01:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 241.2 |
| 4160c318-1603-351a-9b55-84d6910d7f88 | -3.5446 | -47.3855 | 2024-11-01 01:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| ee2ca8c5-45a2-3b76-8c53-0356afa2dc9d | -3.563 | -47.4066 | 2024-11-01 01:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 33e8f30a-a980-3019-8420-68026c46d9b7 | -3.5631 | -47.3847 | 2024-11-01 01:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 344.0 |
| 71461b80-f4a0-3103-b683-4babea7374df | -3.5632 | -47.3629 | 2024-11-01 01:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 5a714dab-10c0-39e3-9fba-00bbd61570c2 | -4.4054 | -43.4746 | 2024-11-01 01:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 182.1 |
| 26d8694e-46bd-30c7-aea9-723a0fe17086 | -4.3866 | -43.4989 | 2024-11-01 01:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| fc3ddf8e-203a-3ffd-a14b-11cb7dc5bd08 | -4.3867 | -43.4757 | 2024-11-01 01:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 255.4 |
| 7b78ee1f-db7d-3e70-8473-7584bb91a21c | -4.3869 | -43.4525 | 2024-11-01 01:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 34569e28-09ee-3637-85d1-fd44f3e42b21 | -4.4056 | -43.4514 | 2024-11-01 01:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| f177079d-3420-37c7-9f2c-1fd0ae379c3a | -6.1039 | -43.9824 | 2024-11-01 01:25:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 5050899f-8555-3987-b925-4f7f454a6090 | -6.1041 | -43.9593 | 2024-11-01 01:25:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 9d4a8fe7-8254-3e99-9d9d-79f02ef6cdac | -6.1043 | -43.9362 | 2024-11-01 01:25:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| abff13fb-7b4c-3685-be7f-832bbce5e76a | -6.1226 | -43.9809 | 2024-11-01 01:25:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 951f7a31-9bfc-36ef-982d-9da97164dc73 | -6.1229 | -43.9578 | 2024-11-01 01:25:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 210.8 |
| 7c1a3947-6593-37a1-9384-838988748be1 | -6.1231 | -43.9347 | 2024-11-01 01:25:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 68ca7181-221c-3dd9-b5cf-58a3c401b1bf | -6.0496 | -45.8072 | 2024-11-01 01:25:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 5ebf9f46-d823-357c-b512-8e3f6ae61bcd | -9.4387 | -40.3419 | 2024-11-01 01:25:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 320.4 |
| d7ee70c4-9424-38dd-bd11-386e9cee4c9b | -9.4391 | -40.3171 | 2024-11-01 01:25:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 723.6 |
| 12c0497e-54a3-35ad-b1a9-294a7397476d | -9.4395 | -40.2922 | 2024-11-01 01:25:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 133.9 |
| 0238f816-5983-3ab2-afa8-5aee3cf51709 | -9.4578 | -40.3392 | 2024-11-01 01:25:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 188.0 |
| fca5d1a9-12c5-37df-ab0d-d0863756475d | -9.4582 | -40.3143 | 2024-11-01 01:25:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 419.5 |
| 0ae36b93-9813-3e05-91a5-24870099b725 | -9.4586 | -40.2894 | 2024-11-01 01:25:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 90.0 |
| bba5720b-7381-366a-be7f-6a60b158e259 | -10.6819 | -65.002 | 2024-11-01 01:26:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 74d34bdb-4d55-3e51-8b98-0383fbdc28a1 | -10.682 | -64.9831 | 2024-11-01 01:26:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| b39be9fd-4ea2-3549-9dae-0e85c6ce97be | -17.6467 | -57.5051 | 2024-11-01 01:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.3 |
| 1875c1dc-50d3-3f6a-9f7f-fcd2e7d6e310 | -17.6661 | -57.5233 | 2024-11-01 01:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.7 |


[Clique aqui para ver as próximas entradas](README7.md)
