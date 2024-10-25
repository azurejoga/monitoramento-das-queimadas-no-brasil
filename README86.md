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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a74288a-85cb-34e8-941a-5ad721442004 | -4.57873 | -49.49564 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c63f047e-cd96-3d22-9ccf-438d53a598e7 | -4.57798 | -49.49391 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0bafb52f-2608-3684-9678-e6874582dd24 | -4.52961 | -49.58989 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5efd029a-2540-304d-b2b7-cf8679ef99ff | -4.44608 | -49.6579 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dc547067-6dee-3038-8d02-ffb252cd201a | -4.44575 | -49.65873 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e56afc93-32f0-3e88-b7bb-81b55eb75ab1 | -4.43403 | -50.13972 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8738e62-656f-356d-96cc-4617270a1872 | -4.42474 | -49.80425 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10343c5f-c1d1-3796-92d5-3f1fbf8ccf18 | -4.2715 | -49.66869 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 53bab1f3-f185-3960-b524-7c13e201f113 | -4.26671 | -50.61189 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10f30e6d-415d-3b2d-9165-715661ba6b07 | -4.2388 | -49.9159 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e7a1697-21ae-34b0-9f88-2ae62db71937 | -4.23529 | -50.63294 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 79691fb8-42cf-3d91-89a5-5916d071e951 | -4.23486 | -50.68914 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1879d0e7-c408-3fc4-af56-9a29a7d661e1 | -4.23467 | -49.91529 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 278c05bd-0416-3677-b374-4ee30ba04d16 | -4.2341 | -50.69421 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ff27b87-e8b0-3850-84db-c5ced72414c2 | -4.23248 | -49.72961 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 603d0d84-bc4a-3547-a62d-065512016474 | -4.2321 | -50.62737 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ca08ad27-4cbc-30d1-b2a2-d9074cafd736 | -4.23192 | -49.73344 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3d648260-c285-3f4e-82d5-b43bd2b2a5ae | -4.23135 | -50.63237 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 632cba9a-e10d-33ee-b64c-49afb482a4cc | -4.2306 | -50.63738 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4c4a41d2-da5f-322d-b86d-b3801d6da482 | -4.21389 | -50.50524 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84bc4ab5-ef05-3645-b3e2-e8767d3247be | -4.21075 | -50.50769 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20911e3e-de6e-341a-9e4f-d32b87ea079c | -4.18561 | -49.40375 | 2024-10-25 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 086c10e7-fcc6-330f-b0c0-48c167e5dec8 | -4.13883 | -49.80569 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc81c22a-c89f-378c-a54e-364ed0b409c2 | -4.10749 | -49.29015 | 2024-10-25 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b0d3c595-4e5f-33bd-b5b9-781fd839bcc2 | -4.06716 | -50.03357 | 2024-10-25 05:01:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c8729bbc-0832-3313-ae96-19d23e3f7579 | -4.06662 | -50.03722 | 2024-10-25 05:01:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41791127-45a1-396b-b9ff-8ace5fd604aa | -4.06332 | -50.0338 | 2024-10-25 05:01:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e91bf59e-835e-3891-97db-638aeb11e808 | -4.06306 | -50.03304 | 2024-10-25 05:01:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0abc8e7d-879b-3350-ba71-5a3f2f0c9182 | -4.02271 | -50.4452 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 721e2762-b47c-3693-b1d4-54544ffeae24 | -4.01924 | -50.44114 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7faa0973-4e07-3fd0-b8c4-80b78146ea49 | -4.01873 | -50.44459 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53545464-f5f6-395f-8817-59848a90e7b0 | -3.99257 | -49.27858 | 2024-10-25 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fc2fd60-4658-3a63-a647-e6aee0a68e33 | -3.97936 | -49.79502 | 2024-10-25 05:01:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68c6d386-e185-3b71-a93e-b4cf41069571 | -4.88953 | -50.68095 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1eb31bc0-2f36-37f3-bf6b-0d389ae6f529 | -4.84232 | -50.9152 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bddc16db-ae69-38c9-b4dd-6d633687f5c2 | -4.81796 | -50.89105 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18cc6a40-9be8-3f31-a799-b68099bc2b37 | -4.81406 | -50.89045 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0f83326-4bf7-3f13-a260-8c4056ba1efc | -4.73905 | -50.69244 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 336d1ed1-53be-3fb0-b0b3-e38c7343cac2 | -4.72489 | -50.7882 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff24f13c-7a40-3a56-86b4-13bcf2b9a881 | -4.72097 | -50.78753 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e1df45c-0957-3d47-a52e-9ad6e2737b6c | -4.61574 | -50.79544 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c23cefd-e98d-3ff1-92a0-e037471028d2 | -4.42061 | -50.78692 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d579dc05-26ac-39ef-b8d1-3c7590456181 | -4.39995 | -50.52713 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f7ae82b-bfa5-3ff4-a1be-110ea364c2ca | -3.94386 | -49.88898 | 2024-10-25 05:01:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 09e3c031-ee7c-3c06-8af5-7f1af93f3152 | -3.93997 | -49.3984 | 2024-10-25 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6154e78d-6452-31b5-8fdc-ca4c69e49414 | -3.93019 | -49.86798 | 2024-10-25 05:01:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6db16ae-2d87-38b0-8ced-f4e888b76382 | -3.92606 | -49.86739 | 2024-10-25 05:01:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02b69567-66a1-388f-acc8-09eefa01d336 | -3.88167 | -50.05128 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb5d2022-3de7-38db-89eb-2d49d967fe48 | -3.88113 | -50.05494 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b213490-eaee-3cd1-a476-f4748e695a33 | -3.87706 | -50.05433 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d94e4f02-a0fd-3d5c-a445-fea582b2aa4f | -3.81016 | -49.91806 | 2024-10-25 05:01:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d289ec1c-79a0-3117-a878-3fdfdd4a2f9b | -3.79726 | -50.03104 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7740a824-6b94-34b8-9dbd-b43a0b6cbfea | -3.7665 | -49.986 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08e6ffc0-6a27-329f-a264-760884ddf681 | -3.76392 | -50.38503 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ae27953-0a80-365e-9685-45aaeb3d2545 | -3.76046 | -50.38106 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48a61975-88d4-3cfb-bbe7-f946ce1e4b45 | -3.75994 | -50.38444 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82f13d2d-39d9-3e47-adaf-d09ed0f83917 | -3.75942 | -50.38784 | 2024-10-25 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3aedd821-5a0f-300b-b19b-630dd7d6c281 | -3.7486 | -49.94277 | 2024-10-25 05:01:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aea07fe5-cefd-3436-95b0-ff8f8eb290f2 | -3.74804 | -49.94638 | 2024-10-25 05:01:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2e740bf-2776-36e5-a4cd-74cb320a4072 | -3.74791 | -49.94221 | 2024-10-25 05:01:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6238c3ce-e6ae-35d3-95e2-7f1647c2056e | -3.74737 | -49.94583 | 2024-10-25 05:01:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2983654d-ac85-352b-9cc3-cb11dcd5e350 | -3.74451 | -49.94212 | 2024-10-25 05:01:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b2b49969-928a-3c22-b07f-b007e508026c | -3.74395 | -49.94575 | 2024-10-25 05:01:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 88e16843-4fa1-3d97-b52c-5c4aa1cadc4b | -5.11185 | -50.72271 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a8066cd3-aec8-376c-beae-78cd87fb0a1a | -5.11108 | -50.72779 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f19b24c8-205c-3a27-9c42-bb6dace0699b | -5.10789 | -50.72209 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc1a8880-8b09-3dcc-8544-e973f153a178 | -5.10713 | -50.72715 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f46bb034-91f7-35a0-9d40-e94ab999e4b8 | -5.06547 | -50.44829 | 2024-10-25 05:01:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97f080df-0da5-3a88-8c5f-78bae99cd9e2 | -5.06143 | -50.44777 | 2024-10-25 05:01:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60e9f62f-d7b9-3528-a747-c1511471c821 | -5.04047 | -50.712 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 857c7c0a-f53f-30d9-a7eb-7eace2bff575 | -5.00529 | -50.84388 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f7011cf-c7da-3766-a494-5b93a8cc4a1a | -5.00453 | -50.8489 | 2024-10-25 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a8f5327-2b2d-3d3e-87bc-fc3933d41656 | -6.41646 | -50.78888 | 2024-10-25 05:01:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d974d366-3e69-3ffd-968f-1dfc67781a8a | -6.41596 | -50.79226 | 2024-10-25 05:01:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d1ed462-b895-3247-b6b1-02577388fbbe | -6.41241 | -50.78851 | 2024-10-25 05:01:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f995600-6601-3c74-b0d6-f55f1ec3b3cd | -6.41192 | -50.79181 | 2024-10-25 05:01:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d5165e4-6070-3eae-96aa-0cbd94d4e62e | -6.22206 | -50.87362 | 2024-10-25 05:01:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29ff4e78-00f8-3b46-95be-94b002f3ce67 | -6.22155 | -50.87709 | 2024-10-25 05:01:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d5d1bdf6-db8f-34a2-b06a-b12f9d6de6dd | -6.21757 | -50.87645 | 2024-10-25 05:01:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c2e8ef1-adeb-3c73-b779-aa9490f8148d | -6.21359 | -50.87576 | 2024-10-25 05:01:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ac0305c-7d2e-3476-b29e-ae62afd086ee | -6.21011 | -50.87164 | 2024-10-25 05:01:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ef2dcbe-0f1a-341a-9279-3d7723f20397 | -6.20573 | -50.86049 | 2024-10-25 05:01:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ebc4fb5-13f9-32dc-a14f-78e6f675efeb | -6.20228 | -50.85632 | 2024-10-25 05:01:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa3219ec-ed9e-39fb-8b58-6e0ec7ef8956 | -6.20174 | -50.85984 | 2024-10-25 05:01:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 619d1960-73ca-33ac-b8fc-16a3648981bf | -6.20122 | -50.8633 | 2024-10-25 05:01:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e841cc2e-4aec-3474-9615-f67cf96a7e60 | -6.19725 | -50.86257 | 2024-10-25 05:01:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02a99117-79cb-3694-8447-fde530f92764 | -6.19378 | -50.85855 | 2024-10-25 05:01:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5deaede6-7762-3202-9d2e-775d8e7f5131 | -6.19327 | -50.86192 | 2024-10-25 05:01:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b1e123b-ed4a-36c2-b67e-df37d501c7cb | -6.1903 | -50.85452 | 2024-10-25 05:01:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c211167-0531-3f14-af1c-521c9aea588d | -6.18979 | -50.85792 | 2024-10-25 05:01:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9992233b-2be8-32c3-8818-bdb217e8a81e | -6.1858 | -50.8573 | 2024-10-25 05:01:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc681fdf-14c0-346e-9f34-a4bf2a611e27 | -6.18129 | -50.86016 | 2024-10-25 05:01:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac79b19b-174b-3224-90af-10669ad4bb37 | -6.17679 | -50.86298 | 2024-10-25 05:01:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cbf2a31-6c50-3958-82da-bd728dd2fbd6 | -6.10732 | -51.11306 | 2024-10-25 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4a98b86-3818-37e8-aa1e-2e6561786f3a | -5.94988 | -50.87924 | 2024-10-25 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d3c73369-6a1c-3c80-a83d-bfb2bbd28809 | -5.79721 | -50.16606 | 2024-10-25 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 600470bb-5c4f-3937-9b49-2ba8652698ab | -5.79305 | -50.1655 | 2024-10-25 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb3216ef-1cb0-34c6-93c8-d33bc7ad1134 | -5.78725 | -50.17626 | 2024-10-25 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26c28a68-a0ac-35b1-9f57-05044217a2eb | -5.5538 | -50.4395 | 2024-10-25 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f07c833b-51ff-3dc9-b869-66a255ceb062 | -5.36085 | -50.93107 | 2024-10-25 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README87.md)
