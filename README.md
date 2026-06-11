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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac87354d-9f8f-3bb3-ae28-45b115fca93a | -12.049 | -45.2796 | 2026-06-11 00:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 52.0 |
| dc1c74e9-59f9-3f21-bb50-21883c9f4d12 | -6.4543 | -44.5749 | 2026-06-11 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 108.6 |
| fb1ec1e3-c3d9-31f8-b95e-109b7d1bfbc8 | -6.4545 | -44.5519 | 2026-06-11 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| f95e0eb8-2a88-393c-a23d-f8d37795767b | -7.6345 | -50.0488 | 2026-06-11 00:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| fad4b369-e2c8-3f16-b4cf-486eade575c4 | -6.4357 | -44.5535 | 2026-06-11 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 73fa9dbe-086c-3e76-a06d-169f674af9b5 | -9.3234 | -45.4787 | 2026-06-11 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 137.2 |
| f617937c-4836-34fd-bca1-97c9a937f57e | -6.4355 | -44.5764 | 2026-06-11 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 2d9b7f10-ef5e-316b-97ba-337b96f5a8bf | -9.3237 | -45.4559 | 2026-06-11 00:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 59ac4989-2746-3dec-b644-234d63fb98b9 | -9.3045 | -45.4809 | 2026-06-11 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.2 |
| c91c196c-cb1c-33f2-a07a-2f689cca1ba8 | -7.6222 | -50.032299 | 2026-06-11 00:08:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 822d30b7-2e9f-35ff-8ece-4cd2ee8a6b39 | -6.9541 | -44.549999 | 2026-06-11 00:08:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4319d7e-c675-34bf-bb78-9b6fa064ac15 | -9.323 | -45.496201 | 2026-06-11 00:08:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dd2069b1-4640-3a8e-801c-21053ada5bc4 | -8.3227 | -43.8176 | 2026-06-11 00:08:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 84c7639b-6e9a-364c-bdf8-a4dc76205445 | -9.2991 | -45.480301 | 2026-06-11 00:08:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ad6d1cdb-43d5-352f-a304-ad1eb5d576ea | -8.3112 | -43.811699 | 2026-06-11 00:08:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ccafafe2-e92a-3ffa-97bd-82265e402aef | -5.0416 | -43.263802 | 2026-06-11 00:08:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cc9f1fcb-4904-3839-8a6e-30c723d9050a | -6.444 | -44.5658 | 2026-06-11 00:08:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81609440-3aa5-3b0a-8f59-7a2e8ded3e84 | -3.5007 | -48.0322 | 2026-06-11 00:08:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84bd5733-2cdd-38be-b2b2-76d12176bfc9 | -10.3417 | -46.596298 | 2026-06-11 00:08:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e12bfd4-3e99-3912-91ce-b12a0559f637 | -9.4885 | -40.3843 | 2026-06-11 00:08:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9aec7ce0-8dda-3790-9e28-3a06867291db | -8.9829 | -48.0877 | 2026-06-11 00:08:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6593591-5233-3c59-85d0-00082dc8ca1d | -9.3067 | -45.468201 | 2026-06-11 00:08:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fb0fcaa0-ef58-3f17-9bd2-5b24e82a9c0b | -9.3208 | -45.486099 | 2026-06-11 00:08:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 34457392-e0a2-3722-8b43-e0f3f788ccd8 | -6.4324 | -44.5597 | 2026-06-11 00:08:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be390195-a274-3cd8-b09c-89cc07f368c2 | -6.4361 | -44.576099 | 2026-06-11 00:08:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9353d75a-0749-30b1-92ce-bc862bcf7920 | -8.3129 | -43.819698 | 2026-06-11 00:08:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 91d4b62a-1cb8-3ac6-99f4-317c0b6e99a7 | -9.2092 | -47.905102 | 2026-06-11 00:08:00 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 09c51985-ac58-3b4b-93d0-08e9b1cefad3 | -6.4342 | -44.567902 | 2026-06-11 00:08:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb5eabfc-29da-3c8a-9742-e8da6b1b6757 | -6.956 | -44.5583 | 2026-06-11 00:08:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8aa184e5-3e84-3ae2-be34-ba07bd118489 | -6.4459 | -44.574001 | 2026-06-11 00:08:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f5051002-118c-3d90-bcda-4394bef07376 | -8.321 | -43.809601 | 2026-06-11 00:08:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 55cb1359-e74f-30d5-912c-6dbc6b228071 | -6.1919 | -44.8647 | 2026-06-11 00:08:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18e60790-afad-34a2-8cf7-a1bf9cf360e3 | -9.3089 | -45.478199 | 2026-06-11 00:08:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8039ee63-3672-34a1-816e-5d6a9fcb0234 | -6.452 | -44.555401 | 2026-06-11 00:08:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4b68bf51-5009-3490-9839-bbe752a6ad18 | -6.9523 | -44.541698 | 2026-06-11 00:08:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf975dc1-0b5b-3b64-acbd-6a58ad90ad06 | -9.2122 | -47.919399 | 2026-06-11 00:08:00 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8a4044d0-869c-3f95-91c6-87e27bbe82a4 | -6.4422 | -44.557598 | 2026-06-11 00:08:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53e4c00e-46ae-379a-8ad9-c4540ce8543c | -9.2969 | -45.470299 | 2026-06-11 00:08:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1f88a8a7-9b03-3821-82ac-835e10de18e4 | -6.4538 | -44.563599 | 2026-06-11 00:08:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44d44149-eca3-39d1-96d5-5a4376d14176 | -9.1994 | -47.907101 | 2026-06-11 00:08:00 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 523c21ae-9140-3bb8-bc2c-7332c659f921 | -10.2868 | -47.609402 | 2026-06-11 00:08:00 | METOP-C | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35e51f17-e8cb-3cfd-817a-4696d955a5d5 | -9.311 | -45.488201 | 2026-06-11 00:08:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 66ac448a-390e-31be-b284-78ab07ea654d | -5.0432 | -43.270901 | 2026-06-11 00:08:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c1b51eb8-9aa6-3ee8-bb8e-8b119c3b5767 | -10.277 | -47.611401 | 2026-06-11 00:08:00 | METOP-C | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 502ac35b-ded9-3bbe-a47f-656deee22103 | -5.04 | -43.256599 | 2026-06-11 00:08:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0494b5f-8741-32f2-bb87-8e5e787d27df | -9.3187 | -45.476101 | 2026-06-11 00:08:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9450744d-6b6b-385e-abff-6ee235c207bc | -6.1901 | -44.8563 | 2026-06-11 00:08:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 997a5238-1bc5-3a3c-bc39-18b7d7b7afaf | -9.487 | -40.377399 | 2026-06-11 00:08:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 95fdf473-c7c2-3524-99aa-d69ae37a1ade | -6.4355 | -44.5764 | 2026-06-11 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 7fc38186-de7c-3693-9432-8c3139b7127b | -6.4543 | -44.5749 | 2026-06-11 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 91988f0b-5619-383c-a526-a052a1d42e47 | -9.3237 | -45.4559 | 2026-06-11 00:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 50.9 |
| a7652be3-00a8-31ae-9265-9f403ba14d9c | -12.0486 | -45.3027 | 2026-06-11 00:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 167f04ab-b250-3be6-9f5b-53af37cb93e3 | -9.3045 | -45.4809 | 2026-06-11 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 72a1a86d-2ca6-3aef-a851-e8332ce590fd | -9.3048 | -45.4581 | 2026-06-11 00:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 63566c01-1182-31c1-b86e-6b8359fd5187 | -6.4545 | -44.5519 | 2026-06-11 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 3695dfef-1528-3590-9506-2669fb042f5b | -9.3234 | -45.4787 | 2026-06-11 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 35372d05-4a39-3763-852a-81c400da538f | -6.4357 | -44.5535 | 2026-06-11 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 946a9ce0-cf30-31fc-9cd4-23b5e52525b1 | -6.4357 | -44.5535 | 2026-06-11 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 7256bbbb-eb7c-3c2e-9e73-92227941b391 | -9.3234 | -45.4787 | 2026-06-11 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 3fd3694f-d3ca-3cf3-80bf-2368128e52fc | -12.049 | -45.2796 | 2026-06-11 00:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 7a2e5a37-50cc-3f48-ae69-186a7dd89735 | -6.4543 | -44.5749 | 2026-06-11 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| fc9eafa4-851c-305c-a9a0-a5b25be566c8 | -9.3237 | -45.4559 | 2026-06-11 00:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 47.5 |
| b7f28cdb-da2c-31b7-a546-68d5b171d45b | -6.4545 | -44.5519 | 2026-06-11 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| e68c0523-90b0-3741-9675-b5c2d2175f10 | -6.4355 | -44.5764 | 2026-06-11 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| a1ccf836-59a2-3532-adf6-4d88963d9a4d | -9.3045 | -45.4809 | 2026-06-11 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 3b10a5e9-f52c-3bd6-9a12-d94c55452e97 | -9.3045 | -45.4809 | 2026-06-11 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 85518cf5-4832-3a51-b01e-a689ce49d588 | -12.049 | -45.2796 | 2026-06-11 00:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| b70f9cc5-f22c-398b-8363-88bb887ffb57 | -10.84 | -46.7863 | 2026-06-11 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 239c20b7-5cf8-354f-ad4b-e706453bb244 | -6.4355 | -44.5764 | 2026-06-11 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 133.5 |
| dcc3a300-2010-343c-9842-8d3fda49c564 | -6.4543 | -44.5749 | 2026-06-11 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| e25d849a-ab98-3bd5-962a-779436a97343 | -6.4545 | -44.5519 | 2026-06-11 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 040844e8-8d08-37d9-ae3c-8bb76885fa72 | -12.0486 | -45.3027 | 2026-06-11 00:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| f71e7638-8041-3a86-be65-0491bd3fc9cf | -9.3234 | -45.4787 | 2026-06-11 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 109.8 |
| eafea1c7-f976-33c4-9404-a5fba7549bf8 | -6.4357 | -44.5535 | 2026-06-11 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 142.9 |
| eccebe65-7782-31a2-8aa5-66cab05b55ce | -6.4543 | -44.5749 | 2026-06-11 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 4c2395fc-0312-3be5-87ef-801fc677e3c5 | -10.859 | -46.7839 | 2026-06-11 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 3cd03e6d-e54f-3026-817e-45e4463eb4ea | -12.8548 | -44.3625 | 2026-06-11 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| a6efba48-44d3-3915-87bb-fff6ffc2a5c8 | -6.4545 | -44.5519 | 2026-06-11 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 7d4de004-042c-31f1-962a-5aca93480a6c | -12.0682 | -45.2768 | 2026-06-11 00:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 85b135ab-ee77-3e7f-b7c1-b6a14e4a949e | -9.3045 | -45.4809 | 2026-06-11 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 2355e559-6202-35e8-9ef0-5828e933524b | -6.4355 | -44.5764 | 2026-06-11 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| ca1a4152-e246-3c87-847b-eaf44cca08f1 | -12.0486 | -45.3027 | 2026-06-11 00:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 90b2f891-c3d0-331b-8ca4-189025192bab | -12.0678 | -45.2999 | 2026-06-11 00:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| cbb5d582-b12f-3140-a86a-a720cec4308e | -9.3234 | -45.4787 | 2026-06-11 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| c67e8e04-38a6-3011-b1b6-b415e9e38bca | -6.4357 | -44.5535 | 2026-06-11 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 140.3 |
| bec75c7d-d686-32c6-9e38-915fd17a488d | -9.5156 | -40.3061 | 2026-06-11 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 61.8 |
| 031043ca-f9fe-3ad4-94f4-db6db422ab14 | -6.4545 | -44.5519 | 2026-06-11 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 749cbe22-d0ff-3df8-b94a-770866e64956 | -9.3234 | -45.4787 | 2026-06-11 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 104.1 |
| f0497539-c65e-30b2-9696-44768898f0c0 | -12.0682 | -45.2768 | 2026-06-11 00:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 8b61040b-b9b9-333a-af9b-ed4ee40087a7 | -6.4357 | -44.5535 | 2026-06-11 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 125.9 |
| f9db52ad-dfbb-3339-bdad-e1c72ed1aa65 | -9.3045 | -45.4809 | 2026-06-11 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 47b06335-4ec6-35f5-9011-edf7bf94bf06 | -6.4543 | -44.5749 | 2026-06-11 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| dc1d1a8a-1f25-3055-92ba-ba2b1f77788a | -12.049 | -45.2796 | 2026-06-11 00:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 7b829be0-719a-3953-a446-d0f6651ffc31 | -9.3152 | -48.9599 | 2026-06-11 00:50:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 5645b3c8-227b-3540-851d-75e643934237 | -6.4355 | -44.5764 | 2026-06-11 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 127.7 |
| c1eb0255-53c9-39ad-ac68-18d2f994cc95 | -12.0678 | -45.2999 | 2026-06-11 01:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| b6425654-2954-3ee2-ba2d-8053d78af8a1 | -6.4357 | -44.5535 | 2026-06-11 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 578e89e3-a724-3760-9466-b9781e872035 | -9.3234 | -45.4787 | 2026-06-11 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 160.8 |
| bb72a098-982a-3466-abaf-d408c85e6950 | -6.4543 | -44.5749 | 2026-06-11 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 3f8c028f-8dc7-39af-999a-2567194cf9b0 | -9.3045 | -45.4809 | 2026-06-11 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.4 |


[Clique aqui para ver as próximas entradas](README2.md)
