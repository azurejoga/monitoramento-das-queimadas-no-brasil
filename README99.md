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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81f02524-949a-3130-aa0b-70605ce5986d | -5.71957 | -42.67161 | 2024-11-10 04:38:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ae8612c7-c319-3384-ba16-a9865db7726e | -3.04405 | -49.53481 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e24265d4-7570-3f53-94dd-d8cc457af105 | -2.20016 | -51.87531 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e6e0f7c0-0f39-36e5-a20d-74368547326e | -5.54101 | -47.19431 | 2024-11-10 04:38:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d0d3d10-deb2-367e-a5a3-3eca30ac230a | -2.66188 | -49.85258 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 62196891-28e9-3936-b8a6-ad4fb2e14297 | -3.02569 | -48.08095 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f518e3e-46d4-3a7e-8a3b-c3bef18068fe | -3.21916 | -50.28329 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 88972755-cabb-38c5-b5f2-044b112a41a4 | -4.05333 | -48.25858 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da79578a-3351-3a52-9d96-893b81bb5e5a | -4.11296 | -46.88665 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c83f2e20-563e-32bd-b178-a525abe106f3 | -2.80844 | -52.99883 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd7ec6fb-5636-33f3-a5a1-57cc9f895a0f | -3.53286 | -50.33207 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bfec5af2-227a-3d1f-8d1b-99e807e8cbeb | -2.81209 | -51.8054 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c2bb5fdd-6c21-379c-9cef-de1791da3c7c | -3.7315 | -53.7689 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3de6439-3c81-39d2-9274-bffcf440fc9a | -4.51382 | -45.69982 | 2024-11-10 04:38:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bca98bbe-4260-30f6-bb26-f6fbca5acf89 | -4.01785 | -48.29211 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fbd30d89-6ca5-34a1-9289-893ba9da9116 | -3.94611 | -46.40912 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf324c69-e15d-3718-8fa8-df5ede5cb629 | -3.94201 | -49.75798 | 2024-11-10 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df9722a2-1f52-3b5d-b73e-16f4a098a529 | -3.02844 | -49.54673 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56edc985-d38e-318c-84c5-36df22131992 | -3.15744 | -54.47698 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37334b9a-41c7-3be5-802a-addbdcec55bf | -2.26557 | -50.67533 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 446c74b2-4b52-36f2-a1d0-65289bad4a64 | -4.2842 | -48.18764 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a3b933c6-08da-3184-9e36-120e1c056bc8 | -4.00717 | -46.52759 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d513874-1a51-3252-9cc2-9d1d4ae36c84 | -6.25391 | -43.55815 | 2024-11-10 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cee05625-ac42-3b81-88cd-d2229c8f74f0 | -2.63762 | -49.89653 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| be7ca76a-86dc-3752-a256-5414011440ce | -2.84892 | -49.22508 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af51007c-7518-38af-ab1f-877b04e21362 | -2.94806 | -54.68073 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f978686b-9de8-3d38-9556-3dde585ed4e4 | -3.95929 | -48.16563 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0fa181ae-ae67-30ea-bd61-39d0ea56fb4d | -3.85148 | -46.61794 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 196f9677-4f93-3648-b511-7d8019142ea6 | -8.41739 | -44.11895 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04a56298-bbb8-3112-ae8f-fb151118345f | -2.68135 | -51.83101 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0994748f-fad0-3595-b449-378a604bec70 | -4.53071 | -47.88529 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 292025f0-f405-3fe1-b6ce-9c7ab09d9a04 | -3.74265 | -50.17894 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66da5f33-5953-3371-8e4f-b562b3ee5232 | -5.17616 | -47.61148 | 2024-11-10 04:38:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0cb38f3d-437a-3a13-99b9-04dc2997b458 | -3.87021 | -49.94954 | 2024-11-10 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e1b7578c-a547-365a-beb9-43f58ce983e7 | -3.94651 | -48.16007 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 0ccd8fc0-c52b-3dbe-a056-6d72a740eb8f | -4.38301 | -48.57293 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c9d7dd19-8bc6-334a-96c7-c2cfb7435654 | -3.6676 | -54.65779 | 2024-11-10 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b44b8e74-0813-364c-8c63-8fee19421e2e | -2.93983 | -49.52937 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c026f4ae-3011-3aab-9e90-7dff0990f385 | -8.39604 | -44.14754 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ac5edc4-5f29-3d7b-a5f2-bd4cc69ea7f9 | -4.60754 | -48.69618 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52a4c9d9-bb20-3de8-9175-b7447d6fceb7 | -3.59865 | -44.93322 | 2024-11-10 04:38:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a14a87d7-1555-323a-b486-f123569c3b38 | -3.82527 | -49.85558 | 2024-11-10 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96dc96ce-c125-3d94-b7f9-165497486d6e | -2.37615 | -49.8303 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a162b639-279c-3f5a-9dd8-254bae071670 | -2.831 | -49.57748 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a59490e-c692-3be2-a1de-0254b792b512 | -2.8331 | -49.45529 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f43d1ba7-6459-30bd-b258-2b5d43b28032 | -3.35339 | -50.05565 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25d5b78d-eaa4-3b76-a223-10c4ca19b1e8 | -2.4754 | -50.48326 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f876b7fb-ea01-3bd7-951a-bc841a464002 | -2.07977 | -52.04635 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66f232ad-1cdb-35f6-87ac-a8332efb738b | -2.19096 | -53.64553 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b94428f9-b989-3919-964d-02ae6d28ca0a | -3.95728 | -46.98758 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52ec3c07-f780-3b27-aa52-5f102dc25449 | -4.23251 | -48.02212 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5e4b4ba-5a78-3d79-8d57-355f7088ae69 | -4.86682 | -50.53176 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c855cc14-0369-3082-a9aa-08bd0a411538 | -1.76066 | -53.75273 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcac3c7a-91b7-34b6-b464-0d0930aeb874 | -2.34435 | -50.58258 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15dc597c-82b5-374c-8084-b697334162eb | -7.2234 | -44.99471 | 2024-11-10 04:38:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bf3bc93-4afb-3b27-bd10-c3f6113e8b9a | -3.04312 | -50.38007 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb34ca1a-af68-3e9b-91e5-97d2ebe183fc | -3.45336 | -47.66442 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5cf1aff5-814a-3b16-b97f-ad1c3855ee57 | -2.87178 | -49.27505 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8686903-edf3-3827-a29b-3a9f0c8dbcdd | -3.09503 | -50.23075 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac7d87ee-2f0b-35e3-afc1-91ef114f70b9 | -8.40921 | -44.14559 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1204e4b2-1186-32a0-88eb-42f7bc02279f | -3.03292 | -54.2115 | 2024-11-10 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a62d952d-628c-3319-add4-4241605af09e | -2.88735 | -48.2925 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdfbb027-b2a3-3275-a585-ef1219db99de | -3.18255 | -50.57979 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c408f55e-9e5b-3c03-b841-696e0dab2bb8 | -3.25682 | -49.89406 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65802757-29c5-3df9-a3f7-576977807d73 | -3.24731 | -48.75858 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b794b77-4dd2-306b-9d2b-9ad2c778a698 | -3.8703 | -51.97435 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 05410e1a-53ec-3df7-81cf-2284a1239a04 | -4.28699 | -48.19164 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8be0d114-ec30-324d-b252-83db19b79c4b | -3.08492 | -49.59119 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eddaa66d-4a62-313d-a1aa-b3996bf01b05 | -2.65561 | -48.6483 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11860fd9-bf34-3542-ae55-d5853808af57 | -7.42933 | -39.76948 | 2024-11-10 04:38:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f73f8b0b-0fdd-3adc-a777-6210fe756ce2 | -2.66636 | -49.89001 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bffda16c-beff-362d-a3f1-6750ee57a8bc | -2.40857 | -50.30503 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 87c8297b-5d0c-35a5-b959-019fe249f143 | -3.10362 | -45.95951 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 165efe41-ac51-3d96-9918-3c8289ede8f2 | -3.88087 | -49.94757 | 2024-11-10 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b67585dc-df0b-3be7-be5c-4a0725c1dbe9 | -4.2364 | -48.01917 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d3d9281-1a9b-3995-b657-27f52dc7d8d5 | -2.76019 | -49.1429 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b05efb0-1c33-3379-9f57-a2a9ff213eda | -2.9185 | -49.36085 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a43ae4c3-4b07-30e8-92c4-c907a98350cf | -3.12007 | -45.97014 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7aef015-2ca0-3425-a84f-c5559aa71819 | -3.70955 | -53.75078 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f9cddc10-6185-3101-8046-2bf89ad1be33 | -2.88679 | -49.38813 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 960d00b2-7ec2-39ff-a01f-ced3b859b196 | -3.8408 | -44.12484 | 2024-11-10 04:38:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b3489602-dda5-31f4-a6a0-6efcb643d391 | -2.99161 | -49.51939 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2216fff7-cfdb-377d-a186-551fd7e4f6d3 | -3.17232 | -49.1044 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be90a0fb-3946-3c9f-abea-09a80f87041a | -4.10548 | -49.134 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 840db1ea-8840-3323-940f-ad242562993f | -2.21453 | -50.56321 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3dc6f36c-8d20-3d16-b952-8568fe2d7e74 | -4.20078 | -48.39858 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d9e18ba-c754-399b-a441-c6ea3e8ded6c | -3.98253 | -48.14791 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bb86a28-221b-3f54-80f1-7180426f5386 | -4.6423 | -46.02881 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0373ff21-e643-3dec-9e1e-6ea59efbf46d | -3.25503 | -48.75272 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c2913f02-6b6a-36e2-85a7-76765bc067f2 | -4.11943 | -55.04721 | 2024-11-10 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ea39cd45-157c-3136-808e-d8279d82dcf8 | -3.12068 | -45.96618 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8cf9dafa-6356-3844-948f-f13de4664f31 | -3.82357 | -46.50095 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c46d650-6d00-3503-a7ab-1d928062b92b | -4.43148 | -47.26153 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6459f578-0f2c-34ab-ba6f-540f3a6539ae | -3.23875 | -46.53454 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64f7a8fc-d797-3e2a-b197-a5209f3714e7 | -4.10766 | -49.12017 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| b0c8b61d-8f24-3e6e-aed3-a285c4a95fbe | -3.65756 | -50.16199 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2049dff6-14da-3a0b-941b-24d53863fdb5 | -3.47575 | -50.38277 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9d78f5b3-3bdc-30c5-a257-626c8b7db18b | -3.37154 | -57.24416 | 2024-11-10 04:38:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1f2cf6e-8621-37a6-be63-7626ceddd15e | -3.62015 | -47.52033 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49c12af9-8e5f-36c9-bbd2-9f7a13bcb62e | -3.33586 | -50.07864 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README100.md)
