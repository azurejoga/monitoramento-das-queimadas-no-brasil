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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82563b79-49d6-33e9-b7a6-7b70e352b329 | -9.10401 | -60.92419 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 43a8e6e6-6a83-338e-bca1-29dda13e5ed2 | -6.80851 | -59.42542 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4e5f94a5-edd1-33c6-8a74-2bc23b6ce3d6 | -6.86838 | -59.4287 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c8e4446b-7954-3dde-9071-0618badc611b | -6.74749 | -58.67207 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 41dae8ca-3578-3761-9513-541e228ea933 | -9.17627 | -59.44636 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f7beee2b-be9d-36aa-8d30-ea63bbfa50d9 | -6.82381 | -59.41029 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a1f53478-94e0-3fbc-a330-7846886880de | -6.75598 | -58.66047 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 49bb4ecc-d027-3047-b820-cdc2a5179ffa | -8.39851 | -62.69295 | 2026-08-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 672eaa28-03ef-3805-ba9c-b8e7b311f4ad | -6.69287 | -58.93672 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 46df34b5-8d7a-3b3c-8313-9e0808256a29 | -9.16568 | -59.45814 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f33c6a2e-dce1-3a24-92a4-7ce284e3906a | -9.04107 | -60.44563 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81f7acdb-ec0a-39d5-b2e3-37a36e771ce7 | -9.18149 | -59.44167 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7d91cb1f-d96d-3718-9afa-70703199c18d | -7.60594 | -60.95303 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7cd9016-cb86-389c-a880-7716e5fc0f9c | -6.12031 | -59.91785 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3980bbd3-f3d3-35df-829c-033107c23e89 | -6.77495 | -58.67623 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 141c2a9c-808c-355c-b526-753604e931e2 | -6.36358 | -62.89571 | 2026-08-22 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abac617c-175e-3097-8229-51515add2eb4 | -6.11603 | -59.92281 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b5bb608-cab9-37c3-a3dd-9f05a6d73cb1 | -9.11807 | -61.59055 | 2026-08-22 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 410eb3f1-c120-3c39-bc19-9b61b11240e9 | -6.14069 | -59.91043 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e11cd1e8-6f0f-34d6-8168-f8d91824c812 | -6.80428 | -59.66713 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4997f923-b65a-3933-b938-ea04116bb066 | -6.53379 | -58.52827 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d2031541-7c3f-31af-bb82-57c073299e2a | -9.17243 | -59.45907 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 49b7c472-73db-35f4-ac4f-5019c4959960 | -6.7928 | -58.6467 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| a5e2e660-8b80-3efc-bb1d-f0e022e49ebe | -9.16734 | -59.46378 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 58b2f22e-2d08-3d4e-93bc-a1ccbd96c75f | -6.37275 | -62.90681 | 2026-08-22 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a30d91e4-c6f5-3634-a9c3-a3ac0001d043 | -6.9654 | -59.04846 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 0d08b95d-048c-3f82-b70e-c918cbde88d6 | -6.13833 | -59.90016 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab98002b-48ae-37ad-95c0-9270aeb6a236 | -6.81211 | -59.40945 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 49d67892-69da-348b-b996-7766a6b84465 | -6.13647 | -59.89422 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 719313d0-4c89-327f-af51-0c97d6debc72 | -6.13366 | -59.9146 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d309382-b326-3967-a694-53f25ca1c181 | -8.90332 | -60.54181 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| edfae1f0-49b8-3073-9baa-d7fe6577ea94 | -7.60655 | -60.94848 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 943c0b3d-af4c-3d24-921b-eb8d54614dfd | -6.54205 | -58.52135 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| df0877ea-b3bd-3e4a-9caf-0191d4601606 | -6.76975 | -58.66229 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 78cb0f46-5dd6-3783-bb89-986b77b9e117 | -5.91213 | -61.2938 | 2026-08-22 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a708e31-3f34-348c-8df6-254c4836082b | -8.40491 | -62.68665 | 2026-08-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e00ba406-6fc9-3653-bd41-affbe10acd44 | -8.89622 | -60.59759 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3aa542ea-96ed-3e42-8877-0bb204bffb27 | -9.18072 | -59.44777 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 79ad1112-da61-36e7-b4ce-380aae525374 | -6.7909 | -59.41778 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 9e78e4a4-8135-31db-9cde-45893c5b04e5 | -6.36314 | -62.89619 | 2026-08-22 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa39055a-cc24-3839-9694-3b4287e53db1 | -9.17699 | -59.44024 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0518aaa0-86ae-3c4b-ba9e-4e4b41dbe86c | -6.96093 | -59.05218 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0d70c86a-eb87-322c-939c-e6388f6e79ae | -6.88083 | -59.43604 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 689b35cd-2785-3b2e-b7a0-523116b601de | -9.40739 | -60.43843 | 2026-08-22 06:08:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 391cabd2-581a-398d-9d07-f8705adc7d0d | -6.90178 | -58.99113 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4aeca9d5-9314-3c19-8c51-7fabca4abc21 | -6.12434 | -59.90847 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76638768-7f04-3ef3-ab9d-c9dd2946bed9 | -6.86511 | -59.02776 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c82e9304-1af9-34d5-bd11-3755b84f12a1 | -6.94235 | -59.3098 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f6250f9-37ee-3176-b66d-fa273855fb35 | -9.41124 | -60.40691 | 2026-08-22 06:08:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a2165346-8f95-3e26-8470-c1297b42b1a9 | -7.55135 | -61.17678 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da17c32c-3556-3cbb-b767-da2d9e8b2da0 | -6.54121 | -58.5276 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a63eddb0-c73c-3fe7-8e95-e9d613c5db27 | -9.18302 | -59.44736 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a171337-4afa-30c9-a6fe-7973fc63e4d8 | -6.93571 | -59.30886 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 57276532-ebcb-3bcd-b97f-06fcfcdca0dd | -8.38808 | -62.68769 | 2026-08-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.0 |
| f20f6d12-12c8-355d-b722-9abb0b998989 | -6.54297 | -58.51456 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5a988fe6-8b7e-334e-bffc-66a49fff9c44 | -6.85815 | -59.41628 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f2158ce0-3adc-3352-8663-b02ca7c72e4f | -6.76675 | -59.44888 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f0ae0afa-5504-369c-8b1d-e68034c135e6 | -6.80247 | -58.62942 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f6e1fb22-aab8-32fb-821d-6a3621ac9134 | -7.60166 | -60.95286 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 810c9b45-6b9d-38d6-8c8e-7b0c6dcd6e27 | -6.87498 | -59.4295 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9aad984d-6245-3dbc-8bec-c1db95a592f2 | -6.77244 | -58.69556 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| a1c11c4f-9cb3-3005-a455-468598e36454 | -7.86056 | -63.76815 | 2026-08-22 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03776f4e-0697-306e-bd48-77178c2c16d6 | -6.12301 | -59.91869 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8af5563e-6e62-3aae-acd0-b68e2858af67 | -6.79204 | -58.65253 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| fa3d1078-dfb3-3e6a-8cd2-bd837dec09c6 | -6.90775 | -58.99793 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 533a363a-9e39-3065-8aed-fa66958de024 | -7.02483 | -59.55376 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40670b14-06b9-3521-9d37-58ad44914295 | -6.94036 | -60.08841 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9689c200-170d-313e-9d07-630983d3f4ad | -6.53428 | -58.52681 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 375d9f75-b2c1-3457-979f-4fde9cbd81d5 | -6.82326 | -59.67503 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 5683d19d-1e48-3aa3-9e72-99e253231d91 | -6.80922 | -59.41972 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 75d9e4c1-2a01-3381-b85d-6679f6f0865b | -7.60224 | -60.94833 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54a09114-f719-3c7e-8e3e-08541dd29b9b | -6.87351 | -59.44085 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 864bc0b8-5641-3345-9d58-1c1b6f5a8fa5 | -7.60711 | -60.95835 | 2026-08-22 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 23b5ecd4-8a0b-31ae-ab4a-0ef37057c759 | -6.85157 | -59.41531 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eb34b532-ce1a-3f22-9941-7f0b577a7750 | -9.18977 | -59.4484 | 2026-08-22 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60cc8a69-116e-36a6-87a0-a2a195708cc4 | -9.4106 | -60.41217 | 2026-08-22 06:08:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8d288cfb-48df-3b67-98f9-e03a1f730783 | -6.77578 | -58.66982 | 2026-08-22 06:08:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2b15548f-669e-3fc9-a236-ee0f178d033a | -6.97364 | -59.06023 | 2026-08-22 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 23498d52-f7c0-3c46-87e2-3d69c97477bb | -6.7832 | -59.4401 | 2026-08-22 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 3bb40fd8-f9da-39aa-8dee-c194fd8dc0fd | -8.522 | -54.8209 | 2026-08-22 06:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 23eee955-75de-385c-b581-9a085a78c514 | -6.8202 | -59.4194 | 2026-08-22 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 44f6f714-6ccf-3871-a65b-0f98ce85e04c | -14.3744 | -51.8038 | 2026-08-22 06:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 80cc696a-7d3f-38b7-9e11-49e4bfc41031 | -6.8018 | -59.4201 | 2026-08-22 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 209.8 |
| 9cb30b11-1eda-35f4-8a28-9860c346a69b | -8.5406 | -54.8197 | 2026-08-22 06:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 6f79955b-afff-3b79-b091-b180e327cf4c | -9.1722 | -59.4629 | 2026-08-22 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 4f38ec49-12f0-37c1-9b11-fd3bc08c1852 | -6.7691 | -58.6873 | 2026-08-22 06:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 99a58686-5800-3a55-acb2-b0b73e904d41 | -6.7692 | -58.6679 | 2026-08-22 06:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 595a22f9-9d1d-332c-a4a8-2c14a629d686 | -8.3903 | -62.6963 | 2026-08-22 06:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 182.2 |
| 5dddbb7b-15e2-3c8b-b62d-f1ca7a018ac2 | -8.3904 | -62.6774 | 2026-08-22 06:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 178.7 |
| 3199c28b-3cf5-3382-adb1-01b653bc9290 | -6.7507 | -58.6687 | 2026-08-22 06:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| e2b030a9-f700-397f-b8ee-168ab7433e22 | -6.7833 | -59.4208 | 2026-08-22 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 129.7 |
| 4eb42215-3fa7-3e92-8c5a-9a77d291e300 | -6.8017 | -59.4394 | 2026-08-22 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| cff4b495-a580-3736-a553-80673c9e9efa | -9.89219 | -67.43281 | 2026-08-22 06:10:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9af06aa-6c7a-36d7-a775-290d83faef54 | -6.8018 | -59.4201 | 2026-08-22 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 190.2 |
| 7c034d8f-4fad-3612-a7b9-294f5e4c2060 | -8.3903 | -62.6963 | 2026-08-22 06:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 175.7 |
| befd7f9b-2ebd-375b-b441-4133e3fdc4bc | -9.1722 | -59.4629 | 2026-08-22 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 87462c6f-48ec-3d91-8267-0ad323182e72 | -6.8202 | -59.4194 | 2026-08-22 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| b871ccf2-5b84-3f5b-b899-c968961bb921 | -6.7692 | -58.6679 | 2026-08-22 06:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 959b0caf-014c-37ff-b5b9-69e43fd4b490 | -8.3719 | -62.6781 | 2026-08-22 06:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 354d5b2b-b5cf-34d3-b71f-a0675d4a173a | -8.522 | -54.8209 | 2026-08-22 06:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |


[Clique aqui para ver as próximas entradas](README81.md)
