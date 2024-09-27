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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4ad95ab-b369-35e6-9ee4-a601637afab0 | -9.68935 | -53.49563 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83bb2236-195e-392c-8ffb-8ef15f07fcbe | -9.68864 | -53.49987 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c2b5bdd-ef3e-34d8-9eaf-dc92566a549a | -9.68847 | -53.4961 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cb3a070-0a7c-37c1-aa71-c55594096832 | -9.68778 | -53.50035 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6110fa7a-0fa4-3649-b0a8-0af46bdf21ad | -9.66905 | -53.52353 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cce537d4-6072-3176-b808-71c299ccf3e0 | -9.66612 | -53.51864 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0870e511-3098-3bcd-afb5-00e1889dc066 | -9.66542 | -53.52292 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8b6b442-2bb9-3f5b-ab67-3e18ae01c112 | -9.66471 | -53.5272 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb0f5a84-9e54-3600-b9de-fa4f14291c1c | -9.66249 | -53.51804 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de4612ea-7471-3599-91d6-19b0e96a17f2 | -9.66108 | -53.5266 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f43eba57-5086-3b29-bda1-a5ee50221914 | -9.61599 | -53.26318 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d74a6af5-d4f4-359e-9e8a-58d36379e722 | -9.61373 | -53.26416 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19ef5c01-26d1-3d9b-9e88-fe30b709694c | -9.61305 | -53.26833 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fea24d5f-79f6-3cc6-8f92-2573d5f349aa | -9.6117 | -53.26674 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ef0d26b-84c5-3f81-a5ff-e193b1290516 | -9.5939 | -53.29517 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c8111dc-f4b8-3846-8357-bc0aa37e5d01 | -9.59031 | -53.29454 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6cb6c2ab-c437-3b6f-9cfb-c9ed1da29b08 | -9.58602 | -53.29813 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb1b9a0b-69eb-3811-9b47-9ded24a2e303 | -9.58105 | -53.30592 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9d59371-4afd-37df-9c37-8b4aeca3936c | -9.57745 | -53.3053 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1da250ac-383f-3b9c-aa37-c15d7add3b66 | -9.57676 | -53.3095 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c624a839-6035-30b9-a27f-93e88762815e | -9.57607 | -53.31369 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f113d789-e784-3cb0-af65-62fe3055915b | -9.56442 | -53.40678 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 20afdeb1-4890-3f74-a286-cc885b6a0ed7 | -9.56359 | -53.38931 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 282c712f-54e3-3b28-b4c7-089498977c2a | -9.56289 | -53.3935 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc1eba85-750a-3869-b64f-f06138f2b924 | -9.5608 | -53.40616 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e65837dd-ab07-324b-a612-27894eaf64d9 | -9.55928 | -53.39292 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 849d7098-6af9-3433-8f76-2aa7e0fc828d | -9.55858 | -53.39714 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca4106fe-2eaa-3a84-b5ea-cb72d029b8e8 | -9.55788 | -53.40134 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 205c1bc0-fcfd-345c-8ed7-f73ac2576395 | -9.55718 | -53.40557 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 866df9ba-0362-385c-a630-d2b7a3d1b452 | -10.05292 | -53.3457 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21f9dd73-5264-30d2-ab35-cd90ebcd133b | -10.04934 | -53.3451 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6727be45-59fc-3550-94e0-6b1864026dd2 | -10.04899 | -53.45687 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 25e51d82-c50a-389f-a149-ea2bee4271c9 | -10.04863 | -53.34929 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5457bf2a-5202-325d-acd6-a2d9db01a67d | -10.0461 | -53.45206 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cd30bea9-a86d-334e-8e1b-730276b894ac | -10.04392 | -53.44302 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 01e53eb7-cb6b-3315-b6a8-3515d89fb7ab | -10.04321 | -53.44723 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd09c015-bb51-3496-8894-723098280fa2 | -10.0425 | -53.45143 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8aef7383-5730-3cab-9312-4e53dfef8278 | -10.04179 | -53.45563 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0dcf583c-2a24-3b94-8984-2009259bf703 | -10.04109 | -53.45984 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37544e4f-e98a-32c1-a69c-5395c570558d | -10.04102 | -53.43823 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| f4518c52-3001-3e44-affa-0d28af0c6fe2 | -10.04031 | -53.44242 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 0f825d4a-5865-324c-8e2b-af57e4ce074a | -10.03961 | -53.44661 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 644d7b13-246a-3e1d-964f-a4a495c21950 | -10.0389 | -53.45081 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1eb94d4-bd04-3da4-a009-5e362d4d973d | -10.03819 | -53.455 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d82359a0-7cdd-36dd-827a-0e33a1bb4b04 | -10.03748 | -53.45921 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d73e629-c277-3031-9c22-779710dcca92 | -10.03671 | -53.44183 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 9b6934c3-5be9-3b51-b7de-08024068947f | -10.03601 | -53.446 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 72005675-b4b1-3ad0-961d-e87323d4f6fc | -10.0353 | -53.4502 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 77908bfb-8b8e-3e6c-8d5a-f3907d329413 | -10.03459 | -53.45439 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6f10044-62ea-395d-b25a-810fdfba81da | -10.03388 | -53.45859 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97ce104c-19e7-3124-9996-778df666e8f1 | -10.03311 | -53.44124 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 7dad0540-eaa4-31dd-bb1c-f79fc5831300 | -10.0324 | -53.44542 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 19401c83-093a-35dd-9645-a5449e1fe43f | -10.0317 | -53.4496 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 69983169-7aa1-3428-97ae-1c0aa89a5903 | -10.03099 | -53.45379 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1f064a9-769c-31ca-8945-de021bf88a5e | -10.0288 | -53.44482 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 9b4e69b6-f240-368b-801d-7dea5b37b2ea | -10.02809 | -53.449 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 173c8d2f-98b6-38cf-85c3-ecb63bc92c19 | -10.02739 | -53.45318 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a8ec2119-8e79-3a31-b7b9-99e03694e15e | -10.02449 | -53.44838 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 88ebbbf5-1eb1-3639-8932-14c7287b094d | -10.02379 | -53.45255 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bf9fa8f5-a59b-3a2a-b48e-9df9ff060c74 | -10.02308 | -53.45672 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 16629f8a-7d8d-3f93-b2ed-5995eef03a8e | -10.02286 | -53.44871 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 13643e3f-832e-3bd3-b839-baed4d8b64d2 | -10.02217 | -53.45288 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 40258ef7-1b27-3a13-9709-186d876ff08f | -10.02089 | -53.44777 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8449687f-ad50-3766-940e-425434f733df | -10.02018 | -53.45193 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9c42069d-2e01-3cd6-9274-5037d789b1d7 | -10.01729 | -53.44717 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4cf1b55d-c499-36a9-b599-25f36af164f3 | -10.01565 | -53.4475 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c2aa208e-9565-37a4-981e-2359a583b553 | -10.76326 | -53.54869 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 416bd8db-6768-37fc-800b-de6902807706 | -10.76255 | -53.55287 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62f94afd-0615-313f-b0b9-f34e76e0c401 | -10.76125 | -53.54952 | 2024-09-27 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f8ffe3c-475c-3c06-88ab-3e21c3439061 | -10.04695 | -53.4911 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a2122dc-efdd-38ac-982a-24e5dcabf3bf | -10.04476 | -53.48206 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 94ccb0a8-da63-31d3-99aa-5227cb593492 | -10.04405 | -53.48628 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e828d3a4-308a-3259-b982-ce1577ab7fe1 | -10.04334 | -53.49049 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35a41b17-c863-35fb-a7e0-1db6707b415f | -10.04327 | -53.46884 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 05fd1760-2722-317c-b1f6-ee4efa014205 | -10.04263 | -53.4947 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f15b396-8c19-33dd-a027-fe97696ac723 | -10.04186 | -53.47725 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| dfd3faa5-e377-3d2d-a5ae-3b581cefa98a | -10.04115 | -53.48146 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 6a7302a2-abf2-34f2-8c0f-c8130efb7a8a | -10.04044 | -53.48567 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| bc3d32e6-2357-33a5-ba70-18214909dc54 | -10.03973 | -53.48987 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb49b768-9f74-355c-9b1d-a5923f20a203 | -10.03903 | -53.49408 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39177b43-a419-3bff-ac17-8ec1aae37068 | -10.03896 | -53.47245 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cfc11911-0f43-3a60-aeff-fecfb9ea9451 | -10.03825 | -53.47665 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6b18e086-e9bf-3a61-a7d3-5dbe195268f2 | -10.03754 | -53.48086 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e62bb0c-a84c-3da9-8de8-cf7f7d70047a | -10.03683 | -53.48506 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d64b3e5f-1482-3df9-affb-4acab78cce2f | -10.03677 | -53.46342 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f913c715-b509-3e87-9e45-3a43b8c4ed94 | -10.03613 | -53.48926 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc6cdae9-ed28-37b9-80d7-1bfc3ec54bd9 | -10.03606 | -53.46762 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 35cbe2e8-8a3f-3c81-b5d4-b82cb6672f50 | -10.03542 | -53.49346 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e8e937d-d23f-3e9f-b3a5-9fe772486492 | -10.03535 | -53.47183 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e31b30f2-2064-3f37-8e5b-5ea8611b0dd4 | -10.03465 | -53.47604 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ff8f2798-963e-3332-b61a-7e88d33a81e9 | -10.03394 | -53.48024 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2dfccdc-d2ff-3925-9e98-9bb7f95a8207 | -10.03323 | -53.48444 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36517681-5dbe-34af-8356-6f2b30e805f8 | -10.03317 | -53.46279 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3873c383-f693-315b-9a84-64af6e704742 | -10.03246 | -53.46699 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8ff09e3-7b57-33ce-8683-3e61f30c3641 | -10.03175 | -53.47119 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 78953156-bbfe-3512-af7d-fcc8776b2a73 | -10.03104 | -53.4754 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 536fbf69-de6e-3f59-bd88-cd8939e54969 | -10.03033 | -53.47962 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 755cc4da-5a8f-3116-b0cd-a7341c326bed | -10.02962 | -53.48382 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 232a12cf-20b2-3cb2-85c4-d5427a33d9d7 | -10.02891 | -53.48803 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 33a7b165-7c0a-3020-baf6-fc3b44d0f7aa | -10.02886 | -53.46635 | 2024-09-27 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README97.md)
