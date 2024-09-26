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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0458aa47-c21b-31ce-99b5-1d6c6d218db9 | -7.3639 | -55.4935 | 2024-09-26 04:15:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 3d910cc5-585d-34f8-a393-321fc51dfeef | -7.3637 | -55.5134 | 2024-09-26 04:15:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 170.9 |
| ac83c73b-534f-3e61-a37c-f3643c8568b0 | -7.2906 | -61.0869 | 2024-09-26 04:15:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 9a0c3aef-d0f4-38bf-8dd9-88a12ef594ca | -7.2905 | -61.106 | 2024-09-26 04:15:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 88434469-6df8-3fa8-bac3-a565f09d7567 | -7.8156 | -54.7252 | 2024-09-26 04:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| c7ba3d34-8907-3d0f-b4c3-e9b52ad323ae | -7.8154 | -54.7453 | 2024-09-26 04:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| d2ad28a2-3dd1-366c-922d-17f36bfa73e9 | -7.797 | -54.7263 | 2024-09-26 04:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| f4c213d5-7aa2-37ac-b15a-0db876fbf61d | -8.1394 | -61.2817 | 2024-09-26 04:15:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 88b39ec0-8bde-30a6-91eb-ad3fde3ae65f | -8.1393 | -61.3007 | 2024-09-26 04:15:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 26.9 |
| a391dbb7-f4f5-35bb-be68-0bdb136b7e12 | -8.3155 | -54.9956 | 2024-09-26 04:15:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 2a5cf28d-acee-325c-ba53-efab1cb223d7 | -8.7087 | -54.7881 | 2024-09-26 04:15:56 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| a5ac5939-c8d9-3ba9-a72c-e561ac4bbfbc | -8.9242 | -63.2804 | 2024-09-26 04:15:57 | GOES-16 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 41.5 |
| af91e515-6da7-3eb3-946f-c03689d9a9bb | -8.9241 | -63.2993 | 2024-09-26 04:15:57 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 3846d490-1134-3a7a-96e7-231b44e02e2f | -9.1046 | -61.1237 | 2024-09-26 04:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 45a878bc-d19e-32f7-a1e9-1748a8ec8ebd | -9.1033 | -61.3152 | 2024-09-26 04:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 4a526b31-9ca9-3267-947d-aa10c79fef57 | -9.1032 | -61.3343 | 2024-09-26 04:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 339369ca-278d-3329-a8e1-ad1365cf7869 | -9.103 | -61.3534 | 2024-09-26 04:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.1 |
| ca28b3d0-41f1-3ba7-bbb1-cef49143a361 | -9.086 | -61.1245 | 2024-09-26 04:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 0411c782-455e-3375-95d1-e1eda79acbfc | -9.1219 | -61.3143 | 2024-09-26 04:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.8 |
| ace300f2-4b85-34c6-89e5-0b7f20b20e45 | -9.1217 | -61.3334 | 2024-09-26 04:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| d005c08b-804b-3b22-b3ea-7b846a6c369f | -9.1216 | -61.3526 | 2024-09-26 04:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 457f6269-0d6f-397c-8372-11cfd3b70eea | -11.2223 | -54.7735 | 2024-09-26 04:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 260737f2-db61-35e6-9271-d81573caa647 | -11.222 | -54.7939 | 2024-09-26 04:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 85d041a5-b6cf-3e6e-b504-c2ef45580eab | -11.2036 | -54.7548 | 2024-09-26 04:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 122c57e8-e24c-3e12-9e8f-f05e93425450 | -11.2034 | -54.7752 | 2024-09-26 04:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 504.4 |
| 4a55b4ca-871a-337e-b8c1-189541505e32 | -11.2031 | -54.7956 | 2024-09-26 04:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 288.5 |
| 95dc699a-1326-3f59-b80b-435d2534ec63 | -11.1845 | -54.7769 | 2024-09-26 04:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 0de91fee-17cb-3b64-9a5b-2d61b5ed1f62 | -11.2788 | -65.2793 | 2024-09-26 04:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 81.5 |
| a902f593-dd63-3dbb-9865-14b5fe7e58a9 | -11.2786 | -65.2982 | 2024-09-26 04:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| b7ea7afd-ae53-3ec5-8fe0-67a94b3752b5 | -11.26 | -65.2801 | 2024-09-26 04:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 144.1 |
| aa78cd54-9143-3c1c-9af3-ad04c2f351f4 | -11.2599 | -65.299 | 2024-09-26 04:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 128.7 |
| d33d26cf-bea4-3964-87b1-9da64401ea98 | -11.2413 | -65.2809 | 2024-09-26 04:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 5c51067f-21e9-30b2-a232-7d96f53b65f4 | -11.2412 | -65.2997 | 2024-09-26 04:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| f61d88ec-7740-3110-be0f-d2ba991e6eee | -12.2367 | -45.5045 | 2024-09-26 04:16:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 175.3 |
| ca39d0d6-9169-3bc2-87b8-c7a08f208462 | -12.2363 | -45.5276 | 2024-09-26 04:16:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 6ca9236a-04c7-3d2e-b759-3eec4ed763f5 | -12.2175 | -45.5074 | 2024-09-26 04:16:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 40c1043d-779f-3b13-b6b5-bacb0aabc94a | -12.217 | -45.5305 | 2024-09-26 04:16:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| aed0877d-d088-3720-ac83-b9c18247a49a | -12.2773 | -62.3167 | 2024-09-26 04:16:16 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 8055f2c9-aa41-307f-923e-73bee1de26f0 | -12.5218 | -48.9173 | 2024-09-26 04:16:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| d8f884be-6304-34a7-bbd0-e88e321aceb1 | -12.5026 | -48.9198 | 2024-09-26 04:16:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 804ca102-b42b-3cd2-9769-f2c36b46608d | -13.4993 | -61.2698 | 2024-09-26 04:16:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 45.2 |
| ca6a2b05-3508-3285-937c-f952aee21317 | -15.3371 | -58.1651 | 2024-09-26 04:16:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 650fee47-46ec-3de4-b178-8fb495b16292 | -16.118 | -51.9867 | 2024-09-26 04:16:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 08564559-3cee-3fa5-bb0a-5d35ba1875a2 | -16.1176 | -52.0082 | 2024-09-26 04:16:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 42.0 |
| bfc42e85-da65-39bf-aea7-937080287e0a | -16.0985 | -51.9896 | 2024-09-26 04:16:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 7cb6baef-3675-342a-ae24-7f689c61c992 | -16.098 | -52.0111 | 2024-09-26 04:16:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 53.2 |
| d55a3ac9-7847-38b6-9a2c-9c58fb486dc2 | -20.608 | -51.4986 | 2024-09-26 04:17:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 152.0 |
| 1d8a61cf-5b6e-3be8-b491-778405102390 | -20.6074 | -51.5209 | 2024-09-26 04:17:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 181.6 |
| 3b406bf9-9477-3464-a087-2d530bc62a05 | -21.9381 | -48.5453 | 2024-09-26 04:17:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 2d3fdb45-9a69-3b5b-89f3-d0d60ef3ab28 | -21.9374 | -48.5688 | 2024-09-26 04:17:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 115.0 |
| a577450d-82f4-35b4-b2a2-b56adee07898 | -22.2162 | -47.5603 | 2024-09-26 04:17:08 | GOES-16 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 121.5 |
| d34b810a-fd14-362f-b6ec-4f97606650f8 | -23.7574 | -51.9145 | 2024-09-26 04:17:17 | GOES-16 | SÃO PEDRO DO IVAÍ | PARANÁ | Brasil | 4125803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 58.7 |
| 5e3e3e2a-abe5-3617-af27-6726e746fb64 | -2.6785 | -57.531 | 2024-09-26 04:25:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 7141d5da-702c-382b-8293-d641514f28c4 | -2.6968 | -57.5112 | 2024-09-26 04:25:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 03d3c0fc-0330-3941-850b-5e32540cd4da | -6.9306 | -63.1053 | 2024-09-26 04:25:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| bb5ec3f6-d29b-3763-bd79-86a9debbc6df | -7.3823 | -55.5124 | 2024-09-26 04:25:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 2cf33d80-0b74-3405-95ad-028e593c1c5a | -7.3639 | -55.4935 | 2024-09-26 04:25:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 144.6 |
| dec945bf-3cde-33a0-9f91-69a4fe590f7c | -7.3637 | -55.5134 | 2024-09-26 04:25:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 150.4 |
| d4b94ae4-e3a4-30ce-8923-9576e6924678 | -7.2906 | -61.0869 | 2024-09-26 04:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| ebb2572d-dd27-31bb-b7d8-08ea9dd734db | -7.2905 | -61.106 | 2024-09-26 04:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 109ee5ae-59a1-3947-9bf6-dfd8b3beba00 | -7.3824 | -55.4924 | 2024-09-26 04:25:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 143.7 |
| 6054647d-01bf-30c7-9014-a904ff94b354 | -7.8156 | -54.7252 | 2024-09-26 04:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 145.0 |
| ce88f68a-61f1-3c9e-8bf8-4ec128828d02 | -7.797 | -54.7263 | 2024-09-26 04:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 33120268-a1d4-3ecd-b0d7-7286507ac047 | -8.1394 | -61.2817 | 2024-09-26 04:25:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 39.6 |
| b656bf2f-fe4b-3846-b858-a2c5184ea5ee | -8.3155 | -54.9956 | 2024-09-26 04:25:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 2f13e749-fe06-3487-b526-10424d33f6f4 | -8.7087 | -54.7881 | 2024-09-26 04:25:56 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 71f3ed6a-ac1d-3946-82eb-ba6ac4bff576 | -8.9242 | -63.2804 | 2024-09-26 04:25:57 | GOES-16 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 5935eee6-2dd3-3807-bd48-c751e49c2a6e | -9.086 | -61.1245 | 2024-09-26 04:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.0 |
| f077de66-4f01-3c24-bcf1-2a454f38a9c2 | -9.1032 | -61.3343 | 2024-09-26 04:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| d411efb7-f375-3667-9754-e096ce294c22 | -9.1033 | -61.3152 | 2024-09-26 04:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| c2d86eff-d640-3d33-8771-e3aca69496ca | -9.1046 | -61.1237 | 2024-09-26 04:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 9f9a1cff-600b-3008-b053-56a723688b31 | -9.1217 | -61.3334 | 2024-09-26 04:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| c7d2bf41-a024-33a7-a2cb-bee1d1825894 | -9.1219 | -61.3143 | 2024-09-26 04:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| eb12a1c8-3b27-3f6c-8844-c18f45522850 | -9.1216 | -61.3526 | 2024-09-26 04:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 2ba028bd-49d1-39da-9873-fc56933739ed | -10.7117 | -60.7118 | 2024-09-26 04:26:07 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| a5dcc690-6195-3aa4-901c-459197041b01 | -10.7115 | -60.7312 | 2024-09-26 04:26:07 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 097792c2-90a3-38e9-91e6-3ac21decf702 | -11.2413 | -65.2809 | 2024-09-26 04:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 54da4702-d989-328c-bea8-a01e0a552ab5 | -11.2599 | -65.299 | 2024-09-26 04:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 86.2 |
| dbb36844-4a54-301e-82b2-b6d0b08434e9 | -11.26 | -65.2801 | 2024-09-26 04:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 118.8 |
| ebe35e60-dc4a-35f7-8081-6ec94a904579 | -11.2786 | -65.2982 | 2024-09-26 04:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 22e73e49-3dbb-3f7d-a172-a5750457acd6 | -11.2788 | -65.2793 | 2024-09-26 04:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.7 |
| d1746d9e-2f8e-358c-96b7-ccd3a3cc9d51 | -14.863 | -51.5019 | 2024-09-26 04:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 2d430a62-2018-3ace-9879-5f2ac764c0ec | -14.8634 | -51.4804 | 2024-09-26 04:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 615622a8-61c9-34bf-86ef-4531debc0fd0 | -14.8824 | -51.4992 | 2024-09-26 04:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 1e77380a-a94e-38af-a0ce-c1cffad9380d | -14.8828 | -51.4777 | 2024-09-26 04:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 18cd6038-b57b-3cc0-902a-08055fbeaf78 | -14.9022 | -51.4749 | 2024-09-26 04:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 0de5f090-55b2-3b42-a992-89b93fc3cd1c | -16.1185 | -51.9651 | 2024-09-26 04:26:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 47.4 |
| f28d5681-02fd-31e0-90a6-0e24a547035a | -16.118 | -51.9867 | 2024-09-26 04:26:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 90.8 |
| ae666aa8-c34f-37cc-9981-12ed72351bc8 | -16.1176 | -52.0082 | 2024-09-26 04:26:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 32.2 |
| ee6f63b2-7490-32b6-9f4c-3781c47dfd0c | -16.0985 | -51.9896 | 2024-09-26 04:26:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| e45b3810-dee3-384b-83fd-cd3e501b72d3 | -16.098 | -52.0111 | 2024-09-26 04:26:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 639268e6-3987-398b-b6f0-5ae4c459433c | -20.608 | -51.4986 | 2024-09-26 04:27:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 160.2 |
| 5acbdd47-e1e2-3c76-9032-cb35fa2f6c49 | -20.6074 | -51.5209 | 2024-09-26 04:27:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 182.0 |
| 2625dbb9-647f-3d84-9466-b1646eb184ca | -20.6279 | -51.5169 | 2024-09-26 04:27:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.8 |
| 9840788e-d9e3-3525-a324-93813c19cdaf | -7.2906 | -61.0869 | 2024-09-26 04:35:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 0db0e3c8-fd8d-38f9-ad7e-2ad3f74ad57b | -7.2905 | -61.106 | 2024-09-26 04:35:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 617dc25e-5af4-394f-a072-a214cdab9d72 | -8.1394 | -61.2817 | 2024-09-26 04:35:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 8bb4050d-a342-329a-9a8e-1a7977aa52f2 | -8.4156 | -70.7535 | 2024-09-26 04:35:55 | GOES-16 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 62e973ab-dddd-3c3b-ad55-861179d1ffa2 | -8.9242 | -63.2804 | 2024-09-26 04:35:57 | GOES-16 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 7d81f8a2-f7e7-3763-9463-a2c2748c0745 | -9.1033 | -61.3152 | 2024-09-26 04:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 34.4 |


[Clique aqui para ver as próximas entradas](README87.md)
