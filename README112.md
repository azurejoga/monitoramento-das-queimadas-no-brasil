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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a34f5aba-0d59-3171-8eed-0267df44e019 | -13.20266 | -47.88922 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77d1a552-cb2d-396b-950d-321841c4db64 | -14.94271 | -46.88171 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 111e2516-b7a5-3a6c-b83d-03eda9d1bca6 | -18.43583 | -43.71597 | 2025-10-03 04:34:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d350288e-a725-377b-b489-42b60deb6271 | -13.75918 | -48.07996 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d69e5d84-1045-3429-8c7f-9840652371ec | -12.63039 | -46.99567 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1aff9cf9-9ba4-3baf-8a20-1a7037c8173c | -16.04352 | -50.92191 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5ff726b6-d85f-3713-baf6-dc49b81b68b9 | -12.8113 | -46.91309 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2cbb2aa6-5526-3afc-b853-7f476e0ca790 | -20.12836 | -44.00835 | 2025-10-03 04:34:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4b974631-9028-3eb1-87cf-063429c0097a | -14.42839 | -46.35292 | 2025-10-03 04:34:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1a676785-a278-33d2-8bf5-6f8f5d723029 | -15.21203 | -47.64921 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e762280b-a39c-39d0-8469-0011a8535a7d | -17.81276 | -52.02856 | 2025-10-03 04:34:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 938a3469-22f2-3b41-9cbc-a32ee8434677 | -14.88171 | -46.85506 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fdc36efe-007e-3b99-9032-ffab9ff4d05a | -13.4753 | -47.23992 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff46a9e9-4525-35cb-b939-4011fb3f76bc | -17.07932 | -44.91695 | 2025-10-03 04:34:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 554f81d4-465e-318d-a270-ae6c84ab2a62 | -12.77802 | -44.91429 | 2025-10-03 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9064c450-1d57-313a-9d20-b28976abe0e0 | -15.66256 | -43.26711 | 2025-10-03 04:34:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cf13ee89-105c-3c42-9b60-aca0f3237e96 | -13.24237 | -47.34882 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 945aa8e2-f4f4-3e3a-88dc-23a3cf68bcf2 | -13.96609 | -48.1134 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6535260-ee12-3196-b133-f8d06fed981a | -13.80337 | -48.06134 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3fd08a3c-e803-35e8-a556-f2afdeb98924 | -13.77438 | -47.58084 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3b6c10ba-2a31-3251-98a4-4dd1db0414ba | -13.33947 | -47.21675 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b27138f-02ee-3a81-8a8d-5b7ccb2e9ab9 | -13.31773 | -47.19733 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ee1fa2d-9292-3ff7-ae10-e805e08f4b3b | -13.97521 | -48.17745 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 300b823e-b38c-3a72-8228-e8fdea45ed2a | -19.50937 | -41.96273 | 2025-10-03 04:34:00 | NOAA-20 | SÃO SEBASTIÃO DO ANTA | MINAS GERAIS | Brasil | 3164472 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 156d8751-efc4-3d7a-9d7e-697cff23b126 | -13.12312 | -47.88076 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a451eb3d-a8ba-332b-8b61-30242d96153b | -14.72276 | -48.0868 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d877415-21a6-3dc8-a077-342bd90c9900 | -19.64851 | -46.80742 | 2025-10-03 04:34:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21aeafe3-90be-3592-bde2-774915cb5b93 | -15.45426 | -45.87918 | 2025-10-03 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e1830ff-9f66-3b4b-8926-b161549c58ba | -13.77494 | -47.5771 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 38016c45-3301-3f2e-a9c4-58e9f4c8f27d | -13.33816 | -48.08543 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26b3bc62-e377-34ff-8155-ac0674ee72b3 | -13.30944 | -47.57987 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 12fe4093-5bf2-3aec-b664-af90992cd74f | -15.65011 | -46.25566 | 2025-10-03 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccfe905a-b965-3aef-b16d-70515b10ae93 | -12.7197 | -48.57979 | 2025-10-03 04:34:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f540ae1b-4b3a-35d4-b8ad-da85c9d7f9d4 | -16.01763 | -50.85406 | 2025-10-03 04:34:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66b62116-57e4-302f-a9e5-7cd85146ee23 | -14.8734 | -48.34146 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b71a98fd-afde-3868-88d2-e85a21dddf05 | -14.86779 | -48.31038 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70d5b533-8d5d-398d-8d84-84515f6ebb25 | -12.63084 | -46.96875 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 37e41c9e-0575-3b68-bb6f-71f31e69bb1d | -13.19929 | -47.88871 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a892460-af7d-3e68-926b-c200963e7587 | -13.68652 | -48.64668 | 2025-10-03 04:34:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f440a090-2b49-3a88-9584-740325595db1 | -13.13486 | -47.89411 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| dad1cc0d-2620-3524-b9f5-01a37ed0426b | -14.0693 | -45.68571 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b3a1536-4f37-3d4c-ba16-17c0b13ceff0 | -14.62504 | -48.22999 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5dc9025d-bcab-3729-99ef-3c3496f69bba | -13.5575 | -47.29839 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 25381993-0c5c-3d34-aa84-52c3e6e03d84 | -13.58774 | -48.18768 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 01d0ef87-4a65-3de7-b739-56fe2ef1a1a4 | -18.15666 | -46.10833 | 2025-10-03 04:34:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fadfa2b-af1b-3f6a-a0b6-6cac772f8363 | -12.63256 | -46.95707 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b252254-b4b0-31fd-82e7-84d0839245df | -19.60069 | -44.63322 | 2025-10-03 04:34:00 | NOAA-20 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc716d7b-28a2-3a4d-b1ee-6909ccad1bed | -18.1548 | -46.11006 | 2025-10-03 04:34:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39f0f686-c32e-3e1e-ae1c-45f9c3feb9cc | -13.75702 | -48.06136 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 421dffcf-63f5-3b32-b856-8c6869c51672 | -16.05511 | -51.04043 | 2025-10-03 04:34:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02136ef2-cab2-3838-a099-1c1c778cc356 | -20.00421 | -44.18445 | 2025-10-03 04:34:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 6f9baadc-3b83-3c72-a3b1-ca8d05d9d06a | -17.35141 | -49.05769 | 2025-10-03 04:34:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c21a80b-a3b0-3b66-b256-ee7da1845e88 | -12.60833 | -46.96236 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 32697d18-b60e-353d-8791-9cfd12d6cb55 | -13.82421 | -48.03772 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71fae653-a565-3fb0-874c-d3441b01478b | -12.67679 | -47.89296 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd779c98-60bc-30b0-bc36-eb29edbd967d | -14.62448 | -48.23375 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99627aaa-d865-3203-9e0f-fec296d9048d | -15.31276 | -46.30003 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a94eb6f-e82a-32c0-96b2-6da05d84291f | -12.90679 | -47.18638 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9b73a47b-5ee0-3cf1-beea-e08d26a4a825 | -13.481 | -47.24902 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0fe5d6f-5538-3917-b809-1ca10728b81e | -14.57722 | -52.4614 | 2025-10-03 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2892b7e4-95b6-36ac-94b7-035520c5a8e0 | -12.63384 | -46.99619 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6118492f-763a-33f3-a023-153e97f3a426 | -15.46264 | -51.56841 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9663b609-2001-3f8b-a1df-16ef50948cb4 | -13.34997 | -48.12081 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81272d9b-d52f-3938-bd7e-5c8d29d75dd1 | -16.35054 | -47.10071 | 2025-10-03 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b205da5-05ee-3484-8442-0f55ddd0286c | -13.68042 | -48.64201 | 2025-10-03 04:34:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3895a2cd-97a1-3be2-9be4-206b81aec25b | -17.58135 | -48.24351 | 2025-10-03 04:34:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1807841a-81f7-372c-9355-a42ae7712d1e | -15.32013 | -46.30082 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d747d0a9-8412-3263-8073-25d243edc74d | -14.65309 | -48.29523 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b6534dea-22b0-38e8-840d-ec5081db4ec6 | -13.34551 | -48.12753 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4b8ba82-f14d-307a-8abe-9b44e32e409c | -19.01726 | -48.48011 | 2025-10-03 04:34:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d97cb26-5edf-36c5-9639-21fd6576df55 | -15.5743 | -46.95392 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f90bf71-93b6-382a-af57-8f173cdcc65d | -13.96732 | -48.16137 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 862138f9-3a24-31e5-932f-31ddf04490cf | -15.33577 | -47.33023 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f039adaf-7570-325f-a71b-4d5bc6796df5 | -15.19387 | -46.40274 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05749435-e864-3c30-b64f-ae42fc14499c | -14.85905 | -49.31594 | 2025-10-03 04:34:00 | NOAA-20 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| c3da3f3d-66d1-3650-8e5f-249b6f32e3c7 | -15.51294 | -45.90435 | 2025-10-03 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99c57843-9452-3318-b949-f547089df758 | -16.35297 | -47.0838 | 2025-10-03 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| eca45f75-f7f9-352f-b1a2-c25ac4328a5f | -15.22329 | -47.18657 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3b858dd-26c6-398d-bb5e-ebe827c1d046 | -14.85685 | -47.2189 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2e94135-633a-3ea6-855a-fc0ffb78df77 | -13.24572 | -47.30266 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec33abfe-e1e8-323a-af89-c0438f0512f4 | -12.53154 | -47.30816 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 395f9812-f3e1-3129-b988-5aa95c19974a | -14.90084 | -48.34227 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 554883a6-03dd-358b-9325-fde861184f55 | -15.30305 | -46.28956 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d0f82ca-d536-39d3-ac1f-0fc4473bca3e | -16.01149 | -48.33993 | 2025-10-03 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d93bd9ce-7d0c-3d0d-baf5-c584876966fa | -14.97519 | -46.85751 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ea59aaa-cad4-39fe-b616-4ee8ab40e1c9 | -14.80825 | -51.42948 | 2025-10-03 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a9d4790f-014e-3cc3-80f3-8a718248f5fc | -13.77835 | -47.57768 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f6493808-eadd-3b78-be49-cf5528fb0483 | -14.90873 | -48.3132 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10c6168b-f40d-3921-bed7-44aefadb9993 | -12.53894 | -47.30547 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b8d29a8-0019-3cdc-9f77-46034e58fc36 | -13.6915 | -48.63655 | 2025-10-03 04:34:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f86c563-db96-303b-971e-3317468c5439 | -13.31002 | -47.57596 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 71414cd2-7a72-34e4-8348-aa1db1a65cd9 | -14.794 | -42.82628 | 2025-10-03 04:34:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4519130b-cb76-354c-b9b1-9678119cdd74 | -12.90564 | -46.91141 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 132afb2b-4bf3-3b54-9a3d-4d4f01eafe8e | -10.89754 | -56.20119 | 2025-10-03 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 87c6ade5-d3d0-31c9-824f-e2683de303fb | -12.37024 | -46.5305 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5ed16ef-69c6-3432-b7a5-11a08a4761b0 | -19.58979 | -45.8998 | 2025-10-03 04:34:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6484577-b1bf-3840-b16d-98a639809870 | -13.22355 | -47.35756 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bf696d32-00cb-31dd-ae93-629d2ba8443a | -12.62627 | -46.9758 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 317a664c-206e-307a-a74c-b5a99c9a7383 | -12.63319 | -46.97671 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 514bc883-8055-36ff-9996-c6c8c8eb3e4a | -15.29513 | -46.29259 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README113.md)
