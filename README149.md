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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9a6a5a0-e5d8-3041-bab9-e21e5366353c | -15.85348 | -57.38101 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73d48ca8-3dba-3a3e-8376-6f775c00ab8e | -15.85174 | -57.3918 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c98249f-9ebc-3b16-be8a-9a36bdd0bed7 | -15.85096 | -57.41786 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f9764959-ba6e-3eca-a14f-04bc4425b3d5 | -15.85036 | -57.42159 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2688287b-ec1f-3cc3-8755-01d8882c5aeb | -15.84958 | -57.38399 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6af2a656-7b35-3923-b30b-25ccd28d3e78 | -15.849 | -57.38757 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d319641b-cfe4-37b4-8ef9-ad01ed04c844 | -15.84882 | -57.40988 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dda3369c-bcd1-36c1-a293-acc63fa9a569 | -15.84841 | -57.39121 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 62fd47a0-42a4-3c83-9ca7-f6fe7da3b684 | -15.84763 | -57.41726 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| c22ec078-bacc-3ab2-a32b-328699aed125 | -15.84703 | -57.42098 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0aedb7ec-d585-3be4-ac36-c68aa652398e | -15.84549 | -57.40931 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 578dacca-4fad-3e9b-b15e-ba5342546651 | -15.8449 | -57.41294 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 880ad300-1fb0-3829-bb89-cc50d12dd48b | -15.8443 | -57.41667 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 83c1a957-918e-302f-a104-aef86ff2b96c | -15.8437 | -57.42043 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e4c26b37-9ccb-331b-9dc5-613c2b89a8f1 | -15.84157 | -57.41238 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb94437e-6ff9-3ccc-91ef-b44e0e249fb6 | -15.84096 | -57.41613 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 410dec89-cc35-30a9-9ddf-0f330585926e | -15.84036 | -57.41988 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 18cdff18-8db4-3cde-b681-f9d20c5c937e | -15.79193 | -57.78202 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60233652-1583-3901-aa4b-7a95f65fad98 | -15.78857 | -57.78143 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bae45749-6bcb-34c8-9e60-756f42d5f542 | -15.74242 | -57.78868 | 2024-09-26 05:01:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3e76406-7040-3b20-9cff-833c54822169 | -15.73966 | -57.78439 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2d07832-206f-3f4b-bb66-b975ddde4f84 | -15.7363 | -57.7838 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c541fd66-0def-33f0-a7f5-d5a726e309fd | -15.73569 | -57.78751 | 2024-09-26 05:01:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f323cb63-e74a-3927-a049-679b264d4d26 | -15.73294 | -57.78321 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48c1458b-0ae6-3fe5-821a-5d3f9292f5eb | -15.73233 | -57.78693 | 2024-09-26 05:01:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f38878f6-4bbb-38aa-83d0-a8109e276201 | -15.73172 | -57.79064 | 2024-09-26 05:01:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bf51947a-6ad0-3815-ad8b-7374cc1ee9a3 | -15.72957 | -57.78263 | 2024-09-26 05:01:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90604801-5d8d-3dee-8a5f-11acb3552682 | -15.72896 | -57.78634 | 2024-09-26 05:01:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b4a89d4-d788-39e9-afd5-1531936e4186 | -15.72835 | -57.79006 | 2024-09-26 05:01:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 869f4e53-c29d-3654-835b-bd38c912985b | -15.72621 | -57.78205 | 2024-09-26 05:01:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf90a753-1a6d-346d-b5e7-a09445103357 | -15.72223 | -57.78517 | 2024-09-26 05:01:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b8a1e3f5-1f4e-3e73-8b73-bd30afc672a5 | -15.64746 | -57.78768 | 2024-09-26 05:01:00 | NOAA-21 | CURVELÂNDIA | MATO GROSSO | Brasil | 5103437 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c751e51c-e14d-3fb1-89e8-2a1a6ede5d60 | -15.75373 | -57.783 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 582aa285-9cb3-3a3b-832a-77fac02f1676 | -15.75037 | -57.78242 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ee473d75-3f53-3f94-b254-112535817f78 | -15.73905 | -57.7881 | 2024-09-26 05:01:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9213602a-5c59-3155-8f48-16a107fe271b | -15.7256 | -57.78576 | 2024-09-26 05:01:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8255d129-012e-3750-8a20-623282858419 | -16.35778 | -57.67443 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 4e0f358d-0c36-3c6e-a77e-1fd49605e92e | -16.35718 | -57.67812 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| f8777f79-3b3f-388e-aed3-470c742ea9b5 | -16.35502 | -57.67023 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 28b89053-d157-3747-8244-f8359cb12f17 | -16.35383 | -57.67759 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 70ac2f56-ebbd-326b-899e-6fb2e8adfb00 | -16.84263 | -57.7053 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0e817f2e-3a0b-3a43-b35a-78ae785e2a99 | -16.83869 | -57.70838 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6de4cfd1-c254-3b26-a839-4987f438c04a | -16.83535 | -57.7078 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 707c7cb5-f950-348b-90cc-cc8804b9bef1 | -16.64081 | -57.54274 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e64a6a8d-a721-3d04-a0bf-f5d4defbc3e7 | -16.84203 | -57.70897 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a8cc197a-5f23-3e7b-b179-b5b485faef82 | -16.64747 | -57.54388 | 2024-09-26 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 7c40bfd0-1d06-3dd6-9c6c-4f6ca691a7b3 | -19.14737 | -57.47568 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 2a06244a-7000-30b9-8c67-dcdf9de32f06 | -19.14406 | -57.47511 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| cb85fba0-5fe9-3276-887a-c3e09e5126ba | -19.14076 | -57.47453 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 76a31b7f-83f5-3834-a0bc-61ed04b33322 | -19.13558 | -57.50718 | 2024-09-26 05:01:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 84e5aaaa-f7d0-35e4-9431-5175fca4fc20 | -19.13498 | -57.51086 | 2024-09-26 05:01:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1bb83400-44cf-36c0-8c09-270fdcf722cf | -25.19707 | -49.32407 | 2024-09-26 05:04:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a4f595f7-a1af-3d80-9e97-3e811cf9e761 | -25.19162 | -49.32686 | 2024-09-26 05:04:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bcbc962f-eb63-3988-9f63-41cc0587e623 | -12.95 | -45.33 | 2024-09-26 05:04:11 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d8922cfb-156d-3af1-a168-14a1856a3fb3 | -12.89 | -51.23 | 2024-09-26 05:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a41b82fb-b111-362f-887c-937c9837d098 | -12.86 | -51.16 | 2024-09-26 05:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0551a279-e45f-3d4a-bd77-b9dec5d81dd9 | -12.86 | -51.22 | 2024-09-26 05:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1468acd0-ff04-38e3-98da-ddba7ab5487a | -12.86 | -51.27 | 2024-09-26 05:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5e220dc9-8ad1-363d-a4c5-b1d2312d542f | -12.86 | -51.33 | 2024-09-26 05:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e5dad9c8-d5bd-3721-b525-936a4fb65064 | -12.87 | -51.39 | 2024-09-26 05:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9f756ee1-492a-3abd-b89f-473a8a9ae5d3 | -12.87 | -51.45 | 2024-09-26 05:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a6e29a2a-fb1e-32ef-aa51-a7cdfcfcf5a5 | -12.83 | -51.15 | 2024-09-26 05:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 07c738bb-8835-361f-a5cb-91ec52ef5bfb | -12.83 | -51.2 | 2024-09-26 05:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 58fc0230-ec53-36d8-bc24-ea7ac41e9069 | -12.83 | -51.26 | 2024-09-26 05:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c05c53d3-6d7e-37c8-89ff-e3dc39073af4 | -12.83 | -51.32 | 2024-09-26 05:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e4a04e8e-33c7-345f-b41c-53d43f4550c7 | -12.83 | -51.38 | 2024-09-26 05:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d4866c75-d3f6-36d6-9641-e733307712c1 | -12.84 | -51.44 | 2024-09-26 05:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6bfed083-3337-3596-a305-203c8637030b | -12.8 | -51.25 | 2024-09-26 05:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 48a975c6-5780-3a2b-9075-3e948fb5ad6d | -12.8 | -51.31 | 2024-09-26 05:04:11 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 210699b4-9eba-3e62-a18c-ecd2d8701c3b | -12.95 | -45.28 | 2024-09-26 05:04:11 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 959e91db-c330-35b6-9b49-74338f2bf4fd | -3.22296 | -50.32072 | 2024-09-26 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 51ae7df5-bbbd-3232-8857-4ed56f98b386 | -3.2008 | -51.14347 | 2024-09-26 05:40:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5723ce46-8ecc-317f-ad87-34b2133b8098 | -3.19196 | -51.14218 | 2024-09-26 05:40:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 5fe45c2b-adef-34ed-930f-b788a1a57bd8 | -3.1736 | -50.2863 | 2024-09-26 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d7a3e4ee-1a49-3968-a639-6e1cecb7294b | -3.14448 | -50.28522 | 2024-09-26 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 905fbd3a-4f9d-352d-8943-e8548d52ca20 | -3.13691 | -50.27504 | 2024-09-26 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0e1209d0-30b5-35d4-b207-8ded31b03ff7 | -3.13559 | -50.28393 | 2024-09-26 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 454c6b87-af51-34bb-a547-b2dcd9a677ff | -3.00819 | -51.07598 | 2024-09-26 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a56d1821-6b8b-3b87-b2a8-cb351ff5f03b | -3.00687 | -51.08478 | 2024-09-26 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 2c098242-9395-3f04-ab8c-b3af0ebbabe8 | -2.95098 | -49.35433 | 2024-09-26 05:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0b72198c-0e52-3481-815e-5d3cd4ae3554 | -2.95026 | -53.71007 | 2024-09-26 05:40:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4893ad11-d232-3c48-8156-6f8abb1c0d0c | -2.9496 | -49.36371 | 2024-09-26 05:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bdc26161-e421-347c-be29-87f94de40a58 | -2.87475 | -51.66214 | 2024-09-26 05:40:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ac5df038-e48e-3f95-bbc8-266ac57fcb20 | -2.86615 | -51.65426 | 2024-09-26 05:40:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3734ba44-bf8d-3614-bbe5-5ec3ac4d2b3d | -2.86481 | -51.66318 | 2024-09-26 05:40:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 18d7976d-d137-3b23-9a0b-f6a5caf09d42 | -2.70022 | -57.5209 | 2024-09-26 05:40:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 1ff4351b-0707-3165-b261-1ebaf9fbb029 | -2.69598 | -57.52781 | 2024-09-26 05:40:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 5f8413b3-6790-352a-a652-59f30c69971b | -2.65766 | -57.53562 | 2024-09-26 05:40:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 6a72a0b0-4189-3a11-96f3-4442d3fcb604 | -2.65442 | -57.55645 | 2024-09-26 05:40:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 17cf7c27-1ccb-3384-b0aa-c92434e299d7 | -2.45885 | -55.61823 | 2024-09-26 05:40:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ccc26ff5-80d7-30e8-b0ed-3519df67d531 | -2.39598 | -51.28268 | 2024-09-26 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c7b5ddfc-8619-3d4f-8a20-2ffaa3faf911 | -2.38712 | -51.28139 | 2024-09-26 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e10145e4-46b6-377e-96b1-bff8bd2a4ea3 | -2.3556 | -47.59858 | 2024-09-26 05:40:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 2290b8d4-8749-3bc6-98d3-8730ecd5f923 | -2.35391 | -47.60988 | 2024-09-26 05:40:00 | AQUA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 2a222fa4-d25a-36e3-a135-8375e46b94de | -2.34563 | -47.59714 | 2024-09-26 05:40:00 | AQUA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 3df17e43-1c9d-31f8-abff-0f3f35062aca | -2.34395 | -47.60847 | 2024-09-26 05:40:00 | AQUA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 5b80e016-2d38-3ee5-9889-d5221fa1e66b | -1.8746 | -54.70371 | 2024-09-26 05:40:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6bed8a6d-1010-3a70-be4c-44dcd8c93333 | -1.87261 | -54.71664 | 2024-09-26 05:40:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| c44b63d8-bc5f-3fdf-a5e0-1fdbab1da0dc | -1.04752 | -53.35309 | 2024-09-26 05:40:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 1f8c328a-f0c3-3030-adfd-553bda88085d | -1.04521 | -53.34708 | 2024-09-26 05:40:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |


[Clique aqui para ver as próximas entradas](README150.md)
