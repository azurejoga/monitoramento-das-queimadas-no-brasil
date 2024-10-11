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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 272e97b8-5c1f-3105-a967-bcdef567a97e | -4.0961 | -48.2739 | 2024-10-11 03:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 01bab4db-d5a8-3807-b424-308464ba793d | -4.0962 | -48.2523 | 2024-10-11 03:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 180.5 |
| 2b5968b0-e2ca-32c5-a852-00a3b8470347 | -4.0963 | -48.2307 | 2024-10-11 03:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 6b3687a6-f4e7-33a2-a974-011475b7726f | -4.1146 | -48.2731 | 2024-10-11 03:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 0ce4930c-5daf-388d-890b-e28021ccb832 | -4.1148 | -48.2515 | 2024-10-11 03:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 461.3 |
| b044b61e-f89d-3cfd-9ba9-826d68e493ed | -4.1149 | -48.2299 | 2024-10-11 03:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 146.2 |
| f257922f-d2c0-3872-aee5-fe393376b1b8 | -8.4231 | -55.4704 | 2024-10-11 03:55:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 2f956720-a681-3032-9035-dadd8ca7298e | -8.4417 | -55.4692 | 2024-10-11 03:55:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| a9c8b470-5277-3bdc-8c74-b06af92fcb10 | -9.6389 | -64.9664 | 2024-10-11 03:56:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 8d48535f-f06c-303c-b3d8-7d0034b847aa | -9.6575 | -64.9658 | 2024-10-11 03:56:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 13a9426c-7601-346b-ba54-1be8b6e86d73 | -9.9481 | -58.1092 | 2024-10-11 03:56:03 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 5a1a3ae0-914a-3e0a-baba-2eb11d04be76 | -10.7059 | -64.1138 | 2024-10-11 03:56:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 80c53b50-b946-3e17-94c2-d0f2d5750a85 | -11.2407 | -53.2738 | 2024-10-11 03:56:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 138aa026-dbe1-3f32-8129-3269892791cd | -11.2597 | -53.272 | 2024-10-11 03:56:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 8df9fcde-98d3-3e9a-9f5f-5c8dadbc52c2 | -12.4179 | -53.1752 | 2024-10-11 03:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| c53c78f8-a1e3-35ae-9e28-7b9eaed4d238 | -12.4182 | -53.1544 | 2024-10-11 03:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 290f5306-392e-353a-b103-1e9791bb94bd | -12.4373 | -53.1523 | 2024-10-11 03:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 161f86de-5f71-353a-8bec-8d6676c7b377 | -12.4563 | -53.1503 | 2024-10-11 03:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 53ba3fff-d12e-3372-9558-1998a4d97bbc | -12.4566 | -53.1294 | 2024-10-11 03:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 59ef35dd-c3f1-3bc0-a159-4a718fcc8ce3 | -12.7673 | -44.8904 | 2024-10-11 03:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 4cd7dcc1-ee1f-3ae5-9548-bec206737c72 | -12.7678 | -44.8671 | 2024-10-11 03:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 0176dff2-2ba1-3ce4-9e16-9c8b4cb84c8e | -12.7866 | -44.8873 | 2024-10-11 03:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| e7968e38-d3fd-3b32-a459-f10a954a96f0 | -12.7871 | -44.8639 | 2024-10-11 03:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| fbb6a7f2-be82-356a-b654-d1255e5c9fe9 | -17.6862 | -56.3241 | 2024-10-11 03:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.2 |
| 1b299a75-d85e-31e5-8263-ba9597220c68 | -3.39216 | -42.21029 | 2024-10-11 03:57:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 70b2034a-01fd-3316-8919-3fcbbf5af00d | -3.95916 | -41.48134 | 2024-10-11 03:57:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4b868c37-1cc8-379b-a2e8-bb67a02038d2 | -2.3801 | -50.32292 | 2024-10-11 03:57:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 817a5645-c1ca-3bfb-a430-1104c3e37c1e | -3.45817 | -44.27766 | 2024-10-11 03:57:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0bf46480-6537-37a8-9384-137d2093bd82 | -3.41984 | -44.4592 | 2024-10-11 03:57:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 75281d8d-0bd4-39b1-b237-ad39cf558439 | -3.41632 | -44.45481 | 2024-10-11 03:57:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f3158528-3a32-34e8-bc28-b96c2e81ce48 | -3.41571 | -44.45851 | 2024-10-11 03:57:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ea16779f-5455-3fce-be0c-3152dda2d5fa | -3.36929 | -44.36856 | 2024-10-11 03:57:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5a2a63a2-2b97-32a2-9ed1-39051660aa73 | -3.36869 | -44.37223 | 2024-10-11 03:57:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7033ffb3-f1c6-3db9-96b4-a4f3494b41a4 | -3.36517 | -44.36789 | 2024-10-11 03:57:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7843549c-d0c5-3b11-a155-e9bee7fcab40 | -3.36458 | -44.37155 | 2024-10-11 03:57:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5adfdafb-f128-37ca-958b-d7695cf0d55d | -2.54042 | -47.22383 | 2024-10-11 03:57:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 50ef236f-fdb7-34a6-abfe-032ffbd287e7 | -2.53993 | -47.22672 | 2024-10-11 03:57:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5de489c6-b032-3ef9-9df1-03ac6319c4e9 | -2.53945 | -47.22963 | 2024-10-11 03:57:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 27c1deb9-1514-3f57-8021-d545b46d86e2 | -2.53896 | -47.23259 | 2024-10-11 03:57:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 985f5bef-eafe-3712-9cde-7cb17692861d | -2.39853 | -46.71327 | 2024-10-11 03:57:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 536e0d91-0a7a-393d-8fc4-13fa9bcaef30 | -2.39575 | -46.70807 | 2024-10-11 03:57:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb146d3c-09f0-3e2b-9188-c962d4bc31c6 | -2.39484 | -46.71353 | 2024-10-11 03:57:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c8a824a-7f63-350a-ae7d-4ce96a4852d2 | -2.03917 | -48.02578 | 2024-10-11 03:57:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0af22552-adf6-381d-9da2-9ed71069f194 | -1.99824 | -47.25742 | 2024-10-11 03:57:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4d3a75a9-2c89-3b82-9dd5-30355b77b290 | -1.99312 | -47.25658 | 2024-10-11 03:57:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9fa105e4-5db2-3d78-9ae8-c02bb956dce5 | -1.9111 | -47.8854 | 2024-10-11 03:57:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1127ace2-874f-31b0-ae43-4e494a1e8e24 | -1.90573 | -47.88461 | 2024-10-11 03:57:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4ef6aa8-f659-3b10-ba80-11ef32d48c7e | -2.80743 | -48.7051 | 2024-10-11 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 59f93688-48d4-3bc7-8726-cd2a43872871 | -2.80683 | -48.70882 | 2024-10-11 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9c573b64-d2ce-3c47-a665-5f78b38a20e0 | -2.80618 | -48.70269 | 2024-10-11 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| af291be1-4b2e-305a-bcdd-6a8063697d6a | -2.80555 | -48.70639 | 2024-10-11 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 55428089-0a06-3ea9-b119-664e8c25e5dd | -2.80246 | -48.70045 | 2024-10-11 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60df997c-38c5-3351-88ce-0a5a0a1dad8e | -2.80186 | -48.70415 | 2024-10-11 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f710ec40-96cf-353e-9a69-a4c1b9ee75b7 | -2.75351 | -48.68459 | 2024-10-11 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34bc8e57-63c1-3d73-b6cc-22a70744d4ae | -2.74856 | -48.67992 | 2024-10-11 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a2d735a-89ae-366e-a1ed-d8b06b8c8062 | -2.74795 | -48.6836 | 2024-10-11 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e2c7b8f-179a-3860-a473-659a41a19e01 | -2.4209 | -48.45193 | 2024-10-11 03:57:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff4f813d-b792-3e68-882e-a84c5665f19f | -2.42047 | -48.45149 | 2024-10-11 03:57:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 817fd339-cdb9-3800-ab3a-c760d47a994f | -2.42032 | -48.45557 | 2024-10-11 03:57:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fed8e4d9-b0d4-3332-872e-0b96b705598a | -2.41986 | -48.45508 | 2024-10-11 03:57:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8d7e97e-0c62-3d03-a297-77b2e05a808a | -2.23764 | -48.01999 | 2024-10-11 03:57:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f20b85b-29bc-3c74-89ff-401af4548af1 | -2.23708 | -48.02342 | 2024-10-11 03:57:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b93cdec4-e950-395a-ab01-67ad338daa21 | -2.71059 | -49.43954 | 2024-10-11 03:57:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4243c76-be24-39ed-a8d4-6a7f2bc320dd | -2.61525 | -49.78458 | 2024-10-11 03:57:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 784954af-7201-34c3-89c4-a04bf1c9a0ff | -2.6145 | -49.78896 | 2024-10-11 03:57:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2ebb5df-5e62-3593-a745-f7e39afea4d0 | -2.50374 | -49.15065 | 2024-10-11 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdd05e8d-3637-3730-a16c-bd881c11cbd8 | -2.49799 | -49.14958 | 2024-10-11 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c1d6954-0d76-3329-910c-0c8d9b9a9df1 | -2.46505 | -50.25917 | 2024-10-11 03:57:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7085cd9e-f486-3848-9bd6-8a9a87f6839a | -2.37929 | -50.32774 | 2024-10-11 03:57:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92fbafff-77d1-3394-9bf6-10e6282728f1 | -2.37306 | -50.32669 | 2024-10-11 03:57:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5fadbff-d02f-3439-bbac-4b5d01c3f914 | 2.34838 | -51.56013 | 2024-10-11 03:57:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| be04ce1f-5875-3663-b3fa-a69431da9644 | 2.34503 | -51.56764 | 2024-10-11 03:57:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8ad059f3-39e3-346d-a01d-f5b5207acd23 | 2.34404 | -51.56096 | 2024-10-11 03:57:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7b8c0c8f-7e54-3811-8d97-878498632419 | -5.96958 | -43.88896 | 2024-10-11 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b382fecd-ed2f-3592-bd1e-fb89728642ee | -5.968 | -43.89833 | 2024-10-11 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57fd728c-7c69-3e77-b2e1-585229614df7 | -5.96212 | -43.89914 | 2024-10-11 04:00:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e3b38024-1edf-3d21-95ee-efbe71f72b6e | -7.9016 | -44.86024 | 2024-10-11 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 908b4a58-3069-3353-acb4-c12871b115d2 | -7.666 | -45.21855 | 2024-10-11 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 298f0af5-253f-3483-b6fa-0c0a2e4f1ab2 | -7.64357 | -44.17317 | 2024-10-11 04:00:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0673a2be-214e-3b7f-bf52-d3ff24c811bc | -7.58448 | -44.76899 | 2024-10-11 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad9ee5cf-a6ca-32c3-b0cc-79c94ffac2f3 | -7.57967 | -44.77333 | 2024-10-11 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9fa36f56-f34c-3ff5-b295-fd8ebd19fac8 | -7.5749 | -44.77742 | 2024-10-11 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28979d5f-3cef-37f8-95f9-d7144e7a3594 | -8.07981 | -44.78328 | 2024-10-11 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 01c8f1a7-0c3f-3d07-aefc-bb7cdbe3c081 | -9.5931 | -44.39466 | 2024-10-11 04:00:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cd6e4c64-6b36-374f-ab57-56a186907d03 | -9.58101 | -44.39745 | 2024-10-11 04:00:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3d4cbacd-088d-3fff-892d-61014ebffd5f | -9.57803 | -44.39223 | 2024-10-11 04:00:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a848a2bc-ff42-369b-8b99-2ee844e2971b | -9.57753 | -44.39441 | 2024-10-11 04:00:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9639de7d-74f9-3682-8197-a7736e8d1d22 | -6.19285 | -43.43198 | 2024-10-11 04:00:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0765f9b0-71f3-3d5d-862a-d49cbd514445 | -6.19211 | -43.43649 | 2024-10-11 04:00:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ab5d8caa-9e1b-3b97-b426-8276d50dc3bb | -4.93702 | -43.01006 | 2024-10-11 04:00:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9a1176f1-5991-3853-b65b-c965cbb6f16d | -4.93523 | -43.01185 | 2024-10-11 04:00:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e7f2d47-66ec-3a41-841d-0ed54b05d5b9 | -4.74531 | -42.92922 | 2024-10-11 04:00:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5584df17-e4c2-307a-ad7c-cbc4f21bb51c | -4.19671 | -42.999 | 2024-10-11 04:00:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e675584-9a2c-36b6-947c-7aa1afa62c1d | -5.07544 | -43.15237 | 2024-10-11 04:00:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0cc0afb7-9dba-387f-bab8-48c195ee85a8 | -5.07243 | -43.14731 | 2024-10-11 04:00:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35db0720-6ba8-3fce-8d55-de8099b8b34d | -5.07171 | -43.15179 | 2024-10-11 04:00:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6515b6f-a51b-3b27-b3d1-81ee9aa13a8c | -5.04788 | -42.97235 | 2024-10-11 04:00:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40528969-f30f-3f5f-8f90-d272e0a830fa | -5.04535 | -42.97376 | 2024-10-11 04:00:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7003470d-fa28-3608-8256-992427fcae8f | -9.34863 | -35.96779 | 2024-10-11 04:00:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 450a6e74-4405-3f87-8230-d55ae3dbc2c3 | -9.34544 | -35.96227 | 2024-10-11 04:00:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README35.md)
