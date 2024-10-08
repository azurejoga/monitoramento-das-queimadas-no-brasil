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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43604e18-4d39-3d32-b0bf-906328f06ea8 | -23.3525 | -53.90913 | 2024-10-08 03:47:00 | NOAA-20 | ITAQUIRAÍ | MATO GROSSO DO SUL | Brasil | 5004601 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3796015c-3f74-3ba9-af65-41d0fdcc2f22 | -23.35073 | -53.9159 | 2024-10-08 03:47:00 | NOAA-20 | ITAQUIRAÍ | MATO GROSSO DO SUL | Brasil | 5004601 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 430ec8bf-f622-337c-9003-615d2f764ec0 | -24.24978 | -54.26468 | 2024-10-08 03:47:00 | NOAA-20 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 0f75abaa-b1f9-3768-a1a6-e7b7fd6d2606 | -24.24303 | -54.26239 | 2024-10-08 03:47:00 | NOAA-20 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 3a4e573d-8e7a-39b4-b907-c5266229d4ca | -23.90246 | -54.2327 | 2024-10-08 03:47:00 | NOAA-20 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f067b93d-96d0-3cc3-9cc6-4ad7cc9cf87d | -23.90073 | -54.23332 | 2024-10-08 03:47:00 | NOAA-20 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 445673fe-7c9e-36ca-86a1-8df3bbbb8357 | -23.90062 | -54.23983 | 2024-10-08 03:47:00 | NOAA-20 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 964f809a-2b0a-38b6-9a66-aa783728d3ea | -23.89884 | -54.24046 | 2024-10-08 03:47:00 | NOAA-20 | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| cafce357-7ee6-3c41-b7f1-925f25e38640 | -22.57454 | -47.12713 | 2024-10-08 03:47:00 | NOAA-20 | ARTUR NOGUEIRA | SÃO PAULO | Brasil | 3503802 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38e252ca-fe07-39ba-976b-4435c4678e66 | -22.5734 | -47.1326 | 2024-10-08 03:47:00 | NOAA-20 | ARTUR NOGUEIRA | SÃO PAULO | Brasil | 3503802 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3541d439-fabe-3508-bf52-2f374537205b | -23.45264 | -47.27543 | 2024-10-08 03:47:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 171530e6-5c90-3a77-8fc1-2fe142ceceaa | -23.44839 | -47.27549 | 2024-10-08 03:47:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| fb4f8ec7-e2ce-38ce-989d-1baeaa0c37ee | -23.44799 | -47.27403 | 2024-10-08 03:47:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bd3037d0-fd61-32ce-b7da-5dc1f1113041 | -23.33684 | -46.77487 | 2024-10-08 03:47:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b45092bc-7eb4-3181-a5bc-f9cb1f8ed38e | -23.33668 | -46.77132 | 2024-10-08 03:47:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6f5014d1-f23d-3aa7-826e-4368bcfb019b | -23.33562 | -46.77628 | 2024-10-08 03:47:00 | NOAA-20 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 46567fc1-82d7-3f97-8b90-0ae3829de1a5 | -22.80378 | -46.7571 | 2024-10-08 03:47:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 1c8d3f02-e985-359b-a4e0-6a662ba1f952 | -22.80283 | -46.76176 | 2024-10-08 03:47:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| f35c4d9c-b64b-3997-b5a0-0e7a6c18fd2b | -22.80182 | -46.7667 | 2024-10-08 03:47:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| b93f10da-7f12-3be0-b682-f769a6b1ff88 | -22.80167 | -46.75876 | 2024-10-08 03:47:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 189e9258-b618-3a7e-a2a2-c706b9eea5d0 | -22.80066 | -46.76358 | 2024-10-08 03:47:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 51189b0e-f4c6-384a-b1b4-f4c8f7331ede | -22.79961 | -46.76857 | 2024-10-08 03:47:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d3241748-7fd2-3ff4-be0a-9cf0377cb27d | -22.79821 | -46.76068 | 2024-10-08 03:47:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 19bbfb6e-63b7-3292-985f-52ecd261cdee | -22.7972 | -46.76565 | 2024-10-08 03:47:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| b8eb3797-a4d8-309e-949b-ffcc03952e52 | -22.79605 | -46.76252 | 2024-10-08 03:47:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| a8235db8-51d7-3439-a662-189fcb3f2a39 | -22.79501 | -46.76744 | 2024-10-08 03:47:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 05557e8a-842b-36e0-8b93-14be247e0d66 | -22.70877 | -46.66377 | 2024-10-08 03:47:00 | NOAA-20 | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 44812670-4aa9-3edd-9702-1512942f33fd | -22.58058 | -46.66178 | 2024-10-08 03:47:00 | NOAA-20 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 025f621b-5d5a-3ec0-b9d4-52bf143bcd7f | -22.57936 | -46.66773 | 2024-10-08 03:47:00 | NOAA-20 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| c5e82f09-525a-384d-a6a4-7ca36b7da7e5 | -22.57549 | -46.70144 | 2024-10-08 03:47:00 | NOAA-20 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4143ab1c-e584-356e-80e7-3f2eb917eae9 | -22.57473 | -46.6668 | 2024-10-08 03:47:00 | NOAA-20 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c96b7e9c-3034-3028-8098-1b9b1ccdbfa3 | -22.57312 | -46.69838 | 2024-10-08 03:47:00 | NOAA-20 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| f5fa4180-e1ce-358c-ad61-8c985ee2fe93 | -22.8239 | -48.42335 | 2024-10-08 03:47:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e094d4e-18a1-3169-999e-5dd0b0069e31 | -22.82325 | -48.42631 | 2024-10-08 03:47:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1c73a53-3966-30b0-8ea1-9c482f6ae4b0 | -22.65658 | -47.63118 | 2024-10-08 03:47:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 17b0667d-d71d-3a6f-ad36-e0d154a94cf8 | -22.65173 | -47.62983 | 2024-10-08 03:47:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 3216d71e-d9fe-36d7-b6f3-f1ff6ef350a4 | -22.64851 | -47.7171 | 2024-10-08 03:47:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d4a5d811-ce69-3b84-95ce-c7b9a7381a2b | -5.5716 | -44.8927 | 2024-10-08 03:55:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 5dc3ffb0-f41f-3675-9f38-e0445a57ce52 | -5.5718 | -44.87 | 2024-10-08 03:55:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| cda0465a-26e6-3de2-8974-24c026ce752b | -9.4087 | -66.5438 | 2024-10-08 03:56:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 4bfc83f6-5d97-3e88-a643-3da8a3be20f8 | -9.445 | -66.7289 | 2024-10-08 03:56:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 6a771266-c962-3a58-905b-8ec42088f0a3 | -10.6256 | -55.9154 | 2024-10-08 03:56:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| da671585-db7d-3033-a642-fcb8b59a0db7 | -10.8568 | -63.8988 | 2024-10-08 03:56:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 27badfbe-d7e4-3e1f-b1bd-1ae0473132fc | -10.8754 | -63.9169 | 2024-10-08 03:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 797c981e-aa00-3f06-bb60-eb39ba57e9df | -10.8755 | -63.8979 | 2024-10-08 03:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| ccd3c7c2-0697-3cb0-a957-4f8c64444857 | -10.8941 | -63.916 | 2024-10-08 03:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 2b9e68dd-588f-3209-bff4-cb1f4da4f277 | -11.2891 | -51.0697 | 2024-10-08 03:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 07a2df7b-d01d-3f66-a472-e3877a1d2491 | -11.3078 | -51.0889 | 2024-10-08 03:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 0637113a-f82b-32b4-ac73-069f1e5d1e80 | -11.3081 | -51.0676 | 2024-10-08 03:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 213.7 |
| 297967c7-74a2-3499-b927-0f0217b968a7 | -11.3084 | -51.0464 | 2024-10-08 03:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 6b0fb6f7-f189-3a50-b15c-1ce2232d8b69 | -11.5233 | -65.137 | 2024-10-08 03:56:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.1 |
| bb62a1a4-0555-3fcc-a35e-9312f565aeff | -12.1083 | -50.914 | 2024-10-08 03:56:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 9e3a5136-440d-34ff-b086-c06891882a78 | -12.1086 | -50.8926 | 2024-10-08 03:56:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| d213673f-9181-3a77-b7a1-b887feee70d8 | -12.5717 | -53.0753 | 2024-10-08 03:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 158.2 |
| 8cb5494e-6080-3182-8d9e-3a75d145176f | -12.572 | -53.0544 | 2024-10-08 03:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 148.9 |
| db2a03d4-bdbd-3a44-8cad-3b9b86c32721 | -12.5907 | -53.0732 | 2024-10-08 03:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 57d54fb2-7994-3c8f-86a5-35190a329473 | -12.591 | -53.0524 | 2024-10-08 03:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 09a439ec-14f0-3618-ab29-5e6c90d5602e | -16.571 | -46.4553 | 2024-10-08 03:56:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 1fb40985-1cc2-3ce2-9631-4db602900ef2 | -16.8048 | -57.4197 | 2024-10-08 03:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.8 |
| 3cfc077c-05eb-3d47-b23f-13231f180f25 | -16.9211 | -57.4881 | 2024-10-08 03:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.5 |
| caebdbe5-72e1-350a-86b4-9cc5bab2c03b | -16.9214 | -57.4676 | 2024-10-08 03:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.6 |
| 8e1b05ec-659d-34d6-8fca-3d2d0bc36dc8 | -17.1074 | -56.851 | 2024-10-08 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.3 |
| 5b64baa1-7f25-3144-b510-98be85f43f76 | -17.1175 | -57.4449 | 2024-10-08 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.1 |
| 203f5f86-b2a7-365f-b4f8-55b1b87871d0 | -17.1274 | -56.828 | 2024-10-08 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.8 |
| ea7a967a-8819-34cb-9d55-e659544727de | -17.1178 | -57.4244 | 2024-10-08 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.1 |
| e2e0f31a-4948-34d8-8499-bf018882a1ad | -16.9407 | -57.4859 | 2024-10-08 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.2 |
| 03451851-0cba-3a86-9f33-043c9bd22a66 | -16.9924 | -56.7003 | 2024-10-08 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.2 |
| ebc89a6e-bccd-3ac2-a671-5640cfd210d2 | -16.9927 | -56.6797 | 2024-10-08 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.8 |
| 0e8d573a-1825-3371-9f24-77857e189c83 | -17.0123 | -56.6773 | 2024-10-08 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.8 |
| fefe5478-5a56-3831-a27b-2b1b0790f7ec | -17.0982 | -57.4267 | 2024-10-08 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.6 |
| 2c228c3f-00cc-3d0d-bfcc-b4080c96106b | -17.0989 | -57.3857 | 2024-10-08 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.7 |
| 74b5bde0-660b-3166-9845-20d58d62b689 | -17.0992 | -57.3651 | 2024-10-08 03:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.8 |
| c051cd78-22a2-3e49-8d65-463f880c8b08 | -17.1471 | -56.8256 | 2024-10-08 03:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.9 |
| b6cee355-87f1-353b-b64d-58bbf3d448a8 | -18.5299 | -52.6424 | 2024-10-08 03:56:50 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 74.7 |
| df4e2bf7-7304-3ed6-baad-d59d4eb20868 | -18.5499 | -52.6391 | 2024-10-08 03:56:50 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 66741d88-c424-32f3-8d0b-6cb5b179dfef | -18.5504 | -52.6174 | 2024-10-08 03:56:50 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 74.7 |
| e6e1a5fd-ec49-3b3f-a069-75820bbba8cb | -20.3938 | -43.9412 | 2024-10-08 03:56:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 101.5 |
| 12c32a02-d9d6-3917-a6d0-361cccf0d5e0 | -20.4144 | -43.9356 | 2024-10-08 03:56:58 | GOES-16 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 120.5 |
| 286b0cba-52c2-3110-9b73-1690c8a0b2b0 | -20.37 | -48.86 | 2024-10-08 04:03:27 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2d851c3c-1660-388d-9031-8061f6d45abc | -20.37 | -48.8 | 2024-10-08 04:03:27 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 507a2cbe-e1c1-39f2-9bb3-8f3a01d49296 | -20.4 | -48.87 | 2024-10-08 04:03:27 | MSG-03 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b3dd41e5-ba90-3613-ba96-14dadb618c62 | -20.4 | -48.82 | 2024-10-08 04:03:27 | MSG-03 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 223b3580-1329-3908-8d6f-b248499adac3 | -20.34 | -48.9 | 2024-10-08 04:03:27 | MSG-03 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b6995b03-b7b5-3a87-8ff1-c5558ac40610 | -20.34 | -48.84 | 2024-10-08 04:03:27 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f60700d7-f2b2-313e-84de-7b0d0e930c2d | -20.34 | -48.78 | 2024-10-08 04:03:27 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ccb6a64e-5ce2-36a5-b1aa-bb13cd4531b7 | -20.37 | -48.91 | 2024-10-08 04:03:27 | MSG-03 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0c8a2f74-27a3-372f-bb21-b9b6b7c64627 | -16.67 | -57.13 | 2024-10-08 04:03:51 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e12418ed-1997-3f50-a451-b7469e0dcbcb | -3.9394 | -46.445 | 2024-10-08 04:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 77a74c96-e75e-30e6-be27-64c02d05f3ed | -5.5716 | -44.8927 | 2024-10-08 04:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 89b9bb28-52cc-3885-b2ee-a567ced744fc | -5.5718 | -44.87 | 2024-10-08 04:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| d90f1c7b-b9a6-3c16-955d-629bb1d5a03d | -9.4087 | -66.5438 | 2024-10-08 04:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| fccda55e-5598-3f0d-abfd-dc9a5c55c65a | -10.6256 | -55.9154 | 2024-10-08 04:06:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 351a3df0-5ab9-3edd-9bce-76ad67db990a | -10.8568 | -63.8988 | 2024-10-08 04:06:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 42.7 |
| cbe9fae0-9b8b-32d4-8601-6aa11af6e46a | -10.8754 | -63.9169 | 2024-10-08 04:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 71.1 |
| bbd61649-722e-3e1b-b69f-0636a394230e | -10.8755 | -63.8979 | 2024-10-08 04:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 22dd2473-e741-3a66-bb39-493ae347ab85 | -11.3081 | -51.0676 | 2024-10-08 04:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 4bb93ca7-5751-30b5-ba76-6227c6b7a8c2 | -11.5232 | -65.1559 | 2024-10-08 04:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 520e7a1e-37bf-3db5-9eb8-df7a13b427a2 | -11.5233 | -65.137 | 2024-10-08 04:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 05f6a2c7-1ed1-37f5-b90a-732a0b4e0df0 | -11.673 | -65.2062 | 2024-10-08 04:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 36.2 |
| b381d4e3-c076-3cc8-961c-73966523a009 | -12.1086 | -50.8926 | 2024-10-08 04:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |


[Clique aqui para ver as próximas entradas](README47.md)
