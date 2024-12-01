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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb8644a4-2355-37b0-ad76-cc011114330e | -3.41747 | -53.22491 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f820932-fe43-395d-8ddb-7b70ceccb938 | -1.9969 | -51.1818 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67adae9a-4941-3b10-9513-76fabddac361 | -2.53353 | -54.03989 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f6aeb533-7fb6-3f8a-9037-6ecd5e004316 | -1.32818 | -51.74606 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fd6361b1-d6b6-3568-85f7-d26065bf43d7 | -4.03935 | -46.93192 | 2024-12-01 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 15c74055-2df9-3fe5-933d-9f0210ebfdce | -3.13938 | -53.84631 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15a1b999-df28-3331-93e7-27e972d06fda | -2.15006 | -50.6239 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 398e5000-6e64-3b80-b29a-fbb5964aa9ed | -0.19946 | -51.54766 | 2024-12-01 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96d96122-cb50-3537-9138-ce8832a49a33 | -4.53125 | -45.74359 | 2024-12-01 04:44:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 385ee883-c456-37d8-b8ab-04b70b545f00 | -3.11424 | -53.27739 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3c8ea15-47b9-3ff3-8e42-318f72d13364 | -3.40774 | -51.97543 | 2024-12-01 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02fdabcc-5af6-316f-80ed-ffc5a5213061 | -1.09204 | -53.39721 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62095872-b267-33cf-ae35-c3b180e7d523 | -1.09851 | -53.38055 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d56d3d5-9591-36fa-b80e-3a616ecd0fc8 | -2.83726 | -48.48009 | 2024-12-01 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e047def-4a77-3aca-822b-b3269799da59 | -1.72056 | -52.62892 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b602b34e-601a-36d6-8608-0fefe6a2caa2 | -3.96903 | -49.96674 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74bddf7c-473e-369f-ad11-bae2bf9ed504 | -2.98216 | -53.28675 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de5caec8-352a-3566-9acf-91289f3e31c3 | -1.72473 | -52.6255 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 828d378b-fe10-31ea-ae24-530167591819 | -3.26954 | -50.56167 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d08a974-998d-31a0-8ec4-a0456f63694f | -1.74471 | -52.65245 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e6f849b-6710-38f0-82bd-3bae60dc1c03 | -2.06696 | -50.71778 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 451fd12d-2a96-34af-91c8-828db47d17bd | -3.22043 | -54.23193 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c056449-a44c-3f5e-9543-2bc2352815eb | -2.86683 | -53.98324 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f32d43d-d252-36e4-80ba-45fff145ba58 | -3.1257 | -53.27495 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 05dc05c6-5e13-3e54-a460-f23bbf486f97 | -3.02943 | -51.54289 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 736de7f8-52f5-3b42-b33b-2b424296ef83 | -4.58661 | -50.96733 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a773432b-1b3f-35a4-9a2a-baf5dcf7f22e | -3.3081 | -50.48985 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d3a2700-2971-3316-8b1f-9e378d400045 | -3.82751 | -50.13633 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 998491ca-9f5e-3508-bced-3350ca2041db | -0.74885 | -51.9468 | 2024-12-01 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c13ec429-47cf-31e9-8655-1d420e574a6e | -2.32328 | -50.68277 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c5aaac9-736a-3c88-9578-08978a913923 | -0.98113 | -51.75465 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6c99d64-e5e0-3cb8-9831-c89df3d9b7d5 | -2.06918 | -51.19297 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8cf6229a-7fef-38c9-ad45-2a09f1825de5 | -2.83157 | -48.47172 | 2024-12-01 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bf308b5-3ba1-3fed-b510-98a260e6a942 | -4.14784 | -48.22671 | 2024-12-01 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 18ad08e7-d8de-349f-881d-c443e9f276a0 | -3.71016 | -51.06774 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6b47cf4-537c-3a98-85b6-4e425f6db385 | -1.99746 | -51.17825 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6275422a-6c68-32a8-83b0-6af4fb9d6d50 | -2.82727 | -54.03712 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 084f4025-d1a5-3423-a078-da0b57675ffb | -3.01145 | -51.78734 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1fa101ae-24eb-35db-b19b-22bef361eecf | -4.00101 | -54.6188 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a727aa8-7013-39e1-a7a2-db80944601e7 | -1.31998 | -51.97036 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c56c39a-f8be-329f-bfce-7ad1b4a18cb1 | -3.48095 | -50.25161 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f17d4176-998a-3732-b685-206b788ddebe | -3.26239 | -48.77501 | 2024-12-01 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 474ec00b-4b67-3818-b30d-3e04df1f1f43 | -4.65834 | -49.73523 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f21c78a-2217-38dd-9718-f722045256d7 | -1.003 | -51.72752 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 93f2cd4c-31b8-3cfa-be0d-76e260cbc288 | -2.89505 | -51.57733 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff2a20ef-ebd3-3b2d-b202-a1bef1838cde | -3.33003 | -50.22116 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69b0e9f6-798a-396f-a2bc-49b6dcd2b6bc | -1.0853 | -53.39174 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1ff712cd-db11-347b-9114-641dd1b6d23a | -3.26711 | -53.62911 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e92e75eb-d2ff-3b9d-aed7-623e8677bdde | -1.08326 | -46.77467 | 2024-12-01 04:44:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56f3a1f7-ae23-3be5-be67-e4ce19519a6a | -2.88322 | -54.07398 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c605605-6db9-300a-833d-c288613d5d63 | -4.3203 | -48.09418 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| abd111ac-ddfe-3a43-997f-0bf2cf5886da | -2.78182 | -52.8671 | 2024-12-01 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f4e677c-d232-3183-b3ae-5dfeb0e2a873 | -2.30275 | -50.68312 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a03b9b8-8fad-3d8a-bed3-65d53fcb4313 | -3.1791 | -53.64327 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce54f3f2-3f01-309d-80cf-941ca0901874 | -2.43749 | -50.43099 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03600324-296f-3803-9e45-a0cf0bfe8475 | -3.26384 | -51.62694 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26550fce-2aa2-3014-8137-31249ce8e710 | -2.20018 | -46.64108 | 2024-12-01 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e30a7e1-5dac-3875-a753-e56bb53cf719 | -2.6577 | -46.57611 | 2024-12-01 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec76954b-b6be-30c2-b1ad-606899e4b1de | -2.12789 | -50.63467 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80e4b1cb-38c4-35e2-b837-69c51dd0a94e | -3.09846 | -53.72282 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6356b083-6018-3947-8852-11bab3c1bc20 | -3.25028 | -50.61885 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 62e5343d-6efd-3ac3-a5c8-be3242bde8f3 | -2.57021 | -51.88344 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bb713f2-fd39-3a22-a5de-8f5538e794db | -1.91767 | -52.65823 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b24683ee-fdd0-3f01-a1b6-496ca73a2fe0 | -2.53048 | -54.03472 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a0e43b7-2786-3bd3-8fdc-3e80884bc6fd | -3.30329 | -50.80099 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75878269-fa14-30d7-b508-0a34a48ff658 | -2.51232 | -51.82924 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b830466f-7740-3de6-908b-78e5b98e5c2b | -4.53765 | -45.69999 | 2024-12-01 04:44:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bdbaeca4-1626-35a1-9b0e-a801135efe44 | -2.47164 | -50.36557 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a816bfb-60b4-3ba7-97c4-a3d609d661f9 | -4.07497 | -50.02587 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 573686a7-0cff-3145-ae8a-d93dd82d86ea | -2.22525 | -53.62932 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a013e643-aefb-32e6-8cb0-1ccab056dee5 | -1.76771 | -50.86067 | 2024-12-01 04:44:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4263575d-718f-37f0-8ce6-7d1e6f531f65 | -4.43221 | -48.2993 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fd44b2c-2432-3da9-a572-c66735a176f1 | -2.86538 | -53.99225 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f02627b-bdc6-3b53-aca1-20f5488e9922 | -4.74622 | -43.71352 | 2024-12-01 04:44:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55d0a5a4-56d4-3ced-a87f-28840ca71f40 | -4.65889 | -49.73174 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba2d1a64-69d9-30c5-bfab-b2b63cc01bab | -2.82674 | -52.58921 | 2024-12-01 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 249ee92f-8d2c-3983-85ce-db6f48afee43 | -2.82598 | -54.09283 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c8cef90-61d4-3808-8fc7-7eda1b0853d3 | -2.6306 | -51.74663 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d72135b9-0041-3f35-b352-9b1ec34d5cd9 | -1.29862 | -55.73999 | 2024-12-01 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1fbaf95-051f-330c-a638-7e259cc31df8 | -2.03514 | -55.77306 | 2024-12-01 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b440979-4e26-373d-a955-195578464e58 | -4.19992 | -50.67245 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c936087-f5df-3335-b1bc-ba4abf9f6091 | -2.65438 | -53.3545 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7c1bac01-102e-332c-8065-3a16fd1b81fb | -4.69274 | -46.80876 | 2024-12-01 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 716d1a05-fff1-3444-8d16-1e204eeea2f3 | -3.49136 | -53.81569 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c778001-fdca-395e-87fa-36b3a6e73fa6 | -3.91941 | -49.87024 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3a0c728a-dd75-30cf-a31c-b85efff44373 | -0.34281 | -51.98658 | 2024-12-01 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54b9030b-2169-35ce-85d2-d6b616ee60dc | -3.97066 | -49.9564 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4cde1c3-16d9-3ff3-8a4a-90466cb4b39f | -3.75166 | -52.2695 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74d0b5ad-29e3-3ef8-8ba3-ec013f848cab | -1.47939 | -52.67101 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6d59460-6c62-3613-9247-3cf79cca5b02 | -3.57613 | -50.42257 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36a15cb8-fbd6-38bd-b7b6-54b78255ad18 | -3.78534 | -51.3412 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99bda4be-fc70-3697-9916-ab9cb4d1f5b3 | -1.07689 | -53.63633 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38371fdb-3429-3ddd-9cad-e3d668a291e7 | -2.80561 | -53.05998 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61655d93-5a27-30ac-af2b-dff6ac14e23f | -3.72462 | -51.10575 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f3850c8-495a-3b21-92d2-015594154a28 | -1.08415 | -52.43306 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2961532-5d8a-35ec-a840-3c9000111445 | -4.01725 | -47.00375 | 2024-12-01 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 621efdc6-9cb5-3b44-ac55-a837abc90848 | -2.29247 | -50.40848 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5816ca95-dc9a-3733-8e4d-ef869f146f8c | -8.13382 | -44.47211 | 2024-12-01 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 638bfc22-5274-392c-a6ef-5a8d67a64fd8 | -2.87753 | -54.01264 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38e200ce-f333-3b52-9fcc-213e87e80209 | -3.40868 | -53.03016 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README46.md)
