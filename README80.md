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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 500e3ca2-f16a-364b-ac30-8635594dc9c8 | -17.05279 | -56.2487 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| b65d4ecf-9ed2-33ed-aa8e-11d71065e86f | -17.05162 | -56.25392 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| cb53555a-b145-30a6-a370-c4f9408c8f98 | -17.05123 | -56.22617 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 79f58fc5-a02d-3876-9d92-b42bdb51f9c2 | -17.05019 | -56.21734 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| e81d7aaa-df9a-3f0f-9a37-6a9cc0d96692 | -17.05005 | -56.23142 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 209af0a1-34f2-34eb-87f7-ff52e1fccf2a | -17.04926 | -56.26449 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 177b4648-8beb-3fa6-84f8-4019b8e05106 | -17.04905 | -56.22262 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| d6488936-3bef-3fd1-89dd-41ccd26c83d3 | -17.04888 | -56.23666 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| cab2423a-ab21-31b4-a8a4-72d7cf588f3f | -17.04791 | -56.22786 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 9b8e618c-8320-3e0c-901d-45ebbce99f4b | -17.0477 | -56.24191 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 5ef888c2-95b2-3e35-b0bb-2b95f68a23a8 | -17.04677 | -56.23312 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 8884827d-93ae-308b-8416-5d952d11d3f8 | -17.04653 | -56.24715 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 4fb68401-0a26-395f-a765-fe6d11d518c1 | -17.04563 | -56.23839 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 2da312ec-c8f6-36e2-b575-5f12d4d300b8 | -17.04536 | -56.25237 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| dcb206ef-3be9-3cb8-a30b-05e3255c58ba | -17.04449 | -56.24365 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| a6ef0c97-689e-344f-b6c4-c5d939f0d182 | -17.04418 | -56.25765 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| c39fb1c7-f241-3f55-9785-e37b0f8fc86e | -17.04335 | -56.2489 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| bc091810-5f92-34ad-997e-2b86d02a2e49 | -17.04221 | -56.25415 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| a0788b1d-4e47-3929-b68a-bd2044f2fae8 | -17.04106 | -56.25945 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f9300b1a-110b-3700-bb3b-9b17d164667c | -17.04028 | -56.24561 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| d844a1bf-ef0a-3c2a-b023-b3b7a075cd01 | -17.03991 | -56.26475 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7fb7f47f-076f-36d9-a10a-c4dc4775ec8b | -17.0391 | -56.25085 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 1d5cbea2-5a3f-37b7-bf92-e45116d4306c | -17.03876 | -56.27005 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 1d7dcc48-bb42-3d94-8f56-106979bdb2f0 | -17.03792 | -56.2561 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 1bd32e57-55df-33d2-89b0-a7fe5442a1e8 | -17.0376 | -56.27537 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 9b193c26-948f-3e0a-8b7f-2d56b9f1ae29 | -17.03709 | -56.24734 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 75ad1d4a-bf41-33ba-b681-363b91a336ae | -17.03645 | -56.28068 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 94a572a5-b165-3f54-b260-2fb7358591b4 | -17.03595 | -56.2526 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| fff82a7e-4e8e-3c7a-9ee5-12efe6db3207 | -17.0348 | -56.25786 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7de2d02d-84ec-3681-afef-b4c70c737f90 | -17.03365 | -56.26315 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 63473d42-0310-31e4-b23f-b589f3feed9f | -17.03167 | -56.25452 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 55f2c508-dd14-3c1f-8f38-c090f3c77a2e | -17.03019 | -56.27908 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 248c9f9b-bb52-313f-96b5-71e042f9f595 | -17.02969 | -56.25102 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 8cc86cb2-286d-3338-849d-9dd0dae731fd | -17.02855 | -56.25626 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 14eb44f1-ab31-3316-888a-1bc8f83943fd | -17.02739 | -56.26158 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 235b23c3-8bb2-3362-b917-555b58b7410f | -17.0952 | -56.17645 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 19.3 |
| 7b72add6-5f0a-3a12-9335-9c0042528335 | -17.09404 | -56.18165 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| dcf429e1-2357-3561-a6ec-6d23c8bfb6fa | -17.09289 | -56.18685 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| 4cf40525-97dd-3d86-8045-0f7de734d760 | -17.09174 | -56.19206 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 003c8616-2532-3b5b-b035-9067f9ffadde | -17.09058 | -56.19728 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 41e09e35-5764-340d-ab18-203397ec2382 | -17.08897 | -56.17492 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 110.5 |
| b8b84223-6bdf-39c0-9fda-11d8fe28faed | -17.08828 | -56.20769 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| af555fa9-c350-3509-a252-398683eb07c3 | -17.08712 | -56.21288 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 4963205a-91a8-3734-a65e-4d7d1c78079c | -17.08666 | -56.18531 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 201.0 |
| 916ff32b-9fdd-3a39-a942-d5e4b1185032 | -17.08551 | -56.19051 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 89.9 |
| 08018f7b-5812-3f07-91c7-ccb011e3e076 | -17.08435 | -56.19574 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 89.9 |
| 96015fcd-1f57-32db-b05a-53cca06eb1ec | -17.0832 | -56.20093 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| 5dfb585f-3eaf-35d1-a157-faf9c44c4e45 | -17.08274 | -56.17339 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 110.5 |
| e4257f48-e34a-3710-b69f-c36de78130ba | -17.08158 | -56.17863 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 201.0 |
| 8277ac82-0a0a-303c-a23c-afec056d6674 | -17.07652 | -56.17183 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 43.4 |
| dd9e811f-acbd-3df4-a633-86e8029ba9ae | -17.07535 | -56.17708 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 20.9 |
| a9142306-d20b-3281-afc6-f5bd8f62c3fc | -17.06913 | -56.17552 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 20.9 |
| d787a6c2-291e-343d-993c-9a46ba299609 | -17.06796 | -56.18075 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 20.9 |
| 67bcf44e-6d07-3c50-859a-f2a0cccf7ffa | -17.06565 | -56.19108 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| cb4e6aa4-b67f-3ef7-9059-564b8c1e237a | -17.0645 | -56.19627 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| a77e8e4f-e7f3-3a12-9085-1d6b79aef929 | -17.06291 | -56.17393 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 8ca6f0e5-a2ec-3ec1-9c4b-1f2a63f39551 | -17.06173 | -56.1792 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 88e85bd6-4288-3a86-9d54-999e6452eb08 | -17.06058 | -56.18437 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| dcc87fa3-9889-37ea-96ab-e35d089e3a69 | -17.05942 | -56.18955 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 66a5a0f1-c64e-3a3a-9463-bdc40414dd48 | -17.05927 | -56.17549 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 92fefc0e-df64-3773-a250-6d7c58b424b0 | -17.05825 | -56.19475 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 7c0fabbd-368f-30b7-91fb-24630d6834fd | -17.05812 | -56.18076 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| c26f602a-9102-34f1-892e-871d1f101967 | -17.0571 | -56.19992 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 78fd0248-732b-3b27-9c06-9eaa68ff580e | -17.057 | -56.18595 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| de10c622-83a5-3596-aa29-c08b4f4a7022 | -17.05587 | -56.19115 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| fbb95ab7-1757-3e3b-954e-abae2035e6b0 | -17.05476 | -56.21037 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 531f0239-efd8-3bdd-8788-aa37f167249f | -17.05475 | -56.19635 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 2c60deb5-f287-372a-96ec-bfc618c24928 | -17.05434 | -56.18286 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 450747a9-9b87-3591-896f-b24e91c6b2f1 | -17.05362 | -56.20153 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| cf1e228a-b531-3818-87a1-c8bded94fa13 | -17.05249 | -56.20677 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| a7b75e07-a480-356b-b094-d7bc0bac07e6 | -17.05202 | -56.19321 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 1d9a1e9b-b0b6-3880-8be0-bec40f7e35bc | -17.04969 | -56.2036 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| c9a6a9d6-b1bd-344f-8909-48fccfcc84ed | -17.04851 | -56.19477 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| c6848480-2ecb-3833-8c16-e244565f10d3 | -17.04738 | -56.19999 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| c6faa124-756f-3753-9525-4d4397c4c214 | -17.03717 | -56.18647 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| 32d23a3a-9133-3015-910b-186dfcd5561c | -17.03604 | -56.19165 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| b406dcb7-9051-353a-a619-a1e43c6fe6b6 | -17.03491 | -56.19685 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| ff7d57b7-92c5-3aa8-a3d5-9c872a293bc0 | -17.03331 | -56.18861 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 24.4 |
| 9f323e20-b456-338a-8b58-da959ce450b9 | -17.03215 | -56.19376 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 24.4 |
| c25e4e9b-0d36-3e30-aa9f-af25a1e49159 | -17.03093 | -56.18494 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| d80f570a-21ff-30bc-be83-77152af8c7f4 | -17.0298 | -56.19012 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 5b632dfe-6f24-3114-bf58-b23e9cc5d9af | -17.02868 | -56.19527 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| fdfac0c7-fa63-3651-bf5e-4031cccaf1a2 | -17.10178 | -56.35615 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| a5ebfb43-c9ce-3b5e-b7ad-e056477c1cab | -17.10006 | -56.24375 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.1 |
| edbfebdb-7abe-3eba-937d-f245aebdbd77 | -17.09844 | -56.22125 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 64fbbb4c-5bbd-3913-9088-27fb6cd4de49 | -17.09838 | -56.35072 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| eb0ac9b3-d099-39fc-90ed-62c82bb88730 | -17.09716 | -56.35609 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 4605f699-21f6-372c-abd4-dde7bb3d7d8b | -17.09551 | -56.35453 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 33cfffef-70a0-3822-8de0-2150a9898ed6 | -17.09265 | -56.24746 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 389df0f2-0cfc-32f8-b7f6-efd3ced5fb12 | -17.0922 | -56.2197 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 98a977aa-9490-3dcf-8804-7727e06f68a3 | -17.09148 | -56.25273 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 025cc0ef-7995-3b20-be4a-0d1f6407ad83 | -17.09104 | -56.22495 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| e11aad85-df75-3981-a15d-0936a61fd833 | -17.09089 | -56.35447 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 76882602-8c7a-3f5f-aff2-e978036cb27c | -17.09032 | -56.25802 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.6 |
| f088b2f8-3643-3031-8513-e311bdec976b | -17.08596 | -56.21815 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 7161e0b9-9de5-3409-9a2b-eece011ac81f | -17.08406 | -56.25648 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 778c6d8e-2387-3d75-83d7-613410c21341 | -17.0829 | -56.26172 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 48b5c90c-a694-3766-98d2-2cc07322dcb4 | -17.0778 | -56.25494 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 1823e5a1-cd94-31a2-b0bc-dc333aa011c0 | -17.07664 | -56.26015 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 9a45b92e-e53b-3187-acc3-2f42ba16bed8 | -17.07548 | -56.2654 | 2024-09-26 04:08:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 19.6 |


[Clique aqui para ver as próximas entradas](README81.md)
