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

## Dados Diários - Página 167

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a566c98d-3a5d-31f5-b06f-ebc66d16a299 | -6.16662 | -55.47347 | 2024-10-09 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0615c49b-b936-3a2b-9c44-6e1029aafc13 | -7.16039 | -55.04457 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e54c4cad-4812-31fc-a1f7-ea5d4b9cad6f | -7.14031 | -55.02351 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c74a29c-0180-3f39-b14a-9245d3605eaf | -7.00785 | -55.32846 | 2024-10-09 05:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f99955b-c991-3806-a06a-86f7d69273dd | -7.00731 | -55.33194 | 2024-10-09 05:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad9a8ce6-b251-3490-80a5-c1afa056cc45 | -7.00454 | -55.32794 | 2024-10-09 05:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 983f214f-1450-325b-bfb9-6cb4991b3603 | -7.004 | -55.33142 | 2024-10-09 05:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f703af3-4df4-3de8-b9dd-7764cc8e289a | -6.87078 | -55.11831 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16a5cbf5-b704-35f6-b242-d1410b85a8f4 | -6.87075 | -55.31452 | 2024-10-09 05:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f0f6a73-e1f2-371f-8d1e-61abe82ea297 | -6.77199 | -55.49092 | 2024-10-09 05:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8103022-3cde-3880-a409-2d4d2676a00b | -6.63957 | -55.38118 | 2024-10-09 05:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54aecc7a-c400-3162-a35a-3fa6955652ca | -6.63572 | -55.38414 | 2024-10-09 05:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f790214f-9624-38d8-aac9-bc3fb56b3188 | -7.97766 | -54.83039 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64eeb11a-5b9a-3076-826f-69189842f73a | -7.97711 | -54.83395 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bd22628-8a30-3320-8335-c03ba8174b73 | -7.9743 | -54.82987 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a505d2e8-bb24-38f0-b019-427596646664 | -7.97136 | -54.78176 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddd68ed2-4a37-3146-86ac-bd2eeca61f99 | -7.9704 | -54.83291 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9af3e43-9d88-3e14-b8f0-9e1e052d7fc7 | -7.96985 | -54.83648 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb7e814b-5b51-3f66-8550-c3767a30a25d | -7.9676 | -54.82882 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 892b8c37-198c-3d89-955e-3326c4912075 | -7.96705 | -54.83239 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a996c65d-43e3-31d1-8b26-3fcf9a526e8c | -7.96691 | -54.78843 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8d792bb-032b-3816-9dd3-f6f4e93fe8dc | -7.96568 | -54.75145 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16c32c1f-d981-309c-af74-a1b67bebdc3f | -7.96527 | -54.79915 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2abe1720-264b-3eb1-aca4-b883bdf3ec7e | -7.96472 | -54.80272 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14d71273-141b-3510-af32-bc7287337184 | -7.9637 | -54.83186 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b0a4697-ebb8-347f-b0e5-ee713502b840 | -7.96315 | -54.83543 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d81074b-780e-31ac-83eb-4f3e27b20117 | -7.96034 | -54.83134 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84fa822a-3dd5-3b71-9319-1966dfd8cb42 | -7.95979 | -54.83491 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 099dce98-2309-35cd-9687-ce7ddbea8d1b | -7.95903 | -54.77248 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39bbf7c1-f724-3360-b8fc-ab08a4d410c3 | -7.95811 | -54.74284 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d7c66b6-7a56-3784-8455-bba49bd21c57 | -7.95676 | -54.76478 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee00248e-ab55-37d3-887d-285efde25c67 | -7.95621 | -54.76838 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fceaaf45-aa02-3e96-a58c-847fa743aec9 | -7.95567 | -54.77197 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54911e13-bc73-3c89-9b78-f1333236bd62 | -7.95477 | -54.76439 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 155d9f01-9b6b-385e-9c08-ef5d8239b9c9 | -7.95421 | -54.76798 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83a9eb20-9d58-3531-a4a3-62b92611ed31 | -7.95308 | -54.75309 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57ab57fc-7c60-3d3a-a459-f54a9697ee5d | -7.95141 | -54.76387 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3515f168-8afb-3a94-b3e7-cf48e3315d77 | -7.88291 | -54.89591 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4af84480-5da1-379d-94e2-7265ee9ff4eb | -7.8823 | -54.87759 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ac2728e-d7ed-386d-a0d9-2ff1b22240d3 | -7.86336 | -54.88926 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f79ddd20-aa91-3261-aaff-20d125f6bcd8 | -7.86117 | -54.90348 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90c25663-9f24-31f4-8098-3001fa40b030 | -7.85113 | -54.90192 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4b7cd1b-978f-332e-b795-2134c0d0dba1 | -8.22575 | -54.89738 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00bad331-e340-3ca6-9d1b-a163c9f9acad | -8.22295 | -54.89327 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e4b838d-bcf5-38e6-894a-f4ab73dd40bb | -8.2224 | -54.89686 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 455eb331-e144-30ae-bbd6-f9a15c264c01 | -8.17813 | -55.05045 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbe589a6-5aeb-373d-bd14-c2486cbe5cb7 | -8.16532 | -54.86599 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db8075d4-03c8-39fb-9c9c-e649f17a8220 | -8.13845 | -55.17481 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93fbaa30-428b-39ff-9589-37ec5395bff4 | -8.1379 | -55.17834 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8818195c-5ead-33e5-9b46-1ef715ea1cf8 | -8.13457 | -55.17782 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2206a711-0fb3-3c95-b308-acb437935e32 | -8.13387 | -55.31471 | 2024-10-09 05:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf94945b-64a7-374b-981e-eee74caa008d | -8.10786 | -54.86796 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d952de34-5d3f-3b94-a2b7-570e1a4cb2b6 | -8.0735 | -54.77826 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5061af29-7202-35cf-992d-75f547aa467d | -8.06568 | -54.78441 | 2024-10-09 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5811750c-12cb-3a5e-87b4-40170c2e8158 | -1.63925 | -55.05471 | 2024-10-09 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffd7f002-9bb1-3786-a37b-152aae6c44dd | -1.63594 | -55.0542 | 2024-10-09 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb85bbea-f1b2-3a69-9eee-a76f630185bb | -1.46699 | -54.96112 | 2024-10-09 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4017553a-029d-3da3-b231-329fbf3f3768 | -1.2413 | -55.68267 | 2024-10-09 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ccde485-4fab-3dfd-9d66-3ca8ab6700ad | -1.24074 | -55.6862 | 2024-10-09 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb9cac98-7da8-32f4-95b8-041460029c1c | -1.24019 | -55.68972 | 2024-10-09 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e95ff26a-2558-397c-8809-892b07b699d1 | -1.2374 | -55.68568 | 2024-10-09 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 727cc1c8-04ab-3ea0-8b73-0a84c1c07446 | -1.23685 | -55.68921 | 2024-10-09 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cc2ab37-c25d-3c0d-8a3c-7787ab0858f5 | -1.17264 | -55.71174 | 2024-10-09 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4653ceb-8e0c-3304-aa0e-bdfc16dc32b4 | -3.56193 | -55.42368 | 2024-10-09 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc7adf27-2a11-3de4-a06d-44ed0114a1ba | -3.54225 | -55.48409 | 2024-10-09 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42e25b29-217b-3540-989d-536e163b494e | -3.54171 | -55.48753 | 2024-10-09 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f21f3a7-ff26-3347-8f82-6471ac6e42da | -3.53894 | -55.48357 | 2024-10-09 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89e59681-08ee-3459-994a-e0196bd81b60 | -3.46187 | -56.31847 | 2024-10-09 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1dc2817e-ec1f-3b2b-87b9-0922db34ea25 | -4.83365 | -55.97733 | 2024-10-09 05:01:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff571637-3039-3b75-a23f-0949d04846d2 | -4.71668 | -55.77083 | 2024-10-09 05:01:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 234e3c19-0be9-3c63-ac2f-3c66fc121c2c | -4.71338 | -55.77031 | 2024-10-09 05:01:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a70130c2-f587-3820-817f-680cd0ea0a17 | -4.60552 | -56.15152 | 2024-10-09 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e8991ab-1487-38b5-b20a-29b7933da4e6 | -4.60496 | -56.15501 | 2024-10-09 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed52dad4-0f8c-334d-a260-6595d6af3c16 | -4.36515 | -55.93227 | 2024-10-09 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55197611-b2f9-3145-b42f-69a6ec779500 | -4.17328 | -56.3496 | 2024-10-09 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35e7eaed-78ed-3ef0-ab02-ced9c01f709c | -5.12432 | -56.11604 | 2024-10-09 05:01:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85ab9284-578b-3da6-a4bb-c759d42c7724 | -7.20118 | -57.20293 | 2024-10-09 05:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b87a786-d5b6-3cd9-a5cb-32ebc3fbb50e | -7.10377 | -56.51191 | 2024-10-09 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29c3811c-477b-3b90-b5ec-315a7b8c9383 | -3.14837 | -57.4834 | 2024-10-09 05:01:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b3535962-e70c-3fe4-8a14-64770ba5562b | -3.04754 | -57.54807 | 2024-10-09 05:01:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab0a2aac-f5ef-3109-bba6-aea86e9399ff | -2.58916 | -58.06103 | 2024-10-09 05:01:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97b07aab-ff2b-378d-8a2f-ce9c0a0575f1 | -2.58508 | -57.40646 | 2024-10-09 05:01:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f305873-fe3c-306d-bf06-5c6914b3da55 | -2.58446 | -57.41034 | 2024-10-09 05:01:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bdd32f73-b7b7-36e3-b195-b3aa73dcaa0e | -6.16287 | -57.75153 | 2024-10-09 05:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d161734-2cf6-3f4a-aeb9-4f464f10171e | -6.15943 | -57.75096 | 2024-10-09 05:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80b687f9-4bd5-3239-8449-2b6ba5be0b2f | -7.19802 | -59.05875 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99a37b05-fe89-3cab-bf17-84dd1690f4c3 | -6.53085 | -58.42004 | 2024-10-09 05:01:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 544fc44c-58ae-31af-96af-31cc7fa06e6e | -6.52733 | -58.41945 | 2024-10-09 05:01:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a7547f4-86fc-3a20-a93b-3bf503156769 | -6.52668 | -58.42341 | 2024-10-09 05:01:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9f3b35fa-0eb2-3089-acce-cc080e682995 | -6.52382 | -58.41885 | 2024-10-09 05:01:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00b92977-2f6e-314f-bd72-19deec2d9b67 | -6.52317 | -58.42282 | 2024-10-09 05:01:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70aa435c-a7bb-3aaf-9772-8c26a5aebae6 | -6.52226 | -58.40638 | 2024-10-09 05:01:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6e70cf46-8321-30a0-88d0-65f6f22dd4c5 | -6.91322 | -59.03289 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bc38b9dd-2ecc-3540-b997-f96a363d3a40 | -6.83341 | -58.99135 | 2024-10-09 05:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb140844-f876-3523-8fcb-6d1c8c6b046f | -4.29155 | -60.01506 | 2024-10-09 05:01:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 864ab5b3-b5e3-345a-bf7d-f7660f347371 | -3.14966 | -59.11018 | 2024-10-09 05:01:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c259b27-1fe5-3049-9116-f3bfd440ebfd | -3.0164 | -59.09872 | 2024-10-09 05:01:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| edccee9e-cab1-3c54-b3e3-18c8aa1060ec | -3.01566 | -59.10338 | 2024-10-09 05:01:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 35b823bd-26e6-3520-9d08-c9a9a36d0a1b | -3.01492 | -59.10807 | 2024-10-09 05:01:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a892d4b3-c867-3a68-b7b6-45c04eb7b9a7 | -3.01186 | -59.10275 | 2024-10-09 05:01:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README168.md)
