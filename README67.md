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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ae59433-abff-3bca-97ee-111c8ff93352 | -2.76465 | -54.03429 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de65d870-77ae-3bc2-88fc-bc3e6a253ca1 | -4.05894 | -50.60948 | 2024-11-21 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c955175a-bd33-3996-886e-753b4e119387 | -3.3849 | -53.26786 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a547b67-6235-36ed-9930-85a0fa625db2 | -3.39586 | -53.71666 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c8a9ad7-db27-306a-841a-ce94977894bd | -3.54179 | -50.53077 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 63b400b1-b418-332c-acdf-99f1594b679b | -2.6276 | -53.97736 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8616d9b7-79da-3911-b10e-8fa04097cdde | -5.2771 | -45.44797 | 2024-11-21 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46736cf8-a20a-3f6e-be86-269698587daa | -4.00294 | -49.92826 | 2024-11-21 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 210d7d2e-f179-385e-a800-11c6e9d07f60 | -2.78441 | -52.5475 | 2024-11-21 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ecd5ff3-8409-3374-9fc9-17aa1367dcdc | -5.26476 | -49.03513 | 2024-11-21 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4865b719-d1af-39c8-96d4-3f3f739dd7d8 | -4.1001 | -48.48533 | 2024-11-21 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be3fc97a-ba9d-3421-aa51-cdfc26572e13 | -3.68892 | -50.22179 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| ae3f7878-e1ba-308a-b1aa-9a815992ad0e | -3.25056 | -53.58085 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c167acd-2fde-3dd4-ac92-2b9fe546f51e | -4.19215 | -53.49292 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a99c5fd-d59f-3092-bb25-9b65fcc988b3 | -2.36923 | -53.654 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d973190f-86d1-38f7-a237-1e4359552c81 | -2.8811 | -53.96416 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a479b389-8a51-34b1-bffe-a6f82d24b7b3 | -6.06955 | -44.14892 | 2024-11-21 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3eb3e4c8-da0e-3c28-9418-5803095cb4b7 | -3.80758 | -52.36444 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b9e625ea-3cd2-3741-814d-9a5c33e8d2ff | -4.08518 | -54.08606 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83c042bd-a38a-36d3-9e65-0218e85e7050 | -4.1131 | -51.05049 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e17d2acb-d735-3adb-8d98-9c9117647c48 | -3.18817 | -48.57885 | 2024-11-21 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2493d935-b559-3b3f-b6ee-633aeb7f9ec6 | -3.10437 | -53.99182 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ecebc24-2608-32c7-8db3-2548d3b7eaf7 | -3.07915 | -49.21286 | 2024-11-21 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 82ba2d6e-e1c9-3ef2-a40c-699c00c9d3c6 | -6.57336 | -47.87065 | 2024-11-21 04:55:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6eef6901-8926-342b-8ac8-bec7f6376e1d | -2.88169 | -53.98197 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 301d1f4f-f6f2-373c-b6fc-92664027cb45 | -3.10541 | -53.74825 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44ca9fa1-7874-3156-93b5-baa42aa544de | -3.45916 | -50.83539 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4e000bf-b3c5-3cea-880b-6fcb7aa103a6 | -2.74214 | -54.11255 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b681fd3-c56c-313b-8067-19783a0b5a85 | -3.74623 | -53.36635 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4deb771-7dd2-3d7f-a756-5e816d8b8ffa | -3.48402 | -50.31706 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3571f2e2-c891-3e23-a17e-b85c8dd9cc9f | -4.1348 | -47.72949 | 2024-11-21 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9903a21d-490f-38bc-b91d-e83f156fb184 | -3.09829 | -53.98732 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c805386-ad45-3cd1-811e-8b9181c1dd4a | -2.59235 | -51.7182 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac388094-1457-3f51-9fe4-4a64f6cda169 | -2.94684 | -53.72018 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a0329801-3ff5-3895-8916-65bef38b96bc | -3.11961 | -53.70113 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66a3bf79-5f30-37e3-ab6d-92855fd3053f | -4.41315 | -45.95886 | 2024-11-21 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d2a9c45-c61f-3fae-a059-8bd2a7145738 | -3.19808 | -54.32348 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4754ed2a-ec14-3114-87ab-6bfdc82db33f | -3.55073 | -50.17221 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 114a9a36-aa0c-3547-a099-1ad1b12a5e8c | -4.12044 | -53.81989 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57fa0e60-3ed4-3780-8a67-f2dbf3687260 | -2.94785 | -52.5661 | 2024-11-21 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44519578-eaf8-355d-99c1-c8cb3db96e20 | -3.51537 | -53.79908 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2964ba51-93e0-3bd3-994f-90fc8b006fb9 | -3.04474 | -54.41028 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9debce9f-abbe-3de3-86bd-5d3015116773 | -2.76347 | -52.11334 | 2024-11-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| eceb97a3-40e9-3b2d-b512-3a41165c50ff | -2.61758 | -54.27886 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3916b68f-010c-35cc-bb3a-e373d4a7c909 | -3.82806 | -50.29207 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fad4324d-5181-3519-826c-205f22765022 | -4.1265 | -53.82437 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11f669e9-b19e-376e-b908-27708f59e588 | -2.94224 | -49.44558 | 2024-11-21 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b604b34-45b5-3650-8559-b1a870914bdb | -3.22267 | -50.58504 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 936cd9c2-572e-3189-82ae-f9330dec9994 | -2.62127 | -51.80724 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b986b68d-fc39-31d2-9157-74f3be8067ac | -2.42567 | -55.52342 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65d2c9fb-1133-3620-90e0-22221f1991c6 | -3.33536 | -51.16228 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1324575-2536-38be-a143-2ec54cff6861 | -5.71745 | -44.8127 | 2024-11-21 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bef7ec35-4bd5-346a-b5b1-180f7dde357d | -3.19697 | -54.33046 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 95c7cfaa-3f79-3207-a6b8-2011abdd73fc | -4.48967 | -47.10617 | 2024-11-21 04:55:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8971fd0-cf85-325b-9fb8-f40441309696 | -2.75287 | -52.11531 | 2024-11-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f5c7805b-231e-30bd-9e19-be2c7b1c3a80 | -8.3325 | -55.09451 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f1454e1-8e6e-3eb9-a831-dc6f3c0d28a5 | -5.21106 | -47.05197 | 2024-11-21 04:55:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a05fa3bd-9679-3213-811e-70fc1aeb0da6 | -3.28372 | -53.67445 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 237f8538-ed6b-3c02-8391-43615e581e0b | -4.39967 | -47.72578 | 2024-11-21 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bcbfce79-8496-3ffc-a804-92887789af13 | -2.73441 | -54.11846 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2e490af-1adc-3e05-b929-35ab7a1bd887 | -3.51922 | -53.79616 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30bbe1b4-b8e0-399f-bbc8-83e068e33e75 | -3.41792 | -49.22736 | 2024-11-21 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e0cbf19-4083-3f65-aa9a-4c6dd2aea6fa | -5.17388 | -51.99859 | 2024-11-21 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c61ee5f1-3d45-383a-a0b1-cebac018ee3b | -4.63837 | -46.3562 | 2024-11-21 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13c302f2-597e-3333-b338-13918e6c7af5 | -2.36301 | -53.80136 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 760950ce-1145-311c-a16f-72b6b7add617 | -3.25251 | -50.55659 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4213a8a4-a085-32ab-833e-fc5575a8e8ff | -2.59121 | -54.0356 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bdb7eb94-2bb3-3b4e-8143-2f132324ebba | -4.0793 | -49.29382 | 2024-11-21 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1fcdadf-16df-3a6a-93bd-443042d702ea | -2.36861 | -53.83052 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9130c60-50dc-3330-8984-2b7ff3af4268 | -2.54362 | -53.99229 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9fcf578-d2f5-3d7b-9039-91cc13b0b523 | -3.50822 | -53.80148 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3343c781-8097-31ec-a6ee-cb667f09e7d1 | -4.41231 | -45.96452 | 2024-11-21 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6916b532-5188-3d9a-a890-60aa097ce62b | -4.81758 | -45.75523 | 2024-11-21 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 568f1f7f-094c-3feb-9da4-c3473c0863e8 | -6.31416 | -49.68046 | 2024-11-21 04:55:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 647c5493-e6ba-396f-9d4a-1bd4bcb80156 | -5.3003 | -50.56741 | 2024-11-21 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8ba2f22-ae70-30b3-8d94-001c95a1507a | -3.79541 | -50.25801 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa8340c7-f767-330e-a897-ce2c834a97ee | -4.11069 | -54.18211 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22a4b3f9-345b-314e-ac13-42983e6265ac | -4.10959 | -51.04991 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dbc87c94-506c-30a8-bf90-1b4d67571298 | -2.63036 | -51.9259 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8d4b6e4-fcef-34a3-b3fa-071bddb08892 | -3.52144 | -53.80357 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7f07302-68f6-3c42-9e10-c2f8fb44b0c7 | -3.45426 | -53.5392 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3e4bdbb-b6a4-3983-a142-f698974b540e | -3.18653 | -53.25414 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65542adb-aa83-30c6-8be3-ef5a75514992 | -3.66671 | -49.49284 | 2024-11-21 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f88d0093-e696-3cc3-929b-4aa609828e8c | -2.73904 | -54.67048 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0adfe116-4536-3a6e-b500-b1e311cba2ef | -3.28359 | -53.84705 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 07717f3f-2f08-31ed-94c2-475adb4cbd77 | -2.53371 | -54.01211 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bc69bc5-7d91-3dc4-99bc-9b43f157d7b0 | -2.79504 | -54.01453 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4fdd880f-3c33-386d-8864-eaa922268874 | -3.60146 | -51.47538 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc304744-e4e7-39df-be48-2df7112c1e18 | -3.70925 | -53.75531 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12707075-733c-35b8-a18a-5709e1b1f68f | -2.92551 | -53.07596 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0a02edc-8b95-3b39-9dcc-887ff6cd4367 | -3.55372 | -53.53401 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2e462612-7612-3afe-b2a3-ef449678e172 | -2.78015 | -54.04416 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d893303-8f12-3952-ba82-4288844d3c51 | -2.61508 | -51.80261 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3ecf5f9-545a-38ef-a7c1-fe97124a0cb1 | -2.39338 | -53.71814 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4acfdf8-055e-39ee-b540-09e8778dc961 | -4.24959 | -43.81038 | 2024-11-21 04:55:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fef949c0-91a0-38b5-a9d1-f671a7a2f263 | -3.45989 | -52.72418 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a77b96f8-f919-3e8c-b644-d33d83ef7f76 | -3.34694 | -51.64601 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45931372-9411-3167-9d2f-a94d0f0e7b1d | -3.56899 | -54.68363 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ff0d4015-59b2-3372-bacc-71d7790572a4 | -3.10807 | -53.7099 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9afec33c-2ae0-3398-9fc2-3c81564dbe40 | -2.61343 | -54.53785 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README68.md)
