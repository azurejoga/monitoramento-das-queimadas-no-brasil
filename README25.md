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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c519f33d-87d5-33cd-9244-db7b6e05ae5e | -6.11612 | -57.73461 | 2026-08-17 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5f24d1ca-dff3-351a-af9e-adc0f314cd9e | -1.53662 | -49.98861 | 2026-08-17 04:55:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a74193af-2c8e-3ed6-abf6-9df4ac58490b | -2.96109 | -49.26487 | 2026-08-17 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c34f743-c424-3afa-acfa-13f3d1faba56 | -2.95773 | -49.26435 | 2026-08-17 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41b15db2-c72d-374b-8f36-56d4810cf713 | -6.24552 | -47.76341 | 2026-08-17 04:55:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 627ca3b6-3afe-36db-a458-efc57282a2c7 | -7.47352 | -45.12203 | 2026-08-17 04:55:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ed57cfd-209c-3e8d-a5f3-764ddb08c488 | -2.76958 | -48.57262 | 2026-08-17 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 10d24422-cb00-36c2-b17b-2036ea158790 | -2.86075 | -51.81307 | 2026-08-17 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bdb7ac8-5769-3324-a9d3-669119d9f8e0 | -5.44868 | -48.91454 | 2026-08-17 04:55:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8cb0e70a-6b3e-370a-8e42-1b3e860535e7 | -7.45291 | -44.86707 | 2026-08-17 04:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64823746-750b-3929-8347-d01875655fcd | -4.36011 | -46.16428 | 2026-08-17 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d11ce93-8ce8-34f8-b353-7a7de73537db | -3.80748 | -59.33807 | 2026-08-17 04:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 694a07ee-61bb-351d-96ac-b18a7edc124c | -7.39899 | -46.82614 | 2026-08-17 04:55:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3e454ea-fe50-3172-b126-fd65395ac268 | -6.38912 | -45.68571 | 2026-08-17 04:55:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7445589f-a9c1-37f2-a1ce-7e93c56a60c5 | -3.80801 | -59.33491 | 2026-08-17 04:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94b55bfc-ae20-35e9-bbb3-363149fcadd5 | -4.35726 | -46.16139 | 2026-08-17 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 07037e08-d5f5-32b9-abfc-2d44fcfc3d44 | -7.17639 | -43.72126 | 2026-08-17 04:55:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 24a58ae5-a179-3e6f-b20c-07375aae2448 | -1.83676 | -54.48611 | 2026-08-17 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc61a34a-33d8-3ad4-8b14-183f7ba69ae6 | -7.45228 | -44.87135 | 2026-08-17 04:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b4de9d6-387c-3d8a-b1ea-dc076b0001e1 | -6.73901 | -44.68519 | 2026-08-17 04:55:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 193660b3-1a8f-3758-a662-03e18b51cba6 | -6.10572 | -57.71435 | 2026-08-17 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8bcbe2fe-75d5-3680-a6fd-2e068434cf3f | -7.17755 | -43.7203 | 2026-08-17 04:55:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f61cc3f1-4784-3423-904a-de7c34141387 | -6.31029 | -43.62186 | 2026-08-17 04:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf157a7f-eabc-3294-b802-fc6da71064d0 | -6.10638 | -57.73744 | 2026-08-17 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 48fd793d-7e44-391f-95e2-b2a47d893a3a | -6.11995 | -57.71224 | 2026-08-17 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0e2c68f8-b028-3b66-b9f1-41d18ceae623 | -6.11536 | -57.73903 | 2026-08-17 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0bae3b98-d0a6-31be-a960-99cc6fdbf57c | -6.5317 | -43.11622 | 2026-08-17 04:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| def4bbb6-905f-3107-bb1a-cdcd14f11dc5 | -6.53629 | -43.1174 | 2026-08-17 04:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92c70718-ddf7-3a9a-86bc-26d482b504cd | -7.3958 | -46.8205 | 2026-08-17 04:55:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92d2caf8-be2d-34c1-be24-063b2a4456c2 | -7.01652 | -43.79033 | 2026-08-17 04:55:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f53fb053-cadc-3678-a3a8-07685e651eac | -4.31915 | -50.2887 | 2026-08-17 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c8c3eec-456c-3845-8042-0787bcb6383f | -6.7118 | -45.36481 | 2026-08-17 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54ff697d-d958-379c-9cbd-b3c3b6c8545a | -6.11985 | -57.73985 | 2026-08-17 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0971601e-ec75-3412-8e4c-7fe9d44da460 | -3.4634 | -56.80096 | 2026-08-17 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00dd99f1-7580-3ac0-a28b-a8de7adc474b | -6.2535 | -47.76028 | 2026-08-17 04:55:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19614c9d-bc1a-3ea7-beb0-28ee91b479ac | -7.01173 | -43.78962 | 2026-08-17 04:55:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7d85c65-9822-3c0c-a721-e96a382c391b | -7.47292 | -45.12618 | 2026-08-17 04:55:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a21d2c0e-3d2b-3b45-a5f1-4ccaa44eb61d | -7.6139 | -45.72503 | 2026-08-17 04:55:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 867454ad-41ff-3d58-88d3-32c78fd7561f | -6.53208 | -43.1111 | 2026-08-17 04:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8f633e48-72b4-3c9f-bba5-a0bbc74c2a96 | -7.23922 | -49.88328 | 2026-08-17 04:55:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 012d1057-bffe-3835-b866-c97c40e920cf | -6.48335 | -51.60363 | 2026-08-17 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b529ae36-b915-3361-a935-6d2c66d64d90 | -4.10355 | -49.06289 | 2026-08-17 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6200b75-6097-3518-807d-e6c298c2c933 | -7.57684 | -48.44185 | 2026-08-17 04:55:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b72f5f6-f7ba-3f50-9056-624e406eda3c | -6.93598 | -45.44262 | 2026-08-17 04:55:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 274f2821-b4fd-3be6-b47b-c6cb4180c653 | -6.93157 | -45.45145 | 2026-08-17 04:55:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2db6def-341b-3f8f-81d4-0d3707b8f1dc | -7.45046 | -44.86983 | 2026-08-17 04:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9340082-66dd-3c16-a76f-81407ac0546c | -7.40218 | -46.83176 | 2026-08-17 04:55:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6cbb696d-0704-3fda-8101-77c7480f3376 | -6.23888 | -47.75788 | 2026-08-17 04:55:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b1dc7843-4687-3fe8-93e0-4a03880b83e9 | -6.74347 | -44.68604 | 2026-08-17 04:55:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99a13390-dc50-3444-b7c6-86d692f36f5a | -6.53052 | -43.12229 | 2026-08-17 04:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5cd1bc81-9237-3fb7-b1e6-5b17a685c2c5 | -2.95718 | -49.26789 | 2026-08-17 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f896cf43-53b1-3556-9f64-ccb3348cdc3a | -6.77811 | -46.33501 | 2026-08-17 04:55:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4f7fc98-87bd-3b99-9b9b-ce1d2020808e | -6.74409 | -44.68171 | 2026-08-17 04:55:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdcac184-50fc-39e5-89e3-7cc695a0dc90 | -6.1102 | -57.71518 | 2026-08-17 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dec60832-040b-3dfc-9b83-9b67d436d521 | -6.38309 | -51.74405 | 2026-08-17 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c82eb26-2ef0-3403-8217-1515c2bc0477 | -6.24187 | -47.7628 | 2026-08-17 04:55:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2e8a512-ac3b-3fde-ae23-d87e9681d8b4 | -6.21411 | -47.72361 | 2026-08-17 04:55:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 903118b9-1761-3ecb-92e4-2fed65911d34 | -6.10559 | -57.74203 | 2026-08-17 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6d0c443b-db80-3ec0-a02e-ea57f447b1a0 | -2.76675 | -48.56843 | 2026-08-17 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 836c791c-d7fa-3eed-803e-5c2b891ae286 | -0.83683 | -47.35954 | 2026-08-17 04:55:00 | NPP-375D | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5d53985c-eaaa-3d25-8b24-d07d60ce532d | -7.17679 | -43.72552 | 2026-08-17 04:55:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d6f39d08-7bc5-32fd-85e9-3674e0c57852 | -4.9463 | -48.40396 | 2026-08-17 04:55:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2307aa5e-e980-3056-a47f-7af120121bc7 | -7.18121 | -43.72202 | 2026-08-17 04:55:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32f051bf-eecf-36ba-ac59-bd4d01f126c9 | -3.89162 | -59.35025 | 2026-08-17 04:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8dfb0f44-5418-3af2-b170-da48f2e51ae4 | -6.02236 | -57.81378 | 2026-08-17 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dec72d8a-4d2f-3ff7-9208-6b64cec979ca | -6.53669 | -43.11689 | 2026-08-17 04:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3897dfd1-e929-3c67-84de-bd3524bce6dc | -6.53088 | -43.12178 | 2026-08-17 04:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2f8e1182-5737-361c-8537-c97bb78fc9c8 | -6.1206 | -57.73546 | 2026-08-17 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fb74cccf-feec-32af-8dca-d2fe2f2dfdc7 | -6.1191 | -57.74427 | 2026-08-17 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81f27df9-56ad-3e13-8b83-8e08f89af499 | -7.02309 | -45.90977 | 2026-08-17 04:55:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3cbcb0bd-aba8-33d7-a9bb-8bfe5229cc84 | -6.11087 | -57.73822 | 2026-08-17 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 620aa677-d2c8-3a21-a812-681e879e907a | -6.82306 | -45.3423 | 2026-08-17 04:55:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86bcc6bd-8a66-3fff-aebe-8300751a2d91 | -6.11164 | -57.73376 | 2026-08-17 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9d613047-3d29-3457-85d1-57c382abde41 | -6.53253 | -43.1106 | 2026-08-17 04:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 235cdb85-f68d-3598-adb3-36a913cfa0f0 | -7.23977 | -49.87975 | 2026-08-17 04:55:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36ea6ecb-3128-3706-99b8-b58b9cc99f5f | -7.45646 | -46.14767 | 2026-08-17 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f54fb00b-72e8-3a9a-90da-95ecd0c5572c | -5.76167 | -47.34694 | 2026-08-17 04:55:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9ada1c8-8289-3692-82b1-55fe5209e2b7 | -4.10016 | -49.06235 | 2026-08-17 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f4737d68-c89f-3c92-9253-5eb8b2767e64 | -7.45493 | -44.87056 | 2026-08-17 04:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6dfd4226-8fa9-3e05-859c-0c6676673a85 | -6.12136 | -57.73104 | 2026-08-17 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d709a210-5c2b-3de3-bb66-35b76ed9da0d | -2.96053 | -49.26841 | 2026-08-17 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5cacd2d-3b92-3492-acc2-63c3117a6749 | -7.45591 | -46.15137 | 2026-08-17 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00db3904-b728-3055-96c5-68dfee910629 | -6.03217 | -57.81084 | 2026-08-17 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6aee2fc4-546d-3326-9654-d69f0e90394a | -5.48803 | -49.09238 | 2026-08-17 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be0c60a9-d846-36ad-8eff-9b7324acfcd3 | -6.52631 | -43.116 | 2026-08-17 04:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| bde6f0aa-08a9-3c23-a0bf-c5506e240035 | -7.24314 | -49.88343 | 2026-08-17 04:55:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 154f49ba-4876-331e-9eef-fd664c3fe54c | -4.9469 | -48.40007 | 2026-08-17 04:55:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40511700-321c-3369-922d-36f19261cae6 | -2.49989 | -48.13614 | 2026-08-17 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7444191d-0396-385b-87c8-603cb0ea7788 | -6.30549 | -43.62114 | 2026-08-17 04:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c34e7edb-c9cd-3793-ae9d-208c1ae4cb5b | -4.12424 | -56.32983 | 2026-08-17 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53c91e87-e8ea-308c-b121-06bba55cf319 | -6.38086 | -51.73661 | 2026-08-17 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| decd32d4-8afa-3d89-9ab5-8169bcca5458 | -6.7776 | -46.33845 | 2026-08-17 04:55:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f06346e-2dd6-3500-83c6-53a562cd2fc7 | -2.87867 | -48.85687 | 2026-08-17 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7c4e1347-747b-3ccc-8ad3-180ff5af8e0b | -6.02689 | -57.81454 | 2026-08-17 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59871358-afc0-37d9-8035-498389e37dc1 | -2.76617 | -48.57209 | 2026-08-17 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 58e45999-99fe-3e62-a30f-1f39a49b3ddb | -6.93059 | -45.4499 | 2026-08-17 04:55:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de3f4b8b-d36d-30da-9cff-0338664cb497 | -6.10714 | -57.73299 | 2026-08-17 04:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6aaf4fb9-20f8-3aea-9457-a091f9d004ad | -3.96516 | -43.10813 | 2026-08-17 04:55:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f098891f-cccf-3607-9718-d1778ed0bb0e | -6.95745 | -52.80777 | 2026-08-17 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ae235a3-0393-311d-8454-3084b7eca41a | -6.73963 | -44.68081 | 2026-08-17 04:55:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README26.md)
