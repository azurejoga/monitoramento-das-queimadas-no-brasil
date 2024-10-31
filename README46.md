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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6abc8fe-1b1a-361e-bbd5-27552409d50f | -1.15345 | -53.38688 | 2024-10-31 05:42:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9add3c4c-90a1-315d-a142-ae2f7eee64b7 | -1.15238 | -53.3829 | 2024-10-31 05:42:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 34433cb2-bc9d-321f-93d3-fdb0069d556c | -1.15171 | -53.38737 | 2024-10-31 05:42:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b480971f-16d6-3b0d-ac2b-2f459b41cc36 | -1.14766 | -53.38523 | 2024-10-31 05:42:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 856ae934-8e2a-3a2f-b5b6-0edb5ad84c4b | -1.0937 | -53.65485 | 2024-10-31 05:42:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1789d4df-ada1-376d-8bba-9c38541d2b97 | -1.08783 | -53.65444 | 2024-10-31 05:42:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| feb69e5e-d688-3db5-8e7b-8f3c46b8807b | -1.08719 | -53.65859 | 2024-10-31 05:42:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7823ab8-db37-3b09-a7c8-f73f7648b786 | -3.20883 | -53.85353 | 2024-10-31 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f6d40d9-9b37-397a-8b99-d369be80c58e | -3.20355 | -53.84814 | 2024-10-31 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06c94796-5501-3dd9-84d5-f6e388f482bf | -4.01679 | -54.80062 | 2024-10-31 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 520cd676-7d95-399c-a0bb-9981fa652527 | -1.4774 | -56.00655 | 2024-10-31 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05425a2e-5f25-3d4f-a97a-83c23c41f591 | -1.47242 | -56.00579 | 2024-10-31 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b84ddcf-31ac-3a53-9254-88de445c5df4 | -2.35092 | -56.50799 | 2024-10-31 05:42:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb8828a0-b083-3bd5-a7d0-5491e407830e | -3.07056 | -59.21387 | 2024-10-31 05:42:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 5cccbbf7-b346-3936-b759-6ee4f0ca7ced | -3.06647 | -59.21321 | 2024-10-31 05:42:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| a08adcfa-cb3b-3ee6-a71c-c5ca7414f4a4 | -3.78151 | -59.19254 | 2024-10-31 05:42:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 803cba45-4ff3-38b8-9aca-be3d4c2977ac | 0.07587 | -60.5345 | 2024-10-31 05:42:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76ea5a8e-b4d4-3d50-8315-3f2cdf78a900 | -0.75997 | -62.90051 | 2024-10-31 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03cf8ff3-2b2b-3e81-afff-5217d0ecf92a | -0.75828 | -62.88947 | 2024-10-31 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92383348-2756-3c10-be43-05cb07bd055e | -0.75663 | -62.9 | 2024-10-31 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de77694b-f37c-3d97-80d8-be0fe0513522 | -0.75495 | -62.88896 | 2024-10-31 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ffe00a0c-8fe4-3f95-adb9-14f580e9b394 | -0.7544 | -62.89247 | 2024-10-31 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93569788-7fe0-3ffb-89d1-7653465a40a1 | -0.69872 | -63.20508 | 2024-10-31 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b132767-a4b9-3ea0-9264-07c27626b5c7 | -0.67343 | -62.93025 | 2024-10-31 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24deba5b-2d37-3fc5-a31f-19b75d177835 | -0.67064 | -62.92623 | 2024-10-31 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ebde1ac-36aa-34ff-b87c-6bc6418168b2 | -0.76385 | -62.89751 | 2024-10-31 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f88770a1-0bdf-3fce-89fe-ec3521c1062d | -0.7633 | -62.90102 | 2024-10-31 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f50760ca-620e-347a-b513-9e89ad83ac21 | -0.76052 | -62.897 | 2024-10-31 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3ab1192-5a16-3c05-9c71-fc6cd6cb6e55 | -0.75773 | -62.89298 | 2024-10-31 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66409f15-f179-38a6-b91a-2eda697665f8 | -0.75718 | -62.89649 | 2024-10-31 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01b61651-531d-31fe-89b5-c48c3b11a522 | -0.69926 | -63.20162 | 2024-10-31 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8ea2f36-fd2d-33ed-b2bd-a000dda0d86b | -0.67397 | -62.92675 | 2024-10-31 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecdbe7d6-f219-30ca-abeb-892cb9c4fa25 | -0.6701 | -62.92974 | 2024-10-31 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c622f313-ea2c-30e0-9575-8bd0a35b4b42 | -1.07008 | -62.65514 | 2024-10-31 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b19530e-405a-3cad-ab6c-126eec800914 | -0.78969 | -63.08085 | 2024-10-31 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 62662026-d685-3eac-8744-355d10b3b6b1 | -0.77125 | -62.89188 | 2024-10-31 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4ba6a74-3ae1-326d-8462-c1ae00e45865 | -0.76774 | -62.89452 | 2024-10-31 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1f293cb9-3820-3c97-862f-a449ef350d23 | -0.77459 | -62.89239 | 2024-10-31 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c6e2eda-3939-3265-a013-a646743041f8 | -0.77071 | -62.89539 | 2024-10-31 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61761197-4d65-3d82-8e9a-9347a7cd482c | -0.76719 | -62.89803 | 2024-10-31 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 834ad8a6-b15e-3e84-94d6-d437056421d4 | -0.76664 | -62.90154 | 2024-10-31 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bdcc4640-8169-3812-b7df-f495a46788fe | -8.72327 | -66.65421 | 2024-10-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f9ae20a-f06a-374f-8fd3-dfd27cffac92 | -8.70226 | -66.61481 | 2024-10-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee2b2d5b-61db-3148-8d9a-3b898044678c | -8.69838 | -66.61779 | 2024-10-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ba0e4db-042d-3b7c-810e-47566cf7819d | -8.58626 | -66.76644 | 2024-10-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5971ff5b-16e0-3bce-8697-2d54f25ec166 | -10.11891 | -66.97349 | 2024-10-31 05:44:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14c1a06c-b151-3cdf-b5ea-f7a1bbc0bacd | -9.70968 | -66.98001 | 2024-10-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13e527a6-d19f-343f-a5a9-88d2e2b03369 | -9.70635 | -66.97947 | 2024-10-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc43a368-9963-3a3f-a7d1-4a6284ecd64f | -9.70081 | -66.97131 | 2024-10-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99ab4a62-6db9-37e6-8bad-3e0298066455 | -9.65461 | -66.63869 | 2024-10-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee4bc94b-486b-360b-a64b-e6cccd956b7c | -9.63667 | -67.24619 | 2024-10-31 05:44:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0117d644-b053-3209-a452-8b4144b75904 | -9.6339 | -67.24207 | 2024-10-31 05:44:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57221633-7b57-37cf-8d16-26bf59fdee92 | -9.63333 | -67.24564 | 2024-10-31 05:44:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b576f89-8011-3884-baf8-83b218abecd3 | -9.63275 | -67.24924 | 2024-10-31 05:44:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2cc611c4-8e5e-3378-aa1b-d411cdc83cb7 | -9.63055 | -67.24152 | 2024-10-31 05:44:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0174d90-b854-3c40-9756-9710b232c179 | -9.54776 | -67.35002 | 2024-10-31 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 52165a81-3f50-3c83-be40-d50ebfadd24d | -9.54718 | -67.35364 | 2024-10-31 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 152efa47-588f-31fe-957d-4f79286c93c8 | -9.50696 | -66.56075 | 2024-10-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b34f9fa1-f243-33fe-a32b-bf7b892e1327 | -9.5042 | -66.55672 | 2024-10-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a23b2e39-aa47-3a0d-979c-c16c8227ca50 | -9.50365 | -66.56022 | 2024-10-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99266ea8-cb66-3c03-aff7-012f369f01ef | -9.43179 | -67.14313 | 2024-10-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e5e5b55-4450-3296-9715-f3c3226bf778 | -9.43122 | -67.14671 | 2024-10-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f89ecaa0-2e7c-331e-9e83-d4da5febf563 | -9.40472 | -66.56231 | 2024-10-31 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 36c5ee1a-172a-31d6-8baa-e84b19810ebe | -9.30788 | -67.76553 | 2024-10-31 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f7dc55cc-ed48-3edf-952e-3e9340557bbd | -9.28048 | -68.78191 | 2024-10-31 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26b0ff2e-b1b4-3e4f-a2ab-9876d3bb9f61 | -9.25384 | -68.18674 | 2024-10-31 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 523b3826-290d-34d2-921e-8fb3cf8decf0 | -9.20336 | -68.40934 | 2024-10-31 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2984369-37ba-3fa3-9d15-0e2919059099 | -9.1635 | -68.34673 | 2024-10-31 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a51631c-0342-344a-be1a-aba22b110fde | -9.16194 | -68.34708 | 2024-10-31 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9431d67c-9887-3082-bfcd-d60f4e10a96b | -9.11882 | -68.4366 | 2024-10-31 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f12011e-2a7d-3c5b-abb1-f6fb8e40c3b2 | -9.11532 | -68.43604 | 2024-10-31 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ae79146-d33e-3241-b3fe-acef49432454 | -10.59286 | -67.79536 | 2024-10-31 05:44:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef919e5e-5bb3-38c4-a696-1ba3c5ec871d | -10.59227 | -67.79903 | 2024-10-31 05:44:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6c1230e-e552-3346-bf3f-5482178c6c20 | -10.58889 | -67.79847 | 2024-10-31 05:44:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15180c1f-e4fd-3112-95f6-bee0d89ecd91 | -10.54902 | -67.8224 | 2024-10-31 05:44:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96da50a0-504b-3196-afff-2672fe6238f5 | -10.53402 | -67.78605 | 2024-10-31 05:44:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2a9ec23-3d6c-306d-a94c-2844b215614b | -10.49138 | -67.89992 | 2024-10-31 05:44:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be3655b1-0050-39b5-ab1c-65684bd94363 | -10.48799 | -67.89937 | 2024-10-31 05:44:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0123a17a-3231-3d33-b6b2-8c16822ab1ff | -10.27761 | -68.0481 | 2024-10-31 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af73074b-2dfd-3089-b686-1aefe178ead1 | -10.21141 | -67.84699 | 2024-10-31 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 014ad92e-395c-3a3b-ade3-10ba26b88f32 | -9.94924 | -68.62128 | 2024-10-31 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6df4ef62-db2f-3843-9ff4-f86e2ce89e00 | -9.94574 | -68.6207 | 2024-10-31 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a52a41bd-23bd-35ac-b21e-14b4fc12ecb3 | -9.9451 | -68.62464 | 2024-10-31 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6536838-cfe2-359f-a5ef-028ebb3a66b4 | -9.93142 | -68.97147 | 2024-10-31 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 715df012-4469-3a46-b7aa-e860291c111f | -9.86307 | -68.96925 | 2024-10-31 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1af64da3-96d6-3368-a095-84bb139f4d16 | -9.78858 | -67.68049 | 2024-10-31 05:44:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 179e4635-5cca-319d-82e5-0edd5633a985 | -9.7852 | -67.67993 | 2024-10-31 05:44:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9220afa1-b7bf-39c9-97e3-eac50ed580c0 | -9.65174 | -68.52959 | 2024-10-31 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56a745af-d37e-3204-8a06-4b1dd38e5fad | -9.41256 | -68.61708 | 2024-10-31 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5b082e9-f1cc-3611-889a-b2a0dc86868f | -9.33969 | -68.77399 | 2024-10-31 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a093ce0a-eb38-334b-b76e-e522b2be1bc7 | -9.33681 | -68.76936 | 2024-10-31 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bffa948a-b9b9-3360-abdc-89c53c2f46ba | -9.33614 | -68.77341 | 2024-10-31 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25575dfa-2b94-34d9-8858-f81f491b161d | -10.68054 | -68.81145 | 2024-10-31 05:44:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 712112a0-4f9e-3e7c-83c5-0f6b0c42ad62 | -10.67704 | -68.81087 | 2024-10-31 05:44:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6fb12f7-6c97-3b7f-9163-706c68bdb580 | -10.51995 | -68.54811 | 2024-10-31 05:44:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c59aa04f-81bb-39e1-8aaa-900cf5ec173e | -10.41843 | -68.39346 | 2024-10-31 05:44:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 925524d9-c8b7-3a72-9581-51ed4981eed2 | -10.1569 | -68.3353 | 2024-10-31 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84f0ef09-37ed-3474-a152-e461efafad59 | -10.09716 | -68.38126 | 2024-10-31 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 14b2352f-1239-3d09-880e-5f6025a8da6a | -10.09433 | -68.37684 | 2024-10-31 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b68ebbf-3f03-34f5-b13a-adbd9b3b2ef8 | -10.0937 | -68.38068 | 2024-10-31 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README47.md)
