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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e721df29-33d6-323d-a474-7b188e873d77 | -2.9582 | -45.7957 | 2024-11-17 00:40:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 211.6 |
| 38f95746-75d8-39c7-9438-eebb22f5b93a | -3.5125 | -50.2343 | 2024-11-17 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| f75c2cad-0631-391a-9790-acab0349ce33 | -3.4436 | -49.115 | 2024-11-17 00:40:00 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| fb5c560e-b105-3d58-99f3-30bd9e6dfc42 | -1.8981 | -46.5808 | 2024-11-17 00:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| e510c505-acbb-395c-b87f-3d746ad17337 | -3.531 | -50.2337 | 2024-11-17 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 0b32f52d-58b3-3e2a-8a45-a9190b7807b6 | -3.4968 | -53.995 | 2024-11-17 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| a31b2a0b-ec6e-3f4d-a5e2-a9ec3e712664 | -8.4339 | -44.1788 | 2024-11-17 00:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| f454222f-9b18-3e9d-8b5a-91e92d54fd73 | -8.4528 | -44.1767 | 2024-11-17 00:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 106.4 |
| f4b64b4c-158f-3ef2-b2c8-0e519230355a | -3.5851 | -50.5255 | 2024-11-17 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| a418591c-bfaf-36d0-9782-d043e31dc659 | -2.8295 | -45.4868 | 2024-11-17 00:40:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 98.1 |
| e79178cc-fca9-3933-aeb8-fcd5689e80f2 | -3.5678 | -50.2534 | 2024-11-17 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 78957f7f-efd4-3dc0-a69d-6e09d160cb12 | -3.5494 | -50.254 | 2024-11-17 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 6e177fe6-1f66-3620-b64b-ddae5666cb7c | 0.6159 | -51.7881 | 2024-11-17 00:40:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 2e7f92e5-865a-333e-905a-53dd5c59bb48 | -2.6231 | -46.0299 | 2024-11-17 00:40:00 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 2d287b26-090d-38d9-938e-cf727ae0face | -4.4681 | -48.1054 | 2024-11-17 00:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 0b18eb96-d48c-3f78-b638-32dd088f174e | -1.9166 | -46.5804 | 2024-11-17 00:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| fb155572-771d-34fe-9569-65b7be2c659a | -2.6595 | -46.2065 | 2024-11-17 00:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 84.1 |
| b337c664-714d-3f9d-9218-8637a878efb9 | -4.5429 | -48.0151 | 2024-11-17 00:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 7c58ed49-e0e4-37b9-a00d-eea2f6d08308 | -2.8614 | -46.7306 | 2024-11-17 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 132.6 |
| 14e65469-cbfa-366e-8651-5a5319fda21b | -12.4004 | -57.5127 | 2024-11-17 00:50:00 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 833b38bc-70d8-3ae2-951a-a0490d586c79 | -3.4968 | -53.995 | 2024-11-17 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 02f0d124-774c-3165-81b7-a70432e58d71 | -2.8615 | -46.7086 | 2024-11-17 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 271bd667-c774-3a46-925b-893a10427e7a | -1.9166 | -46.5804 | 2024-11-17 00:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 136.6 |
| 81ecb400-aff3-391f-abd3-2f384806cf66 | -2.678 | -46.2059 | 2024-11-17 00:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 9dbcb78a-ed4b-3835-b33e-11c99c662a50 | -2.9581 | -45.8181 | 2024-11-17 00:50:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 67d35e77-f771-391a-a668-369b38e51da7 | 0.6159 | -51.7881 | 2024-11-17 00:50:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 81bac185-60ea-3acd-81f0-8a9c5ba92ee0 | -1.8981 | -46.5808 | 2024-11-17 00:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 66aa1a60-7c63-3aac-99b7-f0b751400b4c | -4.58 | -48.0132 | 2024-11-17 00:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 76268d1a-cff9-3982-8887-aa609f6dad80 | -1.8982 | -46.5588 | 2024-11-17 00:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 2ee8820f-e7f3-3be6-b45e-cb52c7a283eb | -2.5987 | -47.5705 | 2024-11-17 00:50:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 41eb1814-ec53-34dd-baff-04f106d2d233 | -2.5988 | -47.5488 | 2024-11-17 00:50:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 5f063d90-a1aa-35d2-9966-87795255b97f | -2.6141 | -54.1575 | 2024-11-17 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 749baaca-b1c7-35d0-84da-b2db032e8c2b | -2.8801 | -46.7079 | 2024-11-17 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| a6d76682-30a1-3093-a718-06dc4d7a2ae2 | -2.8614 | -46.7306 | 2024-11-17 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 5ed65ffc-361a-3b61-8bda-4b0c7ed763ee | -4.5616 | -47.9925 | 2024-11-17 00:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 33519940-81b8-3871-a6f2-5e1eb82360e2 | 0.6159 | -51.7676 | 2024-11-17 00:50:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 7282411c-eaa6-3d84-b88c-fcc2cf5ea3c0 | -8.4336 | -44.2019 | 2024-11-17 00:50:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 078bd6b7-f18e-3bd6-b39e-9386516f91ec | -2.88 | -46.73 | 2024-11-17 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| c661d8a1-c579-319f-81ad-51c3f5be90f4 | -3.7931 | -46.0297 | 2024-11-17 00:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 9ec665bd-7b6c-353c-b540-c8b8290444ce | -2.6595 | -46.2065 | 2024-11-17 00:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 079820f6-b224-3329-8e18-6a2811a5b9e9 | -3.3359 | -52.7643 | 2024-11-17 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 7a448ff4-d427-342d-838c-b5bd879a70a4 | -2.9582 | -45.7957 | 2024-11-17 00:50:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 165.9 |
| c12e3436-86d8-36a3-8da7-7c9e28c0184c | -2.8295 | -45.4868 | 2024-11-17 00:50:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 564c67d0-9c56-3f33-97a9-d59d2e085427 | -4.543 | -47.9934 | 2024-11-17 00:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 3e6b4f65-1b4a-3998-9a50-e7f0c5192c67 | -4.3012 | -48.0917 | 2024-11-17 00:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| db4b7dd8-cc8b-37de-a601-1796c6ca7534 | -2.5802 | -47.571 | 2024-11-17 00:50:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 97723d8d-880e-3819-ac21-2fd2261a0c3b | -4.5799 | -48.0349 | 2024-11-17 00:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 5d856a18-3abb-30d6-a4f7-1197df471d9a | -4.5614 | -48.0141 | 2024-11-17 00:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 5c3742d3-1913-3f8f-8de6-d613e63c3f6e | -8.4528 | -44.1767 | 2024-11-17 00:50:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| a6c454bb-93e0-328b-bdd8-b4260464c02e | -8.4525 | -44.1999 | 2024-11-17 00:50:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 8e2a5068-3190-3802-b0bc-d12edf3f265e | -3.5851 | -50.5255 | 2024-11-17 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| ecc08819-f5ef-3062-b5ba-0a3f6662f759 | -1.9167 | -46.5584 | 2024-11-17 00:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| e866b53c-cba5-3e12-b1b7-d908a373698e | -2.6325 | -54.1571 | 2024-11-17 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| c15be9e4-3848-35fc-8503-6a31df5c3215 | -28.95756 | -49.40441 | 2024-11-17 00:56:00 | TERRA_M-M | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| 50bb66bb-edfe-3d95-b5ac-0ec4c155377f | -28.57855 | -50.15206 | 2024-11-17 00:56:00 | TERRA_M-M | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| d3f0e4fa-fb3e-3fe8-9b85-43153a209420 | -28.96625 | -49.41118 | 2024-11-17 00:56:00 | TERRA_M-M | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| 8cadbdc7-e009-355e-8404-9c7ca5b21e95 | -28.57314 | -50.14397 | 2024-11-17 00:56:00 | TERRA_M-M | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 7dbe2f6e-be38-3145-9227-fe2552384efe | -28.956 | -49.41267 | 2024-11-17 00:56:00 | TERRA_M-M | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 23.0 |
| 7f478f80-c97a-33a7-9d6b-852c4c19fe0f | -27.66113 | -50.65163 | 2024-11-17 00:56:00 | TERRA_M-M | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| c845882f-1fad-3bc2-861b-bd16ffaaf66e | -1.8981 | -46.5808 | 2024-11-17 01:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| b50e3faf-8162-3376-b52c-2b9565e38854 | -3.4784 | -53.9955 | 2024-11-17 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 3f94b8ba-5949-37ba-8bf9-a2f8789ea85a | -2.8614 | -46.7306 | 2024-11-17 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 1e2679a8-085a-3838-b468-126f72c8823a | -2.8294 | -45.5093 | 2024-11-17 01:00:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 324816e2-edc8-3a48-835e-b72007deefae | -2.678 | -46.2059 | 2024-11-17 01:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 583c8c05-316a-3dab-84b7-bfc95ff38239 | -1.8982 | -46.5588 | 2024-11-17 01:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 715995b0-020b-308a-a99f-f48dce65cc2e | -2.8615 | -46.7086 | 2024-11-17 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| d32d289d-50ff-3db1-80e4-45906232d892 | -3.5851 | -50.5255 | 2024-11-17 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| fdeea08f-0c96-3a74-bd67-98b335df3a8b | -4.5614 | -48.0141 | 2024-11-17 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 1d8f20ce-4057-308a-a000-56772511d485 | -8.4336 | -44.2019 | 2024-11-17 01:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 95a1f094-3433-3d6b-b16c-64f23b9221d8 | -2.88 | -46.73 | 2024-11-17 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 3596b783-c7e2-30f1-a177-f0173516bb5a | -8.4525 | -44.1999 | 2024-11-17 01:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 6d2e15c4-914a-3153-a1a0-880ecb885b1b | -4.3012 | -48.0917 | 2024-11-17 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 4c61685b-5be0-30de-9c6c-cebe10eb6931 | -3.7931 | -46.0297 | 2024-11-17 01:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 723318af-a550-3a94-85d3-c6b922550cd8 | -2.8801 | -46.7079 | 2024-11-17 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| e489133c-f52e-3ee7-962b-71d6ffd83b70 | -2.9581 | -45.8181 | 2024-11-17 01:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 85.8 |
| b24e330d-9fd5-374d-86a3-5c4f4cc5496a | -2.5987 | -47.5705 | 2024-11-17 01:00:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| bf3d7e68-db8a-3d21-b40d-4b018caad11d | -4.4103 | -45.5069 | 2024-11-17 01:00:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 379de91f-a24d-3a2b-b7df-fcc045169d7a | -4.5429 | -48.0151 | 2024-11-17 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 9d1b0493-d411-3468-9042-30fd588c4ec9 | 0.6159 | -51.7881 | 2024-11-17 01:00:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 4ed93c5b-a98e-32ab-8a21-dc7eb2cfe25a | -4.4101 | -45.5293 | 2024-11-17 01:00:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 132.3 |
| f69856e1-a49d-3607-8bb7-b70cba0c655a | -3.3359 | -52.7643 | 2024-11-17 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 0bcacb42-4802-3797-ab70-c09049d57611 | -4.58 | -48.0132 | 2024-11-17 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 2c5b82c2-8d28-37d3-bcef-2c3390b31751 | -2.6595 | -46.2065 | 2024-11-17 01:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 1e5d1ffa-1640-38d3-9169-1b7e7cff35e5 | -4.543 | -47.9934 | 2024-11-17 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 5f9a83d6-a78a-30e8-9f83-d5ae80391c12 | -2.5802 | -47.571 | 2024-11-17 01:00:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| c307bf4e-c888-3267-83bc-2736a847106f | -2.6141 | -54.1575 | 2024-11-17 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| e6c355f4-f92c-38d4-9f3f-615c747a06d7 | -1.9166 | -46.5804 | 2024-11-17 01:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 178.2 |
| ff5b68f9-cb31-39e8-ae06-0f962b6edce5 | -3.7745 | -46.0305 | 2024-11-17 01:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 8c2c3de8-1a02-35f0-8ad3-1373d7ee419d | -2.8295 | -45.4868 | 2024-11-17 01:00:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 121.5 |
| b5943290-d99d-32c6-9dcd-5a93b7368223 | -4.5616 | -47.9925 | 2024-11-17 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| a9b9fb3c-91fd-328c-a0fc-0d3880f3027d | -1.9167 | -46.5584 | 2024-11-17 01:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 152.6 |
| d5e457e4-c5ce-3485-9d2e-dae76519fe1e | -2.9582 | -45.7957 | 2024-11-17 01:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 129.8 |
| 55feaa0c-6e82-3311-8a84-3ba82871936e | 0.6159 | -51.7676 | 2024-11-17 01:00:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 73.6 |
| c7baa7d7-82b9-36b7-97a9-d5d9bbb8a4df | -4.5799 | -48.0349 | 2024-11-17 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| d783052c-0870-3525-b351-42d5824a7f42 | -4.4866 | -48.1045 | 2024-11-17 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 9f51ed2d-dff9-3f9a-9b8d-98e170c4b413 | -2.5988 | -47.5488 | 2024-11-17 01:00:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| d869e54f-518a-3c4e-af32-4d6fdbd4a43a | -3.52 | -50.24 | 2024-11-17 01:00:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db09e20a-a2b3-3235-bb4a-4d6906571473 | -1.9 | -46.56 | 2024-11-17 01:00:00 | MSG-03 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e042b15-183d-375a-a424-c1a04c54cde2 | -9.12323 | -44.41467 | 2024-11-17 01:02:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d2a996a2-6601-39f3-ab0f-a23a0976631e | -12.43759 | -43.79823 | 2024-11-17 01:02:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |


[Clique aqui para ver as próximas entradas](README11.md)
