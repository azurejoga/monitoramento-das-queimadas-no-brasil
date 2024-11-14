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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b399ef61-c05c-3d2d-9439-c1b61f8e354e | -17.24896 | -57.47015 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.7 |
| 2865433f-feff-3b11-89ef-99d937a68f47 | -24.08465 | -52.12254 | 2024-11-14 04:46:00 | NOAA-21 | CORUMBATAÍ DO SUL | PARANÁ | Brasil | 4106555 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 630496c0-1588-365c-845f-e749d9e3189a | -21.84929 | -56.43677 | 2024-11-14 04:46:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 2a2429ce-455e-3848-952e-013c93cf9c7a | -23.96123 | -54.04831 | 2024-11-14 04:46:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 912cb125-885c-3166-8520-92c39adee04a | -23.06122 | -55.18506 | 2024-11-14 04:46:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c332c433-f992-398f-bfb4-272eda1e30a0 | -24.74077 | -52.13173 | 2024-11-14 04:46:00 | NOAA-21 | MATO RICO | PARANÁ | Brasil | 4115739 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bca86998-a231-39f6-a21d-c789da7dc70d | -26.92048 | -52.71222 | 2024-11-14 04:46:00 | NOAA-21 | CORONEL FREITAS | SANTA CATARINA | Brasil | 4204400 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| daf97d81-2b2f-386f-a58e-d9d32be4ddc5 | -23.10548 | -52.09532 | 2024-11-14 04:46:00 | NOAA-21 | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| b7fa65c9-34ab-3025-848d-537372b0d99c | -21.9064 | -56.46082 | 2024-11-14 04:46:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7b1b73e-ac87-39b3-9926-79083417e8fa | -21.85285 | -56.43748 | 2024-11-14 04:46:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bbece6ab-76f5-368b-ad9f-c968f6d75332 | -23.04198 | -47.85813 | 2024-11-14 04:46:00 | NOAA-21 | LARANJAL PAULISTA | SÃO PAULO | Brasil | 3526407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 076191c2-20a7-342c-8a43-ebe5504495d8 | -21.90716 | -56.45649 | 2024-11-14 04:46:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 009feddd-6254-3513-8bc3-79c03305b06f | -23.59312 | -47.43921 | 2024-11-14 04:46:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 44bb18c7-4e4b-32dc-be16-eb542a5344ec | -21.50971 | -57.92236 | 2024-11-14 04:46:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 0a3e7e86-0f2e-39bc-afb7-3843374a0b34 | -24.24387 | -50.74039 | 2024-11-14 04:46:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e0f5aace-e7fd-3208-9e03-f695a33564d0 | -29.13356 | -54.89383 | 2024-11-14 04:46:00 | NOAA-21 | SANTIAGO | RIO GRANDE DO SUL | Brasil | 4317400 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 63cd680b-3d8d-3306-bee3-0d06ee2af26e | -24.91834 | -53.44187 | 2024-11-14 04:46:00 | NOAA-21 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3429519e-b1ed-3d9a-9009-948b7925753b | -21.85174 | -56.43631 | 2024-11-14 04:46:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6faf0ab9-c99e-3f7f-9e18-c898467a03ca | -22.68563 | -50.47484 | 2024-11-14 04:46:00 | NOAA-21 | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 11621875-4d3a-3271-a6ac-acf6e1e97a02 | -29.77937 | -51.17759 | 2024-11-14 04:46:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| ef46200d-a9b6-38e9-90af-a50baf99f7d2 | -23.96182 | -54.04455 | 2024-11-14 04:46:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| 108f214b-b734-3def-a73e-d249c0b5129c | -28.58797 | -49.44336 | 2024-11-14 04:46:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d3e9c47c-cd11-3af2-ae54-7530277b40b7 | -1.8106 | -52.1652 | 2024-11-14 04:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 125c2f7a-f2f7-3256-9ccf-fbf3b27a7435 | -1.6246 | -53.268 | 2024-11-14 04:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 6432842a-577e-3084-8868-be07db1398ba | -17.6066 | -57.551 | 2024-11-14 04:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.0 |
| 290a6dab-0e79-31dc-b341-81dbca7523b0 | -2.2729 | -45.347 | 2024-11-14 04:50:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 47.0 |
| c94178ad-076e-3202-973d-76c9a7c851a5 | -17.5675 | -57.5351 | 2024-11-14 04:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.4 |
| 8d923653-866e-3d9c-b051-1c0d916b0c5a | -17.2543 | -57.4698 | 2024-11-14 04:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.3 |
| 724b9af6-bbfd-3f45-b0d2-f813c63d8ae7 | -17.7052 | -57.5392 | 2024-11-14 04:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.0 |
| 59eb315a-f276-33f9-8893-df1b29958b21 | -17.2547 | -57.4493 | 2024-11-14 04:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.4 |
| 534ae974-8af3-34b7-be89-a676e3cd7fef | -17.5869 | -57.5533 | 2024-11-14 04:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.3 |
| 8b2568da-f38f-3baa-b62a-120b2bd25e41 | -17.5872 | -57.5328 | 2024-11-14 04:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.3 |
| a2cc366c-5d6b-3a57-a9de-880006f5e92b | -1.643 | -53.2677 | 2024-11-14 04:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 4c30c7c5-24e2-323f-b080-279014c10c7a | -17.6079 | -57.4688 | 2024-11-14 04:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.0 |
| fe52d93f-fc74-311b-b2b0-53eb4e7fd6d5 | -1.643 | -53.2677 | 2024-11-14 05:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 3752664e-8046-3f49-aa9f-a850bce2cac8 | -17.2543 | -57.4698 | 2024-11-14 05:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.5 |
| ea9d14da-a7bd-3f59-9c1c-a22f0e5c93eb | -17.5675 | -57.5351 | 2024-11-14 05:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.3 |
| 0d38e987-af94-35f8-9589-87e905eb1f21 | -17.6066 | -57.551 | 2024-11-14 05:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.6 |
| f8738e00-11c8-3488-a4db-a2862c9f791e | -17.6079 | -57.4688 | 2024-11-14 05:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.7 |
| 13caa006-b3a3-323f-837c-9278a224742c | -17.7052 | -57.5392 | 2024-11-14 05:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.7 |
| 7a2e62a5-0ecd-3a59-b0a6-62439eda8e93 | -17.5869 | -57.5533 | 2024-11-14 05:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.4 |
| b9a17e5a-fc3b-339e-865f-c83b0fccc63e | -1.6246 | -53.268 | 2024-11-14 05:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| f50bbacd-d8ed-3db7-8b80-f7041704a360 | -1.8106 | -52.1652 | 2024-11-14 05:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 14b24a71-9a91-3e18-9e6a-702bd4c69db6 | -17.5872 | -57.5328 | 2024-11-14 05:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.8 |
| 6a518bf1-42b7-38d5-9238-82219f5c1038 | -17.6076 | -57.4893 | 2024-11-14 05:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.7 |
| bf29ae7b-2da7-3e9d-99be-6467c17f5e83 | -0.89649 | -51.73529 | 2024-11-14 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b90c786-5e70-3a89-a8e5-d449b1ab999e | 1.07206 | -59.25089 | 2024-11-14 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af492c08-daa5-3d88-9d7c-40a9ebc07b7c | -2.3775 | -48.52571 | 2024-11-14 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e42996b0-ac91-32ce-bfcc-4bc6b92ed410 | -2.92077 | -48.07014 | 2024-11-14 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fce85a71-d796-350e-bd2d-884890d944a2 | -4.14171 | -43.85003 | 2024-11-14 05:01:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fba381fe-b8d1-322b-802c-d072e379253b | -1.60944 | -52.50173 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ec195d1-2edd-3e3e-8e1c-5a549c4db96b | -0.90192 | -51.72395 | 2024-11-14 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb33e929-4e86-398b-88b2-e06b070353f7 | -2.65899 | -51.67979 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce6f4fbb-3e88-3e4c-9a51-0c5c6ea95df3 | -1.667 | -52.53307 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6da34fae-f404-3199-863b-727d0adeb274 | -1.36609 | -52.3337 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1ec3c178-5ee6-3eb0-82bc-35fe4df3b61e | -4.16522 | -46.24717 | 2024-11-14 05:01:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57bf172a-f6e8-3ac2-a04d-231916359fe8 | 1.07149 | -59.24722 | 2024-11-14 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2cb02e4-4ef7-301a-b396-e95f884ed094 | -3.30072 | -43.5094 | 2024-11-14 05:01:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6bbc0b7-3db8-3bbc-bd28-811f98d12a92 | -2.3778 | -48.52738 | 2024-11-14 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43939dbb-2060-38f7-9d00-3dbadbb98bbc | -4.3524 | -49.6862 | 2024-11-14 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e6faf05c-faa2-36a2-81c7-edc62f485bb9 | -2.90318 | -46.85624 | 2024-11-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e49c56e0-ad6d-38b3-8230-5a3b740c5f5e | -3.16754 | -50.45479 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d92cb3a-72ac-3ce9-8b0e-7c5b6fa4061e | -2.74907 | -51.62529 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8cec7c1e-6e67-3e4d-8924-e2b643f345b7 | -2.64324 | -46.16247 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2396ebe3-2f6d-33cd-bcbd-b2164376b1fa | -1.86507 | -55.67598 | 2024-11-14 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f79fe765-9f1e-3d20-b0dc-88bb6e4b0072 | -0.19943 | -51.50708 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5d532ae8-2348-3585-9f5c-965265b5c3e6 | -2.20641 | -53.74724 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65820df2-f7c7-35f9-8121-b8b8cd219d35 | -1.20884 | -51.76803 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9051847-20cd-3240-a897-0d4fa01494ef | -5.19889 | -44.35463 | 2024-11-14 05:01:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1322bdd-9b0d-3560-bc62-921f97dc9eb5 | -1.80168 | -52.17184 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 26dd8946-1f7b-3155-a60c-e39e5872bba3 | -0.90129 | -51.72791 | 2024-11-14 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d7000e0-87aa-39d3-b939-1f4c98f6c8e9 | -1.95032 | -53.33124 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c6b8438-b6bb-3e92-84dd-60f36e926065 | -2.17239 | -48.54943 | 2024-11-14 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12da274b-4784-31da-af98-8b0fe7198da0 | -1.39509 | -51.10347 | 2024-11-14 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96f02bd2-817b-30e7-a39a-daf92c51abb4 | -1.44612 | -47.78473 | 2024-11-14 05:01:00 | NPP-375D | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d1900b3-7112-3711-9271-bc89afa628e5 | -2.65231 | -46.1801 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 003ff5fe-4e6a-3bce-bdc5-12395a3c2038 | -1.33611 | -48.33019 | 2024-11-14 05:01:00 | NPP-375D | MARITUBA | PARÁ | Brasil | 1504422 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0fddc672-8ee0-39a3-b383-863c7ec2ca17 | -1.55197 | -51.22011 | 2024-11-14 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db033a6a-e445-3369-8bc9-c2168ba37f9c | -2.58287 | -51.92458 | 2024-11-14 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd34e6c9-4d6a-328b-9739-38fe1a8795e8 | -1.38809 | -52.1859 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e11b9654-5416-3e4c-af4c-c74ad9bf1a32 | -0.89066 | -51.72626 | 2024-11-14 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5b39738-1c89-35e7-8a57-1af353b154b9 | -2.66939 | -46.81846 | 2024-11-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00a06cd5-8670-3961-a81d-8d81b78a23dc | -3.14637 | -54.48133 | 2024-11-14 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f151df4f-5484-38ce-be81-970173e9ff16 | -1.04302 | -52.43938 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc40070b-43ff-334e-a9b8-e62d692c23f1 | -1.80107 | -52.1757 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3bcc07a-041a-35b6-9f73-991c9e65f55f | -1.36029 | -52.3483 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a9a284ac-b847-3424-b947-dc1da892ae54 | -1.96389 | -51.54438 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38d501c7-bd3d-3565-8f71-e62110e899ba | -3.86755 | -43.94026 | 2024-11-14 05:01:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 333ee15f-15c2-3c46-b995-0df8c57765d9 | -1.79878 | -52.1674 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| cb72bdbe-dc83-3c15-aaf9-0d41cb5eaecc | -4.52104 | -46.47697 | 2024-11-14 05:01:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9beb945-0326-3e9a-a41e-1c2423a4cda5 | -2.35078 | -53.88089 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d6a9c11-a484-363c-bec5-d3451bea3ac0 | -1.86563 | -55.67245 | 2024-11-14 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23113956-2769-3ca6-8dc5-5e14627b9916 | -2.83322 | -50.44233 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d693a23-dd43-3e1f-abc4-6b5c878d2373 | -2.40496 | -45.34395 | 2024-11-14 05:01:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e44873b5-b58f-3b31-96e0-b9670077cfb2 | -2.02377 | -46.5019 | 2024-11-14 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4ab61e29-adee-35ae-a31e-d6792702896e | -2.42017 | -46.26834 | 2024-11-14 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09d25d13-03d8-3041-9c29-6068955fff98 | -4.21197 | -50.49527 | 2024-11-14 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8ed7a102-fa35-3d9d-9f1f-9d4c60582fd3 | -2.29263 | -53.79973 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c41bf24-940d-3808-a3e1-15b4820228ad | -3.49623 | -50.83823 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2525152d-cd9c-39bd-9a02-6b5557d335af | -1.5157 | -51.55194 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README41.md)
