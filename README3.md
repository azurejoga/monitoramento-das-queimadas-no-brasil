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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ae5cd4d-8ecb-35ea-8ce0-dbc09440f1a2 | -4.4148 | -45.954899 | 2024-11-13 00:07:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6978b612-671c-3f10-9a67-020dd848f5ce | -4.401 | -48.849701 | 2024-11-13 00:07:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42823626-4150-379d-8ec6-1f8167c6caf3 | -3.5636 | -53.0229 | 2024-11-13 00:07:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef5b1d0f-849d-3ae2-a278-75a4a29a6e21 | -2.2815 | -47.917301 | 2024-11-13 00:07:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 950dc49d-316d-3ec1-9ef5-41616786e27d | -3.2452 | -43.272701 | 2024-11-13 00:07:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65f8b0f8-f51d-39f4-bb10-9a6b9cd8533c | -2.5998 | -48.2393 | 2024-11-13 00:07:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41a6f101-7021-33c7-be61-1971f679a45a | -2.714 | -45.288601 | 2024-11-13 00:07:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 16dd78e2-d3af-3774-af95-b893a94563cd | -1.8395 | -46.2836 | 2024-11-13 00:07:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a7fd98c-a15e-3ae7-afd7-2b461dda5a88 | -10.0415 | -36.376301 | 2024-11-13 00:07:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 1a5d94f3-a668-382b-9574-6aef39749f09 | -2.0234 | -46.098 | 2024-11-13 00:07:00 | METOP-C | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 12cf43d2-56db-3f51-8b1c-17be22402937 | -3.0577 | -50.328701 | 2024-11-13 00:07:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b16ba776-f205-3eb9-ab2d-9158dc48508a | -3.9377 | -48.184799 | 2024-11-13 00:07:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69e7711f-1a1c-3ba7-964c-2fec651ea204 | -2.5573 | -45.868599 | 2024-11-13 00:07:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 62e37215-eeab-3f4f-a83b-47b379ab705f | -3.255 | -43.2705 | 2024-11-13 00:07:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3388ddc0-d83b-3d92-8487-aaaf08e14a5b | -2.8843 | -46.817001 | 2024-11-13 00:07:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f203d4a-0821-30d6-898a-4983484a41f8 | -15.8644 | -43.790199 | 2024-11-13 00:07:00 | METOP-C | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 820a2f42-5827-3f96-88c8-31d3012d2486 | -2.5268 | -45.597698 | 2024-11-13 00:07:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f4d05bc3-eb99-313d-bc4b-16d75afa953e | -20.630899 | -47.426899 | 2024-11-13 00:07:00 | METOP-C | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e448cdd7-a3ca-3456-98c3-61858ec31d15 | -4.1487 | -48.399601 | 2024-11-13 00:07:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3af1582f-bed7-3bc7-a10b-8d0475960478 | -3.334 | -48.961399 | 2024-11-13 00:07:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f129e8db-48f5-3a4a-ab92-614f2edb2e64 | -3.1662 | -50.450401 | 2024-11-13 00:07:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9b844f4-a58a-32f8-a3c4-241cd4f2502b | -5.4889 | -42.901299 | 2024-11-13 00:07:00 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c51dba3c-e849-33d2-a761-4f41681b4694 | -2.8818 | -46.805901 | 2024-11-13 00:07:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b78906e-2122-33c7-ba96-80e4ac01bf04 | -2.6871 | -49.355701 | 2024-11-13 00:07:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33f9a6a4-52cd-3b85-8965-79c8ccf33754 | -7.8746 | -35.225601 | 2024-11-13 00:07:00 | METOP-C | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| accb8d58-9fe0-34fe-9a7c-97052da697e7 | -5.604 | -44.887001 | 2024-11-13 00:07:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a734a208-c989-32d7-b5af-1e482f329aea | -3.6567 | -50.138699 | 2024-11-13 00:07:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47927ab7-2ccb-379f-bde1-a77155820da7 | -5.0659 | -44.2714 | 2024-11-13 00:07:00 | METOP-C | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aca3dff1-8a88-314d-8b16-241747a572a8 | -3.0383 | -50.332901 | 2024-11-13 00:07:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30e86976-df67-3553-9f70-6d2834579acf | -4.0683 | -44.1339 | 2024-11-13 00:07:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f9faf03-e575-31d7-b174-dfbc19cd4a1f | -4.7113 | -42.787102 | 2024-11-13 00:07:00 | METOP-C | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ca153afb-16e9-3b12-8a2d-ab6d9adc33a6 | -3.5396 | -40.7253 | 2024-11-13 00:07:00 | METOP-C | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1ed0ef32-8a9c-3083-953c-cd2f6696abe1 | -5.2404 | -37.6912 | 2024-11-13 00:07:00 | METOP-C | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 2e2cd554-d39a-37f8-a3f8-3f18a04ba69d | -4.194 | -42.323898 | 2024-11-13 00:07:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 37d4ea08-cf50-3460-a19b-6612e717c305 | -1.4821 | -45.616901 | 2024-11-13 00:07:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2f684601-d782-3a33-8842-daab463602e0 | -3.0339 | -50.313301 | 2024-11-13 00:07:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58ba98f2-9fa8-37dd-8a2f-5388a82db14e | -4.7776 | -45.833 | 2024-11-13 00:07:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1805af97-6d12-3826-ae07-2f0fd2f96563 | -3.6707 | -50.156101 | 2024-11-13 00:07:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 515fe90a-a998-39be-897c-ee92265d8843 | -2.7258 | -45.295502 | 2024-11-13 00:07:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1217fcd7-b0d3-3fdf-9eb8-1b1d34aabdb4 | -4.3617 | -44.112 | 2024-11-13 00:07:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c8619e90-9806-37b7-81ac-3eaf6c33fbb1 | -4.1354 | -43.975399 | 2024-11-13 00:07:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f26c7472-a2b9-345e-978c-d4198a140495 | -4.3599 | -44.103901 | 2024-11-13 00:07:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 087bd666-2943-3610-9ef5-b98c411683da | -5.2332 | -38.676498 | 2024-11-13 00:07:00 | METOP-C | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| cbc3d792-4cf6-3c1b-b06d-87cd1be6f191 | -3.0533 | -50.309101 | 2024-11-13 00:07:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a6d3799-f6c2-3f26-a4bd-3b51a0356bf5 | -3.1606 | -48.3675 | 2024-11-13 00:07:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4607185-a22f-319b-b507-9ae386813617 | -6.818 | -46.780602 | 2024-11-13 00:07:00 | METOP-C | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4aba8087-5ded-3674-a887-3ac3ab9647a4 | -2.7772 | -48.072102 | 2024-11-13 00:07:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1eab9a6c-fa40-3af4-9052-eb6ab0913f3d | -2.3666 | -47.659 | 2024-11-13 00:07:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf31e756-0384-3a00-b361-fef8d3f4fe2b | -17.7752 | -40.1982 | 2024-11-13 00:07:00 | METOP-C | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| af4ccacc-11c1-317d-beb0-e5911546cc56 | -4.3966 | -43.7187 | 2024-11-13 00:07:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f830ec1c-fb81-31d5-86e4-728da9463e5d | -3.3405 | -42.469299 | 2024-11-13 00:07:00 | METOP-C | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9057044-fb70-3e25-bbd9-0e09129a9a46 | -5.3548 | -43.5411 | 2024-11-13 00:07:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c0164d30-4b75-3357-a9ce-efbbae520103 | -3.1565 | -50.452499 | 2024-11-13 00:07:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7224429a-d68d-380e-a966-ef2cfabd6064 | -4.3275 | -50.415901 | 2024-11-13 00:07:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81534170-dcfd-3db7-98f2-3c4235547f73 | -5.4872 | -42.893902 | 2024-11-13 00:07:00 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c7aaa0b2-55a9-3ada-93c9-903ce361a4b2 | -2.872 | -46.808102 | 2024-11-13 00:07:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 999d3951-3b4b-340e-a65c-fb0d9979ee66 | -2.7238 | -45.286499 | 2024-11-13 00:07:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cce1c925-e442-317a-8e1a-1d1944c741e3 | -3.3438 | -48.959301 | 2024-11-13 00:07:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ec2ce5c-83f3-3d2d-bb86-8f8f9d6d970f | -4.3359 | -43.814602 | 2024-11-13 00:07:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7d00e02-217b-3e0d-a9c6-c97c9539265e | -4.124 | -46.8591 | 2024-11-13 00:07:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0e64e665-bd7d-3ba7-929a-ab563be924cf | -8.1202 | -38.616901 | 2024-11-13 00:07:00 | METOP-C | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| b8eff4c0-61dc-3955-ac95-131d2b3962d1 | -18.0142 | -42.6147 | 2024-11-13 00:07:00 | METOP-C | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8e775b3d-e8d3-3e0f-9bb4-ce90372053d1 | -4.671 | -44.573299 | 2024-11-13 00:07:00 | METOP-C | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0703af24-d025-361c-a34f-1db49f2cef9f | -4.1956 | -42.331001 | 2024-11-13 00:07:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7e54b1ba-f666-3916-b651-0663d1536024 | -10.5588 | -36.726601 | 2024-11-13 00:07:00 | METOP-C | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5066bad5-f616-3704-b0be-160d70a0b607 | -3.3403 | -48.943501 | 2024-11-13 00:07:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81a674d3-b454-3279-a027-a61b02fa00b5 | -4.4143 | -48.8638 | 2024-11-13 00:07:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55123282-6d20-3c7f-ae29-13ba3ba9e607 | -3.4137 | -51.061298 | 2024-11-13 00:07:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e253b84-4afd-38ce-944b-94b9cbc4fcee | -2.5366 | -45.595501 | 2024-11-13 00:07:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 898552ef-6331-349d-98dd-0819d17b10e8 | -6.966 | -40.3713 | 2024-11-13 00:07:00 | METOP-C | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 80a010a6-0929-3d4c-b428-8bb4f789ad68 | -5.0492 | -44.472401 | 2024-11-13 00:07:00 | METOP-C | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3e1884a-3d7f-3a8d-8279-52fa6623cad6 | -3.4864 | -50.8391 | 2024-11-13 00:07:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 470ca463-0c15-35f0-9470-8f911276da76 | -3.0621 | -50.348301 | 2024-11-13 00:07:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f94eb15a-1034-3070-83ee-bc728eadc578 | -2.6834 | -49.339199 | 2024-11-13 00:07:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 136ca134-7ce8-3cec-bf84-a85a47edf768 | -2.9869 | -51.0145 | 2024-11-13 00:07:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2af0eab0-c874-3040-a6e9-bd212257b1b4 | -3.3334 | -48.9482 | 2024-11-13 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 0c093938-4684-3465-853c-94c748b64acf | -4.4264 | -48.8609 | 2024-11-13 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 6d9fbf46-3f5e-3837-bdb3-907364cdc1dd | -3.9483 | -48.1724 | 2024-11-13 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 5754e9b2-1a47-38f8-8bcf-90883bcadea2 | -3.1602 | -50.5812 | 2024-11-13 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 2ee97663-7092-3135-b92f-0a63beb5eff6 | -2.7189 | -45.2883 | 2024-11-13 00:10:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 52.0 |
| afad5e35-8d86-3a75-abdf-c58f93de71c0 | -2.7033 | -49.3513 | 2024-11-13 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 9a04d432-9a17-3f76-ab5e-8d33e72760b3 | -3.0505 | -50.3122 | 2024-11-13 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| f2c4ec8f-031d-3866-a9e8-2e04f0f24150 | -2.248 | -53.7426 | 2024-11-13 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 379.8 |
| 082852ce-6aeb-3285-95d5-dc7b9ada125c | -3.3518 | -48.9689 | 2024-11-13 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 73ec4cca-4783-3b17-aaa7-039929d5bf80 | 1.0663 | -60.5985 | 2024-11-13 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 120.7 |
| a6cec3ae-19a8-32c4-8f1e-bb7fe6ceacf7 | -2.7033 | -49.33 | 2024-11-13 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| dac071d9-9d97-3113-adb8-201b8baa72eb | -2.2296 | -53.7429 | 2024-11-13 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 6ea603d3-d032-3165-807a-7cf18d474bf1 | -3.1501 | -53.2371 | 2024-11-13 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 55049818-9a8e-3c38-80b4-2c6154b8dbf7 | -3.5743 | -53.0015 | 2024-11-13 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 9e655c35-f5d3-32f7-9d28-977d9f87ab8b | -3.3519 | -48.9475 | 2024-11-13 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 445c1291-2302-32d5-bdc5-ea149b0f1894 | -2.2112 | -53.7432 | 2024-11-13 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 02bb07d9-5faa-386d-a399-c1465259e520 | -2.2663 | -53.7422 | 2024-11-13 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| ed75f256-cdb8-348f-9327-80cd5b208a0b | -3.1096 | -54.3066 | 2024-11-13 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 60268696-a91f-333d-9ccb-1ab2d0725035 | -3.769 | -50.6863 | 2024-11-13 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| a43d00f0-491f-3e77-bcd9-068fd3b43da4 | -1.6444 | -52.536 | 2024-11-13 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| bb622d71-f4c3-3d6e-87aa-4a46770c29ee | 1.048 | -60.5986 | 2024-11-13 00:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 174.5 |
| e84e37dd-f6a9-3625-8665-bcd900315cd3 | -3.0689 | -50.3326 | 2024-11-13 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 830c4505-bb12-3228-b8bc-d0e09d55e819 | -3.1501 | -53.2574 | 2024-11-13 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 81e3df5b-0169-3259-b72d-02e58dff39fc | -3.1321 | -59.0098 | 2024-11-13 00:10:00 | GOES-16 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 14fe375b-9afd-3ca7-916c-5915fe4b787c | -10.7425 | -49.5244 | 2024-11-13 00:10:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |


[Clique aqui para ver as próximas entradas](README4.md)
