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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c530e77c-313d-399e-bd3e-48155d29cb6d | -3.1843 | -50.583599 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5a43b15-5898-3dbc-9f97-207c10d34e62 | -2.1768 | -53.693001 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0cae361-899d-3aff-a299-f19925d1deb0 | -2.8455 | -51.797501 | 2024-11-06 00:54:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9168470b-ebd4-3533-a74c-895be22c30c9 | -3.0408 | -53.2771 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67a909cc-e2e5-3926-8814-755e0fcecd20 | -3.1292 | -51.1035 | 2024-11-06 00:54:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9159d17-95ff-3458-9427-26627ec6c0e4 | -4.0797 | -53.944401 | 2024-11-06 00:54:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bd75c0c-de77-3489-a70a-c289b078d1cb | -3.4818 | -52.0965 | 2024-11-06 00:54:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6109d0d7-282a-349f-a4d0-be484583d444 | -3.7215 | -49.433498 | 2024-11-06 00:54:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 005f0be4-0fa3-3360-8972-6428487fdb29 | -3.0089 | -54.0853 | 2024-11-06 00:54:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4312b000-7cda-3fcd-a59d-425423886f49 | -5.0224 | -43.591 | 2024-11-06 00:54:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2663b8ad-5b8c-36e2-be79-8e4ba0108389 | -2.8451 | -51.347698 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e36080e1-f602-326f-8750-217d100ecd8a | -3.5267 | -51.305698 | 2024-11-06 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41f002f7-a524-30c4-9b82-8b14e93f6a4c | -2.7943 | -51.4855 | 2024-11-06 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c13d215b-ee0f-3356-84ba-a639b2286562 | -2.8113 | -52.905602 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b15ccaaf-a2b9-30c8-82d5-9f40b0106678 | -6.5042 | -44.683701 | 2024-11-06 00:54:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 12568c8a-b45b-3ec0-b0a6-b33eae674461 | -3.2175 | -50.370499 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 230babe1-619a-3b8d-84f3-439a0411299a | -2.2628 | -46.465801 | 2024-11-06 00:54:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba3121d2-6e36-3793-856f-9aa5181363ac | -2.8196 | -52.896599 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 651ac067-32d2-3016-aefa-d160f4d973d0 | -3.2338 | -53.399799 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 420a39af-2b1d-3254-8259-140d81664611 | -2.8604 | -51.772202 | 2024-11-06 00:54:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f8c7125-8930-37c5-9819-518ce1d92c28 | -2.9691 | -53.865799 | 2024-11-06 00:54:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53407097-4db7-3617-8687-f8be0969c7a4 | -2.8289 | -52.9375 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e90ab4ec-2a80-3271-96b0-e340d03ad209 | -3.0489 | -51.0686 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f126c0ab-19e5-3d47-922d-36f1c5e865eb | -2.606 | -54.534 | 2024-11-06 00:54:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be3c9f3a-c8a6-32f7-a80d-869462600176 | -4.3604 | -48.637699 | 2024-11-06 00:54:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 997d03ec-452d-379c-bd38-babe2375f166 | -3.1164 | -54.2402 | 2024-11-06 00:54:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8626aebc-fd5c-3513-8315-da9c42b094d9 | -6.1284 | -43.993 | 2024-11-06 00:54:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18b3cf24-2783-3398-a9a4-645d5ecfe752 | -4.134 | -43.565498 | 2024-11-06 00:54:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 95dade1e-4de5-3d9a-a897-3755d51b7934 | -3.221 | -50.385601 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 931b06f0-e171-31ce-b8ce-64b47834980e | -2.8538 | -51.7883 | 2024-11-06 00:54:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b13d27b6-6019-3f8d-baf5-1060e73e4117 | -1.8588 | -54.692299 | 2024-11-06 00:54:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb202f77-ca13-33ee-b72a-595c4c129cfc | -3.9986 | -43.2626 | 2024-11-06 00:54:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d9a4d91-d076-361d-8a09-ee3f363b1426 | -2.9424 | -54.788799 | 2024-11-06 00:54:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1415fe5-283b-3b1b-8fa1-589e8208fbdb | -4.2682 | -49.168301 | 2024-11-06 00:54:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9abde42e-6a9c-3e7b-a9f0-5dfde8760e05 | -2.9757 | -53.262901 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4750c797-c694-34e7-8f88-c207381799f8 | -3.6791 | -50.2257 | 2024-11-06 00:54:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 009ac5ab-8d87-3b0d-be37-f757b7a5acb8 | -1.2931 | -54.563099 | 2024-11-06 00:54:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d1064ae-4508-38e0-b483-826535efea62 | -2.0343 | -53.5662 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47e5082e-8dff-3e17-ab7d-ee82bc6f3227 | -2.1753 | -53.6861 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5ac8181-cbf6-307a-86c7-d80cbb756f3c | -2.5779 | -54.004101 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3c279e0-75e5-3007-ba9b-3045611efaf1 | -3.2905 | -53.106602 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6db62acb-38b7-3ed1-87d0-871f733107bd | -0.0444 | -50.786301 | 2024-11-06 00:54:00 | METOP-C | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b9dc81e-823f-32af-bd86-d3504d325ea2 | -2.5851 | -51.338902 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce777fe0-18cd-3e53-985e-416ab3bb3310 | -3.0149 | -53.434101 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f20cc6a-e545-350e-af94-9b5786e28ec1 | -2.844 | -51.790501 | 2024-11-06 00:54:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32ec6a72-686a-383c-84c3-c707ad364c11 | -2.8408 | -51.7766 | 2024-11-06 00:54:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5659c521-4849-369c-b43c-ab8683007ee7 | -3.9584 | -48.156101 | 2024-11-06 00:54:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e18a3106-1898-3dd3-99ab-56daebd89814 | -5.3245 | -43.0681 | 2024-11-06 00:54:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1efbe62e-106a-3e6a-bd60-2887063625ca | -2.9577 | -53.861 | 2024-11-06 00:54:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25a1de9a-1b4f-3481-afc2-f7d7aaf1b36f | -1.3536 | -51.9491 | 2024-11-06 00:54:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9aae01eb-6846-3be3-9cde-57e8f4ef8297 | -6.5053 | -47.500198 | 2024-11-06 00:54:00 | METOP-C | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 670b7512-c0f6-3837-8f69-9e857fabfd21 | -6.503 | -47.490398 | 2024-11-06 00:54:00 | METOP-C | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5670e500-8338-39a6-9919-6884fb4f9abc | -1.818 | -53.657501 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3aa42ff2-eb33-3f1c-a17d-820e53a778b1 | -1.2962 | -54.666801 | 2024-11-06 00:54:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0250e1da-6a75-36ab-8728-0d1d0acabf16 | -2.834 | -52.914799 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 650113b5-129a-3a5c-a207-36babc27fad2 | -3.1506 | -51.151299 | 2024-11-06 00:54:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94f69ae1-b2d9-32e0-80f0-f4038a2d1ae8 | -3.3413 | -51.620201 | 2024-11-06 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1268dfa6-97d7-3895-a1bd-f0def9a5e341 | -2.4269 | -53.659 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e59152ef-e76e-3278-8d1e-2c3784ca91cc | -2.1607 | -53.667702 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cb5608f-a538-3a55-bec6-89013ad8ae5f | -2.5583 | -54.008499 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b696e3e0-c296-3fd1-bce7-fb16c7c9c45f | -3.203 | -53.219398 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49617026-dd2e-3b51-959a-b14aa4ea4891 | -3.2105 | -49.2323 | 2024-11-06 00:54:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57f4ec83-d10a-3a67-8a61-216a1b9d60f1 | -4.129 | -43.587101 | 2024-11-06 00:54:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0dc10058-6037-33f9-9597-af3c2e770f37 | -5.5554 | -43.712002 | 2024-11-06 00:54:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ba503647-32d4-3aaf-8faa-1d211d83760d | -2.8572 | -51.758301 | 2024-11-06 00:54:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77ce5ab1-baae-3f85-ac96-f4282fc7306f | -4.1935 | -51.020901 | 2024-11-06 00:54:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 353752bc-a662-3dc4-954c-6ddfbf066601 | -2.8435 | -51.340599 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d92dbdd0-0891-3517-abdc-bfeb83b098f6 | -2.8588 | -51.765301 | 2024-11-06 00:54:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94211f5a-32b6-3265-aeac-5378d660fa40 | -3.1686 | -50.204601 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48e0ae75-6a9d-3c2a-a550-910f513dcc9a | -2.7211 | -54.134399 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbf5b543-39c5-3d21-9b9f-b559acf8e59d | -3.0007 | -54.094601 | 2024-11-06 00:54:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77dd4505-8691-395f-8b60-0f49c9615ef3 | -1.2076 | -53.649799 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 459585f2-eb86-3066-9cec-1edcf1b152b3 | -2.5823 | -51.8638 | 2024-11-06 00:54:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00d983ac-c177-3d68-a3b1-cc287b9db010 | -3.3652 | -49.497398 | 2024-11-06 00:54:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f926e8e-c9ea-33dc-b4f8-150010f87547 | -4.3625 | -48.646599 | 2024-11-06 00:54:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5be0a99d-baa6-3e1f-a624-e3472accca2d | -3.0916 | -51.119499 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7980bb55-671a-387a-9031-09b8dc07932b | -6.1007 | -43.964298 | 2024-11-06 00:54:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65a3add7-8aa5-38f3-a359-c7a5b99b31dd | -3.6376 | -51.7868 | 2024-11-06 00:54:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71efc7ef-fc3b-3574-8ebc-5f1c5378af47 | -2.8176 | -52.932899 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3155d47-3a0d-34e9-8a00-54a3df50301a | -3.8909 | -50.2495 | 2024-11-06 00:54:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37c4a7bd-8137-300c-a309-16b8e4ab228e | -2.8294 | -52.894402 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae1e8ca5-0cfc-30f8-af57-7a0ab1e22372 | -2.9162 | -51.030201 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3375cb0-6cb6-3612-8c0d-453db5e352d1 | -5.6659 | -45.936501 | 2024-11-06 00:54:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c1cb1218-8dda-35d5-b98a-2be145bbc12a | -2.8474 | -51.760502 | 2024-11-06 00:54:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9226a04-e4bb-3012-aa73-2d6a18743c32 | -6.1201 | -43.959499 | 2024-11-06 00:54:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be75b91a-1f64-392d-9720-0817a146988e | -3.0685 | -52.4977 | 2024-11-06 00:54:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7798c1c1-fbfc-31f0-8ee7-2ef54eb96f67 | -0.8458 | -52.837101 | 2024-11-06 00:54:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2d94f2a-0f98-390c-81a6-3f0050d01b4e | -3.2171 | -53.101398 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffc6794c-da1e-3b64-8bc1-023a7ce2b707 | -3.1762 | -50.5933 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06cb1f10-3b7d-3e52-9248-03b7462c761e | -2.9115 | -51.0541 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef4cdaeb-26c3-35cd-975b-b2a0849d2409 | -2.9294 | -51.0425 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29d908ed-fd7e-3a84-8341-ae92cf23cec1 | -2.8407 | -52.898998 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 161afa5f-310d-37b3-9566-62218d8015fc | -4.1146 | -43.570202 | 2024-11-06 00:54:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be627718-1279-3d79-b0dd-c36093f6a457 | -2.8057 | -51.490299 | 2024-11-06 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32e5edb2-c7f4-380e-9a3e-01b178756e01 | -2.8258 | -52.923901 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd0fd92d-244c-38a1-b8a6-816327bde276 | -3.0247 | -53.4319 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6ce454e-dd97-3592-8c26-4acbeb787bb2 | -2.6772 | -51.827999 | 2024-11-06 00:54:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec283b3c-1a03-3dc4-9835-84ae02d821d8 | -10.4058 | -48.9244 | 2024-11-06 00:54:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d19fb42-1e9f-34fe-bb6a-1bc1f6587ea5 | -3.0361 | -53.256599 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1737233-373b-3dca-a630-675ac46f9f5a | -3.595 | -58.594299 | 2024-11-06 00:54:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
