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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff8d22f4-ba0b-3637-bade-367477439abd | -14.3385 | -57.5913 | 2024-10-09 04:40:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 73fc9206-f422-3984-aa58-afbbc48db774 | -14.28041 | -51.95055 | 2024-10-09 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 761c74c1-26ed-3930-b8b8-a28402471b62 | -14.10959 | -51.09339 | 2024-10-09 04:40:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5128424-7210-36f9-b2c7-739efd40985f | -14.10683 | -51.08928 | 2024-10-09 04:40:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f05f9df8-640d-315b-8e3e-a2d549bdf0b2 | -14.10073 | -51.08462 | 2024-10-09 04:40:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b47b4940-c1e3-3bde-b72c-d33e69dde899 | -14.09741 | -51.08407 | 2024-10-09 04:40:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 367ef950-a104-323d-8f49-ca48a7b2eff6 | -14.09685 | -51.08763 | 2024-10-09 04:40:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e02c86a3-1cab-3558-99cb-bd17126448c3 | -14.09629 | -51.09119 | 2024-10-09 04:40:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0760b8e-86e6-3f6a-a721-b8a0340dd7d1 | -14.09296 | -51.09064 | 2024-10-09 04:40:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdeaf2e6-560b-3b6b-b72f-5129bbe64e1e | -14.0924 | -51.0942 | 2024-10-09 04:40:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 827e04da-65a0-3703-8b4c-64899336e7f0 | -14.09184 | -51.09776 | 2024-10-09 04:40:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1939430-dd77-3df4-8092-e1741220c475 | -14.09016 | -51.10843 | 2024-10-09 04:40:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 90872e72-9e2e-385b-874c-b026ee69883c | -14.08959 | -51.11198 | 2024-10-09 04:40:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2b9f23e-c088-3029-9928-e8011bd6beaf | -14.08795 | -51.10077 | 2024-10-09 04:40:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc4f3bf2-4ffa-36b7-b886-c488940dc054 | -14.08739 | -51.10432 | 2024-10-09 04:40:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf501a8a-20dd-3e2d-97b6-80e1ea31e430 | -13.91024 | -60.22889 | 2024-10-09 04:40:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88fbd34b-f441-3121-b084-93c357f93701 | -13.90497 | -60.22789 | 2024-10-09 04:40:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fda00845-5a1e-326b-9d04-768b309ecf6c | -13.49903 | -56.65306 | 2024-10-09 04:40:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d0f526d-9940-352a-ab3d-48214dd8b673 | -13.42272 | -61.92077 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 142ab8af-81f1-3d2e-bc61-f0aeda9823e8 | -13.42184 | -61.92517 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| acec2091-7571-3ff6-ad96-266501e7007f | -13.42065 | -61.91798 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c704a2e0-2484-3f39-aaee-3add95f6fa4a | -13.41974 | -61.92235 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e315693-a111-3809-9ca9-cda6d5b92a93 | -13.41883 | -61.92674 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2ae941f-034a-3a74-be5f-442186654516 | -13.41683 | -61.91948 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 892bb76a-266f-3bdb-9390-de1124b06799 | -13.41295 | -61.92545 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5766d24a-cc5c-36a3-b880-7e0b41e2464e | -13.41007 | -61.92255 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ad391a12-6e9d-3d32-b863-f2b076d58289 | -13.40919 | -61.92693 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 993f66a2-301d-3e98-8401-28b5b94cc2c0 | -13.40706 | -61.92417 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5ac5a6e2-b716-3e5a-8588-2487f0b785f2 | -13.40615 | -61.92854 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6b0b3fea-a424-3da9-be9c-db77af659752 | -13.40524 | -61.93295 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a3d54df2-86b4-31eb-9233-db1ed3e16780 | -13.40418 | -61.92126 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 000c6e18-ea44-36f8-bbb4-54f6a404b509 | -13.4033 | -61.92564 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8089a8e4-c4da-38d7-ade7-f709e54a2058 | -13.40242 | -61.93002 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 07cf3b3f-311e-3a00-96ef-676ab4315a9f | -13.40154 | -61.93444 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b365383e-6c52-3333-a404-0d0fdcdac6ed | -13.40117 | -61.9229 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 996a8a33-4639-3dfd-9a97-ee463df9e70a | -13.40026 | -61.92728 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 20f7bba9-8210-3817-929c-a8601d7d9822 | -13.39934 | -61.93166 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 98a6f7c7-aba2-3ed2-ab1a-f52fbab6ebf1 | -13.39752 | -61.94043 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2909e9a7-cb59-31ed-8143-9d0500bcdda2 | -13.39741 | -61.92435 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 22703b37-e0a8-349b-923a-5eda02c6cca2 | -13.39662 | -61.94477 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c33485a5-059c-3b34-97a5-88e220fb9bd7 | -13.39653 | -61.92875 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| dfc89bb1-9698-3ed9-880e-e3899fea111f | -13.39565 | -61.93314 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 47f28f8f-fb02-3578-be9a-b382c2f4dcfd | -13.39476 | -61.93753 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ac6b3a0-1a8a-3e1f-a683-fd75eb9eef93 | -13.39388 | -61.9419 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c28705c-6904-355c-83a6-10c25015ba22 | -13.39152 | -61.92306 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 41322370-0252-3e67-be57-c276dcfba809 | -13.39064 | -61.92745 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5b90af3c-0583-3dee-b978-d71a751bc5ad | -13.38975 | -61.93185 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8b35df4b-ddb9-3446-a056-fe3ead47dabb | -13.38768 | -61.97273 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 52f47950-7220-377c-ac7e-0049cd01b4a0 | -13.38475 | -61.92613 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2b01963-816a-3cef-97b5-c3455cadad43 | -13.38387 | -61.93052 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35b51278-5ded-3c4c-a197-327ab32b1151 | -13.38298 | -61.93489 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cfdf21e-4904-38ed-bb86-98a62c957720 | -13.38177 | -61.97145 | 2024-10-09 04:40:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b22c272a-65f6-3c2d-9957-c9ef809e42aa | -13.31864 | -53.72747 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dee7ec3d-e9fd-31c9-a959-a75b19356888 | -13.31723 | -53.72575 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b5dc0c9-3deb-38af-b6e2-d2252f368d8e | -13.31653 | -53.72983 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8cbe47e-8dae-3427-8ea1-ff1780b75a92 | -13.31577 | -53.72272 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ee4e717-0217-3330-afb3-e8ce496e51f3 | -13.31509 | -53.72681 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64f0ddeb-73a6-3377-9dc8-499de62b5f96 | -13.31441 | -53.73091 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48d1d4d0-6f4c-346a-9561-071a79a091af | -13.31437 | -53.72101 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87cd6169-30a4-3dfe-81f7-d6f7adb7c77f | -13.31367 | -53.72509 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b9530be-e6fa-3035-9416-2e57e263ec85 | -13.31297 | -53.72918 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac462255-6cd5-3094-9f3d-192e14e24063 | -13.31221 | -53.72206 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23d6f42b-13d1-3b0d-9c69-1779853a7815 | -13.31153 | -53.72615 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c704936d-7abc-3bc7-aaf7-290ceca79135 | -13.31085 | -53.73026 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e59efaf6-d6c0-3d08-abdc-c10cdbe8fcb8 | -13.31017 | -53.73438 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 992e0871-46e8-3c8a-bb14-078a19d7a42c | -13.30934 | -53.71733 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14c13b12-e55f-32ff-9dae-094033450f0c | -13.30866 | -53.7214 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 214c1527-1298-3a9c-b9b0-8bba65a01589 | -13.30798 | -53.72549 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0718e21b-052f-3b97-96af-091a45b3e65b | -13.3073 | -53.7296 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5cf5bcb-f510-368e-ba15-4cb00e1f2338 | -13.30661 | -53.73372 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c06f4367-9cae-3280-aba3-2f21dc7802f8 | -13.30592 | -53.73785 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb109a50-2b0e-347d-950f-8cf914c0816d | -13.30579 | -53.71667 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e976610d-d383-30fc-a8bf-3299690c6ed8 | -13.30511 | -53.72075 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abac677d-e4c4-3c85-aa22-7e681c0c6c87 | -13.30442 | -53.72484 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d14b7c15-a1b6-333d-b853-8f0f0874dbd3 | -13.30374 | -53.72894 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d86db9b6-dca3-3857-8a92-c1c5096dd88b | -13.30305 | -53.73306 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca044626-c25e-3889-9cba-554cee7739ff | -13.30237 | -53.73719 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d5de350-a711-323d-8d6b-2580b917f888 | -13.30019 | -53.72829 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25212651-b949-3663-98be-4803412c12b8 | -13.2995 | -53.73241 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67680600-07f3-3d22-a3ed-a8c17972c6a4 | -13.29881 | -53.73653 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9131811f-bae4-37e1-98a6-57014bfb0174 | -13.29812 | -53.74065 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c9f83da-b80a-3ba7-8988-b25700ee7d33 | -13.29526 | -53.73587 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c7e04c1-8b16-3336-ba5c-623f715a4692 | -13.29457 | -53.73999 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4111f0f-8e8e-3973-8623-ddb2f7d9a3cf | -13.2917 | -53.73522 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e850446b-2cd7-304d-a232-f5e9d5eefa25 | -13.29142 | -53.69308 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7fdb7e9e-9d07-3830-afd7-80e578827bd7 | -13.29101 | -53.73934 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee49bffd-dff8-381d-9db3-224cb3eaf6df | -13.28814 | -53.73458 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 01d00b52-ddd5-34bf-8d38-005b07aa19d7 | -13.28745 | -53.73869 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e1b2dc7b-8c1b-3861-be7f-3183b2152824 | -13.28719 | -53.69651 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 80cfe0a6-418c-33a7-992a-01b3b3cd6fba | -13.28363 | -53.6959 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| fdbc80b9-cf90-3311-a74f-0b3652002298 | -13.28295 | -53.69997 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2f375d52-3bb8-3fca-89b8-d0ca25f74aa2 | -13.28008 | -53.69529 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 6393430f-959f-36d2-861d-5575c98a16b4 | -13.27939 | -53.69936 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 64808abe-ba8c-3584-8224-f0bb92432ab1 | -13.27653 | -53.69466 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 004bc295-0ac2-3483-b043-9bcc0f4033ac | -13.27584 | -53.69873 | 2024-10-09 04:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| af02d7b4-895d-3aed-ad26-392d03f5f1d4 | -13.19899 | -47.99521 | 2024-10-09 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3f74f65-9b76-3dd8-9b98-f2fb706fd86b | -13.19127 | -47.99813 | 2024-10-09 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6643c9d6-4b3c-34ab-915f-3c97c3715434 | -13.18771 | -47.99755 | 2024-10-09 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c14af565-837e-3444-8d7c-da2126ccbe49 | -13.18713 | -48.00156 | 2024-10-09 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9486860-55e9-3552-bce2-d287e5c1950f | -13.1869 | -51.17552 | 2024-10-09 04:40:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README143.md)
