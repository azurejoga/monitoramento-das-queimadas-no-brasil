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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 109991d3-3d40-3fa4-84ae-0b24e9f3a570 | -7.03384 | -59.41639 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7618cb0-5102-3f11-87a7-03f38888b88d | -7.03333 | -59.41928 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96e8b555-b366-3dec-86d5-03053fc584b9 | -7.03282 | -59.4222 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| acb264cc-7e60-3fd6-90ad-593e8b52cb76 | -7.03248 | -59.36537 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aaafa5d9-3a76-3ece-a68b-fea28b4b5723 | -7.03238 | -59.39525 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47cbf9e5-c838-386c-8435-bddf8ef752e5 | -7.03231 | -59.42511 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c2f1bcb-269f-3cd5-8d24-606d3751b2a5 | -7.03197 | -59.36829 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cfc25462-5970-3af2-9cdf-a74d1dd7c3af | -7.03146 | -59.37119 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e5632662-4b07-3b92-965e-ac60f04f1b0a | -7.02832 | -59.41842 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5de8ef6-5c15-3dfe-b1f6-8fbbadd5a0e7 | -7.02781 | -59.42133 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 698fefb6-e257-3a25-8cf9-3becee122fc0 | -7.0273 | -59.42424 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a484ff92-c75b-3e66-8317-4e1b71a759a4 | -7.02698 | -59.36737 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62e4757f-591e-3ecd-a71b-b29091528920 | -7.02688 | -59.39723 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 07fac3cc-e0ec-3c21-8125-22c87f136468 | -7.02281 | -59.42043 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c83bc5ae-f0c5-334e-a93c-1a21dd22b622 | -7.0223 | -59.42331 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccd8d185-7dcc-3fae-8ad2-a8f27817e594 | -7.01483 | -59.40709 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fc15a9d-fa05-36b1-ad21-2675878093af | -7.01432 | -59.40999 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60b457fb-6774-356f-b158-08f0927fa067 | -7.01381 | -59.41288 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 717ffb23-f5aa-3029-b2c1-93cae787b108 | -7.14642 | -59.30379 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6bb0af97-449e-33f5-a7de-374d60875588 | -7.14543 | -59.3094 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 514f2314-0ffa-35eb-9b32-22fabd2dd3f2 | -7.14047 | -59.30851 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4283666-87af-3a51-bd0a-698bcf8e00d2 | -7.13651 | -59.30201 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c986445c-b553-3f06-b6a0-083406324539 | -7.13551 | -59.30765 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 397d36d6-4e72-3fb2-910d-8be9fba01cf0 | -7.12658 | -59.3003 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a81fef2-a54e-3460-8364-19de3c920a0a | -7.12558 | -59.30595 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7476f9f-82e1-3f5c-acc9-c2a5006a2e3f | -7.08634 | -59.26201 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d076b32d-a54b-3150-92d8-ed29532d55ff | -7.08537 | -59.26765 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7cdfaeb9-189d-3ea0-8146-498dbe6144a0 | -7.08344 | -59.27881 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c126c84-6dd8-3529-a9b6-94077053208e | -7.0814 | -59.26109 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6bc39ba0-07fc-38dc-92ab-092d4be6ba15 | -7.08042 | -59.26671 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 687f4c5b-6e35-3bbf-a623-c6628efd6cbb | -7.07848 | -59.27794 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 767101e4-4886-32a3-a721-fe903b890239 | -7.07548 | -59.26578 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1bd98c7d-5330-3ef8-ab01-d156b66bbbfb | -7.07451 | -59.27141 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9d49fd9-12bd-376b-9f88-5c44a784401f | -7.07054 | -59.26484 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b0728e99-f994-3c93-b5fe-0700d5177858 | -7.06956 | -59.27049 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f1b0abf-006e-39e0-b3ca-fd8ad5f31131 | -6.80888 | -59.1461 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cfcac39d-5888-3c03-8dd7-d1ed26d63b05 | -6.80789 | -59.14481 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2dffbe87-7b82-3ce8-8453-0bb955d53c16 | -6.80395 | -59.1452 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 152a5282-e6a9-3cba-aa5a-0d2bb99ed5a4 | -6.80296 | -59.14392 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f8f266d-23e2-34d4-8e09-12bbaa57efe4 | -6.80201 | -59.14951 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25720f59-aac8-3ab4-a247-0dbf5afa42b0 | -6.7889 | -59.31601 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7707b6e0-17e8-3abe-8a44-a977f4752169 | -6.78839 | -59.31886 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 384a3c40-a8d1-3cf0-991f-4c1feac1b33e | -6.78789 | -59.32172 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec6ab52d-1005-3ba8-9482-0401bc72539c | -7.4707 | -60.60936 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21d34435-e25b-3a72-b359-b75ec6c2684b | -7.47008 | -60.61284 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd5de8d9-6090-3425-bc64-e2c43ad70c49 | -7.29633 | -59.73859 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f6fb0dd-1fd0-390e-a907-fa1bba6ab54a | -7.29579 | -59.74166 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 00998b66-3979-33bc-ac99-70e3a5d0f376 | -7.18679 | -59.77631 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91c6898d-c7c5-350e-8df0-1379a32e9082 | -7.18625 | -59.77937 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c8710c0-6d32-3292-894a-a6023192fba1 | -7.04233 | -59.42688 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e3cf212-8786-33b8-badd-fb6b63b68517 | -7.04131 | -59.43273 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93b2d7aa-5086-3f14-afd3-d3e78edfb6cb | -7.0408 | -59.43566 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c1c6164-8c3b-3651-8597-fc535df4590c | -7.03682 | -59.42887 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfaf26cf-f65a-3a2a-8e44-08bf0adee487 | -7.03631 | -59.43182 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa3d8591-139d-39f8-8de9-c90df7f78443 | -7.03579 | -59.43476 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9361b9e9-299d-3546-8aa2-54b7867abb3d | -7.0318 | -59.42804 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bda8e94b-ef77-3bee-90d4-a980be215095 | -7.03129 | -59.43095 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d18a2565-000a-36b5-ad6d-22418c3ee20b | -7.03078 | -59.43385 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9b2ca62-4f0e-329f-bff7-e01dd123acd8 | -7.02679 | -59.42714 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1b873d1-93ef-38f7-a634-538a38587792 | -7.02629 | -59.43003 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72e628d6-3432-3a7e-be38-7d78c65ca49a | -7.02179 | -59.42619 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c2007e0-b32f-3eaf-a664-a2c10394f098 | -7.02129 | -59.42907 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36f8f64d-868f-3501-9295-b3497e1bc668 | -6.96789 | -59.47269 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58a4feec-4916-3103-bd28-14d3171f72ae | -6.96738 | -59.47567 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a044b8cb-9dec-39e3-8f8b-d5db5963e8dc | -6.96687 | -59.47866 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a05dff04-45b4-32cf-963f-3e4d1a106527 | -6.96682 | -59.47341 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4370d21a-a45c-3e38-9044-36c587f1a841 | -6.96628 | -59.47639 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e51e148-22f2-3723-86f2-1dba7eb0c207 | -6.96575 | -59.47936 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 816cccdb-2cc0-351b-a983-a0b57b469f88 | -6.96184 | -59.47779 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bcb329d-108b-36bd-934c-a6acf6ba7f04 | -6.96072 | -59.47848 | 2024-10-10 04:44:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6de3fc03-f48b-31e7-b032-d3d506725446 | -9.24345 | -60.48116 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b9e74f2-b14e-37db-a24c-3b7047d85494 | -9.24288 | -60.48428 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ecfcaf7f-72d8-3ddb-9f32-9f58874fe073 | -9.20951 | -59.78454 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 64cd1cd3-ad2b-3d9e-ab1a-96bba8247ee1 | -9.18482 | -60.35472 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05556673-bcf5-3459-876b-2c6c52bac5ae | -9.17968 | -60.35376 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf5103a7-ab5b-3efe-8042-131bb5de7ce1 | -9.17913 | -60.35686 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e68a492-d34f-3066-bfb9-73daa4cc03ac | -9.1726 | -60.30452 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72053ee9-6d4f-3a78-81db-92df8e2c5aa1 | -9.07002 | -60.57457 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a72fda8-2a81-31f9-a2b9-a572ae2e4b7e | -9.02997 | -60.58646 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca565fd2-82a1-3076-a3e4-8f1568a36dad | -9.02661 | -60.54473 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22d3110d-6d35-3558-a132-5c646694ca48 | -9.18167 | -60.35301 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e88f08ef-8494-33b1-9b31-c3c9e1d48a54 | -9.18109 | -60.35612 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98148081-751b-3193-8fa3-127c4379bb86 | -9.17771 | -60.30553 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b79a210-df45-379f-8d34-285b8d4cbb67 | -9.07523 | -60.57557 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6665667a-28c7-3157-ac44-607177c9594b | -9.0606 | -60.59633 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44c2c21e-7b4c-32a6-b6e5-4d3fdacb21b8 | -9.05539 | -60.59527 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07f3999a-9de5-38ce-8b7b-a6c459aa3c96 | -9.04837 | -60.4534 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e58bf29-91f2-38a3-b1e8-88b85ec58dc9 | -9.04781 | -60.45652 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 980ddb98-17b9-34c2-8e4d-65e988ce289c | -9.03055 | -60.58334 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd0c95e6-c71e-3d10-9775-4e4ab9351abb | -9.38692 | -61.04869 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39c2e4fd-0747-3050-ba34-0d16f682a19f | -9.38628 | -61.05208 | 2024-10-10 04:44:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6214ecf-7d7a-3308-a35c-7365a5800bc0 | -9.94959 | -60.10799 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c7929561-d42d-3051-a420-1c8ab6afd559 | -9.94667 | -60.15253 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85343fed-31b5-3661-bc6f-ff6da8df7863 | -9.9446 | -60.10704 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5fa3fe07-82e3-30ef-aaec-1321ead413ab | -9.92572 | -59.83811 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f45d4f9c-60b9-30df-98b4-c255de985002 | -9.92425 | -59.93849 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5771d56-19c9-352f-b867-687ffc75e26d | -9.90154 | -60.31458 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7e2274f-a4bb-362e-8ac2-07c73caae3f9 | -9.89987 | -60.21004 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2c1d7fa-0181-3445-aeca-bed4416e6f3f | -9.89933 | -60.213 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f899146-e064-371d-a938-dd52d4951a2f | -9.86331 | -60.32316 | 2024-10-10 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README118.md)
