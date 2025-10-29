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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c783d6fb-f50f-38be-83ba-0e75bb828dd5 | -4.12083 | -51.14218 | 2025-10-29 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 269a61c2-3c97-30f2-96aa-66062e4658d2 | -6.13946 | -41.68805 | 2025-10-29 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 31036809-545a-3ee7-ba26-027d95273959 | -6.13753 | -41.71747 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 114d1153-bb07-315a-b682-4be1738c9f92 | -7.34305 | -42.47201 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 23d7ad5f-5b03-32b1-b57e-afd11500b1a8 | -6.48052 | -42.24509 | 2025-10-29 04:44:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 151109c5-58f2-328a-b674-db3c24592cea | -6.20929 | -55.66623 | 2025-10-29 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3cab70a7-7f0a-3562-a4e6-bebd9f7be9f4 | -5.3322 | -45.43031 | 2025-10-29 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 278414d9-aec2-3dce-8e06-9b88c4451dd4 | -8.29392 | -49.31555 | 2025-10-29 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ae695d0-45c7-35bc-ab4e-32937c8d2851 | -3.42695 | -50.11462 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5b22fb0-fe25-33e9-89b3-86105f4e6bad | -7.67056 | -45.94909 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05aa802f-0eaf-3014-b54e-0c45a7629083 | -3.44318 | -50.22626 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d78e3a6b-2145-3ad6-b441-02a30aba5877 | -3.31182 | -46.53611 | 2025-10-29 04:44:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1b154741-97bf-3b2f-a425-8d8c53489014 | -2.19877 | -51.36714 | 2025-10-29 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a83d6c5c-e2e5-3f07-a168-42f82947f06e | -4.47416 | -43.44222 | 2025-10-29 04:44:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| cdf5f59c-cb2a-3518-857c-cc91d6340bf4 | -6.47446 | -42.24138 | 2025-10-29 04:44:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| db7489b3-bb95-3b26-a10e-7daa72964a62 | -4.92237 | -44.01604 | 2025-10-29 04:44:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a6713f7-7404-3519-9f07-8792ce45ca34 | -4.00406 | -49.0341 | 2025-10-29 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08ad6fdb-4a0c-3e97-bcb9-645a54c9c4ad | -8.61882 | -44.80284 | 2025-10-29 04:44:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10d0be16-4db4-39ec-9a11-48329d4b8e73 | -8.6703 | -43.92302 | 2025-10-29 04:44:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4faed8ae-f59b-3d91-8a47-e885484d1fb6 | -2.24078 | -52.00319 | 2025-10-29 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87b71a28-d071-3e01-9fd3-079a63133b2f | -8.03135 | -47.4175 | 2025-10-29 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8331f048-49ed-38a4-8dc0-97847f52cbb3 | -6.1438 | -41.56028 | 2025-10-29 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3c230416-e3f2-3e8b-8ee4-b032460db237 | -6.30097 | -41.88176 | 2025-10-29 04:44:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| de6b0550-82ea-3d3f-bc4a-1aab80ae1c3a | -7.74295 | -44.72229 | 2025-10-29 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d0eb36c-4cf4-3508-9633-f866ec3ff45b | -7.69073 | -46.89428 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e91b1c3-303d-3d0d-9155-74f3acc02bbf | -7.27253 | -46.90193 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 048038ee-9a46-313b-87f3-9eeca4d9dc0c | -3.14882 | -53.14481 | 2025-10-29 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3f9f3ca-0ffa-30da-9955-cc047c195cd1 | -3.98482 | -49.67917 | 2025-10-29 04:44:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5d6864b7-d190-368e-a304-ff50a5719881 | -4.68184 | -50.84129 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bd8f0c1-9631-31d4-97b4-5c0114e0e41f | -5.69977 | -49.30829 | 2025-10-29 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4409e35f-59d2-3595-a140-7112e0a5e34c | -7.08869 | -47.2546 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fb3cb5f-bbe1-3ec3-8c59-0882cf73259c | -7.22644 | -46.722 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54189d3c-4014-3a93-bfd2-9ba48d40f9c5 | -6.139 | -41.69139 | 2025-10-29 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 642f6448-6a45-3148-94ae-d781de14e3b2 | -5.16625 | -46.16432 | 2025-10-29 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee05afaf-36d2-3c84-a12e-57f4684b0121 | -4.20192 | -50.09174 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a164a6e0-7892-3a9b-a219-619d4cd00031 | -5.61589 | -47.1149 | 2025-10-29 04:44:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69bc8b06-47e2-32c2-b507-c1c93b6f299c | 0.4562 | -60.49044 | 2025-10-29 04:44:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08af66cb-36de-3eb5-aaaa-57aa17c93e60 | -3.81455 | -48.65456 | 2025-10-29 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 664e1683-7a9d-3aa9-9c63-b131fc48039b | -4.20024 | -50.08089 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50c3ee22-2206-3e90-87ff-60b6c7565db5 | -6.48973 | -42.24544 | 2025-10-29 04:44:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b48ff494-cb32-30d5-85d0-62c6a1476709 | -5.97673 | -44.02075 | 2025-10-29 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a36d603c-4cf0-3d2f-b6b0-ebb990260fbf | -1.49563 | -53.13106 | 2025-10-29 04:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1f10efe-3927-3a01-bb68-717f00c5a15f | -6.98985 | -46.23335 | 2025-10-29 04:44:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d2b9d230-ad74-3048-ba80-dfd4bb3c1706 | -3.7396 | -49.7042 | 2025-10-29 04:44:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62ef96c4-9bc1-3873-b357-9ea3f85a7b31 | -7.59646 | -46.79874 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b61a8735-5074-3053-a986-47e6bae8078e | -5.59654 | -45.36185 | 2025-10-29 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce0874ea-4ba2-3785-9eae-85d675f6e467 | -6.14178 | -41.68821 | 2025-10-29 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6255d90a-1e52-3452-8e9e-35bb4457d52f | -6.14732 | -41.57408 | 2025-10-29 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9a45d2e8-cffa-30f4-aabb-009f5704e428 | -6.09753 | -42.44213 | 2025-10-29 04:44:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3801f620-3ed2-3f70-9066-4cdbfe454e5b | -6.14685 | -41.57734 | 2025-10-29 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 190b086d-b2fd-305c-9c2d-d30ba6b79e05 | -8.33322 | -46.16073 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cec50266-c117-3012-8e1e-3612051b4dc1 | -4.21623 | -50.08691 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5aeb8180-70bf-38ca-a16a-dcb575114eb3 | -7.49572 | -47.04012 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20d0d591-ddcd-3bfe-a90c-8ff8b37e40d1 | -4.6634 | -46.40501 | 2025-10-29 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d175153e-91f8-3b08-b9f7-6c187137f827 | -8.5617 | -45.70666 | 2025-10-29 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f82365f-19e8-36a2-b900-61ac9afe7bab | -7.12301 | -47.20414 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6194993e-3b79-382e-84c7-98b1c964eca6 | -5.43957 | -46.2886 | 2025-10-29 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 687b55ac-a9ce-3c63-9793-9c3c6fb17218 | -4.66877 | -50.96646 | 2025-10-29 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ca5723d-5c78-393e-9d94-b1c3011d0532 | -3.7099 | -41.5645 | 2025-10-29 04:44:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 68b38dd3-2790-3be4-9d85-d193c38c7f8d | -4.5828 | -50.77945 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aa1a6ea5-c03f-39e9-ba9a-eb1d01dc001d | -7.09143 | -45.24943 | 2025-10-29 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3d9f963-92b5-3c84-9efb-0cc42e04a147 | -3.37475 | -50.14519 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8646708c-80e3-367f-9f9f-358f23a9e55d | -8.5485 | -45.70883 | 2025-10-29 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc8aca18-f79c-3f65-8c03-b3437d7ffc98 | -3.36988 | -50.17611 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af1da0ef-c7f6-3f48-948f-ab96d4621e85 | -4.20346 | -48.35915 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0975c73d-7f86-33a2-9700-1ebe2a7802d9 | -3.82758 | -55.81385 | 2025-10-29 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ac80200-80b9-33f8-9fbe-d6ae2adb930b | -6.79338 | -48.62003 | 2025-10-29 04:44:00 | NOAA-20 | ARAGUANÃ | TOCANTINS | Brasil | 1702158 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 435e8bb5-a137-31e0-8ca4-4a07b3b9c5c1 | -6.97675 | -47.33121 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0acd9a24-521a-3861-a962-65920ae9698b | -7.64551 | -46.9194 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f535104d-d0cf-35ae-8062-41288d0e0f8f | -3.65075 | -49.9239 | 2025-10-29 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40fd9a0c-254d-3df5-b618-cde2ec2a0cd6 | -7.53754 | -47.30315 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f5d961d2-5f4b-39a3-bc29-516f40eda629 | -8.01123 | -46.20533 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edd305ba-a89c-38c5-bd77-7f2697791d98 | -3.04859 | -49.51861 | 2025-10-29 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a49a8e1-fec6-3374-9ea2-02e16f34212b | -8.31701 | -47.86208 | 2025-10-29 04:44:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 495e629f-7605-3fe1-8e38-8c07f7c24d94 | -6.95634 | -47.7414 | 2025-10-29 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4194ed1-f732-330f-b4d5-a6e348ecfc7d | -7.80429 | -46.47656 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c71532d2-c28e-32a7-9684-ddd05a47b113 | -3.30934 | -51.28705 | 2025-10-29 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a09c8bb-f39e-30c8-bac4-85c4fe21c44f | -7.7474 | -44.72294 | 2025-10-29 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a1e39e7-613e-30a3-9f65-0f809b64db36 | -6.10931 | -41.72425 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dc066742-8b43-3130-922a-90a08bc202f1 | -4.29103 | -49.65522 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 58e4902b-1b75-3a82-94a8-bec7bdbbe5a5 | -6.11022 | -41.71784 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 00cc743c-efeb-3535-bba9-36df2b03f29e | -4.0844 | -46.93436 | 2025-10-29 04:44:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e95d26c2-e01a-357f-86c5-e1843e999712 | -3.66094 | -49.81593 | 2025-10-29 04:44:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63d3dceb-4ed6-38ee-88f4-6361323f31b7 | -4.75835 | -46.97732 | 2025-10-29 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ca423ea-f38b-3e1a-8c32-9ade1b19831b | -3.52909 | -51.57477 | 2025-10-29 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e5255bd-b81a-3e6d-b9fa-799b667a65a2 | -6.49574 | -42.24052 | 2025-10-29 04:44:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8b6845be-f244-3688-926d-0d385c8b6e7e | -6.11452 | -42.43225 | 2025-10-29 04:44:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e485292b-5951-3866-a71f-afd9699dd606 | -4.20962 | -50.08588 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 8e3e84e7-aef1-3b1c-ab86-5f5c0c80d3cf | -4.66822 | -50.96991 | 2025-10-29 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4dde5389-b8aa-33db-930e-915c12c9ac7b | -4.72763 | -46.81735 | 2025-10-29 04:44:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46cc7c14-2464-3272-8193-9676794d4bb8 | -5.34146 | -45.1687 | 2025-10-29 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d0281248-b8bb-33e7-887f-f40e404a8924 | -7.26937 | -46.89682 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57c20f9b-e4e5-385c-8c39-663de455c3e6 | -3.1139 | -51.21289 | 2025-10-29 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91fa26f6-6a45-3226-a115-93cdc5d88e1a | -8.21123 | -47.29686 | 2025-10-29 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07aaabf2-e695-31ec-969d-3638b989a1b1 | -5.75579 | -53.40118 | 2025-10-29 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07ebf8d5-4148-359d-ae14-ee5cb60211a3 | -6.91042 | -42.86942 | 2025-10-29 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6bd0f6ce-dead-31df-89de-b8ffbae8920c | -2.93862 | -54.16301 | 2025-10-29 04:44:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83c996eb-3787-3990-a0ee-bcac2f3f7c08 | -5.23783 | -45.13807 | 2025-10-29 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1a6f785-df3a-3712-967b-dd75eb3c37df | -4.21798 | -44.24372 | 2025-10-29 04:44:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 463d0240-ccee-342c-9571-aa48e9476712 | -5.40591 | -45.22087 | 2025-10-29 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README60.md)
