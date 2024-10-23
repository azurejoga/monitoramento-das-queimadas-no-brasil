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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3013d26-c6fd-37fa-bb15-92cc09194dbe | -2.73227 | -48.66916 | 2024-10-23 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c54013b1-ffbc-3e91-b887-fd489bd8f0b6 | -2.65768 | -48.12725 | 2024-10-23 04:51:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b129bd5-36de-36c6-ae83-fbd75984b6c4 | -2.51373 | -48.20915 | 2024-10-23 04:51:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d7f8f7e-c951-36ef-b0a1-6295a06956f9 | -2.4834 | -48.04558 | 2024-10-23 04:51:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 734b590d-21cf-3f4d-ba9d-b889216b2362 | -2.48227 | -48.04403 | 2024-10-23 04:51:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 165dab8c-3943-3c86-8da5-b44406e65ba8 | -2.48161 | -48.04844 | 2024-10-23 04:51:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3debbac-47d9-37db-87c1-bf30dca3bbea | -2.40643 | -47.64514 | 2024-10-23 04:51:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66f0a2a6-2572-3bae-bf61-ed285cd22746 | -2.65399 | -48.12663 | 2024-10-23 04:51:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aeeabb51-8f9a-3c62-854a-ae3f9db6a0be | -2.51673 | -48.21404 | 2024-10-23 04:51:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e2e0180-6e26-335d-a600-eb3d31cdc863 | -2.48271 | -48.04997 | 2024-10-23 04:51:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d97c6d50-237c-3091-b3b9-02379d0001ba | -2.45133 | -48.49443 | 2024-10-23 04:51:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 82909b33-ff96-3fe2-9b91-1c62cc2ddd82 | -2.43713 | -48.53902 | 2024-10-23 04:51:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6dd43f1d-f2a5-38a0-a8c7-b7984f7a936a | -2.43353 | -48.53846 | 2024-10-23 04:51:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9f0b9562-775a-3901-860f-fe154a0785b4 | -2.36147 | -47.98412 | 2024-10-23 04:51:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb719c2b-e23e-3c32-8575-aa7533ade203 | -2.35777 | -47.98354 | 2024-10-23 04:51:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e50f290-5a64-37e4-a120-af9f908e7ff7 | -2.23613 | -48.40837 | 2024-10-23 04:51:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4581f19-ede4-3f98-a005-13a00dbad548 | -3.4605 | -47.67182 | 2024-10-23 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d95f90b5-6a62-39d6-8870-2fef23918181 | -3.13956 | -48.75158 | 2024-10-23 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40580ae0-2b50-313a-a7c0-098b658d9556 | -3.00992 | -48.75504 | 2024-10-23 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f9205294-a26a-359a-a0db-7c92c3ce1894 | -2.96413 | -48.00558 | 2024-10-23 04:51:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 32a6f3b4-0296-3faf-b912-328fe35cdd3e | -2.9604 | -48.005 | 2024-10-23 04:51:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 37c40b2d-c1af-3f7f-9c27-39eec9022579 | -2.18427 | -48.81856 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 621dda16-6d67-39cb-82f3-a64e2dc0d66b | -3.40317 | -48.95219 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9b19968-39eb-3924-9977-844015c7e028 | -4.54624 | -48.83292 | 2024-10-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb017c33-ffbe-365b-ac9c-da9a1a8cee74 | -4.49462 | -48.11091 | 2024-10-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 929792d8-6e65-354f-9419-301aab9ef0b4 | -4.48706 | -48.10975 | 2024-10-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d7dfe91-c9dd-37d4-ae95-b4081ead1ee8 | -4.48636 | -48.11436 | 2024-10-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e6279be-5efd-31de-bfaf-831f924c6360 | -4.47054 | -48.11663 | 2024-10-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a9ca4729-9133-37c5-b8f7-691fcf101605 | -4.46607 | -48.12064 | 2024-10-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d40dcc2-1c44-300c-822a-4e3355e6c204 | -4.4066 | -48.83608 | 2024-10-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d251e54-4f0d-357d-937b-a7e09e56cbe0 | -4.40595 | -48.84027 | 2024-10-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e9693b8-59b2-3676-be04-4e76bd40d1ea | -4.40297 | -48.83553 | 2024-10-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| baddf04d-136f-32f4-a1d0-2ae56c166a1d | -4.37502 | -48.47468 | 2024-10-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 409c91d0-cfe6-38ce-a2b5-a6947c8bf6b2 | -4.37291 | -48.47215 | 2024-10-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ea52a5f3-7903-3b3a-ae3b-eb1939d1721a | -4.37224 | -48.4765 | 2024-10-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c2c686af-d295-3a1e-9845-f730d3fbeed2 | -4.37131 | -48.47415 | 2024-10-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bde16101-af2f-320e-8ae4-d851681cd2c7 | -4.37067 | -48.4785 | 2024-10-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9be44a5c-faf3-3aa0-8781-cba97bb0d5f4 | -4.36854 | -48.47592 | 2024-10-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c119d029-5999-3326-a35a-b2415e7e6297 | -4.36787 | -48.48026 | 2024-10-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56b2bf46-a749-3806-9001-74cea9178ce0 | -4.36724 | -48.60289 | 2024-10-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18bceddd-be6a-3cf4-9f6c-d231b083d160 | -4.35132 | -47.80616 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 23679fd4-8fa0-37d3-a4cb-1e893b599048 | -4.35059 | -47.81092 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 448c7bad-df86-3265-86f9-cfdc6162852c | -4.34569 | -48.6238 | 2024-10-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c028d5f6-4776-3c21-a09c-d72eb91b6ffc | -4.34269 | -48.61891 | 2024-10-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2512eefd-cbc0-3c89-baa6-656b2415c18e | -4.34202 | -48.62325 | 2024-10-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5ffeeead-3fb2-3602-8496-82af0b590eb6 | -4.33835 | -48.62271 | 2024-10-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2fb83c4d-ad96-3ce7-a31b-051e4cb2614f | -4.28507 | -48.62767 | 2024-10-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a70cb756-8f24-378e-8f44-c79ee718779f | -4.24556 | -48.34638 | 2024-10-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21c62a01-22aa-3d3b-ba0c-939c9d398e35 | -4.24185 | -48.34573 | 2024-10-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f790640d-508a-35b2-a64c-3fc0fcee8dab | -4.24119 | -48.35009 | 2024-10-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82452d8b-0a46-3bb9-b5db-a8e3391a7d6c | -4.23943 | -48.13361 | 2024-10-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a5c3f29-c6ea-3e5b-b106-16c251f1eb7f | -4.18432 | -47.98536 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 54864be6-1ee1-37c7-8868-f5af511a3fee | -4.18362 | -47.98999 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 2f08a390-3019-3686-a9d8-ea808e9bc2f8 | -4.18292 | -47.99462 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 952557bd-1be1-382d-8fef-f57f7933a011 | -4.18053 | -47.98476 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| d23088e7-b6b8-384e-a08d-60a282e42f03 | -4.17982 | -47.9894 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 13f529ca-c2c5-3abd-9988-9fac6226be46 | -4.17674 | -47.98413 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| b8aed6f3-5c0b-3f80-855e-0d7f5bed9869 | -4.17604 | -47.98876 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 80c843c8-12a6-3d63-b771-6c484e3e4ed1 | -4.11116 | -48.24055 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63be5db9-219f-3dfe-8bbf-84c80ed5cf0b | -4.10675 | -48.2445 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5b4aefaf-865b-39e9-8d9e-f4bf4e9d97bf | -4.09997 | -48.2387 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa1bbdbe-3504-3eae-bb42-7264137bc3a9 | -4.09929 | -48.24323 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a3f98d09-6f76-34bf-8127-42f735ea1044 | -4.08276 | -48.27731 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41c4db21-0254-3f8c-9543-300969760100 | -4.08129 | -48.27497 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2f745c5a-1f39-3240-852b-fe1a991a2016 | -4.0806 | -48.27942 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d3947cf9-4a28-3929-a067-c12cdd07699c | -4.07904 | -48.2767 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| cb5c31ab-f056-38c0-8229-97c1c72e0536 | -4.07757 | -48.27436 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c11e621-0105-3dc4-b209-e2a9f1d9097d | -4.07051 | -48.24594 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96eea2ab-321f-3a45-b679-772c5cbe6783 | -4.06679 | -48.24532 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92b29911-fabb-3048-9e2a-b462584dcde0 | -4.06609 | -48.24983 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e7034d7-2b6a-3a69-b71c-3bbddcacedd7 | -4.06521 | -47.92645 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e2093dee-43d4-357a-935f-7ae5e1b28e96 | -4.05005 | -48.10378 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d8f9e53b-452e-355d-a4e3-5e3bdf3b16f7 | -4.04934 | -48.10843 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7edf5fe0-1c5d-3e48-af83-ba61c31b9393 | -4.04628 | -48.10325 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6d12e1ef-0894-39ca-9028-acab7e985a65 | -4.04557 | -48.1079 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 115f3537-07fd-34f4-ba5d-b80cc9c739a3 | -4.04488 | -48.11252 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| bf77d807-1fd0-37e6-bf53-2e8a8694cdfd | -4.03819 | -47.95103 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c5b20ab5-8f18-3453-aa2b-776dd573630b | -4.0375 | -47.95567 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cadecfb2-730f-3956-9701-022a52cc048d | -3.99956 | -48.95684 | 2024-10-23 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45d1faeb-875c-3059-8fcb-0d07a4ddb67b | -3.97889 | -49.02089 | 2024-10-23 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| eb5a88f0-a15a-3ea7-a59a-fa4686e292cf | -3.97827 | -49.02499 | 2024-10-23 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 3803f1bc-1174-33d9-8ba5-02da74976fa6 | -3.92916 | -48.33543 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c0bed99-a9d5-3bc1-99b2-bbeedc7f133b | -3.92546 | -48.33484 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1db893b6-b930-3e38-99b4-ae3a4a2d8706 | -3.92478 | -48.33927 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae665349-08b3-3151-b38a-49fc727ea064 | -3.91639 | -48.36927 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c4363f9b-2b9b-3d3d-a96e-e98d4ade899f | -3.91269 | -48.36872 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cd285cc3-9b37-3309-a358-b27d8585a19a | -3.91063 | -48.33253 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9c198f60-c065-3460-9c52-cfea319799a6 | -3.90693 | -48.33193 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ab7357e6-5fbe-3b38-97fd-987361b872a3 | -3.90322 | -48.33135 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| acead213-f5a1-3b8b-87ca-2a7221181b76 | -3.90019 | -48.3263 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7a73361-5955-3d70-9bc9-88a21b7de27a | -3.89951 | -48.33078 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1589c4d6-24d9-31c9-a4cd-ec37b38968fe | -3.89648 | -48.32575 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a35df40f-1820-3049-854b-dac00d1a95d0 | -3.89581 | -48.33022 | 2024-10-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d2b8b22-a856-35a9-836e-c2497b896347 | -3.80593 | -47.79877 | 2024-10-23 04:51:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20aa52a8-c85e-3b4c-8d25-0b104f2315e6 | -3.80521 | -47.80345 | 2024-10-23 04:51:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2090d3a-bc49-3b8f-a1f2-236a9155b2a3 | -3.79901 | -47.79288 | 2024-10-23 04:51:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9b665df-1c61-3a8a-a682-13981c1a1643 | -3.76934 | -47.73038 | 2024-10-23 04:51:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5647dca5-ec6d-3c1e-becb-d4822353eb88 | -3.72846 | -47.82044 | 2024-10-23 04:51:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5523c908-3b89-3fd3-a73d-f364c7417907 | -3.72534 | -47.8152 | 2024-10-23 04:51:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5cc527ee-e2f3-3740-85f9-11953e22a9c9 | -3.69269 | -49.04719 | 2024-10-23 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README37.md)
