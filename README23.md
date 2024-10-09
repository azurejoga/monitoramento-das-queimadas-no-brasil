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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd688ce6-ccff-380c-bce6-d11d3a16c0b3 | -13.94 | -44.53 | 2024-10-09 01:04:04 | MSG-03 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 93f5138e-b07d-3600-b5ba-89db3c88a55b | -8.48 | -48.64 | 2024-10-09 01:04:38 | MSG-03 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 50dfa811-dcaf-3b7e-b173-5dce2efe6a93 | -7.17 | -35.07 | 2024-10-09 01:04:43 | MSG-03 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c2d278d3-1630-3fa5-87bf-6b68db2f421c | -1.11 | -53.6173 | 2024-10-09 01:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| ed379fba-bf3b-317d-83a1-6a7b5aa03249 | -1.1284 | -53.6171 | 2024-10-09 01:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| a0a9cc52-c4d2-345e-85f8-8bf68179b2fa | -3.8007 | -41.6229 | 2024-10-09 01:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 70.2 |
| 9f5a0812-3c99-378d-9a85-2853a2c76197 | -3.8008 | -41.5989 | 2024-10-09 01:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 112.6 |
| 7c82b675-8eb5-31f7-abe7-1c34a966128b | -3.8196 | -41.5979 | 2024-10-09 01:05:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 86.0 |
| 33bbc32a-704b-3d05-813a-730f9ec8a0a1 | -3.9021 | -46.4689 | 2024-10-09 01:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 79bbc559-955e-3a61-bb57-74109472f6ca | -3.9023 | -46.4467 | 2024-10-09 01:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 86.9 |
| c94bb565-e69a-3e08-bd33-33333ae0ceca | -3.9207 | -46.468 | 2024-10-09 01:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 6390c244-3581-30e0-8c1c-c4feaa2bdeaa | -3.9208 | -46.4459 | 2024-10-09 01:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 43167607-6e71-3e3d-88a4-b6928a0ce27c | -3.9393 | -46.4672 | 2024-10-09 01:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 58.7 |
| b972a739-8a27-3d3d-b702-8f4e42d1a134 | -3.9394 | -46.445 | 2024-10-09 01:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 0457db48-1336-3a90-bd94-8ab754246ba8 | -5.4421 | -49.5559 | 2024-10-09 01:05:37 | GOES-16 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 415ae3b0-2046-3472-956d-8eef2cb00f61 | -6.7613 | -60.0751 | 2024-10-09 01:05:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 1cdaba29-ef31-3d2e-8fa4-4796b1fcdad3 | -6.7614 | -60.0559 | 2024-10-09 01:05:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 190.2 |
| 639c7617-7e42-33a9-ba73-b2cf003ec6b8 | -6.7615 | -60.0367 | 2024-10-09 01:05:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| b4189c3a-a270-3b1c-8cbf-4426d0800e72 | -6.7798 | -60.0552 | 2024-10-09 01:05:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 264.4 |
| 70dbda9a-39aa-34a8-94be-e71c49703360 | -6.7799 | -60.036 | 2024-10-09 01:05:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| c5949049-5e5a-3ef6-84e2-d8947bdbfa3e | -7.1714 | -35.0841 | 2024-10-09 01:05:46 | GOES-16 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 59.1 |
| 3a1acc26-c62a-3f8a-a940-95db273a44b0 | -7.1718 | -35.0566 | 2024-10-09 01:05:46 | GOES-16 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 129.5 |
| 11f4e1e6-4661-3e09-8569-a9c2520f478b | -7.1909 | -35.0541 | 2024-10-09 01:05:46 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 55.8 |
| 2e909035-5e84-318e-a6eb-5844f0f52fe1 | -7.1871 | -59.7893 | 2024-10-09 01:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| dd0b56dc-00b2-36e3-af09-2de825f351b8 | -7.1873 | -59.7701 | 2024-10-09 01:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| f4c6bacc-fe15-30ab-9b2b-311299bd5b68 | -7.2435 | -59.633 | 2024-10-09 01:05:48 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 24556f13-0d4d-3214-86b1-f3110e342ef0 | -7.2619 | -59.6323 | 2024-10-09 01:05:48 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.9 |
| bf89a8d5-7e42-3fe1-a452-7d214ae2fc69 | -8.3403 | -44.1195 | 2024-10-09 01:05:53 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 55.8 |
| e0dd4787-9dbd-3d4e-a45d-51916d7e02d1 | -8.3406 | -44.0963 | 2024-10-09 01:05:53 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 955420e8-853f-33aa-8a02-a220ffa50272 | -8.4919 | -48.6476 | 2024-10-09 01:05:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 177.6 |
| 48cf2f13-ce7c-37a9-81ac-360f6dff353e | -8.4921 | -48.6259 | 2024-10-09 01:05:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 128cfb09-50da-3c01-b8bb-ec43d322bdcd | -8.5107 | -48.6459 | 2024-10-09 01:05:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 142.9 |
| 3b54a3f8-1dc8-378f-97d5-7a368a89b68f | -8.5109 | -48.6242 | 2024-10-09 01:05:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 82.5 |
| e16fbc57-00e4-3f45-b1ab-95d36e3b7410 | -9.0543 | -63.2375 | 2024-10-09 01:05:58 | GOES-16 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 46291f89-229e-3998-abf2-0f2f590bd6fa | -9.1573 | -61.5803 | 2024-10-09 01:05:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| f6c4cebe-e259-33cf-8c5c-6100b0f31693 | -9.9105 | -58.1313 | 2024-10-09 01:06:03 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 6f7a1cdf-cf20-32bc-8b0b-40e906af0693 | -9.9292 | -58.1301 | 2024-10-09 01:06:03 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| db73fccc-c22d-346b-9a29-346b5d5bb377 | -10.3894 | -61.2502 | 2024-10-09 01:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 8cd55cd7-b879-3f68-abd5-14606aad3428 | -10.3895 | -61.231 | 2024-10-09 01:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 3adc4e7b-b7b2-30c4-a879-b167053deeb0 | -10.3843 | -64.8255 | 2024-10-09 01:06:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| f5eb70fb-27bd-323a-9644-f05610202211 | -10.4287 | -60.9979 | 2024-10-09 01:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| df6e81a2-46df-3973-b172-3e82ea6c8fa3 | -10.6068 | -55.9169 | 2024-10-09 01:06:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 19136635-3504-37fb-b063-f8e5e1629f00 | -10.6253 | -55.9355 | 2024-10-09 01:06:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 2ea1c1c4-d203-3ef1-8f62-2a3ba0afb51a | -10.6256 | -55.9154 | 2024-10-09 01:06:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 15f02107-5d8b-3ba4-ae5f-4545d174ff77 | -10.6258 | -55.8953 | 2024-10-09 01:06:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 3e179ba7-4d46-31ed-a124-eb4c2dd999a3 | -10.5943 | -64.024 | 2024-10-09 01:06:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 51707979-0e4e-3228-ab8b-5d071c305b3a | -10.8567 | -63.9177 | 2024-10-09 01:06:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 2657815d-0cd6-3d52-8a4e-7bef0d5ec542 | -10.8754 | -63.9169 | 2024-10-09 01:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 2d4647c1-49b1-3c1c-a524-7499698ed4a7 | -10.8755 | -63.8979 | 2024-10-09 01:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 34f59fc4-d9fa-34e9-9944-9702d608cb68 | -10.8925 | -64.1623 | 2024-10-09 01:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| f1dbf363-01fc-3815-9e15-bae878980e4a | -10.8926 | -64.1434 | 2024-10-09 01:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.4 |
| b31f1cc0-4036-3483-8473-a8c1c3798e47 | -10.8941 | -63.916 | 2024-10-09 01:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 78.1 |
| f5966729-06ae-3f2f-af13-2430e86a3577 | -10.9112 | -64.1615 | 2024-10-09 01:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 147.4 |
| 56436617-ffa4-3d82-9f4f-2f2aca51c239 | -10.9113 | -64.1426 | 2024-10-09 01:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 170.9 |
| 6d94fd05-3834-35a5-b17d-44f274436c42 | -11.464 | -49.4853 | 2024-10-09 01:06:11 | GOES-16 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 3f612cff-93b9-370c-be2a-cdee85b1194b | -11.5726 | -58.9619 | 2024-10-09 01:06:12 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 96885859-4d5a-3879-839e-88f13531fd7e | -11.5728 | -58.9423 | 2024-10-09 01:06:12 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 50.7 |
| e6b0e54b-bfb0-3dac-ac9f-cfb2f3796e06 | -11.6806 | -64.0312 | 2024-10-09 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 7d49df93-0cbb-3815-83d5-4eee819015de | -11.6808 | -64.0121 | 2024-10-09 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 30dfdbaa-959b-35f8-b8b8-2c5b4bdc3735 | -11.992 | -51.0553 | 2024-10-09 01:06:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 37909848-3972-30dd-bc38-5300d24e6cba | -12.011 | -51.0531 | 2024-10-09 01:06:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| edfaac7c-8ad2-3913-8aa9-63f25076ed16 | -12.7673 | -44.8904 | 2024-10-09 01:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 7d789367-2ce3-32f7-860d-9de763dcae20 | -12.6676 | -63.0819 | 2024-10-09 01:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 47e3a2b1-fe9d-3b85-a582-fb1b1187cb20 | -12.8589 | -62.8211 | 2024-10-09 01:06:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 5a7872d8-792e-3d42-a147-311c0f7c3b45 | -12.8591 | -62.8018 | 2024-10-09 01:06:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 153.8 |
| f8409f6b-17d7-3b15-bfba-243ce708c438 | -12.8779 | -62.82 | 2024-10-09 01:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 35877456-28f2-3038-81b3-7ad26559be50 | -12.878 | -62.8007 | 2024-10-09 01:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 317.6 |
| 90bfc14b-a7b8-3fe0-b303-720a5caa7a47 | -12.8782 | -62.7815 | 2024-10-09 01:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 85.2 |
| d871c690-3b45-3c79-b68f-c6e8e25e2085 | -12.9166 | -62.7214 | 2024-10-09 01:06:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.1 |
| a66bf8b2-afc0-39bc-8d90-53f6df187b4e | -12.9377 | -62.4697 | 2024-10-09 01:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 2bcba8f7-322a-3a62-8292-95aae0b3d88e | -12.9378 | -62.4504 | 2024-10-09 01:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 1682724b-046e-38b7-aa04-40b74c5892a8 | -12.9566 | -62.4685 | 2024-10-09 01:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 0fa36fb0-d158-3f85-a4ba-8ef3f8fb9bd4 | -12.9568 | -62.4492 | 2024-10-09 01:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 6e5dfbe0-7326-3372-8d8e-bb76d5472fe9 | -12.9756 | -62.4673 | 2024-10-09 01:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 3976b653-6e2b-3efe-ab59-f97a1f7b5b8f | -12.9757 | -62.448 | 2024-10-09 01:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 48.7 |
| ea74d3c7-993e-3750-942d-bd84241f3b9f | -13.3065 | -53.7227 | 2024-10-09 01:06:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| c6c7fd0f-85fd-3bcf-be06-a1daf6dc7b35 | -13.379 | -61.9194 | 2024-10-09 01:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 1c1f66c7-b3c3-34cc-9807-3d6303361d2c | -13.3978 | -61.9376 | 2024-10-09 01:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 66661bef-f74c-3fd2-b39a-8012f1602632 | -13.398 | -61.9182 | 2024-10-09 01:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 164.7 |
| ee416969-f53f-3412-a4a2-372914e4d22c | -13.417 | -61.9169 | 2024-10-09 01:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 9c6d6abb-b665-3b9a-8c5f-a5395d0a317b | -13.8759 | -44.5622 | 2024-10-09 01:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 48d71f1d-8a9d-32bd-99c1-f4a979758915 | -14.1197 | -44.9637 | 2024-10-09 01:06:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 82a52589-cbd2-36c4-9b24-0f53a6e9e309 | -14.1392 | -44.9603 | 2024-10-09 01:06:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 1ba78c0b-41c3-34df-bea0-25f2d270f1c5 | -14.1397 | -44.9368 | 2024-10-09 01:06:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| b8bff3af-9fab-394e-95e7-26b0af8c4308 | -14.1587 | -44.9568 | 2024-10-09 01:06:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 8f7454fd-8bf7-3d54-a4dc-cf290f331dee | -14.1592 | -44.9333 | 2024-10-09 01:06:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 3e26fb71-624f-3671-8928-5cec52861c71 | -15.5996 | -57.3699 | 2024-10-09 01:06:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 8f6e0ccf-ac89-3217-a188-90e4b4b6393b | -16.3988 | -55.9479 | 2024-10-09 01:06:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 50.2 |
| d4b825de-b131-35d4-9f8c-02f0480f68c1 | -16.4184 | -55.9455 | 2024-10-09 01:06:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 102.9 |
| 3790d421-9dc0-35e6-bd55-356e9b18aeb1 | -16.4187 | -55.9248 | 2024-10-09 01:06:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.9 |
| d1e8c06f-755f-36ae-90da-f8d72ff5968e | -16.4379 | -55.9431 | 2024-10-09 01:06:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.5 |
| 077aeaaf-9103-35c6-9382-1fc8eb9d1c07 | -16.4383 | -55.9224 | 2024-10-09 01:06:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 60.1 |
| b12caf89-e56c-3dc2-a783-d75ce4635365 | -16.7575 | -56.7081 | 2024-10-09 01:06:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.8 |
| 5f23392d-7409-38ca-a6c2-f56fe8c7e28b | -16.8743 | -56.7352 | 2024-10-09 01:06:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.0 |
| 41ba018c-59f6-3619-86f8-6564787e59eb | -16.8898 | -55.8039 | 2024-10-09 01:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 121.3 |
| fb268df6-d9ec-366e-ae29-967aa114d22e | -16.8901 | -55.7831 | 2024-10-09 01:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 112.5 |
| 1754b053-59cc-34f0-a506-f823d637a963 | -16.9091 | -55.8222 | 2024-10-09 01:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 49.6 |
| 8744fa5e-0b5e-355f-a7a2-5ded094a7579 | -16.9094 | -55.8014 | 2024-10-09 01:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 147.1 |
| f025aa63-a185-3a0e-bf92-4eb40806e8a8 | -16.9098 | -55.7806 | 2024-10-09 01:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 124.1 |
| cacb91c4-4704-3bf6-9160-3560d7ee9c69 | -16.929 | -55.7989 | 2024-10-09 01:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 51.8 |


[Clique aqui para ver as próximas entradas](README24.md)
