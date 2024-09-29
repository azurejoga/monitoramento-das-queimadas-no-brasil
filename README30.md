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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d637415-2411-3eae-8d1d-aa5d46671ce4 | -11.79243 | -47.60526 | 2024-09-29 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08ddfc62-770a-33c5-a3f0-613ad226bf88 | -11.79162 | -47.6097 | 2024-09-29 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 387b9b3b-4104-3f10-b66f-468054dec5d0 | -14.1844 | -47.04601 | 2024-09-29 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2c965c2-b100-3636-8afb-c38ae98f3166 | -15.62465 | -47.2233 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e6e0524c-ef40-36b4-9428-ccca25c75a97 | -15.4262 | -47.43872 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9268e14-9d35-3a0d-b2bf-3d58078a7d47 | -15.42214 | -47.43787 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79673861-b9f1-33c5-9c1c-50c6a202d81d | -15.4188 | -47.43319 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7aa91c26-6183-3e86-bb80-ec8808d0f37a | -15.41809 | -47.43701 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cbe44965-6782-377c-9826-0f7d2e079c15 | -15.4174 | -47.4407 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 100e75eb-031e-360f-8679-856dad5f2f20 | -15.41473 | -47.43236 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0d609ea8-e145-3c15-8952-79283e11cb38 | -15.41403 | -47.43615 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| bc91a1cc-23ca-3786-b273-86f3167b5c21 | -15.41334 | -47.43986 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 50e1c452-12f5-318e-b8ee-362be3e1df75 | -15.37468 | -47.44619 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 466c3845-be08-31df-88a0-c98f015f888d | -15.36215 | -47.44548 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d1feaa71-e648-379e-ac61-595d7a6d9de5 | -15.3095 | -47.47923 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c83ce9a2-732d-3aa4-9320-19f9cc35b1ac | -15.30885 | -47.48275 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 23acfcb1-0fac-3be7-82c9-460a2890fe1c | -15.3065 | -47.47249 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 19705cac-0210-3f23-81a3-f9deee6e8108 | -15.30593 | -47.47558 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8dfb943b-6d2a-3c05-b27b-d9b93a4f6dff | -15.30536 | -47.47872 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6785b88a-7278-3a4d-96d5-b6b0cbc7d04b | -15.30473 | -47.48212 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5d60374-6253-3a20-affd-308cbc14b0d3 | -15.30408 | -47.48566 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c9385f6b-3e01-3525-b6c9-28b690aa82d0 | -15.30234 | -47.47209 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bcbbfdde-0a5c-3933-9a66-60e4b69437ab | -15.30177 | -47.47521 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4e0df6fe-4c0b-35fe-81c7-8998dfd67590 | -15.30119 | -47.47837 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 71e6461c-90d2-393f-a83f-495c701962e3 | -15.30057 | -47.48174 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4f83dae4-9ed1-3b67-9944-e4e61f7fa0e1 | -15.29993 | -47.48518 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 27453ce5-b705-36c3-891e-d4d201e05ea4 | -13.46357 | -48.57203 | 2024-09-29 04:04:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6ce219d-6f3e-369e-8372-74c1947d1512 | -11.58343 | -48.43299 | 2024-09-29 04:04:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cf5c5476-ae2b-3e04-a7c4-3b1bb5fe7a39 | -11.57877 | -48.43217 | 2024-09-29 04:04:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0405ac30-3d08-3fc8-b4c0-095a7746e1e5 | -13.47383 | -48.59747 | 2024-09-29 04:04:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9bbb14be-ec0c-36bb-bfef-d609ab99d124 | -13.47293 | -48.60226 | 2024-09-29 04:04:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c177a6e-b093-36ae-ba6d-2d27c58dda4b | -13.46842 | -48.60123 | 2024-09-29 04:04:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 113ed7ba-3ecc-33a7-9255-75cd8e264f90 | -13.45557 | -48.36056 | 2024-09-29 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca278cae-4e3d-35f4-87e9-f20d56eec42d | -13.45257 | -48.58091 | 2024-09-29 04:04:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc0872e2-41ee-3f2a-bdf1-8780975118b3 | -13.40236 | -49.12951 | 2024-09-29 04:04:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c65d1aec-de78-3be0-bce5-5bcede0ddcd4 | -13.18472 | -48.52152 | 2024-09-29 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9fe13d1d-e7b6-3fd1-b777-1a88d8b8eb97 | -13.18021 | -48.52048 | 2024-09-29 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f047589d-a127-3f70-a3a1-c73ec9d64c74 | -13.16908 | -48.50453 | 2024-09-29 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9cd18f80-94c6-320d-af43-3435be257a51 | -13.16455 | -48.50359 | 2024-09-29 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 03fa2784-6323-35db-bf08-89e213c989a8 | -13.16002 | -48.50272 | 2024-09-29 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 06ecfe17-31e6-34de-aa91-0b06fcd3072f | -13.15921 | -48.50703 | 2024-09-29 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 736b04d4-e7ec-38a5-b335-2bbcf3ec1d7f | -13.1584 | -48.51133 | 2024-09-29 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c3b3b730-8313-3ed6-a330-4e1d3e52d49e | -13.16899 | -48.5553 | 2024-09-29 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 627b3d96-dfaa-3adf-8c0c-527da49fabb7 | -13.16441 | -48.55459 | 2024-09-29 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ff3d7273-c188-35ef-b6d2-29d5cff5c73c | -13.16347 | -48.5596 | 2024-09-29 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| be040d90-6980-360d-93a0-4fe1d8edacb0 | -13.03544 | -48.61147 | 2024-09-29 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 54994102-de76-3fc4-8fd4-865fcc749b31 | -13.0317 | -48.60609 | 2024-09-29 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8970ea29-5796-39ca-b458-a796f62ebba1 | -13.02885 | -48.62125 | 2024-09-29 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2afe900c-1243-34d8-88c3-4dbcf27857fa | -13.02705 | -48.6056 | 2024-09-29 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9c12de18-cc78-38a8-b9dc-651e8318e18f | -12.75217 | -48.48051 | 2024-09-29 04:04:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1665fd0a-993e-3ea7-a4eb-eb0d7188c626 | -12.75126 | -48.48542 | 2024-09-29 04:04:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 837ba239-9280-36b6-b8e1-d030ffae6eb1 | -12.75042 | -48.48997 | 2024-09-29 04:04:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e83ece4-284b-3e97-b939-f997debdf92f | -12.7477 | -48.47913 | 2024-09-29 04:04:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2d070c6c-c4db-3f29-885a-0ad11416e5d8 | -12.74674 | -48.48429 | 2024-09-29 04:04:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b458389-dcd4-37be-9b60-fc5b5062ed39 | -12.47919 | -48.39613 | 2024-09-29 04:04:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e8523ab5-d276-3f51-a3b6-07352ed5c6cd | -11.69474 | -49.97127 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a463e5da-5ea3-3b56-a1ae-93dbad9753d1 | -11.6896 | -49.9703 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f517f429-3c82-363f-a0af-8c7cda2462fa | -13.07602 | -50.85733 | 2024-09-29 04:04:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 12da17e6-d084-35e2-891a-c7f24d6e5f1f | -12.54846 | -50.63773 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a124675-362f-32e7-9142-da27b40d2a0b | -12.54781 | -50.64106 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 284e36f3-bebe-3003-9d18-e257dcc82934 | -12.53129 | -50.64128 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fbe4921-0b69-321d-80f9-9e54d26d7ae4 | -12.52938 | -50.62976 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63e0322e-419d-385e-a692-e0c224f21bd6 | -12.52874 | -50.63314 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| abba58e9-46af-367a-ac88-7e3d193d324a | -12.5281 | -50.63651 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6aa7d823-cd7f-3433-bb99-d0b4c1fcb27d | -12.52799 | -50.63017 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3224383a-97e4-36f3-a966-07ed879a4a20 | -12.52746 | -50.63989 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 385f52c0-52bd-3729-8fa7-73b520d10f81 | -12.52733 | -50.63354 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a0ea708-9639-3ece-8e8d-eb2e32df5f7a | -12.52667 | -50.63691 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 06672ab4-a238-3800-943e-8fd48a9fc2fc | -12.526 | -50.64027 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0c3e195a-a187-3120-b5c6-764aeb3f1f77 | -12.52281 | -50.6355 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| af9862a7-77e5-316e-ab48-58c01bd61e29 | -12.28864 | -50.49609 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b700859f-edbe-3c9b-aa7d-042910f9a9dc | -12.28736 | -50.50276 | 2024-09-29 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16f841af-c110-31de-b65f-33c2639cb55f | -12.24099 | -50.65805 | 2024-09-29 04:04:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5fb6c47f-9c41-36c7-946f-da77ccf2d99f | -12.23633 | -50.6536 | 2024-09-29 04:04:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4bdb33d-4405-3d3b-a885-c1e768e4864c | -12.23567 | -50.65701 | 2024-09-29 04:04:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd38a1c7-f785-3abb-831b-b74f2b45c11b | -13.69509 | -50.93882 | 2024-09-29 04:04:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf037bb9-8f5d-35cf-9276-d71bf816ba7a | -13.69048 | -50.93439 | 2024-09-29 04:04:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f9dd36a3-de02-3cd2-9824-55955034855f | -13.59487 | -51.58588 | 2024-09-29 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48855a0b-539b-34b8-a344-655684e1e69e | -13.59011 | -51.58101 | 2024-09-29 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e827a54-064b-33fa-80be-cf622cfe450c | -13.58936 | -51.58473 | 2024-09-29 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25134cb5-5f0c-37b7-afff-3f529da5f71f | -13.20833 | -51.23147 | 2024-09-29 04:04:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b7f6422a-f66b-34c2-b669-7597acda146a | -13.20291 | -51.23037 | 2024-09-29 04:04:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8334570-a251-3a7f-94eb-62b694a1cbcf | -12.86428 | -51.15332 | 2024-09-29 04:04:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8f2acd0b-62a6-34ee-9bb4-80099dab3afc | -12.86366 | -51.15082 | 2024-09-29 04:04:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 74d40526-6ea2-3419-9d9d-93be1d1d5a59 | -12.86297 | -51.15442 | 2024-09-29 04:04:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 40bdce61-2e05-3b37-a88e-684a95c4a04f | -16.43264 | -53.94332 | 2024-09-29 04:04:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2f2392a0-fd7e-3465-84b7-f22fe77c5f04 | -16.43157 | -53.94819 | 2024-09-29 04:04:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c6913945-2597-3e41-a8d7-b9bd05cfee6a | -16.43052 | -53.95302 | 2024-09-29 04:04:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 86284043-8a4b-38f6-a053-2fc643be6fee | -16.42449 | -53.95164 | 2024-09-29 04:04:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9931aa58-234d-345c-bd7f-97eb3c450c40 | -16.65095 | -55.22131 | 2024-09-29 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d7591020-6954-3dd0-81e5-6a982539a077 | -16.64462 | -55.21801 | 2024-09-29 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| bc86e812-fb6e-3a56-bd71-2298a9b9f5b2 | -16.6445 | -55.21975 | 2024-09-29 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d22beb82-18b9-37da-852a-4aab29eb9578 | -16.64332 | -55.22369 | 2024-09-29 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c24b4c4e-7093-3f8b-9f12-b5ea3f985b1c | -16.64323 | -55.22544 | 2024-09-29 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| eaacf684-123b-30cc-b8c3-3f5c497ef266 | -16.63815 | -55.21655 | 2024-09-29 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 2433e0ff-9e85-3de5-a49f-d93529ca4399 | -16.63803 | -55.21827 | 2024-09-29 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| a74142eb-5df8-34f8-a717-bd454456864b | -16.63685 | -55.22223 | 2024-09-29 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 8171fdaf-cfcd-35f2-83b2-f3ba274b9171 | -16.63677 | -55.22395 | 2024-09-29 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 15e6589b-d7be-384a-b98d-affa8d2eeaf8 | -17.12214 | -56.20911 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| e3a10b4c-e969-3a44-8304-a94d17742d05 | -17.12065 | -56.21555 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |


[Clique aqui para ver as próximas entradas](README31.md)
