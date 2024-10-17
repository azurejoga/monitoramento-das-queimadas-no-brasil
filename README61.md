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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 738b3134-2946-3292-a3f7-524dbc4f6946 | -9.36599 | -66.50536 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5feb18f1-1ffd-3255-9b27-170a0ce3901b | -9.36584 | -66.50198 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3206778-e5a7-322a-8f11-54a9fbee1a26 | -9.36524 | -66.50594 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 224cba1e-8dbc-34c6-a551-f6811ea41126 | -9.19145 | -66.0771 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5f66afd-d8c0-347a-ac13-875819dfd178 | -9.19083 | -66.08123 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca683423-b820-3cc2-bc85-7b0776cb2497 | -9.18663 | -66.08483 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26a65027-8060-3bb6-8a53-aeb971ffa711 | -9.18601 | -66.08896 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 167910bc-911b-3e62-9c36-2c804f890103 | -9.1022 | -66.02357 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b1bf8c1-ef7f-3788-afad-239367feb858 | -9.07337 | -65.92155 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 46e5d634-7a41-34c0-a1b1-d55f53d0ff1e | -9.07039 | -65.91682 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96ddcb10-efd4-39b4-8842-d02cc5e2c255 | -8.4563 | -66.9549 | 2024-10-17 05:53:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2939eb7a-bfbf-3ffa-b466-cdcb564dacbd | -8.45574 | -66.95863 | 2024-10-17 05:53:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1ed3b021-e11b-3ae2-8c22-5a7403b5396c | -8.45517 | -66.96236 | 2024-10-17 05:53:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86a6986b-2de4-39fd-b4ed-5f042817e2cd | -8.45461 | -66.9661 | 2024-10-17 05:53:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 40edac31-2ca7-3fa5-89b1-dac767cde9e3 | -8.45288 | -66.95438 | 2024-10-17 05:53:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51166882-7d43-3eb1-8f56-a403ba14cd44 | -8.45231 | -66.95811 | 2024-10-17 05:53:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e90fd28-0840-3eb4-8279-7b8c7f3c191d | -8.45175 | -66.96185 | 2024-10-17 05:53:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4cffdecb-5ad5-3fc6-b1f7-500c731d494e | -8.45118 | -66.96558 | 2024-10-17 05:53:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76732f2c-4d91-3c9a-849a-8408951ca2b3 | -8.44889 | -66.9576 | 2024-10-17 05:53:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8f2a3b6-c5fe-343c-b9ac-1aa08c47ebb4 | -8.44832 | -66.96133 | 2024-10-17 05:53:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4706cfc5-46de-39d0-b5f5-fdef2414efa0 | -8.44776 | -66.96507 | 2024-10-17 05:53:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b24facb-0096-3c39-b426-10f1016a383d | -10.29739 | -67.53498 | 2024-10-17 05:53:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e03d8a1b-358d-3767-98bb-591ba0986d9e | -10.27221 | -67.1649 | 2024-10-17 05:53:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d544160-89a1-3363-a64b-46f5d007a2f2 | -10.26945 | -67.27735 | 2024-10-17 05:53:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 554af8d4-130b-35c2-97b4-406b5b8ccd0c | -10.25257 | -67.09212 | 2024-10-17 05:53:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6edef851-624c-342c-bf79-5f68f86f6191 | -10.25136 | -67.09116 | 2024-10-17 05:53:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca530283-a131-3c5b-8078-0dd386acd605 | -9.61899 | -67.15788 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f630834-7307-37d0-9f62-a9d90bc51be2 | -9.57309 | -66.64369 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1dee83a3-faa5-3f7d-bc39-afe5b6df368f | -9.57016 | -66.63923 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bd01feb3-a60e-3a3f-8f77-7db99422fbe9 | -9.558 | -66.72153 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a874f59e-6697-35c6-a0e5-b5899e0da51e | -9.55742 | -66.72544 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09bcaf3d-ed5c-382a-b180-ebabc294af1c | -9.55393 | -66.72491 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2287db6d-be24-3187-bc00-9e425e9a1cd3 | -9.50032 | -67.10941 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c523dbb4-eee8-319b-a3b5-520446e5b382 | -9.49519 | -67.12022 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fdba5f90-1aac-308a-8035-12633d3beb26 | -9.47251 | -67.08671 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 052fe28f-3d1d-38d5-842c-9469518ad078 | -9.47136 | -67.09428 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a63dffe3-fd40-378a-af2c-b606f23f151a | -9.46617 | -67.15134 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd6f9ce9-8775-3e91-96fd-e1bdfa61707a | -9.46392 | -67.09698 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d5e997a-791b-3be0-b9fa-cbdf1e329cca | -9.46274 | -67.15082 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e13932b-c230-3ad1-a2d8-7ac56aa1c385 | -9.46217 | -67.15457 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0d50b25-01e5-350b-b732-d0d84303b02e | -9.45303 | -67.14548 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ef9f072-e4d6-3e38-9811-b991c8823fe6 | -9.44903 | -67.1487 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ad832c6-5c67-327a-904e-3084fda08347 | -9.44329 | -67.07066 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97a0afc4-85d4-38d7-aa1d-9655c7209391 | -9.4425 | -66.74487 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8456b71-d02a-3a00-9635-fa8145a51add | -9.43985 | -67.07013 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07587ab4-1579-3955-bddd-7a7a2e8287ed | -9.42904 | -67.16483 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abad7ef7-5064-3c52-a6a0-47aaa82c6143 | -9.99991 | -66.90549 | 2024-10-17 05:53:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02e772f9-1ed6-3fb9-814d-bef6eea90527 | -9.99585 | -66.90885 | 2024-10-17 05:53:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d01d24bf-1172-333c-941c-368f89d47617 | -9.96684 | -66.86462 | 2024-10-17 05:53:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6047d6d-14a0-314f-b6b1-df163ba6c8c5 | -9.9386 | -66.75694 | 2024-10-17 05:53:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f03bddc9-324f-3522-b75f-18f0361557fc | -9.90068 | -66.86711 | 2024-10-17 05:53:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f92e134-b1fe-31ae-82ea-3e38bcabf871 | -9.85418 | -66.71687 | 2024-10-17 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a08a57a9-20d3-3eb4-a25f-584e9a6a82ff | -9.84815 | -67.00511 | 2024-10-17 05:53:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac6614bd-4c92-3701-9464-8d9bf411b4c6 | -9.81646 | -67.26426 | 2024-10-17 05:53:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb6ee023-0a78-3a6f-8267-60b726bbbd7e | -9.81303 | -67.26374 | 2024-10-17 05:53:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c01973c-eb5f-39e3-9616-687f0a868c50 | -9.77152 | -67.19249 | 2024-10-17 05:53:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbee7c65-1d49-3038-a2d1-5e04935324ae | -9.74776 | -66.5354 | 2024-10-17 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bfb7578-8f65-3f94-96a5-52407bb762f7 | -9.72529 | -66.6376 | 2024-10-17 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b86d5d5d-619e-3005-83de-7aee0bf53765 | -9.71637 | -67.06778 | 2024-10-17 05:53:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f48926f9-6df9-34ef-a239-d771f1d602fc | -9.6676 | -66.83281 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06c350f3-01d9-3dea-82e7-9249ca5ec3f2 | -9.6647 | -66.82841 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28f0dc03-481d-37bc-8812-7bcb6b5ec700 | -9.66412 | -66.83229 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ceb72c44-9ca7-3619-b0d9-f35dcff3a762 | -9.56958 | -66.64314 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f06bb00-2f25-379c-a239-373d5e82eb2b | -9.55684 | -66.72935 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1e9dfcf-1108-3f77-bd71-a632f9eccb71 | -9.55451 | -66.721 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65e27b57-fea2-3412-b7a4-36c02f4355fc | -9.49688 | -67.10889 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8fa715d9-9d25-3998-8fb1-711e972fdde1 | -9.47422 | -67.09858 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0811d9b9-b4b8-3d5b-9e37-06911bf66802 | -9.47194 | -67.0905 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9b2617a-a13a-3866-9602-6b7f647d0839 | -9.47079 | -67.09806 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58ba17a0-3c98-3291-b29e-80a16a65d99f | -9.46908 | -67.08617 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e502e240-526f-3ae7-be7c-8617c7c57ce6 | -9.46735 | -67.09752 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77c0c2ca-b64a-3cc1-a96a-b4f558bb732a | -9.4662 | -67.10504 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01e6efe4-c594-3c69-ac64-079e1dd62d56 | -9.46334 | -67.10075 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33d79874-d605-336c-9571-c271e12e476b | -9.45874 | -67.15404 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3dc56166-4848-3b03-bc86-9bde66940837 | -9.45246 | -67.14923 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 177cca60-1dd7-38a1-89a9-58709a7a2365 | -9.45189 | -67.15298 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99ad60a1-cc87-3fd3-bea2-bb09700d86ce | -9.4496 | -67.14494 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00249aef-9946-33ad-b0b1-994fe60a12c2 | -9.4456 | -67.14817 | 2024-10-17 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8238665-3f95-311a-986d-d23a0ec4f2cd | -10.0956 | -67.22458 | 2024-10-17 05:53:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f80df98-4163-3adb-84ce-4521aa0e8cfb | -10.09502 | -67.22836 | 2024-10-17 05:53:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2812b920-f40f-35ae-8679-bf19bb2ed36c | -10.02938 | -66.96945 | 2024-10-17 05:53:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c54befc4-687e-34ed-8946-b54ea3f4b55e | -10.02134 | -66.92857 | 2024-10-17 05:53:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0512676-d82f-31d0-944e-5cacf2f73582 | -10.02075 | -66.93245 | 2024-10-17 05:53:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d276682-cacf-35d9-8b9d-2753390170a8 | -10.01728 | -66.93192 | 2024-10-17 05:53:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce61df45-fefe-3de3-b002-2e6593719499 | -10.01621 | -66.82022 | 2024-10-17 05:53:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29d72930-af78-350b-9141-bc619671382b | -10.00049 | -66.9016 | 2024-10-17 05:53:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c644ba2-55c7-3013-9332-cb4693d63d6c | -9.76292 | -67.34094 | 2024-10-17 05:53:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dc42381-d67e-30c6-8e3b-08dd88fcb4b2 | -9.68053 | -67.37784 | 2024-10-17 05:53:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 947f1f3c-2bb5-3a15-a6f1-41762ff4ab4a | -9.67997 | -67.38154 | 2024-10-17 05:53:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14d03640-96bd-3b6c-8c5a-5a4faec4d47c | -9.67712 | -67.37731 | 2024-10-17 05:53:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bda1100-698b-3172-b719-f1516a8c2e13 | -10.0978 | -67.34839 | 2024-10-17 05:53:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c839a8d4-a4ac-343a-b536-756ea04450ca | -9.41662 | -67.82379 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab640fd2-1e35-39a6-8b99-0d746061c1de | -9.41381 | -67.81968 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a376086b-9043-3179-90d0-0f3dceb45564 | -9.40941 | -67.84848 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09dbb9e4-2805-3070-bfed-cb5879894216 | -9.39625 | -67.75415 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34206b04-54b8-3767-8a7f-eabacc9cbd40 | -9.39289 | -67.75363 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eaa55de0-36ed-39d9-a4aa-b2b296a54f97 | -9.37592 | -67.86533 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 83138860-c048-310d-9961-be2f3088d24f | -9.37587 | -67.78481 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1693d331-eb1f-3ef1-8688-2426a2413c93 | -9.37537 | -67.86893 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ead8de4-a522-3f0f-a7fa-f5a6e5f9fec4 | -9.37371 | -67.86549 | 2024-10-17 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README62.md)
