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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7b08ad3-888b-3dd8-a06d-b5743b14da6e | -8.18796 | -54.77371 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7923402c-45d1-3d53-921f-718771e718b8 | -5.81964 | -53.52323 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9125c2df-f281-310c-be0f-37b16a44d19b | -6.75825 | -59.1174 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47d8a97d-a2d2-3658-9b05-b67fb8ca860d | -10.42625 | -50.26184 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9053198-6511-3309-9768-73486cb3baca | -9.03363 | -61.65115 | 2026-09-21 05:42:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad63d872-e6fe-37f9-b742-8caabb236b7e | -6.3297 | -59.95153 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b236380-a9e9-36fe-b1fb-004db6bebd27 | -6.74075 | -55.09615 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 197ce869-ea64-3a0f-9ca9-6df2b90ebbf7 | -10.37788 | -48.92101 | 2026-09-21 05:42:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8fc43a19-7a85-31af-907c-33b41de606ef | -7.32521 | -55.20403 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 92e3a326-74a6-3710-a3d8-595473901ef9 | -8.01318 | -71.14079 | 2026-09-21 05:42:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7091d49-afd6-3193-b7cb-4b33392ecfc7 | -9.6711 | -64.59327 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e8f873e-662b-34b9-98b0-e89a72d7cd0e | -8.08391 | -55.33942 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8046c7a-3b7f-33be-9e69-f1f51aa20d0a | -7.33136 | -55.61187 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b9be3f31-b008-31af-aab8-914445c8beac | -6.13457 | -59.94189 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6636025f-3c9b-3555-bbfd-f523b3540d0c | -6.77915 | -58.60879 | 2026-09-21 05:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 154a96ea-f331-3344-9407-41f929872161 | -8.8339 | -50.48353 | 2026-09-21 05:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cae4ee5-df2d-3c7b-b63f-12498e691b8b | -11.02604 | -54.1466 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97da7b71-fe89-3098-924e-89702fab894a | -6.41189 | -56.10012 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f97a5f1f-40f0-36b4-a7d5-8485f2c8d3f9 | -8.60632 | -54.61361 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7aa1bc0f-1f59-31d6-a85d-a7df78cf8080 | -6.309 | -57.74339 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e54763b2-5034-3e0c-bb21-9f0ca9f1eba5 | -11.02531 | -54.143 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dc631d3-cce4-3e1c-b141-361e97e59f69 | -6.20707 | -53.56636 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48c160bb-4988-3074-8ef4-977b4e1196c9 | -6.34793 | -57.8841 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96b42791-9993-3323-b437-1857bf339fdd | -6.74248 | -55.09814 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e75e491-77a0-3264-a089-a3026a493b1a | -8.83323 | -50.48902 | 2026-09-21 05:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe62d2de-9079-3d3c-ab0b-0572bbee2935 | -7.80943 | -61.80472 | 2026-09-21 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81360062-9875-30cf-8a24-c62c524aaf94 | -10.46027 | -51.33036 | 2026-09-21 05:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 062e2b5d-d8b7-3b89-886d-4ea80caeadea | -9.74827 | -65.05425 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e296b6bb-b27d-3502-a333-bee37ebc5252 | -10.4597 | -51.33504 | 2026-09-21 05:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63bcbaa2-7991-322a-b1fb-adb2bb062e6c | -5.80937 | -57.74199 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96f23b75-e657-338d-978c-11e8624cc070 | -11.80606 | -49.80841 | 2026-09-21 05:42:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 43cdf77b-3a61-3d15-838a-a8a9fe4f4768 | -7.58177 | -57.68826 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2d5a0107-f1f0-3747-bb99-65559723a116 | -6.03597 | -53.27765 | 2026-09-21 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24198f36-a22c-3cd5-9794-72363cba83f4 | -9.61708 | -65.36456 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1377c195-ea42-3d00-a09b-73b57190285c | -7.58574 | -57.68886 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3bf8e6e7-998c-3145-874d-00bf7f638286 | -11.35745 | -51.43186 | 2026-09-21 05:42:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f90a80b4-6e85-3d20-8901-55a8835e4ddc | -8.60483 | -54.61825 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9dfdb97-c933-351e-b83c-f5dc5b95a1b4 | -6.89141 | -55.65781 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62ed6cc7-cf3d-3eb0-9f77-6ec3bee497df | -6.11733 | -55.63208 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f8d1086-ec24-3dda-868e-9d4513eca053 | -9.56117 | -66.05469 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7c1b777-bb96-3dc7-968f-605b72688f10 | -5.81085 | -57.73244 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d04afa7-89e9-38cb-9ee4-d7c8673eee19 | -10.47943 | -50.29824 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65854a1f-1e1b-3934-ab8d-fbdb8f85056b | -6.15453 | -57.70864 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2aad0a68-84f3-3531-ae80-a460118b8105 | -8.1907 | -54.70096 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 16255aae-b228-36f7-b4d8-abe5a2604270 | -7.28188 | -61.11592 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79ff8e13-b3b2-36fb-b30b-d3cbdfcfecd3 | -9.56982 | -66.04746 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cdaa7abc-7257-372e-a219-a3d743cbf32e | -9.03316 | -60.36372 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f564f1eb-3243-3eb6-9392-875c9fcf73ad | -7.99211 | -70.90653 | 2026-09-21 05:42:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4005ec38-0f22-3088-8741-299dbe26eb23 | -10.40218 | -50.23451 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6bda5f9f-c7a6-3042-8c15-e34b6e89039a | -9.56772 | -66.06018 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8614137-acb0-3bee-82f5-4be907fd54c5 | -10.80159 | -50.84257 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8e3f47be-83df-3aa4-a70d-57331ef2084f | -10.45919 | -50.272 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9ffc5817-b8a3-3efd-9c1c-72b0ae40000d | -6.41961 | -55.01059 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0ab3ebf-3b33-3058-ad56-1508d0027f98 | -10.81 | -50.7703 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 34feaaad-f905-3659-9c77-9ce45d2680a3 | -11.03511 | -54.15092 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b6a02c0-189a-3089-a2d3-64afd4c5704a | -6.75165 | -59.11217 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd94e159-92cd-30c4-bea9-245b5a133692 | -6.45603 | -59.98113 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffafab87-7f1d-3ee2-b3ab-9849d61c9573 | -10.86896 | -54.08308 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da60f367-0ea8-3b52-b460-3f3446a00722 | -7.48762 | -64.70154 | 2026-09-21 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 787daeb2-01bd-34e3-8a1a-b6a75576a93b | -6.46009 | -59.97784 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8ba5638-01d8-3dfd-8851-ae8394caf9aa | -6.29448 | -59.92661 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1529d043-d391-39ef-9ee0-a521194010ce | -6.7459 | -59.07706 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31212373-7417-3d9e-a5b1-b4ac9ab1087f | -9.74763 | -65.05809 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4f3d223-0014-3d28-a20e-74ecdc98011b | -6.29964 | -59.93914 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07ff38a5-263c-303e-91a7-3375c3eda0e7 | -4.5063 | -59.56087 | 2026-09-21 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 702a3306-d24f-3059-a758-b250d7fdefa7 | -6.1415 | -59.94297 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25b27952-3d4f-3797-9844-7335828d97ca | -5.20693 | -56.1092 | 2026-09-21 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93e3cab5-6a72-3a41-8afc-299d994077f6 | -7.58005 | -57.67235 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0b4399ed-efc1-34ab-8ab7-1556a170cbb6 | -11.36379 | -51.43272 | 2026-09-21 05:42:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55f06f6b-e7ac-3b21-89d4-a9b1000c708e | -7.81666 | -61.80227 | 2026-09-21 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96d354db-0ea0-36e1-80e9-6029adafb947 | -6.43754 | -55.64034 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68745827-16c3-3594-8f62-5f466e328a72 | -11.01388 | -54.14816 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c334ed04-6a04-3ba3-986f-3dd48d041f70 | -10.91128 | -53.96606 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57c4a017-0bdc-3832-a191-c4a3811a4e5a | -9.97899 | -50.26305 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e47a224-c341-3adc-8917-0d8b3ea62bb4 | -9.56326 | -66.04202 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92a1597d-b011-30c5-a3e9-d08fdea4b3a6 | -6.07177 | -57.72899 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| de2a3690-3d61-30ad-bf07-d50143c831ce | -10.89927 | -53.97458 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32c790ff-20c8-3c49-872f-9d796be70a96 | -8.78499 | -68.84608 | 2026-09-21 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 46109542-57ef-3c27-9eef-d6a514f22d70 | -6.36502 | -58.28599 | 2026-09-21 05:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1708b3e6-c76f-3e3a-82ff-75cf95aa91d1 | -6.3127 | -60.01487 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 29cc194c-a0a8-3b2f-ae06-b682f11265fd | -5.98026 | -57.77667 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eee59a8b-aa8a-3ced-8c6e-73a8087107f4 | -9.30585 | -62.31469 | 2026-09-21 05:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60a02d14-7a9c-38f0-b864-ff8302ad5551 | -6.18053 | -57.74721 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ff0f2a6-2947-3ea2-9472-bb341b3dff77 | -10.88403 | -54.09196 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b8b240f-02aa-3963-a3b8-667834cdef07 | -9.29611 | -60.53234 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d39877d5-3e3e-3288-931d-761adda1b0ca | -5.84823 | -53.54291 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49f1df7d-cbb0-3a38-a38a-bcfc36642f4a | -10.88812 | -53.9765 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61ebbf1c-6958-3324-bcb2-7e0c6d2c3b85 | -11.03876 | -54.16472 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c7d5f31-fdf9-3a97-89a1-501f5c415f26 | -6.38111 | -60.02094 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05e283ce-42aa-3059-869f-48bf4e0ed910 | -5.21061 | -56.11374 | 2026-09-21 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e048aa3-db95-3dcf-881f-4d69d3d5a109 | -8.18828 | -54.73494 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ad564f1-c05f-3c89-9a12-3688173ef86b | -6.45778 | -59.9697 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d132b93a-c691-309a-bbc5-67566bfd335e | -10.6998 | -50.77029 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4893025-d574-31e6-bdbc-4c883c9e890d | -5.37504 | -55.9044 | 2026-09-21 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4984559f-ee1f-3df0-9d48-eeae3cf4d063 | -8.18411 | -54.72893 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 670d942a-80fe-3c58-8a41-59c6c7d59825 | -7.21518 | -60.69046 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 30206185-1b0b-3ce0-bad6-e363c8805738 | -6.07089 | -55.61838 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1658b666-47e0-3d5c-8a06-588df9cc8447 | -5.86118 | -53.48981 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2d5757c-4b94-364f-bfbd-8f2ba245c438 | -5.84955 | -53.53377 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c591a56-15e3-3eb6-b779-710ec10eb582 | -9.55506 | -66.00162 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README92.md)
