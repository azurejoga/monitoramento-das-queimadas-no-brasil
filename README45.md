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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6fad8883-e0e4-37d5-b9f2-2af733a0b9c3 | -2.52454 | -47.07183 | 2024-11-29 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6c73e11-5379-30ff-a164-6fbe3aea45c2 | -1.18903 | -51.77521 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e583f2e-e212-3764-b9f6-2441e80eb34a | -3.44296 | -54.12185 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c2c134a-6dd8-3523-9bc9-443a21c5fc17 | -1.21997 | -51.79834 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d219d48-5c50-30f0-8658-c1452b2c9f4e | -2.83806 | -54.03024 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70e78c67-a0d8-377e-a2bf-d4af35404557 | -2.67378 | -46.14469 | 2024-11-29 04:57:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 70a3f9a3-76c8-3d7d-a7ca-72882928f465 | -0.22984 | -53.13225 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69a6c1d4-2a48-37e5-b187-32f647bf4d63 | -3.73231 | -51.09195 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd0d5db3-bf65-3905-8b07-2cb9825c5d2b | 0.88858 | -50.95757 | 2024-11-29 04:57:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06b35193-8def-32db-99e6-8b6f463da8a7 | -3.22005 | -54.0902 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b15c6c21-a7a8-3bdf-b9f4-2c79da9d2dcc | -1.29193 | -51.72437 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb1b4bb9-c04b-39e9-8243-e0a6a0af1bac | -3.68182 | -50.88005 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d48b32ef-6970-39d6-a889-98a312b3a74d | -3.33743 | -53.20682 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6ab2f1fb-c284-31d2-80dd-a62e257d23df | -3.66462 | -51.03799 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c36c05a-aa59-3ef8-a2be-975f6f288b29 | 0.25147 | -49.86097 | 2024-11-29 04:57:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1542da13-b3cf-39eb-9a1a-e6a7ef554880 | 1.20862 | -55.97917 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 623b968c-1b55-3962-8f53-73882af1099a | -2.45053 | -54.72143 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 725ecde1-9d4e-38ce-9cdb-251f483639d8 | -2.66791 | -53.02811 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3ae2008-fab0-31f3-adc9-78361bde2df4 | -2.98443 | -53.35642 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ff5e969f-5609-32f4-b477-028c524ef673 | -1.04954 | -51.73909 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cb5cebb-51cd-33d5-8843-0f0bf119cfc1 | -3.10684 | -53.81144 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0ac014cc-e57a-3abf-9c2f-a4009c1fa3de | -2.72517 | -48.66897 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7a3413c-1b5d-340f-87f5-428207c5cfc3 | -1.58324 | -52.23914 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee094737-d39e-3201-b1fe-5efd49d526c2 | -2.96511 | -53.71915 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3fe077a3-bf7c-30b0-af05-e28223210106 | -3.04691 | -54.41357 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d897284-dc54-3934-84f9-d7bd1e53c07c | -3.35637 | -52.66756 | 2024-11-29 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e2cc385-b80c-30c1-8c3d-c6b9d31c9ab5 | -2.78447 | -52.8688 | 2024-11-29 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4c8e9c78-2061-33a6-aa77-ed5d44ad6082 | -2.83981 | -46.80458 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 12fa8d44-e7be-3cde-b358-37f6482f9855 | -1.31109 | -51.7347 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7ab2d7e7-4bbc-3c65-a7b0-273d38bbdfcd | -2.98637 | -53.29679 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 94e3610c-af5c-3ca1-877a-72a330340a43 | -2.2401 | -53.63374 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f87f461-86ef-3f23-81b8-007c8b3327ab | -1.62984 | -52.13797 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 332f3506-15d5-3e2d-a4bf-69695f02e058 | -1.93676 | -53.44209 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 640bb789-ecba-3602-9e7a-44aed610dc7f | -1.10709 | -53.57183 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d860bfe0-91d5-3a7a-8eb3-157434917c56 | -1.58514 | -53.84073 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 15ff52f2-b329-3082-a5ca-6a3e6166bd60 | -4.05099 | -46.83333 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a77e72d-37d4-3671-9463-9430efacef85 | -3.16722 | -53.64554 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad4c28d7-4ce1-3028-993d-3f7f43e1bb76 | -3.3333 | -46.70179 | 2024-11-29 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| da15c72c-58ce-3632-bf66-07dbe4750879 | -6.09715 | -43.97071 | 2024-11-29 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b63ca59a-4963-30d5-b4e7-f7824483bd6e | -4.34095 | -47.57507 | 2024-11-29 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 75685a2b-424d-366d-941c-f8d05d3ddd6e | -3.23597 | -53.92361 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d919269-67d2-3b96-82e8-a26c368de2cc | -4.94568 | -46.99376 | 2024-11-29 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 763beafa-a80c-3393-b81b-b28f1544ab17 | -2.8326 | -54.0435 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 131de977-7cf1-3a40-9444-25dca3ec74c8 | -1.07979 | -53.35328 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1eda4d5-3ee7-379f-aeb8-1b7ee5806ab5 | -3.0693 | -47.31754 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 208c8065-da00-3997-933a-550972ea5910 | -1.19856 | -51.75831 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e764eacc-1e27-32b4-bb86-5a9222dd5c6c | -2.9556 | -48.33683 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 833956c1-982d-3a78-acec-9db1e3a27632 | -3.50443 | -53.79345 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ffc5708f-de20-3d82-90a0-89aeddc094f4 | -2.84798 | -54.03177 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fc1fa68b-67b7-3d51-831d-983e72ad0daa | -1.35166 | -55.00548 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 64caedad-41e1-356d-b000-e5a09bdfd25f | -1.53746 | -52.6642 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8d16f15d-7aa8-3eaf-89e7-cb6b54bd56e7 | -1.39233 | -53.63765 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6155ee5-e9d6-3f8e-8cea-d53dc8fea0b4 | -3.70401 | -47.12396 | 2024-11-29 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2d36a1a9-1fe8-367c-8bab-acc3a81236a6 | -2.33875 | -54.37354 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c4edbc9e-cd78-3819-a505-c8fe8d1e7e8a | -4.12589 | -50.50299 | 2024-11-29 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80f7f416-4782-36b9-be43-d3530ca523df | -4.91254 | -44.03373 | 2024-11-29 04:57:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 539a81a8-2c1f-3690-b485-b9c4feef1379 | -4.1914 | -50.68909 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fbc4d150-b476-3630-b8d1-d46c4d5ea5ee | -1.13788 | -53.69962 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93c8c12c-9d66-3043-af1d-cf8b22e2f707 | -3.10523 | -53.82174 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd57b380-8e4d-35a8-9fbb-e7a84067d370 | -1.66163 | -52.7187 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11554624-cf9b-300e-b3c9-4aa2143ba461 | -2.10039 | -50.35115 | 2024-11-29 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 92176040-1a84-3b81-b972-8741c94a6dbe | -2.95388 | -45.72001 | 2024-11-29 04:57:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ebcc914-a83a-3665-8108-0f71fe37c23b | -3.79508 | -46.68657 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5bcef625-42a2-3374-9a2e-62c7e7090594 | 1.85085 | -55.81994 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e8878800-e430-38b0-8ac2-2f1751b53c34 | -2.25035 | -53.45967 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 627201cb-dc7f-3de5-9515-65359382a60e | -2.44168 | -53.67203 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 402e5ecd-5fe9-34bd-a77d-6b37a6c95ccb | 1.21557 | -55.95255 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d921b25f-cc0f-35e5-b584-ddf524f1bb31 | -2.62029 | -54.05229 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd3db3bb-4d2e-3939-93d1-1fe61dd78e11 | -2.60791 | -53.97982 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 753c525e-04fe-37ca-9b90-66d715c0cea6 | -1.13842 | -53.69618 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8693945-1372-384a-a9b7-823963b239c8 | -2.87096 | -46.87553 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| daea4a46-df2e-353d-bc5a-1d080bbb453a | -3.74338 | -49.85229 | 2024-11-29 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a054254-1597-303a-8280-345720b282e3 | -1.20452 | -53.88342 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d42daaa4-a6d6-349a-b283-7b1cb1b77296 | -3.61532 | -50.19032 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9605716b-84d7-39b0-8a08-5b5b71c44934 | -2.84468 | -54.03126 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e2a7f2d0-c858-3d8c-bfcf-e1360fe918b8 | -2.79796 | -48.68684 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77269969-5ee8-372a-9e0f-d5051b8bae62 | -2.74058 | -54.1097 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 787b74d8-c4d8-304e-be85-3a61adac5e76 | 0.98483 | -50.26794 | 2024-11-29 04:57:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b4d72cc9-5cfb-3b33-ba11-bd1ff4d62ff3 | -1.341 | -52.13303 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb985327-e6f6-3208-ad12-9dbdb81cf315 | -1.23233 | -51.80757 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f6221d2a-d47a-31bd-a505-0e4ef0c0ddd1 | -3.56391 | -51.64081 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 71f3543b-d8f5-3362-9a53-0721e3f87fb7 | -1.64598 | -52.10057 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3816b3f-8d77-3a60-b436-ab0cf69330f8 | -4.00109 | -49.96854 | 2024-11-29 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 305cbb34-53c0-330c-8d07-196b36debb2a | -1.09456 | -53.60859 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 720d7d6b-8cfd-3bf1-9046-1d3e50e47e0a | -2.85844 | -54.02986 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3d8ffb0-ef03-3aaa-a0a0-218acffc6956 | -1.32064 | -52.81057 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6f3e6a0-d215-3dd4-9f5f-a48db52d6edf | -0.87419 | -51.72337 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 74889b2f-30ef-36fd-961c-26037b1faca8 | -1.51787 | -52.02652 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71f7ae0d-e2d1-3772-a30f-6128d81f7677 | -1.58435 | -55.24336 | 2024-11-29 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a93dfb73-9a74-37fc-85f0-b898a3cce295 | -1.16808 | -53.67965 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c66de72-3f3a-3d6f-bb36-c38d79fb625f | -1.14214 | -53.80253 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb949b09-ec93-30ae-b95d-28cac6240b0e | -1.14193 | -48.33479 | 2024-11-29 04:57:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec88f024-b55e-3f6e-b9d8-111d481244c3 | -0.29831 | -51.79545 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a4e2825-1cf8-3f3e-ad6a-c4c8d7a28243 | -2.88566 | -46.84013 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 284b5227-1bc4-3af5-bd0d-6330fe446c3f | -2.37436 | -50.40178 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e03160f3-2683-3716-bce1-5ba84664949a | -1.07302 | -52.43606 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a9e3694-5985-3108-b52f-42cc6cb11aac | -2.78551 | -52.99316 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e29a56cc-e4fc-35b9-9f90-98079fb59855 | -2.83843 | -46.81383 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c742c277-4717-39f7-87bb-0b6630a3c6d3 | -1.99995 | -52.0928 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9048b839-4567-35b8-bff5-7c5f058486a1 | -1.46643 | -51.14047 | 2024-11-29 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README46.md)
