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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c932e79b-3c7f-3a41-b798-746c7d13a219 | -17.1311 | -57.44871 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 59fd068e-4e4f-3bba-a36f-292b92da8ca1 | -17.13057 | -57.36032 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 04a0e4ad-7b4c-379d-bff8-d3be6e597d49 | -17.13037 | -57.45261 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| fd02fea4-dac5-387a-ab07-a6f8249a668e | -17.12988 | -57.43232 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 266f0a81-a252-3618-b458-4aae49f82977 | -17.12985 | -57.36416 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 29645c9e-3da2-328a-b736-07cfbe041e99 | -17.12968 | -56.84926 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| cbc0cbbc-ad60-37c9-91c1-ef106733b64a | -17.12915 | -57.4362 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0194b7ab-778a-3d03-922d-b423b4a66051 | -17.12869 | -56.85465 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 91f5c762-0160-325c-8650-f654f828e0ae | -17.12842 | -57.44009 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ad97bbcd-8069-36a8-8605-cb2617bd91d5 | -17.12769 | -57.44397 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 007d7c3a-4989-372b-87d7-30279436c008 | -17.12696 | -57.44787 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| e2b43e48-bdc2-3bf2-ae19-a8f03c4bdfb2 | -17.12646 | -57.3595 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 8b521a2f-132b-3cb2-9ea8-e8ff49c7b1d6 | -17.12623 | -57.45177 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 0265ff55-f4b7-3ace-a99c-46ca68f4144f | -17.12575 | -57.43148 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 764ee5c8-c06e-32c2-9150-c64efbaa33e0 | -17.12569 | -56.84847 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| df220931-3bbe-3bcf-a15e-a000b7f4ef96 | -17.12549 | -57.45567 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ad85a8da-9b2b-3f03-b183-fc95102ab256 | -17.12502 | -57.43537 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a388232d-1e8a-385c-9aad-7a823c032ac7 | -17.12476 | -57.45958 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e971a360-817d-34cb-aaf5-a997eb98f8b8 | -17.12469 | -56.85385 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e2f097fc-0049-3bb9-a05c-7c6fe6fecebc | -17.12429 | -57.37101 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| ed22f2f5-db71-32b3-bc44-c6caec33b4b9 | -17.12428 | -57.43925 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 323fccb8-bead-3860-a3df-b6a1a30e363c | -17.12403 | -57.46347 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 274b792d-0c6b-3ff7-8e5b-c6e7444f8b9c | -17.12355 | -57.44314 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 2f193d77-8703-3989-aa4a-4e0fabd94ca8 | -17.12282 | -57.44703 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 1ca4d0e5-a1b8-3a41-a2d7-1e5cf75f5657 | -17.12234 | -57.37132 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 28912256-8e27-3f00-8f08-7a449e8108f8 | -17.12209 | -57.45093 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 1e43ed1c-8294-362e-9b97-cdf00ea56192 | -17.12135 | -57.45483 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| d83c9fae-5afd-3ad3-96e9-fe60335afd73 | -17.12089 | -57.36634 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 9aae9d23-e4be-3228-8e06-0250ba0ed6c1 | -17.12088 | -57.43454 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 44bafe8e-0fc2-32a7-826e-a83c64f57716 | -17.12062 | -57.45873 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| d8156f14-4d29-3b18-8a97-8d93d1d20d99 | -17.12017 | -57.37019 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 346e3bd8-d312-3fb1-8b19-d9d233c7cb2d | -17.12015 | -57.43842 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1646cbe6-cd0c-3010-abf0-252fb85417fe | -17.11988 | -57.46264 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 908fc3f3-d6e3-3a7e-8d34-464034ef5b9c | -17.11942 | -57.4423 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4a21f5c6-b7a3-354f-b52c-c64d3546fb09 | -17.11892 | -57.36662 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 6f276ffa-3ea6-3ed3-ab03-1d168b34c79e | -17.11868 | -57.44619 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| a009a610-f678-3309-a400-1f96eda8f6dc | -17.11822 | -57.37048 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| a628c629-5cdb-3128-8509-10ddac01a2d0 | -17.11795 | -57.45009 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 7c902d62-3341-32c0-ab19-f0ca0b38df29 | -17.11721 | -57.45399 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 29522fc6-a061-35f5-b19c-cff3079bb001 | -17.11677 | -57.36552 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| f7dda8be-64ab-3653-9b28-34f04cf7af91 | -17.11674 | -57.43369 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 21226c00-9290-3d3a-bb4f-375bee81f249 | -17.11648 | -57.45789 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| cdd30a24-f055-3585-ba3f-7ed40b64b38a | -17.11605 | -57.36935 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 18b875a2-d4e2-3c4e-9c67-2143f4dde2af | -17.11601 | -57.43758 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 2c0e1cbd-fbbe-3a8c-af07-358cf201d7bd | -17.11574 | -57.46179 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 33b2bada-f222-3394-8a16-c452260b1eeb | -17.11551 | -57.36194 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| c2caf077-0ed1-3e40-9362-c68ead382e25 | -17.11529 | -56.8563 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d219b13d-f7e9-3dc2-9625-34c7c8f36689 | -17.11528 | -57.44146 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| ebf1c8b1-6fc1-373f-9085-83833e1556ff | -17.11501 | -57.46569 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 925d20a2-1e04-3a07-9505-ed03e3e22ff5 | -17.11481 | -57.36579 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 286ac1ee-cec2-3fc6-be73-600aa5316af5 | -17.11454 | -57.44535 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 9c54acb0-f07d-32b0-a8c2-258888f206b8 | -17.11411 | -57.36963 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 1351dce8-a1e8-32bd-82eb-3fa52eddf71a | -17.11381 | -57.44925 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| b136c232-7ee7-3ae1-81d0-be4ee24491fc | -17.11307 | -57.45316 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 9e392df4-0d19-3bc6-b23e-527171c47f74 | -17.11233 | -57.45705 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 2541f90d-186c-3405-85da-772858aa9a45 | -17.11187 | -57.43674 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 15245dd0-743b-3b45-aad7-6b70c8108de5 | -17.1116 | -57.46095 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 942f3f22-3c55-383b-a3b3-8b324b428b25 | -17.11139 | -57.36111 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 0f8565d9-a1ee-37a1-8f60-94b5faf297ed | -17.11114 | -57.44063 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 6fdcb9d1-2613-3147-8fde-adcf6620487a | -17.11068 | -57.36496 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 734c0568-0f18-3d2b-a4e6-5df217350808 | -17.1104 | -57.44452 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 30fc3707-d29e-35c2-94b1-3b9c70c5d83d | -17.11037 | -57.43724 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 02228498-48a4-38a7-9d9d-634682856036 | -17.10966 | -57.44841 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| c1a80006-6893-3140-b926-82711691beda | -17.10966 | -57.44113 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| e352b345-4fbc-3089-b6e1-7ffb74ca0935 | -17.10895 | -57.44503 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| 0d315a40-0515-3efd-8248-70636ea303f9 | -17.10893 | -57.45231 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 4c44a5af-ad6f-30b5-9615-62ce45d65a83 | -17.10819 | -57.45621 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 195b0431-8621-3c03-813c-818bfb9593ef | -17.10773 | -57.43591 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 4a4466ce-f2cb-344c-bcde-825bbb7efe4b | -17.10753 | -57.45283 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 05185623-cbe8-3a76-bfb5-bec12406a467 | -17.10745 | -57.46011 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 136edcd2-f33f-341b-b502-803a5f7da241 | -17.10731 | -56.85469 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5424b9e7-67da-3136-a817-8041927c9eb4 | -17.107 | -57.4398 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 3d803b15-3f5d-3f98-8fce-55e73c0efaff | -17.10682 | -57.45673 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 453f5d80-c738-37c3-81f9-e1e34b6dacc1 | -17.10626 | -57.44369 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| f8fa28d6-60ee-3112-9d6f-7bf365dd871e | -17.10623 | -57.43639 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 5b06baa3-240d-3b0a-8fc3-32ac950199cc | -17.10611 | -57.46063 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 57e1e3c1-c10e-3b51-876f-a0b7e2fa90cd | -17.10552 | -57.4403 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| ffdcfc1f-531a-3afe-b6f6-b0a52f4e3876 | -17.10481 | -57.44419 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| 61a50b8e-c00b-3631-b608-0b785a7e197c | -17.10479 | -57.45147 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 9d74beff-04e6-3cc3-b555-4a5a1ed06858 | -17.10405 | -57.45537 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ff24c28d-3625-35bc-8bca-7e2b3aab6828 | -17.10373 | -56.85526 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 78b5d075-dda9-3a7f-bb38-3600fce7c951 | -17.1036 | -57.43507 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 7f4618ae-f37f-3d23-a766-217361590d64 | -17.10339 | -57.45198 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d2deb245-6816-31e7-9af7-024e23acd299 | -17.10332 | -56.85389 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c5b97b80-abdd-3279-abb8-6371273672f3 | -17.10331 | -57.45927 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 596a06b5-ba50-3b86-b5ef-314ffe329a77 | -17.10286 | -57.43896 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 3b6dd654-f22c-3a36-bcad-225badfdc7d3 | -17.10273 | -56.86066 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| bb7ea7bc-a609-3544-a712-b0781f0ec131 | -17.10268 | -57.45589 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d80cfd07-1e35-34c5-9eab-53a009c97226 | -17.10234 | -56.85929 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 4c4808d2-9c9e-3906-8142-71b67e7c9aba | -17.10212 | -57.44286 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 3648c43c-a06c-386b-acc1-e02a1c70e3ab | -17.10209 | -57.43555 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| c323540b-21d2-37d7-baa1-12be5f0ec592 | -17.10197 | -57.45979 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 94301af5-0a87-3b0a-9aef-13c6b07a3667 | -17.10138 | -57.43944 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| a6be17f6-4f1d-3b3f-a9bb-bce102ba2cce | -17.10067 | -57.44334 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 787650c9-3a54-36a4-81af-89d34bc5d587 | -17.10065 | -57.45063 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e101a64e-ec5f-3519-ae4f-66b9dccb67b5 | -17.09996 | -57.44725 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| d29fd1e6-cc9d-30ba-948e-c6d220ea9826 | -17.09991 | -57.45453 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 0b318a8d-94b6-3ae1-862e-7cf0eff25dc2 | -17.09985 | -57.33084 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 9ecd2694-768c-3b59-9312-23c0cf0bc444 | -17.09974 | -56.85447 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 57931bdc-414a-3b13-b059-e45daea8b432 | -17.09932 | -56.8531 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |


[Clique aqui para ver as próximas entradas](README134.md)
