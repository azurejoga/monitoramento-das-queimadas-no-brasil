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
| 9f7deec2-548a-31d9-9cbe-55f352ba3bf4 | -6.3134 | -47.6261 | 2026-09-20 01:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 66f921f1-a538-3546-95f0-3ada7ca45e49 | -13.0177 | -46.9125 | 2026-09-20 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 9700b6c6-5dd6-3516-ace2-9810bef0b658 | -7.5334 | -45.4367 | 2026-09-20 01:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| df115245-aa41-3a76-bb1b-047516d80969 | -7.3073 | -55.6163 | 2026-09-20 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 7a490e1b-9b98-3671-bb9e-f7fdd7b9c6be | -11.4537 | -45.3892 | 2026-09-20 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 20acd005-ccbe-339c-94ff-28be3356da5a | -12.5227 | -50.0267 | 2026-09-20 01:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 4ec4b4f0-da1f-3451-929a-419081839cdf | -3.7454 | -51.8082 | 2026-09-20 01:50:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 419e5390-8973-3433-b4f8-0f286a59c41b | -11.118 | -54.0268 | 2026-09-20 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 126.0 |
| fc671b4f-09e0-3836-bfb0-17824c1d9704 | -14.6661 | -46.6919 | 2026-09-20 02:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 5d0903d2-2620-3e90-ba43-98af17dd9494 | -11.118 | -54.0268 | 2026-09-20 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 7ca30b4d-5b62-3758-bcc1-830588cea5c6 | -5.8595 | -53.5196 | 2026-09-20 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 86464515-2533-32cd-8c91-2b79dfb41e67 | -8.1688 | -54.7432 | 2026-09-20 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 71f2c296-7531-384b-aabf-b68b456cdc21 | -11.3793 | -51.3989 | 2026-09-20 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 2dda1eff-12e7-3ca9-a9f8-8ae040468511 | -3.7454 | -51.8082 | 2026-09-20 02:00:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 32f72e2e-4d5c-33f6-9503-4295ccf565ad | -6.2948 | -47.6274 | 2026-09-20 02:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 217.7 |
| 70a8c64a-a9fd-37b5-b976-30eb9e1ac1d8 | -11.2307 | -54.078 | 2026-09-20 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 598db145-1100-3fa6-8d83-650f68da6c39 | -5.8408 | -53.5408 | 2026-09-20 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 85bcdfb7-2fe5-30d7-bed5-91da07e42210 | -2.8791 | -57.8184 | 2026-09-20 02:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 1aaaafb5-083d-3bd1-a7ab-5983feebbc72 | -5.841 | -53.5205 | 2026-09-20 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 0098f1bd-cd0a-3e39-ba37-4150f798707a | -7.3259 | -55.6153 | 2026-09-20 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 7e14d617-8b49-3fba-8fb7-b49259e49ce5 | -13.0177 | -46.9125 | 2026-09-20 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| dab1276a-332c-3b28-8bd2-80860f91fc81 | -5.8593 | -53.5399 | 2026-09-20 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 71cf8254-1325-3370-b925-dcef77ea9014 | -6.295 | -47.6055 | 2026-09-20 02:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 216.1 |
| 96bb2a87-6de0-3c86-9aa7-a264c63ee1cc | -8.7911 | -60.7935 | 2026-09-20 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 24f886ae-8ce4-3634-b73b-c86ea6f8ab9f | -13.037 | -46.9096 | 2026-09-20 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 1f8d7c9b-e815-3cfa-b541-26783bc29bc0 | -14.7051 | -46.6852 | 2026-09-20 02:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 6f48a860-1dff-3a4e-b073-be38f5201405 | -7.5472 | -45.8868 | 2026-09-20 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| f6286991-48c4-3c97-b794-d87d751e335d | -11.0991 | -54.0285 | 2026-09-20 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 180.1 |
| 55d3b065-fe98-32bf-ae77-fdf4c6553e81 | -12.7423 | -46.2058 | 2026-09-20 02:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 41a56c0d-4c29-39f3-865d-30da1e39d52f | -8.1686 | -54.7634 | 2026-09-20 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| ac400fc2-603b-36b4-b74f-47f09a26b66e | -2.8791 | -57.799 | 2026-09-20 02:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 28833f03-d452-3913-ab68-be8d1d02f6bc | -12.7428 | -46.183 | 2026-09-20 02:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| bc8461e8-619c-3c3f-98d4-0c4d88e5e258 | -9.131 | -45.7273 | 2026-09-20 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 02bb503f-7dcf-3c56-b233-b6e938e43b0f | -14.6856 | -46.6886 | 2026-09-20 02:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 195.6 |
| decca3be-0f5d-335a-a4d3-ce11670aa20e | -7.5522 | -45.435 | 2026-09-20 02:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 08b470ec-2a0b-3ef6-9573-ec511c5905f6 | -6.3134 | -47.6261 | 2026-09-20 02:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 2c2f05fa-428b-3272-a01b-bef6f1938f22 | -11.8739 | -47.657 | 2026-09-20 02:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 9aa9b742-6579-33d5-8557-2397a168c76b | -11.0802 | -54.0302 | 2026-09-20 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 6cf89914-9eff-391c-9ee2-af8ff200b6e2 | -6.3136 | -47.6042 | 2026-09-20 02:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| ddaef2ad-d772-3b1b-8203-e18fedb64143 | -11.2118 | -54.0797 | 2026-09-20 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 350c067c-480e-352c-972d-aee45c565708 | -3.6946 | -60.6025 | 2026-09-20 02:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 5b961439-f1ef-3e3c-8235-08b8ac42ea69 | -10.2976 | -50.2585 | 2026-09-20 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 33828033-849c-3e43-9e3b-83b77ac5f46c | -7.5284 | -45.8885 | 2026-09-20 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 3675c69e-6f48-3f4c-af06-cd79af5521b3 | -14.6851 | -46.7115 | 2026-09-20 02:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 78.5 |
| b1d2e87a-761e-3699-b351-194f40c32bd1 | -3.7453 | -51.8288 | 2026-09-20 02:00:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 1d0cdb3f-7401-3d3a-aafe-9df3edbc8dc6 | -12.7621 | -46.18 | 2026-09-20 02:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 9da9f59d-8ec2-38f4-998a-86f550b36b51 | -3.6807 | -60.598801 | 2026-09-20 02:01:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a78232e5-6b44-34b6-b35e-af220e813c22 | -2.8815 | -57.802799 | 2026-09-20 02:01:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 68a1030f-b077-3bba-8c90-9cb96534cbf5 | -10.5731 | -68.670303 | 2026-09-20 02:01:00 | METOP-C | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 6c24f99e-0e4f-3d41-b359-cf80b574e205 | -8.2395 | -61.372898 | 2026-09-20 02:01:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 61fa81ac-d540-36bb-ae00-046f13332719 | -3.6904 | -60.5965 | 2026-09-20 02:01:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 704de3d3-5bfd-3eb6-a655-019b885cfdd9 | -9.5477 | -66.025497 | 2026-09-20 02:01:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e20d420b-2e41-3a77-89bd-69e5da8bea40 | -2.8897 | -57.836102 | 2026-09-20 02:01:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8f2804d0-3bb6-397f-b3df-8dbaf662612a | -3.6858 | -60.619598 | 2026-09-20 02:01:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6ffc32d9-3aa8-3a89-8b6e-64a2d31392ef | -9.9324 | -60.7239 | 2026-09-20 02:01:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 14a55cca-0f18-3167-8550-46d25c93a756 | -9.5556 | -66.015297 | 2026-09-20 02:01:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8142101b-ebbb-32bb-9ca7-c40cb24213fd | -3.6853 | -60.575699 | 2026-09-20 02:01:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 283e72b1-d664-3f9b-9ba7-28bff557dac1 | -10.5715 | -68.663399 | 2026-09-20 02:01:00 | METOP-C | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 8d005b43-be26-3068-8c3e-f5fa6295d051 | -3.1123 | -61.4212 | 2026-09-20 02:01:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 94fcdf24-78bb-39be-8854-84da7f54de0c | -3.1078 | -61.402599 | 2026-09-20 02:01:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ee1111c8-6216-3335-a207-cf83e13ca90c | -2.872 | -57.805099 | 2026-09-20 02:01:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bd886481-a1f0-32bb-937e-89c0bf093071 | -11.801 | -49.8345 | 2026-09-20 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 3c811da2-5057-3002-ab8e-0fafae0c9386 | -6.295 | -47.6055 | 2026-09-20 02:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| d3db46c7-f3b6-3ee0-994f-edbc7a904243 | -11.118 | -54.0268 | 2026-09-20 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 5334267b-7676-3054-87d3-e471d530ab99 | -11.2118 | -54.0797 | 2026-09-20 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 60a313f0-264b-3f39-a98c-93f176f1c1e5 | -3.7453 | -51.8288 | 2026-09-20 02:10:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| b0865631-7d1e-3841-86b5-666a111105b8 | -6.3134 | -47.6261 | 2026-09-20 02:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 9c701cf1-6fd4-3a35-b39f-e5e496813a0d | -2.8974 | -57.8181 | 2026-09-20 02:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| f25cd5f1-112f-34bd-8a8f-8e974c6e589c | -2.8791 | -57.799 | 2026-09-20 02:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 0ce35194-3312-38b9-9fe8-29cacdd6b024 | -2.8791 | -57.8184 | 2026-09-20 02:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| f4ac6b9d-00e7-3857-b668-5d9aecec01d4 | -5.8595 | -53.5196 | 2026-09-20 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 57ec65e3-27fc-3aee-928b-e812fce052b5 | -5.841 | -53.5205 | 2026-09-20 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| deb12ffd-cf0b-39d0-8f50-b03928a2ec4e | -6.2948 | -47.6274 | 2026-09-20 02:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 177c16ea-220b-39ca-9b25-1867b61172c7 | -3.6946 | -60.6025 | 2026-09-20 02:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 6a557af9-ed56-30d5-96d8-94f2a27c9e01 | -11.3793 | -51.3989 | 2026-09-20 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| f76c99c4-9252-3ec6-8493-f646c5236148 | -7.5472 | -45.8868 | 2026-09-20 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 2467516c-3a18-34e1-949c-2c45536a494a | -11.0991 | -54.0285 | 2026-09-20 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 194.1 |
| b9d4bfa9-6a4e-3e8f-8f1e-4c7e83080363 | -7.3259 | -55.6153 | 2026-09-20 02:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 72ed5d55-5fc8-3e6c-98f9-5a40791df3d0 | -14.6851 | -46.7115 | 2026-09-20 02:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 66.0 |
| e8a635ee-f2e5-3f03-aac5-2326e34a9c19 | -8.1686 | -54.7634 | 2026-09-20 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 61ac611a-7246-31a5-8189-61d218523572 | -13.037 | -46.9096 | 2026-09-20 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 7f7a8d0a-5dd1-369d-8faa-422eabfd38e2 | -7.5284 | -45.8885 | 2026-09-20 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 159853f3-00f9-3420-a6ee-05ac6bd8b6f3 | -9.131 | -45.7273 | 2026-09-20 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 54.9 |
| cce4b688-62eb-384d-8f67-86f8f02a24f1 | -11.2307 | -54.078 | 2026-09-20 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| f50c067f-9bf9-329d-b5a8-294c946493f7 | -5.8593 | -53.5399 | 2026-09-20 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 8f4fbc47-617b-3bf2-b042-1a3fd81c5eaf | -5.8408 | -53.5408 | 2026-09-20 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 9cee9901-4377-3b0d-8cbc-fcce865faf54 | -14.6856 | -46.6886 | 2026-09-20 02:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 155429b5-1177-3f32-bc10-3d8311f0bd56 | -7.5522 | -45.435 | 2026-09-20 02:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 3237c602-b166-3aa0-8a0e-9db69d90281f | -11.379 | -51.42 | 2026-09-20 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 939a1351-c5eb-34a2-a6d2-e710af2e5544 | -14.6661 | -46.6919 | 2026-09-20 02:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 1388caed-bf1c-39d0-9758-8700248d161b | -3.7454 | -51.8082 | 2026-09-20 02:10:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 00ae2b98-16a2-3ea3-a7e8-e5d9bad3e9cf | -6.29 | -47.63 | 2026-09-20 02:15:00 | MSG-03 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 16ef79d9-eb8b-38a9-bdd5-7fc99318c6b6 | -7.5522 | -45.435 | 2026-09-20 02:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 5bd3396e-d7bc-3f81-910f-d413640c17a5 | -6.3134 | -47.6261 | 2026-09-20 02:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 33128b9e-7428-37c2-ba3b-864d875bb2d6 | -3.7454 | -51.8082 | 2026-09-20 02:20:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 3ce42874-fbf8-391a-9aa2-a0a2fdfda123 | -11.2307 | -54.078 | 2026-09-20 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| ae4d8e37-011d-3b87-be45-a03274e0e969 | -9.131 | -45.7273 | 2026-09-20 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 31e22f55-f15e-3533-a4cc-3217b4b92cd4 | -11.801 | -49.8345 | 2026-09-20 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 88b3eebb-2647-3c1c-83e1-8d942132b23d | -14.6856 | -46.6886 | 2026-09-20 02:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 160.6 |
| ce01eae4-cca0-3256-bd8b-a3a003334346 | -14.6661 | -46.6919 | 2026-09-20 02:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 67.4 |


[Clique aqui para ver as próximas entradas](README8.md)
