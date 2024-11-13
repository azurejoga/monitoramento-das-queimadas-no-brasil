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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42f5cdf7-0829-397d-b193-6b99fa95ab56 | -2.72627 | -45.3015 | 2024-11-13 04:04:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a930e3bd-83ac-357f-9907-60bd9e4cc3ca | -3.32699 | -48.9811 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7f78f5a-39bd-39df-8c86-26824b195b7a | -3.49478 | -50.83855 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 53a96492-77f1-34e0-9f60-c2635b67d6a3 | -2.24705 | -49.33118 | 2024-11-13 04:04:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52aac235-738f-3883-8cfd-0872905bf4c3 | -3.06425 | -50.34171 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2ad59ce9-d402-3cde-8091-20a7ee1affea | -2.19218 | -48.38502 | 2024-11-13 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c940e5dd-c28e-33ca-be79-7ae9b4a5b947 | -3.34102 | -48.9894 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26255127-cad4-33a5-aca2-07e3794ebc67 | -3.00028 | -51.04111 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 19e2e27d-79b2-34c5-b46e-edb3ee476036 | -2.24831 | -53.7476 | 2024-11-13 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a4431f13-4b07-33d6-b8d9-d92feca32d9f | -2.60888 | -46.16982 | 2024-11-13 04:04:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a69b356d-8c7d-3132-8cfe-313b96fbdd25 | -1.65194 | -52.63136 | 2024-11-13 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 78e73e95-b5f0-39d1-90af-efb54354310b | -4.06877 | -45.87455 | 2024-11-13 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 18980c78-1278-30c6-83ce-65d41ebb5599 | -3.34362 | -48.97486 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ba37215e-6594-3dae-a3d9-ebc94c4ef87c | -2.21283 | -53.75058 | 2024-11-13 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0621b5ba-c9a7-3850-b26b-6bf5a6c77cc4 | -4.42023 | -45.95314 | 2024-11-13 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6af330a7-664e-33ae-b12a-7068f904bc0e | -2.46514 | -48.4514 | 2024-11-13 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbaa776a-7ce2-3ffb-bf8e-de787632032e | -3.4935 | -50.84602 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a46b758b-2d19-33de-b632-10bc68a59077 | -3.05326 | -50.33992 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1088da10-fe3c-3a38-babb-cf4462244193 | -3.35455 | -48.97082 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2d02da1c-4894-3675-bc5e-18aaf34e1b58 | -3.02098 | -51.09764 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1252057c-9141-3792-95df-5a40d973eaa2 | -2.71934 | -44.86166 | 2024-11-13 04:04:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27cb6869-c6ce-33ce-87e5-b4bf069cda51 | -3.46353 | -39.58326 | 2024-11-13 04:04:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3d66a9c5-72e3-33c4-a70e-33794943595d | -3.76917 | -50.69216 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0be6d4b-9ac6-3c4e-a563-1da04e887152 | -2.9901 | -51.03112 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 88bb4fac-766a-3cc2-a4da-57f46195ba58 | -3.17109 | -46.44893 | 2024-11-13 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a1b4092-3930-31db-9862-62057ebc7542 | -3.85353 | -49.11998 | 2024-11-13 04:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b504ed8-f985-35ab-a67c-841700a4c14c | -2.72314 | -45.29591 | 2024-11-13 04:04:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7969a94a-6cab-33b6-9415-dc2fc4faeabe | -2.24727 | -53.75396 | 2024-11-13 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cb4d87a7-4665-37c7-9eae-6b51bab33c87 | -2.43662 | -49.22047 | 2024-11-13 04:04:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93fc88be-8fa4-36be-b083-96d299fc6fce | -3.35538 | -48.96399 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a54405fb-9fd7-3672-a8da-421703e9313f | -4.07312 | -44.13862 | 2024-11-13 04:04:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eebf681b-350e-3e5e-b656-8b4728c2c2cd | -3.19222 | -50.28619 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68eb04a0-bdd5-33ea-9523-2ec6c039642d | -1.39135 | -52.39709 | 2024-11-13 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| be514d03-26a2-3181-b36d-9e93a9c92bb2 | -2.60637 | -48.25248 | 2024-11-13 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9a21561a-282a-35e8-b531-234a0716a246 | -1.41483 | -51.12073 | 2024-11-13 04:04:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4092f471-37ad-3971-8398-2fb69a0a8471 | -1.38976 | -52.39948 | 2024-11-13 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 535e7a7e-b147-3840-8e49-dd10cd13a5a5 | -3.29477 | -51.59492 | 2024-11-13 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7709b705-6662-30cd-b259-3f8edd5ddf77 | -2.28853 | -47.91442 | 2024-11-13 04:04:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e7610f9-1ad8-3366-bf20-1a9a003b9946 | -4.81707 | -44.35589 | 2024-11-13 04:04:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b16cd1e-db62-352d-a405-bb0215b8a128 | -0.03648 | -50.77653 | 2024-11-13 04:04:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87151047-ea6f-348e-81d2-ec1b34c512b7 | -1.39847 | -51.10924 | 2024-11-13 04:04:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c866f7ac-f099-3a21-ba2f-9b42ed7a9163 | -4.11456 | -46.48856 | 2024-11-13 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9dbfec9-5471-3754-8dc2-002ce56a1656 | -4.0719 | -46.45061 | 2024-11-13 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b334802f-64f6-3b93-9ea8-43cce539f932 | -3.76855 | -50.69587 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34944c82-2452-3bc6-a38c-b8f9fd355a8f | -4.45118 | -45.36989 | 2024-11-13 04:04:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03b50b7b-1e79-3929-8f4d-ebbcc0bdc323 | -3.05207 | -50.34705 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d2a135c2-8178-3476-bda8-98501e0e18e0 | -3.3504 | -48.96314 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 356c389a-2c26-3101-92d7-c9d03896b39f | -4.36553 | -44.10699 | 2024-11-13 04:04:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ed1dff92-a3de-3c94-a3de-302cb843bf75 | -1.71168 | -46.14894 | 2024-11-13 04:04:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7218080-40f8-3c0f-8cb9-33c39fa04e28 | -3.8422 | -46.01656 | 2024-11-13 04:04:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a95ac3f-1d74-30d5-9ccc-e3c2b48bf269 | -3.07093 | -50.33551 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| dbeceaad-4279-33b8-8685-b6edc27a17b1 | -3.33267 | -48.97772 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7f43b835-e69b-365f-b14b-552c3b1f6338 | -4.07406 | -44.75472 | 2024-11-13 04:04:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b90366a-289c-306a-ab2a-8b9737aae6e1 | -2.24147 | -53.74854 | 2024-11-13 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 99cc89ee-a196-3f25-8574-e2d757010d9e | -1.39776 | -51.11355 | 2024-11-13 04:04:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72e29a63-36f4-3056-99ea-1cf5a58a9924 | -4.12779 | -46.85631 | 2024-11-13 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f05857ba-a2a1-34a0-b99b-ccf743ae2a1b | -3.14895 | -53.24195 | 2024-11-13 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 11af9af5-6f34-38d8-8eca-fc07c35de658 | -3.76672 | -50.70668 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76c411a7-02e3-3ede-bd2c-f4ef7bfe6338 | -3.07343 | -50.35438 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62cbe7cf-3ea4-3264-a5ef-ac972a831090 | -3.9478 | -46.70889 | 2024-11-13 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d19a82d9-f51d-37ca-aa95-3fbe3c0d6c8f | -3.09405 | -54.30763 | 2024-11-13 04:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 92b28966-05f1-320d-a602-ed1e8f017210 | -2.65971 | -46.79317 | 2024-11-13 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 726137b2-ea5b-3e0a-b97c-a7f842e67c4e | -3.04348 | -50.331 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 87ad3aa5-bda2-3ba5-9e62-16e22e2abbb4 | -2.75011 | -45.7024 | 2024-11-13 04:04:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1ff0ba6-3f97-3fb0-805c-b2e9d69f3ef7 | -3.06485 | -50.33814 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 9d3d8079-422c-3d8b-b9a1-2e70b1e95008 | -2.71921 | -45.29528 | 2024-11-13 04:04:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2b80ff6-ad6c-3a74-8bc3-3bdbc0b7134c | -3.35856 | -48.97741 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 431cdf38-7ed2-333f-af2c-aed46ebbdadd | -3.34645 | -48.98749 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa48315b-598e-39bd-ac10-cf8a474a778e | -2.15846 | -50.65593 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e7de6416-913c-3080-b386-411e5932ff7f | -4.04971 | -48.31662 | 2024-11-13 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9eb873f1-ccf7-360f-a081-5d4b974d2f3b | -3.35144 | -48.98833 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 894032b4-6b20-306f-a80e-57ea5c6f7b85 | -2.99548 | -51.03879 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7987b50b-a664-303c-a04b-eca3143f3f46 | -2.10831 | -50.7 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc4cd24e-fd2f-38ce-9c28-bdbcf6366cf7 | -3.33986 | -53.21423 | 2024-11-13 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b89dd5a8-e396-38c3-809c-cc475b5c3632 | -2.45871 | -48.82748 | 2024-11-13 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf501b75-b7f3-32b6-ba6d-880682536fea | -2.99519 | -51.03609 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 3f3f83ae-828c-3b0e-871f-2fd430b1c79f | -2.66433 | -46.81944 | 2024-11-13 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 74dd40dc-4edc-34ea-ad3d-ff08658a8a5b | -3.10423 | -54.30302 | 2024-11-13 04:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7b49dc3d-8c9f-35b5-99ee-cda6417eda0d | -2.66212 | -51.72815 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0f884257-9844-3f0d-a788-67bef6eeb7e3 | -2.9848 | -51.34594 | 2024-11-13 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 825f66be-21f3-3f0a-ac0f-2778fe1ec685 | -3.25676 | -43.26628 | 2024-11-13 04:04:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1b4afbb4-fa0a-3d85-8523-b9e30406a4e3 | -4.42819 | -45.95454 | 2024-11-13 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 735dd3ca-1495-3a2e-a2f9-8d75fd2538ce | -2.11651 | -50.69715 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d6b6ff1b-3358-3836-8e0a-f85f511afd3e | -3.14805 | -45.97528 | 2024-11-13 04:04:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d76a62e-6f60-36af-a02a-ba16650e7715 | -3.23525 | -50.67259 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a4102d0a-fcd6-3d40-aeda-153f6ebd0395 | -3.2504 | -43.26131 | 2024-11-13 04:04:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 07712ffb-e713-33b2-b7e5-1cc165b89f88 | -3.76054 | -50.70939 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b55fa85b-3a56-3cb6-9bfb-957a576becf7 | -3.4822 | -50.84425 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fa0aad3-c7f6-31cb-a55e-58138af15369 | -4.33048 | -46.54588 | 2024-11-13 04:04:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1b112a1a-2180-38d4-9ea7-611c7bd8ab6b | -2.53289 | -46.32259 | 2024-11-13 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 871bec01-5629-30b4-8d4d-635d54cdd309 | -2.11034 | -46.6696 | 2024-11-13 04:04:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81feaff9-badf-3d15-b672-524a5dc8234b | -3.99892 | -46.53148 | 2024-11-13 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b27846f7-6b9d-36b9-9e36-97244f6a3aa5 | -2.11467 | -50.6969 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72687064-2299-3f78-a783-07c911b83258 | -3.02868 | -50.98291 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10f013bd-d275-3355-bf42-3d0c8b661fda | -3.16962 | -50.45565 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6d43c5c0-dd8e-3dc8-8665-798f9dd37856 | -2.97894 | -51.34489 | 2024-11-13 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efb8ce8b-f0c4-35d5-a6b6-9e28c4e8a855 | -3.3605 | -48.96589 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff3a43df-ce27-39da-a2d0-b08c75d0432e | -2.98548 | -51.34193 | 2024-11-13 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5a43ebc-1060-3412-a860-377529b6b57f | -3.34691 | -48.98465 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c275d68e-9c39-31a6-b4c4-7389b4449915 | -1.28317 | -52.48359 | 2024-11-13 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README16.md)
