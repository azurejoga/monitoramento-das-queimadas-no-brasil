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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 590f17ee-6b35-32c3-b7d4-ae97fca2062e | -4.94452 | -48.24036 | 2024-11-09 04:55:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5c5d566-0463-3553-a7c0-111b67b83e11 | -5.93115 | -43.65136 | 2024-11-09 04:55:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5263c585-2eb7-323b-b00a-289eb31dd60b | -3.25102 | -46.47448 | 2024-11-09 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c201c307-014f-397c-8e09-ddc25cf3da1d | -3.10808 | -54.15612 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87fe07e6-3caa-3337-b84c-81a42f3e873a | -3.97938 | -48.40583 | 2024-11-09 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f5a76ad-ee81-3802-91fc-e37f0167428f | -4.20045 | -48.39762 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d96f186c-c670-3f04-8830-ef339072f528 | -4.82605 | -47.31783 | 2024-11-09 04:55:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66d9bfa2-bf1c-329e-87ea-3f647f117151 | -4.05935 | -48.31426 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 339f72c3-a699-3b7b-a287-a26c1de4c25d | -2.60819 | -51.30195 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88ffdbb1-7b1d-3786-a6b7-ab1713488b78 | -2.81894 | -52.96651 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 584e0910-79ab-348f-9763-5007eef96f47 | -4.76487 | -49.48537 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43d631f9-ebdf-3047-9b94-8f0c9039bbcb | -7.4603 | -43.57772 | 2024-11-09 04:55:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c4d87bc-58a9-3fc6-8844-a3be97d97205 | -1.21774 | -52.13116 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50b49341-85e7-3c23-88e7-e5628ad1636d | -2.58299 | -49.12803 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4b7cdf2a-f4ca-32ee-8ba5-9f5af1528cb5 | -3.75345 | -54.6389 | 2024-11-09 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db00b307-c925-32eb-8b86-7bf50932460b | -1.35683 | -51.40152 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a53191d6-73e2-3a90-a063-12933ab30063 | -2.88507 | -51.74528 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a40121e0-587d-3671-aece-a8547484782e | -3.04292 | -50.36148 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52265147-7dc8-37bf-b5af-e9370198261e | -2.81479 | -51.81177 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fbcb4371-ffe5-3505-84cb-90ee2a371cca | -2.40634 | -53.63326 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd62ea6c-ba76-354b-9cb0-757747710abb | -3.35242 | -50.12444 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 401ec06d-cf40-3ea0-afa8-35c1860d70df | -2.20835 | -52.78238 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce57bc1a-b167-30d7-a395-a11254c8a33f | -1.38759 | -52.21128 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b42c5b5-2c0e-3368-8d76-5354ea4657d5 | -3.04802 | -51.14075 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c9830fe-4857-3338-8883-2707b61e1187 | -3.57092 | -50.54756 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86f875ed-2264-317d-931c-7c280acd0899 | -4.20576 | -45.85493 | 2024-11-09 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62733cd0-f0ce-3c05-b0ba-ad38003c76b5 | -2.24538 | -53.7714 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cde8f663-2081-3e17-88ac-2e3ccfc99388 | -3.05083 | -47.691 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ae70a07-6d90-3be3-a2ab-6ec7aa8e7e04 | -2.2053 | -50.3408 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99c8815e-7292-33de-ba01-1061323b77d1 | -2.37427 | -48.57612 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b494a226-a903-3b36-8f7b-6f48af84bb53 | -4.01523 | -48.3001 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78d6c734-87e6-35b6-aca0-9c255c3d4158 | -2.11597 | -50.85135 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8965e584-d6d9-38a2-a744-35ca41e395d7 | -2.38224 | -53.74301 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a2269ea5-e1fe-3926-b478-81b47acff4d0 | -2.61162 | -51.30247 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b1c9cc7-6e1b-3209-b7f6-22832ad871c9 | -5.50518 | -47.17148 | 2024-11-09 04:55:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1935eec1-308d-3df8-a046-386ed29c131c | -3.16117 | -54.48081 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42c138de-cb66-34d9-a5bf-b805f3cdf48f | -2.42688 | -50.49497 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f4930eb-a772-3d29-b322-2accf4422128 | -3.44822 | -51.46545 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a73700f-ecb8-3de8-a5bf-dce76083bfb3 | -2.55401 | -53.98384 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b183d9d-fd19-3247-95bc-7fe9659c82b0 | -1.05918 | -53.35489 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 879d182b-4661-3757-aa85-bb357e40fc78 | -1.98738 | -52.29726 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed1e3d8c-0349-3cdc-a54e-151ddfc8b5a8 | -1.68809 | -51.91644 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc29e6fc-a550-3cb5-95c1-5058f26e98a5 | -3.09498 | -51.29471 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe5ab125-bd99-33fd-aa18-f296a95fb97b | -2.3634 | -52.69727 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 66e14c8e-6d52-392a-95da-af2db75f920f | -3.96339 | -48.12211 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd074d8a-a929-3519-b502-2f2e02a2fdb5 | -3.5544 | -49.91982 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2cfb7d43-bfbc-3624-9a81-b8f31f220245 | -2.11025 | -46.20402 | 2024-11-09 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1e67aa1-fdf0-3e39-b51b-28c8422afe71 | -3.53863 | -52.16763 | 2024-11-09 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb923c9f-1e95-3946-a6bb-ea16f13b8aac | -3.68238 | -51.30394 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5d3bb8ef-46b2-3e6c-999f-6f89c778bb41 | -3.97823 | -49.78793 | 2024-11-09 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 44a6da6a-4b5c-3fda-afd7-ac304bebfda0 | -1.84213 | -52.33548 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5d057f7-d042-349b-8e0a-9a4d7d5113fa | -2.85604 | -54.10561 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebb25e70-4986-3c05-9836-2e689064b9be | -2.96361 | -53.87346 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9548a923-d590-361a-ba4a-0ab6df406e4b | -2.30916 | -50.67101 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbe29b3f-10ef-3cea-912d-3007f4629b8b | -4.35233 | -46.82026 | 2024-11-09 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39808b54-5e07-3f94-b631-388ac3d7443d | -3.1365 | -49.71658 | 2024-11-09 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 660d14c6-4a24-3b5d-b8a7-e155bdb83151 | -4.09585 | -48.32306 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2276171-c3c3-36fb-9013-819011352efd | -1.14596 | -53.65977 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 30bba42b-52b5-3746-9721-c1cd4c815e81 | -2.88903 | -51.74218 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d78045f9-1df4-3c41-984d-839d15b4f3ff | -5.43049 | -46.94362 | 2024-11-09 04:55:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4995e472-3d9a-39d3-babc-144ed7276a2f | -3.88689 | -52.39278 | 2024-11-09 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cce0abdd-210c-3f07-943a-559fce163a96 | -1.61527 | -52.65816 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c1a071d-25e7-3aa3-bb96-190c02c8fb8c | -1.4459 | -53.0023 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7301a6ce-0003-3c3b-b754-f7ac479dcd60 | -3.51013 | -51.67519 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 11dc6e38-6611-3038-9bb6-ecfb44706432 | -0.04299 | -50.78753 | 2024-11-09 04:55:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c0c966d-7168-3369-a50c-6ef87ba429c5 | -2.06228 | -53.27855 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8142e59-0004-3084-9aa1-daa7c8141b4a | -3.04704 | -50.3699 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c53ddda4-568d-38f7-ab99-ce780e5c5257 | -2.95972 | -48.02814 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7da72958-055e-3875-ae8c-8f3be4414e2f | -3.95671 | -48.16688 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fc24cb95-3119-3e8a-a59b-edfda2e54411 | -3.50199 | -51.02332 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 721b52ba-175c-3828-a29f-d3e36be33be7 | -3.11484 | -50.14328 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 14f1d5f2-9ee2-31a7-8dca-e2c5e1dba9f0 | -3.03278 | -50.35577 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3756793e-c32a-3eef-a76b-4abd3c8cda91 | -1.33801 | -54.6085 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 325fad85-72a4-3ea7-8c69-37efbda396cc | -3.2549 | -51.13197 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0efbded4-4efe-3f6e-bd48-b189da2283a9 | -2.81925 | -54.01408 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 103bae72-de7e-327e-b863-8806edf9230b | -3.82613 | -51.91005 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b588bf0-0083-375f-9dd2-a1e9fc966cb8 | -3.64139 | -50.18121 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e26080f4-f762-38de-9041-5836562a6aea | -2.55456 | -53.98035 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3a477fe-08eb-3b2c-b9fb-3df7c3b7d38d | -2.99779 | -49.2392 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| a5908baf-2cf1-301d-8a85-8c65357356d9 | -2.15632 | -53.69366 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c65a938e-742b-3002-b13c-ea8d9ca435db | -3.07146 | -50.98797 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1d21846-b3b0-389d-95d4-4fd82198947a | -2.21922 | -50.88191 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e8552af-7e18-3748-86b4-0775f45e988f | -3.05604 | -53.99435 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5fea7e26-bc12-36da-be51-e228307dd178 | -3.01518 | -53.43913 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58e6c5b3-9eae-3698-b046-7d2d243077e5 | -3.76504 | -51.76584 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5ba1984a-9829-353f-838d-53dc587317f9 | -1.24677 | -53.38795 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59489f4b-f422-349a-8c22-2082e70e4244 | -2.40688 | -53.62981 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63038bae-2c6a-31d4-b085-bb245d4a10a0 | -2.06614 | -53.27562 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7bde2079-d402-3989-96ac-9ffd90331d82 | -3.25439 | -53.7485 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62c4d704-9844-3c65-9b19-560f9ba02a94 | -4.40135 | -49.40899 | 2024-11-09 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e9a2b68-b8d6-3843-a985-49db794845ee | -2.88934 | -53.31664 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50f789b9-f448-32d3-be70-6178b3dd0779 | -2.63298 | -54.65809 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c975ae0-04a9-3e2e-a4b4-d2f41441a733 | -1.15543 | -51.99295 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0707e72b-a35f-3cd7-97af-b7f7adb22bef | -2.23387 | -46.55465 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b59d271f-2967-3cbc-be4d-c0ec9af43d4a | -2.31086 | -46.48156 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 777084c3-d2c2-3ef9-8085-606f5433beb6 | -1.51677 | -52.18848 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 28e70f50-b0eb-36c7-9c65-b290679666a6 | -2.57112 | -48.18121 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2dc30d4-f8b4-301d-948d-81f6884c596e | -2.84545 | -54.08607 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e26d5fa2-34ea-385c-ae86-416be18af3a1 | -1.52295 | -52.21442 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f3e57b85-5e95-3a9a-8109-65fa54a024ca | -3.0822 | -50.56964 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |


[Clique aqui para ver as próximas entradas](README90.md)
