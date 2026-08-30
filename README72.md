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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efe850df-5bc4-3009-968c-0a0d5a8db833 | -10.50387 | -64.52415 | 2026-08-30 06:14:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de10e2a1-3a27-3a08-90e8-ee57db6d5f65 | -9.70846 | -60.73109 | 2026-08-30 06:14:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 705fc7db-f108-3faf-8b63-e6b1daa25d39 | -9.74952 | -66.75886 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04afd6f3-db14-3ee8-a989-e0125d5f0224 | -9.88861 | -60.27774 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 8c443eb8-6b4a-3ebd-9076-1e47e40c4c4a | -10.50351 | -64.52699 | 2026-08-30 06:14:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc3ceedf-8b7b-312c-b941-5e19f606a575 | -8.65814 | -62.84137 | 2026-08-30 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24618a6e-c789-33ad-ab53-d1045c1c38df | -9.00231 | -65.43772 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3460843d-103c-33bd-9f54-0bfa2d0dc234 | -8.95683 | -62.40065 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70e4afaf-0196-36d9-a9ca-060fdc67b9c2 | -7.55507 | -61.32493 | 2026-08-30 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 678d4a1e-7c99-3e49-a50a-6a75a3b8a90f | -7.96816 | -70.02705 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0cf822de-6b7e-3116-90ba-f3d9c2f4b7bb | -8.96198 | -62.40533 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61baba22-9200-3170-af84-9d3f7acb6373 | -8.59969 | -70.21759 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2644f466-a977-3850-9473-86d3b38e9571 | -7.30285 | -60.59267 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45ced049-3c0c-3135-81be-828a2a2b4e69 | -9.23838 | -60.41248 | 2026-08-30 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c72ab12-3ada-3ee2-b906-e4a9b838a679 | -8.77802 | -70.81536 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93c6b8ec-672a-32f7-a31b-552c9434cd97 | -6.91243 | -59.48738 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2da9e61-42f0-3062-895f-98f74ac5113b | -8.91109 | -66.95264 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebfe1720-793e-3baa-af19-d88f0a59ae69 | -8.95166 | -62.37547 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12c0f784-d9dd-3491-961b-4d567730680a | -8.85397 | -70.61645 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d78ec68a-a2eb-3b76-8967-62856d43988d | -10.48698 | -59.60938 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 609286f3-1f9b-3864-bed1-27dfee532e5d | -8.59026 | -66.96133 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0710b711-bdbd-3c54-aab1-e30687ee4a16 | -8.94548 | -62.37857 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e295f16-113a-3acf-a700-5922dddb808e | -9.03938 | -67.61903 | 2026-08-30 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44df6992-73d9-3a3f-a331-c23d3fad666c | -8.96248 | -62.40146 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e7e35fe-0d63-32a9-8666-58271107ed9f | -9.9375 | -60.52214 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fe3726fa-291a-3a3c-9f79-5d2dee2c1e14 | -9.93172 | -60.51604 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1372d969-9f09-3e6c-9cae-f3d7180ba93d | -8.95413 | -62.37676 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 670000ab-1c36-3a7b-9282-442d63492358 | -8.95782 | -62.39293 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23449341-93a3-3eba-9916-3f9b92551e2a | -9.93683 | -60.52743 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4dbc603f-fc14-34ce-8175-de5d529ca162 | -7.56162 | -61.32132 | 2026-08-30 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f76a3199-7612-3b8b-be4d-c05689edf59f | -7.314 | -60.60391 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9fbba40d-980c-3da2-aa79-1520c6f89dee | -8.10708 | -70.21388 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97c54b17-50b4-3af9-a61a-78c7742c2944 | -10.48026 | -59.61648 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 07dcc0d8-0e04-3e4d-90e6-f04097e111fa | -9.88792 | -60.28345 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 929095a1-3220-3675-b45a-9e2ed87c0d2d | -9.07063 | -60.49463 | 2026-08-30 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0031fcbc-a6ee-31af-aa38-c54f7f4d0f62 | -8.90165 | -71.39748 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b333f859-1364-33e9-a4e1-86ff0e67b5c9 | -10.48514 | -64.51089 | 2026-08-30 06:14:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d01fb6b-6ba0-392a-9c00-73ad6da77641 | -8.95933 | -62.40393 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c11dd0e3-3030-3bb3-a00b-dc496a22a042 | -10.48013 | -64.51025 | 2026-08-30 06:14:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b40f3fe-70a4-3050-ad49-959593f4ee33 | -10.48571 | -64.50674 | 2026-08-30 06:14:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04eb0c54-7471-3cc9-9ffb-e2cd7cb69a00 | -8.95534 | -62.41226 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09753b27-d008-3177-9c38-960e045ceba0 | -8.72774 | -70.78137 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a51412d1-bbfa-3621-9709-672a0e1e1ed7 | -10.48052 | -64.50735 | 2026-08-30 06:14:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cbf1966d-4668-383a-970f-acb1592a949d | -7.30222 | -60.59744 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cdf5297b-0467-373c-9548-8e9d59dc6364 | -8.25468 | -62.75464 | 2026-08-30 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1a7b17f-f569-37c2-bbcd-cf715df181d3 | -9.06092 | -65.42163 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b745b5fb-9fb9-32b1-bf03-006b836512f8 | -9.15285 | -59.50655 | 2026-08-30 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dfe2797b-f3f9-309d-af30-743066899f85 | -9.01612 | -65.40562 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ead74e29-1a4a-3d7c-aa40-9f27b73c3473 | -8.59181 | -70.2283 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c658fd3-e701-3e16-b403-1b3ba6e04a43 | -7.56102 | -61.32572 | 2026-08-30 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b2a87929-77c9-3bf7-bb82-4a8cee972761 | -10.48851 | -59.60525 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 508d600a-58fb-31e0-9161-197d1403a368 | -9.85043 | -60.27157 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a2f8687-a1f1-3060-9801-99063375add1 | -8.59681 | -70.21326 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51e9ab5d-33a0-3a3e-9bb3-e6b7ad2d85cd | -7.24284 | -60.62676 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3b97e010-18a3-3e8a-b458-ac938add4a8d | -10.4794 | -59.6145 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 22a50803-233f-3006-af33-bc9b2edcc0e0 | -8.25341 | -62.75834 | 2026-08-30 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55e939c3-8160-3a53-aec7-eafb09dbdf50 | -9.74908 | -66.75814 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 28feb61e-c89d-3225-96e3-f0c4b2c243d3 | -9.92267 | -67.87838 | 2026-08-30 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b3128a7-4dda-3699-8140-0b79b70a7e81 | -8.88135 | -71.263 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 435c9fad-cc74-39c3-933a-ed35aae7386c | -9.07126 | -60.48947 | 2026-08-30 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd75b236-4924-3ee6-bee5-2b460cca4f03 | -7.2422 | -60.63149 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 76ee5261-8d55-3072-a867-e160ec9af4d2 | -8.86448 | -71.46063 | 2026-08-30 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8369e505-33ea-3331-8dcb-fe1eaa680805 | -9.06024 | -65.42641 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ac2d14db-4cc9-3ade-a053-066b6064c705 | -8.58613 | -66.96078 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3559fa1-6655-3306-bf95-c38c58b82aff | -8.94797 | -62.37986 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c62fa48e-add3-3695-9323-ceffb4230e61 | -9.23772 | -60.41775 | 2026-08-30 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07c1b379-abf2-3d46-8807-8bcc6d1e8a3a | -8.93533 | -67.36304 | 2026-08-30 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60be7cdb-80fd-310b-b43f-6881a2c0f96c | -8.9147 | -66.95696 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd3b2bd8-d051-383b-82c9-47c18c8463e9 | -8.92978 | -67.37313 | 2026-08-30 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31bf6397-c811-3bc1-ac59-64965b3b7878 | -8.95115 | -62.37931 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2769752f-ca01-3af0-b48a-5eef28bfb80c | -10.48014 | -59.60843 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e203a5a-9278-3e20-82f4-a3d4c8499e10 | -8.21638 | -70.48225 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3eb8bfaa-6029-372d-a505-b990b213750a | -8.58253 | -66.95648 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d20cfd12-6b74-323f-a0d9-8de41ff92a1b | -8.74039 | -69.5673 | 2026-08-30 06:14:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c62869f-9271-3fb6-a710-65ea2a8ae953 | -8.946 | -62.37472 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62c9145d-60ae-3595-89d3-f25e5af970ec | -8.34881 | -70.84976 | 2026-08-30 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e5442f2-a51a-3d93-aa27-fb3c2d0c80af | -7.39862 | -60.58632 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ed9c68e8-4b83-39f3-bc6a-f84025a3bf6e | -6.07987 | -57.89294 | 2026-08-30 06:14:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3eb1294-7df2-31c0-b24f-28bd2e9b6400 | -9.18043 | -71.63352 | 2026-08-30 06:14:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a073ed14-c664-3484-9669-3ff49f8eef13 | -8.60831 | -70.20724 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6f7f1a9-dd53-3d64-b260-183fad52be68 | -7.29601 | -60.59659 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 906d08cb-9344-377c-82c6-8ca85d5a9334 | -9.93239 | -60.51871 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 516bd9f3-a4ba-399a-a273-173f26c89849 | -9.2311 | -65.88695 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a4a6bfb-9581-3979-af6e-ce71c0a5d4b4 | -8.94748 | -62.38371 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91e2b41b-8222-31d1-bb9d-f3a5cb2dcfe1 | -8.9318 | -67.35887 | 2026-08-30 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| f6233e42-6e53-398c-bcab-7a1705136bd0 | -6.07887 | -57.90014 | 2026-08-30 06:14:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91279c7d-9661-31df-8322-6e5a9d7269c2 | -10.48622 | -59.6156 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fa2d454a-52e4-30c3-b821-8385f1bcf0fc | -7.62384 | -61.33278 | 2026-08-30 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2713c3b5-8c4c-3f79-a115-63bb39a84d47 | -9.51097 | -65.57924 | 2026-08-30 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a60f5f11-e09f-3186-83d5-9f46e74b1372 | -9.05698 | -65.41619 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e9c422a7-42a7-356c-b42c-f217fc320b8e | -7.39926 | -60.58165 | 2026-08-30 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ffe83de-18ad-3bff-bee9-475313c1e104 | -7.55744 | -61.30731 | 2026-08-30 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b890e787-d81d-3f65-b4d8-d90ea88ba8cc | -8.25377 | -62.76163 | 2026-08-30 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a127ba6d-98fd-3a72-a417-543468718952 | -9.93175 | -60.52402 | 2026-08-30 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8e32554-35fc-36b9-9f61-d34fb57ef64d | -7.69593 | -61.1576 | 2026-08-30 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8b9b1b6-add0-385f-a982-f8869f300123 | -8.95985 | -62.40005 | 2026-08-30 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9134e0c1-432a-35bc-82ef-e86a9de97ee0 | -7.55685 | -61.3117 | 2026-08-30 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 89d95eb1-a6f5-307c-b922-ca5b1eb6ed0a | -8.58307 | -66.95275 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3ab5156-1d2e-3bb3-98b1-211ca957b93d | -9.09323 | -65.49096 | 2026-08-30 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1dc6d3e1-3b75-362c-82d8-742cda5bcd57 | -7.96791 | -70.34591 | 2026-08-30 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README73.md)
