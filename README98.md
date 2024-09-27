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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 068d50eb-d092-376e-a35a-88231e274e09 | -12.54802 | -53.50683 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b136cf73-0a1e-300a-9d83-b9bcab1519b5 | -12.54384 | -53.51025 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a638443f-f851-3a5c-83b5-62466dcbab26 | -12.54316 | -53.51425 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f145b41c-44a9-3b92-adc0-73bb52a61f8f | -12.54303 | -53.49356 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ac0df09-a1d7-3d64-a64b-573ba37f42d9 | -12.54235 | -53.49759 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f2cad9e-afb0-31b2-a14f-908dcb7f4931 | -12.54032 | -53.50964 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 955c3fed-656d-3a55-a130-7fdfb23db655 | -12.53965 | -53.51365 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 28453b39-51eb-3c87-8c9b-c98cdea09c16 | -12.53953 | -53.49295 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dff116fc-d9c4-3ae6-8a23-29945193d8b6 | -12.53897 | -53.51766 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8337570c-7c16-3267-9d2d-7eec3f853094 | -12.53601 | -53.49236 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d79d49df-c8df-3bf8-9b34-7deecb427696 | -12.51983 | -53.48133 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41fd5eef-86ff-3cba-9080-20bc082272cd | -12.51915 | -53.48536 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b2095b6-9af5-330d-a154-a2249da6d5b2 | -12.51902 | -53.48203 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 30c55913-60d9-3b86-b3f9-a46243a72025 | -12.49512 | -53.4738 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c8778666-caff-38a8-8f41-da43a00882c2 | -12.49446 | -53.47783 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 512fcea4-c666-3ce3-ad02-4fccea722697 | -12.49398 | -53.50251 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7db854ad-d9cd-3a26-88fd-7411b4046f47 | -12.49162 | -53.47319 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ee7e2b1f-5b8c-39b1-8953-c06636b2ea3c | -12.49095 | -53.47721 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b440eb46-c979-35e3-9760-b9cfc41a15b9 | -12.48562 | -53.5093 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3e18b312-7f04-3f26-81bc-040394fc79c2 | -12.48277 | -53.5047 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f741adc4-86fa-3cfb-8208-23f429b1ffcf | -12.48211 | -53.5087 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a922766-7978-3c63-b835-54fbe85bfe32 | -12.48144 | -53.5127 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 178badcd-3495-3871-b4a9-0a1f5ab7ddef | -12.48078 | -53.51671 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28573cd6-f0db-33fb-abe3-97e2b0fe7796 | -12.48011 | -53.52074 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 240412e6-166f-3d2b-851c-2fdc3283f297 | -12.47876 | -53.52881 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55c2ab55-55aa-3342-b5f9-e266aa8b5239 | -12.46991 | -53.47354 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e93018a8-e976-3650-9915-5ca2f542c515 | -12.4664 | -53.47293 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb45fbd0-3638-344d-9832-16512aecb037 | -12.42982 | -53.45435 | 2024-09-27 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e037ea17-4318-3fbd-915c-aa6c8fd779d4 | -6.25463 | -53.27596 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a16243df-101c-3911-b9b6-26c1a0e771df | -6.23492 | -53.34779 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bcf5874-cff5-3a31-9626-25c0ba356878 | -5.81927 | -53.87875 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 374de9b2-3084-3e0c-9f43-8c7968b3b0e1 | -5.8192 | -53.87664 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e3e6245-af74-39d8-b203-79e42704e6b1 | -5.81537 | -53.8781 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a88cc0d-b860-3047-aab4-9bb2c2e59a8b | -5.81529 | -53.87599 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a47fe52d-1e91-3dca-9271-a230b1256502 | -5.73616 | -53.6931 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6433149-d1f2-3fc8-9258-fe659e5601d6 | -5.73315 | -53.69586 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7579ace9-cf79-30ff-a725-9e0393158dea | -5.73152 | -53.69727 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b69e84b-399f-3a1a-8140-529ac250e752 | -5.3956 | -43.42736 | 2024-09-27 04:42:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| f4b9b92f-d25a-3db2-b235-ba14fb05d8fa | -5.02201 | -43.78569 | 2024-09-27 04:42:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 8ab716f5-b3b5-3cfc-8452-c53036fa0ee0 | -4.78776 | -43.70569 | 2024-09-27 04:42:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 1c391c88-23a9-39d3-9585-50d6ec107a88 | -4.78107 | -43.7122 | 2024-09-27 04:42:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| ff8a2346-c920-3e8b-bc5e-edeaa754599d | -6.57287 | -44.16846 | 2024-09-27 04:42:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| a759d830-e6a2-3107-8df0-b55949b50c13 | -6.08857 | -44.69482 | 2024-09-27 04:42:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 1b0891b7-ba18-386a-b508-585839798afc | -6.05861 | -44.02488 | 2024-09-27 04:42:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| ff7a7252-8be0-3274-9f9b-81de3e08bb26 | -3.21077 | -46.77705 | 2024-09-27 04:42:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 127.5 |
| efc33c56-3315-39e1-9306-5c1c89c169f6 | -3.20958 | -46.78461 | 2024-09-27 04:42:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 58cab594-e654-30fd-8260-c775d526cf7b | -6.87194 | -42.84192 | 2024-09-27 04:42:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 32.5 |
| 5df5b725-642b-34b9-8c2f-edff7df3bc92 | -6.29399 | -42.49821 | 2024-09-27 04:42:00 | AQUA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 1aea4558-1fc2-379a-aa50-5097191050e6 | -6.09749 | -41.78459 | 2024-09-27 04:42:00 | AQUA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| c013effd-b117-3801-b47d-40ae04e28e51 | -5.4085 | -43.41568 | 2024-09-27 04:42:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 37.1 |
| c1efd293-c5fa-3310-9d5b-9252e69e1d07 | -5.40521 | -43.43594 | 2024-09-27 04:42:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| c513cf41-afa6-337e-91c5-e3a977490346 | -12.67874 | -54.65874 | 2024-09-27 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 22fe4777-a8cf-3460-8eb7-8c9f134fc23e | -12.67796 | -54.66323 | 2024-09-27 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b5ed67be-9f20-3796-9ba9-6331cd0b8c5e | -12.67503 | -54.65809 | 2024-09-27 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d3fe62e7-08d6-316d-a4ef-e0483f94aa0c | -12.67425 | -54.66257 | 2024-09-27 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 860837a5-e0b4-3dc3-80a2-7cc7f60817ef | -12.67132 | -54.65743 | 2024-09-27 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 3746e1f6-3ab4-3261-bcb2-c31a90a49907 | -12.67054 | -54.66191 | 2024-09-27 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 939bd54e-4a65-3e65-ae5b-179131fd5bcf | -12.66976 | -54.66641 | 2024-09-27 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6a11f264-b2a7-3aeb-bece-d37be7eb04db | -12.66683 | -54.66126 | 2024-09-27 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bf2e8c96-4cba-338d-8088-9d728c4438ca | -12.66234 | -54.66511 | 2024-09-27 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| eb81cb26-4a5d-39ca-b4a7-4da643d2d79c | -17.11569 | -56.19423 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0f851816-eacc-39ba-a3ce-1adb50b80b57 | -17.11482 | -56.19908 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5992a964-7f7e-3261-b34c-7ea007682a31 | -17.11395 | -56.20394 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 948b9bd7-daa4-39d4-b7d4-255038fd122a | -17.11365 | -56.18379 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c5f007c0-3af7-30d3-a4be-de903b633b7b | -17.11277 | -56.18864 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 20847904-4569-36de-a8c2-0da38e524170 | -17.1119 | -56.1935 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8406f3ff-6c99-358e-8c48-b1808cb7637b | -17.11103 | -56.19836 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7fc36090-6c28-3bd1-9a07-849f7a668aaa | -17.11016 | -56.2032 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e4fd9813-1bc1-3b04-896f-a1cb3126b67d | -17.10898 | -56.18792 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fd1d17cd-0985-38c4-8258-87d83b344760 | -17.10811 | -56.19278 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a45490e0-9dbe-335d-8716-86f7da39f919 | -17.10724 | -56.19762 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f7e282f4-3e7c-3836-88f3-2836651222d6 | -17.10637 | -56.20248 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 614c38f4-fac6-35aa-80fa-3199188a1c3a | -17.06127 | -56.15134 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 21abe3f0-26f2-3048-8b58-859593b32eff | -17.06042 | -56.15617 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| dc1a787d-149d-3992-875b-2fcbb06bd7f2 | -17.05663 | -56.15545 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 35e8ea15-fdbc-358d-8c24-6f15bc18e021 | -17.03425 | -56.17121 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a890ec8b-401b-3b15-8028-0dafb5a7f856 | -17.03339 | -56.17607 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 78eaa348-27f1-3648-87f3-10dbfa8d828e | -17.03132 | -56.16562 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f8db2f2f-5473-3d37-a52b-745503aab779 | -17.03046 | -56.17048 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 23249423-cb5b-3d25-abe7-b5b8e61bba1f | -17.02959 | -56.17533 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e3a00e2c-8f5a-3967-88dd-1601ed1c35a0 | -17.02753 | -56.16489 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7d8375d3-32ba-348c-9901-3da5f004f7f7 | -17.02667 | -56.16975 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5e3a48f9-741d-346d-8149-d4e124c888e7 | -17.0258 | -56.17461 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9b9b983e-b584-3d45-878a-e69b4c5e74dc | -17.02374 | -56.16416 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c5024851-5e8b-3d36-828a-35d195461ce7 | -17.02287 | -56.16902 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5ce8c3f3-4634-3179-ae80-551187a46ecd | -17.02201 | -56.17388 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| da62c5b8-4839-3a84-926d-96955f6d72c7 | -17.02081 | -56.1586 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| afba276d-f08f-32f1-aa17-6362c9520682 | -17.01995 | -56.16344 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 78b3f620-cfa1-3502-99f6-4134107c6a2c | -17.01908 | -56.16829 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ba121733-6589-3b93-afba-aec0881c5a86 | -17.01822 | -56.17315 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9d24e986-3d01-38f1-816c-ff1528686141 | -17.01616 | -56.16272 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8039f5ba-8e02-33f1-b3f0-9f41181ea92e | -17.01529 | -56.16756 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 711bd5d1-ced8-3094-a3e2-1c7161399319 | -17.01443 | -56.17241 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| cb1f4567-2b29-3f9a-bd28-a55b3574235c | -17.014 | -56.3294 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d2624930-6548-3916-bd41-24958199f190 | -16.73742 | -55.55141 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ab3f53ef-6656-3c4e-8977-02b6975c35b2 | -16.73663 | -55.55596 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| da957c09-7be3-3df6-8d53-68e4e95f8a9e | -16.73452 | -55.54619 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 235fb2d2-be5e-3bb5-a35a-360a23e04af4 | -16.73373 | -55.55073 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 63940882-98dc-37c3-8197-d032d03fd436 | -16.73162 | -55.54098 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| f5f79e92-e6ae-3896-a226-3e54c87eec5d | -16.73083 | -55.54551 | 2024-09-27 04:42:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |


[Clique aqui para ver as próximas entradas](README99.md)
