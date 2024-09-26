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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59f1a01e-238e-340a-afc5-708fbf22c4a1 | -9.1032 | -61.3343 | 2024-09-26 04:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| a6f81fdf-67af-3f26-89b7-60c6a8e5c31e | -9.103 | -61.3534 | 2024-09-26 04:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 4cef858d-96a7-3df1-9084-6437a9bed977 | -9.086 | -61.1245 | 2024-09-26 04:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 26a4bc2c-c206-3f2f-b1ce-f8d07fedb381 | -9.1219 | -61.3143 | 2024-09-26 04:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 7585d39e-51e0-3b82-bc3e-792b0a4c6e0c | -9.1217 | -61.3334 | 2024-09-26 04:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| cf0e4b37-ae33-3d96-aba6-f80c184390ff | -9.1216 | -61.3526 | 2024-09-26 04:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 722526dd-1c7a-369a-a610-533d1405782d | -10.7115 | -60.7312 | 2024-09-26 04:36:07 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| ec779372-5d9a-3184-9379-05d64a93629a | -11.2788 | -65.2793 | 2024-09-26 04:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 28b275cf-0fdb-3086-ae34-5bf4d28cc574 | -11.26 | -65.2801 | 2024-09-26 04:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 369626a3-4cde-3839-838a-cf2b3b8b636c | -11.2599 | -65.299 | 2024-09-26 04:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 91.3 |
| bfa7d4c4-a5a2-3e2b-a513-109df06abb48 | -11.955 | -60.363 | 2024-09-26 04:36:14 | GOES-16 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 33aaa73c-cfc9-3a2b-9f85-70dfe124913c | -13.5064 | -57.2552 | 2024-09-26 04:36:23 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| d28103d9-b392-3021-9a74-30185658403b | -13.4873 | -57.257 | 2024-09-26 04:36:23 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 6ed28ccb-d35d-3897-aa5c-22498733a62a | -6.9306 | -63.1053 | 2024-09-26 04:45:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 38.3 |
| dada41a8-daae-325e-920b-f75f87e12d2a | -11.2786 | -65.2982 | 2024-09-26 04:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 43.5 |
| b81c4b37-d4d7-352b-b5e9-c95aed2550b6 | -11.26 | -65.2801 | 2024-09-26 04:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 9d8999b7-9cf9-340c-adef-eaec30065c49 | -11.2599 | -65.299 | 2024-09-26 04:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 1a541cf4-806d-3114-b363-581efcd175a6 | -11.2788 | -65.2793 | 2024-09-26 04:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| c3effd45-7810-33a8-8af1-47966e8048c5 | -3.8002 | -41.59419 | 2024-09-26 04:55:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 158d6cf3-6c00-3a57-a1ef-ebd10ef4c477 | -3.79944 | -41.5994 | 2024-09-26 04:55:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3c92d4d6-5ed1-33e8-8ed6-da4cac4e626f | -3.79606 | -41.58829 | 2024-09-26 04:55:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| ae8883aa-8f4f-3229-b953-3dfb53709049 | -3.79532 | -41.59361 | 2024-09-26 04:55:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 008bebe5-480a-3d72-bf49-966c76fb007d | -3.79459 | -41.59883 | 2024-09-26 04:55:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e5f7745d-a599-3f76-ba26-cf3244a3175b | -3.79455 | -41.58812 | 2024-09-26 04:55:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ff826560-ffe4-3a59-80e7-e6eab83c1d57 | -3.79377 | -41.59344 | 2024-09-26 04:55:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8ba304ef-9afd-34e1-8a92-3da0c5228a4b | -3.53626 | -43.55663 | 2024-09-26 04:55:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b47e2034-4709-33e5-9274-4a5ae0beea82 | -3.53262 | -43.55797 | 2024-09-26 04:55:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6cd41075-f08f-3261-8922-b313d29ecc5d | -3.30082 | -43.52058 | 2024-09-26 04:55:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5a444eae-ca56-3735-a710-d22aa85b87f1 | -3.29891 | -43.51833 | 2024-09-26 04:55:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb794c4b-0f73-3d70-ac22-4074f2e692e0 | -3.29836 | -43.52215 | 2024-09-26 04:55:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 759f784f-04b7-37b0-91b2-2272069a9b00 | -3.20068 | -43.88913 | 2024-09-26 04:55:00 | NOAA-21 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce3b2167-5d56-3ece-8d32-403071571650 | -3.1952 | -43.88832 | 2024-09-26 04:55:00 | NOAA-21 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3c11288-bc4c-3f3c-9c92-28cd955a3738 | -1.17048 | -46.86148 | 2024-09-26 04:55:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73c0e8b3-b505-36d9-80b7-f3e154ca28f0 | -2.7341 | -46.77776 | 2024-09-26 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| acf4b5f3-ffa8-39f8-af15-fe16f30e38b1 | -2.73343 | -46.78224 | 2024-09-26 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9bf33552-e3c4-3d98-b78a-ed101de43855 | -2.7316 | -46.76376 | 2024-09-26 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2100e70c-9050-3f79-bac3-7c8792ddf886 | -2.72879 | -46.76163 | 2024-09-26 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9847b6aa-d5e3-3d54-91ae-eb44a7f83e18 | -2.72811 | -46.76604 | 2024-09-26 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4eb79ace-79b6-388f-a0fc-a74799190ffc | -2.72714 | -46.76307 | 2024-09-26 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 050b880c-fb86-3a99-b21c-b220ee781d19 | -2.72464 | -46.74897 | 2024-09-26 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9dc2bd66-7185-3013-9958-1bc8eb0d33e2 | -2.72213 | -46.73493 | 2024-09-26 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 529e48b4-4a7d-342a-bd0b-c25da65eb1e9 | -2.72194 | -46.74686 | 2024-09-26 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 469f8e42-0411-3baf-95ad-10d17b56c8ff | -2.72125 | -46.75131 | 2024-09-26 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 270dd40d-859b-384d-a15e-0c33ef22ef7a | -2.72018 | -46.74825 | 2024-09-26 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 06c1df13-b8fd-3a29-8689-13a93ac58fb0 | -2.71952 | -46.73289 | 2024-09-26 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a2723906-5ad2-3f89-9c04-42fb32a9ba6a | -2.7183 | -46.72979 | 2024-09-26 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9a623582-f7c3-3fe7-a720-ae265c59f456 | -2.71765 | -46.73425 | 2024-09-26 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bdd51e9b-54ea-3cbc-b8d9-17d8436686a0 | -2.71504 | -46.73222 | 2024-09-26 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b4379a4-9dcd-3767-b850-61e69b0f7dcb | -2.71436 | -46.73666 | 2024-09-26 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 06d79910-46ca-3b99-879b-0f40b54785c9 | -2.71404 | -46.7684 | 2024-09-26 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66e5e116-9871-3ad4-bbc3-e5e0cc5425ba | -2.71335 | -46.77284 | 2024-09-26 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17b4e588-08f6-3ee4-bedd-eef5845f58a4 | -2.70957 | -46.76773 | 2024-09-26 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| de83fda2-9b50-37b5-92bf-b32482805da7 | -2.68304 | -46.73201 | 2024-09-26 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7a5955df-00c8-32fa-af06-41bfe0683ba0 | -2.68235 | -46.73652 | 2024-09-26 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 769fac0b-8155-3aba-bb1f-aa11c8f7aeb0 | -2.68168 | -46.74095 | 2024-09-26 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 504e642d-c501-3ac2-b4e4-1df5dc41cea3 | -0.72842 | -47.52565 | 2024-09-26 04:55:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a92e3ecd-06a4-3634-8889-835afd823536 | -1.93782 | -47.90221 | 2024-09-26 04:55:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16a114e8-c550-3d32-b812-734b52b27a1d | -1.9109 | -47.88683 | 2024-09-26 04:55:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84c8929a-8be8-320a-a262-e48c55d1ef20 | -1.90391 | -47.87925 | 2024-09-26 04:55:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a467759-fe30-3349-8d49-131f1ec78368 | -1.42268 | -47.41038 | 2024-09-26 04:55:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb1f5b3b-5824-3a1d-b2ff-e89629663feb | -2.92328 | -47.83212 | 2024-09-26 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| adc495b4-49f3-3fcd-af11-4f377de96d24 | -2.89818 | -47.88619 | 2024-09-26 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adb9385b-0e67-3944-a8a9-2d93daf1610f | -2.89762 | -47.88998 | 2024-09-26 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 271da723-4d1e-39ff-a9eb-f6cd6added99 | -2.3555 | -47.60165 | 2024-09-26 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ab0398b9-407b-328e-9f45-bc08d72a7c64 | -2.35491 | -47.60548 | 2024-09-26 04:55:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6fc76bae-d215-3ba2-abbf-fe39dff9a7ab | -2.35432 | -47.60927 | 2024-09-26 04:55:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e7a2bc5-0689-346b-9614-94840ebf9954 | -2.35131 | -47.60099 | 2024-09-26 04:55:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cad857e1-6caf-3a6e-9964-3f47ee76e069 | -2.35072 | -47.60482 | 2024-09-26 04:55:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 57014dfc-e3c8-3618-9350-00ac35c63a1d | -2.35013 | -47.60863 | 2024-09-26 04:55:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a80ecd7-a3d4-31b7-98cc-2de802d2ca7a | -1.18586 | -48.8164 | 2024-09-26 04:55:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f31b856f-5c0f-3488-bcb7-c690cf15d498 | -2.62119 | -49.11315 | 2024-09-26 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c036d54-6467-35a8-ac27-e8acd1538e7c | -2.56599 | -49.12112 | 2024-09-26 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afc3294d-9805-3973-9214-94b8effcab8e | -0.50656 | -50.68357 | 2024-09-26 04:55:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d0c0c7e-a857-30a9-a881-5412cd80a9d8 | -2.40731 | -51.30516 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 533a6ca4-3358-321a-96b0-bc46f4b904aa | -2.40619 | -51.28984 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b328b79f-0ce7-31f1-bf6d-6c349fb1d83c | -2.40562 | -51.29355 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec6e2604-9456-3c25-8842-5610b3003d99 | -2.40335 | -51.28563 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8410d7b2-1047-3806-bd18-0200aca22c82 | -2.40332 | -51.30833 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20ae8441-4a17-3682-80c5-4274463cc5a4 | -2.40277 | -51.28933 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b60950f2-2deb-3db3-b76a-25e65b389f79 | -2.4022 | -51.29303 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3a5ce88-bdcd-30a5-8f54-c52f23b2304a | -2.40108 | -51.27768 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b7593bd-0d70-3e7e-b7d3-dec0807d36ff | -2.4005 | -51.28139 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ab7bd1a-7405-3192-9a87-fb6307c25793 | -2.39993 | -51.2851 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1730b115-512d-3c27-8385-1be4a707b0d1 | -2.39936 | -51.28881 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f109c586-b06a-30de-8b2f-7b643e97cbe3 | -2.39878 | -51.29251 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74319a38-e90b-311b-8a6c-b53ddc1f36d0 | -2.39708 | -51.28087 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b8e7671-841d-3e06-8c52-66091bc6b31c | -2.39706 | -51.30359 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbaae3f8-6462-3b9b-868b-3553a8336e50 | -2.39651 | -51.28458 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a195585-1361-32b0-893b-7bb6eda5a32d | -2.39594 | -51.28828 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46220b3d-d43b-3157-a8b1-e72830dd003e | -2.39537 | -51.29198 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1d2aec5-437b-3d9d-a28e-e6352aeff195 | -2.39479 | -51.29568 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 662f2ecd-7119-3b8d-a395-05af8a45d07b | -2.39422 | -51.29938 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 373ee335-4af8-395f-803c-0d9e191693c0 | -2.39367 | -51.28035 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 718dde53-6e04-38d6-bb09-168c065cbca1 | -2.39365 | -51.30307 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bf2452b-6407-3ccb-8cc4-ac14ab035fea | -2.39309 | -51.28405 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e26b01c-9c0f-3654-8512-422997b70114 | -2.39252 | -51.28775 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66d64436-f2ff-3ae4-b094-8263714549d8 | -2.39025 | -51.27982 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19791628-c7f3-3f0c-a67f-c98e789effd8 | -2.38968 | -51.28353 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd92c3ec-78ae-3be0-be6e-93239cec02a6 | -2.3891 | -51.28723 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c929ffe-4663-3c48-8e0d-8c111d988ba3 | -2.38683 | -51.2793 | 2024-09-26 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README88.md)
