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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2a2de2f-9225-33ae-80f2-c7a1cda1bc25 | -12.2888 | -43.7495 | 2025-10-27 01:30:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 380d4539-86aa-3cdc-bdcf-e10ea548c117 | -10.8401 | -56.959 | 2025-10-27 01:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 537e17ae-e381-33a2-b0c7-c38f3a38bd57 | -4.4807 | -43.4005 | 2025-10-27 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| e884d663-1e76-3850-84b9-0c3117e1e228 | -7.8411 | -46.4646 | 2025-10-27 01:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 1e18b0f6-2d5e-31f4-a067-5e892127c010 | -7.8408 | -46.487 | 2025-10-27 01:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 512b9595-e7eb-3e61-a2ee-f99c12bac09b | -4.4804 | -43.447 | 2025-10-27 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 154.3 |
| e99f0813-a726-3beb-8a7f-92bb434f05bd | -4.4805 | -43.4237 | 2025-10-27 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 364.9 |
| f9b12784-e375-3af9-99d7-7a0e09e3519d | -7.0692 | -46.7541 | 2025-10-27 01:30:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 664ca832-dc87-335f-8bce-02b767adc38e | -4.3879 | -43.3129 | 2025-10-27 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 0f737b46-139d-3be7-8c6c-19b7af7a019d | -4.4617 | -43.4481 | 2025-10-27 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 53b979a8-d623-3c4e-ac87-d59859bfc971 | -4.462 | -43.4016 | 2025-10-27 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 19defd8a-2634-354b-98a5-85cdc0f40859 | -4.4992 | -43.4226 | 2025-10-27 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 868c140d-f6cd-3b99-83c1-b229139bca8b | -4.4618 | -43.4248 | 2025-10-27 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 144.5 |
| d3e34ff3-8aed-30a5-97a9-186e26f0a214 | -4.443 | -43.4492 | 2025-10-27 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 13b0df09-92e5-333f-be95-9730f56d270a | -12.5258 | -47.5678 | 2025-10-27 01:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 590ff5ed-bc4d-34cd-8772-3bad651af47e | 1.1502 | -51.0603 | 2025-10-27 01:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 51.1 |
| bcfd48b3-c859-3ffd-bd52-1051380cf0cf | -4.3877 | -43.3362 | 2025-10-27 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 5ff2d5f7-ffa9-3a27-b525-7f4172470a80 | -7.8596 | -46.4853 | 2025-10-27 01:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 585b8d90-2ad7-37e3-8ebb-d43bd40b1098 | -4.4477 | -45.4824 | 2025-10-27 01:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 58.2 |
| cc0134ad-3bb9-3238-b75a-7ad1040350ca | -4.3879 | -43.3129 | 2025-10-27 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 8951db56-3829-37f7-8d99-0a5e6414000f | -4.4618 | -43.4248 | 2025-10-27 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 0fb83ae2-bd50-3c21-9aee-d28db34b3fd5 | -4.4805 | -43.4237 | 2025-10-27 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 239.6 |
| 13c939b9-f4db-35f7-b792-d7c0c6550d8d | -4.4431 | -43.4259 | 2025-10-27 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| b08e0f13-29d9-3c4a-8fc3-5a399cdbb21e | -7.8408 | -46.487 | 2025-10-27 01:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| ba3b47a7-cf7b-3c40-857d-e70cd5fd9ad7 | -4.4665 | -45.4589 | 2025-10-27 01:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 175.6 |
| 9cf1b88d-1255-3e29-8c2c-c6e8d76244a7 | -4.448 | -45.4374 | 2025-10-27 01:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 83.3 |
| dde9efc0-8e17-37cb-8e20-e5ba250c6762 | -4.4666 | -45.4363 | 2025-10-27 01:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 41.5 |
| f3b7f97e-a112-3f16-a302-8f8b43a99784 | -7.8411 | -46.4646 | 2025-10-27 01:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| ad224a30-1bf6-3a72-9a7d-c9abd909f355 | -7.0692 | -46.7541 | 2025-10-27 01:40:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| e38e2a22-5034-3adc-904a-6ac0b673189f | -4.4804 | -43.447 | 2025-10-27 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 095d8f2d-4b7b-39fd-8ec1-43ac8ff2a180 | -4.4479 | -45.4599 | 2025-10-27 01:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 405.9 |
| e9c702b8-1f2a-3b12-97a1-ab3fb8941ea6 | -4.4807 | -43.4005 | 2025-10-27 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 31de5008-92be-3619-904f-7834c1222728 | -4.4617 | -43.4481 | 2025-10-27 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 35.8 |
| ec291c5b-58d5-3d98-8164-579c395f9457 | -10.8401 | -56.959 | 2025-10-27 01:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 0e6e9ab9-a610-3acd-a17e-732b7fcbe7b4 | -4.462 | -43.4016 | 2025-10-27 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 5144e17e-8d24-3222-9bcd-6db9e4ba00fc | -4.4431 | -43.4259 | 2025-10-27 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| de622f2d-04ac-3ea1-aa9e-b926d5496b52 | 1.1502 | -51.0603 | 2025-10-27 01:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 83.3 |
| a82288bd-8d28-3606-8d99-718031388e83 | -4.4804 | -43.447 | 2025-10-27 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| acc3ff0d-f679-3c91-80ae-e99441accabf | -3.5595 | -44.5305 | 2025-10-27 01:50:00 | GOES-19 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 1a779a10-3900-3dbd-a75a-ce2a75a4ec62 | -4.4805 | -43.4237 | 2025-10-27 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 221.2 |
| 5e670be1-4244-31a3-8720-80399eb72144 | -4.462 | -43.4016 | 2025-10-27 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 5c96b357-3524-3f6f-8547-40405e5db129 | -4.4618 | -43.4248 | 2025-10-27 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 11074ddf-326e-3526-9f5c-fa31d44ac3cb | -7.0692 | -46.7541 | 2025-10-27 01:50:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 55cac0b0-dd85-37a9-9762-c17b466de637 | -4.4617 | -43.4481 | 2025-10-27 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 285a1df0-37f1-3d1e-b8e9-b56364ecfbc1 | -7.8408 | -46.487 | 2025-10-27 01:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| ae79b8b4-1cee-3aeb-8397-440b6e506e5c | -4.3879 | -43.3129 | 2025-10-27 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| d83b5ab9-a050-3c8b-be81-145eabf0e77e | -10.8401 | -56.959 | 2025-10-27 01:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 99abc270-5342-3ddd-9140-328209e107bf | -4.4807 | -43.4005 | 2025-10-27 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 0da1965f-cf35-3835-87e7-59aca37e503e | -10.7484 | -44.1932 | 2025-10-27 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 8fb8fe22-574e-3021-ab2e-e632812d9186 | -4.4433 | -43.4027 | 2025-10-27 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| fe0293cf-7597-34d1-b8f8-14e5120e1660 | -7.8411 | -46.4646 | 2025-10-27 01:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| db367330-6e3a-3b66-9017-7476256803ab | -8.97024 | -65.93003 | 2025-10-27 01:52:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4bdab673-f02f-306e-849e-0ca179ce9b8d | -9.9995 | -47.1772 | 2025-10-27 02:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 69d85aab-b651-3171-a0c8-f225caa782a5 | -4.4618 | -43.4248 | 2025-10-27 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 118.2 |
| a73bf846-889a-362e-b6bb-3b1823a8ee29 | -4.3879 | -43.3129 | 2025-10-27 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 3ee263fa-0c6e-3dee-8e6b-d14232161e53 | -7.8596 | -46.4853 | 2025-10-27 02:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 39d68208-6fc5-39ae-a5d9-fe3c6e95a837 | -3.1612 | -50.3298 | 2025-10-27 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| b99357ff-0d81-3215-8736-64f1f910fe2f | -4.462 | -43.4016 | 2025-10-27 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| e6a0df82-eaa0-3882-bf4b-6485134d8281 | -10.7484 | -44.1932 | 2025-10-27 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 1128effa-9bba-3d0f-80ca-99f7f76d39c0 | -4.4807 | -43.4005 | 2025-10-27 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| ad91804a-d127-3fb3-836d-5a48b45010b1 | -10.8401 | -56.959 | 2025-10-27 02:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 32d6a0a6-367e-3315-b3f7-0dc9a22f7c6f | -4.4431 | -43.4259 | 2025-10-27 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 091d1796-1752-33da-a623-9d83afb27783 | -7.0692 | -46.7541 | 2025-10-27 02:00:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 9e037845-b253-30f1-9235-29afa3b7ee7b | -4.4617 | -43.4481 | 2025-10-27 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| c29d81e7-4b00-3f00-b32c-457b4d3872f2 | -4.3877 | -43.3362 | 2025-10-27 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 8dc4aa0e-b5a7-36f5-a286-25f8c8492e7c | -4.4804 | -43.447 | 2025-10-27 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 7c3f9c9a-0929-3c33-b81c-0fb578585db2 | -4.4805 | -43.4237 | 2025-10-27 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 4b035c6e-7756-3500-9930-74dda21b3bbd | -7.8408 | -46.487 | 2025-10-27 02:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 146.2 |
| ca151fd3-1edd-36a5-b7e0-d2c10a1f1fc5 | -7.8411 | -46.4646 | 2025-10-27 02:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 67ff900c-d2fd-3deb-826b-3d3227a00b05 | -4.4992 | -43.4226 | 2025-10-27 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 1f95b54b-6ca1-3fb5-97be-794bb8825c51 | -12.6544 | -52.6273 | 2025-10-27 02:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 5b01e4aa-7fa5-332c-8218-d539ed295e7a | -7.0505 | -46.7557 | 2025-10-27 02:00:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| b4c322e0-b925-34da-8bea-0e24317f430f | -3.5782 | -44.5297 | 2025-10-27 02:00:00 | GOES-19 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| fc80eb04-7e86-35d7-bab2-d4a53fb430dd | -9.4761 | -40.3862 | 2025-10-27 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 71.4 |
| 0bdcb188-d955-33a8-84ac-cf9e695fd193 | -7.8599 | -46.4629 | 2025-10-27 02:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| fe0be546-1cff-34ac-8074-5a131618e8c3 | -4.4804 | -43.447 | 2025-10-27 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| c1263b64-dc1f-3cbf-8c9b-757e5c9def57 | -4.3879 | -43.3129 | 2025-10-27 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 13eb11ee-32ea-3eed-a1a7-f0e61be013fa | -3.5595 | -44.5305 | 2025-10-27 02:10:00 | GOES-19 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 956f8366-1f7a-33d0-b2f5-5daae2fe4e33 | -7.8223 | -46.4664 | 2025-10-27 02:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 92c8e825-51f2-3296-8db2-40d274a3bee7 | -4.4666 | -45.4363 | 2025-10-27 02:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 2b6ca726-81c4-36e5-8c88-c80510247d2a | -7.0692 | -46.7541 | 2025-10-27 02:10:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 9229e46b-f085-3173-b364-1f2c583d8e08 | -4.4665 | -45.4589 | 2025-10-27 02:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 208.5 |
| 3c5e3423-d9b7-31be-8e50-2503b4d895a7 | -4.4618 | -43.4248 | 2025-10-27 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| de1b64c3-7276-375a-996d-bd0e99999bc8 | -3.5782 | -44.5297 | 2025-10-27 02:10:00 | GOES-19 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| b96e0f6c-209b-34d2-805f-ea5b7db0cd35 | -15.1748 | -49.3893 | 2025-10-27 02:10:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 85.5 |
| a6428c56-917e-32bb-97dc-2fb3d52a8761 | -7.8411 | -46.4646 | 2025-10-27 02:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 7bb1079d-6daf-364f-8916-2b98230389b6 | -7.8596 | -46.4853 | 2025-10-27 02:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| e3355fc1-5eea-3abc-8cfb-762b73517a99 | -4.448 | -45.4374 | 2025-10-27 02:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 78.2 |
| c816052a-96c3-3809-a8cd-022515695bab | -7.8408 | -46.487 | 2025-10-27 02:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 1cf5aca3-49cc-3405-a438-abf227e0447f | -7.822 | -46.4887 | 2025-10-27 02:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 6ddccaa2-78f5-386f-87e8-981e379e211e | -10.8401 | -56.959 | 2025-10-27 02:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| f5a03b27-548d-3857-bc2e-4bfb1bf80bc7 | -4.4479 | -45.4599 | 2025-10-27 02:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 254.2 |
| 4f245d63-c8fa-3586-bbc0-d8bd89dd141d | -4.4431 | -43.4259 | 2025-10-27 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 93308ccf-b489-3c15-a60f-5ceaa23bfd7e | -4.4805 | -43.4237 | 2025-10-27 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 192.2 |
| c68c88d4-5838-3c04-842f-8c5ef15881b0 | -10.7676 | -44.1905 | 2025-10-27 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 3670bd79-67d1-3e9b-8e24-61c5191c1169 | -3.5595 | -44.5305 | 2025-10-27 02:20:00 | GOES-19 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 67d8b215-4d24-3a1e-a228-da80bef015be | -4.3879 | -43.3129 | 2025-10-27 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 955d0bea-db19-31a8-91df-aca41a7eb992 | -9.4952 | -40.3834 | 2025-10-27 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 91.7 |
| d020e145-b534-3c14-876e-f92bd1849cdc | -4.4804 | -43.447 | 2025-10-27 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 056884bb-55ff-383b-8607-b21e622e1888 | -4.4617 | -43.4481 | 2025-10-27 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |


[Clique aqui para ver as próximas entradas](README11.md)
