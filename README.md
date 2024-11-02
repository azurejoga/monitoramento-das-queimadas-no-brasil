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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0418af80-fc7b-3036-8775-fd1d56eacb71 | -4.55 | -43.1 | 2024-11-02 00:05:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 296b859e-7f96-39fa-8fea-b2a02b4a95d6 | -3.25 | -53.4 | 2024-11-02 00:05:08 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0387c1b-2bc8-3062-b0b7-de3cccdadb43 | -3.21 | -44.43 | 2024-11-02 00:05:08 | MSG-03 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4ee133ab-3126-3794-9d6b-ba05402cec42 | -1.1834 | -53.6771 | 2024-11-02 00:05:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 130f841f-afa7-3640-b685-782e6c3d23de | -1.5531 | -52.2101 | 2024-11-02 00:05:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 38be2b0a-7f47-34c3-b90e-434b837cb63d | -1.5531 | -52.1896 | 2024-11-02 00:05:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| e7369b60-04d9-3398-ad76-e2c338079e90 | -1.5714 | -52.2098 | 2024-11-02 00:05:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| f2786050-4ef5-3907-8ef1-6c18ed04928c | -1.5715 | -52.1894 | 2024-11-02 00:05:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 78392c9d-86fe-3f89-bc31-defe898362e2 | -1.5899 | -52.1481 | 2024-11-02 00:05:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 4c79d656-7624-3a34-be0a-e7b2a6c09cd4 | -2.053 | -59.3906 | 2024-11-02 00:05:18 | GOES-16 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 291c5da4-ddf6-341b-a4c4-b270643177e6 | -2.1746 | -53.6834 | 2024-11-02 00:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 38dec73d-0b7f-37d7-8b28-3cabf45a1023 | -2.2663 | -53.7422 | 2024-11-02 00:05:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 125.4 |
| cb05ebfe-727a-3edc-85ef-93cff451017c | -2.2847 | -53.7419 | 2024-11-02 00:05:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| b020d7fd-f6d2-3181-b291-5828bba57097 | -2.3245 | -46.5262 | 2024-11-02 00:05:19 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| b4747afe-c986-3cd2-9652-56d959de6108 | -2.6759 | -46.7585 | 2024-11-02 00:05:21 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 1aa8dbc6-066f-3269-9b56-cd997ae9bb6e | -2.6944 | -46.758 | 2024-11-02 00:05:21 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| f98101e2-7c6a-3984-9a43-1ae4feb6a9aa | -2.8056 | -51.7539 | 2024-11-02 00:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| fd1b4a12-dbf6-35b6-972c-f36018dcf4d9 | -2.8386 | -52.8794 | 2024-11-02 00:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| f0ba7dba-3665-3ba8-8022-55dcc1aa0776 | -2.8509 | -49.3895 | 2024-11-02 00:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 68e5684f-e0e7-3e0b-9d19-39cb3ee4f36d | -2.8808 | -51.3179 | 2024-11-02 00:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 630ba893-6170-3706-90fb-23e96a5579b3 | -3.0088 | -51.5834 | 2024-11-02 00:05:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| fabd7d4b-ab7f-3623-b303-95ab0d893a04 | -3.055 | -54.1675 | 2024-11-02 00:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 4104692c-27cd-3418-aa3c-3e346cc1f7b3 | -3.0734 | -54.167 | 2024-11-02 00:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| ddd084f7-3064-3fb1-90c4-ee5f240ddb37 | -3.1027 | -51.1249 | 2024-11-02 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| a0170e8c-b3ba-31ce-b1ba-0240eb86ba80 | -3.1097 | -54.2865 | 2024-11-02 00:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 563168c7-f4bd-3829-9b89-f924a90db434 | -3.1098 | -54.2665 | 2024-11-02 00:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 625a5268-3869-31b2-89fb-9e105f06c87e | -3.1281 | -54.266 | 2024-11-02 00:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| e6ab2580-afa4-3222-8499-4c1b45d3cc0e | -3.1282 | -54.2459 | 2024-11-02 00:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| c74add09-82ac-3084-b05f-8b78634f3ff8 | -3.1767 | -51.0812 | 2024-11-02 00:05:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 359140ab-547e-3914-8e20-003da5c24373 | -3.2063 | -44.4317 | 2024-11-02 00:05:24 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 7bbe872e-a5a7-3c31-85eb-7996652152b6 | -3.2064 | -44.4089 | 2024-11-02 00:05:24 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 6be22776-dbda-3a51-b054-8cc5baac2ae2 | -3.2249 | -44.431 | 2024-11-02 00:05:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 234.4 |
| 9d3d1286-9fcc-3824-acd8-ef3bff817722 | -3.225 | -44.4081 | 2024-11-02 00:05:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 265.5 |
| 1007860b-9aba-328b-a30d-a8a33d33bdb4 | -3.2719 | -50.3473 | 2024-11-02 00:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 5b0d5c60-bbda-3ee8-b4a7-ce437190cf39 | -3.3461 | -50.2609 | 2024-11-02 00:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 8b039339-f174-30cd-a8e6-da578d9527e8 | -3.3462 | -50.2399 | 2024-11-02 00:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 2648b843-c782-38f6-b1b7-e5da36b60923 | -3.3673 | -45.7131 | 2024-11-02 00:05:25 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 3020c3f2-a625-3b5b-9efa-fca5d1b70bc5 | -3.3646 | -50.2603 | 2024-11-02 00:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| ccbcb6f9-2e5c-35b4-9332-2191c841ed21 | -3.4198 | -50.3005 | 2024-11-02 00:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 51ae279b-aa45-3893-9a05-1bb0ee1ca9fa | -3.4199 | -50.2795 | 2024-11-02 00:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| db102343-ba94-30cf-a16c-fff1b50988ef | -3.7701 | -43.5554 | 2024-11-02 00:05:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 132.4 |
| bfd32906-690a-3c85-8373-b3e6fc74ed4f | -3.7703 | -43.5323 | 2024-11-02 00:05:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 289f844b-7b33-3ca0-ae44-3c86f155bfb9 | -3.7372 | -46.0545 | 2024-11-02 00:05:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 2ad67023-d756-3269-bd62-7d404e53bdf8 | -3.8144 | -48.9729 | 2024-11-02 00:05:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| aa16267c-ea6e-350d-8bed-97c686f5d5e0 | -3.9473 | -48.3666 | 2024-11-02 00:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 653679e6-d5d7-380c-b36a-a3f42135f88f | -3.9474 | -48.3451 | 2024-11-02 00:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| e417c749-5fde-3aeb-b273-40dcd6ed9e08 | -4.2213 | -45.9423 | 2024-11-02 00:05:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 87a235ac-b380-3336-8bf1-e05f9d17e50f | -4.3867 | -43.4757 | 2024-11-02 00:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 26cd7685-1036-3ad0-a754-94c795edcc83 | -4.4054 | -43.4746 | 2024-11-02 00:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 3b431814-9c6a-354a-9773-4f467fde3cae | -4.3537 | -48.6068 | 2024-11-02 00:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| efc520e5-8b1b-363e-a42f-a6bc507c6102 | -4.4094 | -45.6416 | 2024-11-02 00:05:31 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 329b1fae-8434-356b-80c6-254164b20f71 | -4.5575 | -43.1162 | 2024-11-02 00:05:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 160.8 |
| a6731db5-e21a-3f65-a0c2-352fd0f174a1 | -4.5577 | -43.0928 | 2024-11-02 00:05:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 277.2 |
| 411be4bb-fbcc-3b2a-b415-0dde6603a3b1 | -4.5764 | -43.0916 | 2024-11-02 00:05:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 558030a2-daf1-3def-bbd2-3fe621509fda | -4.6072 | -43.9945 | 2024-11-02 00:05:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| c5ae8903-d17d-3f25-b86f-14c3b405f361 | -4.665 | -46.3862 | 2024-11-02 00:05:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 84.3 |
| d6faebe3-b196-3048-9a7f-08019916caa0 | -4.6837 | -46.3852 | 2024-11-02 00:05:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 147.4 |
| 92d4f004-b582-336d-ba2b-4f1e457ab898 | -4.6838 | -46.363 | 2024-11-02 00:05:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 16d528da-aff6-3f9b-80ea-55960acd2e16 | -5.1146 | -46.0264 | 2024-11-02 00:05:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 86.0 |
| a31de66f-9006-31d6-bb00-db91e0aa577b | -5.1882 | -46.1557 | 2024-11-02 00:05:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 29bb356f-bb1a-359e-8a45-3c8ea4a4585d | -5.3065 | -43.0663 | 2024-11-02 00:05:36 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 84ab201a-2a04-3eab-bdc8-4c2d910a6cd2 | -5.3252 | -43.065 | 2024-11-02 00:05:36 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 8cc10dd4-8e55-3019-ae73-d40511c5b4ba | -5.3266 | -45.1589 | 2024-11-02 00:05:36 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 3a806f6a-fbe6-33fe-97ee-8f5752d8c747 | -6.5631 | -51.1126 | 2024-11-02 00:05:43 | GOES-16 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 84945620-26f0-3da8-b95f-f984f3014c69 | -1.4532 | -46.7217 | 2024-11-02 00:15:14 | GOES-16 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| e0b1aeb9-e66b-3901-9b4c-027293bbe40a | -1.5531 | -52.2101 | 2024-11-02 00:15:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 87829915-02e6-3ee7-83af-32481b830b6f | -1.5531 | -52.1896 | 2024-11-02 00:15:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| afbe610b-005d-3bb4-b794-9bfd59b138c4 | -1.5899 | -52.1481 | 2024-11-02 00:15:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 945fffaa-a9a1-39fc-8fbe-ea4f59a931ce | -1.8604 | -54.6911 | 2024-11-02 00:15:17 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| c3a1161b-15f7-301b-ad2b-5aa43203ec35 | -2.2663 | -53.7422 | 2024-11-02 00:15:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| c5d75d26-ccc3-30e8-b932-6075d7199299 | -2.2847 | -53.7419 | 2024-11-02 00:15:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 9ddfcfe9-9c8d-3bd1-983c-bef829c03e0e | -2.6399 | -51.7168 | 2024-11-02 00:15:21 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| aca2900c-3438-359c-9c33-ecca8a77ee95 | -2.6759 | -46.7585 | 2024-11-02 00:15:21 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 2efca1e5-200b-33ee-a987-33f366a458aa | -2.676 | -46.7365 | 2024-11-02 00:15:21 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 4114447d-ecd2-3be0-bbd3-4fae9974f8e5 | -2.8061 | -51.6095 | 2024-11-02 00:15:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| da373576-0e58-3890-adfc-7709ceba4e52 | -2.78 | -48.5806 | 2024-11-02 00:15:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 8dfe75d9-c102-3b0c-bec4-20e91fe81b52 | -2.8056 | -51.7539 | 2024-11-02 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| d708700c-e50c-34ff-a53e-eb31a053c7c3 | -2.8386 | -52.8794 | 2024-11-02 00:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| fca3ad76-5026-3e2c-be81-590d60252e2a | -2.8509 | -49.3895 | 2024-11-02 00:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 6f6cb954-937f-3693-9cf5-76159a2069d1 | -2.8555 | -53.3459 | 2024-11-02 00:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 44e6e403-7c28-383f-8df1-206abdb0ecf7 | -2.8808 | -51.3179 | 2024-11-02 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| b1791fca-d4af-3389-8acf-54bfbec70dff | -2.8809 | -51.2972 | 2024-11-02 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 572846ac-430d-39b7-98ab-c1f6bc1aa33b | -3.055 | -54.1675 | 2024-11-02 00:15:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 320d750b-eb43-3014-8cc1-91a5e011ca05 | -3.0734 | -54.167 | 2024-11-02 00:15:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| ac5da1c0-d0fc-3ae5-9ef5-2c366fa2d76e | -3.0088 | -51.5834 | 2024-11-02 00:15:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 64cc2ca4-c848-31bb-8047-2d9595419cc0 | -3.2063 | -44.4317 | 2024-11-02 00:15:24 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 78e2313c-9412-3db5-938e-7c6d1a44dc06 | -3.2064 | -44.4089 | 2024-11-02 00:15:24 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 021a9667-74e2-3a57-bf21-abc4dc3e49e9 | -3.2249 | -44.431 | 2024-11-02 00:15:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 131.6 |
| ad04efde-be8e-300b-9e5e-554d2f592d82 | -3.225 | -44.4081 | 2024-11-02 00:15:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 179.6 |
| c4a39131-7a0d-3be3-98b7-a788aa3b0b85 | -3.1027 | -51.1249 | 2024-11-02 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| ee74951c-a8c5-38f9-b476-71aa38215d59 | -3.1097 | -54.2865 | 2024-11-02 00:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 0f48aaf0-4e7b-3ef3-a00f-c511e31a2b3e | -3.1098 | -54.2665 | 2024-11-02 00:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 3bb5036e-c401-3e7f-b776-41cc964d57b4 | -3.1282 | -54.2459 | 2024-11-02 00:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| e2507aec-40ef-3a6c-85c1-40bb0c990bc0 | -3.1281 | -54.266 | 2024-11-02 00:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 7caa43cb-3a06-3dcb-9648-13b938c2f1f4 | -3.1767 | -51.0812 | 2024-11-02 00:15:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| e947dbd3-670d-349a-ac20-dd2be5e93a60 | -3.2719 | -50.3473 | 2024-11-02 00:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| acfd0082-373f-36ba-99c4-e7ea147c6830 | -3.3461 | -50.2609 | 2024-11-02 00:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 24374c64-62d4-3d87-9724-816bcd18b7a9 | -3.3462 | -50.2399 | 2024-11-02 00:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| d08c0b2a-1b5a-358a-a9a3-563c7aca5618 | -3.4199 | -50.2795 | 2024-11-02 00:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 2071d016-6e1f-328e-b427-0d2f33a50646 | -3.7701 | -43.5554 | 2024-11-02 00:15:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 127.2 |


[Clique aqui para ver as próximas entradas](README2.md)
