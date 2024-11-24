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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 384a19a7-e344-3daa-9c11-e3c85c9ec34b | -2.77133 | -54.06625 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3b76a3c-fa2b-3b82-b906-fd88c968507f | -2.70014 | -48.82796 | 2024-11-24 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8013fd08-bbfa-353a-a309-b75e22306079 | -1.60565 | -46.88056 | 2024-11-24 05:14:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f051847f-9544-3c90-8293-b622bd3ca184 | -3.48513 | -50.08417 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75f204b5-518e-3869-929e-b1975d5f1a41 | -2.62259 | -51.80026 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51955dcf-7eba-362a-a142-295260502610 | -3.25672 | -53.70955 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5dd84536-af10-3efd-a3fb-8b832ddb8496 | -0.8187 | -52.8286 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 89deef2b-b616-3ec1-8e16-55b791eb3884 | -3.1067 | -45.78665 | 2024-11-24 05:14:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| becdb6e2-374d-3eea-bc76-abcbfc44214e | -3.68043 | -47.13325 | 2024-11-24 05:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f71270d-4cd2-3267-84d5-38f51a2ac6bf | -2.23232 | -53.66418 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87c7e428-a68e-37e0-826b-bab5bbabace7 | -1.24289 | -51.78773 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c02e385-aaca-3211-b743-0a59544bbcf1 | -2.82459 | -54.0226 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3bc50950-59a0-3164-85f8-5146e7e0a616 | -2.89504 | -54.01179 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aaf6d8fe-d2b2-3fc6-9a7f-80d9ed00ed14 | -2.81756 | -52.85727 | 2024-11-24 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eda604f5-b6de-3fbc-9aa0-6b362b6f8fa6 | -1.45057 | -53.39632 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0707e9bd-4345-3e1f-a7a9-d9c7f116aa47 | -2.44498 | -49.08986 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 471b0247-1c85-3530-a2fe-1d3248450481 | -2.7331 | -54.1141 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2737502d-889e-3b65-b30d-d15aa161d575 | 0.41898 | -50.8493 | 2024-11-24 05:14:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| adff82fd-ed04-3084-9cc0-673cce0c56a3 | -3.05267 | -52.7591 | 2024-11-24 05:14:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e0dd527-453b-3f2b-ad2f-210da4f258ed | -3.24915 | -53.2854 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a498b4b5-ab1a-3ec5-8dff-99c19f0f777c | -3.70343 | -47.60931 | 2024-11-24 05:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8de04dc-149c-39de-a8f0-9ca30b905eaa | -1.43095 | -53.4162 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2178fb19-f35e-3999-b0c4-4abbf51ca80b | 0.40696 | -50.86018 | 2024-11-24 05:14:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96695c6b-5d3f-3c00-b567-4dc489dd0f85 | -3.49675 | -49.93417 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33575a3b-47fb-313c-b77b-e8d873217e94 | -3.00166 | -51.55172 | 2024-11-24 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e3aae54-b7b5-39e4-bad0-841f28d9a6d3 | -3.11863 | -53.11063 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b1dba41-c09d-30f2-abf5-856e1135e6b6 | -1.61142 | -52.58087 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00edc8a5-33a0-3172-b57e-bb399b787a34 | -3.63304 | -51.51929 | 2024-11-24 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f4350fb-c829-323a-bab8-58a06ed3aa5e | -2.62975 | -54.38578 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6d20f048-b474-3491-a13c-552749aa49c7 | -2.1661 | -53.78859 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 889da4b8-7e9b-3665-9c28-7a41636f0c79 | -3.54544 | -49.88463 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a406d492-bcad-31d6-bed5-c230cca66fd7 | -1.62223 | -55.17325 | 2024-11-24 05:14:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06224083-71eb-309c-bb3e-431870c84bb7 | -2.01226 | -51.17511 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cf32822-a781-3fd4-82cd-57c6ce2a6d4a | -1.19679 | -51.97104 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 002d507a-bb28-3a5c-bfe0-6263e78c3d30 | -1.22814 | -51.7978 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b5ff62dc-8d85-3c5b-ac51-076711b42a56 | -3.25042 | -50.1204 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43f26070-9822-37c2-be55-921637ba3547 | -3.32413 | -49.89827 | 2024-11-24 05:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53c47451-1cf9-3558-ba7e-0ce64829da5b | -2.44577 | -49.08821 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82ff3968-bdb2-3f4d-b4a3-a6c3cd3ecd43 | -2.45601 | -49.0882 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51aabd26-ab5f-3202-af39-df156502a733 | -3.09855 | -54.29548 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3cf66bd3-0a61-3758-ba27-da79ed11c900 | -1.70115 | -55.01519 | 2024-11-24 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c73eb815-2f6b-32f7-abb3-1b2f2c40a341 | -1.39733 | -54.5054 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f41bb8ce-ddd7-3543-bfb1-05aa5b4a57f6 | -3.30024 | -50.3609 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1373d8e0-87d1-39b0-abaf-10a28532c2db | -2.73403 | -54.13283 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| daa7bcf1-a8a2-3926-89bb-c14ba327c961 | -1.22401 | -51.73947 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3daefbb5-61c4-37c4-9693-d4e83a0d2df8 | -0.87696 | -51.72205 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe2b0815-ef4e-3a4c-a95c-536749ae0937 | -1.6438 | -53.8755 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f8e0cab6-ed2a-34a4-9ff1-c6c39e3ae524 | -3.05539 | -53.22253 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8a1cd88e-81ec-3c91-ae91-883f8d0eb291 | -2.57872 | -51.88331 | 2024-11-24 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e896f087-88ca-3841-b863-8e3d4164b63e | -3.49064 | -49.91809 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| faec89ed-4144-3e27-b4be-8750b3c7a3f9 | -1.99006 | -53.29211 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9c626d23-3b13-3e17-9079-590ba7da2da3 | -3.68515 | -50.11493 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6a1dc4bb-d3d4-3f28-89bc-0c8249f76a1e | -1.89804 | -54.59207 | 2024-11-24 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7cb6b69e-f054-3d1f-ad85-b0c3aa5c345e | -1.61197 | -52.57725 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eb1f7b33-7b33-3ca6-b5e9-6d13ab000e52 | -1.48472 | -52.52083 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9db44f91-eb03-369e-92b8-c95eae838f38 | -1.12596 | -53.4039 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed2b1547-6325-3d2a-b9dc-eba85ba20286 | -3.2671 | -53.82467 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 63e31bc7-34ac-3075-b6e1-7500ab13f923 | -3.02154 | -51.36115 | 2024-11-24 05:14:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97823b51-6f0d-39c7-a832-d800ebf1ddeb | 0.41006 | -50.8507 | 2024-11-24 05:14:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1f452ffa-89e2-3f9b-a71c-01591f68db42 | -1.72812 | -53.2525 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bb3719a-9836-32fb-b46a-065e632e27de | -3.64707 | -49.88825 | 2024-11-24 05:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1a0a6cc9-9b0a-3ad6-be41-35f30ddcb7b5 | -1.43672 | -54.56278 | 2024-11-24 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4318d2d1-d20a-37ae-a1ce-a36d09bc137d | -2.63904 | -51.89648 | 2024-11-24 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 755ca01c-a189-36d5-9260-9cb50e1668d1 | -2.53962 | -53.99494 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 605ca6d1-385f-3851-a150-1b304afe1ed6 | -3.13334 | -52.98585 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 07bb5d00-a556-3793-912b-e402e14213b3 | -3.22428 | -53.92501 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4fc27c5c-6c80-396b-a40c-ba412a9ef825 | -3.64303 | -50.22413 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bca48cb2-375a-30fd-8b6f-87bc405cacb2 | -2.74136 | -54.11071 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 98e9486d-ebb7-367c-b736-ac4b484112de | -1.12981 | -53.40451 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c56d5a68-e93f-343b-b347-d0693f35f095 | -1.69905 | -52.60483 | 2024-11-24 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ca48597-fdca-3c46-bd77-589d9a2265af | -2.61193 | -54.25214 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 23906230-2e5f-3ca0-9051-ba1be0aa735c | -2.70542 | -51.99324 | 2024-11-24 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c1ceba8d-55b8-32dc-988b-1521f05d8a79 | 0.61386 | -51.7743 | 2024-11-24 05:14:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6547cdd3-f36c-357b-ba59-9af69936841b | -3.22289 | -53.93429 | 2024-11-24 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88bf2a17-51f6-3577-9b1f-b9ff002eca37 | -0.84129 | -52.54803 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e37b4e4a-6d59-358a-9933-fd5990504f00 | -3.25013 | -50.12244 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bdc6795-29a1-3f6d-96e0-301f2c4c268b | -1.11309 | -53.39985 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4eb069df-bb08-355e-b43a-8c49e34d618f | -0.95465 | -51.64739 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3d43f2b-8acd-387f-99de-f5e56e884705 | -0.95934 | -51.71693 | 2024-11-24 05:14:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a1396ee-da61-39b9-810b-8f0573be1112 | -2.61791 | -54.25916 | 2024-11-24 05:14:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5bff0b94-0cd4-339c-af57-f04717a364c6 | -3.03853 | -49.44999 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1960153a-4406-33f5-a989-19824dbf439d | -2.28594 | -53.63036 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe864e71-00d4-386f-adb4-0daaaa4b152f | -0.95896 | -51.64806 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a82b8a91-5259-3fe1-8739-d470f50ff88c | -3.53486 | -50.44366 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1161259-c488-3ce9-9b12-7cc85e7437ca | -3.04464 | -49.44451 | 2024-11-24 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 12c23acb-8877-3858-932d-e9cd62296c55 | -1.25377 | -53.32053 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70c612f8-dbb4-3182-88d6-38b2ec9b96b6 | -2.06856 | -50.31405 | 2024-11-24 05:14:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00b530c3-41bb-348c-8fab-b320707514ce | -2.15336 | -50.62011 | 2024-11-24 05:14:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f64f4189-aec9-3bf7-b079-87469ca6a376 | -3.64437 | -50.88808 | 2024-11-24 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3a66c73-d9da-3c97-be5a-75dfca523cd0 | -3.27369 | -53.01443 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea8378cc-1240-31da-b2c3-223f88538f46 | -3.05888 | -53.22651 | 2024-11-24 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a803363-0b8e-3416-8b65-262525e80450 | -2.85296 | -53.96531 | 2024-11-24 05:14:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b8d747da-c6c9-3ebe-8a52-d2a48d4530bc | -1.8374 | -46.63958 | 2024-11-24 05:14:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 343d1d87-1e48-3484-b2b7-0bf8f99aa556 | -1.43237 | -53.38201 | 2024-11-24 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| efea831e-1a06-33fe-8c76-f52b813835ba | -1.13881 | -51.67785 | 2024-11-24 05:14:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88cc2ce7-4757-37db-99ea-fce9db496ac9 | -1.69573 | -55.02661 | 2024-11-24 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d06a1b0-8e5d-38b5-80aa-35c82d43a80a | -3.17639 | -54.31837 | 2024-11-24 05:14:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 444205f0-386b-326c-ba88-7bd8582d6951 | -1.60305 | -54.95227 | 2024-11-24 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9a6a5c96-0f9f-3439-819f-560a89af8640 | -1.60537 | -54.4129 | 2024-11-24 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ffb75128-56a2-3888-ae45-71b879101717 | -0.2553 | -51.59198 | 2024-11-24 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README75.md)
