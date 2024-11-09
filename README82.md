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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5d42fff-24ac-3fba-ba39-a17f3bc8e207 | -2.1836 | -53.73697 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d0287e2-9870-3136-a1a4-53944a6fc587 | -3.98319 | -49.9903 | 2024-11-09 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28e26803-697c-3d9d-836b-df7b036d16ce | -3.78149 | -48.88718 | 2024-11-09 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6da89c27-7409-33b3-8bef-6a55bfd38072 | -2.27695 | -50.67004 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f504056-af8d-3e41-86cf-7f76bec38ae9 | -3.79112 | -51.8223 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aed4ccb1-abbb-34f8-b339-f384c456d596 | -4.18158 | -48.79867 | 2024-11-09 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b634d967-b6ac-3262-801b-de9cace85d42 | -3.21917 | -50.38212 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7efe148d-7686-3df2-bb3e-e81ac4550c6c | -2.37047 | -46.58545 | 2024-11-09 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdb2ed60-48a9-3432-b0bf-81d01902361a | -3.58272 | -50.27315 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4784f8e2-e744-3323-83d3-9eb6d1ea3331 | -2.9533 | -46.75172 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 956298b3-5de8-355e-aba1-2680c2e3c001 | -2.8023 | -49.58624 | 2024-11-09 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 502cc118-e161-376f-8166-bc1cf995d86c | -3.43682 | -51.11682 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1594675b-7f00-3471-8226-ec2adc548fbb | -0.32804 | -51.41699 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bae29db-c43f-3d92-9020-2ca21cf1ba6c | -1.60998 | -51.97655 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab33821c-ccb9-3b09-84ac-a80e55f1ee51 | -2.26043 | -50.4311 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f34f0f0f-0a05-3615-bd1c-4a590c2a3a1e | -2.44882 | -46.31606 | 2024-11-09 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d21a5dd1-d67e-3f37-91f1-a423c8bf3f6e | -3.80872 | -52.02217 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5c9376d-ea79-31b0-bd9d-604ab30a26e6 | -2.77935 | -52.87196 | 2024-11-09 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a00ec27-4091-3cc9-8275-d79733576c18 | -6.23618 | -47.27432 | 2024-11-09 04:55:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8fe2dee-8abd-39f9-b327-9c5191290d9e | -3.34439 | -45.16026 | 2024-11-09 04:55:00 | NPP-375D | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2c45fd4-9263-3fab-9909-1ce2bbae0628 | -4.57356 | -48.01562 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 792b89fc-3f26-3d1a-b171-ebca9d05f369 | -3.04356 | -50.35741 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 747df616-dc94-3f0d-8f40-d1b98725a5cf | -3.97685 | -48.17383 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cee6a7aa-9028-343b-bc14-b12e29496df6 | -2.9519 | -54.45576 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b80e72ba-b2da-3ff9-a50b-70584806175a | -2.89279 | -45.38404 | 2024-11-09 04:55:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff9dcb1c-7222-3ae8-851d-91163d41ab49 | -1.38354 | -60.35706 | 2024-11-09 04:55:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 05736525-c14c-3fe7-b04d-b3480ffad4c4 | -2.30687 | -50.66264 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e69d60a-a149-3400-ab71-623b080bd1a6 | -2.95849 | -54.16518 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7184d61f-d729-33e4-9686-a80d03822caa | -6.26506 | -44.54319 | 2024-11-09 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bfecc834-fbc4-3025-a047-3b266d567f23 | -2.45724 | -49.84079 | 2024-11-09 04:55:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f05831d5-1bc5-3b2c-9b4c-f70a01c30506 | -4.24706 | -47.57188 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| a22275e2-0575-3529-875e-616f350d8ea8 | -6.27656 | -44.54118 | 2024-11-09 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9831eda6-adeb-3ca8-ac57-ba0cbb593861 | -4.84868 | -48.62964 | 2024-11-09 04:55:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72e7816f-9e58-36c2-8411-f643fca10f54 | -3.09251 | -50.21656 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ff764157-8c83-31c8-bc8a-4c3cc8b4ae81 | -4.37932 | -48.58246 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ab3e1329-8467-3f5f-a70a-dbdaa55c9e30 | -1.82941 | -53.72754 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b44ec8f-9159-34cb-a082-69f47a6dc130 | -0.79613 | -51.2385 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c49c60f-fab0-306b-80a5-224e1acc507b | -3.22739 | -53.25299 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1b9f298-73f2-355c-96d0-31ffaad8c8b9 | -3.05271 | -53.99384 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc855fb1-cf64-3116-abe2-8ccaa188c2f8 | -3.72807 | -54.22093 | 2024-11-09 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 0a09b610-a6c9-3b5f-9634-07a58565f713 | -0.36793 | -51.42683 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 671524ee-7376-3012-b8eb-ac756e42ccde | -2.54843 | -53.97586 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 339a109a-9875-34d4-8d99-f4bad2adc7c6 | -3.65149 | -50.13938 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3794cd79-811a-3f97-a8d2-009161d5ca69 | -5.81028 | -44.12313 | 2024-11-09 04:55:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc72ca80-b42f-368d-9329-00298fbd4a13 | -1.17532 | -53.90761 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 082f2b50-8a36-3393-a917-476964eca8a2 | -3.13971 | -51.63448 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6c0a381-8ce3-3f29-bc88-ccc255fbe1ab | -2.43824 | -53.6628 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5770729-b7bd-3d11-9971-b4675681e247 | -2.9537 | -53.91458 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 937458fd-3ac7-3be9-bad8-a90c8995dd98 | -4.25017 | -47.58085 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 5b839b46-4626-33ad-a0c9-9d4707f62cee | -1.08019 | -53.17789 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74eefb87-290c-3886-a13d-86333c717f78 | -2.89195 | -45.3896 | 2024-11-09 04:55:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e28df91-c935-3f57-9b2f-a16445ef4da5 | -3.04587 | -50.36611 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c68d3c8-41fa-38b8-bc72-5e6cce384fbf | -1.24438 | -51.7649 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce0a4a87-6198-3ee7-85a6-d05bae89b345 | -2.8489 | -51.7768 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad3319d9-8ac0-31ce-b70c-6df78b08b7a1 | -2.58297 | -48.21202 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b9b6058-5435-3ce7-87e4-d32e28920186 | -3.25896 | -51.1287 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| db830d90-e94e-3aad-9fa6-8208972fe966 | -2.45952 | -50.40198 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f59e10a-148d-3c9b-a524-edfff42d32b5 | -2.45364 | -50.39286 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20f1d4c4-89a1-3c13-b449-0260fc464e6d | -1.219 | -52.94207 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac335ca9-449e-35aa-ad50-1011972a6db2 | -2.078 | -52.03799 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1ffcef5-0ee9-3b4f-ba74-95bfc08fe967 | -2.15362 | -46.6876 | 2024-11-09 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 796e3c29-f9db-3be9-8ee5-bd4f087731a8 | -2.77104 | -54.04605 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 333ecf7e-8f59-34c7-aaf3-8800985a2edf | -2.63057 | -46.77024 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c619e1cb-40b0-30a0-b626-1fbab525dbe3 | -3.04893 | -51.34109 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d36d6f3e-e5c2-3cfc-98df-dfa2305a1aa6 | -2.13054 | -50.82622 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35ae73f1-c624-3e7e-8667-cb61abe6c4e5 | -3.59063 | -50.27008 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 714780d4-f667-3251-a48c-4fb45e45e364 | -2.18625 | -48.34066 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c322f52-5616-3b04-aed0-e774f04907f8 | -4.61086 | -49.58088 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 470c1a46-efda-332b-80b2-ef6b5b968147 | -3.08344 | -50.56165 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| f13cb9b4-78c4-33a1-a126-16d2b806dc5b | -2.40639 | -48.52454 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 13a64832-84b4-3758-b071-01fb18ad26f9 | -2.24816 | -53.77539 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 56e4551d-8022-34b4-9ce3-78e105286f35 | -2.0808 | -52.04203 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5baaf951-c809-3b69-acb3-a9b49b0a0cab | -5.46998 | -43.65609 | 2024-11-09 04:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 74ecb8b5-059f-3b35-9a47-4011c42db9e2 | -3.05401 | -49.70849 | 2024-11-09 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc9366a8-dba4-3333-8c40-03c9e5ba7bfe | -2.84775 | -49.44196 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 244a79a5-3651-36ce-9963-3331990b2a56 | -2.60512 | -54.02008 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| addc64e5-5ee8-3b61-8f21-60369530c12b | -2.14047 | -50.80815 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27456957-409a-3a08-b75e-4fb8bfc13fb1 | -2.81486 | -54.08486 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35eb810a-acfe-3721-948d-d5030a03f654 | -2.94119 | -49.43541 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e1c5ab8-7fc1-35a3-9eb8-d2678eeb0844 | -4.84657 | -48.64392 | 2024-11-09 04:55:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca6aed20-28c7-38fb-b9b4-65f03aae1038 | -3.09592 | -50.24269 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 975a3b6c-ff43-351a-96a9-d6505ec9548f | -1.15766 | -52.00047 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80760668-5296-3a0c-919d-301812fb861a | -2.96359 | -47.36716 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c114e5f5-512d-361d-891a-4360b471051e | -2.83922 | -52.90248 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 879712f0-8f29-35e5-8a20-5f76144f4a92 | -3.33635 | -50.08297 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 77159631-a9fe-369f-adfd-1abaee2efa3c | -4.36005 | -48.14896 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d10ba20-fbec-3cfb-916d-1cac3e3eab85 | -2.57854 | -54.0234 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b002db72-858d-3bc2-89fa-45b311881cc9 | -2.4119 | -50.30809 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cdf753b-e13d-3ce7-8843-163e8aec02f6 | -4.21058 | -48.54889 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04fcf460-cb10-37b8-83e0-b0f3d868c26c | 0.81447 | -51.88329 | 2024-11-09 04:55:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 246c05c8-cf24-3c32-be71-02056de7fbb0 | -2.44504 | -50.25921 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 459f4178-1143-30a4-90c4-bffb8da55837 | -1.62032 | -52.54213 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aaefe1a1-4a8d-39ca-92c6-edcbc49405bd | -2.21014 | -50.72831 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1f1105d-8b99-3d72-ae43-5c23cb7f2277 | -3.07386 | -50.57645 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c9493ec8-3c3c-3aa3-8e64-b084b66c709c | -2.81197 | -51.80765 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87192d09-df70-3f1a-958c-2af1fe2fb890 | -3.11699 | -51.1086 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ac28123-2908-36bf-a454-826170b11b07 | -2.95724 | -53.71995 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f31a406-ac03-32f8-b1dd-44ee3cd85856 | -0.95686 | -52.30455 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01f0b980-90dd-3915-b8b1-2e7e8536936a | -3.20411 | -51.03893 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b755a928-497d-39db-b116-03dfd9f5105b | -3.26485 | -50.78601 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README83.md)
