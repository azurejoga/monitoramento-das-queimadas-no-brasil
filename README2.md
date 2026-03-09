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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df935e49-d3ed-3120-90bb-072a4a985550 | 2.69237 | -60.2534 | 2026-03-09 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6fd315fa-dd18-3856-a4c1-8998fae5d808 | 4.25829 | -60.11182 | 2026-03-09 04:38:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 86c7f53a-5802-324a-8f96-af73401f3d3e | 2.8696 | -61.06737 | 2026-03-09 04:38:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 12d5dc84-f7d1-38c8-8c7f-487c2839d6ce | 2.70964 | -60.2566 | 2026-03-09 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fc7e0cab-a4da-3ff1-b18f-bc6c484e8955 | 2.70201 | -60.25157 | 2026-03-09 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9f03b720-08d2-34ab-b841-f48f1e0e906f | 2.32146 | -60.22677 | 2026-03-09 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 17d8f4d1-059a-390d-9bf2-3138b6e09fef | 2.8714 | -61.0607 | 2026-03-09 04:38:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f84fc459-a5f7-3356-bf98-2fcc228c7c06 | -8.44353 | -45.1316 | 2026-03-09 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 800e276f-70a4-35a4-95c7-3e4d8b9362b7 | -3.4203 | -48.33559 | 2026-03-09 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 74711efb-3383-3241-aaf3-0d4551a8b692 | -21.51233 | -57.53661 | 2026-03-09 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff4ed6f8-0600-3c86-a083-77f25c2eb347 | -24.4092 | -54.17747 | 2026-03-09 04:46:00 | NOAA-21 | MERCEDES | PARANÁ | Brasil | 4115853 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6a00ae7f-5e1a-332b-a54e-9ed0f397cc92 | -24.10635 | -54.30464 | 2026-03-09 04:46:00 | NOAA-21 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 479c2465-1f16-34b7-acf2-3ba91771de19 | 2.69827 | -60.26195 | 2026-03-09 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f330738-6062-3a31-983c-7287b4e79643 | 2.31778 | -60.22872 | 2026-03-09 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4da641e0-a5c8-3621-942f-55c5e57b5f03 | 2.85805 | -61.0944 | 2026-03-09 05:08:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ac4b706-9dfd-38c4-be1f-c49215fe45bf | 3.6195 | -60.83873 | 2026-03-09 05:08:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d60c06a8-b008-3862-a7e9-42782723b846 | 2.72677 | -60.35857 | 2026-03-09 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 76039b06-db5b-347a-b235-72a04fd2f0ab | 2.87079 | -61.08204 | 2026-03-09 05:08:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 091fba44-6ee0-38c7-8eed-97b6d5c588bd | 2.88028 | -61.07876 | 2026-03-09 05:08:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 749767ac-9b6d-3b55-b7bb-53e55621a2d3 | 3.61849 | -60.83498 | 2026-03-09 05:08:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87999b49-3e62-3127-b735-3cf266d3ac03 | 2.66093 | -60.63026 | 2026-03-09 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e96788c0-d2a5-334f-af56-f1f9aae79ad4 | 2.73719 | -60.36615 | 2026-03-09 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3f7c6ff-7cc8-3267-aca8-61ef9a4bc24f | 2.86595 | -61.11412 | 2026-03-09 05:08:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6216fd5-e250-3a82-8789-8f82b3760870 | 2.87954 | -61.07366 | 2026-03-09 05:08:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1ff6281-d4a3-302a-9a8f-f02caa433cf7 | 2.65775 | -60.64037 | 2026-03-09 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d971812b-62d8-3310-bc99-519dc5f1b9ae | 2.87953 | -61.0755 | 2026-03-09 05:08:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fda997fe-9008-332b-9ad9-39ccd6f59f58 | 2.71106 | -60.25542 | 2026-03-09 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2f8bbbf-ebdf-3ee6-b303-551faf2c9408 | 2.7059 | -60.25167 | 2026-03-09 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9633c6b8-35d6-3f24-9d90-ac29a3bf436e | 2.69894 | -60.26639 | 2026-03-09 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba2aeffc-f876-3e59-a044-552583c28054 | 2.31717 | -60.22483 | 2026-03-09 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 26117825-1ee2-3a79-b2eb-e18b556a4e67 | 2.69312 | -60.25822 | 2026-03-09 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1cdd1ab3-5432-3348-84ca-073062193238 | 2.66164 | -60.63498 | 2026-03-09 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1240fb69-c1f2-3925-8406-0e7f0747083d | 2.71038 | -60.25097 | 2026-03-09 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| afe33212-ba40-3b6d-914f-77161f64ccfc | 2.69693 | -60.25309 | 2026-03-09 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 10eb3ec1-1d49-3add-b428-19461408ab8b | 3.61926 | -60.83998 | 2026-03-09 05:08:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 79b02ebf-fa18-34ef-a01c-d067abf4c0b9 | 2.69378 | -60.26263 | 2026-03-09 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42aece8c-179b-3367-b143-73488807ac24 | 2.32158 | -60.22394 | 2026-03-09 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b5af536c-326e-3e59-a446-73f071dd3e33 | 3.38386 | -60.37894 | 2026-03-09 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 814f01a3-8070-3094-b23a-de572b7f480b | 2.73129 | -60.35783 | 2026-03-09 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a9bf6da-6200-37dc-8f23-1d70c9763f6e | 2.87157 | -61.08713 | 2026-03-09 05:08:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b701ed0-03d2-3726-bc47-6d8a5408148d | 2.69245 | -60.25379 | 2026-03-09 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 87dcd243-636e-30a4-8276-0edc1fc70982 | 1.99418 | -60.60844 | 2026-03-09 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 085c171c-056f-358e-bb3e-da82e62ab8e6 | 2.87555 | -61.08131 | 2026-03-09 05:08:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd981651-ca07-3d15-824e-80227c5001e7 | 2.66553 | -60.62957 | 2026-03-09 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19316884-1ead-3b38-8804-0bee00bd50c8 | 3.37929 | -60.37967 | 2026-03-09 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2e6220f-4589-35d8-a699-301a76ec2a0e | 2.86674 | -61.11923 | 2026-03-09 05:08:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 533de3fe-dd80-3c13-a6c5-254e7655e13b | 2.86994 | -61.10827 | 2026-03-09 05:08:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9525e4d-b08f-3ade-9628-8260920bab4b | 2.70657 | -60.25612 | 2026-03-09 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc2f448b-167f-34b1-bd26-8cae00bbd70a | 3.4935 | -60.75415 | 2026-03-09 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a67ff689-d101-306e-ba94-198d51d09837 | 2.70141 | -60.25238 | 2026-03-09 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4aadece8-6e63-3c48-a326-89a751954121 | 2.7358 | -60.35709 | 2026-03-09 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| edf7884f-a444-30d9-a887-f628cdf99dc3 | 2.86435 | -61.06443 | 2026-03-09 05:27:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f26a515-bd93-3a01-810e-c71bea1d9da5 | 3.38154 | -60.37772 | 2026-03-09 05:27:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c724b15f-2f5f-39e6-999e-5014458bb991 | 2.73678 | -60.3634 | 2026-03-09 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fc53b11b-2ed9-3f2f-b58b-5ac30a8ab2ac | 2.69581 | -60.25387 | 2026-03-09 05:27:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9a7295df-cc6f-3d26-a8e0-edeb712154d7 | 2.73732 | -60.36683 | 2026-03-09 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1205ad7-8616-3380-9fc4-9bcd9173b03f | 2.69856 | -60.24992 | 2026-03-09 05:27:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 87f3d8df-7297-3ae8-ae50-40c6aca65037 | 2.73239 | -60.35705 | 2026-03-09 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e525626a-f69a-3573-92d9-88379c8de2aa | 2.7057 | -60.25232 | 2026-03-09 05:27:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a51de189-3379-395e-b933-23002ab4973b | 3.37338 | -60.58348 | 2026-03-09 05:27:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2b18c41-4e2c-3380-9554-2a2322b63c44 | 2.6991 | -60.25335 | 2026-03-09 05:27:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fe1bd1b3-8b34-33b9-84dd-894f457d384a | 3.91659 | -60.25829 | 2026-03-09 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c81af496-1570-3ed0-86c4-3983e7050822 | 3.93004 | -59.91109 | 2026-03-09 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0509aff8-ffc1-366b-b0b1-7a9281f05d72 | 2.6547 | -60.63985 | 2026-03-09 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6bff6099-6086-30fb-a6dc-ee00da6be318 | 2.69359 | -60.26124 | 2026-03-09 05:27:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aef36196-b17a-3628-a385-23e3b0b0714a | 2.709 | -60.25181 | 2026-03-09 05:27:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 23de8982-99e6-3cb2-b94c-2c66c8aeee5b | 2.69743 | -60.26415 | 2026-03-09 05:27:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 591bd3c9-d9f3-3e7b-a847-a7b794dd2952 | 3.6203 | -60.83543 | 2026-03-09 05:27:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a7b8f363-b835-387b-a4f4-7a5b822af9ab | 2.69251 | -60.25439 | 2026-03-09 05:27:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f99866e5-e87f-3b7e-90e5-efd0ffd9fd83 | 3.38041 | -60.39198 | 2026-03-09 05:27:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 404c9edf-6da7-348e-9d18-19a563ed0411 | 2.69413 | -60.26466 | 2026-03-09 05:27:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f12a0f0-4212-3147-91d2-3815723862be | 2.70516 | -60.24889 | 2026-03-09 05:27:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b9867edb-b178-3145-af1b-a07b66691cdb | 2.70186 | -60.24941 | 2026-03-09 05:27:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 987fd332-dd8c-3b3a-8e55-23f3de6ea3e0 | 2.66353 | -60.63142 | 2026-03-09 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 721270bb-915d-3661-b52c-9f1d10c06fe2 | 2.66022 | -60.63194 | 2026-03-09 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 684c888a-2cf7-3fc1-a46f-1a30b4b234dc | 2.92054 | -60.72863 | 2026-03-09 05:27:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f6752447-d400-3130-aa31-14dbb7bb7192 | 2.86103 | -61.06495 | 2026-03-09 05:27:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 950639e7-5d2e-39c5-8784-f61cdf151fb5 | 2.65746 | -60.63589 | 2026-03-09 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc657380-a1db-3432-bbf4-17c5880f0494 | 2.70846 | -60.24838 | 2026-03-09 05:27:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d39385bd-fe59-310a-aa58-33fe31167439 | 3.37987 | -60.38854 | 2026-03-09 05:27:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fd3606f-1b66-3762-9a5b-6299182b1353 | 3.72024 | -59.83199 | 2026-03-09 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6d92bb52-133b-3537-8aa2-ced04866925b | 2.66629 | -60.62747 | 2026-03-09 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c9109f7b-6beb-3b94-815d-396c5434b8e6 | 2.72525 | -60.35465 | 2026-03-09 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2f1b6dc3-a451-3ca3-b289-3d3a87d70f72 | 2.82478 | -60.7687 | 2026-03-09 05:27:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d86de8ef-1fcd-39a0-8679-4831d277827a | 3.69989 | -60.28506 | 2026-03-09 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45e0306e-62a6-3e10-a25a-c05858294d62 | 3.92949 | -59.90766 | 2026-03-09 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f66327f-17dc-3bf7-b0b9-05b5319466b4 | 2.7291 | -60.35756 | 2026-03-09 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d9e45d78-8eef-31c7-9f0c-55a4ab4414ff | 3.72079 | -59.83542 | 2026-03-09 05:27:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 43dbe35c-bdc4-3ec2-9a9b-e43d010dee8f | 3.38208 | -60.38116 | 2026-03-09 05:27:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db9f2b38-4111-397a-91ce-f75c9cda5d07 | 2.73569 | -60.35653 | 2026-03-09 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 749077b5-97fe-369b-bd27-4ca0f5b580c0 | 2.7258 | -60.35808 | 2026-03-09 05:27:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e0965ffe-b5f6-3753-9054-030018f4d82a | 2.69526 | -60.25044 | 2026-03-09 05:27:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| aba307e9-1292-3cde-8066-a939eb0ec258 | 2.39524 | -60.39603 | 2026-03-09 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e60e87d7-446d-3099-af7d-3ad3e33af1c6 | 1.86615 | -60.29313 | 2026-03-09 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 173ad23d-36f7-3877-b36e-19cc0a39c0ca | 2.31762 | -60.22563 | 2026-03-09 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e366a1af-1e22-3a9b-986f-b07477ce0f63 | 1.8409 | -60.30773 | 2026-03-09 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3759d0f-568f-3c85-a9ec-33f672532c98 | 1.70898 | -60.29013 | 2026-03-09 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b4c80802-5ec5-3804-a2cd-59f6ff535ae4 | 2.32037 | -60.22169 | 2026-03-09 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78237b46-612c-32a2-88e8-f84cffb6fb20 | 1.70952 | -60.29356 | 2026-03-09 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f13c241b-fcd5-3d60-92db-733698aa3a23 | 1.71227 | -60.28962 | 2026-03-09 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |


[Clique aqui para ver as próximas entradas](README3.md)
