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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4bad7a3e-1bf6-38a0-946a-bf136f95d60a | -9.7231 | -65.00437 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3a127a6-6659-3eaa-a4f8-3267d3b5e372 | -8.4352 | -70.41554 | 2026-08-31 05:36:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3956922-f575-342e-abd7-4d34ce7a2596 | -9.0511 | -65.41231 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9b006de-8a47-3a31-9cd2-c94507872560 | -10.75461 | -54.00407 | 2026-08-31 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 856f8b6a-becb-3470-a35c-215358349213 | -9.07353 | -60.4217 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7603e7ae-978f-3369-9c0e-3e8959a53849 | -11.17989 | -55.1015 | 2026-08-31 05:36:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ee82f18-7057-3355-8b1a-e245addadf9b | -12.01064 | -60.51114 | 2026-08-31 05:36:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 02af4b04-6900-3d3d-901c-fc3d92d52e69 | -9.94346 | -60.5216 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8f6975b-367b-3295-b442-d868fa4e1196 | -10.74449 | -50.64193 | 2026-08-31 05:36:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe06e17e-8660-35e5-9d8b-9ae7ef0a2210 | -10.81623 | -50.6559 | 2026-08-31 05:36:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d2c1326f-98c0-36e4-98ee-2f997e153163 | -9.83672 | -64.97305 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fa172f6-45d8-3e34-ba42-b47cc32fb672 | -8.97048 | -62.38715 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e70f628b-e0c7-3733-89a0-ef7e2b4b8eea | -9.04928 | -65.44617 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 217c233f-117c-3b54-94fe-1912b42a401b | -8.86858 | -66.77506 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d53b28f4-08e8-3ea2-a1cf-6098dffa2102 | -9.25191 | -60.4353 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b21903b8-d94f-3429-b869-ebb97604cc2e | -10.57157 | -50.37003 | 2026-08-31 05:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9203252a-eb96-3275-b3e7-043f4ee2701a | -9.5946 | -60.52475 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c20b5f5-a540-3451-bafa-6e373dfef3dd | -10.81511 | -50.66486 | 2026-08-31 05:36:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 55c3ed26-c8ca-3648-9a74-08779d8b0a7a | -9.35989 | -60.30257 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7527575c-ac02-3101-902b-16ace13ea013 | -11.47997 | -58.51382 | 2026-08-31 05:36:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2437746a-8dca-3c20-bfb3-11f8cad58d1b | -8.68062 | -62.81368 | 2026-08-31 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27f2ccf6-0925-3a59-8025-c3cdca363922 | -10.57238 | -50.36719 | 2026-08-31 05:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 17e05bc0-e63c-3d71-b00a-83879eb66fd8 | -9.89096 | -60.27498 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24b72963-b67a-3fc2-b3e7-cc83ff277c0d | -10.75534 | -53.99879 | 2026-08-31 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11f0b79b-2615-3705-9513-4171a6b72d04 | -10.48066 | -59.61216 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16a73053-6260-3b08-8c04-0963bbeea506 | -10.50302 | -59.6273 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3509744f-1b00-3d83-ae7d-f5f83dc77ebf | -8.60215 | -70.21827 | 2026-08-31 05:36:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39f72728-a870-3fe4-8cab-f0dd96916bc6 | -10.81679 | -50.6514 | 2026-08-31 05:36:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ba5cab6e-9d20-376d-9d8a-3481d2f0b332 | -9.71917 | -64.99352 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 178a8645-8570-32f0-87c9-f56354c2850b | -9.78807 | -59.4472 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cf6d962-a5b6-3154-b26e-cfae49720bd2 | -8.97107 | -62.38357 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2570478a-7ca5-30db-a38c-14695392da7b | -10.74422 | -54.04105 | 2026-08-31 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d913f13c-676e-3bec-9b10-bef383dc915e | -8.799 | -62.49273 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4746d24d-084a-3fcb-bad0-f28809bbc5eb | -9.72383 | -64.99997 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9df23eb-65ad-3ecd-b989-87b8f3ea9333 | -8.85758 | -47.06739 | 2026-08-31 05:36:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1487cd43-1153-381a-b71d-566254200cbe | -8.61314 | -54.76878 | 2026-08-31 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6ca6a8a-9bd6-3159-a96c-5457d973429f | -7.57769 | -61.34752 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 916f7abd-90d6-365a-95a0-5bcbd9ed7549 | -7.45115 | -60.73847 | 2026-08-31 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 27f4ef0a-13cb-3890-bb05-2e3bfcb74bbd | -6.86325 | -59.48009 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04dd8af4-3060-3a9d-8172-c1ae5d5791b7 | -9.17362 | -59.63249 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3e38e4d-c6fd-307c-87b1-147a05fb14ff | -6.86773 | -59.47347 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abfe05ca-4e96-30cf-9814-5fe96b517f99 | -6.90538 | -59.49768 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab01af9f-3c85-3928-bc27-d786c9c14ec4 | -6.86718 | -59.47704 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee08b17b-861b-367b-816c-4d9433621328 | -7.69121 | -63.33008 | 2026-08-31 05:36:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f57b09bb-5e5e-3c10-89cf-5958cd659561 | -7.58711 | -61.35261 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ef2c13a-fd5a-3026-9591-3c9beeaee0d3 | -6.91043 | -59.48748 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a64727b6-f777-35f4-9030-baea5012b7f8 | -7.24088 | -64.72952 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cddfa496-c722-3643-b0aa-2f0e695b8122 | -7.60536 | -60.93794 | 2026-08-31 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fcfa469-9e0a-3b5d-903a-cca311e07c53 | -6.76788 | -59.44372 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20f78e30-15d3-3db0-99db-1f38988f05a1 | -6.86492 | -59.46936 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30b62c21-2465-3f78-ab43-a9e1f7c7d997 | -9.15437 | -59.53126 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6bd4fb9-b529-388c-87ae-e55fff6add49 | -7.81108 | -63.25755 | 2026-08-31 05:36:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0728545-201a-3d7f-a78e-bf1a8edf823e | -8.25981 | -62.75314 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8a95251-7347-354d-841b-bf5211a82a60 | -8.71371 | -52.36766 | 2026-08-31 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f76b13d6-4df2-3d81-9127-056919ca5195 | -9.19392 | -51.55784 | 2026-08-31 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bfb0d9f8-97f0-345f-8b60-af91198e27fb | -7.55989 | -61.4163 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1549ce3-7c3a-3bd7-85b6-a88b3f042518 | -7.55933 | -61.41979 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e7aae76-a4fc-3086-9ce7-e9375ab5cf8b | -9.17307 | -59.61356 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0aa60381-fb8b-37a0-a849-3688b0215c1f | -6.80328 | -59.46025 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dfb44fbe-65d7-37ea-adab-f51e72e33b38 | -9.3091 | -56.8056 | 2026-08-31 05:36:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10ea7a7f-40b5-39b0-a898-e2d104aa374e | -9.16531 | -59.36896 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d77c20e6-8cb2-3e19-b513-9057bc19f306 | -8.61692 | -54.69107 | 2026-08-31 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ccc4c60-5f95-39a1-9f57-aa5d35bbbed3 | -6.81788 | -59.45521 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd9b7886-b147-3021-aecf-9352f0253008 | -9.16473 | -59.37271 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b9d3d65c-8c58-3d93-ad7a-54d235372a13 | -6.86099 | -59.4724 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ce20a90-98fb-3ce3-8d57-d3b6fc4d077c | -7.69534 | -63.32677 | 2026-08-31 05:36:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 649867fe-926e-3b01-879e-c8c4a29940b1 | -7.30418 | -60.59399 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 028794d1-d603-39e8-aa16-a4a0dbcb947a | -9.00484 | -60.60148 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bed7f65-42a0-37c8-a20b-054dfaa877a8 | -7.51887 | -61.37389 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4fcabac-3942-3fe5-a75c-574cb0f27ab0 | -7.92483 | -61.33489 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d169b124-875b-3452-84e8-13a9e446a1e6 | -8.61516 | -54.78675 | 2026-08-31 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e3e579c-2dbc-3308-b279-5e16f3dcb5f0 | -7.34074 | -60.59979 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5586c821-3ca6-3057-9d4d-226c67f8b31e | -7.30638 | -60.58008 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 61338019-54a8-3040-b261-94b1807714c4 | -7.33519 | -60.59178 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 28bc3f6f-ac39-3b10-a9f6-c91df2a76c9b | -7.52372 | -55.33796 | 2026-08-31 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aa592842-e3bd-3485-b321-44cde8feac75 | -7.69248 | -63.32232 | 2026-08-31 05:36:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8f2698c-629f-3e51-91df-3729fd226abe | -9.41125 | -51.69103 | 2026-08-31 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47411953-1280-3c3d-aab6-5de6d96d2715 | -7.29674 | -60.58229 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f0152a1-dc0a-344a-a831-65f052051276 | -7.58379 | -61.35208 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9422acb3-e523-3929-9385-9380e7ae15bc | -9.17702 | -59.63303 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ff49ab7-78a7-33de-b3f1-eb0cbc3cdf36 | -9.01262 | -60.59549 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e20b8f9-923e-37b2-b929-c242021d3cd4 | -7.58268 | -61.33758 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e642e482-aa55-36f7-a168-06fb0bc4730e | -6.90763 | -59.48337 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b0389baf-051a-3815-8729-22af8f0b9b44 | -6.92056 | -59.35648 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cba23f71-2d80-3c22-9000-3cf5937390ac | -7.79418 | -61.57559 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 301af816-2205-3c7f-927c-17ee918ca6dd | -7.52487 | -55.33012 | 2026-08-31 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d499cb6-f51c-39af-b292-94e114c2c3c7 | -6.86155 | -59.46883 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39224a76-83d2-34d3-923f-6413510d9392 | -7.34406 | -60.60032 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fd6085ee-2f31-3d0d-a619-a0800757b8ae | -7.52348 | -55.3105 | 2026-08-31 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 522b9181-60b2-30ea-add6-dd14177a8c21 | -9.15948 | -59.54344 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46233694-51f2-38fd-9c32-4dc8c7a9834a | -9.16179 | -59.50586 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c05dd6e5-0e3c-37d7-a0a2-8cd22dabc30a | -7.3025 | -60.58303 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd7db5f8-f60c-3938-8a0c-0b5bd9229f3b | -7.62058 | -55.29602 | 2026-08-31 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a36283c-2720-32bf-9992-4eb87a31dffb | -7.62185 | -57.61544 | 2026-08-31 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d946e5b2-b757-37ca-bd82-f2c25b197011 | -7.5222 | -61.37443 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e678aaa6-1732-3eed-8783-44d4fed7645d | -9.207 | -59.41758 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 210009be-d4c9-3e7b-8359-63977f174da3 | -9.14924 | -59.54182 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46f9b4d1-460e-3b26-a024-19e3d70fc423 | -7.58102 | -61.34806 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49074d6d-308b-36d0-a6fe-0df82f7ebe05 | -7.62535 | -55.29277 | 2026-08-31 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d22fbc54-6bdd-38c9-a1cc-31765357577f | -7.51951 | -55.33749 | 2026-08-31 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README66.md)
