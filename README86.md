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
| 26a0f07a-1c4b-3dd9-a8c3-8d671dd7263c | -3.52355 | -53.51596 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 038610af-f603-3bf5-b1ea-a1c34afe0ace | -3.17943 | -54.32225 | 2024-11-24 05:40:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e305bd7-f12d-33ce-ba69-bb308a028817 | -3.36955 | -53.32558 | 2024-11-24 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5748f6c-0e6f-363f-ae45-18c1565653bb | -3.50364 | -53.81727 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ed2f70e7-7aae-3a13-a617-e431efa6c32a | -3.25693 | -54.23697 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d02699fc-b68c-319b-ac84-a5bbad5ff1df | -3.51348 | -53.79211 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a985d67c-8c8e-3319-be12-adc949a565b5 | -3.50552 | -53.80467 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bccf82e7-5c4c-301c-a23c-b3e60d9e5a97 | -3.24718 | -54.22554 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91dea598-058c-36ab-b970-ab38f128d367 | -3.51218 | -53.80082 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02a5ca35-05a8-3e19-9bfb-b246f3a97078 | -3.24602 | -54.231 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab1ca086-c630-32d7-8e98-024b4ca888bb | -3.25302 | -54.22374 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3178dd5a-bb73-3c88-a064-488eea017a38 | -3.4192 | -53.28569 | 2024-11-24 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 833d1425-79ea-3cb2-becb-0a05c64e5470 | -3.23448 | -54.22921 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 545e2a69-6c5c-3a39-b969-8fefe6876a8b | -3.50681 | -53.79596 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7856572-52d8-306a-b2cc-5b81b46ce7d6 | -3.23854 | -54.24463 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52133fa5-7ed7-3812-b589-0f8cf6a78c1f | -3.5183 | -53.82079 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 485cbc25-d859-306f-8b0b-8e2b20ea611a | -3.24878 | -54.25174 | 2024-11-24 05:40:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b5845b8-aed9-389d-b671-aad239149db6 | -3.2495 | -54.25048 | 2024-11-24 05:40:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30a9f1ff-52bf-36b2-8034-5f4f4643314f | -3.27153 | -53.82039 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8382273f-e3d8-336e-803d-5cbb23a4df21 | -3.25055 | -54.24004 | 2024-11-24 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d40fb0f5-1d0d-3543-88dc-ad1dd7424fc9 | -3.4749 | -51.99447 | 2024-11-24 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3c61dcb4-20a1-3751-895e-afa9d8d0ac7c | -3.42534 | -53.28671 | 2024-11-24 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68ad4abe-31a0-3e8a-9131-eeb89f486422 | -3.52427 | -53.82155 | 2024-11-24 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 607b2157-597e-39a7-9e7d-252dc56bde09 | -2.85675 | -53.96286 | 2024-11-24 05:42:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 005d4a4d-da88-30ef-9b5f-cfab60483ec0 | -3.6728 | -50.25129 | 2024-11-24 05:42:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 57623e30-f98e-332c-8839-b025e71279f9 | -3.29779 | -50.35824 | 2024-11-24 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3934b7b0-b641-3246-92da-0e5acadfe4a8 | -3.58639 | -49.35256 | 2024-11-24 05:42:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0e0bce48-c36b-354a-898e-b2f9df8ceff8 | -3.24201 | -50.11872 | 2024-11-24 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bb1db994-fef6-361c-b59e-a3eb95623ad1 | -3.24216 | -50.6601 | 2024-11-24 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 9549e753-9dcf-3a49-92fd-281d0394c346 | -3.32038 | -49.89682 | 2024-11-24 05:42:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b2d8760e-ddc3-3fe6-84ef-0c465cca138c | -3.85943 | -50.05748 | 2024-11-24 05:42:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 14e3e096-d2e6-3b6e-84fe-9552e20de745 | -4.39898 | -49.65383 | 2024-11-24 05:42:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d2eb5f40-7a0a-3b48-8775-6ef5756912a2 | -4.08142 | -50.36056 | 2024-11-24 05:42:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8920aa4c-e3e3-3701-ae33-131531c9e553 | -3.29126 | -49.91053 | 2024-11-24 05:42:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5a309193-3675-3556-ac04-19521872c7c3 | -4.63998 | -48.84019 | 2024-11-24 05:42:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 46d3db6e-e533-3e77-badc-1e220923dc06 | -3.26649 | -50.43721 | 2024-11-24 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f446b29b-0697-3e7b-a4e7-d745ff5b414c | -3.70363 | -47.60337 | 2024-11-24 05:42:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9534756e-532b-3c85-88aa-79f7428e6599 | -4.15369 | -54.58155 | 2024-11-24 05:42:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 3c989094-c8f0-3d45-bf0b-cc18794e6d6f | -3.24049 | -54.22139 | 2024-11-24 05:42:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| d791b71e-dcc8-3c78-b9fa-53324be8bd94 | -2.9987 | -52.50655 | 2024-11-24 05:42:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ec5a6cf0-1d9a-3feb-a85b-de35e561a2e3 | -3.10083 | -53.9986 | 2024-11-24 05:42:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 70c24cf8-9f35-307b-8bd2-a9e8319f9a47 | -3.75864 | -49.92926 | 2024-11-24 05:42:00 | AQUA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 419d38b6-af58-3a4d-b916-f926c9fa99ec | -3.0651 | -49.19425 | 2024-11-24 05:42:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 05b2a536-1e15-31f7-9e1e-2de93b488d51 | -3.51345 | -53.81902 | 2024-11-24 05:42:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 8d25ee7a-d5bc-3de8-8cfa-c79ee9c2e516 | -3.67166 | -54.57734 | 2024-11-24 05:42:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9431f97a-3736-37d1-8ff3-6b5b477a673d | -7.56502 | -49.40211 | 2024-11-24 05:42:00 | AQUA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 96e83694-6364-3569-8360-6a7321e7b632 | -2.8559 | -51.81819 | 2024-11-24 05:42:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9339fdea-44e5-32d9-977a-f6db65ebb557 | -3.81797 | -52.2301 | 2024-11-24 05:42:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e465fe6c-4a07-3980-9929-443708c48969 | -3.84631 | -44.05307 | 2024-11-24 05:42:00 | AQUA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 70dc6d5a-29b6-355b-8c7b-0a69bd25ccfb | -3.60227 | -47.50224 | 2024-11-24 05:42:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 48777fb8-2a3f-32e7-b261-cd5fce91e867 | -3.06926 | -50.94968 | 2024-11-24 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| ec79e2be-fffe-346c-a161-e17f3d92a9b5 | -3.7006 | -47.59628 | 2024-11-24 05:42:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8f9bb006-bba6-3902-817a-a8bd854ec219 | -3.29258 | -49.90174 | 2024-11-24 05:42:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cc49b944-da68-393e-b027-2b7e7c7120b6 | -3.82566 | -52.41152 | 2024-11-24 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| fd542dba-e112-370d-92d5-81df14c670ef | -3.7468 | -50.00837 | 2024-11-24 05:42:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ecd9be5e-4f0a-3a3d-96dd-0249a2df2164 | -3.64142 | -50.21976 | 2024-11-24 05:42:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1f91cc2f-d8db-3928-b666-4eaca3673e61 | -3.47499 | -51.99345 | 2024-11-24 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| b34ba4bb-8f01-358b-b193-5caefac11f91 | -3.69905 | -47.60662 | 2024-11-24 05:42:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 41015af2-8ec8-354f-a049-dd163491d9ad | -3.96283 | -46.72607 | 2024-11-24 05:42:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f94eb2dc-a708-3af4-967a-0c144a557b54 | -3.47646 | -51.98376 | 2024-11-24 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ea65532e-5a52-3b0d-bf00-ee1da7edc5f7 | -4.37555 | -49.75002 | 2024-11-24 05:42:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3567f4d8-531b-365a-852e-53e80a57f448 | -3.27019 | -53.81435 | 2024-11-24 05:42:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 26071dfa-72bf-3bbd-9bf9-7e35421c49eb | -3.7733 | -52.39791 | 2024-11-24 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d0b1dcc5-e6c4-3f81-ac39-49abfa54c30c | -3.77175 | -52.40812 | 2024-11-24 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e4f44dde-fdf0-395a-a1b8-59f9a6e5345c | -3.03552 | -49.45287 | 2024-11-24 05:42:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| a99dabc1-4a18-34d4-9437-e220746e0881 | -4.63089 | -48.83894 | 2024-11-24 05:42:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 8bc03a82-5a7b-309c-8517-a9f37e4f2ff0 | -3.24963 | -53.27621 | 2024-11-24 05:42:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a903fb17-d726-3567-a457-ae5331976bee | -3.06377 | -49.20317 | 2024-11-24 05:42:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 03194490-4f72-3716-b6d9-58a83dca8a45 | -3.18049 | -54.32392 | 2024-11-24 05:42:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| ca7ca0ed-2613-30c5-8684-20ecd20debe6 | -2.69873 | -51.9901 | 2024-11-24 05:42:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9416e541-1051-3c23-b71d-bfc46b138b0f | -3.15248 | -50.57764 | 2024-11-24 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3ddf7ea0-7952-3291-8a18-a02e8da06cc5 | -6.86576 | -51.98489 | 2024-11-24 05:42:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 61cd4ad2-18a4-3da4-a661-adbb99fe429f | -3.02666 | -49.45158 | 2024-11-24 05:42:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9f9c3cd5-9636-3ede-a82a-ef0652f01b06 | -3.63019 | -52.25115 | 2024-11-24 05:42:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 71b24b61-9b20-369f-99cf-c88141d876d6 | -4.15583 | -54.56786 | 2024-11-24 05:42:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 9b6bbb51-f110-37ea-b6e8-175616f04825 | -3.38532 | -50.31701 | 2024-11-24 05:42:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 5b1b94ab-ece5-34cf-9fb7-b141be07e286 | -4.49063 | -47.10808 | 2024-11-24 05:42:00 | AQUA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 667ff09c-935b-3d07-bd1c-77608c18fc6e | -3.2396 | -53.27465 | 2024-11-24 05:42:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| badffc83-9062-349f-ad45-3228ed4f2709 | -5.9537 | -48.04617 | 2024-11-24 05:42:00 | AQUA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f4c0e4c7-a2cf-38f0-988a-7c387ac39cf7 | -3.221 | -53.92394 | 2024-11-24 05:42:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| f113e94e-84bb-38f8-bfe0-a7b8703dd3e1 | -3.05275 | -53.22294 | 2024-11-24 05:42:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 22d856a6-59e0-3dee-ac4f-87d17d833232 | -4.2148 | -50.40149 | 2024-11-24 05:42:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| ac335c0e-6984-3df5-96d5-aee27ffdf5b3 | -3.50833 | -53.8111 | 2024-11-24 05:42:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 1b0d0c08-2578-3153-a24a-ffe1905745d6 | -3.60072 | -47.51268 | 2024-11-24 05:42:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a0b0ad1f-ede7-32b4-9886-834068129c6c | -3.10626 | -53.99291 | 2024-11-24 05:42:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| df53b8f3-7cff-3b53-b8c4-8eed8594e27d | -3.28168 | -50.03475 | 2024-11-24 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5ace7277-e81b-3cc9-ae0d-530d8a0617ca | -3.03684 | -49.44403 | 2024-11-24 05:42:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 195a7ba8-1a81-3eae-b3aa-cfdfd4214213 | -3.51542 | -53.80649 | 2024-11-24 05:42:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| f447920d-bcf6-3e39-9f4b-85a59383f70b | -3.074 | -49.19554 | 2024-11-24 05:42:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9e1ec6c4-958e-3e41-b96e-b0f6f86b68a3 | -3.86075 | -50.04869 | 2024-11-24 05:42:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| aa234b52-f261-35ed-b513-e5ae03f29021 | -3.25126 | -54.22302 | 2024-11-24 05:42:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| e18f67bd-7873-3a0a-a3cf-3680703f72bb | -3.384 | -50.32583 | 2024-11-24 05:42:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2f09eea5-2fb1-321b-9460-65570dcd0004 | -3.15115 | -50.58651 | 2024-11-24 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8218c826-3968-3a49-a214-c0dce7805984 | -4.36742 | -48.5648 | 2024-11-24 05:42:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 012c22cd-e0b8-35e4-87a3-8960c461bc95 | -3.80581 | -51.33662 | 2024-11-24 05:42:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 51eb4ff9-6204-39f3-86c2-4ae0836e3d03 | -2.90408 | -51.56065 | 2024-11-24 05:42:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7895aecb-1bd7-3ee5-9234-530c7eee3cf3 | -3.38018 | -50.72919 | 2024-11-24 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a2199929-a88d-3728-a86a-d2cdc490afd6 | -3.93075 | -48.14627 | 2024-11-24 05:42:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5c6322f0-c0e2-3313-9ffa-16f4a8fb0e04 | -5.09596 | -43.14162 | 2024-11-24 05:42:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 35.2 |
| a454a42b-d6eb-3b2b-9a7e-0937bd946da1 | -4.40786 | -49.65511 | 2024-11-24 05:42:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README87.md)
