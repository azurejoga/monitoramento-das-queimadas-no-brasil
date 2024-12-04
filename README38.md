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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b87a7867-ff25-39e1-9547-47855c312bac | -3.30007 | -54.16439 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0471f183-0c82-38d9-bd77-474cfa35279a | -3.12207 | -51.26778 | 2024-12-04 05:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 856cd8ba-15c7-3d03-8842-a5792f29b375 | -2.76459 | -54.04287 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d541c91e-d3fa-36e7-9c83-ce7761c508d4 | -1.26982 | -54.11951 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 897a4f4b-50a4-397c-904c-6e45bb3a799b | -2.67005 | -52.45182 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3014457-f58f-3d7e-92e5-6fa224c4fcab | -1.7543 | -52.63591 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4fe51eac-b38c-335a-b42e-f8c19c951dae | -4.26706 | -50.85244 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ec60b1c-499c-3243-a45b-29ee5a399782 | -2.37298 | -53.96034 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 130d35ed-126b-3fcb-ab65-9dd0b5c57b9a | -3.25495 | -53.6191 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7144a5aa-b380-3aec-b094-f97be98f34e2 | -1.62341 | -53.5294 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0521964f-1815-3b79-80b2-82ef5c69bd0c | -2.79373 | -54.11947 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1065b5e4-5265-3cc6-9b19-dc5b334b1871 | -3.07969 | -53.91635 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06502f9e-15b5-3582-a256-b6a76a3637c2 | -3.1885 | -54.48807 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1697a4de-36d4-37a3-958d-3a9d4341e514 | -3.0586 | -54.49265 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54033a56-4db5-31a7-bd4c-524164aba9a8 | -1.98387 | -53.14974 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0acec688-82fe-342f-9c1f-69270daebc36 | -2.62471 | -54.0893 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 293291fc-8001-3026-985c-e330bee4b270 | -2.86742 | -53.99329 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d149212f-d9e7-3d57-9b07-1a9920065236 | -1.58312 | -53.74516 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb9bfb25-27e2-3768-aef5-636aa3460f59 | -1.6954 | -52.33451 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e7bc21de-0f5a-3563-b801-fa4b653c5fc6 | -3.27683 | -53.24867 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 268db7bd-0e54-33cd-87b3-33c50e7db1f2 | -2.73729 | -54.04227 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57955a3c-26e8-3643-81a2-99895143e614 | -3.21261 | -53.11959 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2bc2269-c76c-3282-8a73-bd6d3a3d9c93 | -3.3293 | -52.23472 | 2024-12-04 05:03:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31f91283-5b74-378a-a8ac-570c0d322417 | -3.1039 | -53.09606 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a6a8ba1-26be-3dd1-adf5-c9bc85196c95 | -2.35731 | -53.92902 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5deb6367-f7ba-3934-beeb-cec995162049 | -2.80699 | -53.04436 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99fd5c0d-12b3-3ed9-b1ee-6883d0923c75 | -2.47312 | -53.70718 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0900ff1c-1a20-34e1-87bb-dc0487b14185 | -2.64032 | -54.09886 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0235494f-b629-3c1a-a0a0-139c165dfa02 | -2.98162 | -52.97693 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 586464df-30ee-36d7-a551-1c5465095d35 | -1.13047 | -53.79111 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbfcf6f4-ca28-36fa-89ae-9715186bfb24 | -1.96728 | -51.53899 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6822758d-71d4-323a-8b2b-3daa106214a3 | -3.08359 | -54.113 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4bcbbc4-f8b7-3004-a454-d393091a8ce9 | -3.12977 | -54.62488 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| b6ad4d28-d047-31d3-8829-d32a6e0cb9e7 | -1.64804 | -52.37969 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f85f150e-f25a-3d6f-b305-4aa1d433248c | -2.72985 | -54.31034 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7bf145e0-6eb7-3c90-b960-97cb42314204 | -2.73039 | -54.30684 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e2b7369-b346-318a-9eeb-aead0d033107 | -3.33687 | -51.6399 | 2024-12-04 05:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1d434f2-7f62-3b98-a128-1add61b8961c | -3.7635 | -52.08294 | 2024-12-04 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 598328ba-d8db-3694-84d4-a50b0a7784f0 | -3.03542 | -54.04771 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| acb2c602-9828-3bb3-b896-38ae5637220f | -3.12036 | -54.61989 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 037f05fc-786a-31d2-9f58-a22e80490c10 | -2.62082 | -54.0923 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eedb1f84-18c4-3933-93ac-8482b3510651 | -2.87028 | -54.0191 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2fe0bcf9-7e87-35bc-806b-5b4dce39a4a0 | -2.02756 | -46.33893 | 2024-12-04 05:03:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f463c25b-4bf1-3302-ae79-1d9b8928d585 | -2.00495 | -53.28435 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 498e4028-55ee-31ed-9f97-f360f797473f | -3.12124 | -53.98102 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ede3158-fd13-3e14-b8e9-6b9efa2a00cd | -4.04569 | -47.00404 | 2024-12-04 05:03:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b481aaa4-af07-3062-94dd-f663d7674f1c | -3.05954 | -51.71383 | 2024-12-04 05:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b642e081-68be-3482-9685-091ede6ebb8c | -2.9823 | -53.90894 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af1b0e09-2dee-3df8-bf88-5b81069a7419 | -3.40341 | -50.23311 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 159fca6a-b421-3baf-ad04-5c6c8b61762f | 1.07793 | -55.99541 | 2024-12-04 05:03:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d43a0e09-e016-3391-9927-98d29e201963 | -3.96466 | -50.56872 | 2024-12-04 05:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6fcc091-ddc0-3b06-b88b-f45e2414e397 | -3.60874 | -50.79751 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 46c8e076-2aa4-3943-9502-313d9bbf40a2 | -0.82361 | -51.62032 | 2024-12-04 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20b8cae9-48e3-325e-b9c4-f6b554d28e05 | -2.35558 | -54.48684 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ea69ea48-ae97-384b-9f2c-efa6084c6bc8 | -2.99893 | -53.82355 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df4ce7fc-2cbb-334c-8e7e-a3d0b39d0034 | -2.57869 | -53.68277 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e3b9b6a4-911a-3c1a-90b1-25a447ffab06 | -3.6513 | -51.12529 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3041db7-c05a-3b4c-926d-c5ccb4e78c68 | -3.26739 | -53.6285 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fc3520b-00eb-37e9-91ba-e12d646072cd | -3.03142 | -53.40909 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12cbf945-7066-36f8-aa45-3d6b843d087e | -2.02238 | -46.33807 | 2024-12-04 05:03:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5dad497-b734-30a9-99bc-bd682fd16842 | -3.26262 | -53.34177 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ed64bc6-89f3-3ed8-b42d-ba14d75aa5be | -3.15323 | -50.62371 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5ce5f64-1025-34c1-b6b2-88707184084b | -2.73797 | -54.08208 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a877b48-63bf-3c9e-818b-1ccf41a802d5 | -3.26783 | -45.37175 | 2024-12-04 05:03:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 886a50b6-2f09-396e-a100-ae59988f2a82 | -4.02173 | -49.96611 | 2024-12-04 05:03:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4d0a9ea-ed21-30f9-9046-ec6dad59a034 | -2.89625 | -53.89592 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31b1a21c-14fd-3579-9d77-9e82d1f136e3 | -3.01998 | -54.02028 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e2e88e0-3ae3-3df6-9502-bab40c8982c6 | -2.94968 | -51.40665 | 2024-12-04 05:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c5ad062e-9e29-37d8-bc7c-5fdc39ecbe1e | -3.06375 | -53.26633 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d4b8ff22-73ae-3a44-a909-9d8d15fb363b | -3.09404 | -53.25198 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1597cc4d-b935-3b51-86eb-f55fbb00e2b3 | -2.78385 | -53.21695 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3aa4ff9-bd8e-3871-83c0-af77accc8262 | -1.67834 | -52.51517 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77d64293-940c-3958-b03b-6a0fd092c37c | -3.81731 | -46.95278 | 2024-12-04 05:03:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9818d0d-93e3-3900-91e3-4fd9145d2165 | -1.64556 | -53.82315 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e200b85-49eb-3a30-bcb1-c6f9b61bc270 | -3.08373 | -53.36433 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7f4d833-0dd4-33d3-8821-4898a5fb8c96 | -3.02054 | -54.01673 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47d21303-0736-3578-a0e2-56f3c8aed08e | -1.656 | -52.38057 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 420e140e-d1c3-37ec-8894-bf29072db8c5 | -3.52283 | -52.16166 | 2024-12-04 05:03:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41d9ca54-9554-348b-aaea-991219b9e7c2 | -3.05365 | -54.50257 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c8a6e51-437f-3338-aa53-de9d4446df31 | -3.83703 | -50.90917 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| db0b482b-9a95-3bb0-a823-c09cdcb981c3 | -2.52882 | -54.0495 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3d55dd4-14f6-31a3-8dcb-2497842a6ee9 | -3.29228 | -53.66941 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6442469b-7b69-3091-98a7-254c1cd6bf9d | -3.26456 | -53.62435 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1c424aac-eb5f-32a5-a5a5-e487a2a32489 | -3.11963 | -54.01347 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 122556a5-444b-3e91-8564-7457f54afacd | -3.12405 | -53.9851 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 44353a6a-3e9e-32ca-9a20-61f442dff109 | -3.29015 | -53.82768 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12335719-52ab-3741-97a8-0276067f7511 | -1.75318 | -52.62008 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3c597915-660c-34b7-8f3a-0760ceabbbf4 | -3.44515 | -54.08522 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 928e8c32-98db-34fa-9531-6fb6e49f517a | -3.55246 | -50.18165 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3d86e59-eadf-3b72-94f6-1d1961a56f44 | -4.05417 | -53.55473 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10341d67-bdfc-3b68-b18b-97e52424a2da | -3.12069 | -53.98458 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ef4a2f9-1cb3-383a-997c-b5f5940c7b1f | -3.05921 | -54.51053 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 39693973-425f-30ad-9443-20503c5ef48f | -3.13138 | -54.61451 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 8ea4c752-731b-306f-8fa6-d77bdd000f37 | -3.2499 | -53.65187 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 981b2da3-fd48-31d4-af98-67446512d439 | -1.73986 | -52.61411 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 53ab8349-f3b7-30cc-afd8-c8194685ac7c | -4.19373 | -48.4209 | 2024-12-04 05:03:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b1671b5-352a-3661-b991-599b3805c45f | -1.70174 | -52.61706 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e76fd224-7d4f-3195-9198-3df508fafdd5 | -2.6162 | -54.36366 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fae505f9-d8b8-384b-aa77-53103e7d2f39 | -3.24088 | -50.42054 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da85dec5-3fb7-39a4-bc93-ced9023c425d | -2.81675 | -53.04973 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README39.md)
