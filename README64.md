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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4bddbe31-511c-3190-846d-22d586a7f5ad | -9.04788 | -65.43509 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18a20d3f-990a-31df-8632-86277b56fa37 | -7.50286 | -70.05165 | 2026-09-02 06:01:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 407d563f-06db-351e-947b-d834ba4255af | -8.56354 | -63.18763 | 2026-09-02 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 683e970b-0c71-3120-8259-c41a2d0b2768 | -8.74553 | -62.56943 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 16f9b56e-c2e1-32d3-bcbe-a37e09687503 | -10.49469 | -64.32751 | 2026-09-02 06:01:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 26b65335-20f7-3496-8933-b41cee5ebafe | -9.03061 | -65.44501 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07a3e43f-87be-34be-9eb6-16ebe7397508 | -8.89027 | -70.55234 | 2026-09-02 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cec5aafd-89b8-32b6-ae5c-bcdd28234975 | -9.03275 | -65.4302 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2556b652-59f8-34a5-916e-4854bd694b9b | -10.48484 | -64.32045 | 2026-09-02 06:01:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 15.5 |
| f3847ed5-b440-36ce-a16a-2273ea042787 | -9.84168 | -64.99074 | 2026-09-02 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8acc19b-f2ff-36db-8fbd-a7f10e27ad95 | -7.68851 | -67.12174 | 2026-09-02 06:01:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e1107b88-a5ae-3af7-813e-4d4a38fd2cad | -5.57643 | -60.19851 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 692d2922-815f-3ddb-8524-e007bd90e6b8 | -7.20912 | -60.68081 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 24b32449-fa9f-3018-b3ae-fbd22795c79b | -7.77126 | -61.19895 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c9472c5-5613-3bfc-ad6d-a9dacd6f2e57 | -8.86068 | -69.15089 | 2026-09-02 06:01:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30e3a32a-ac51-3525-ae66-2ae95c583e9b | -7.35886 | -60.60992 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6f2b2051-640f-3eea-a057-2c95c847c42b | -9.45069 | -67.47132 | 2026-09-02 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc04eb43-a9b9-32ab-9716-46d720f20f6b | -8.75828 | -62.59489 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34902d84-9281-3315-bfe4-c177ce40d0b8 | -8.06574 | -72.37452 | 2026-09-02 06:01:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6d75e2a-be8a-3756-b378-08fe031427c1 | -9.00063 | -67.8053 | 2026-09-02 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 914a2a28-9ea8-32ec-9240-bb8cedda857b | -9.55633 | -67.48969 | 2026-09-02 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 987fab9a-85ab-349d-8f46-c1897e6e5b52 | -9.84113 | -64.99484 | 2026-09-02 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c1a4c7b-98d5-3ce4-ba15-51bbb1778fcc | -8.33212 | -70.73016 | 2026-09-02 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62914109-11c6-3ee1-82c7-44c39f5ab442 | -7.20513 | -60.66885 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f66ba081-42b4-3e82-8e32-f2765473f924 | -7.69945 | -67.1234 | 2026-09-02 06:01:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d084706-5f16-370c-b084-fa97bec77a70 | -9.25099 | -68.18687 | 2026-09-02 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4738c87a-fb24-335f-b585-257bbe313f0e | -6.76048 | -59.44319 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c2d837ba-ba05-3530-8c99-4ce3dfc40400 | -9.44234 | -67.42602 | 2026-09-02 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f36ec992-289c-388b-a43b-34410211f0fb | -7.20413 | -60.67607 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad8d60b3-c06b-3aef-a2f3-e494e05dee8e | -5.17992 | -60.28962 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fb3a859-e49e-3b5c-9458-53bb3cbb988c | -8.26476 | -62.76301 | 2026-09-02 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e1e5e12f-4e64-3e3a-9229-2f9c82299f45 | -6.64591 | -59.43374 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0695cdf9-30a7-3714-ad1d-108913f67f43 | -7.25962 | -61.10862 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7415fd14-1f35-36f0-877e-1d60a5d097dd | -9.01485 | -65.40864 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 65506f31-2f07-3ed1-8f2d-954bbc2f7aa4 | -8.81075 | -68.69186 | 2026-09-02 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a82a0b6-1e7d-333d-8168-46cf997d7745 | -7.54111 | -60.71902 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2436e405-41e4-3518-872d-f2de92873896 | -7.3404 | -60.57743 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5372f3f1-d181-3ea6-b0dc-621d3da466ce | -8.78789 | -62.48279 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87873ced-e3d8-3231-b46f-6e52eaef1c11 | -8.74072 | -69.42939 | 2026-09-02 06:01:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c563efd-db2e-3b84-9976-3a9477237505 | -9.0697 | -71.96278 | 2026-09-02 06:01:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a73ca52-681e-3a40-a1a7-2e9c1f6bea33 | -6.91803 | -59.64888 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fa1f4ec2-6823-311a-9361-1edb41b2ea0c | -9.61993 | -68.59995 | 2026-09-02 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d060604-ad16-3f86-a588-d67a18f4e04e | -10.48621 | -64.32191 | 2026-09-02 06:01:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 9e5d141e-8663-348f-a31f-3cdb2f6c3320 | -7.346 | -60.57814 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa061b6d-5ecd-3d0a-8e15-6e76fc963c8d | -8.76302 | -62.58995 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a75e7d15-89ef-325a-bd28-0ec5d6610a54 | -9.88536 | -68.86182 | 2026-09-02 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e281794c-dc45-3cf5-bc55-e789d4bff392 | -9.03603 | -65.39909 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d59b7144-9bbf-374f-a8a1-af0b02c4b330 | -8.78248 | -62.485 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f8195942-68f5-36f1-b8c1-3e4034e38f60 | -6.85577 | -59.48262 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9c7d7c74-1806-3b3a-8b06-63f9d3712bad | -9.03551 | -65.40285 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 32e58dcc-cf37-39b5-874a-abdbde33d01f | -8.26549 | -62.75762 | 2026-09-02 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dfc0e07a-8f65-33b4-a67f-4bea4cc9e44f | -9.44601 | -67.42655 | 2026-09-02 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87d3361a-87b6-3262-8dc2-e7ad4b06c6aa | -9.87389 | -64.97878 | 2026-09-02 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9536b16c-76de-3b27-9383-f26e292e3714 | -9.02133 | -65.45121 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b167db5-c018-3d9c-83c8-c182af9f75dd | -7.60009 | -67.41722 | 2026-09-02 06:01:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9722f860-fe4e-38f8-bb0f-faac7694d100 | -6.69419 | -59.94406 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8b3331b3-018f-375c-85b1-027172f0c954 | -7.53556 | -60.71823 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f77b0a4-a9b7-36ea-b759-7d2b8eeb4d08 | -7.53617 | -60.71674 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81b08409-3d8a-39ea-bdd7-01e1c1df267f | -9.92723 | -60.48397 | 2026-09-02 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 835a552a-aff7-34fd-af71-e68b8416f650 | -9.03706 | -65.40044 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 386c65bd-3ca9-353d-8265-86b09c39d774 | -6.6874 | -58.76643 | 2026-09-02 06:01:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e50e5f15-098d-3605-9683-dc0baa76c7cb | -9.02186 | -65.44753 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ca4a28f-98df-3635-bc9d-cb43a3833cc4 | -7.76912 | -61.1964 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1218c8f4-30a2-3dd5-9155-d081bf95a01c | -7.36492 | -60.60702 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3396af2-2c51-374a-8797-c9cf17e1fdf8 | -9.83076 | -59.47543 | 2026-09-02 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c53c4b41-8d2d-3014-90af-9d8a5a5d8338 | -7.89261 | -71.74798 | 2026-09-02 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6dedebb9-c6cb-30d4-9050-dd45cc3e6e3a | -14.49914 | -59.84406 | 2026-09-02 06:03:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7d2d6398-165e-35a0-987b-2283fc82dfc9 | -14.50725 | -59.84304 | 2026-09-02 06:03:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d9424340-c7a4-3276-96ce-71af2648646c | -10.89972 | -68.55882 | 2026-09-02 06:03:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b1c7c0a3-41e5-3331-8f21-3f363e9676e8 | -10.16423 | -69.31373 | 2026-09-02 06:03:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca5f628a-131c-32a1-bcd5-f99ab94ab87d | -14.51235 | -59.84184 | 2026-09-02 06:03:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9dfb4e0b-4429-3780-b27f-8547273a2486 | -10.16762 | -69.31425 | 2026-09-02 06:03:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0960d8f-d36b-337c-aad1-9fd800d45a4d | -10.16975 | -68.99687 | 2026-09-02 06:03:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eda9452d-733f-3533-966c-08662aef5368 | -10.43602 | -67.84271 | 2026-09-02 06:03:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3d4342a0-6f6a-36f4-9d17-afdbac02019b | -10.16478 | -69.31004 | 2026-09-02 06:03:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b5b2cf47-226e-3c93-92ba-32f8dd895e27 | -14.50553 | -59.84499 | 2026-09-02 06:03:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d2107b66-0bb1-3daf-9322-ba14696b3f49 | -8.4669 | -54.7237 | 2026-09-02 06:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 1c091d10-7d73-3b2d-bbdc-52a5be832748 | -10.9009 | -45.3509 | 2026-09-02 06:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 41b973ff-f5f0-3d62-b4d1-d194af4ebb01 | -10.9204 | -45.3253 | 2026-09-02 06:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 0b148f1e-8c7a-3b12-bcc8-cf6ada1d8b43 | -10.92 | -45.3483 | 2026-09-02 06:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| b63ace4f-69c7-370a-9826-401b30a8782f | -10.9013 | -45.3279 | 2026-09-02 06:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| f8514d56-b811-3e68-a038-140aed25efc7 | -6.6948 | -58.7678 | 2026-09-02 06:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| db2fbf56-40dc-368e-a83b-4820e0e6cddb | -10.9 | -45.35 | 2026-09-02 06:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 45dfa02d-6250-31d9-839a-8f4b4a440eff | -10.9013 | -45.3279 | 2026-09-02 06:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 1e70f658-7e04-3a3b-bfad-42ff20f59a5a | -11.3524 | -50.6159 | 2026-09-02 06:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 74af0102-303c-3ebd-ad6a-95d43bfd957a | -11.334 | -50.5752 | 2026-09-02 06:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 49d346b9-04b6-3684-a32a-05138bb5e69f | -10.92 | -45.3483 | 2026-09-02 06:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 058a112d-9241-3fbf-93af-bb876bc9b09f | -10.9204 | -45.3253 | 2026-09-02 06:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 185.9 |
| c7077203-c8bd-3080-bcc4-c7cc2221ae96 | -11.3337 | -50.5966 | 2026-09-02 06:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 7aef4983-4d1b-3f7e-807a-24bc486b4008 | -10.7774 | -44.7463 | 2026-09-02 06:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 42.2 |
| d05783fd-6557-3664-9485-bc3fbf11d41d | -6.6948 | -58.7678 | 2026-09-02 06:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 5976a24e-20ec-3498-a8a5-9a599fca4aa1 | -6.67721 | -43.41191 | 2026-09-02 06:27:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 32799ec0-187f-36bb-9229-89fcba8c0d73 | -3.23539 | -47.23288 | 2026-09-02 06:27:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| c1233552-2f2f-3870-ace1-6b7d4b3c3a25 | -4.36016 | -47.77605 | 2026-09-02 06:27:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 768d6805-84c2-3c35-881c-923e3bbfe580 | -6.67853 | -43.40316 | 2026-09-02 06:27:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ce0c1cd0-9405-39bc-9a57-6631e9a5a3b2 | -3.24421 | -47.24897 | 2026-09-02 06:27:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 23bfb57f-4380-37a0-847b-12e9e80cdc67 | -3.85 | -44.0499 | 2026-09-02 06:27:00 | AQUA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 48a037c7-a85e-33f7-accc-b8316fad978b | -6.91387 | -45.71318 | 2026-09-02 06:27:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8b97429d-2eee-3a6f-afbb-394f9d509b10 | -3.8486 | -44.0591 | 2026-09-02 06:27:00 | AQUA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c50cf3d6-02e8-3b21-a083-d08d6d49e6a3 | -3.23311 | -47.24735 | 2026-09-02 06:27:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |


[Clique aqui para ver as próximas entradas](README65.md)
