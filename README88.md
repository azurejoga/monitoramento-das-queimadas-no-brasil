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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1feb69a8-5cf0-389a-aac7-39697fed8a35 | -7.73729 | -61.57016 | 2025-09-01 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5ec2a38-a5b8-3642-bc99-c28750d17ceb | -6.83045 | -52.82415 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7776b09c-28f4-3486-8c7a-ef77a6f90a82 | -7.09461 | -63.0409 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b45daebd-c4ba-30e1-a3f4-6948702a7b3b | -7.70256 | -61.4799 | 2025-09-01 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1b4586c1-ae39-397e-9642-dcdf153db26e | -6.81779 | -52.81757 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1e2df26-e864-3321-912d-0b86aac2bde8 | -7.06755 | -63.0674 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c3c1349-a70f-358c-b4dc-30a72df0de98 | -6.44166 | -55.62379 | 2025-09-01 05:50:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6590aec-f61b-3bba-8980-44350a8f3739 | -7.08689 | -63.19747 | 2025-09-01 05:50:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adbc7a2d-7d38-3d4e-b672-3f19a9efb4c7 | -6.43617 | -55.61837 | 2025-09-01 05:50:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c6e453b-4dfb-3e2b-a7cd-a1ce6e143d3b | -7.69471 | -61.47475 | 2025-09-01 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 738734ca-bb8a-3fe3-bfaa-12b256c4fe2d | -6.34055 | -53.42854 | 2025-09-01 05:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b6d63dc6-67ee-3513-bb46-2392363d6007 | -7.59066 | -61.62817 | 2025-09-01 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8054511-466d-3ed9-b03a-acac1d44aad9 | -6.81683 | -52.82504 | 2025-09-01 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ff5db4ee-5599-3736-9a7e-e957a6664240 | -7.56635 | -63.41193 | 2025-09-01 05:50:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6a97b48-983a-3ef6-8ff4-322502cbac05 | -8.85333 | -70.62482 | 2025-09-01 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93a5b85c-be7a-385b-8cf8-28e87237f9ad | -9.00998 | -65.69561 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1de19e68-522e-3281-a24f-61a9bccf2422 | -8.66296 | -62.92369 | 2025-09-01 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5c539679-2500-3cba-9f89-345bbaf8437b | -9.13574 | -65.85402 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5573240-2cd5-3af8-948c-66207c788142 | -9.1396 | -65.85098 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a6e1340-dc0d-32ed-8c1a-ea25c0ce73ba | -10.26602 | -68.78741 | 2025-09-01 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b0c8de9d-74be-328b-9495-a7b657f87f31 | -9.05114 | -68.36687 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ee721a59-34ab-3dd4-b72d-494985217e9d | -9.83068 | -65.05988 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89b04b14-cf0d-3fad-a029-d131045a9fca | -9.07298 | -65.42252 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98b2688e-5b95-3063-b17a-d62d6e2d9cc1 | -8.62407 | -62.58964 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab6edd2d-74d7-36cf-ac64-8e612ea0dac5 | -9.07871 | -65.43114 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 397adb24-c3c3-30c8-9235-06c49a05150b | -8.83322 | -71.36784 | 2025-09-01 05:53:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f8e5d992-af4a-3ea1-a88f-bdf2a8d96c51 | -9.17907 | -67.72968 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7327678d-f261-30ae-adf2-16b89d5a054b | -7.95936 | -63.49028 | 2025-09-01 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d046df4-8430-3967-a548-3a7ff87a943e | -12.43657 | -63.92698 | 2025-09-01 05:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c49831cb-100d-3bae-a470-ad25509e6872 | -9.14356 | -65.84784 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1690466-6215-3e85-a568-75ec435f9132 | -9.12378 | -65.54502 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8939c7ef-d355-3cd1-96ec-1f2371898788 | -8.63275 | -62.5857 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65985618-ab70-320e-9878-35355beeb21a | -12.42326 | -63.91024 | 2025-09-01 05:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 40d87540-ef0d-347a-baa0-2b9ebd9a483b | -8.06833 | -70.83465 | 2025-09-01 05:53:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c107a9c6-c3c1-30fe-93d9-2388de3f2dfb | -8.72073 | -62.4146 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bba50869-8259-3df6-85d3-f524883e994e | -12.44882 | -63.92383 | 2025-09-01 05:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f2ae362-385d-3b20-8998-74e29f99a61f | -9.02586 | -70.66461 | 2025-09-01 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f4a070e-d7fe-3d6a-a4c5-8ab21cf77959 | -9.06953 | -65.42199 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be295735-d23d-3a2e-a9f0-e64e742449e6 | -8.5581 | -63.00999 | 2025-09-01 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e18e1368-10a8-34a5-8070-1edcebc2f1e6 | -9.13465 | -65.54286 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fac06ae0-dd41-3654-841f-907983b728fd | -11.5192 | -54.47887 | 2025-09-01 05:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b9bd5ac-2765-3877-b3a0-f0aee9cd483c | -9.07066 | -65.43761 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1935a818-be5d-31f9-a4d9-eabf16099f54 | -8.61613 | -62.58849 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 379625e5-ce9f-3b93-8470-20a21f94fa14 | -9.17184 | -67.71066 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e45e25ac-989f-3aa4-965f-c35af8546cc9 | -8.0949 | -70.2207 | 2025-09-01 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 693d6726-2501-33ca-9b57-b7888e40978b | -9.17574 | -67.72914 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8a8bb7a-e51d-3497-bff2-dc0b35959068 | -9.83539 | -65.05251 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f374de13-31ec-3f6c-a236-c953d406690c | -9.12664 | -65.54929 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0031a7e8-7bd8-3c3b-971a-a1807a8bec58 | -8.65353 | -67.24835 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 21d496e6-da5f-341a-995f-1f727c20c5a5 | -8.44411 | -70.1399 | 2025-09-01 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 840d5322-4fbc-3ca0-9469-1162b16e8fb1 | -8.68555 | -62.40232 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf0ee3d2-7e1f-39bd-9f1d-056062ad51eb | -7.90512 | -72.87532 | 2025-09-01 05:53:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a40a1a39-5f68-3c94-8bf1-232515f7c753 | -8.5093 | -67.12894 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c407c09-866d-305a-93e2-f9b7f6fd72d3 | -7.8141 | -71.94793 | 2025-09-01 05:53:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 906fc6d5-24bc-3fb6-a3d9-2750f7ff902e | -7.66163 | -72.29138 | 2025-09-01 05:53:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca1dd0af-e26f-3941-989c-299bbf2698a0 | -8.37885 | -70.75984 | 2025-09-01 05:53:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce64debf-3913-31f7-be61-bacb2fb0bee2 | -7.93489 | -63.01171 | 2025-09-01 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b409a3a7-3eec-3e98-bd52-025f519694f0 | -9.01055 | -65.6919 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e85c11b4-6a8c-37b0-8aa5-ac12617db75d | -10.51898 | -69.23392 | 2025-09-01 05:53:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c578758d-c724-3cf1-a857-bb26a8ea3320 | -12.43755 | -63.92886 | 2025-09-01 05:53:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43d29f76-40f2-3315-a25f-011ffd1c427f | -8.52361 | -72.69572 | 2025-09-01 05:53:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b1967d2-2858-35cb-bed5-6acf8549cbb9 | -8.54967 | -63.01365 | 2025-09-01 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdfa8fbe-dd3d-3a76-8268-ad4f3ec81cb0 | -7.75114 | -70.27 | 2025-09-01 05:53:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fdba54d-76db-3096-8b0d-6ea1fe775949 | -9.3585 | -65.44563 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b916dddb-f840-3d3c-b7db-db8d9719dd60 | -8.83812 | -64.1509 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 269063bf-2de4-32f4-8312-01c3727adb51 | -10.08634 | -68.99492 | 2025-09-01 05:53:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| daadbb73-0d44-3995-8539-2b1ae90aac01 | -9.14071 | -65.84363 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f9bc92c-4b44-3353-829e-3dd09fae83d3 | -8.53683 | -64.15161 | 2025-09-01 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b6207396-2f2e-3ee5-9a2b-5e49bad75319 | -9.27775 | -67.64516 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 566653f8-eb50-3973-9e11-4feb68d45101 | -8.72775 | -62.42283 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd584646-20db-3565-8f5e-898ff2be3722 | -9.07353 | -65.44191 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f8f205f-c7f5-3b14-95d2-5a4732116e10 | -8.65075 | -67.24434 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67d76e34-7693-30a7-bbf1-9b95600cb367 | -8.64143 | -62.82508 | 2025-09-01 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e021853f-3977-38eb-800c-904c6d4bf6ce | -9.82775 | -65.0554 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25819d68-09a9-3685-8a63-64446adf1996 | -11.64984 | -57.3614 | 2025-09-01 05:53:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f5ad3c7a-7271-3dc0-b551-88f21afba5e7 | -8.73728 | -62.41364 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4369869f-6be3-3695-9126-fcf38cbb7621 | -8.96714 | -65.97401 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 079a0caf-ed80-3a67-a600-ff662b52e150 | -8.03906 | -70.06788 | 2025-09-01 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8eb9f9e-e44b-302a-9a75-d7ed52c1e708 | -7.46296 | -70.13562 | 2025-09-01 05:53:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2925b10b-ba53-39e0-b36f-2ef74f4b828d | -8.85054 | -70.84547 | 2025-09-01 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 860b0d43-4003-3d9a-91c6-04330250fb91 | -9.64342 | -63.11744 | 2025-09-01 05:53:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e5c56979-031b-39a5-8f57-e102576ad344 | -8.62481 | -62.58455 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87c09d1a-4951-30a0-bbdd-255f24340167 | -9.87186 | -65.02569 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3651291f-4792-391d-acdb-98fa6be32728 | -14.31231 | -60.34715 | 2025-09-01 05:53:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 16cd583d-ddde-3323-ae22-31a0a15c5c89 | -7.97263 | -63.66546 | 2025-09-01 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7a1aeee-d140-3c49-ab34-eae4f47f410b | -8.6441 | -67.24328 | 2025-09-01 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 835784b1-dfd8-3188-a66a-0370b5a1a855 | -9.08158 | -65.43543 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24d17f8a-8b2a-31e2-b955-e6dcb52c0ece | -9.45391 | -62.34615 | 2025-09-01 05:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0508e20-15c4-375f-8fec-e32c677d2f4a | -9.13008 | -65.84563 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 535ea528-2fde-3e93-8354-4e6fd4720597 | -9.14752 | -65.84468 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e5dfb69-ce63-316d-925b-4e00e29a9701 | -10.50066 | -68.1047 | 2025-09-01 05:53:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4dee92c-961b-31cc-a0e1-01134ff8b245 | -9.14095 | -65.54767 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05ad51e1-12c1-3182-9f0b-195107e77af5 | -8.69643 | -64.20418 | 2025-09-01 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d981b89e-f644-3f8f-bbf0-cf52907e80bd | -9.06551 | -65.42523 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22a5cce0-d835-3295-85b2-d56dc8ea63b7 | -8.63597 | -62.5914 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50b59ffe-5f90-3f87-9f38-c3f6a789f389 | -9.88191 | -65.00692 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0024083-6707-39a6-ba35-0666eefbfa0e | -9.07295 | -65.44568 | 2025-09-01 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 903616a0-593e-3df2-95aa-b386ee162a5d | -8.71972 | -62.42159 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59a9605b-58f2-3932-9bb0-eacb2ec3e997 | -8.60893 | -62.58226 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4861b8d9-42ce-303a-a79c-cff1d788963a | -8.68104 | -62.40519 | 2025-09-01 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README89.md)
