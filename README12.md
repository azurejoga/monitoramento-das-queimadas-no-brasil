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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55e1353b-690c-3c7b-b39d-b6c53ae3c2e7 | -6.08465 | -48.05737 | 2024-12-02 01:11:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 270.9 |
| 218a508a-bf14-342a-bc93-0150c8584335 | -3.38159 | -49.85876 | 2024-12-02 01:11:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4eda9eea-39d6-3ba4-8f89-8ba56719b2ea | -3.62338 | -52.49952 | 2024-12-02 01:11:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 48dc54af-7bf5-35e6-b84f-287f461f6eaf | -3.70562 | -51.06172 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3f08155b-e22e-3132-9ddf-9782e90ad9a0 | -3.65752 | -50.43741 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1f532a95-65b5-30db-8644-6bfc22fc8311 | -4.77405 | -46.43673 | 2024-12-02 01:11:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 34.5 |
| c9c5bc7f-ed61-3ffc-868b-b65b5ffc1f55 | -3.27627 | -50.20983 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 914c104e-5a6c-34c7-a646-41226089ae21 | -3.54849 | -51.45586 | 2024-12-02 01:11:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 02d7e48d-0ad3-3ad9-889e-e901e4990562 | -3.8222 | -52.08194 | 2024-12-02 01:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0e70482c-ea03-3bb4-ac25-9515d00d0d37 | -3.64655 | -52.6642 | 2024-12-02 01:11:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 52fba17d-eb74-304e-9925-1d270b1fca0e | -2.59818 | -45.24396 | 2024-12-02 01:11:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 0b2af9f3-8405-393e-81d8-bac3675b9071 | -3.54485 | -51.49763 | 2024-12-02 01:11:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 86212c73-1d29-3192-9b01-f5cdcbdf9b28 | -4.5677 | -45.47356 | 2024-12-02 01:11:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 5d0423bb-932c-36fd-b116-c31bd1a77681 | -3.65112 | -51.11914 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 7634935b-88ea-3376-a2eb-f0ec0888b387 | -4.39921 | -49.77734 | 2024-12-02 01:11:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 795a20df-c016-3223-a4a3-e94da661f833 | -3.37107 | -49.86036 | 2024-12-02 01:11:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 1dc6bcdf-8332-34b4-a209-cd2fdcacf0b3 | -3.77967 | -52.03626 | 2024-12-02 01:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ac0ab5c6-44ba-3899-9514-32acec33f4c0 | -3.69179 | -51.81369 | 2024-12-02 01:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ae2c0e26-900c-3012-b909-1c49647bfda6 | -3.58894 | -52.05648 | 2024-12-02 01:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| aa971184-56e4-376f-9c21-0b400055a161 | -3.70344 | -50.25769 | 2024-12-02 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7de8b8e2-a9e6-37a5-9881-eae521c93d88 | -3.71004 | -52.1967 | 2024-12-02 01:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5747c47d-45d9-3065-bec9-b2f167d6166a | -0.20851 | -51.35064 | 2024-12-02 01:13:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a3ca0e95-6582-34ac-a74d-c2bd8c7eb4c1 | -2.88777 | -54.16163 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2181f475-c4ad-3f19-a993-8fc1f5a67de1 | -2.5691 | -53.39076 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| f7a94877-b879-3217-815a-f11ae2b1cb9a | -3.038 | -54.0473 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d0e0cdea-58ad-32ac-8897-9b257f099b41 | -3.49705 | -53.82899 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 254d8129-f565-3b2d-a00f-2f910b6da923 | -3.03106 | -54.19234 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 18b5bc45-d998-35ab-b348-5f50aca21f08 | -2.6574 | -54.08941 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 67e48230-386e-345a-9226-f3ded7aad53f | -3.05513 | -54.49673 | 2024-12-02 01:13:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f97fe687-287a-3a59-bdaf-c54105350177 | -0.31863 | -51.77879 | 2024-12-02 01:13:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 0c2c95d2-c3c8-3868-9eaf-25d71e4abe7a | -2.83242 | -54.08846 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| d6e05b07-4d4b-3b2a-876d-7bc38051e84f | -0.60318 | -51.69873 | 2024-12-02 01:13:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 62ba6301-2331-30aa-9393-11b15982e21a | -2.7985 | -54.03931 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b03207a0-28b9-311b-90d6-bbd50f60bf69 | -2.97469 | -53.25761 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6f511fba-6a12-3791-b697-ff3c3124bc4d | -3.48475 | -53.81907 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ecf78250-d643-3b71-a9cd-20de216e8701 | -2.533 | -53.98755 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7c774b29-1f7a-3ba3-9f82-7d15f891f3c3 | -2.26836 | -53.60543 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 2107ff39-a2a1-3c1d-a513-da1a6ba97553 | -2.41458 | -53.66867 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8d3d8954-6b2e-3f51-89ef-26ab0cc73dcf | -3.2956 | -52.0679 | 2024-12-02 01:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 74746fd8-badf-3544-b537-4224ac2bf0b8 | -3.23823 | -50.65134 | 2024-12-02 01:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ad578e1d-e3ea-321c-80ed-624e81585a15 | -1.24735 | -54.54729 | 2024-12-02 01:13:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0e766cd6-99fc-3ddd-9223-79c1525d454d | -1.73693 | -52.7738 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| aecc1a05-7c96-39d8-8f2d-8c0fec36ee4b | -3.10104 | -53.2425 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fea70fbc-d2a4-3ae0-9257-b40ee4b81702 | -3.28673 | -50.56285 | 2024-12-02 01:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| afac2c32-4b8c-33dc-84af-414d72c8aa59 | -3.75749 | -54.52002 | 2024-12-02 01:13:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 386f4a3a-d789-3390-89fd-202603a4f6c7 | -3.1619 | -51.12281 | 2024-12-02 01:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| a07cb866-5a2b-3a31-af98-8fc8c85c4b40 | -2.8053 | -53.03857 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| df5d370f-bdb3-3c2c-8f00-de8c5a1fdc29 | -3.12724 | -53.0965 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e516b1d5-75bf-3d5f-b5b2-edc6aa0bcf88 | -2.59268 | -54.2218 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2d92a4a2-f435-3b6c-bcb1-122e7a4a12bd | -2.37474 | -52.20191 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 71530a28-e3a6-3ad5-ab9b-5eea2402a170 | -3.50713 | -53.83656 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 8047b92a-23d0-3c9a-a3b8-7829272cfb92 | -2.79154 | -51.8941 | 2024-12-02 01:13:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d95842bc-df1f-3f96-ab62-1a688da72085 | -2.70074 | -47.73837 | 2024-12-02 01:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4974dbaf-06a3-3157-815f-b5e342e05401 | -2.53395 | -54.05928 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b807e76b-76e7-3be9-af9a-7ceb48879582 | -3.06791 | -54.05517 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3ce352aa-f627-35a6-b80d-a15a305df9c1 | -3.21413 | -53.12331 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 18c95787-4e89-3ac3-8c1f-6d3f7435cdec | -1.61762 | -53.8992 | 2024-12-02 01:13:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f1df6c98-e489-31d5-9895-eeeeb21e6e9b | -1.0644 | -53.63504 | 2024-12-02 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 64632e04-338c-35d1-a899-9a0cee473b91 | -3.09705 | -53.74547 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 87aaf619-26f9-3618-9a4d-d5194189c161 | -2.44389 | -53.61946 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| f4c600c3-fa3f-31fe-802a-ee21f0ee8eda | -3.49733 | -53.44213 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4d204b40-d2f0-3f14-83ee-457e044a628a | -3.03861 | -49.38328 | 2024-12-02 01:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f2a2bf69-3476-36ee-83ba-63c1ae8480d3 | -1.69918 | -52.63682 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7113b1e7-1752-31e1-8fc2-436e2cc3fa2a | -1.37457 | -54.93071 | 2024-12-02 01:13:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 58ab5542-6d48-3e3a-8374-128d966cf957 | -2.69698 | -52.92185 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 390428ef-4afd-35d5-842b-257d345fcc2d | -2.45602 | -53.62984 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| ad062ef2-47a7-38c2-a3ea-8bcddb86dc51 | -3.08535 | -54.11572 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5eb0dc89-9264-3fdf-9038-efb1f653bb76 | -1.62767 | -52.38298 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ca49c020-b83d-302a-8910-214596e3b723 | -3.1137 | -53.99474 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| df6424bc-5aa6-32fd-a079-3c7cb6bc1d15 | -2.79636 | -53.03984 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a923800c-a7a9-3f17-b889-5f86f4b55a68 | -3.02791 | -54.03973 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 05d0d11d-6ec4-3ee3-a383-b9242817ac43 | -2.98943 | -52.51039 | 2024-12-02 01:13:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| bb9ef1e2-0883-349a-b359-f65915ab5a35 | 1.60424 | -50.93957 | 2024-12-02 01:13:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 6002160e-3365-317c-8ee1-de5a14f7520e | -2.82194 | -51.83971 | 2024-12-02 01:13:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 3c715b5c-03f5-3705-aabc-e17b8af3e350 | 0.86069 | -59.68548 | 2024-12-02 01:13:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 04ccf2f8-fa64-382c-8567-16fc189a295d | -2.88674 | -54.01199 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 6f9b83fb-0d30-3233-8af3-2b9ac66f38de | -3.49828 | -53.83781 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 0ab96aff-b24f-3e7a-84d1-b725807a2a0b | -3.52981 | -52.15791 | 2024-12-02 01:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3d96923d-e26a-3c55-b309-e8a127a473ea | -3.1145 | -53.8059 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 797b06ff-a72c-38aa-83a8-dc7b13d544ac | -3.50863 | -53.78241 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 612b58bd-b189-3907-ad34-641e3cb428b1 | -2.68868 | -51.88476 | 2024-12-02 01:13:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0d934a65-63b7-3d4f-87cc-5bf3420bbb7b | -1.57836 | -55.33834 | 2024-12-02 01:13:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dd5e623e-9fc5-3a5e-9b3a-47c81e30f2ab | -3.29695 | -52.07746 | 2024-12-02 01:13:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 1afa19c0-5911-34ba-9145-9d28b9ae08bf | 0.88838 | -50.95613 | 2024-12-02 01:13:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 16c6a88c-8228-333c-841b-a2091cd2e5a9 | -2.86933 | -54.02932 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 63b15785-48f4-37e3-ba88-7b367801a92f | -3.11493 | -54.00356 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 906837dc-2c15-3008-8e80-f7bebea279ee | -1.09543 | -53.65169 | 2024-12-02 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| c9f6aefc-5c1f-3fdc-9f4a-226caac231e1 | -0.60172 | -51.68814 | 2024-12-02 01:13:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e865defc-9e89-39ce-91ac-7a96be02e412 | -1.31669 | -51.67704 | 2024-12-02 01:13:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1af26030-3d16-3779-a583-ec09a0ec529d | -2.5315 | -54.04166 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9a257401-229b-3edd-a682-272c85a7c4f1 | -1.92228 | -52.97858 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6ea965b5-3602-3f3e-92de-b16960e01383 | -0.98296 | -47.80859 | 2024-12-02 01:13:00 | TERRA_M-M | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| b1a68766-14e0-30ae-a0bc-a29448f26709 | -2.01775 | -54.32137 | 2024-12-02 01:13:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 18f1a015-ad16-3777-81ef-bb5c8b762cff | -3.09836 | -53.28823 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 44ad44c3-2638-3af3-a209-f91b29751064 | -2.77807 | -55.35552 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| d3ebeade-a025-3409-b66c-24b3ee830175 | -3.43137 | -53.88957 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 28af9666-6af5-3a37-866f-df2c9be25356 | -2.98715 | -53.34652 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 63b5c5e9-50af-3c8e-aad7-52577611dcec | -2.64899 | -46.78381 | 2024-12-02 01:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 8eed8bfd-8abd-3c01-83d0-51204306e904 | -1.94796 | -51.21236 | 2024-12-02 01:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b117f2e6-673d-3a2a-a441-1edeb877f78a | -2.86443 | -53.99407 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |


[Clique aqui para ver as próximas entradas](README13.md)
