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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8d08dcd-1ae8-3bc3-9bd5-e7db051a9a71 | -6.99309 | -59.04824 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2bf298e-9afc-3582-a832-4cc25d4f19d4 | -8.97149 | -60.5112 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ef05551-65d3-30c3-8f34-7a4b997633c3 | -6.70835 | -58.93967 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7fd3b0c2-7813-3672-bc99-b893152123a1 | -7.56207 | -60.85407 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6984fc14-a21c-30f9-8946-f880720c6f9b | -6.85758 | -58.97839 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a38bc14-cfc6-32e0-845e-918c3adec3b9 | -8.09356 | -61.35763 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 54b4a4c8-998a-3d27-b5b9-a9ba556d0da0 | -7.14264 | -47.52979 | 2026-08-17 05:16:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b00727e9-2457-3b80-99cd-10cf1692c3e9 | -8.58269 | -54.68779 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ac2dd3e3-4a0e-3cfe-bc3c-baa2b359fbdf | -6.04287 | -57.69877 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e649de48-fcbf-365c-8fe2-bb29ca039cf0 | -6.82858 | -56.43756 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc92d80b-a1ce-3bff-a467-4ebb4d6e24c0 | -7.87842 | -63.75153 | 2026-08-17 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a96b0b7c-940a-30ba-85cc-1cd51ced0727 | -9.15845 | -59.67415 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc101d44-b9ae-3cf0-b2e5-af5bc415901c | -7.37717 | -55.49572 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58c44df7-0ec7-37da-ae35-88bf83f19c9f | -7.4279 | -60.021 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d842fe5e-ea44-35df-92e6-0d00415fa58f | -8.90039 | -60.56467 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f72a68e-3ce4-33a6-837a-d9a7e7d668e5 | -7.38014 | -59.99467 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d991fcb6-8fc8-35a6-b7ab-497b138e5e52 | -6.83196 | -56.46001 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 888bc1ac-b5a5-34bd-b58a-45810ab80ea7 | -11.10333 | -47.28431 | 2026-08-17 05:16:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 685bcae5-5c7a-3763-b3ea-020a221030b2 | -6.70949 | -58.93253 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c208098-2590-3624-9d7b-337278a93553 | -8.97258 | -60.51683 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e7da485-b7d3-390a-9c42-ddd8a42c6d66 | -6.77927 | -59.46106 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1469b6c3-12df-3f6c-bed8-07428fd5a492 | -9.17929 | -59.67383 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d29f298-c2ba-35d6-8c67-93e47f88e315 | -8.96595 | -60.53564 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2b0d28f-e745-3f0e-8beb-72078b3729cd | -6.72071 | -58.92701 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e4bbae2-0c5a-325a-8dfc-c19d28ca3ea9 | -4.94297 | -48.40339 | 2026-08-17 05:16:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e6fb6d3-6609-30e4-950d-1da2362fcfeb | -6.54411 | -58.49936 | 2026-08-17 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89207ece-2209-3d2c-938e-3c67ec1dc5ef | -9.37074 | -57.35653 | 2026-08-17 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cefda5a4-21dc-3d07-814e-526b31772e46 | -8.58333 | -54.68346 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d558dc43-5c00-3f87-8384-866b8c18e560 | -6.8475 | -58.97676 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fea2e70-5fea-3741-8b22-c8fd06fba497 | -6.62859 | -59.0706 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5daedc5-66e6-3094-8b73-cb15d27cd7ac | -7.54655 | -61.37616 | 2026-08-17 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbb39284-9ab5-324b-ba87-0675295a8290 | -6.86265 | -56.41729 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa5a049f-f2ce-3d99-9c6d-107cffcd5b19 | -7.40409 | -60.02209 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5e04c48-6809-3a1d-8db9-e54be62a2cfd | -6.10542 | -57.73387 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 29af6a65-0f4a-3995-9335-ca2945718816 | -7.38377 | -55.48815 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40fc1313-e261-3d95-9b20-7e6fa15accff | -6.10873 | -57.73439 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7e2a6b12-edfd-3458-92d5-28786bf5d1e5 | -7.52841 | -60.68592 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c17e7803-20b6-3762-8bd3-353db3c17c99 | -6.63259 | -58.96051 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 53f8d9bd-bf16-3ee3-adb1-a7322129dbe4 | -3.24356 | -51.56048 | 2026-08-17 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 137fa917-05b2-3b36-b148-179538398da6 | -6.96004 | -59.03921 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1c92221-5131-3613-9179-994cad3c1d7f | -7.58572 | -61.20976 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92c29798-047a-3b4c-96a8-e0e12c76ee2c | -7.3748 | -55.51102 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d46ea659-10ab-3050-a9c5-ac6405b5b42b | -8.72903 | -62.89919 | 2026-08-17 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c371e01-d5a9-32c7-a9fd-f90106eb6b79 | -8.95867 | -60.51452 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b956cd7d-96de-38e6-a3b2-13cb0c8fe2ab | -8.60044 | -54.66858 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a084bd68-ed04-3244-9605-b3b2bb9fe894 | -6.98195 | -59.03173 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6425fce9-099d-3fcb-8ed8-757cfe812f12 | -6.77987 | -59.45738 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94f4ccc3-e0aa-33f2-a9af-8e409d61ae95 | -9.05609 | -60.38722 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7c7ca80-fb94-3bfd-aca6-6de5bed94463 | -4.1217 | -56.33353 | 2026-08-17 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1af397a2-36bc-3d3c-8edb-62f0c48cd706 | -8.97845 | -60.51233 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 448eb627-cb9d-3a5e-84aa-a4fecb31e4cc | -6.62135 | -58.96603 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9b5b7dbb-990d-3089-a1e1-978f834e3234 | -6.64152 | -58.96933 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3503eb3c-fc30-3333-9e56-bf74c2c38ad1 | -7.45646 | -59.99835 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 81aa978b-6e45-3efb-bf0c-79b201a5da86 | -6.83348 | -58.9782 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0eb87315-f67f-3759-abb2-f4fca1b78336 | -8.97522 | -60.5317 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 169c7d3f-ca86-3bd0-836d-930eacf7a541 | -8.06442 | -48.53234 | 2026-08-17 05:16:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1f8bf10b-d82b-3f62-8044-d49fa4d426bc | -6.82077 | -56.44363 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 895fbfc0-d228-362f-981b-84e044669c83 | -9.12798 | -46.01702 | 2026-08-17 05:16:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b90c06b9-67db-3530-a28e-036b788bcb6d | -6.02314 | -57.82317 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5567f9eb-abea-35db-804d-35bf32254f6b | -6.85028 | -58.9809 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85395756-02a7-3a8e-9df4-e36dfe59bca8 | -7.37193 | -55.50663 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf1043ba-30e9-3aef-8b84-211dfe665baa | -6.83027 | -56.44879 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4c86b90-e253-3be8-8a29-0fdc776dbb08 | -6.605 | -58.39377 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5994c359-f956-397c-86ed-cc0bc7cec6f4 | -6.1181 | -57.73942 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49a54992-23db-3ad0-ac0f-4979a7d7e63d | -6.63093 | -59.05616 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b94baaa1-4167-309d-aca1-a479c49140bf | -6.62697 | -59.05923 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 832fc4f8-dfa3-3f0e-981a-55c6085ab105 | -7.37683 | -55.51059 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d770c5b-8fa1-398a-983a-47088f7f13c6 | -7.55433 | -61.17378 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d01c53c-436e-36c2-8ec3-bebab2220736 | -8.98926 | -60.59787 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fd3eac4-02d4-3f41-94bb-89f709dad5a9 | -8.50924 | -54.90321 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12937547-5af8-3c92-9bfb-b96d9de3c1ee | -6.82302 | -56.45129 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46bf67b2-0afa-3263-b358-3c74c4d51943 | -6.96283 | -59.04335 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7e1f456-d7e2-3a05-ba87-418a4fc76655 | -2.86021 | -51.81314 | 2026-08-17 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47a31252-eb7c-3236-812e-b4cd6672828b | -4.9482 | -48.40415 | 2026-08-17 05:16:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da5e6929-1049-3f15-abbe-260971da7002 | -11.13398 | -46.51352 | 2026-08-17 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2c3557cf-8b86-3030-a7c2-101cb1d8f769 | -7.87772 | -63.7555 | 2026-08-17 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a7b6fb6-e903-3681-b348-81794466383c | -8.90159 | -60.60085 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e9ded8a5-f17b-3993-8ec3-f0c2f4dc78fd | -7.39476 | -55.48593 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6de11f88-c622-3713-89e5-570de97a230d | -7.49994 | -60.08016 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20bc85af-eec1-3c53-a4a0-eb255f5024c5 | -6.8431 | -58.96137 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 239be4a9-a089-319c-ac7c-0fb90b48fe5f | -6.83301 | -56.40901 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8281058e-d0de-34e9-b418-bf8752bd5b65 | -6.59774 | -58.97352 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d579789c-4097-3b59-bdc3-3ee2bd12dedb | -7.89026 | -61.79916 | 2026-08-17 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cd6c448-dc02-3c92-a411-378a96e0e233 | -9.12787 | -46.01574 | 2026-08-17 05:16:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61a24cf9-fcc1-3779-8c47-6df4253bf73b | -9.546 | -56.80077 | 2026-08-17 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a29dfabb-8e50-3d60-a6ff-238299d0f465 | -9.15904 | -59.67052 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 567b51fb-6b45-38d3-a266-23285b39834e | -7.55461 | -61.17109 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78092b17-6390-33dc-b1f5-5a15af803832 | -8.6415 | -54.71872 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9678a427-41a1-3f63-b4b5-58f17d7151c0 | -6.12581 | -57.73356 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31482267-f0ce-37a9-8f8d-28c0e35722ed | -6.11755 | -57.74288 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cfe5a9a-c158-388e-b062-d74d40888ba5 | -8.97973 | -60.50461 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4247f2c0-17e6-375c-a257-504468aff2da | -8.58673 | -54.68563 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| b6ded766-8e73-3a9a-aee7-2aede9580612 | -9.48313 | -51.67303 | 2026-08-17 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f378ca1e-d77e-3250-9c32-1bc783764be4 | -7.37658 | -55.49954 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7adda9d3-969a-33e2-8f39-123e462cdff1 | -8.59063 | -54.68454 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 81eeec94-04ec-3de3-ab4a-a831725f34dc | -9.27504 | -56.90306 | 2026-08-17 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e57b028e-69e9-3a71-9cb3-f05c0408b639 | -8.58572 | -54.69259 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| afbb00d1-fda2-352b-a1c8-309762da3671 | -9.1765 | -59.66965 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77c80b10-6e75-3586-963f-6650d5751810 | -6.89443 | -59.00644 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55e38b4e-cb73-304d-b94d-d0f468e70341 | -6.6443 | -58.97345 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README45.md)
