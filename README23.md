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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae281aea-5fd3-32a7-9067-46fae04d878e | -12.4141 | -64.1281 | 2024-11-10 03:40:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 4687839a-498b-3305-a33e-84e05181d308 | -3.9669 | -48.1716 | 2024-11-10 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 17cfa36b-dce1-3027-9cbe-2494c7f5e8f5 | -2.7772 | -49.3492 | 2024-11-10 03:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 2522e119-21f6-34af-8c02-61431c4dac88 | -2.9355 | -51.482 | 2024-11-10 03:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 0b155c04-8eac-33b0-871a-3823457a2ff8 | -2.8803 | -51.4628 | 2024-11-10 03:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| e36c7e48-36d2-3d80-ad57-cc8a8019e744 | -17.6266 | -57.5281 | 2024-11-10 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 233.4 |
| b25a02dd-cd92-3832-b220-2e1384ae6758 | -3.2428 | -53.0519 | 2024-11-10 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 1df417ee-b307-39bb-91c8-49e2802d88e8 | -1.2934 | -53.7163 | 2024-11-10 03:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 4f92d3d8-21d9-3685-b9b6-02969c622073 | -2.7586 | -49.371 | 2024-11-10 03:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 67838c72-0f18-360b-9488-c5907837394a | -3.2427 | -53.0722 | 2024-11-10 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 90d3ea55-d114-30ae-a11a-d7814526b54b | -12.433 | -64.1272 | 2024-11-10 03:50:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 35a44dae-c461-39de-88d0-bdd1a3277045 | -4.4349 | -44.6229 | 2024-11-10 03:50:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 9e24edba-0710-3920-9133-1895a64c7cc5 | -2.7772 | -49.3492 | 2024-11-10 03:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| dd12e842-7100-3ca9-bbba-8656550329ae | -3.1239 | -50.4358 | 2024-11-10 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 217.1 |
| 54845fd1-1e96-3f8d-9532-59220c5120b4 | -3.967 | -48.15 | 2024-11-10 03:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| fa44a768-c85b-3831-a2f8-b97511a4ffff | -2.9171 | -51.4825 | 2024-11-10 03:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 9ccaee70-c0a8-36eb-95c9-0a3a32a739ad | -3.9483 | -48.1724 | 2024-11-10 03:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 4a3d0230-2f10-3ef1-988d-281e8b9f4c59 | -3.2243 | -53.0727 | 2024-11-10 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 1e2ca706-0201-3300-b795-2500d76b25e7 | -17.627 | -57.5075 | 2024-11-10 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 239.9 |
| 47e604a6-47d8-3c60-90dd-28a252b48023 | -17.6073 | -57.5099 | 2024-11-10 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 306.2 |
| 0afb1b42-4e81-30d7-82c1-4119f77da4a1 | -2.7587 | -49.3497 | 2024-11-10 03:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| e372351e-c519-3e99-a0fb-1f2dfbe2d4b4 | -3.9669 | -48.1716 | 2024-11-10 03:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| a5df365e-a7a1-3e1a-bfe3-b6faa7c41c44 | -1.2751 | -53.7164 | 2024-11-10 03:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 8d8babae-9a2a-3b78-838f-838262d139ef | -3.2244 | -53.0524 | 2024-11-10 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 5856f516-cb6e-3e1a-ab1f-1ab83fefd7c7 | -2.0953 | -48.8338 | 2024-11-10 03:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 7bb3886f-206f-3b6b-9ac5-311b4cf2051c | -3.1423 | -50.4352 | 2024-11-10 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 425.3 |
| d802dcad-3c2c-36bc-8a15-f8bc2fb9db1f | -2.8803 | -51.4628 | 2024-11-10 03:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| f50a44f5-b8f2-3367-a921-2489a916b979 | -3.1424 | -50.4143 | 2024-11-10 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 2a4dd5b8-4c7a-32c5-b868-a2ddf5986b3a | -3.4383 | -50.2999 | 2024-11-10 03:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| c42f4985-79cd-36d3-8a77-7dc1d1c561e1 | -17.5872 | -57.5328 | 2024-11-10 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 34086018-194e-387d-85ad-2ba680a2abbf | -2.418 | -46.3024 | 2024-11-10 03:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 9a897dd0-74e0-3403-9ef0-a13c27cb93bb | -17.6069 | -57.5304 | 2024-11-10 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 348.6 |
| cc02f557-c07a-3b3b-8504-2188834b7c71 | -17.2933 | -57.4857 | 2024-11-10 03:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 125.8 |
| 6ed3136f-f149-3dcf-86c0-65a75dc83d2d | -3.1422 | -50.4562 | 2024-11-10 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 266.1 |
| 83a04ef0-dda7-314e-8a8f-60f7ee7d567b | -2.8802 | -51.4835 | 2024-11-10 03:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 417a3105-46c0-38c5-9ad3-a62572953226 | -3.6004 | -47.3395 | 2024-11-10 03:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| bfee30e2-5553-3666-a0da-0daac487d594 | -1.5347 | -52.2104 | 2024-11-10 03:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| ed42bd6b-22eb-3cb6-90d9-6cbfb21a4811 | -17.5875 | -57.5122 | 2024-11-10 03:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.9 |
| 2f30ec17-9aa1-389f-815b-4afca50f9984 | -3.9668 | -48.1932 | 2024-11-10 03:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| f96627ee-4bbd-30ad-b966-6780f3af237c | -2.9355 | -51.482 | 2024-11-10 03:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| b2129f37-c271-370e-ad3f-c443efd093b6 | -3.1238 | -50.4568 | 2024-11-10 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 141.7 |
| c5c14dc7-bb65-3adb-baa3-16b5db2f7fe1 | -4.1099 | -49.1315 | 2024-11-10 03:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 67c3cf3e-2c84-3bc1-a414-c076c8980711 | -3.525 | -44.0286 | 2024-11-10 03:50:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 06a71c7a-9b83-3354-94b7-46dbf18fb023 | -3.9485 | -48.1508 | 2024-11-10 03:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| c5c61705-c3b5-300f-a468-b44e5d3b39f7 | -3.6004 | -47.3395 | 2024-11-10 04:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 9b056ef8-a455-30c2-ba64-263dfdbef170 | -3.2168 | -50.2861 | 2024-11-10 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 14423bd5-beb5-36b2-bdf0-ee324feec527 | -3.525 | -44.0286 | 2024-11-10 04:00:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 6f6c95c3-17ea-335a-9afe-9231dc43a537 | -1.5347 | -52.2104 | 2024-11-10 04:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 6e0e8802-d53f-316d-a474-015b381bf10f | -3.2536 | -50.3059 | 2024-11-10 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 7674c7b7-e239-3ef1-88ac-dbf8894eea03 | -3.1423 | -50.4352 | 2024-11-10 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 459.2 |
| 76a17248-0e12-36b3-872f-743d09ac88f3 | -3.2169 | -50.2651 | 2024-11-10 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 8d1fc64e-43b5-3be7-ad32-8cb8cfbd90fa | -12.433 | -64.1272 | 2024-11-10 04:00:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 70.7 |
| c944d4ad-0c0d-3a3b-aac0-d496ac376e34 | -17.5872 | -57.5328 | 2024-11-10 04:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.4 |
| 476df9a2-aa26-32a9-877f-8cb6dd9025fe | -2.8803 | -51.4628 | 2024-11-10 04:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 65b92cfc-9e6e-35cc-aec9-e9c431bc9c85 | -17.2933 | -57.4857 | 2024-11-10 04:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 132.4 |
| feed817c-f6ad-3774-b69c-3b2f1ab71b3f | -3.2353 | -50.2645 | 2024-11-10 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| fd858aeb-0000-3e67-adf2-59ffa23b683e | -17.6073 | -57.5099 | 2024-11-10 04:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 274.4 |
| 819e3ab0-20cc-351d-ab58-c6b9c7096e88 | -17.6069 | -57.5304 | 2024-11-10 04:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 322.2 |
| 52a40610-dbe3-38f0-a6d3-4bcb34867a3c | -3.2244 | -53.0524 | 2024-11-10 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 1cba64d0-503a-387e-b172-9ed4ee21f365 | -3.9483 | -48.1724 | 2024-11-10 04:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| a1da4a59-6734-368b-9117-17d9c502681f | -17.627 | -57.5075 | 2024-11-10 04:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 237.3 |
| f7d4f8a9-b2c9-3ddf-8be4-0dbcdb1bffad | -3.1239 | -50.4358 | 2024-11-10 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 241.8 |
| b5688e5c-262f-36a4-8be0-7906adc7da6d | -17.293 | -57.5062 | 2024-11-10 04:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.1 |
| 449095b0-0445-3e3a-97bd-e53f59840f0b | -3.2352 | -50.3065 | 2024-11-10 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 148.1 |
| d5a8c6aa-76cd-3b61-9327-d2d04d8f4230 | -3.2428 | -53.0519 | 2024-11-10 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 79f83d58-6deb-3b9b-b64c-0505ea78c8d6 | -2.9171 | -51.4825 | 2024-11-10 04:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 1531ad0b-0c99-33a8-a1e3-7fcf139fc49e | -2.9355 | -51.482 | 2024-11-10 04:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 54256434-757c-3654-86ba-31e788255303 | -3.1424 | -50.4143 | 2024-11-10 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| dec0297b-a41a-3cbb-8b8c-030428509686 | -3.9669 | -48.1716 | 2024-11-10 04:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| cff5507d-0083-33d5-ab86-adf94c5b90a9 | -3.967 | -48.15 | 2024-11-10 04:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 8c719fb5-4bbf-3845-a3ae-c85c0ce3ab04 | -17.6266 | -57.5281 | 2024-11-10 04:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 229.9 |
| f90fa549-5ea0-301f-b34c-5cdf9e9ee3b0 | -3.1422 | -50.4562 | 2024-11-10 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 176.0 |
| 381be438-0686-3ccd-8905-508b51e5571b | -3.1238 | -50.4568 | 2024-11-10 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| cf3b2686-6730-345d-ad88-2baa60ac22fc | -3.9668 | -48.1932 | 2024-11-10 04:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 36a23fe8-cfa0-3a59-bf47-916ffb504877 | -2.931 | -52.7753 | 2024-11-10 04:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 9f8fec54-8b51-33ef-9d23-8790b071e6f3 | -3.9485 | -48.1508 | 2024-11-10 04:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 61805712-2b78-3851-8782-13c4270aefb4 | -3.4383 | -50.2999 | 2024-11-10 04:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| e0846c52-7c75-3cba-869f-cb3b0277eef6 | -17.5875 | -57.5122 | 2024-11-10 04:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.1 |
| ec5d4efa-110e-3dca-a772-669bb4f59490 | -3.2352 | -50.2855 | 2024-11-10 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 162.6 |
| 70296665-b47b-3dd2-bffd-39e1f901f6bd | -2.418 | -46.3024 | 2024-11-10 04:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 46.7 |
| f651fb99-a9bc-3531-9657-78feaae7af0d | -2.8802 | -51.4835 | 2024-11-10 04:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| fa024439-c43f-36c3-8d27-3e65d0e5923a | -3.23 | -50.26 | 2024-11-10 04:00:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f67fade-509e-3780-af32-c10e030ff034 | -3.23 | -50.32 | 2024-11-10 04:00:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79d3c108-a293-32a3-bb03-ef42d8e5c58b | -3.14 | -50.47 | 2024-11-10 04:00:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3ecd3f9-32d4-3451-b4f9-e77a0244fefd | -3.14 | -50.42 | 2024-11-10 04:00:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99986226-9011-3580-913b-8653ef0fea1c | -17.6073 | -57.5099 | 2024-11-10 04:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 260.2 |
| 56308650-a88f-314a-b212-9a5618ac54da | -8.3778 | -44.1386 | 2024-11-10 04:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| e813e62e-b9d9-3d32-9d1d-74419ff0b83b | -2.7772 | -49.3492 | 2024-11-10 04:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| b39b45a5-0e0a-3c40-8a47-4f84dbd4c734 | -3.1238 | -50.4568 | 2024-11-10 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 2956d5e0-fdbc-3b15-87c8-63f625acbab9 | -3.1424 | -50.4143 | 2024-11-10 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| ec6ed98b-8e27-3ad2-8656-ac5f657e7a7a | -3.9485 | -48.1508 | 2024-11-10 04:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 03cbe4b4-9fc7-3f48-99d5-b8ffc078b228 | -17.5872 | -57.5328 | 2024-11-10 04:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.8 |
| f38b3cfe-9c7c-3b3f-a46f-e74e6af2cc9c | -2.418 | -46.3024 | 2024-11-10 04:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 2d60c0e2-3e39-318e-9487-60b197af1675 | -2.9171 | -51.4825 | 2024-11-10 04:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| efecb4da-ea86-3fec-90a2-ff62e20a5e0a | -2.8802 | -51.4835 | 2024-11-10 04:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 139ef684-12f2-3a55-8042-cfb409b06caf | -2.8803 | -51.4628 | 2024-11-10 04:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 86cebebc-f5cb-3efa-9753-f9bac31440af | -3.4383 | -50.2999 | 2024-11-10 04:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 279c4207-35d1-33bf-87c0-7daa722b100f | -8.3967 | -44.1365 | 2024-11-10 04:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 0c08bf46-1793-3a6e-b455-fe0a6828abec | -8.397 | -44.1133 | 2024-11-10 04:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 397e8089-aaad-37de-ac63-70f7e5846c75 | -17.627 | -57.5075 | 2024-11-10 04:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 235.5 |


[Clique aqui para ver as próximas entradas](README24.md)
