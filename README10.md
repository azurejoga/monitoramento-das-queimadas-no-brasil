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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 528be9f0-331d-3bf9-b318-71a0d5cdd19d | -11.00535 | -55.08259 | 2025-06-15 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8fcf434d-f215-3754-a816-7e7ae8d462df | -10.92334 | -56.83873 | 2025-06-15 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83cd67a6-a7d7-341e-8254-2f7171e1824a | -9.42028 | -48.44918 | 2025-06-15 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3b969b1b-a66e-3c1a-9524-8cc8d2bd8f5d | -11.88624 | -54.68398 | 2025-06-15 04:46:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 299c77cf-4773-38c6-837b-07a485d53df2 | -9.41124 | -48.43468 | 2025-06-15 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48fed14b-3aef-359b-b473-f87827073b9f | -10.08344 | -52.74565 | 2025-06-15 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 07e0d384-395b-33f9-b83c-b8a1c2d31009 | -10.84087 | -53.77116 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ae0251fa-82e5-3265-90a6-d578568ab686 | -8.58794 | -45.86119 | 2025-06-15 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7165159-009b-3a33-bcbd-0147b0801bb1 | -7.20409 | -43.10592 | 2025-06-15 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 6320fe2e-ce25-3469-b3c3-b8246e3f2a5a | -11.72967 | -48.87125 | 2025-06-15 04:46:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34c74c14-7d54-32db-89ae-dcf5a4a639c0 | -8.37423 | -47.05375 | 2025-06-15 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2ba0f345-a588-3ab8-b613-5eacb37f3523 | -10.4525 | -47.95045 | 2025-06-15 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 131071d7-bd0e-3116-9a6b-3fe0fa7969c3 | -6.44454 | -45.73271 | 2025-06-15 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fbb1eb58-451d-3d78-9c87-7966db07cdb9 | -10.79871 | -47.57328 | 2025-06-15 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 283b6ce4-f4a0-37f0-b6b6-c0045f6a4eea | -12.32387 | -46.60146 | 2025-06-15 04:46:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d8635118-15c1-3ca9-a34a-ba3de4574d72 | -10.24271 | -52.23326 | 2025-06-15 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9a126419-53e9-3998-855f-d8cbd8565d2e | -12.08904 | -49.48885 | 2025-06-15 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f43e9303-6ae6-3b44-8a1f-1d40c14132eb | -10.85318 | -53.78075 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a8b6768-4e4a-3fba-825b-79acb10843d7 | -9.04128 | -47.01812 | 2025-06-15 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d576ecb-8784-3926-8d41-5277af97f597 | -7.2038 | -43.11061 | 2025-06-15 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 6c6bd9c2-1048-3031-8d48-8bf06060ef91 | -10.56982 | -52.01464 | 2025-06-15 04:46:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e35cc118-2e8e-3726-99f6-5ea0450c8673 | -10.07349 | -52.74406 | 2025-06-15 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 700a5aed-3e2f-3759-a7c0-0f1ccc6c44bc | -10.09119 | -52.73967 | 2025-06-15 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 46cdd065-9e97-3753-9219-ab47c27bf4c5 | -11.88559 | -54.68784 | 2025-06-15 04:46:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a4da975-7a90-3fd8-8129-299b6c3ba545 | -11.57739 | -47.8723 | 2025-06-15 04:46:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 995dfca6-3981-305a-86db-2ca76cb25f92 | -7.20918 | -43.1085 | 2025-06-15 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d81a8ef5-ef18-310c-94d5-3580083fbb01 | -11.75108 | -46.74841 | 2025-06-15 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a58c2477-34bb-39f8-868e-ad6f4ff0cc26 | -10.8492 | -53.78389 | 2025-06-15 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d49e3d05-ea5f-37aa-8523-35b896b32884 | -9.40397 | -48.43358 | 2025-06-15 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89a4243b-13cd-337d-a2ed-c0cee47bb18b | -7.20908 | -43.10667 | 2025-06-15 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b1f65d90-137d-3184-9b83-ead121d67d56 | -5.40654 | -48.55965 | 2025-06-15 04:46:00 | NOAA-21 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8231b27e-7729-36e7-9fc5-1b663516018f | -15.39819 | -47.89616 | 2025-06-15 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7cccc77-37e9-3480-9b87-2a3950a89df7 | -13.91446 | -54.60406 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bc6589d9-6956-3b21-9eda-cf3f136395e2 | -15.41461 | -47.86517 | 2025-06-15 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 367bc1a3-8a45-3cc3-9b18-fdd24c729f35 | -16.64917 | -54.39354 | 2025-06-15 04:49:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1f7d59c-7d59-33e1-ba83-8d26b4fc757a | -14.83599 | -48.43586 | 2025-06-15 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6b9e56fa-c3ea-3b45-9329-6bba8623caf5 | -13.90645 | -54.61042 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ffc68d83-c755-3d22-ba84-7c4a6acced92 | -13.91512 | -54.64261 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9024df61-23c0-3622-a179-72d302c19b08 | -12.69089 | -52.39639 | 2025-06-15 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f29d879d-4857-3a33-87db-0394152bf5a9 | -13.91663 | -54.61206 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 26.4 |
| fc2d3c35-2aa1-3963-ba44-444cf6e34e96 | -14.02977 | -55.12041 | 2025-06-15 04:49:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f65f7660-1e0b-39af-a748-58c9432b5251 | -13.94345 | -54.49025 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 835bac8f-b408-3441-855b-97450fd6a503 | -13.94683 | -54.49084 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4d1b250c-b98c-32fd-b481-18b1114df029 | -15.4151 | -47.8614 | 2025-06-15 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e6e598f0-3a48-380a-9606-76e3a2677d3e | -13.92402 | -54.60949 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5d53232-d39a-36d2-8b94-08c27b348b18 | -18.41154 | -54.57076 | 2025-06-15 04:49:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e5e9dc6-6bf5-342b-9b63-b27091637c96 | -12.72494 | -54.97055 | 2025-06-15 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c0cd968-2b0d-386a-a343-49a1161921ca | -14.67485 | -53.13084 | 2025-06-15 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70e5fc69-b9c5-3aa8-8ed6-d23a7e63b47a | -13.91606 | -54.65819 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 47764fd5-f145-37c6-bc1a-419a12b7a482 | -13.95081 | -54.4877 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9d69eefc-304f-303c-8d04-30bd1a7547f3 | -12.16495 | -56.54163 | 2025-06-15 04:49:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 534a3678-595c-3730-9d78-8258945821a1 | -13.95466 | -54.44263 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59e0052a-c1a6-387c-a050-8e654a06bf4c | -13.09167 | -52.28813 | 2025-06-15 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 22b65366-6dad-38ac-8c9f-5b145249bc04 | -13.92558 | -54.62129 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 35934c76-8108-3847-943b-11b0e65ebe63 | -15.4038 | -47.85249 | 2025-06-15 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3cc15c4-c4f4-3699-8fd5-f0e70f39bc3a | -15.39684 | -47.8741 | 2025-06-15 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e50a0261-3d10-37fd-9a1e-752ddea10082 | -13.91668 | -54.65443 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 47ccc79a-7328-379d-b82d-680ffb75ce48 | -15.63888 | -49.37369 | 2025-06-15 04:49:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 110e62da-f058-3d89-ae6e-a98b24645f8d | -15.40095 | -47.87474 | 2025-06-15 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d0467260-eac1-3836-ba27-f1b158a0e2f6 | -13.94068 | -54.48595 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 96e64cbf-0ba9-31a4-b1f9-dbe6328856f1 | -13.92341 | -54.6132 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 597bd66b-c381-3d14-8974-d02f40529ef3 | -14.83532 | -48.44075 | 2025-06-15 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 73397085-e5e9-30b4-aa0e-3d50f6545182 | -13.22809 | -49.83671 | 2025-06-15 04:49:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 805f097e-c1e9-3d9b-8cc1-6c27c7407afa | -13.90706 | -54.60668 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| fce89077-e546-33f5-acd2-443b8b564f6e | -13.90306 | -54.60985 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6689939b-be0c-3a62-bdb3-b197da945131 | -14.8334 | -48.42564 | 2025-06-15 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bcfb43c2-ec9c-3324-94c7-b00111499bce | -14.03322 | -55.12101 | 2025-06-15 04:49:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23fecccb-cc25-3cd7-89a3-07d2cc9fdf5f | -12.69308 | -52.40387 | 2025-06-15 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5fea33f4-1562-36fd-a070-fc83e0e552a4 | -13.92219 | -54.62069 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 960475b8-0761-3b3b-af02-1acdea927968 | -15.4115 | -47.85713 | 2025-06-15 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a404d971-4f5c-3d7d-bd38-210cdfb64b73 | -13.94008 | -54.48967 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 85af5dcd-0eb2-3cb0-9d95-62096d5b0bab | -13.91729 | -54.65068 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f6c1b3ff-5018-3898-8076-84094c922734 | -16.2865 | -52.93636 | 2025-06-15 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c9b48ee-7ff2-3fda-a569-6b3371177af7 | -13.9179 | -54.64693 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b4bae2b0-1d69-3730-b440-7d188886ff81 | -15.39019 | -47.86197 | 2025-06-15 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a32ac141-adf6-3dff-8dba-1ad39722e34f | -15.33243 | -47.35863 | 2025-06-15 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54225cee-b44e-34df-9170-5532f1db8d80 | -14.83987 | -48.43652 | 2025-06-15 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 076e1d0f-1ef2-3008-b7be-e2938cf87fde | -15.3969 | -47.87403 | 2025-06-15 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af628421-0954-3829-9fb5-1f00b4dacab4 | -15.41413 | -47.86887 | 2025-06-15 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19c64551-530b-3e6b-ac3f-b41152ec5c4a | -13.9154 | -54.61958 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 26.7 |
| dc10d40f-8271-3385-81f1-ef2aa37fabb0 | -15.41365 | -47.87258 | 2025-06-15 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 580fd62a-a248-3e68-9103-7b21bd7255c3 | -15.41051 | -47.86488 | 2025-06-15 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b2ac2e3-65a1-3a70-af74-7aa0e04a2cc3 | -14.03666 | -55.1216 | 2025-06-15 04:49:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d3e8be5-e396-37a7-a1f2-3f56fe79cb4d | -13.39919 | -52.69624 | 2025-06-15 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b681392e-545b-3378-9261-6d7a36222a55 | -12.69034 | -52.3999 | 2025-06-15 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2765f4da-b70a-3ec5-bf0c-6227a74134b9 | -14.02913 | -55.12427 | 2025-06-15 04:49:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4969e05-ed2c-3d45-ad32-6c4b3f49ba1d | -13.91385 | -54.60778 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3088824f-5c23-3074-911a-6f94c0db621c | -13.91818 | -54.62389 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 26.7 |
| b4638d25-63f8-3e20-80bb-61573e935565 | -15.41269 | -47.88001 | 2025-06-15 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2829603c-6bb8-3ed5-b0ed-859d3d97614a | -15.56945 | -47.85577 | 2025-06-15 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 181b62a5-54d3-3404-b7c9-78dee95df8fb | -13.94732 | -54.44514 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bfd32e9b-5020-38fc-a5aa-297bc19749c1 | -13.91267 | -54.65759 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b8982289-cd6a-3471-8111-bb81e9dec335 | -18.39805 | -44.1909 | 2025-06-15 04:49:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a99ad63b-0658-39e5-8668-e36f855e8567 | -13.92002 | -54.61262 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 3fd019c5-a839-39de-837a-d2452c027279 | -13.9114 | -54.62278 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b569be74-9219-3418-ad7b-42fad6532d33 | -13.92462 | -54.60579 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb0c5a00-dd7e-3e79-99a5-0ba809125e94 | -15.41317 | -47.87631 | 2025-06-15 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe6601f6-a62d-320d-a79b-ef9692b85a81 | -15.40049 | -47.87828 | 2025-06-15 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d2a8623-2d26-39fe-a8ce-0829d34a73ca | -15.33294 | -47.3547 | 2025-06-15 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2947fb3a-74cd-3c59-bc6e-c89e1ee5e133 | -13.94406 | -54.48652 | 2025-06-15 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README11.md)
