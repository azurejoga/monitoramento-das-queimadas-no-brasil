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

## Dados Diários - Página 186

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 200c51e7-f1f4-307b-9f2a-8ca37da182c2 | -3.44127 | -56.93642 | 2026-10-08 05:42:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aaf456c8-fa09-3606-92bf-3030b12794af | -3.87198 | -55.99627 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7dec77cf-deb0-3e7e-bccc-78e136d77d24 | -3.98095 | -56.21503 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 242e46b1-d585-3fe8-8ad2-10f9a0e43d54 | -3.47271 | -59.56724 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4150852-6254-35ea-96c1-cccaaff83cf1 | -3.02207 | -53.92716 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3cab3fb4-3dfc-3288-bca1-0f60e209d433 | -3.0803 | -53.9603 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| c55472ae-2be5-3eff-90fb-7db49bd5b9f8 | -3.28606 | -54.05608 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4a3bc35-3e7d-36ff-ae78-513438b3c8f5 | -2.99099 | -54.06266 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51e0d449-3f77-3744-a2aa-3305d027f122 | -3.30228 | -54.697 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdfc460a-a95d-398f-9096-df3ed2b7b1d0 | -3.12101 | -53.79488 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 305b5357-a579-3637-be50-f15fdb05aa00 | -7.21675 | -55.10604 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38ae3ecc-26db-345d-8575-1e98c634ecb1 | -2.89018 | -54.16345 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a839919d-6e8f-3e6c-8f18-6870864d02b2 | -3.17069 | -50.45478 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eac43054-aa1e-36b7-a76b-c2e480c906c7 | -3.28071 | -54.05529 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46851ddf-4684-33aa-905c-f16933256a36 | -3.52861 | -54.67278 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c49cf506-1028-39b4-ae0a-a35d99ef37d0 | -3.02904 | -54.09874 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7817a956-4e7c-38ea-938d-cf5b4e61b330 | -3.96666 | -56.11814 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0e51d898-3a4b-3889-b7ad-1f82cdd2590b | -3.18689 | -58.65889 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7182ac1-7232-36b8-8b2d-4a2b0e7d07fd | -3.52186 | -54.66704 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65f30023-b18c-3074-9332-6dfd86fe68f6 | -2.99533 | -54.07008 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d75443a1-e672-39e7-857b-7ad18df34dfe | -3.51025 | -54.53515 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f6f26c5-4251-3cd2-b473-d6d503133d5b | -2.75312 | -54.11457 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc12283a-b9c7-3a05-8027-e9495cede37d | -3.02239 | -54.07087 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c068f9a-7812-3485-aaef-57591173d1be | -3.30606 | -54.03141 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b5fabc0-967b-3374-816f-392cf643da6b | -3.08437 | -54.26358 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1b44edf-69bd-3341-a6b3-bf747de9172f | -2.92924 | -54.11957 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 84376840-38bc-3b59-b31d-ecb61bb179cc | -2.76781 | -54.08487 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98970384-e9d7-37f1-a95a-c013ee679304 | -4.42864 | -59.49226 | 2026-10-08 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46e39b84-1a9a-3990-a974-4fd37eb45e4c | -3.01028 | -54.07911 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d9f6dcac-f3cb-3d9d-9dbb-d730c97e55bc | -3.61819 | -55.50496 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50f8d433-b25a-3459-9752-f62f5077d521 | -2.51643 | -56.25699 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b871712-f912-37ae-b9b2-2e615fddf376 | -4.38521 | -59.90457 | 2026-10-08 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80949bbf-0d4a-3a31-8d89-83ed33e96f48 | -2.50263 | -56.07461 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| da7be6be-e1f0-3a29-b499-c3e2eba86f18 | -2.98904 | -54.07584 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5e0784a6-c2d8-3ad2-b943-28653f38cab6 | -3.29293 | -54.00887 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34732e42-2795-301c-8c55-26711b722850 | -3.09148 | -54.28772 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df330389-0e5a-37b3-bc24-2a12526088c3 | -3.81973 | -57.17208 | 2026-10-08 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e446dc2-5ccb-38bd-b9f9-f1fa67fdd77c | -3.27983 | -60.99448 | 2026-10-08 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d995b885-c1c0-3da2-ae1f-d9574e1fad9d | -3.25775 | -54.04104 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 965d8dbe-74cb-3735-9856-a51e858b7024 | -4.09777 | -52.07315 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 762957f0-8534-32d1-a1c4-273f956e3a94 | -3.28309 | -59.41544 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c5ddf63-d95c-3ba0-85ac-90bcb37f8bd5 | -3.27271 | -54.05045 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 113e6311-6c44-354e-9ee4-3871c91b1381 | -3.60017 | -61.633 | 2026-10-08 05:42:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94d1df2a-6fc5-3b8d-88ea-ce9b125d288f | -3.02492 | -53.94485 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 14113321-a5e7-3b10-a02e-bf1a2ea8eb40 | -3.69245 | -59.64684 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4a9a2cf-af78-3e46-a63f-d80aa55f9871 | -5.25997 | -60.17477 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07196d61-d146-3245-827c-b1ccbde33fdf | -2.99631 | -54.06351 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50e542a0-4d74-3d9a-9c48-5ca7aa3c6cc8 | -3.31143 | -53.86887 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1a846bc5-6231-367b-9715-55a5c28aea87 | -2.84304 | -57.48665 | 2026-10-08 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d6a80f3-7e9f-3c8b-a2a0-dd8b12ae3cac | -2.77408 | -54.07915 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| afd1fd9d-9c48-3cfc-acf3-cce22ce12214 | -6.24554 | -52.86876 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d49ef2f1-c594-30da-80ab-d1a5edff0b30 | -3.73833 | -59.44925 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d7bd77e-65ef-3096-a8aa-27a48b726f3c | -3.01646 | -54.11021 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4430ff9a-481e-39e1-9b8f-b7f06c56c36f | -3.29256 | -54.0636 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 824d02ac-8f22-3409-99bd-4eeafedbcb25 | -3.86725 | -55.99565 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f593f20-a230-3293-832d-674e97b206c6 | -3.48618 | -59.57833 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8797fede-0ff9-3fe3-b01a-ca00bf3aac46 | -2.97505 | -54.13363 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4822ca4-8f27-3017-a69d-9d982aa05c3f | -3.57544 | -54.67608 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b39ebadb-a4d1-3758-bd6e-96db52daa20b | -3.0277 | -54.07166 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11ed63a4-8761-3101-a62c-d9a5074d3ee6 | -3.31191 | -59.61202 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c29ee5b-c4f5-3952-90c5-2b240f8f833a | -2.38471 | -56.13923 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 566a42fc-6657-3e56-8430-817cdb83592a | -3.30309 | -54.05167 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eb909c41-85b3-34fe-910b-a408ec56d449 | -3.17037 | -50.5924 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| f0d56e0b-474a-395f-a300-889f3cb48b0f | -3.17269 | -50.60263 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| def4a46c-cf8d-36a1-8a23-ed4610d16c30 | -3.55312 | -59.50055 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 054dd29b-a9c8-3c9a-8261-ef6d7fb541b0 | -3.10149 | -54.2925 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b684193c-03df-3621-9c91-71cabf918ed3 | -4.60311 | -56.08147 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28292185-c2d3-3c99-b14c-605134981dd0 | -3.2317 | -57.88032 | 2026-10-08 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 31224ff6-52b8-39cf-a725-0411d98324df | -3.8433 | -55.98503 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fe409608-fc04-336d-a293-9b53f2a38fab | -3.29824 | -54.0475 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd697a80-1c76-3a76-a06c-100b9287f949 | -5.29341 | -60.10468 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be909d3a-fb75-3465-827f-ddd197e7c3bb | -3.2953 | -54.06759 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e194abc1-76cb-3114-a10d-158f084c4cdf | -3.67527 | -59.63526 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7abebcbd-0084-3528-afd9-50c9fca290c0 | -3.29873 | -54.04413 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae741ee2-35fa-3ebb-a201-298acfa9a6be | -3.29578 | -54.06429 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4253a7ad-c4ce-3744-abd9-378500838d12 | -6.99725 | -59.11325 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 084e52d9-4655-3040-a420-ee9146778d07 | -4.14126 | -54.92255 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53465a7e-cf7c-30d8-88ca-fdab4271251e | -3.70839 | -60.54601 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44f8f9ee-4f6c-3e60-afb3-7f555a599fcf | -3.48118 | -54.62276 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebced2dc-efcc-36f5-840d-bb26b3b6e5ea | -6.25157 | -52.86958 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 43ef55f3-4336-34b3-a935-ef477a71e50a | -3.00786 | -54.2385 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 863e4e22-4aa8-3a06-b2c3-7c2f3db07b68 | -3.57213 | -54.66302 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3aa2f292-2a55-37a8-a611-0acc35d4a863 | -3.30042 | -54.67504 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 366bbbfe-c02d-36d7-a9ec-cb9ac2822874 | -3.08767 | -53.94735 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8a63a9f5-dde2-3720-95fb-9c11596ac88c | -4.37388 | -54.74999 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe93845e-9f52-38c1-a075-b9654614dd00 | -3.47506 | -59.57661 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29130a24-6669-389d-aa0f-6c9557cc3a0f | -5.29717 | -60.09939 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73ac8118-3290-3340-88ff-e8f2b9d81885 | -3.0088 | -54.08899 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| aff51e84-ba5d-3dd1-877c-82fbf36068ee | -3.00077 | -57.75645 | 2026-10-08 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0c706bc-3f20-30b5-b9bc-0f874aaa88cb | -3.56924 | -54.35763 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cd4af19-26c9-3d88-a189-0e5d9d3c853c | -3.30554 | -54.67582 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c4fdcc1-9101-389a-b151-3d69930264a6 | -2.4698 | -56.07424 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 252f40c6-c9b5-3e58-97e4-ed7563b1a567 | -5.29912 | -60.0922 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 906ecd66-d03f-3af6-aef4-906bede2ae98 | -2.44003 | -58.01852 | 2026-10-08 05:42:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81bfe446-c6e0-33b3-93ed-80184f853ef9 | -2.82983 | -59.24451 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbef05fe-3888-354d-b8dd-88729d0dbea4 | -2.46377 | -56.08307 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab362f9f-065e-3df5-894c-61f40ef798fa | -2.4761 | -56.09463 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71a2904a-5e44-3bd8-8e6d-652a48fd7c42 | -3.57682 | -54.66689 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5667324-f11e-3bf0-b2b3-d814b087d0f3 | -3.35877 | -50.47693 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab75c744-46de-3d69-8bcf-204373987d56 | -5.29782 | -60.09504 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README187.md)
