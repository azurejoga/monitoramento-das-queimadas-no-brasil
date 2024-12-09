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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ee03539-2fd5-3b9f-b566-6ff5798c8d94 | -15.98171 | -57.17571 | 2024-12-09 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b72ba69c-ad81-378f-b79c-1eb46e1176d6 | -21.19571 | -44.9375 | 2024-12-09 04:23:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1b8efa1a-1b5c-3969-a1c5-b68f411ce8a0 | -20.41706 | -43.55293 | 2024-12-09 04:23:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2095d1a4-9b30-3afa-86cc-f04296d62f8a | -20.81036 | -44.56802 | 2024-12-09 04:23:00 | NOAA-20 | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 57e278c7-ae10-3e97-9b6e-b5370e1f9a9d | -19.30002 | -45.54491 | 2024-12-09 04:23:00 | NOAA-20 | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e8ff91c-8de1-3d0f-b42e-7a6b51025f73 | -21.03959 | -47.39505 | 2024-12-09 04:23:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 23b4ce94-ea15-35dc-a639-32202b6b0545 | -19.96814 | -44.21805 | 2024-12-09 04:23:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bb8c6a8e-c5f3-3b36-aa4b-3d830e15a7d6 | -3.2351 | -42.4353 | 2024-12-09 04:50:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 01a4e834-7646-3134-a73e-0103c868fff8 | -2.7823 | -53.2463 | 2024-12-09 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 4edf8142-100a-3e8b-a58e-0aae7efc7f58 | -3.2351 | -42.4353 | 2024-12-09 05:00:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 60c8d906-9142-3758-9263-7c55113760eb | -2.14827 | -48.04232 | 2024-12-09 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 80a8aa64-6463-3f61-a4dd-bcd3252197ba | -2.80228 | -53.24742 | 2024-12-09 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 821977bf-32db-33bf-bfb7-c802665b9cc5 | -3.07308 | -54.0733 | 2024-12-09 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4704d6c-ae19-30b6-8f68-5c36c97c6a28 | -2.90963 | -48.01763 | 2024-12-09 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 488b3f01-3966-3d13-8864-373ed0e77862 | -2.78324 | -53.24874 | 2024-12-09 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 89021b75-3d05-3f3a-9871-39dd2eca87df | -1.66061 | -53.41255 | 2024-12-09 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12db8543-66fe-3670-b891-33df4f1f2532 | -1.77774 | -45.9099 | 2024-12-09 05:10:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fd09e535-98c0-3894-82c1-83d4fb005d01 | -2.97783 | -53.86653 | 2024-12-09 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5c12b75-6191-3215-874c-5c18e109c2ae | -1.69778 | -52.56647 | 2024-12-09 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33c570d9-1715-3446-a2f8-da956465f788 | -2.14873 | -48.03925 | 2024-12-09 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 07160494-c3d3-3b0f-9a45-f8fbd487bcc2 | -2.46618 | -47.96558 | 2024-12-09 05:10:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 862b286a-eb09-318b-bd19-0d000e28baf2 | -1.7461 | -52.8077 | 2024-12-09 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1ae02bc-37e6-3ec3-8cc2-b5156c29258d | -2.78455 | -53.24018 | 2024-12-09 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| bf375ae2-9bed-3816-9e91-17dac8829321 | -2.04799 | -46.63756 | 2024-12-09 05:10:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e038c9be-a676-3ca4-a61d-e62813b8a543 | -1.6124 | -52.63971 | 2024-12-09 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4b21ac0-e731-356a-bb03-20da34b8fe20 | -2.62388 | -48.05663 | 2024-12-09 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9bc57a21-632a-31a0-b7ed-3b19157caacc | 0.80885 | -60.27313 | 2024-12-09 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc8df559-5a4f-30cc-b09b-882dedc9df7e | -2.63517 | -48.0613 | 2024-12-09 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4190da17-4758-3907-a27d-a054387178e7 | -1.61002 | -52.63673 | 2024-12-09 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2fa9e1dc-ecbe-30bc-ae97-42d9d2e80f2c | -1.78299 | -45.91505 | 2024-12-09 05:10:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27d2e659-1c82-38d3-974c-5969488d8ed1 | -1.61378 | -52.63732 | 2024-12-09 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2f58debc-0fef-3ee8-a942-d8f99f2c7277 | -3.1063 | -53.75922 | 2024-12-09 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ff92ed9-e98f-3230-99a4-d8eb8a3972a8 | -2.62315 | -48.63441 | 2024-12-09 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10193897-91d9-384e-8913-c2c725eb9717 | -2.78692 | -53.24932 | 2024-12-09 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 82e632cc-1f2e-36c4-9e4b-012b8eab44f4 | 4.06304 | -61.16093 | 2024-12-09 05:10:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 43f296e6-933e-3376-a66f-2a50c7b78a04 | -2.62481 | -48.05967 | 2024-12-09 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1ba221a7-389e-3bdc-8d4f-61312fc888a6 | -1.54545 | -52.67551 | 2024-12-09 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dacc4a58-6843-3e52-834b-99824d7c2130 | -2.63376 | -48.06137 | 2024-12-09 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e69574f-27d1-3f90-9d3c-dc1ce18a7961 | -3.48306 | -52.82887 | 2024-12-09 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec8945ca-8675-364b-9b10-a24c465f3a17 | -2.62341 | -48.05978 | 2024-12-09 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 760ee01b-8a49-3c98-82b0-0c3e328c43c0 | -2.90916 | -48.02078 | 2024-12-09 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69e5c46c-afe3-341f-b21a-c34e7cb93792 | -3.10098 | -53.74572 | 2024-12-09 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 410a79cc-aa26-31f3-b58b-b2b5f1497996 | -2.62999 | -48.06047 | 2024-12-09 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f0d4b07-051d-3ec5-b825-33415421c43d | -2.47138 | -47.96641 | 2024-12-09 05:10:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a0ef6d8-3009-3618-b9d8-1168ed86271a | -2.7839 | -53.24445 | 2024-12-09 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 0917dbeb-c4dc-3130-9498-b45e7884bc2d | -1.61311 | -52.63519 | 2024-12-09 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5bc6b6d-3dd8-3912-8409-893f1840ede3 | -1.65998 | -53.41667 | 2024-12-09 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df86aa8b-85c3-3582-b91b-e5dfcb73496b | -2.62906 | -48.05745 | 2024-12-09 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f797e175-ecec-3fec-8a67-1e4a470020ed | -1.64551 | -45.91791 | 2024-12-09 05:10:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f333c42c-a4cb-30d3-bbf1-7b136bceecf2 | -1.64747 | -45.90513 | 2024-12-09 05:10:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ad2ef9a-b98a-342b-81a9-392f3be439c0 | -2.83508 | -53.05964 | 2024-12-09 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f9428824-ba34-3a11-b8b9-b2d9c15f5c21 | -1.5417 | -52.67493 | 2024-12-09 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b64b4186-e8b5-3439-a4ed-2d9d96bb83a4 | -2.83136 | -53.05907 | 2024-12-09 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee67779d-7fb4-35d8-ba73-dd0f864a26b3 | -2.91559 | -53.06933 | 2024-12-09 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e01e77d9-fd73-3f45-901b-4dbb3927245b | -2.62811 | -48.06368 | 2024-12-09 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2733cd43-a622-3054-bd5a-9b05d5a0b378 | -2.79191 | -53.24134 | 2024-12-09 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9477254e-333b-3a67-9697-3bc4b50cff16 | -1.6107 | -52.63221 | 2024-12-09 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ce1d3587-45b2-3e2e-ac50-d42ea9168955 | -2.62859 | -48.06056 | 2024-12-09 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 74016871-81c3-3974-8a4e-de1429a0d13b | -1.41366 | -53.48599 | 2024-12-09 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4947cc25-a865-3057-af76-fc5d6fc4d112 | -1.41723 | -53.48657 | 2024-12-09 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 251cf72d-e9f6-3cdc-aaa4-58281a1a6bec | -1.65083 | -45.9114 | 2024-12-09 05:10:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e0e9585-0282-3c26-8a49-764e4c708cf3 | -2.99671 | -53.04831 | 2024-12-09 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fddc15c7-a9e6-3bc9-9378-e55977d00d3b | -3.10538 | -53.24826 | 2024-12-09 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 117c7e64-c211-3cf0-b1ed-20830759acbe | -2.99364 | -53.04334 | 2024-12-09 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1f034c7e-bf93-3e75-95d2-67543bee101d | -1.37238 | -53.47686 | 2024-12-09 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 711e7cca-7841-39e9-8b08-2b3cd017f9c7 | -3.10907 | -53.24884 | 2024-12-09 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d77547d6-dbb3-366b-ac62-5853d85223ea | -2.62526 | -48.05653 | 2024-12-09 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e6f51a58-6112-3fa0-aeb8-85a8bd0c1209 | -2.62954 | -48.06361 | 2024-12-09 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5c1e373-9b39-31f0-95a8-b7898c3b1cc2 | -3.00111 | -53.04446 | 2024-12-09 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4d4f68ae-a351-3b40-9f43-00c2c2999b74 | -2.54827 | -45.3933 | 2024-12-09 05:10:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fcc8ca31-46fc-3320-b5c4-d747faf35069 | -1.65021 | -45.91567 | 2024-12-09 05:10:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6c849835-cf1c-3be0-b830-8dec387d4130 | -2.8635 | -46.71945 | 2024-12-09 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d1dcf0ea-b828-3fa9-931a-6fa4f8d281d6 | -1.77708 | -45.9142 | 2024-12-09 05:10:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 663624bf-3071-3347-97d6-1e3da5e25865 | -2.55445 | -45.39419 | 2024-12-09 05:10:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13cb1e03-9c41-3ab9-8bdb-069fa22e99bb | -2.46664 | -47.96245 | 2024-12-09 05:10:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fca205d5-9b33-3457-a113-8667e773be87 | -3.00045 | -53.04889 | 2024-12-09 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c1942aa9-f3bc-3a32-95a9-d065717eec13 | -2.62272 | -48.63729 | 2024-12-09 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f7cd994-3d7b-30ee-b6ac-3f1213714ad2 | -2.46144 | -47.96161 | 2024-12-09 05:10:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed066e2d-b526-30fa-b2b9-7bb5613bd2be | -1.60935 | -52.63461 | 2024-12-09 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08ba2fdd-f35b-37df-aa81-47add7c56d0a | -1.60864 | -52.63912 | 2024-12-09 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab37c65c-c589-39b2-8502-b16482593c1f | -2.83439 | -53.06408 | 2024-12-09 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e08c3095-f11a-3acd-b32a-d5ef4ad5f5b7 | -1.65205 | -45.91452 | 2024-12-09 05:10:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 773a6f6a-98fc-35c5-bfc4-ff48f63ef31b | -2.99805 | -53.03947 | 2024-12-09 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0b256106-2dd1-3aa2-a569-07ee3d189d29 | -2.78758 | -53.24502 | 2024-12-09 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 668ea663-c071-3a2d-9132-5323d77649a2 | -1.64681 | -45.90938 | 2024-12-09 05:10:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8c24c137-20c5-3aba-b0a9-32ed849dce66 | -2.54757 | -45.39808 | 2024-12-09 05:10:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6bb7de4b-ad49-3c38-bb29-aa7a4bed0db6 | -3.098 | -53.74105 | 2024-12-09 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4a61ca05-bb32-37bd-97c9-f266d690140f | -2.99738 | -53.04389 | 2024-12-09 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6efb0ac0-360c-3552-a0d5-e38d9689af0b | -1.87219 | -53.30498 | 2024-12-09 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 81accce4-9177-3c50-99b6-ce5f1c924d2d | -1.88203 | -53.28926 | 2024-12-09 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5b3c1671-179b-3af7-a355-b319e373f2fc | -2.99431 | -53.03891 | 2024-12-09 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 99009dde-389f-3cab-85cd-875f7abc8fd3 | -1.54102 | -52.67942 | 2024-12-09 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58048556-8220-3c5c-ada8-a08dd8f0b85f | -2.63044 | -48.05735 | 2024-12-09 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7c0f1824-0de4-3156-8103-e7936036156f | -2.86146 | -54.05976 | 2024-12-09 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cca914e4-ebc2-3a05-83b1-63f2c9908454 | -8.78736 | -48.74755 | 2024-12-09 05:12:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be218ad3-f604-3b2b-83b9-d917670c4f9f | -8.78689 | -48.75117 | 2024-12-09 05:12:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec9b8e9b-cbe5-3591-a373-a63ec3d05654 | -7.98294 | -50.695 | 2024-12-09 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b97e6599-42b1-3421-af88-da42f7ef2d07 | -3.58011 | -53.28143 | 2024-12-09 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 152fafb9-92aa-3352-93f8-3b31eaa787be | -9.51536 | -54.73582 | 2024-12-09 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdd4a4cf-a0ba-37d4-b30c-c3a7618856d7 | -3.8292 | -52.42405 | 2024-12-09 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README12.md)
