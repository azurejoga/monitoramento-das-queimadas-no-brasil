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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3027e66-09fc-3e72-9038-8f1745ea31cb | -7.28225 | -60.66216 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8576f252-0d9f-30b4-b1f9-50fc05b82475 | -7.28566 | -60.66268 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87a613fc-d1d3-3ca8-abb4-3da201b3711f | -11.6538 | -52.20142 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 11d671f7-b3ba-33d6-8c02-6e29d6fba1d5 | -6.34135 | -58.18639 | 2025-09-02 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e2c5490-af8e-39be-b87d-67e6f79814cf | -11.6566 | -52.21428 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 89ba464b-4987-3ab3-80e8-6f1153a3a711 | -6.82707 | -52.81077 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5509aca8-eb38-3726-98dc-c66459779137 | -7.5959 | -61.63605 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5726ff2-e68d-300f-846f-a9c9db06c25f | -9.44723 | -60.57644 | 2025-09-02 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20788ca6-d720-3ea8-b4cd-bb331855dbdd | -11.66208 | -52.21951 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9b6e8231-82e8-31c4-aaf9-c30b9bf5d7b0 | -9.32701 | -56.27306 | 2025-09-02 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b58657e-c232-3cc4-a217-ace873364645 | -11.66585 | -52.20329 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| f0b8998a-43e6-3e27-a122-5095063a1f0d | -8.7262 | -62.40957 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cc56c93-0698-3bab-841e-e054d474ffd4 | -11.83971 | -51.5245 | 2025-09-02 05:31:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a27e5058-e8ff-3121-8ba5-483ce2fa168a | -7.66494 | -61.10191 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72f3ab89-1370-34f9-bfbf-5d94a4e31478 | -11.65166 | -52.20455 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 88ca0879-d646-3884-b8fc-26cb9a4c5f6d | -11.64672 | -52.0418 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7b7f9c00-f8a1-3cd0-9f2a-d156f4d48f12 | -6.04192 | -52.17934 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ac1ecae-c500-3de6-b8e5-52522166e7a8 | -5.32142 | -55.88358 | 2025-09-02 05:31:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9cf479f3-0c21-3fba-8841-d80f0e5f6964 | -7.0843 | -63.185 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5b87917-160e-3fdf-bac2-854f87b6d208 | -7.07667 | -63.06052 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b73ee16-7a7b-3d9a-9840-d681f102cffc | -11.66431 | -52.21656 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 6c0dfa37-0e08-3968-8e97-3679b7b33a24 | -11.65796 | -52.16534 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0aa0f179-eafb-3c8c-af56-f5ac4baec113 | -8.50524 | -63.90841 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 765844c2-ff2f-3133-9c30-b76764daf36c | -7.66267 | -61.0942 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1300a0d-337c-3782-aeaf-0fd3fc967703 | -11.66869 | -52.16576 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 70666659-f94e-3c4e-b336-8d31df22c164 | -6.82563 | -52.81501 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd7b1e97-b46c-30a5-9aa2-c243d27b9c64 | -11.66702 | -52.17939 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4039d4a4-3aed-304c-b11b-9662f9ded963 | -7.47807 | -63.82604 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 763ff28f-1bde-326a-aab2-1e0614368990 | -5.31711 | -55.88297 | 2025-09-02 05:31:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c169c9c-9dcf-3d77-bffb-f3d850c85353 | -8.73398 | -62.42512 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71f998a8-a599-3971-97e4-10b9145cb2ef | -7.6739 | -61.08859 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ea9a7945-e146-3df2-a879-7c4d69ebdf18 | -9.34378 | -55.2232 | 2025-09-02 05:31:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b965542-c104-3ec6-baff-6de906ed7993 | -9.25098 | -60.49263 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e550f06a-a7ec-3e4a-be8b-ef8cb0a632a4 | -7.5507 | -61.33998 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 38644827-f5b7-36d7-9227-e12c0bff2da6 | -8.66485 | -62.92239 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f0db2b45-580f-3e2d-a1f3-52869d3aad3d | -9.32764 | -56.26863 | 2025-09-02 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47acdd8e-cb5b-3981-b994-8baeefcf8590 | -6.13904 | -62.53041 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68b4fb28-2e76-37d9-9c3d-6578cfc502da | -7.47409 | -63.82914 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac0b52be-6ba0-3533-a338-76f28277669a | -11.66637 | -52.19883 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 2caa8e93-cb99-3020-95b0-cbb62bb42dfa | -6.47658 | -56.00573 | 2025-09-02 05:31:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d37f0ab3-dcc1-3fe3-bd89-6cef18b65f33 | -9.45476 | -60.57367 | 2025-09-02 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1351f902-7181-37c7-b495-f9fa66c4b7df | -6.43871 | -55.6416 | 2025-09-02 05:31:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca0d519b-9aed-30b7-bdf6-2b26faf699f8 | -11.31464 | -55.21486 | 2025-09-02 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cedb923-5a41-33a8-858d-a1004ede8764 | -9.27202 | -59.75324 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f464f9e-55fd-365a-a4d4-4be1d5d37672 | -8.68019 | -62.39867 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be53f8ac-3ec5-39a8-8943-490d8f495766 | -8.96622 | -65.97252 | 2025-09-02 05:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7fc81dca-78ff-3f8a-accb-cafb1fef717f | -11.92647 | -50.61444 | 2025-09-02 05:31:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c871b019-98a0-30cd-8daf-5799c78b8f20 | -12.94018 | -56.96446 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a5f2777-7c50-389c-8357-ed991d230014 | -12.41945 | -63.90625 | 2025-09-02 05:33:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3d96368-1d31-3d07-b3ad-c94689cbd525 | -12.6284 | -56.99937 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6dfc34ff-15dd-339f-bdbd-500645f4bd12 | -12.92676 | -56.96262 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ccdd3ba7-218e-3f8e-85c5-ba5379c6b264 | -12.60945 | -57.00579 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ad37e7f-abbd-3f9c-954c-b1f09a6c9162 | -11.65669 | -57.35791 | 2025-09-02 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| be372195-f953-3db9-9350-b8d19870f728 | -14.58544 | -54.54364 | 2025-09-02 05:33:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5e8fbf23-609d-3efc-8e63-8b43495bb88b | -11.82983 | -62.92931 | 2025-09-02 05:33:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9b834f3-abf2-3677-9c25-99af0e4a1833 | -14.97996 | -50.20041 | 2025-09-02 05:33:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 860e69e2-dd25-3e6d-8dff-c9a398870608 | -11.65357 | -57.35883 | 2025-09-02 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 15af8b26-6d59-3826-84ba-cb214337fda5 | -15.642 | -56.01394 | 2025-09-02 05:33:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 86290ef6-8899-397d-9c56-56edfe9f4f11 | -12.44661 | -63.92897 | 2025-09-02 05:33:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d79e1f67-a9bb-3357-9743-dd70e7b051a6 | -12.93302 | -56.94973 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7915ce15-17d8-322f-9a64-2accb2b20788 | -12.97829 | -54.76088 | 2025-09-02 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5760a0a0-37fe-3ede-b720-0c290c064b5e | -12.91573 | -56.94257 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f04ed8b-445d-3895-84b6-c400616e1e09 | -15.73014 | -53.64829 | 2025-09-02 05:33:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec2ea3a0-9ac0-3586-8d4e-405c56bb804e | -12.93547 | -56.99991 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9bb857ef-c0b7-3693-bb9d-a0a26247163d | -12.9779 | -54.7641 | 2025-09-02 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| decdb0c9-5a21-3095-85fa-b6f45760d871 | -15.73254 | -53.67881 | 2025-09-02 05:33:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af2624ff-8987-3c32-9b25-35d025ba2166 | -12.93605 | -56.99555 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a46046cc-d4e7-3499-b953-db06b6876c8f | -12.63344 | -56.99555 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4df80bc-80f7-3b99-ba76-d22d01777693 | -16.29809 | -52.94953 | 2025-09-02 05:33:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 718ca424-2ccb-38b0-b6c6-08a312556ab2 | -12.93043 | -57.0037 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8accbb41-8dba-3ef7-84f1-2d17fa35cccb | -15.73272 | -53.68114 | 2025-09-02 05:33:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 448a3bd4-6d20-33ec-8488-3ae529ac56ff | -10.40507 | -69.3836 | 2025-09-02 05:33:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1213b184-b90f-3c53-8e08-1da087ffabf9 | -14.20331 | -51.65441 | 2025-09-02 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1be109ee-0323-3602-b157-9e95f3201b24 | -12.91691 | -56.93351 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11734473-640f-38a3-89bc-b6f82d985848 | -12.92079 | -56.93871 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8af5487e-c730-30e3-93f8-addc610323ba | -12.63284 | -56.99998 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e09bb646-d05d-3375-8083-e682c09ee2b7 | -11.65616 | -57.36186 | 2025-09-02 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 616f2ad3-2086-3b3e-821b-d245727722b4 | -11.53446 | -61.03594 | 2025-09-02 05:33:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4476fc0d-a606-3782-999c-558e5eb568ef | -16.28602 | -52.94695 | 2025-09-02 05:33:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ccfb384e-8a1f-3623-b485-4bf953bd1be3 | -12.92199 | -56.92953 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5b2e1f1-80f2-38c4-beb1-e6434135c0aa | -12.92209 | -56.99805 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae89a655-f967-3e6a-a6a8-f6266704f7b9 | -14.58467 | -54.55034 | 2025-09-02 05:33:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0207b29-5187-3057-8380-ada79038a1ff | -12.42668 | -63.90381 | 2025-09-02 05:33:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f61dd28c-77ce-3ba1-839b-4f2183cf35eb | -12.62959 | -56.99051 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 777f466a-ed78-381b-a3cc-5b983c66944d | -12.92795 | -56.95364 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63e9d30a-ea81-3878-ac12-d7f162ec0f90 | -14.59804 | -54.57644 | 2025-09-02 05:33:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a88917d0-9555-31fd-adaa-7eef524544a2 | -12.90562 | -56.95019 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49bd88f4-9c25-3c22-ab1e-2b47cee41b0c | -12.91631 | -56.93807 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a5c4d37-23dc-37ee-a042-23815b6694dd | -12.91901 | -56.95227 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a6c9d22-7fc6-3e4c-91f0-efd330c293ee | -14.56506 | -52.99743 | 2025-09-02 05:33:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98e44d9a-3ded-3c8d-90cd-10c072419f8e | -12.91843 | -56.95676 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9fd631f-8c5d-361a-9000-0535696bae92 | -16.30466 | -52.94577 | 2025-09-02 05:33:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e181de90-8b90-3e3d-84ee-d7d79878effa | -14.31981 | -60.34064 | 2025-09-02 05:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 624f401b-fe26-3762-a4db-fc4e46b5e196 | -12.9256 | -56.97142 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41cad6a7-bdb8-38ce-86ca-8669b02d4bea | -15.64131 | -56.01958 | 2025-09-02 05:33:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c35704af-f59b-361e-80cc-3e703bf35068 | -14.58007 | -54.54278 | 2025-09-02 05:33:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f81d4304-82e5-3a9a-b669-42a2681d65cc | -15.72723 | -53.67395 | 2025-09-02 05:33:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55985ab1-5850-3f64-ae96-06244f8b04b2 | -12.92289 | -56.95745 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eae090c5-1364-3d1b-a1b7-2c1c1c96f0ad | -16.29162 | -52.9524 | 2025-09-02 05:33:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e46bb6df-288d-3650-9173-d33c0c353f8d | -12.92735 | -56.95814 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README81.md)
