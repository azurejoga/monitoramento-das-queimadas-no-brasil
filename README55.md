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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 198aa74e-84ae-34c9-b5de-acfbf50fe1aa | -7.93095 | -63.04582 | 2025-08-22 05:38:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98ace41b-c1b7-3311-b395-3c7d912b08b6 | -8.87559 | -62.41583 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0c6c334-0aff-336f-9c9a-cdb395970e1f | -9.95037 | -60.17752 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a35363eb-ec89-3aa9-8692-7c79ed870885 | -7.45589 | -59.94474 | 2025-08-22 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18139e0d-f888-3b05-8ad1-c037d1797dee | -9.20925 | -59.46796 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 58d7cab6-b503-3244-8f58-8427abadbce9 | -8.86763 | -62.39947 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58bc0429-31e2-3d22-9c7b-dba32cb141dd | -9.94583 | -60.18175 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dffe3a0-8a03-3d4f-86a5-67ca23cd3aa8 | -9.17548 | -59.6965 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8a95820-83f3-32f8-b4b4-6d8a91e12b25 | -3.55374 | -62.07866 | 2025-08-22 05:38:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11131a6a-4db2-31ae-acbc-395f70a4f585 | -9.66451 | -67.24604 | 2025-08-22 05:38:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d27afd0-0477-304d-9942-de0fbb56b0fa | -9.18534 | -59.6299 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d226dae2-548c-3a1a-ba70-7936c39b2a4f | -8.87389 | -62.40421 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf5a0d9a-af0d-38cb-9b7d-3921fc61e5d0 | -6.62572 | -58.54397 | 2025-08-22 05:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 945a658d-f271-35e3-b26b-03e9103f4f5c | -8.89526 | -72.70743 | 2025-08-22 05:38:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d112893-c2df-3f9d-9fa7-9c43280738d4 | -8.71335 | -69.46088 | 2025-08-22 05:38:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f7100af-44a8-328c-b98c-809522e3b652 | -4.10129 | -60.66381 | 2025-08-22 05:38:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 974d5378-002d-3d41-b0b0-560223625371 | -5.80984 | -59.21568 | 2025-08-22 05:38:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce6fc024-fa1e-310a-ab33-09bb3a7e71c2 | -5.88204 | -57.75624 | 2025-08-22 05:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 276912e5-9f45-35a8-9063-ef401eddeea5 | -9.19176 | -59.63786 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 467acf16-fac0-351a-8c27-4ddc788f4155 | -9.15438 | -59.59451 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4d255e5b-74f4-32f4-9120-29905ab0cd3d | -8.90895 | -69.43315 | 2025-08-22 05:38:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b10effb5-10c1-359f-9fb2-289087fed085 | -4.55817 | -55.96587 | 2025-08-22 05:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ce16e55-f5f8-342a-8044-f539750e8fcd | -7.75443 | -70.15851 | 2025-08-22 05:38:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e632a403-3bb8-34d8-99ed-c68ae5486412 | -7.55713 | -63.86141 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eaa4fdde-f7bc-3de2-a3c3-f5d6df808c84 | -9.75133 | -62.77418 | 2025-08-22 05:38:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eb1080b6-290e-3439-a70f-865d3f60509c | -8.89344 | -72.70704 | 2025-08-22 05:38:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 394138f6-bfc1-343e-ab5f-27dcd74763f3 | -6.8768 | -59.82487 | 2025-08-22 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ecb7fa8-d55e-3c71-b1b7-4e44225604ee | -5.87185 | -53.63376 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd935f2d-2848-3504-b94d-5809d0d782dc | -8.86193 | -62.41372 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9ca55df-0383-3f07-aa19-3108d3db34d3 | -9.18856 | -59.63216 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 63c90411-f287-3f5e-92c2-075387430792 | -5.87798 | -53.63085 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c3facc9a-5274-35f8-bee7-eb8fb393a91a | -4.83508 | -55.76551 | 2025-08-22 05:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3530f74-bfcd-3311-a173-e0f9998764a8 | -8.89061 | -62.42882 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80542d9d-3f00-369a-98d9-1d38c2f2ef42 | -7.93819 | -63.04333 | 2025-08-22 05:38:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79b9a400-f33e-3aba-a0ad-8c087a10001c | -5.88513 | -53.62054 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea46d20c-e6eb-3c5b-a9a1-ccc5a1c1cbd9 | -9.21031 | -59.44872 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b99de374-39e4-3081-b367-a376d0f081e2 | -9.50585 | -60.5078 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d280bd11-2967-323f-a387-8b9373baaefd | -9.21653 | -60.79053 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| aa3d7313-5739-37ee-a86d-db73f727faca | -7.10822 | -62.96846 | 2025-08-22 05:38:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa244a3c-6617-3909-9b59-9c57fe528957 | -9.51935 | -60.54659 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f431ac33-2d77-3b44-9bf3-a22e0d521052 | -7.29945 | -59.62284 | 2025-08-22 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f7267f2-bd97-3441-9dd7-eda3342b6b84 | -4.83435 | -55.77058 | 2025-08-22 05:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8c0e87d-3cd6-3e5a-988b-56b5847e69a0 | -9.21228 | -59.44741 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba6b74d5-9da7-3b4e-91cd-58a1634793ea | -5.80599 | -59.21512 | 2025-08-22 05:38:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db236a14-53cc-3ffc-b987-00a43d7f9dd8 | -9.18321 | -59.64162 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ffbc0b86-b4e4-3d8f-b040-a7e3e0c6a4ba | -6.27269 | -53.70739 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c44ef89d-9039-3d64-9f7d-33eb00a01d15 | -8.89117 | -62.42511 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ed63d8b-5220-36db-bec8-edd9f7013be2 | -4.89081 | -55.98577 | 2025-08-22 05:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ee3b2d4-112c-3628-b013-1a873b9ca599 | -6.16098 | -53.77094 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c074375d-ca01-3c43-8f80-17f0dfbfec22 | -5.15522 | -62.52782 | 2025-08-22 05:38:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd698e97-c324-37b6-ba24-2e7a4be31c7c | -9.47414 | -57.82234 | 2025-08-22 05:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5fc6545-3719-3406-bb2c-8bcfd2e4f70b | -9.22311 | -59.75406 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16937315-8e01-37e3-b1a6-189a69eddc81 | -5.88109 | -53.62896 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8754e1df-b91d-3ebf-a74f-3a47187a3eb4 | -10.87533 | -50.84964 | 2025-08-22 05:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7de78f5b-c557-35c4-acac-61351a89df1b | -8.88755 | -62.40634 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c50c0ad2-a031-399c-96cd-a99327704f45 | -9.20528 | -59.46739 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c9c86fb-e21c-399a-a4ae-1e1a7341fe2d | -7.54604 | -63.84539 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42b7444c-1333-3abb-8c94-f2f0b422ac6f | -6.44316 | -53.38465 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5c019f2-e38f-3caa-bff5-fef983589a0f | -6.87372 | -59.81977 | 2025-08-22 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b8e68d0-0dd9-3c18-8d3d-d830a575670c | -4.60786 | -55.75178 | 2025-08-22 05:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0317874f-55a1-32d7-aee5-545cc4be9320 | -9.21103 | -59.44357 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ededf98-3ead-34ab-8e5d-c8758f5298d0 | -11.8975 | -55.89838 | 2025-08-22 05:38:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d48c2c2-fe92-323e-8fe0-11bcda2264ba | -8.88412 | -62.42852 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95fb864b-6a41-33fb-a12b-912d24d5cbf2 | -6.2732 | -53.7038 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d3c34fe-07a1-37c3-964b-397b8a8de482 | -7.9315 | -63.04229 | 2025-08-22 05:38:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94886655-572d-3089-b684-56d3c5621b9c | -6.8917 | -52.86377 | 2025-08-22 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 78444ffc-a89b-3ce0-906b-2af846809d25 | -8.88714 | -62.40556 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2592d929-5b00-30e3-91a4-9ceaa2f2e67e | -10.85725 | -50.81929 | 2025-08-22 05:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| dc081989-3409-30e8-9243-601dac0fb5f9 | -5.88271 | -53.61781 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 385a96da-579b-3dee-9bc3-57dacdce9cf0 | -9.21001 | -59.46285 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d409d471-9394-38c5-82cc-168eb476f248 | -5.87336 | -53.6228 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdc9bf7a-6754-3876-ae29-351df7031af1 | -8.69048 | -63.66926 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df1536eb-e80c-3dd6-b51b-7f5e8fe34f11 | -9.51656 | -68.46963 | 2025-08-22 05:38:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d152df3-f9f5-352a-b3ae-c31706ed1135 | -6.44699 | -53.39118 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a35be4d9-7c1b-399d-84f2-31059aebff06 | -9.19034 | -60.76448 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41ffc7f8-175f-3464-8ee2-4d8adc9cd5e5 | -9.18265 | -59.59367 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 75f0b521-6712-3d40-97d4-59876095430c | -8.60647 | -62.62223 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a325a30-a56b-3ee7-8338-656b627563ad | -8.87786 | -62.42376 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2933e20a-b7b8-398c-96d7-09d7a4d42e23 | -6.57535 | -59.87771 | 2025-08-22 05:38:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b5fa3d9-960e-3b8a-8f23-682bbd124ffd | -5.44511 | -60.1819 | 2025-08-22 05:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6c69834-89c3-3cfe-b4b6-45440d2a4133 | -8.42322 | -70.70752 | 2025-08-22 05:38:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eebec05c-3274-3086-8625-eccc54d3abaf | -8.60703 | -62.6186 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b88588a-f2de-3d16-b33b-fa8f3a37637b | -7.51059 | -63.83265 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 101d2901-3576-3715-a88b-0879d1e7e723 | -7.5891 | -63.44199 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69b7bcfb-2cdb-35ed-b643-dc46078d5b41 | -9.20743 | -59.4693 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e28074f2-55b0-32f4-9cad-efe48abf2352 | -8.89469 | -72.71049 | 2025-08-22 05:38:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| acb6ec31-9abe-3ae7-9543-e9cbb2c1aac3 | -8.55083 | -66.95435 | 2025-08-22 05:38:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a354570a-8cfa-32ce-a6ce-36592bffa205 | -7.30641 | -59.62874 | 2025-08-22 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3bbc5918-909c-392e-843f-9e7e5bfb0b16 | -9.94967 | -60.18231 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c21ab16b-f543-37d6-b6f0-abe9658a92ff | -6.44814 | -53.38312 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e9bf2ef-d134-3bed-8e27-f68bc5416db2 | -9.50455 | -60.51683 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59809165-3497-3164-a652-ce7dc97137fd | -9.23767 | -61.02363 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 344433d2-39fb-37cc-814d-5f91c2878561 | -9.50764 | -60.52189 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ddac641-a708-3dc3-819f-b3b7c4c795b6 | -8.54793 | -66.94967 | 2025-08-22 05:38:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7f3545b-58e7-3c3b-9146-27f6851cf5b0 | -5.44211 | -60.17716 | 2025-08-22 05:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81c52391-b21c-3059-bcc3-6837a12d8099 | -5.44488 | -60.17924 | 2025-08-22 05:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23a4a0f4-987a-377b-ade7-f4b6ec0ae8be | -8.62228 | -62.60978 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 849f8925-b2c4-39d0-a26a-c2d4b18cfd05 | -9.18785 | -59.6372 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 499c7f6a-d541-37fb-87f8-6ec1b3bd91a5 | -9.02157 | -63.90459 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36ed00bb-2fec-373c-a8ff-84adbcebdf88 | -7.9276 | -63.0453 | 2025-08-22 05:38:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README56.md)
