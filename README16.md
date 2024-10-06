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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 593b4bfa-c131-3ec7-8056-0f678ad8e81b | -14.06671 | -45.16559 | 2024-10-06 00:50:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 7cd815e4-a8bb-3351-a5b1-c868c02259c6 | -3.3153 | -49.1241 | 2024-10-06 00:50:01 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6747d702-13c2-3a8b-9e11-8adf8641435c | -3.3173 | -49.132801 | 2024-10-06 00:50:01 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82c51f66-dafc-3791-b501-7e3d6918ffa1 | -3.3075 | -49.135101 | 2024-10-06 00:50:01 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9de298f3-20de-3f81-83d5-371ec2cbd6b8 | -3.573 | -50.384201 | 2024-10-06 00:50:02 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afaba79b-0d1b-3831-bbdc-f15431d65c65 | -3.2604 | -49.109299 | 2024-10-06 00:50:02 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5219ed62-9abd-3367-93f6-dd75fe242832 | -3.2624 | -49.117901 | 2024-10-06 00:50:02 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c1a05e5-e189-3bee-aa6d-8d10959a095b | -3.2644 | -49.126598 | 2024-10-06 00:50:02 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69b16030-399d-36a6-a649-8f3734bb5a3e | -3.2664 | -49.135201 | 2024-10-06 00:50:02 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69888fb4-3099-3180-9f97-f49b554430f3 | -2.7151 | -46.792801 | 2024-10-06 00:50:02 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 463cad5b-7f26-33f3-89dc-fb66cd47138a | -3.4928 | -50.258801 | 2024-10-06 00:50:03 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf0d15f1-3aba-3e0b-9cb4-6b71efe7fb75 | -3.4945 | -50.266399 | 2024-10-06 00:50:03 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4488a7f-5ff0-3b5e-bce4-e18316842a00 | -3.4202 | -50.121498 | 2024-10-06 00:50:03 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ffda0f1-5ba3-33fb-aaba-d57da1ed6086 | -3.422 | -50.129299 | 2024-10-06 00:50:03 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 148cd7f2-f7dd-3404-823a-b13a633aa53b | -3.1202 | -48.9473 | 2024-10-06 00:50:04 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e8a88c4-a9c5-39a5-9c00-11c8ed258a25 | -3.1223 | -48.9562 | 2024-10-06 00:50:04 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92bbc98e-1a45-321d-94cc-ff09181a131b | -3.1243 | -48.965 | 2024-10-06 00:50:04 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a088f419-17ee-3ada-a66c-19b3c33fca90 | -3.4156 | -50.372101 | 2024-10-06 00:50:04 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4371857a-aafe-3a60-bb9b-034ea9be641e | -3.4174 | -50.379601 | 2024-10-06 00:50:04 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43fbb331-3bb7-39d4-974b-d8f3934ef202 | -3.4041 | -50.366699 | 2024-10-06 00:50:04 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29f48b68-0267-35e8-afae-49b6d7283dbf | -3.4058 | -50.374298 | 2024-10-06 00:50:04 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da5f5b4f-ab66-3790-9208-0f72284c76fd | -3.509 | -50.827 | 2024-10-06 00:50:04 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6a7d0c3-814f-3791-85fa-2af4e257ae46 | -3.5107 | -50.834301 | 2024-10-06 00:50:04 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90888b9c-ec05-330b-86f2-74f3bb50d675 | -3.396 | -50.376499 | 2024-10-06 00:50:05 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc3c7850-36ca-38d2-9f0c-7f0139c6306b | -3.3143 | -50.063702 | 2024-10-06 00:50:05 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12a8f95a-3f75-3a63-b6c3-0e369a97e44e | -3.4378 | -50.650101 | 2024-10-06 00:50:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cba79f7f-ed74-3155-b98c-9841facdeb93 | -3.4395 | -50.657501 | 2024-10-06 00:50:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68342a71-918b-3837-9a4a-e17d143f5120 | -3.3066 | -50.436298 | 2024-10-06 00:50:06 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f72455d6-7af0-3831-8cfe-15ee30b9a443 | -3.3083 | -50.443802 | 2024-10-06 00:50:06 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecd126ab-3e49-36a2-b001-792eb14545d1 | -3.31 | -50.451401 | 2024-10-06 00:50:06 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0cb53f4-7054-318f-af4a-45b57ef6a1ec | -3.3118 | -50.4589 | 2024-10-06 00:50:06 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f43033a8-bed3-342e-b5c4-8764d1ad012e | -3.2985 | -50.446098 | 2024-10-06 00:50:06 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 916f4734-b7dc-344b-bd0c-c6d84fe3728e | -3.3002 | -50.453602 | 2024-10-06 00:50:06 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2781f1c8-7827-3846-b988-26a3ebd0bc93 | -3.302 | -50.461102 | 2024-10-06 00:50:06 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fe31259-7480-33b9-bbb9-73dbc57d8a98 | -2.8245 | -48.422501 | 2024-10-06 00:50:07 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dde7dbbc-5f94-35b6-81b0-0cc823150c67 | -3.287 | -50.440701 | 2024-10-06 00:50:07 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c91d5f9-8be6-3957-a46d-a2a106382ab4 | -3.2351 | -50.3489 | 2024-10-06 00:50:07 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b54e71a5-3b43-3ba8-b0f7-14994c68a37b | -3.2369 | -50.356499 | 2024-10-06 00:50:07 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77a3e309-e6aa-31b5-b930-af4e7806ac4f | -3.2386 | -50.364101 | 2024-10-06 00:50:07 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcf81c25-4efb-3cdb-ba1d-b9cb5e053932 | -3.2271 | -50.3587 | 2024-10-06 00:50:07 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 335a1377-0339-370e-ba9a-0575b994b114 | -2.8105 | -48.5854 | 2024-10-06 00:50:07 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f7621ca-f21b-3493-828d-6bc8b649f055 | -2.8127 | -48.594799 | 2024-10-06 00:50:07 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6021621f-f6b7-31b3-a251-eb7c8a758ae0 | -2.8007 | -48.587601 | 2024-10-06 00:50:08 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 024982e8-05d4-353d-914f-0deabfbb8125 | -2.8029 | -48.597 | 2024-10-06 00:50:08 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfcaf426-423c-357a-8f67-a553f24355d1 | -2.8005 | -48.675999 | 2024-10-06 00:50:08 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11856903-d08c-3354-bd88-ec96b85ffa78 | -3.2294 | -50.820702 | 2024-10-06 00:50:09 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77466e48-d76d-3336-a73c-ae4b489c9b5d | -3.231 | -50.827999 | 2024-10-06 00:50:09 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 271c66ec-d6c9-3294-bd57-564341f2b0a1 | -3.2327 | -50.8353 | 2024-10-06 00:50:09 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e29b0754-c349-3ce0-8c5a-2f905421998d | -2.7298 | -48.6824 | 2024-10-06 00:50:09 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39c93481-45fa-32f2-a163-a0fbdfe097c7 | -3.1245 | -50.405701 | 2024-10-06 00:50:09 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d0e65dd-da55-3e2b-bf3a-5ad7b83a506b | -3.1262 | -50.4132 | 2024-10-06 00:50:09 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac56c668-93ee-35bf-a2e0-df5d698028b3 | -3.2196 | -50.822899 | 2024-10-06 00:50:09 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ab2676a-9790-3dc0-995e-0cc1b0e30fae | -3.2212 | -50.8302 | 2024-10-06 00:50:09 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d00dcb79-0f7e-3baa-979e-b74f6a42bb48 | -3.2229 | -50.837502 | 2024-10-06 00:50:09 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd9f0d86-e59c-3321-b15b-2b9bb0c5f11b | -3.1129 | -50.400299 | 2024-10-06 00:50:09 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cfa39ae-b801-32ec-aaa7-5e52cb328e0a | -3.1147 | -50.407902 | 2024-10-06 00:50:09 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db940954-bfff-3379-b5cd-017d3df57ec3 | -3.1164 | -50.415401 | 2024-10-06 00:50:09 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71af9cda-79b3-3539-b711-88607fa5dae3 | -3.2878 | -51.440601 | 2024-10-06 00:50:10 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32299b5e-646c-322e-b8c2-fb972e13141b | -3.2894 | -51.447701 | 2024-10-06 00:50:10 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87168775-d858-373b-86f4-8021f343017c | -3.0922 | -50.444801 | 2024-10-06 00:50:10 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71a0b8b2-687d-3ed2-a127-68952101484d | -3.0939 | -50.4524 | 2024-10-06 00:50:10 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8209719-c565-3960-a51c-2a5625df0ffb | -3.0956 | -50.459999 | 2024-10-06 00:50:10 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd7b1fc2-ba1f-3559-a6e2-8d17f5dc8138 | -3.2992 | -51.445499 | 2024-10-06 00:50:10 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16ab142a-7db8-3e46-8738-27308388b6de | -3.3008 | -51.452499 | 2024-10-06 00:50:10 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6bad38d-2984-31ab-b48f-64cb4c5fbfb6 | -3.291 | -51.4547 | 2024-10-06 00:50:10 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b93d080-f38d-3b8b-a1b6-8244e5f57a25 | -3.8555 | -54.005402 | 2024-10-06 00:50:10 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1041a7f3-3fc0-384e-9fdd-d101e1b0768e | -2.6896 | -49.0448 | 2024-10-06 00:50:11 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0581bdd-3401-3a92-8bc2-4b0637a9969b | -2.6917 | -49.053699 | 2024-10-06 00:50:11 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1f34a2f-78ee-3524-9ff0-8a84850aaf99 | -2.6937 | -49.0625 | 2024-10-06 00:50:11 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b8ab40d-6283-3813-aefb-2a9c4dea4b40 | -2.6778 | -49.0382 | 2024-10-06 00:50:11 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fec1184f-72d3-397a-a377-6dca6f339e75 | -2.6798 | -49.0471 | 2024-10-06 00:50:11 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07657055-76da-3766-abcf-04ca56edd4ca | -2.6819 | -49.056 | 2024-10-06 00:50:11 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 754b25a8-9690-3d49-b2d7-aec8bd863237 | -2.6839 | -49.0648 | 2024-10-06 00:50:11 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 983e18bf-0af8-3239-a7fa-90db981e0626 | -2.6859 | -49.0737 | 2024-10-06 00:50:11 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6926d34-9e5f-3bbb-a7a4-0ba53c86bba9 | -2.67 | -49.049301 | 2024-10-06 00:50:11 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93880eda-a310-3e5c-9cb0-5c220b14a888 | -2.6721 | -49.058201 | 2024-10-06 00:50:11 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7027b0e2-c1a2-38e1-a739-9cfbe89fde12 | -2.6741 | -49.067001 | 2024-10-06 00:50:11 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95ca8341-8807-3f7c-810e-7c7735d4d82e | -2.5264 | -49.006699 | 2024-10-06 00:50:14 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf5024e7-91ed-3833-8121-933b3f02c9ce | -2.5284 | -49.015701 | 2024-10-06 00:50:14 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa710190-c69e-3cab-97f5-c8b70a2610d5 | -2.5166 | -49.0089 | 2024-10-06 00:50:14 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 341b90e9-ab42-3d47-9dd4-cd14f4f2d10c | -2.8449 | -50.444599 | 2024-10-06 00:50:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ac7a568-c8f2-39a4-9e6a-8d1cdb13a372 | -2.8466 | -50.452202 | 2024-10-06 00:50:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4355fc40-19e6-3b4b-9373-100e68762e36 | -2.8483 | -50.459801 | 2024-10-06 00:50:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 965a8944-607d-3bf4-8683-0f88a4e8e967 | -2.8368 | -50.454399 | 2024-10-06 00:50:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58da4b7d-43d4-39ac-9a1e-48f3c42111e8 | -2.8916 | -50.694801 | 2024-10-06 00:50:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e88343b1-fec5-3097-9230-d3d129eb7f78 | -2.8933 | -50.702301 | 2024-10-06 00:50:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 308158af-96b3-3182-b635-88f53e929ac9 | -2.8818 | -50.696999 | 2024-10-06 00:50:14 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c2b31ea-4711-34c0-973b-1b979dc31a1b | -2.3649 | -48.617001 | 2024-10-06 00:50:15 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5440199f-8f59-39bd-9bc8-f41d8c4c58b5 | -2.3671 | -48.626499 | 2024-10-06 00:50:15 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 821a145a-cc62-3a4f-bfc8-0fcc6dab6aa5 | -2.3693 | -48.635899 | 2024-10-06 00:50:15 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 474923ab-f09c-332e-b0d3-43518c3b8ab0 | -2.3968 | -48.845299 | 2024-10-06 00:50:15 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72fd9c7e-500c-360f-8a55-7ee0bbf76ea2 | -2.3989 | -48.854401 | 2024-10-06 00:50:15 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ad4ba91-6cd6-315d-a4e0-a0effb4caabf | -2.1936 | -48.1399 | 2024-10-06 00:50:16 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f17c55af-1efc-37eb-af7e-54a0b2c518d9 | -2.196 | -48.150002 | 2024-10-06 00:50:16 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b6bf37a-59ac-3b1a-95c1-79d829ace525 | -3.3212 | -53.367901 | 2024-10-06 00:50:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffe9a211-dd75-32dd-a825-80c186e83659 | -3.3228 | -53.374802 | 2024-10-06 00:50:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16a216d4-d956-3b3a-a91f-4095ec597459 | -3.3243 | -53.381699 | 2024-10-06 00:50:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64d97460-1aa8-3a31-83ab-90221db6920d | -3.2068 | -53.133801 | 2024-10-06 00:50:18 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a307d9d-2a87-38cd-bb45-146c8dc42d64 | -3.197 | -53.136002 | 2024-10-06 00:50:18 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e344fde0-de92-387b-abe7-7038f4a9d71e | -1.7561 | -47.176701 | 2024-10-06 00:50:19 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README17.md)
