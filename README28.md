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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63d863f1-27f6-317d-8080-6c15b91ec582 | -4.36816 | -47.24495 | 2024-11-05 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21da6fc5-008f-3060-b9cb-9008d1e3b43b | -2.80806 | -51.77805 | 2024-11-05 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 938e8957-9780-3276-935c-cbfbb8bb14bf | -2.93789 | -49.43707 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b964f3d-1bd5-37ce-960d-89f4c7046b75 | -2.78216 | -51.61003 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b6efcb8-177e-37f4-a9dc-7d9eafdd5c06 | -2.07185 | -53.26516 | 2024-11-05 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89ca8b71-4dad-3e60-8ddd-d55c83607105 | -3.04069 | -54.21093 | 2024-11-05 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 22eea215-7dd3-3775-a297-2679e0c81c9c | -4.9578 | -46.78256 | 2024-11-05 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d55b0135-861f-3b50-8d1c-6beefe0cb006 | -3.33228 | -50.27247 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a5e037f-9a13-3f08-bb3b-b0c1c66374df | -3.55881 | -47.39065 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 3359049c-0af0-3687-8b91-e1b175542d66 | -4.91118 | -44.36136 | 2024-11-05 04:55:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a4398ac-0270-356e-a812-4e8b59952363 | -3.85457 | -52.31148 | 2024-11-05 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd4dc01f-b880-35c6-a69a-842ee99d01f8 | -3.557 | -47.3731 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49a8063a-9ad1-3c20-87ed-c68851780159 | -3.55943 | -47.38657 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 0ae0bb1f-7d59-3ba0-88ef-7f8af399efda | -3.86032 | -51.40881 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b3c92fe-147b-31a6-b0d1-2b5b46d9f527 | -3.0472 | -51.07035 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f6a057f-6540-3645-9b5f-a9171d943f42 | -3.09538 | -50.28165 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ee26e34-1350-3bc3-8dd4-e801dfc7b1ff | -3.09305 | -50.27273 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b33f87e1-8255-3f4c-a3b4-99fc5e33b857 | -2.84428 | -51.79757 | 2024-11-05 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c451e070-b1d7-3b52-becf-29a1987f858c | -2.89725 | -48.6025 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 415c3568-2882-3d00-a175-9ddecaca43cf | -2.60883 | -51.3039 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9f0bde2e-c5a7-32db-8ec9-1154ade4404f | -2.60482 | -51.30711 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be537ffc-aa4d-32c4-a310-82b041e4afa4 | -4.4762 | -46.4644 | 2024-11-05 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3c00e0c-3599-3010-975a-ed534ce5a279 | -6.30351 | -42.04288 | 2024-11-05 04:55:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7bac73da-e902-3bea-8f43-c4611907bd99 | -2.8364 | -51.80376 | 2024-11-05 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fba35dbf-e71b-3c61-8f50-9beab6477213 | -4.34772 | -45.5039 | 2024-11-05 04:55:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e25c95c-44d5-3159-b86f-1936b3ee6462 | -2.18279 | -50.3175 | 2024-11-05 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f00d2d7e-3d2f-364e-bb48-86a0ca5f7fcf | -3.5521 | -44.62978 | 2024-11-05 04:55:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6520d19-765e-3cab-acb7-768a84aeefef | -2.16518 | -48.31457 | 2024-11-05 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f5f2846-2f37-3bf9-a96e-fd6c9d53aded | -1.86386 | -50.80304 | 2024-11-05 04:55:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1994e4e-747b-3f7d-a85a-2eebb5eddce2 | -4.79646 | -43.78275 | 2024-11-05 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b791c3cc-c6cc-30ab-a950-46de41d7afd6 | -3.11669 | -51.10459 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d9c1d2f8-077c-3ac0-9013-1764cc4f56f2 | -3.40229 | -50.28203 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bbd60834-b165-3977-b493-6713c92c4756 | -2.84119 | -49.48487 | 2024-11-05 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ea96164-dba4-3998-9e29-5c043ee6d92c | -4.59562 | -49.52407 | 2024-11-05 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0aa1b511-213e-3de2-a18e-02f9a90f20de | -4.62574 | -45.70286 | 2024-11-05 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aa4a198c-3094-3af3-aaa0-f540e093a53a | -3.03292 | -53.26853 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 75670b91-329d-3713-b555-c15ebf6c0a3a | -2.64544 | -46.76451 | 2024-11-05 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cfcd2662-f319-3997-ad27-ff17b26474e3 | -5.97598 | -45.36694 | 2024-11-05 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 626d12db-0c44-38d3-9b5b-4439a10f8e17 | -2.71011 | -52.96392 | 2024-11-05 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 021f26c8-88bc-3d78-819d-6b90ed1d2697 | -2.1303 | -50.2554 | 2024-11-05 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0940a6d9-edf9-3a37-bcb0-c740129449c0 | -6.5198 | -45.93151 | 2024-11-05 04:55:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eccd88f8-fe35-3945-b7e2-5aaf2b8ba393 | -2.65491 | -48.56941 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 9be8cbec-ec9b-35ed-af95-7676b8c5cd04 | -3.54141 | -47.38786 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9392c0a9-3758-353f-ac08-82d6ea6f6147 | -4.91194 | -44.36198 | 2024-11-05 04:55:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47492172-2698-39bc-9023-9089baa22ab0 | -3.23977 | -50.16928 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5974dbc-d8da-3d03-9304-c2cae1138650 | -4.26862 | -50.72496 | 2024-11-05 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 217e13ef-caa8-32ec-b25d-9ae49fa6e53c | -5.22356 | -47.47021 | 2024-11-05 04:55:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ede42dd1-9dc4-3d34-bf04-8264a835398e | -5.30035 | -46.24622 | 2024-11-05 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4a4057f-6381-3fb1-8531-adee3d8c6b7a | -4.88792 | -46.70706 | 2024-11-05 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c3c7ea8-3088-30f0-9264-c7bb5af5805f | -5.06424 | -44.23778 | 2024-11-05 04:55:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9bfb68ad-f391-3175-9268-c24150e68314 | -2.79417 | -51.4421 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bafee12d-d19c-32ba-a797-339eda771fdb | -3.95718 | -45.83469 | 2024-11-05 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80ce3a7d-3462-39d4-be10-ba7635413995 | -2.6475 | -48.56479 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6ad34c1d-8000-33b0-8582-21a810e8173c | -4.91243 | -44.35844 | 2024-11-05 04:55:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1122aea8-3931-3e84-b836-08a3f4da48b6 | -6.11092 | -43.95901 | 2024-11-05 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| aa440264-2e52-3e90-967a-fdf937eaf81e | -2.23876 | -50.41994 | 2024-11-05 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 820e1f6d-0a81-348b-a24b-79d8c17c4c29 | -4.55973 | -45.80239 | 2024-11-05 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d146fe2f-6c2c-3dd6-84f0-4c77e976297f | -4.89977 | -46.72416 | 2024-11-05 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6997eddf-b4d7-375e-8f35-75096c4bd9ae | -3.5408 | -47.39189 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a9298c3-539c-33cf-acb5-8381e6578fdd | -2.6616 | -46.74861 | 2024-11-05 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 842e431e-e3f2-3fac-a0a1-c38d8af73697 | -4.89116 | -46.71776 | 2024-11-05 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d224bfb1-92e7-3229-8125-99a150fd7e94 | -3.3464 | -50.25311 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79c5471a-9960-33ba-8d46-4f044c8bd6aa | -2.61611 | -51.72643 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 83d7c1c8-071f-36ec-85f4-25091615ae35 | -3.10559 | -50.28745 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 615c0225-3d45-3012-9b58-ca4bbb49a787 | -5.44445 | -43.26075 | 2024-11-05 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e1b4318-7e63-3dc1-bac8-b5477b9ad921 | -2.89743 | -49.39796 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c19874a3-be0c-340e-ae19-25778dd4cfc4 | -3.04391 | -53.2632 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79ca8304-9b56-3a16-aaf9-f31428aa8026 | -2.71065 | -52.96049 | 2024-11-05 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffe9b41d-d163-36a6-93f6-b15e3f8800c8 | -5.30373 | -46.25719 | 2024-11-05 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ad572f6-dd27-3861-869a-bbda5d60591f | -4.88324 | -46.70644 | 2024-11-05 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0fa8fd2-9098-3e72-962e-cf2adcdbab08 | -3.73587 | -44.54439 | 2024-11-05 04:55:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| baf5d637-4ac7-38e9-aaec-a82d2b831952 | -4.26147 | -50.72383 | 2024-11-05 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd68d587-e37f-337c-baf6-5e95fb2822a7 | -3.40293 | -50.27782 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7328e6b2-be7f-3d5a-bf63-ca681f28dce7 | -2.67195 | -48.51245 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad9bc6fa-0583-33ef-83f9-b44bcf1651f0 | -2.94969 | -54.67789 | 2024-11-05 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4af0f8e0-d089-3c85-9985-09f8d6c76158 | -3.25407 | -53.07018 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 559a9cf6-a0e2-3059-87d9-c13bf56774ed | -3.21506 | -53.10296 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 43264a4a-ccc6-3c6d-bc37-e8b29a3947ae | -3.09667 | -50.27328 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f7359ab-dd57-394b-92d7-ee873bb46a34 | -4.91691 | -44.36641 | 2024-11-05 04:55:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8638b0c-d15e-360b-92e5-9251b5a6d4ef | -5.51564 | -48.08436 | 2024-11-05 04:55:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4b7cb49-1ed0-3b80-ae6e-4a408b5f668d | -3.03568 | -53.27248 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ae12d44-1e96-30ee-be55-fdc9332554d8 | -3.03845 | -53.27642 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5f4fbb2-8c71-3b07-9ddd-401abcc5f32a | -3.5489 | -47.39727 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ef488961-1668-33be-8d0b-014a1c6fb360 | -3.79953 | -51.9428 | 2024-11-05 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2af90db2-11c5-30af-90cc-416fdbf9d5d9 | -2.65889 | -48.57001 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c69ec037-b30d-32c3-959e-af5b889d5658 | -4.91666 | -44.36219 | 2024-11-05 04:55:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3834335-537f-3b3e-8c19-5ec1b81276b5 | -2.8808 | -51.31433 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b20ba887-63f0-3cb9-a52b-70f5bb810aa5 | -4.78475 | -48.909 | 2024-11-05 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d3d7b9d-dcbd-38e1-9754-381bf82fd451 | -2.65094 | -48.56881 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| d9de5d00-3569-37bf-ac07-cf8d2fe5856c | -2.83937 | -48.4594 | 2024-11-05 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7840636-aabf-3ea6-be05-529aea80430a | -3.95608 | -46.37226 | 2024-11-05 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72400390-5eb6-356a-ae7b-daa177a69619 | -3.95971 | -53.89957 | 2024-11-05 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e767f07-97bb-32c1-8bb2-17c660aabdae | -4.2052 | -50.63558 | 2024-11-05 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b7e8d20-1a49-3e99-b395-9b3f2b1a051a | -2.16369 | -50.50655 | 2024-11-05 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d6f5fed-ff9f-3889-b331-70857ea23ec9 | -2.85248 | -49.48661 | 2024-11-05 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 105c8e00-5e70-3a95-a2f5-888a670f7b25 | -3.48 | -50.38644 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e97684fc-f457-344e-9d3d-a0de89e56b40 | -2.92379 | -48.31334 | 2024-11-05 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96c62d97-89c2-31af-8836-69e20d397b4b | -4.53884 | -46.57298 | 2024-11-05 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 549796bc-864a-333b-a9c6-9fdee027aada | -3.04613 | -53.27058 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e940178-3ecd-3eb8-bf9c-561dd922ce88 | -2.8075 | -51.78166 | 2024-11-05 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README29.md)
