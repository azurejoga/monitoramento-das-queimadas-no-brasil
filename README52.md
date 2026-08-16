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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2739de8e-fff5-302a-a838-4ff54ec501d4 | -13.70138 | -51.88028 | 2026-08-16 05:36:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6ed8688-f564-3ca8-b64c-efc6cd6c89f0 | -6.97883 | -56.46456 | 2026-08-16 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba287500-9978-35f2-99e0-6bf4fecbc5f5 | -7.33811 | -59.60192 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c2f88780-b62f-3082-af4f-b57e5e29a94e | -8.96628 | -60.51695 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3baeb581-7d0c-3264-8336-5b38f03a9a59 | -8.95212 | -60.58594 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08129113-56d0-3f0b-bb1b-b13e77d9be69 | -7.58449 | -61.23789 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59c7b179-eb99-37b6-9aee-004281de06b1 | -6.85584 | -58.96215 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a77f5786-52f2-3e44-a341-59770aa5b4df | -8.98479 | -60.52334 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c53dcdd7-dd48-3245-890c-28c0a03cac25 | -7.38407 | -59.98866 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4f49a8c-03fd-3751-aa0f-65d8a15d2218 | -7.58893 | -61.20913 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6dcbdb91-cb6b-3669-b9a9-013c77b04a3a | -9.14497 | -68.20422 | 2026-08-16 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f2f85fa-f29d-3976-b64e-1683b29d8c82 | -7.35006 | -59.59542 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4db2947e-fd65-360f-b9b6-c97933b8cfa7 | -8.96738 | -60.53297 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fa6c17d1-ccab-3f7e-83f8-cd9652e7ca78 | -9.42174 | -60.32932 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6431af86-94bb-3fda-91e5-1abdf8f2e238 | -7.61379 | -60.93443 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c244f243-0309-3f11-a83c-c3bdd6842ef6 | -8.94813 | -60.56564 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 264fe7ff-cf5e-31dd-8a79-5fada7683541 | -6.83432 | -58.98085 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 108d84d0-e380-3a88-a77e-03b6231ba60d | -6.62197 | -59.05215 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2d94bba8-ff30-3c20-ba45-5fb9d161e9c4 | -6.62561 | -59.0527 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 99d7da21-2aa8-37c7-a05f-f98a15623226 | -10.07979 | -60.49655 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88bebde4-a8ac-3d11-a8f0-5970da923367 | -6.69951 | -58.95929 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4dfe802b-bb53-3579-ae72-aa72e8c824e4 | -6.71853 | -58.92953 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b84dcf15-94d6-383e-905b-b46b820d3241 | -8.61163 | -54.70544 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aea47ff6-391a-36a7-b8e6-aba2c0b72c1e | -8.95737 | -60.57491 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 840d6292-7b35-3a3c-8bd2-77587b73388e | -8.95753 | -60.5275 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 7c8c1d2f-150c-30c1-b9a6-671b45f4b3e5 | -9.71315 | -69.06987 | 2026-08-16 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9665de2-3b30-3f93-bbfe-2a382784970a | -8.97553 | -60.5263 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0a90a289-480d-32ed-b679-ee871139d544 | -7.59968 | -70.36107 | 2026-08-16 05:36:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6748e23-4de5-3ea4-9250-6341fdb746bc | -6.62624 | -59.04847 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a12e574b-46c1-3454-8ef4-ffb1cb67bd92 | -6.62607 | -59.07438 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 20b80050-9feb-3786-940d-6d5875385912 | -6.97575 | -59.00925 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 797cacfc-a37d-38ae-bdbc-a84e8cdb6c74 | -6.61896 | -59.04739 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c38aa4de-504d-3a73-b89b-364467d32b9b | -9.29773 | -56.81638 | 2026-08-16 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f80cf97b-3075-3c05-822b-32112f93b8b1 | -8.65402 | -54.72915 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2df31e96-042b-3da6-8046-1ac662ee3dac | -6.59977 | -59.00099 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c9ea38b-536f-3d35-a385-ce4147bb282f | -8.95983 | -60.53577 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 13bd85fc-de9c-343e-bcb4-86f937343975 | -8.6012 | -54.70282 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a54398f2-9851-39cc-90bf-23e8619d7212 | -8.95449 | -60.57053 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d7805170-89fa-3680-9cc4-3a9e6e7f7dee | -7.53195 | -55.58873 | 2026-08-16 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0ac710d-2e34-3875-961d-1c0a21a701c7 | -8.42661 | -62.67344 | 2026-08-16 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3f2e9a68-b735-3330-b4a4-776c05cff55e | -6.69714 | -58.95025 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 965a28b2-9de4-3fa4-9fad-7014f33bb106 | -8.61538 | -54.67705 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8528985-79c2-3568-8e66-9d3056bb8285 | -6.59432 | -59.11279 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f2331aad-a9ed-3cb2-bf3c-fb4b44000a17 | -8.98477 | -60.59455 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e188e247-bdf3-33e0-b73e-c3e5ddc14cb0 | -6.61405 | -59.05529 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fda01ed-a52c-39a7-876e-796e909533bb | -6.59324 | -58.99321 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e23b30f-19ab-3372-aa72-1672555d046b | -6.6023 | -58.98392 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6913f00d-3a34-3649-b7e1-2d8aed1069bb | -8.90176 | -60.59002 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 47e5955f-2d60-36d5-aa6c-e8d976b26ea2 | -7.83873 | -61.35453 | 2026-08-16 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48b8ec69-e680-3ca0-95b0-4980b53f5ad2 | -8.64906 | -54.72843 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d11cbc6-29ec-3ae2-a6d9-be7874aae9d4 | -6.9637 | -59.28509 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b0ef325-711a-3d21-b0fc-f95f9cd02f2a | -9.48693 | -60.4725 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec0167b5-1eb9-308a-9c23-3754e73fcc9e | -7.4132 | -60.00924 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 030267e4-f77f-3e5e-a415-b1bb703930b7 | -6.60054 | -58.99434 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5163ab0-d47c-36e7-a648-85bd19be5250 | -9.40256 | -65.95829 | 2026-08-16 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 454a0bab-8828-39d0-bbe9-4457a33b2abe | -8.43377 | -62.67102 | 2026-08-16 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 832b7b48-39de-309e-b15a-b3784404df3c | -7.34587 | -59.59895 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 03d45a22-fcbd-3536-aed4-dc57ba4aba25 | -9.24942 | -56.90697 | 2026-08-16 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ac2d6fa-6754-3d35-a83c-f928cea75294 | -7.419 | -60.01816 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b31b1c56-1397-3d22-b414-6e3c3df3cca1 | -7.0642 | -56.65265 | 2026-08-16 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0b6d158-1716-32aa-bf57-aa1aecf68251 | -9.29339 | -56.8157 | 2026-08-16 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e3722f5-e8bc-3077-8474-f214dd3e5f4b | -11.511 | -54.63902 | 2026-08-16 05:36:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68ff515b-2cc2-3bb7-ae63-212da0a1c4a6 | -6.85694 | -58.9799 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cbcbb042-7415-39bd-96af-6c56f34d918a | -6.85456 | -58.97075 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b6af2719-140b-3f55-aebf-2fecc2a08999 | -7.55463 | -61.17423 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aeab0df2-06dd-3b16-9357-f3dcd46f4bcc | -6.62688 | -59.04425 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c76e817e-062d-3c40-b00b-c19e34f13497 | -7.4091 | -60.0126 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11feb05d-3386-3491-b0a9-5c3129cc904e | -9.21069 | -60.86202 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c450fe18-ddce-38ea-af48-333916784edc | -9.20721 | -59.67701 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbf323d0-9786-37ab-ae5d-09b28edffffd | -6.60041 | -58.99672 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2814410b-cc97-37f2-b87a-48c49a9eb8d8 | -9.1409 | -68.20351 | 2026-08-16 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d50c9faa-13e3-3461-b0bd-fb2f16fb2503 | -8.26923 | -57.34133 | 2026-08-16 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 867c5ffd-fa84-3d8c-b439-50f69a577176 | -8.65056 | -54.71729 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb0cdac1-5cff-34c6-bcde-f1486251a62d | -8.97324 | -60.51803 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3f4ca8f4-eae0-31d7-bafe-7c49b16188d1 | -7.06476 | -56.64872 | 2026-08-16 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75d1e086-51bb-3d32-8989-a2c427d8b9e6 | -11.57974 | -54.68958 | 2026-08-16 05:36:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 72b897c3-73a7-3129-87f6-772ed0b786a1 | -8.89312 | -60.55315 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20f52dd7-ac33-3e3f-bc6d-1743e8637726 | -8.26045 | -57.34379 | 2026-08-16 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04e58831-dd73-35d3-8d77-6a1675491eab | -8.89424 | -60.59281 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e321983c-ea05-3551-8cbc-ed739e074ba8 | -8.95101 | -60.57 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2abd569b-bc15-319d-a017-32eb67799a9f | -8.96101 | -60.52804 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 6aabc99f-205d-39eb-81cc-2995a1c863c9 | -6.85025 | -58.97449 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 08249011-71ad-38ad-b8d5-71014aa70917 | -6.60353 | -58.99916 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f4974fd-7215-3744-b199-3b1fea9a2eff | -9.08909 | -61.40551 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83493467-6f12-3ad0-82db-a0f0ceb87464 | -6.59623 | -58.99803 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca1075a6-a08c-3f5e-a8c3-c7056f8e1731 | -8.8966 | -60.55369 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| cc308e7b-1f6e-35f0-b26a-d3f8a70216c3 | -8.61462 | -54.68277 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37ec43d1-f3af-328d-88a1-fe45063f18db | -6.97209 | -59.0087 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 801799de-43be-3b3c-8a37-aeadbc7e0c2d | -9.3738 | -57.36728 | 2026-08-16 05:36:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3029b526-dfbb-320c-a88e-6502839719ce | -9.13066 | -66.96886 | 2026-08-16 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3da1555b-a8df-3b18-b263-dea37941b26a | -8.95057 | -60.52642 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 96d87450-6dc2-3f3d-bd78-8a53ba04e45b | -7.35363 | -59.59595 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f062297-fddd-37e3-b73d-0396c71ca135 | -6.97144 | -59.01301 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc5e1304-549f-3c38-92ab-88c628df3520 | -8.97443 | -60.51027 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a95a75d7-b431-31da-80a2-f6e8cb1030a8 | -8.95635 | -60.53523 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2cef9217-38e5-3fb9-ba7f-383c39c466b2 | -7.55126 | -61.17371 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 248ec3bc-143b-3189-9ba7-e7acabad442d | -6.85758 | -58.9756 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 75e8d35d-ed70-312b-b27c-6062307b82be | -7.83928 | -61.35095 | 2026-08-16 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9850d6cd-f80e-3246-ae90-3e84a8e45cb3 | -8.97203 | -60.53719 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2cd3301-47c1-398e-862d-2f8dc8ded737 | -8.94998 | -60.53029 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README53.md)
