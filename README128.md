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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99c0f2c5-f3cf-321f-8a8f-7b5c33b9bf45 | -12.64034 | -63.09382 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 373fe7f6-bd75-3f98-ad25-7ff24fbbd603 | -12.63699 | -63.09326 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7fe816bb-dbb9-3bc8-a509-ebd362607891 | -12.6364 | -63.09688 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6faf5de1-c41a-3376-adb8-1eef79e5d6f8 | -12.63549 | -63.14508 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33cc8312-8466-3fcb-9ec1-eff938b14b6b | -12.63491 | -63.1487 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7107f58e-26e2-3636-9e1b-1dc9b37e1367 | -12.63306 | -63.09632 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cac6833b-e731-36ea-8ab8-f211dd59c624 | -12.63156 | -63.14814 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aba27103-7e47-3364-950b-26e8e4c8108b | -12.45455 | -63.00359 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 6a95fac5-3e2c-345b-958d-20ff6abefe7e | -12.45397 | -63.0072 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 1a2e1015-c97f-376f-8a97-ecdb385cae32 | -12.4512 | -63.00303 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 8ab2ed6b-760e-3d56-b5af-98d5dd9728d1 | -12.45062 | -63.00664 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 688c1727-18b4-34c5-be56-d448c2aa1e4c | -12.45004 | -63.01024 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 154f0e34-83a9-3ff1-a052-64d295ba5a28 | -12.44888 | -63.01746 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6354265-0b6a-35af-ab5f-42e2df9e0b1f | -12.4483 | -63.02107 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64454c72-2155-339a-bf1f-fac6b1c3efd4 | -12.44786 | -63.00247 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b59a64e9-db81-3645-a784-5f586bc570d9 | -12.44728 | -63.00608 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d105f016-1c09-3d09-8452-02f6e1748f1c | -12.44495 | -63.02051 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05dd5575-880d-33b1-910b-2890f3bef524 | -12.44393 | -63.00552 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6d40cfb-c375-3831-8139-bcb66b4be3b7 | -12.44379 | -63.02773 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 678053ce-b964-3d5b-bd77-05bb46b7a468 | -12.44044 | -63.02717 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b8b7dcc-1b7f-3648-a8ab-9125f2247db2 | -12.99567 | -62.72141 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b5bbe163-2231-36da-b20b-76baf604dba4 | -12.9951 | -62.72496 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bee7867c-4582-3c8a-89d5-49292dcf82fa | -12.99178 | -62.72441 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e84feec0-11ae-336d-ae86-1b7f4135acd5 | -12.98996 | -62.75703 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c497008-0f60-3cf7-810d-e4087252e2e6 | -12.98606 | -62.76003 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 477dea41-3378-3ea3-8455-bee81249a714 | -12.97426 | -62.791 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e832284c-1a0c-371f-b3f9-0f7e1e4c2a0c | -12.91572 | -62.7339 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95feef97-15cf-3ef6-abd5-f848070471ac | -12.91078 | -62.72211 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47754228-f8fb-30bf-8797-c9efcd4592c0 | -12.90689 | -62.72512 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f578d3e1-9500-3541-9040-dc753f1f5e62 | -12.87997 | -62.7865 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 36746d61-b705-329e-8acd-61b3067120c2 | -12.87493 | -62.79666 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 08cfcf51-b3c9-3bd7-b454-9e8e831d17b4 | -12.87435 | -62.80023 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c52d4d8f-4294-3b1d-9adc-35a2d6fe0818 | -12.8716 | -62.7961 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c7a77577-062e-3f8e-82a6-507101dd4db2 | -12.87102 | -62.79967 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ad533f40-69cf-3b6b-9b44-5f810ccaa42f | -12.85886 | -62.79032 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6d626ea-180f-3561-abeb-3d4a003211c4 | -12.84765 | -62.79931 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11e470b1-0bb7-32a6-9c8b-4cdfab069b24 | -11.96635 | -64.76604 | 2024-10-08 05:25:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4d567bc-cdc6-3ebf-a22a-5fbd9ac7ae1e | -11.96278 | -64.76542 | 2024-10-08 05:25:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d3839dc-ff2d-389e-bced-3cad7d26a624 | -12.19295 | -63.66493 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 790f3754-39a5-363a-8a5a-033d016132cb | -12.19233 | -63.66867 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a526bafa-b573-374e-a4c4-9330513f3319 | -12.18954 | -63.66435 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43be7bcb-6794-3b70-9396-1ff5c25f51ab | -12.18892 | -63.66809 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1177cf43-e2bf-34c8-b730-e5977a584c23 | -11.99421 | -63.52896 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0efb8320-20e6-3733-b893-00bc9079184e | -11.99081 | -63.52837 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca8577f0-c6b6-3c11-a399-bdd1217f3ddc | -11.99019 | -63.5321 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13ecc537-1124-3591-8aab-7be49241748e | -11.77007 | -64.20309 | 2024-10-08 05:25:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8403ea87-1ad5-346c-a0cd-9d82b9b4a958 | -11.90546 | -64.93179 | 2024-10-08 05:25:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a956892-1939-3f4b-8339-8ea760f8c0d0 | -11.90475 | -64.93601 | 2024-10-08 05:25:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45ddc0fb-24bb-3640-ba21-5665550f9c3e | -11.69656 | -64.96857 | 2024-10-08 05:25:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 07a12bf7-8482-3fa3-9c7d-66e5418a07d2 | -11.69015 | -65.02905 | 2024-10-08 05:25:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d497634-81fb-3695-8851-e1b6f41b9ef4 | -11.68943 | -65.03335 | 2024-10-08 05:25:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83e8d92c-e066-3fa2-9452-ef0aa19a8ceb | -11.68862 | -64.97151 | 2024-10-08 05:25:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f6ab2a0-a0aa-3143-87f8-9a940cc75b90 | -11.68501 | -64.97086 | 2024-10-08 05:25:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65a5e584-d6a0-3f17-bc1b-d14aa0f2cfc6 | -11.67135 | -65.20847 | 2024-10-08 05:25:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08412626-c32c-3793-b509-9e7b1b57aef6 | -11.67062 | -65.21285 | 2024-10-08 05:25:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2a9e5439-1dc4-3acc-8ac3-d7a5783e67c9 | -11.66988 | -65.21724 | 2024-10-08 05:25:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 09d0aeb5-863c-3f5d-adaf-846c72522a0f | -11.66696 | -65.2122 | 2024-10-08 05:25:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4a78b3a6-0e1e-3daa-9192-45fb52565920 | -11.66622 | -65.2166 | 2024-10-08 05:25:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| edfaebb4-9dba-3937-9ea3-4ee1ef274503 | -11.66256 | -65.21595 | 2024-10-08 05:25:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1f5c6f50-cff6-3578-8988-f90b6f13a48e | -11.58201 | -65.00244 | 2024-10-08 05:25:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6f770a2e-0093-3865-b6ea-875098abcb53 | -11.58129 | -65.00674 | 2024-10-08 05:25:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 16d03d4c-ab6f-33e8-b95f-1e54e0ab71b1 | -4.39744 | -48.68808 | 2024-10-08 05:29:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 14b1cad7-5cc9-32ae-84f5-072c47f56b05 | -4.39612 | -48.69687 | 2024-10-08 05:29:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5a51871b-54ba-3e24-9717-a791e12e7091 | -4.38729 | -48.69558 | 2024-10-08 05:29:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6704780e-eec2-37e0-a620-c4c80e6a0705 | -4.32275 | -47.70541 | 2024-10-08 05:29:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 84c50c89-2721-39c3-bdc7-315666af7108 | -4.19501 | -48.56525 | 2024-10-08 05:29:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f4d4262b-774f-31df-ae47-c43ddc77c2f3 | -4.19369 | -48.57405 | 2024-10-08 05:29:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7465f727-cb51-3bc6-b97f-2ec0ff8c93e2 | -4.16167 | -51.0476 | 2024-10-08 05:29:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| a78dafd5-9232-3144-9e51-db8aeb92dc83 | -4.10239 | -48.25158 | 2024-10-08 05:29:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| f261ac20-f41a-328f-a852-7bc2f5d84302 | -4.10107 | -48.26038 | 2024-10-08 05:29:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 20cff6f9-d917-3e30-9171-646afb4a6116 | -4.09976 | -48.26919 | 2024-10-08 05:29:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d3e9981f-eaa9-37eb-93fa-a7bf2005864f | -3.94405 | -46.44529 | 2024-10-08 05:29:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 32.7 |
| f5dcf267-90d1-3b89-88fc-9fcacc0eee59 | -3.9381 | -46.43867 | 2024-10-08 05:29:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 2501b2b6-5ff6-3f36-b4be-93f854122f67 | -3.93662 | -46.44856 | 2024-10-08 05:29:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 63b5e257-3646-3687-aea1-b106d09a0a7a | -3.91392 | -48.33776 | 2024-10-08 05:29:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bc14d805-93c0-326a-bab1-a98623c1995f | -3.9126 | -48.34655 | 2024-10-08 05:29:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| d6421bde-2713-320c-b687-18607c421017 | -3.57629 | -54.32852 | 2024-10-08 05:29:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 84071be3-3c7a-31a5-91ed-2e5514deee08 | -3.57168 | -54.33908 | 2024-10-08 05:29:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 5046d2a5-0bd1-3d4b-a18d-3108dce26c1b | -3.47069 | -47.65727 | 2024-10-08 05:29:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2fb05e1a-8824-3c0a-9350-848fa1ba9c27 | -3.46935 | -47.66623 | 2024-10-08 05:29:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a38fe9af-1407-3139-b3bb-e265ae59660c | -3.39389 | -51.45997 | 2024-10-08 05:29:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 03f19b0a-6ef7-3bfe-9ea3-a0d8fe81d453 | -3.38401 | -51.45849 | 2024-10-08 05:29:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 49038042-783d-3095-a571-649c78da8a38 | -2.9882 | -49.52489 | 2024-10-08 05:29:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 82158829-db64-3394-a232-953a32b0d140 | -2.98683 | -49.53403 | 2024-10-08 05:29:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 4516db2b-5fc3-32aa-a43d-3437bebcbad6 | -2.97619 | -51.02587 | 2024-10-08 05:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c0d24408-b499-3323-8703-23fb43b8a905 | -2.9539 | -50.29826 | 2024-10-08 05:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 071689bb-56ce-3d91-af71-c8b04373e1b0 | -2.88114 | -52.89692 | 2024-10-08 05:29:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fe39ca4a-b575-3a4b-940e-e85d17fca76b | -2.88068 | -52.90367 | 2024-10-08 05:29:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| de719dbb-b29f-3608-8189-817808b33280 | -2.86957 | -52.90219 | 2024-10-08 05:29:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a3fe057e-d67a-385d-866d-7bbf096d5768 | -2.80032 | -48.5657 | 2024-10-08 05:29:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b59bf510-f9e3-3d87-b96f-e7431326e468 | -2.799 | -48.5745 | 2024-10-08 05:29:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 190792de-ed86-3343-9608-711b749b5535 | -2.75734 | -49.52546 | 2024-10-08 05:29:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3731b78c-dafc-3029-bb05-4b831f74a3ad | -2.46161 | -50.25414 | 2024-10-08 05:29:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 870a1b54-114e-3e86-a7a4-9299e7e15c1a | -2.29071 | -50.54427 | 2024-10-08 05:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f8e1f1ec-d1a4-381c-b496-4fdb0621cbb3 | -2.1455 | -50.69656 | 2024-10-08 05:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3e2de825-2660-3461-8f23-26815497d6fc | -2.14391 | -50.707 | 2024-10-08 05:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f37f5bcf-dca0-32bf-923b-47ace0aba093 | -1.64171 | -52.57367 | 2024-10-08 05:29:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| af6eb5a1-7561-30fb-aa65-b84bcac85548 | -1.63963 | -52.58109 | 2024-10-08 05:29:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 22cb2a13-df5a-3cf9-879e-9c95559144a8 | -1.63952 | -52.58781 | 2024-10-08 05:29:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| f6f0454f-56b1-34e1-bb56-c5b0928dc395 | -1.02914 | -53.72092 | 2024-10-08 05:29:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |


[Clique aqui para ver as próximas entradas](README129.md)
