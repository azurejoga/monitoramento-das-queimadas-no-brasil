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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3685eb5e-d6da-33f3-a881-eac60ba42bb2 | -1.14611 | -49.19072 | 2024-10-16 04:04:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 572ebba4-41f6-35c6-90f6-274227dd8a64 | -1.14557 | -49.19398 | 2024-10-16 04:04:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2f2bcbe-9f0b-3757-8458-812c1f358cde | -1.14295 | -49.18689 | 2024-10-16 04:04:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f99b9ff-f147-3a41-82ba-86ecf45ae073 | -1.14244 | -49.19016 | 2024-10-16 04:04:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac1a4d31-10a1-32a4-a167-85c760dafadf | -1.14193 | -49.19342 | 2024-10-16 04:04:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d374f913-33d3-3c8f-82da-6073660dbbba | -1.14134 | -49.18659 | 2024-10-16 04:04:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 204cfa8f-55ef-3264-bb3c-ce02cb53edb8 | -1.1408 | -49.18985 | 2024-10-16 04:04:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14ee2554-5f36-33ed-bb79-85e6ab299a3f | -1.13971 | -49.1729 | 2024-10-16 04:04:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| da8dfd5a-d90d-3973-a75e-8550e16a824b | -1.13919 | -49.17618 | 2024-10-16 04:04:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b0a83197-aebb-37f0-acda-0db821c70192 | -1.13873 | -49.1694 | 2024-10-16 04:04:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0d1d62c-221b-3bf8-b609-84d7ed0135cf | -1.13867 | -49.17946 | 2024-10-16 04:04:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c54935e4-4172-3120-b5db-5d5ab456240a | -1.13819 | -49.17266 | 2024-10-16 04:04:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b85a1ab1-f8f2-3e4f-ae9b-c6fb7034134d | -1.13765 | -49.17593 | 2024-10-16 04:04:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fa95d74a-4a9b-336d-bbc5-d19aeaa085af | -1.13711 | -49.17921 | 2024-10-16 04:04:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1df9a6a6-d4eb-3b84-b847-1075de7e667e | -0.86535 | -48.70979 | 2024-10-16 04:04:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3df5f62-c275-32c2-8902-3e9bc347dc7a | -0.86486 | -48.71287 | 2024-10-16 04:04:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 322023c4-d880-3bf2-a94a-e646cc0d5cd5 | 2.28784 | -50.85244 | 2024-10-16 04:04:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 073c9698-0151-3d03-8195-7d713a77c191 | 2.28161 | -50.85342 | 2024-10-16 04:04:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 477df363-aba5-3cb5-bb16-71dd06b0d3b4 | 1.0016 | -52.2164 | 2024-10-16 04:05:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 04b90b59-d3fc-3dd3-bbd0-810b144b1148 | -3.1098 | -54.2464 | 2024-10-16 04:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 7d1e7132-6513-3ef3-8426-14a34ba6a0f1 | -3.1099 | -54.2263 | 2024-10-16 04:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 142.0 |
| 9e6ecd35-cdc6-3d3a-b7d8-0a89a60309af | -3.1282 | -54.2459 | 2024-10-16 04:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 02c97285-b3a9-3c00-8c7c-22a122a945b9 | -3.1283 | -54.2259 | 2024-10-16 04:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| b36e2b68-0a43-3388-ab39-f74ad04f8594 | -3.958 | -46.4442 | 2024-10-16 04:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 5b90e3a9-1fd9-3965-a517-ac951b45bff5 | -3.9581 | -46.422 | 2024-10-16 04:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 1e0feb45-87c3-3aa6-90de-1c89fe5b92be | -9.1728 | -65.3945 | 2024-10-16 04:05:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| f683ba8c-a3ac-3b09-aa44-e4916e54297c | -8.18839 | -40.99978 | 2024-10-16 04:06:00 | NPP-375D | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 099d65d3-eeec-3899-8e76-b72b6a4def7d | -3.27914 | -50.93941 | 2024-10-16 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c60996ce-1be5-3993-8adf-cb66c0bfab92 | -3.27521 | -51.52341 | 2024-10-16 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0a972eb-7c01-35b5-b79d-437de0d8b712 | -3.19864 | -51.03077 | 2024-10-16 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d01a9d19-c9f7-3abd-8c0b-d9245222cde2 | -3.19794 | -51.03504 | 2024-10-16 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c0e9e73-ff8a-393f-84f9-0547937631e6 | -2.90547 | -51.82078 | 2024-10-16 04:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ece9bf2a-7eb9-32c6-ad61-cab2779c7890 | -2.90015 | -51.81491 | 2024-10-16 04:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f208bd3d-7e95-34fa-a34a-3e07742409ce | -2.88562 | -51.67866 | 2024-10-16 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aa7fbca1-6f25-3672-bbde-b32aa8f5b6d1 | -2.88485 | -51.68319 | 2024-10-16 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 03a02810-cec1-32d5-8c7f-5be25d3d56ae | -2.88475 | -51.68091 | 2024-10-16 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ffe964bb-9081-3293-a450-19a8ff4b475a | -2.88407 | -51.68773 | 2024-10-16 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 03040038-ba0c-3664-9aeb-7effb70cf4ec | -2.884 | -51.68546 | 2024-10-16 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| cc7a383b-a2a0-3dc0-9e82-6eb16a52e197 | -2.87955 | -51.6776 | 2024-10-16 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cf78e12f-80e0-371c-ac8d-0e21e844fbb8 | -2.87942 | -51.67527 | 2024-10-16 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8bbe4d9-29d6-3989-a800-c573a05b8f0f | -2.87876 | -51.68218 | 2024-10-16 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 07cb907d-39d5-3a17-8b3f-9b8a140716fb | -2.87867 | -51.67986 | 2024-10-16 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b90d9568-a620-3591-bf97-679112c9b1fb | -3.75108 | -51.93715 | 2024-10-16 04:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1c87ff0-e509-3d09-8bcc-d8319af37004 | -3.7164 | -51.40445 | 2024-10-16 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0169fb6-0435-3607-9959-77b2461f0b18 | -0.98106 | -52.44305 | 2024-10-16 04:06:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ce8c004-6214-37c2-a56b-c73d18e80689 | -0.98016 | -52.44858 | 2024-10-16 04:06:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12970da3-9bfe-3917-9136-1b867e4f4eb1 | -3.12385 | -54.23115 | 2024-10-16 04:06:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| d599998f-338e-3f4a-8e5e-9288ebad29f1 | -3.12271 | -54.23772 | 2024-10-16 04:06:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 11a34fc7-f10f-36d6-a327-b25523948593 | -3.12158 | -54.24427 | 2024-10-16 04:06:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 06159ae0-b178-3b46-b6f7-fd59ca2e69d9 | -3.118 | -54.22299 | 2024-10-16 04:06:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 8d0beb15-02b7-3c7c-ac66-11e8cb3423b6 | -3.11679 | -54.22994 | 2024-10-16 04:06:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 2ecff949-720f-3c6e-910b-06cd7e76ce2f | -3.11566 | -54.23643 | 2024-10-16 04:06:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| a8bb2522-2725-3398-8ec1-d6c167dd0aab | -3.11454 | -54.24286 | 2024-10-16 04:06:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1beffe48-cd65-32f1-aa55-cc8817c93493 | -3.11222 | -54.2144 | 2024-10-16 04:06:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0f3cab1f-9edc-397c-9348-a7cf2f2aac1e | -3.11102 | -54.22129 | 2024-10-16 04:06:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 022998c7-f512-3fda-b687-e7a8053da02f | -3.10975 | -54.22857 | 2024-10-16 04:06:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 57a92724-60a9-34e0-9620-0c4440230998 | -3.62755 | -54.67084 | 2024-10-16 04:06:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1946ac6-8de3-3aa3-9bd3-cc962b2bf703 | -3.62256 | -54.67004 | 2024-10-16 04:06:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5e82dbbe-11e7-3fd1-a070-fabe4e43c8c3 | -3.62033 | -54.66978 | 2024-10-16 04:06:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 835eb0ca-2e25-3814-ab40-5bcfb87ef44b | -5.02336 | -37.6506 | 2024-10-16 04:06:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c80d6417-84ca-352c-bfa7-0d5891c5813c | -5.02138 | -37.64789 | 2024-10-16 04:06:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6b6b5dfb-b615-3524-b2fc-99e98a352362 | -4.98937 | -37.41089 | 2024-10-16 04:06:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1697b586-b074-34fd-b9c3-873576fb255e | -4.98565 | -37.41031 | 2024-10-16 04:06:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7232760b-d873-34c8-996e-16ce085d725f | -4.7299 | -38.45662 | 2024-10-16 04:06:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b5f48577-9026-3650-bc98-94bafbd599d2 | -4.72578 | -38.45998 | 2024-10-16 04:06:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 568fb959-980d-3098-89b7-70ada6cd00f7 | -4.72226 | -38.45943 | 2024-10-16 04:06:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 375b7fde-daa8-30d4-bcaa-5057878ea9b3 | -4.72166 | -38.46334 | 2024-10-16 04:06:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d0396f52-ba24-3612-86ad-8a9c1d4b3acf | -5.33127 | -37.83271 | 2024-10-16 04:06:00 | NPP-375D | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6bd872db-3026-3b2c-9214-a62b708a7d9a | -4.66867 | -43.86232 | 2024-10-16 04:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a67e052-7e45-3432-b6a4-02acf3e769b5 | -4.36505 | -43.94587 | 2024-10-16 04:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e22f8478-711a-3af5-86e8-759bfb99e8a8 | -7.36537 | -35.23154 | 2024-10-16 04:06:00 | NPP-375D | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7ee550f9-faad-35ba-8124-a5cc31acbdbb | -6.56758 | -35.12152 | 2024-10-16 04:06:00 | NPP-375D | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 01d6b30a-8528-347e-8748-50b9e7c2cb11 | -8.07228 | -34.97733 | 2024-10-16 04:06:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a6fa2be5-3cd1-36be-847e-580d061dd399 | -5.45677 | -36.71249 | 2024-10-16 04:06:00 | NPP-375D | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 359c73fb-599d-34fd-b25f-2e80ddbf7c9b | -5.45604 | -36.71738 | 2024-10-16 04:06:00 | NPP-375D | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| af758990-f108-3384-beae-b5d12f536bef | -6.64697 | -37.37619 | 2024-10-16 04:06:00 | NPP-375D | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 43936d23-e5b6-3529-83c7-7db54df4cb41 | -8.80211 | -37.71059 | 2024-10-16 04:06:00 | NPP-375D | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4e7dbd9a-60b2-3d9e-a79a-d1b9d60ac29c | -8.80046 | -37.70837 | 2024-10-16 04:06:00 | NPP-375D | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5d1a5766-ef0d-3bed-a093-6a78c8182526 | -8.64738 | -36.93029 | 2024-10-16 04:06:00 | NPP-375D | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a1eef8d6-50ff-39e3-ab7f-29acc0e2e6a7 | -8.64688 | -36.93379 | 2024-10-16 04:06:00 | NPP-375D | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e37f0ab2-92ac-3d65-8d00-b5c1423c1bb0 | -3.49512 | -39.6712 | 2024-10-16 04:06:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b68f2edb-a353-3446-b2bc-e7a56039fb82 | -4.79114 | -39.77579 | 2024-10-16 04:06:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 590330ff-425a-38af-be2b-b5dadf50b4b7 | -4.79058 | -39.77937 | 2024-10-16 04:06:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 661ecebe-5c2f-3f3d-9b9b-36f3bd2b7e71 | -4.79002 | -39.78293 | 2024-10-16 04:06:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 45ca8aa4-9057-3697-9539-602b3a792d7f | -4.78947 | -39.7865 | 2024-10-16 04:06:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a4459e83-fb37-3b40-9083-9bc0bf753e07 | -4.78666 | -39.78239 | 2024-10-16 04:06:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e0d0b394-a7a8-343c-a791-ee5775944497 | -4.7861 | -39.78595 | 2024-10-16 04:06:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c50cd2b7-4742-3c7a-ac71-e56191b54abe | -4.33626 | -39.13596 | 2024-10-16 04:06:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| acf1a91d-a372-3e60-bc22-f1d8ed415da4 | -4.33569 | -39.13964 | 2024-10-16 04:06:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| adf6d76b-dfb8-38fd-91e1-16a986107ea6 | -4.33284 | -39.13542 | 2024-10-16 04:06:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b274596b-7cc4-320e-a1a8-7ddc2099946b | -4.33227 | -39.1391 | 2024-10-16 04:06:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cfe8d1f4-d008-3585-85a5-6c28f17604e4 | -6.83835 | -40.08062 | 2024-10-16 04:06:00 | NPP-375D | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b57e1141-dfa6-380a-95d7-0aa04fa62f12 | -8.13308 | -40.07412 | 2024-10-16 04:06:00 | NPP-375D | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| be8c0be9-b682-3d76-a884-03c8e0084a9c | -8.0043 | -40.59378 | 2024-10-16 04:06:00 | NPP-375D | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e14a4d6f-0daf-3768-8038-c45b2bc850ab | -8.00149 | -40.58968 | 2024-10-16 04:06:00 | NPP-375D | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f324dddf-4e57-3e10-abd4-9b3a3b510fb9 | -8.00094 | -40.59325 | 2024-10-16 04:06:00 | NPP-375D | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0dafb240-8d9a-3e19-8924-b60ea2a00a2c | -4.30624 | -41.48363 | 2024-10-16 04:06:00 | NPP-375D | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4bae3a62-abbd-3b28-a92c-53ddcf88ae28 | -7.60336 | -42.21961 | 2024-10-16 04:06:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 29589780-5d60-3234-ab4f-0c686bd698c2 | -7.60281 | -42.2231 | 2024-10-16 04:06:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 41235c48-a4f0-37a2-8767-bc4658b6c54a | -7.59948 | -42.22256 | 2024-10-16 04:06:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README31.md)
