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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c722fba1-546c-3027-83a9-324a292dec22 | -6.14227 | -44.63514 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa6a64d4-5afd-35f0-9888-d6c3fa4b7508 | -5.50711 | -46.96128 | 2025-10-05 04:44:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8fefe6f2-7a15-3b9a-8cd6-541a8e60cb7f | -4.26774 | -46.75566 | 2025-10-05 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 04f1b504-6580-3f77-83fb-b21c085a894d | -6.42797 | -44.46667 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cb1a6990-17fc-3ea1-b233-2419a16bbcb8 | -3.1261 | -48.96548 | 2025-10-05 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dbe96be-d2fa-3650-8fa5-dc7c329251a1 | -5.91674 | -42.89701 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 589355be-8407-3f26-91ef-2578638fe2fc | -2.36218 | -45.67651 | 2025-10-05 04:44:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c054820e-2d5f-3a1f-bbbf-d7902d30e787 | -5.87663 | -42.53182 | 2025-10-05 04:44:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b89e8d32-7126-32c1-b584-840362aac625 | -6.0679 | -42.66416 | 2025-10-05 04:44:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6e389ed7-91c4-390f-9059-bc849800f01e | -6.08626 | -43.48249 | 2025-10-05 04:44:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 32fed0c5-38ba-3a1b-b7c7-2b1f36a6cc73 | -5.24238 | -42.63872 | 2025-10-05 04:44:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad6d973a-f71a-3bd5-987c-467a85843b59 | -5.64982 | -43.62268 | 2025-10-05 04:44:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7abcb680-c381-3c1a-afe6-2dc28c50cb0d | -2.60868 | -49.40337 | 2025-10-05 04:44:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4025629-47f9-3571-9532-0bb0f253a855 | -5.84023 | -44.45097 | 2025-10-05 04:44:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 8daa67b6-bdba-3e3e-a1a2-513062d70924 | -4.75472 | -46.60551 | 2025-10-05 04:44:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a399aa0-63f3-321d-ac8e-ce9be48127f8 | -2.89126 | -50.73281 | 2025-10-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 532d1a16-e499-3e2c-8c8c-2991a3a7a225 | -2.89786 | -50.73383 | 2025-10-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0972e58-8245-3a5d-acd9-8a6205427123 | -5.64992 | -43.91503 | 2025-10-05 04:44:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bcad4270-aec9-3161-945f-6e744458ce68 | -5.9469 | -42.87265 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a0aed000-15e5-3fb2-95d0-fa121432bebe | -5.89525 | -42.91718 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 26acbbe6-b531-3bc0-b035-922263480a58 | -4.2728 | -46.74731 | 2025-10-05 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b5c92e6-85e4-3852-84a4-abd5d493bd2f | -6.12604 | -42.8679 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9c687ba4-5d38-3174-a527-a11ecff9c0cd | -4.6399 | -43.187 | 2025-10-05 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 4fbe05b5-c8ef-3c38-a7aa-010681fc3a48 | -5.58611 | -48.90318 | 2025-10-05 04:44:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 064f26ba-8451-35bd-9623-920f07e0f650 | -2.6881 | -48.39323 | 2025-10-05 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50143420-4ace-376f-bcee-b66317dd0200 | -2.68753 | -48.39688 | 2025-10-05 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81a271c0-c9eb-313f-b035-bc3e8499f13b | -3.08732 | -47.78955 | 2025-10-05 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 720a5e54-84ff-3337-b64e-507426479474 | -5.22216 | -43.76003 | 2025-10-05 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5297b74-52e6-3551-8958-1ba3bc3c673b | -5.58773 | -43.40529 | 2025-10-05 04:44:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| db3cff41-bd7c-3221-9e88-5f6142abf628 | -4.80534 | -48.22171 | 2025-10-05 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 189b1996-5819-333c-8986-bf43dfd27f2a | -5.13055 | -46.23714 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 956f72bb-498c-362d-85f1-7189d0c6b892 | -5.78613 | -42.92867 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| fc198ca1-1c64-3c34-a90a-1a5a7a1979e3 | -5.83379 | -45.81538 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33c03c42-3e61-3379-a46b-dba7640b7f8d | -5.78119 | -42.92799 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 263aca3c-1381-3a86-87f5-aff87cf68508 | -5.91321 | -42.89669 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| ac847d83-cec8-3338-8d95-4de700dca328 | -5.9224 | -43.32661 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a8857c8d-6ed4-32e7-8f56-2479063b9091 | -5.97283 | -45.88803 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 942dad14-76d0-3e12-8c7a-2668548b6087 | -3.8141 | -51.29228 | 2025-10-05 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 80ba44d7-87d4-30bd-bd69-f4868f1c826a | -6.40044 | -43.06469 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8400f01c-eb7c-340e-aa40-b98e9fd933ef | -6.2911 | -43.91617 | 2025-10-05 04:44:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1f95cc35-d52a-3ed4-92cb-3e4c73925a31 | -5.80094 | -45.78187 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| beb5a5c5-d9aa-31cc-b980-d66f4fcfa65f | -6.15487 | -44.67233 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 0248eff8-5ff9-36a8-ba4a-2a2c919d3f44 | -5.85177 | -43.37402 | 2025-10-05 04:44:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96894a61-4ba6-341c-bafe-b37360dac36e | -6.34165 | -44.02711 | 2025-10-05 04:44:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 73a7ef74-15cb-3ceb-9fb0-972e57393cc1 | -2.89402 | -50.73676 | 2025-10-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d8fc500-0925-3b2a-93b5-567405ae0153 | -5.65016 | -43.9117 | 2025-10-05 04:44:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d7a6b5aa-8faf-384f-ba0f-dccb178d6467 | -6.16112 | -44.66022 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 43444528-d407-36f1-8b25-db55dee4b3e8 | -3.84061 | -44.55418 | 2025-10-05 04:44:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c57c3288-580a-30f3-9efd-1da6479a19e4 | -4.27214 | -46.75173 | 2025-10-05 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b1e9167b-3209-3f01-a20f-c2c295f3d481 | -6.70544 | -42.16127 | 2025-10-05 04:44:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3af6ee1b-bb67-31e1-8bf9-62a41a0f8f82 | -5.23139 | -49.06844 | 2025-10-05 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9952e305-5f24-30b5-8624-0ad8eac34509 | -6.70211 | -41.94718 | 2025-10-05 04:44:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cce5ec88-0a19-33bd-91db-0cafd77c59a9 | -6.36479 | -44.62058 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11524978-558b-3909-8211-5ebc7f8c975a | -4.23517 | -46.75808 | 2025-10-05 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7026fe6d-e751-3ba6-9772-c4af3b976400 | -2.90116 | -50.73434 | 2025-10-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6b7680d-c957-3a3b-85e6-4b9b38b5b738 | -5.79689 | -45.78122 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42234800-a9af-30cd-a975-e0440a720b82 | -5.3638 | -45.95798 | 2025-10-05 04:44:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26b9ea18-dff7-34e8-8a4f-0e20edf23c47 | -5.69473 | -49.31339 | 2025-10-05 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2b4b686-f9d1-38a1-8fdd-238acbeebad1 | -3.53502 | -49.83506 | 2025-10-05 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb99c6a2-ad83-3e88-8d83-5acd4a4a61f0 | -3.8482 | -41.57302 | 2025-10-05 04:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 7876fdcd-7dbc-392c-955b-9cfb0dff91d2 | -6.00692 | -42.51704 | 2025-10-05 04:44:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 29472a29-db62-3c67-8660-22e844a42bd9 | -6.06497 | -41.24359 | 2025-10-05 04:44:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 525f5d1d-dd77-3fae-806a-7a8296a66a7f | -6.66991 | -42.38069 | 2025-10-05 04:44:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0c9ce26e-0a02-3d8d-8f2c-aefd341ce4fb | -5.66886 | -42.70034 | 2025-10-05 04:44:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f144d8ee-a226-31ad-ac09-d5bb760ce22a | -6.15232 | -44.65898 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 2a60d65b-9e9f-393d-9d89-dd985f2fb815 | -6.38017 | -43.88998 | 2025-10-05 04:44:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e5a0c506-90c0-352d-bec8-26ef1bf87945 | -5.79791 | -48.45713 | 2025-10-05 04:44:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98776158-2493-3fe1-ac62-1fdb0153cf89 | -5.84172 | -42.89146 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| c41b7e1e-9c54-3fb7-9e5b-30cb15cc4220 | -5.47729 | -42.79377 | 2025-10-05 04:44:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 03a305f5-2e60-3603-a1dc-c20339a77f6b | -6.70364 | -42.17439 | 2025-10-05 04:44:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 312555a2-5304-36b0-a5fe-87d5de1f9552 | -6.32775 | -41.63026 | 2025-10-05 04:44:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6a9ad1f5-fdfc-3e6e-a377-30cea953be61 | -5.8143 | -45.95003 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9db985c3-252e-393c-870e-fcbe8379098c | -3.77868 | -53.93397 | 2025-10-05 04:44:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| aba1eab5-8aa4-3519-a166-8fe35710d33e | -6.14165 | -44.63946 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24f88718-2226-3f65-a60f-2bcec2a20b89 | -6.2385 | -44.254 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5f6b1cf9-eaad-34e9-855e-b471481385cb | -5.11435 | -45.46679 | 2025-10-05 04:44:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 952e8718-0387-3472-a4a1-92a3ab895c40 | -4.25506 | -48.568 | 2025-10-05 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 41808441-cc4d-3d1e-bf2c-94ccc833545c | -6.33558 | -43.90305 | 2025-10-05 04:44:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e84655d0-0af3-3e4f-82ff-4c9997f3dd5b | -2.61308 | -49.39693 | 2025-10-05 04:44:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b995101-a19a-3e2c-9b54-71a9f37c9613 | -3.79961 | -51.19059 | 2025-10-05 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b269e10-6f0c-3a46-99ca-bdc06595b833 | -3.67517 | -41.76114 | 2025-10-05 04:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cd62d6a5-7de8-30d8-a63e-b000c22a90e3 | -6.70407 | -42.17122 | 2025-10-05 04:44:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 374d6897-faf5-371e-9ebd-39e5438d51f6 | -5.94066 | -43.30224 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6319bae3-c8a6-3fee-9a9c-794ef6c6855d | -5.80552 | -45.77892 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0df21e55-90e2-3aea-ab24-221fdcbc505a | -3.83407 | -43.49781 | 2025-10-05 04:44:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4b905fd-293b-382f-b706-0a893cbbbfea | -6.15483 | -44.64163 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1236ffbe-8436-3a8f-8fc0-f8eb93938de4 | -6.40695 | -43.05437 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 6392ec6a-d3cc-3409-9b86-e36ff1d382b0 | -6.15038 | -44.61002 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 36e5c767-ee4b-3c5d-93f7-1756d63973b0 | -5.82975 | -45.81468 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e68cdb0-aa90-3647-9f3e-624cdfa8cf23 | -3.95416 | -49.89693 | 2025-10-05 04:44:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0c1ef7f-ac2d-3497-8638-af2b73cc16ea | -6.4228 | -44.47078 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d809259-7c8b-3360-ab12-a510dee841e9 | -5.0042 | -47.21522 | 2025-10-05 04:44:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a57ba87-8301-319a-bf05-5851ab3db91d | -5.82215 | -45.81002 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8757ec59-efc3-306e-9726-dc46eaabb727 | -4.27149 | -46.75616 | 2025-10-05 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e7eb348-8b4c-34e7-836f-20cd113b90b6 | -5.85193 | -43.37471 | 2025-10-05 04:44:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb104c7b-3c8c-3825-9b74-5c6584a252eb | -6.14606 | -44.67121 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6382386f-7d80-3fef-8424-d9bd3a8d9172 | -5.91216 | -42.53704 | 2025-10-05 04:44:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2f80bf5c-1c25-37bc-b068-17a9ea474d0a | -4.53043 | -47.08153 | 2025-10-05 04:44:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0726ae5e-f7ee-3b35-9988-44c6008369d5 | -5.36431 | -45.95446 | 2025-10-05 04:44:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 866594af-6dad-3098-8958-e3f512b6fb2a | -5.91258 | -42.8909 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |


[Clique aqui para ver as próximas entradas](README79.md)
