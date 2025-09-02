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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b073246d-6554-3e25-9e8e-f5e7607b4d6b | -11.42517 | -55.18852 | 2025-09-02 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc50c148-3110-3ea3-9b50-a51908669ffb | -14.59794 | -48.0694 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1bd080d9-5993-3d20-905f-91b1cc49ff24 | -13.54335 | -46.98192 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8c174be-e87c-3190-9246-823ea7544010 | -7.59205 | -60.47943 | 2025-09-02 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c1de911a-7892-32e1-8031-b6961648b743 | -10.75882 | -59.84071 | 2025-09-02 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 12775354-109f-3010-8c7f-582c86e20bdf | -7.54846 | -61.32878 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 30100c62-b37e-39f9-aec0-c43dfa969c04 | -13.31122 | -46.846 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 252ce691-6b27-3e9b-a85c-c0f6728dcc6f | -12.98063 | -48.10394 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2c67c106-4980-3096-aef8-f928d44bdd94 | -9.32866 | -59.57212 | 2025-09-02 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc3a3c73-c5af-3d3f-9210-6a7371d991c3 | -10.29273 | -47.51861 | 2025-09-02 05:06:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 29a70355-33dc-3adb-aae8-c613cac9271d | -14.73159 | -46.74876 | 2025-09-02 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0399cc8f-477c-37eb-8884-2d2be5422298 | -12.93019 | -57.00029 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 90124a36-86bd-3871-8376-c803d367cd6b | -11.64577 | -52.04164 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 488ed059-b7f4-3daa-b310-3322e210ae1b | -10.28941 | -47.51971 | 2025-09-02 05:06:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4eefd8a1-aa05-397b-8128-ca7293f2c9ef | -13.33984 | -46.85125 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b0cb753-97c0-3d3d-9528-031f0f6ea7b3 | -14.72833 | -46.74888 | 2025-09-02 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa239d19-8029-3e24-ac7f-9d7e9c44f4b9 | -7.67263 | -61.08873 | 2025-09-02 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 96ba3d11-6cbe-32bf-a7f6-f57b650c29f7 | -9.61043 | -55.38185 | 2025-09-02 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a8ba0f4-96cd-388e-937d-fef94cef8b8f | -9.83796 | -48.61769 | 2025-09-02 05:06:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d608097-6e7f-341e-bb9a-67bd3caf154c | -9.75443 | -46.92229 | 2025-09-02 05:06:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e30486c-1554-3813-b799-27eb981eda04 | -11.432 | -55.18958 | 2025-09-02 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a412897-b5ab-3797-a504-60c9c045d4ea | -12.87191 | -48.04858 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e749f8b9-45b7-3abf-b83f-75c183d95377 | -8.66605 | -62.83623 | 2025-09-02 05:06:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf8d9a72-42e3-376c-b18e-04ad276f4f5a | -10.05226 | -48.14873 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c247295-4d20-33b6-b5a0-d089cc05dc5e | -12.57041 | -44.78684 | 2025-09-02 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae97bd56-d9d2-3648-b59e-70c5eecedd58 | -12.92183 | -56.94463 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cd8084b0-3766-3af6-ac7c-fbe6f0fb1202 | -9.33929 | -55.21522 | 2025-09-02 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4c707bf-bb30-33dd-8f8d-d2e4b675d362 | -12.76544 | -48.08976 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 97b2a780-9747-3daa-8423-6327932c44bf | -8.66242 | -62.83118 | 2025-09-02 05:06:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c1bb79f2-ba57-3f07-8c9d-56c8bce4156a | -6.98769 | -63.014 | 2025-09-02 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a010bebc-7b77-3b02-b3fc-22894bfa1165 | -13.31282 | -46.83214 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f3755461-903b-3ee9-97f9-df9eb934b7f9 | -12.86622 | -48.05047 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8e48ab5b-c114-3ad0-bf2a-ec5fa7203043 | -14.78225 | -48.18329 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 108202fe-ab4f-3d8a-b69c-c1b8fd867f20 | -12.37966 | -59.85199 | 2025-09-02 05:06:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 2902f2aa-0db6-3746-a50d-27342e96bb45 | -12.99165 | -48.10275 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ad92dceb-cd24-3acb-a132-30f300ef8ae2 | -10.05951 | -48.13318 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4bbdeb7a-bf4d-39fa-b99a-9fc1abae9425 | -12.61411 | -48.1886 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9a3f7925-c9a1-3d47-a9c8-2b0811bc6fc8 | -12.86667 | -48.04685 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a2a42d58-0044-30ff-a09c-02e6b00cb990 | -14.59569 | -48.04536 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3d7c8016-b64a-3ef5-9506-d2077a34c488 | -14.58768 | -48.06761 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e31121ec-1608-32db-9681-eb2d0ff8e91a | -9.43817 | -60.57524 | 2025-09-02 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 712cb853-6d73-3b27-aa78-685164b3e87a | -12.91962 | -56.93702 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fecb4aeb-ab50-31c0-b7e6-6070a88e8dd8 | -13.72615 | -46.93168 | 2025-09-02 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 71303322-5a75-3d74-a178-f66d84261741 | -9.84192 | -48.3148 | 2025-09-02 05:06:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7c23ecb4-3029-37ae-b9e7-44e215145237 | -7.66253 | -61.10024 | 2025-09-02 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4b26592-369c-3973-b458-fcec3c4ad499 | -7.45318 | -63.15812 | 2025-09-02 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79f09fd4-b772-3088-ba26-af9eb877a823 | -8.65447 | -62.60966 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eabb5383-a732-3fd0-a701-478464ecc33e | -14.61283 | -48.0416 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b3eab1ee-d014-3126-b197-4a16be2b281f | -11.97471 | -45.8781 | 2025-09-02 05:06:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6353701d-2a83-3c4d-bc3d-443216b87a80 | -12.80957 | -48.06852 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b3d04ac-26c2-384d-a38d-54d34f459b52 | -7.36413 | -61.65596 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b32d6187-0bde-3dbf-85d5-93b2b675a72e | -11.54856 | -44.84263 | 2025-09-02 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb8dd4bb-abe4-3a99-b628-8b278d88481b | -9.75995 | -46.92328 | 2025-09-02 05:06:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e606663f-ff16-3318-9287-5a951f401b9a | -9.44724 | -46.77419 | 2025-09-02 05:06:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b4642de-24f0-353e-96a1-8ea653be27bb | -7.53981 | -61.3309 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bb7bbece-ac69-31f2-bc4b-e74415a62e18 | -14.05491 | -44.55441 | 2025-09-02 05:06:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 60df50bd-79a7-37e5-8b4d-43b75f5ee05f | -9.72591 | -48.95897 | 2025-09-02 05:06:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f69cbfb-20b9-314b-b784-79825a40021e | -10.05267 | -48.14563 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd362a2a-745e-3253-a8aa-5f0cbc2bd4b2 | -12.9963 | -48.10954 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b3a05abd-cc49-3b0c-8ac8-aa79a11078e8 | -12.94635 | -48.08896 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3cc8054a-77b5-3bed-9476-5b7c55c2321c | -14.60302 | -48.07346 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4bc2b761-6944-3f17-ba3b-5e78850a070d | -11.65986 | -52.17764 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 721c7387-ff7d-3401-b34f-626817120e0b | -7.76675 | -61.19995 | 2025-09-02 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d6f2ce4-cdce-3454-9cdb-f437b2aca467 | -12.91688 | -56.95471 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 24878d97-564a-3aa2-8adb-66d6f835318b | -12.88395 | -48.17097 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b258f739-724d-3087-90cc-5f016e90100e | -9.44075 | -60.577 | 2025-09-02 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c57ad6ce-f8c6-367b-adf8-af504c01ad0f | -12.62094 | -48.17683 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7e489900-6bce-34d2-b3e7-5b96b27852d4 | -8.85977 | -64.22884 | 2025-09-02 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9022146c-76c7-3081-a970-d2a1169c6bb8 | -14.2729 | -45.25357 | 2025-09-02 05:06:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 49d0d2ea-0d89-35ed-b367-4c42ec49dc3e | -14.27345 | -45.24805 | 2025-09-02 05:06:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a51624e5-22ee-39d1-9835-8fa3302155e3 | -12.98282 | -48.10246 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 86c26877-04e3-341b-8140-7bd62eed9fba | -11.91601 | -46.45609 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3721d9ee-bb7a-3242-9788-6aa3c09c7224 | -9.84225 | -48.31235 | 2025-09-02 05:06:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bded654f-d93f-349a-aca3-add0c289fcf4 | -11.65648 | -52.20206 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| bd6b188c-4035-37eb-9782-4666f9967ef2 | -8.68921 | -62.39999 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b9364a8-6f6b-31e7-b530-1b703080c265 | -7.4774 | -63.82222 | 2025-09-02 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ce8b190c-ee91-32b8-93ad-8b45f6b86338 | -11.47691 | -50.48152 | 2025-09-02 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bad5929f-2066-31a7-8973-d5598959d7fe | -12.91136 | -56.94656 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea436ec9-a938-3065-97dd-5b1bfec30fb3 | -12.56385 | -44.78595 | 2025-09-02 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3869a71-d533-34ad-9045-c48d5807a77f | -14.59524 | -48.04948 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 34a6b6d1-53da-38fb-aa8e-10cf6b5a63ec | -7.07625 | -63.07492 | 2025-09-02 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70ae35c5-a403-3890-9494-1681a6ca4038 | -11.67979 | -52.15174 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 359de51d-3a16-369a-ac2f-b0552f718c01 | -10.83871 | -47.27867 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc67d18a-5d48-3b2c-9a8c-bc6f91d000cb | -11.88971 | -46.68029 | 2025-09-02 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91403b76-ba89-3769-804f-c8fbcd3252e2 | -12.64949 | -48.25051 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ad6dc7a3-7ad0-3377-b32f-67c2b813f978 | -12.6145 | -48.18546 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 52aa8c41-ab64-378e-a405-39850426fd2f | -8.82774 | -52.01184 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22cd7d6b-5a83-3e22-a042-ebe8b1bd1520 | -9.48595 | -46.51207 | 2025-09-02 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 22f34d77-ea0c-3e2c-a9bf-c8e56cc3f6c1 | -11.88923 | -46.68417 | 2025-09-02 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7dbeabd-13aa-3f01-a010-74a94b65cf0c | -7.70168 | -61.11032 | 2025-09-02 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f9a4f7e-b952-3fd5-ac9a-d9d0a6b1c4c9 | -10.05908 | -48.13647 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9e0ad3e5-ffe3-3bd7-80b7-68c21b63149a | -11.05549 | -52.06602 | 2025-09-02 05:06:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98e78ae5-c325-3828-863e-d1c2555f86f4 | -12.8104 | -48.06144 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aedacc8c-44cc-3648-824c-9851cfe9a5cb | -10.83488 | -47.4485 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8cfed1b-9a5d-34e2-8618-a4f0bc3659a0 | -12.94176 | -56.99129 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e03379e3-0ebd-3658-b689-b8cfa19d322d | -12.92688 | -56.99976 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1143fff7-5cd6-3107-aec3-d5c4654396e5 | -12.80465 | -48.06408 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6f1b3e1-0711-3f25-914f-81d4279af72c | -9.34492 | -55.22348 | 2025-09-02 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00c12f82-8230-383f-92a9-684e45400291 | -13.52967 | -47.00215 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19361545-f770-393e-b9c8-ce301ac0229e | -11.66288 | -52.18528 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |


[Clique aqui para ver as próximas entradas](README70.md)
