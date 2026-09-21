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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c3601fc-bb5d-3909-a660-f67278f6ca36 | -4.3535 | -55.660999 | 2026-09-21 01:40:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f012d6a4-ca0c-3284-84a4-6f56f3dcf918 | -9.5653 | -66.038399 | 2026-09-21 01:40:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4ebd365e-9549-3856-8394-49965b266703 | -6.7407 | -59.4305 | 2026-09-21 01:40:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1bdcb178-d983-376f-96d9-d63f732208a4 | -7.5655 | -57.681499 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 705a87f7-bf07-30f9-9937-e565f1110814 | -3.05 | -61.2691 | 2026-09-21 01:40:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 695071f8-65c8-3ef9-be34-837bf30ff4b2 | -9.5486 | -66.009102 | 2026-09-21 01:40:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 23ffe852-b5fc-3766-853c-3e22d12a0319 | -7.5542 | -61.334702 | 2026-09-21 01:40:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7e913648-cde6-3d05-b7cd-a0c80763ed63 | -6.6526 | -59.9687 | 2026-09-21 01:40:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 62135181-7ec1-37b9-af6c-4a477ba855d3 | -7.5722 | -57.666599 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9a1a643-55d5-3c4e-a9c4-77e6be736427 | -6.1328 | -59.952801 | 2026-09-21 01:40:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 22dda437-1c04-3775-ac0c-958589803529 | -3.3918 | -59.524101 | 2026-09-21 01:40:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 68c33d80-6953-3c84-926e-aa5b968d5a68 | -3.3354 | -59.808201 | 2026-09-21 01:40:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3c3e22cb-31de-3c90-89c5-06a6cca68a64 | -3.4216 | -59.258701 | 2026-09-21 01:40:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5ec9046d-db13-3d63-8ba5-4f1b3e1d9d03 | -6.9882 | -61.342899 | 2026-09-21 01:40:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 839dd2f8-15be-333f-af98-e522b4a02abc | -10.1019 | -64.335197 | 2026-09-21 01:40:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 274a1e36-adcf-3ea6-8942-d9bf716738e0 | -7.5849 | -57.6768 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d9db0ef-1ebb-3c77-bbbd-1aa2896c87f6 | -11.0863 | -51.054798 | 2026-09-21 01:40:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 97d2391f-739e-3894-820b-50a253c70f59 | -6.736 | -59.410599 | 2026-09-21 01:40:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0cd3aab0-7c13-39ce-920e-314eafc65295 | -9.5584 | -66.007004 | 2026-09-21 01:40:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aca88316-870c-3dd8-8485-f1327dba6cd8 | -3.6949 | -60.589802 | 2026-09-21 01:40:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 93dd5a33-1b19-3d5f-935f-b4de4b773f22 | -11.9119 | -63.268501 | 2026-09-21 01:40:00 | METOP-C | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d8708d47-4446-3743-9332-b62a9a50c798 | -11.9913 | -58.0746 | 2026-09-21 01:40:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f4e2c25a-fae8-31c7-9769-bd7f7ac56610 | -4.3486 | -55.682598 | 2026-09-21 01:40:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| faf9293a-2b59-362e-8d5e-3d656409c3d0 | -3.4341 | -59.267799 | 2026-09-21 01:40:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5368dc96-2273-3dcb-ac8b-375eb8c50063 | -6.3746 | -60.014599 | 2026-09-21 01:40:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a59c8287-e95d-32a3-8204-00169d3bf9a8 | -10.7616 | -50.807999 | 2026-09-21 01:40:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f42ab033-de10-39df-a7e4-3448dd8cf950 | -6.3115 | -60.0098 | 2026-09-21 01:40:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 72542808-05aa-38b6-95f4-4bd9f1353326 | -10.7908 | -50.7649 | 2026-09-21 01:40:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 066d7c01-e264-3a39-be58-722fbb6164c0 | -5.8405 | -53.5294 | 2026-09-21 01:40:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 630e745e-88e2-37c2-9e95-89a619edf849 | -3.0521 | -61.277802 | 2026-09-21 01:40:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 90110256-079f-304b-b950-6d456aab6647 | -3.0757 | -61.290699 | 2026-09-21 01:40:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eacef395-31e0-3e9f-90b1-6cdb0d830a97 | -11.3369 | -51.3685 | 2026-09-21 01:40:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3314df71-c246-33cb-978d-645833defa04 | -6.2019 | -57.797401 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76078688-2b22-3fb5-b463-4704f55dfa1a | -10.5408 | -54.498798 | 2026-09-21 01:40:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2ade1bb9-e205-32db-956d-f85fbf04cad7 | -6.1859 | -57.773998 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 755ff420-544d-3868-abbe-b18d7b0c46d6 | -7.5916 | -57.6618 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 634bad2c-4e88-3133-a9ac-7c53e590a4bd | -5.0164 | -56.104599 | 2026-09-21 01:40:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8696314-36b1-34ea-ad9b-e423544a4782 | -3.0696 | -61.264599 | 2026-09-21 01:40:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 378cfce7-0050-306b-8332-e9de99652240 | -10.4606 | -61.309502 | 2026-09-21 01:40:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 490c68ac-b6a0-38c7-ad2d-b9ef2453df04 | -7.5813 | -57.703999 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f3ef2d8-c679-35cd-9603-f44bb1c4c124 | -9.5488 | -65.684898 | 2026-09-21 01:40:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aa2241ea-2726-3a74-84cf-4b6a0c63ee69 | -7.5783 | -57.691601 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e73f791-ab73-3885-bd22-f2ddb3761faf | -7.5819 | -57.6642 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d11705ae-50bd-322c-9abb-cf38babf1e1e | -11.3465 | -51.365799 | 2026-09-21 01:40:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 58cfb2a2-86d9-3256-a723-5501c02c16e0 | -3.4956 | -59.6143 | 2026-09-21 01:40:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da1ca1ff-6e09-38f3-8c7b-eaba1d6147df | -8.7902 | -60.794998 | 2026-09-21 01:40:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 82821e46-0ee8-3668-bb75-98953c5a5df4 | -11.0378 | -54.1474 | 2026-09-21 01:40:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5d706583-010c-3241-a068-eac6225e272e | -6.4385 | -59.9799 | 2026-09-21 01:40:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c00fbf73-fc02-3046-b0bb-01493780cd74 | -3.4854 | -59.571201 | 2026-09-21 01:40:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 17e8f3c9-5a7a-3d91-813a-390652f740d6 | -3.8226 | -59.3428 | 2026-09-21 01:40:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4f8c5f88-9f53-3257-b773-9f80861cb07d | -7.2385 | -55.613098 | 2026-09-21 01:40:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bbad42c-f51e-382c-95e6-983bb4e8e4e7 | -9.5688 | -66.054199 | 2026-09-21 01:40:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 88ff9471-c865-37e5-97f2-2928e79ba3a2 | -14.658 | -54.460201 | 2026-09-21 01:40:00 | METOP-C | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 879bf6a7-fa09-37f6-991a-6dd9459fe953 | -4.3392 | -55.644001 | 2026-09-21 01:40:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 823f1202-fe6f-3945-9d36-f1ca3df6299c | -7.588 | -57.689201 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 525e3c0e-98e8-3ca4-8aa2-55ac25716a59 | -6.0958 | -57.615299 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e88a69b-e821-3f1c-8631-2126c8e8dc76 | -5.834 | -53.5037 | 2026-09-21 01:40:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6448a56-4728-3701-aa0e-ce479ca3ff0d | -5.2038 | -56.1147 | 2026-09-21 01:40:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 349fe5e8-6855-3b40-bdfe-048a389a1f56 | -10.4624 | -61.316898 | 2026-09-21 01:40:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd5a6c66-c695-3a92-bcd4-cd01650c9631 | -6.1988 | -57.7845 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad9240c4-b3bc-3112-99dd-4fcd72e134b2 | -6.4558 | -59.9659 | 2026-09-21 01:40:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8e38178a-e536-3fa7-b611-bdef15ea5036 | -7.5947 | -57.6744 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5537c92f-3849-32e3-a91a-44fe695e2096 | -10.5429 | -57.443699 | 2026-09-21 01:40:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad0c4532-224b-39d7-b0b2-fccebd42383d | -8.9053 | -62.345402 | 2026-09-21 01:40:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cffeefce-9e37-3de2-bba0-508a372cda5d | -11.9888 | -58.0644 | 2026-09-21 01:40:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 09c77899-babc-3d69-9536-41148895fdcd | -3.82 | -59.331699 | 2026-09-21 01:40:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 63f6ee84-f83a-373e-9434-b1144f884d7f | -12.3172 | -50.7033 | 2026-09-21 01:40:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 60a8c9c4-c40f-35cd-9bea-2db2a9ec55bc | -3.0717 | -61.2733 | 2026-09-21 01:40:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ebafd712-68b7-3c29-bceb-b901ef974cd4 | -6.7578 | -59.115002 | 2026-09-21 01:40:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4de4f10c-e439-33ad-b467-71e7cecbdfc9 | -7.5505 | -61.319099 | 2026-09-21 01:40:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bb5cce25-3319-30e7-9640-8b04dff2f52c | -5.2135 | -56.112301 | 2026-09-21 01:40:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 890e498e-ab69-301a-b97c-f31a0e3be277 | -10.8004 | -50.762199 | 2026-09-21 01:40:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 784dd259-b116-3745-accd-b80e61b46082 | -3.6008 | -59.059502 | 2026-09-21 01:40:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dfd9cf3d-cb29-331e-be58-29b1d61d15b6 | -6.158 | -57.9561 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8b2df9b-c760-3c3c-95e6-694491be836e | -11.0332 | -54.168999 | 2026-09-21 01:40:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 494fc24b-9fd4-3dd8-bdeb-a08deb6615cc | -3.048 | -61.260399 | 2026-09-21 01:40:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5b6d7708-0142-3b15-8604-9aa7bb1d2012 | -6.3137 | -60.0191 | 2026-09-21 01:40:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd649a0d-c9df-320b-916c-9998e98434c1 | -6.1956 | -57.771599 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25fd6428-b742-31a4-83d6-f079f3be8562 | -8.169 | -54.774101 | 2026-09-21 01:40:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4443c36-002a-348f-9712-a3391921fdf4 | -6.7382 | -55.094799 | 2026-09-21 01:40:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37e27641-6749-33cb-8170-699ff10945ec | -3.3478 | -59.8605 | 2026-09-21 01:40:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4b9f9f6c-0c6d-3fd2-8e5b-d516f2aa86ef | -2.8715 | -57.809601 | 2026-09-21 01:40:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f8f836c3-8eb1-3b07-813b-35bdea772cd0 | -3.3319 | -59.445202 | 2026-09-21 01:40:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 88d7f03b-358b-3117-9ac6-bf5567daf481 | -6.4505 | -59.9869 | 2026-09-21 01:40:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ca5f282-01ab-3fa3-a15f-5266c6f985f4 | -6.7478 | -59.073299 | 2026-09-21 01:40:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3f7930db-26bf-368c-b8c9-08f7add91e81 | -6.1603 | -57.7113 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4514a2e-9570-3db1-afd6-dac9a6577201 | -9.5505 | -65.692497 | 2026-09-21 01:40:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e80902a9-b972-3345-944a-89d36a6a274f | -9.5538 | -66.0327 | 2026-09-21 01:40:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| df949a54-0a8c-3fb4-8516-993d2e75839e | -3.6883 | -60.561699 | 2026-09-21 01:40:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c25030ef-e167-3027-b830-43c92a634294 | -3.4243 | -59.2701 | 2026-09-21 01:40:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 294cc086-631d-34e6-bc1f-85f9097e89c9 | -6.7711 | -55.636299 | 2026-09-21 01:40:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d8352c3-ebaa-3c83-9d51-1a9f0526998d | -5.847 | -53.554901 | 2026-09-21 01:40:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f5fb7c4-03ab-3660-b8ec-fade97d2e4eb | -3.0619 | -61.275501 | 2026-09-21 01:40:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 86e43b6e-2123-3de9-bff9-748a350482c4 | -9.1434 | -64.469299 | 2026-09-21 01:40:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e5a8f5de-9ded-32b5-a551-43a62805f0ac | -5.7681 | -57.580799 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90137e1f-0651-3c14-82a7-cdecf872c2c5 | -10.5215 | -54.503899 | 2026-09-21 01:40:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ba17365d-339b-31be-ae59-d344a203fabd | -6.4602 | -59.9846 | 2026-09-21 01:40:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 91a78163-77a9-302f-b410-b9de635001e1 | -9.5503 | -66.016899 | 2026-09-21 01:40:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| be27625e-2d4b-37d7-a3e2-e793d7e6094d | -11.0453 | -54.892502 | 2026-09-21 01:40:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e86bb90d-d7ac-3757-b7d0-19761a9f3052 | -20.878 | -57.686901 | 2026-09-21 01:40:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README15.md)
