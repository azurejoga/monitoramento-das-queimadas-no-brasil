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
| f3b77b00-7f86-3c03-a031-b90d82c34990 | -3.7087 | -44.5009 | 2025-12-15 01:20:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 046938a7-2e4a-3a26-9a61-299cd333fb54 | -4.4424 | -46.2872 | 2025-12-15 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 3bff9791-958c-3f96-8a94-5c019bcced47 | -2.2348 | -45.6396 | 2025-12-15 01:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 41e11f2e-3a33-33b9-9ae7-ae9dc1d69d9c | -3.7086 | -44.5237 | 2025-12-15 01:20:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 0f4dd243-c1fc-3c30-8b79-807fad90f2f0 | -2.2347 | -45.6619 | 2025-12-15 01:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 53.4 |
| ddfed3a3-0328-3e43-8919-44a47cdb2d76 | -3.7087 | -44.5009 | 2025-12-15 01:30:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 1c12d363-1918-338b-ab40-92a73db41d18 | -4.4424 | -46.2872 | 2025-12-15 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 932d7b90-37df-33f8-bfee-3cd72a0a9399 | -3.7273 | -44.5 | 2025-12-15 01:30:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 8bd12108-a657-3e7f-b6eb-f0a2b8196cf7 | -6.427 | -35.1506 | 2025-12-15 01:30:00 | GOES-19 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 67.3 |
| 1d594d02-1467-3822-a721-eda9496d77cf | -2.2347 | -45.6619 | 2025-12-15 01:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 55.3 |
| f40c98ff-35d5-32be-8349-a51185939f16 | -14.2968 | -57.589802 | 2025-12-15 01:36:00 | METOP-C | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d6632b12-14cd-34f3-917c-3a6ca7b3d78a | -14.2948 | -57.581501 | 2025-12-15 01:36:00 | METOP-C | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 976f47f0-94a2-326f-9561-79ee3eacf6e5 | -16.076799 | -56.597099 | 2025-12-15 01:36:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 928095fc-07b2-3cee-9bc2-b93732e4b7db | -14.3066 | -57.587399 | 2025-12-15 01:36:00 | METOP-C | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 63c2154a-b3b8-3dfd-8943-72439bfc1fb8 | -3.7273 | -44.5 | 2025-12-15 01:40:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 22c0e331-07e7-34af-93b3-b96ed9934ba9 | -3.7087 | -44.5009 | 2025-12-15 01:40:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| ee0c814e-1992-3f4b-8ef5-6cc754e42ea1 | -4.4238 | -46.2881 | 2025-12-15 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 205b7d2a-aff7-365b-8fba-42dcbd6b5558 | -4.4424 | -46.2872 | 2025-12-15 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 55.6 |
| ace2ec50-3a8e-33d5-8576-6b443feb5038 | -3.7273 | -44.5 | 2025-12-15 01:50:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 63808f2d-7ac0-3024-965d-7544706c1455 | -4.4424 | -46.2872 | 2025-12-15 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 7385d7f6-fa45-3048-9a5a-fed33723b965 | -3.7087 | -44.5009 | 2025-12-15 01:50:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 8bcb5a96-75f6-3b3d-9536-358f75b9b0d1 | -2.2347 | -45.6619 | 2025-12-15 02:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 47.1 |
| b171f5f1-a98e-37ec-a4d0-899fb68e6aad | -3.7087 | -44.5009 | 2025-12-15 02:00:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| a54c0570-9136-3a5a-a252-442c95925c85 | -4.4424 | -46.2872 | 2025-12-15 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 55.6 |
| ca964c06-38e6-3cde-9863-995aee7b68bc | -3.7273 | -44.5 | 2025-12-15 02:00:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| d514dca0-4561-391b-b540-c17160ca81b6 | -12.6213 | -58.0917 | 2025-12-15 02:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| ca5d6676-0f99-3642-ba32-c7daf76ff0f6 | -2.8325 | -54.8328 | 2025-12-15 02:10:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 99bf7880-3210-3805-919a-0979b265b54b | -3.7087 | -44.5009 | 2025-12-15 02:10:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| a891f77b-3f01-3945-96fb-dd368ae4f2a0 | -4.4238 | -46.2881 | 2025-12-15 02:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 9ad4b0c1-8e1d-3139-b5df-6cae654dd391 | -4.4424 | -46.2872 | 2025-12-15 02:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 50.7 |
| a5416d01-be5b-3df0-83e0-54c8fe30c42d | -4.4238 | -46.2881 | 2025-12-15 02:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 374ae64a-88b9-3199-805b-2abecbbd2034 | -5.62434 | -35.35157 | 2025-12-15 03:02:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0eeb4c97-f3b0-3407-9f2f-c0aa0ae02e23 | -5.6252 | -35.34682 | 2025-12-15 03:02:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a61ee261-f7c0-3f1d-8c8d-21c3df7a0024 | -8.958 | -35.34823 | 2025-12-15 03:04:00 | NPP-375D | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 46e5abdf-2785-3631-9bc0-6d84096d5bfb | -9.11073 | -35.45071 | 2025-12-15 03:04:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| feb99877-dfd1-3312-a67b-78761c1ce13c | -9.1075 | -35.46741 | 2025-12-15 03:04:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8654067b-a72e-3a61-9917-8ff18b951485 | -9.11007 | -35.46287 | 2025-12-15 03:04:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 3ff66605-3b37-30b4-90aa-dcc0cdece6c1 | -8.9588 | -35.34404 | 2025-12-15 03:04:00 | NPP-375D | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5dd39ebc-a750-30bc-9502-b0e9002c0bec | -9.10243 | -35.46226 | 2025-12-15 03:04:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c8dee144-aa90-3399-b8ae-0f792664f7a3 | -9.1034 | -35.46614 | 2025-12-15 03:04:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ff78429b-b7cc-32ed-890a-831da575fa83 | -9.11084 | -35.45871 | 2025-12-15 03:04:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| b1efc586-a638-3e40-8e22-efea5a08fef6 | -9.10831 | -35.46322 | 2025-12-15 03:04:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| aa84dd14-49a0-3b6e-a7d9-a962d24fec9f | -8.9646 | -35.34525 | 2025-12-15 03:04:00 | NPP-375D | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 24f963bc-3de4-3096-b67c-a561438ea06e | -9.10992 | -35.45488 | 2025-12-15 03:04:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 8a334bf1-ebcf-3d7b-a2da-5904bd86efd3 | -9.10407 | -35.45377 | 2025-12-15 03:04:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ce969ff9-93e5-3b2e-8faa-df4a0359360a | -9.10576 | -35.45343 | 2025-12-15 03:04:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| bb0125c4-7b96-3645-ac15-b87ab938dd3e | -9.1016 | -35.46653 | 2025-12-15 03:04:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2ba91f90-0512-32c7-aa91-02efef150dfe | -9.10912 | -35.45904 | 2025-12-15 03:04:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| 62d15539-6739-39dc-93ca-fd0e29a2cde5 | -9.10261 | -35.47036 | 2025-12-15 03:04:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1afc32a0-1549-3a6f-8624-bf4643577565 | -9.10325 | -35.45802 | 2025-12-15 03:04:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 108d447e-8836-3fe3-896f-1fba7497b251 | -10.18752 | -36.40288 | 2025-12-15 03:04:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| f361b0b2-f3fd-3e08-8c75-db9e926b351b | -9.10851 | -35.47124 | 2025-12-15 03:04:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 997ac27c-1ae5-353d-a8ad-cece72788448 | -9.10669 | -35.4716 | 2025-12-15 03:04:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 925a91e0-69ca-3a36-853c-54ed27ca5f41 | -9.10929 | -35.46703 | 2025-12-15 03:04:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 35ade382-38f5-3e2d-8a78-0dac3ebd0f1a | -9.11515 | -35.46815 | 2025-12-15 03:04:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ca6d2663-1efb-3eb1-98e2-33f9329744dd | -9.1116 | -35.4546 | 2025-12-15 03:04:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 45b9f174-4021-3185-b826-215656224030 | -9.10419 | -35.46188 | 2025-12-15 03:04:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 1ce64660-258e-356d-9a3d-391dc776fddf | -9.11339 | -35.46834 | 2025-12-15 03:04:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 22c2c23b-8032-3810-bf55-6a8d0ed17f87 | -9.10498 | -35.45764 | 2025-12-15 03:04:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| c3e1a852-90ae-3463-bef2-6f2b46b11674 | -10.18843 | -36.39823 | 2025-12-15 03:04:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 90f19982-1d6f-3d1d-ba4d-069b3af556ae | -2.76051 | -42.64122 | 2025-12-15 03:21:00 | NOAA-20 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0eb898e5-9575-31fe-8751-4b86453f8432 | -2.75947 | -42.64724 | 2025-12-15 03:21:00 | NOAA-20 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5db0833-bd60-36a3-ba50-7ac66472a33f | -3.65636 | -39.8552 | 2025-12-15 03:21:00 | NOAA-20 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e7d03419-49ef-33c5-b369-6cd595f6c61a | -3.12418 | -41.77679 | 2025-12-15 03:21:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6fb92495-775a-3eb7-94f3-aa2cdd478636 | -3.71086 | -39.62635 | 2025-12-15 03:21:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 81f73d0a-79de-3af2-a811-83cc74fccccb | -3.71639 | -39.62725 | 2025-12-15 03:21:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| fe8fcee5-9a2d-361e-94fa-3fd3229d7373 | -6.31049 | -35.24902 | 2025-12-15 03:23:00 | NOAA-20 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3793dd96-8323-3acd-b787-9e98997db3f6 | -3.96683 | -41.53254 | 2025-12-15 03:23:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| de8e7f7d-7301-3739-8595-d0b89a054a8d | -4.80759 | -38.9842 | 2025-12-15 03:23:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 744e204e-aa9b-3581-8d11-029146c22bca | -3.96597 | -41.53753 | 2025-12-15 03:23:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e60c108c-5c23-323d-aa05-41e85a35ba0a | -8.96184 | -35.33968 | 2025-12-15 03:23:00 | NOAA-20 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 4a685eba-e2f8-3fa2-839c-f3a08fd1a483 | -6.1018 | -40.01578 | 2025-12-15 03:23:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d87a1b44-6082-3367-83f7-2a17b1b8b09c | -5.62651 | -35.34472 | 2025-12-15 03:23:00 | NOAA-20 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 5.8 |
| d39b1ab6-f7d2-353c-95cc-31349d814e1b | -5.6225 | -35.34404 | 2025-12-15 03:23:00 | NOAA-20 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1fe416ab-cd55-36a2-ba65-2af193f59600 | -6.48044 | -38.8273 | 2025-12-15 03:23:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 487b4c8f-7ae2-373e-84ff-c60934fb5510 | -6.09658 | -40.01785 | 2025-12-15 03:23:00 | NOAA-20 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5f6b07d2-8df9-3091-a1af-e25d771af870 | -6.09721 | -40.01434 | 2025-12-15 03:23:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9104b902-bd15-3acc-843d-65ae00ccffbf | -6.6073 | -35.20639 | 2025-12-15 03:23:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c68e7c89-4948-30d6-9ecc-2b21c83cbde9 | -10.14436 | -36.60333 | 2025-12-15 03:23:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b775833d-54e3-3837-b158-69783d352f6a | -10.1833 | -36.4001 | 2025-12-15 03:23:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 68730bd6-633b-37df-bd70-4c644d19bfc2 | -6.60684 | -35.2099 | 2025-12-15 03:23:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a931c999-936c-3707-9eb1-aca1786dd703 | -5.62533 | -35.35172 | 2025-12-15 03:23:00 | NOAA-20 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bd6ea681-c0ce-3cd3-b65a-96f16322b6b3 | -9.91587 | -39.03463 | 2025-12-15 03:23:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c4bd1a8e-5f24-3efc-b327-4ffa5ff380c5 | -4.80814 | -38.98103 | 2025-12-15 03:23:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ae333a58-6f3d-3c1d-8a27-115dd612ffa3 | -7.76311 | -35.10344 | 2025-12-15 03:23:00 | NOAA-20 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| c3efaf0e-36b6-39f6-9618-06df92f2e082 | -10.18825 | -36.34708 | 2025-12-15 03:23:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b912dc25-b95e-3e14-b2d9-c62a2464ffce | -6.09639 | -40.01457 | 2025-12-15 03:23:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 07c7ee04-0721-3410-9556-9d85623523e0 | -9.10881 | -35.45358 | 2025-12-15 03:23:00 | NOAA-20 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c016b290-b7c4-3934-afad-bf0beeedc494 | -6.48093 | -38.82447 | 2025-12-15 03:23:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d01b79e2-0d22-335c-8099-319c6193946d | -9.34246 | -35.56791 | 2025-12-15 03:23:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 88346808-ff6f-390f-b96a-18b35b8915af | -8.79904 | -36.95387 | 2025-12-15 03:23:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cc490528-a504-3c61-b99d-24cf15497886 | -9.43403 | -35.64633 | 2025-12-15 03:23:00 | NOAA-20 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 50e60063-e695-3840-95d0-315b0fd5d355 | -7.67294 | -34.94587 | 2025-12-15 03:23:00 | NOAA-20 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b3acf2a4-a4cc-3d85-b57a-bd668015c9cf | -10.1403 | -36.60263 | 2025-12-15 03:23:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cf8605cc-2861-3b73-924c-84143139d22b | -6.16564 | -35.17607 | 2025-12-15 03:23:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5e3f2805-ba77-3d28-8b44-66321fa6c8e3 | -9.19238 | -35.62522 | 2025-12-15 03:23:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 143a58a9-6244-3ea1-99b7-263d7f8784f8 | -8.17165 | -34.98088 | 2025-12-15 03:23:00 | NOAA-20 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ac1cbd32-b4ee-327f-a80c-e4b558cc8931 | -9.108 | -35.45836 | 2025-12-15 03:23:00 | NOAA-20 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fbb35c19-1e1f-3cf4-9fc4-242f1039df21 | -3.30012 | -42.54348 | 2025-12-15 03:23:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 953c367b-bd07-3095-af93-49ab1a799b3b | -4.69619 | -43.25888 | 2025-12-15 03:23:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README3.md)
