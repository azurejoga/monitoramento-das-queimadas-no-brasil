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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6854a892-c47a-370b-adfd-6259c285c2e8 | -2.69 | -53.3497 | 2024-10-10 04:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 8fb10417-9c1d-3e6c-9165-b6151b31f236 | -4.0961 | -48.2739 | 2024-10-10 04:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 6b81f408-d88d-3cd6-a434-b7ed405e5db2 | -4.0962 | -48.2523 | 2024-10-10 04:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 20c0b70c-0cf1-3e83-82bf-8c80884196be | -4.1146 | -48.2731 | 2024-10-10 04:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 3bea6ec8-132c-382a-ad12-cf86f5a52566 | -4.1148 | -48.2515 | 2024-10-10 04:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 150.7 |
| de3dc79f-c86f-314e-b89c-dc7afafc37d5 | -6.7654 | -59.3252 | 2024-10-10 04:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 6d1eb171-b4dd-3361-bf62-6c06e875d746 | -6.7655 | -59.3059 | 2024-10-10 04:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 03a87bb4-4ca9-3006-ad19-8f4ef3a755d9 | -6.7839 | -59.3245 | 2024-10-10 04:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| c02314e5-ccf2-3437-9d9d-09ad4dd8c549 | -6.784 | -59.3052 | 2024-10-10 04:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| cc18dede-da09-314c-bf95-9131a95f1e4c | -7.0417 | -59.4103 | 2024-10-10 04:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| f2b74ec4-1389-367f-ada0-c64e0a8f77c9 | -7.0601 | -59.4095 | 2024-10-10 04:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| b0683761-15bf-3ab4-9d4e-23713cccf405 | -7.0786 | -59.4087 | 2024-10-10 04:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 150.8 |
| ee0ad3e1-03b5-33ad-8878-e8993cbcdc84 | -7.0787 | -59.3895 | 2024-10-10 04:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| a25bcab3-6220-30d2-8370-4e8676ee7b94 | -7.0971 | -59.408 | 2024-10-10 04:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 02276745-abdf-3f7b-bbfb-5b68742d3c31 | -9.0842 | -61.3925 | 2024-10-10 04:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 592fbffc-3095-33da-9ad7-aecf29268b09 | -9.1035 | -61.2769 | 2024-10-10 04:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 62408a6d-90a9-365a-bcd3-0378cb995a88 | -9.1221 | -61.276 | 2024-10-10 04:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 8eedaadb-5b6c-31b7-8133-a9a89943e301 | -9.1223 | -61.2569 | 2024-10-10 04:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| abe83529-baae-3a89-af1e-f1a34d87ef2b | -10.3632 | -55.8554 | 2024-10-10 04:26:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| d1459861-a6ac-36db-a7a4-dd95c2d085ff | -11.0254 | -57.2237 | 2024-10-10 04:26:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| fab74fd8-2b32-3107-8cef-d552afed7709 | -11.0256 | -57.2038 | 2024-10-10 04:26:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| eed151e0-4d42-3f24-9c4a-f9dac2e05b78 | -11.0443 | -57.2222 | 2024-10-10 04:26:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 9fd25e5e-4258-32ce-9c45-7a1ecabbbd65 | -11.0445 | -57.2023 | 2024-10-10 04:26:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 35590bf0-b0ab-3614-9393-08b1c87cc5b9 | -12.3067 | -59.1641 | 2024-10-10 04:26:16 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 69c68bb9-32b1-3eb0-8f59-3f9322d4c3be | -13.8579 | -44.4949 | 2024-10-10 04:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| f6b4406c-10dc-3499-8711-dcfa68debdc5 | -2.6533 | -53.3506 | 2024-10-10 04:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 03f2f559-e319-3213-96f5-daa3e013238e | -2.6533 | -53.3303 | 2024-10-10 04:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 76c8fb5b-08f1-35f5-a901-f7c28c3542c6 | -2.6716 | -53.3502 | 2024-10-10 04:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 226.7 |
| 78613325-c626-3c7d-9ab5-364d0636c797 | -2.6717 | -53.3299 | 2024-10-10 04:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 138.7 |
| 6dc1e432-6081-3b35-9482-0aeb8a2e3a4e | -2.69 | -53.3497 | 2024-10-10 04:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 13850e7c-486f-34a3-8905-3ac9e94bba42 | -4.0961 | -48.2739 | 2024-10-10 04:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 0c2ae49c-511e-35bc-bfd6-675646dc7548 | -4.0962 | -48.2523 | 2024-10-10 04:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 0f3393dc-a1f3-3161-a84f-836735e82a0c | -4.1146 | -48.2731 | 2024-10-10 04:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 7cebf8dc-fc6a-3799-bdff-01584689bd60 | -4.1148 | -48.2515 | 2024-10-10 04:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| b221e5a1-16b6-311f-8dcc-5cf26371351e | -6.7655 | -59.3059 | 2024-10-10 04:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| d6250967-aa68-3659-832a-bbb1331adf2b | -6.7839 | -59.3245 | 2024-10-10 04:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 99205b2c-9246-3d65-a921-e564b3dcc7ae | -6.784 | -59.3052 | 2024-10-10 04:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 85146aba-93d2-3284-8532-1692171f83da | -6.747 | -59.3259 | 2024-10-10 04:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 9e2ba970-c697-340c-848d-4b37f295d315 | -6.7654 | -59.3252 | 2024-10-10 04:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| cd5f0a15-4800-3ba4-92a8-c6592ddf8400 | -7.0417 | -59.4103 | 2024-10-10 04:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 31e56308-eeef-3ef8-89e1-e94aa57b1796 | -7.0601 | -59.4095 | 2024-10-10 04:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| e78c4ad2-3bf1-370a-be80-594abdad3f2c | -7.0786 | -59.4087 | 2024-10-10 04:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 171.8 |
| bd9d356d-0764-3402-91a2-64c9df075979 | -7.0971 | -59.408 | 2024-10-10 04:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 9bcad674-0528-3df3-abf8-8ba506c0b743 | -9.0656 | -61.3934 | 2024-10-10 04:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 2caf6791-cc93-3477-b007-faf4944d4547 | -9.0841 | -61.4117 | 2024-10-10 04:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 0afec7fa-01db-3bb5-92dd-d4f97582759a | -9.0842 | -61.3925 | 2024-10-10 04:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 724356bb-2291-32da-af6c-25871e6b6951 | -9.0843 | -61.3734 | 2024-10-10 04:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 6da4a1bd-729d-3188-9281-185ee1ccb0ec | -10.3632 | -55.8554 | 2024-10-10 04:36:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 05bb97ae-1b9a-36f7-85a2-ec12dd6aa349 | -10.6832 | -51.0907 | 2024-10-10 04:36:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| f9c7d82f-5573-315e-95f8-7b15e881229f | -10.6643 | -51.0927 | 2024-10-10 04:36:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 552c3afa-fb85-3687-9cb5-4340bd606d0e | -11.0443 | -57.2222 | 2024-10-10 04:36:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| a24dee24-c4e8-35e9-8af0-6d999f466f69 | -11.0254 | -57.2237 | 2024-10-10 04:36:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| ebe64dcb-985f-32ac-ab5e-d5cd077920ed | -11.0256 | -57.2038 | 2024-10-10 04:36:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 4def80ce-1973-3084-99eb-9d98471665e6 | -11.0445 | -57.2023 | 2024-10-10 04:36:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| ce732af4-b4fa-3220-aa07-b7b800cace1d | -13.8574 | -44.5185 | 2024-10-10 04:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| a9a76ff2-fcba-3efd-bc14-8924cb6a667c | -13.8579 | -44.4949 | 2024-10-10 04:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| a0dccc6e-55ae-3d17-a1d0-ce9c7b70fbe9 | 3.29936 | -51.35989 | 2024-10-10 04:40:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b0ba27b-cb3c-3529-b106-0b4fd30442c1 | 3.29525 | -51.35656 | 2024-10-10 04:40:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28a39e5f-ed5a-3392-b64c-40843156fb4a | -1.51152 | -61.59734 | 2024-10-10 04:42:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 538c6f10-9b6d-3601-a24c-13a0f669d288 | 2.05645 | -50.9189 | 2024-10-10 04:42:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e1902eff-c8e4-32f5-917d-2d8c4f329008 | -4.38718 | -41.458 | 2024-10-10 04:42:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3d8d7831-7d3d-3e52-9cab-af75837b1134 | -5.81601 | -39.08234 | 2024-10-10 04:42:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a75acd60-5f14-322a-af9a-08dd5b5a6541 | -5.81369 | -39.08014 | 2024-10-10 04:42:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a0ef4a00-69ab-3cfd-9661-8a85cf4de17f | -5.80967 | -39.08146 | 2024-10-10 04:42:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e4f30fb8-ed9e-3453-96a8-0ed3688d6a23 | -3.95972 | -41.48296 | 2024-10-10 04:42:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4bf94226-5012-3f4c-82fd-0e3d14c36359 | -3.95923 | -41.48618 | 2024-10-10 04:42:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f78902cd-2725-3ba9-8eef-0081cce2aced | -5.19477 | -41.30542 | 2024-10-10 04:42:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 27867d1e-1b6c-385e-821b-7a3f74908b36 | -5.19429 | -41.30885 | 2024-10-10 04:42:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cffed568-9d24-312c-8cc2-d2ee3feae5df | -4.95012 | -42.98438 | 2024-10-10 04:42:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 84824d10-956d-368e-b415-24233a678eaa | -4.94936 | -42.98969 | 2024-10-10 04:42:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c6d687de-7d78-35eb-9838-87954a919a87 | -4.9486 | -42.99497 | 2024-10-10 04:42:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c6845d0-ce94-3d53-aaad-6ec9f58cb25e | -4.94529 | -42.98365 | 2024-10-10 04:42:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 86d202d7-2c1d-39a3-9b2f-c545f36c1873 | -4.94453 | -42.98896 | 2024-10-10 04:42:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 86cd3d7c-ec34-34ef-a999-ec93be139d09 | -4.94377 | -42.99426 | 2024-10-10 04:42:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb5ec801-6df1-3c04-83cc-08cd1af8f8e6 | -4.71632 | -42.94928 | 2024-10-10 04:42:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8b3b931-5a5f-3139-88ff-c2a9fa97a08c | -4.716 | -42.94604 | 2024-10-10 04:42:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6ad7ed3e-edc3-3db6-a8b9-c90d7812d0e9 | -3.29988 | -43.5107 | 2024-10-10 04:42:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5bb63735-48bd-3679-ac02-507b3d63cc10 | -3.45821 | -44.28194 | 2024-10-10 04:42:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf574f32-b1c5-3476-99b6-f29fd76b6317 | -4.49734 | -43.8468 | 2024-10-10 04:42:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e97a5328-2129-3627-a157-f48fc9526c20 | -4.49283 | -43.84611 | 2024-10-10 04:42:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b111548f-db59-30a5-ad49-57f80ca6df93 | -4.40408 | -43.52217 | 2024-10-10 04:42:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36bd166f-530f-306a-add3-dd3c950962d1 | -4.39959 | -43.52481 | 2024-10-10 04:42:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44e23cfd-a4fc-3da6-884d-9a453d31bd51 | -4.39496 | -43.52419 | 2024-10-10 04:42:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec5062b8-e698-3f99-bccf-04af114db75a | -4.02621 | -43.23774 | 2024-10-10 04:42:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 962f8df7-b50b-31c6-8ed1-a3f937564425 | -4.02442 | -43.23509 | 2024-10-10 04:42:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f835e96c-085a-311c-ad5f-092b9f007286 | -4.2841 | -44.38545 | 2024-10-10 04:42:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d062811f-6f52-3beb-b4cf-e6c5a7e01302 | -4.28225 | -44.38712 | 2024-10-10 04:42:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3afc5c0e-9973-3a91-95e7-270c3e855b63 | -4.2817 | -44.40196 | 2024-10-10 04:42:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1b3a73a-5c98-37ba-8453-7851a04d7df7 | -4.27973 | -44.40359 | 2024-10-10 04:42:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06a1b71c-de59-3070-931a-d5311cd80282 | -4.0454 | -44.26073 | 2024-10-10 04:42:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37171e19-909a-3e0b-a36e-5a7436e6a6ed | -4.04476 | -44.26495 | 2024-10-10 04:42:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c06f0c91-3825-336a-a6c4-20037b8b663e | -3.78676 | -44.3683 | 2024-10-10 04:42:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9082b14e-e223-39ba-ba04-c694dc998cd4 | -3.78614 | -44.37243 | 2024-10-10 04:42:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 544c88aa-0096-3188-92e2-2021daa2de85 | -4.8187 | -44.35396 | 2024-10-10 04:42:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42fef91b-2022-30e5-845f-1319113a4972 | -4.74406 | -44.58351 | 2024-10-10 04:42:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cef41353-36d6-3243-b2ab-889b554d5ee7 | -3.21975 | -45.45248 | 2024-10-10 04:42:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad9b19e4-9969-3818-95f7-00a12d5350ee | -3.21923 | -45.45589 | 2024-10-10 04:42:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 998ea0ea-134a-312b-939c-e4bf4b1ef475 | -4.49516 | -45.71365 | 2024-10-10 04:42:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8b10a4c-e6ee-34d7-a05c-8806f5cd439a | -4.49118 | -45.71299 | 2024-10-10 04:42:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7377a5e-2705-3ba6-95c3-23cf1f6e4555 | -4.46344 | -45.89495 | 2024-10-10 04:42:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README85.md)
