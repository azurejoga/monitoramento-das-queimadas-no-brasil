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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51ae2ed2-e748-3019-be83-aaba5c17169c | -9.93727 | -50.23314 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de8dab9d-a696-3f01-87c9-c0b89f207022 | -10.0281 | -50.19463 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 705cb8e0-7738-31a4-ab50-91e61dbf99a8 | -8.91908 | -46.61212 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 30623435-2780-3666-8b5c-46b3352fc3f9 | -6.74473 | -44.59988 | 2025-10-04 05:04:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 399c8b6d-444c-39a4-88ba-e44e4cc9e113 | -6.24858 | -44.23456 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c479be91-1390-3c9e-85ce-58f03958bf13 | -9.92542 | -50.89859 | 2025-10-04 05:04:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d5b02f40-ad4f-3b35-a2dd-f6f47b560bac | -8.84682 | -46.7792 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c0c9fa48-2a00-3de0-bb73-936c42cc1d39 | -8.91444 | -46.60413 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ec9f5a4-7718-3404-8e28-50b808c0a2ad | -5.78185 | -42.91906 | 2025-10-04 05:04:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| e550affb-2be6-3666-b975-0878aef6a9c9 | -4.31969 | -48.09573 | 2025-10-04 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bdfc0a79-2b1e-3ce6-a6f0-fe009f8c5ba0 | -7.8692 | -48.21234 | 2025-10-04 05:04:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ab05b76a-09b0-30aa-b0e2-2d11cc4465dd | -4.45033 | -43.24006 | 2025-10-04 05:04:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| f945b53b-518a-30c6-a320-55e681fb51d0 | -8.81564 | -44.82092 | 2025-10-04 05:04:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d4503db2-32a7-3065-91e8-4e5d5382a86e | -8.87325 | -50.90592 | 2025-10-04 05:04:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63504cbe-3285-35e8-91d5-cd4225a7fb33 | -8.06245 | -44.80389 | 2025-10-04 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c70f1220-31ac-3fb8-9060-1cd0e862599c | -9.35164 | -45.79994 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ede5cbda-61b4-3048-b223-456eb386e827 | -8.22076 | -55.20551 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0810789b-2f27-3b5e-8987-0115852a6733 | -6.10144 | -43.48556 | 2025-10-04 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 934ad4ab-5574-34f2-9f3e-8121751ebb84 | -5.50415 | -49.95162 | 2025-10-04 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43f6b3dc-4e63-34cb-b26d-afde2977680b | -8.62173 | -54.98257 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba20fb8a-e2dd-361d-8fda-ab7a02b9fe3e | -4.44163 | -43.25085 | 2025-10-04 05:04:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 73df634a-d40a-3d11-972a-d0e80fe82fa8 | -10.53849 | -44.51836 | 2025-10-04 05:04:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| df117721-c301-36a3-bf82-8c7424947c31 | -4.64319 | -43.18779 | 2025-10-04 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5d283812-7c43-3922-8fa0-545ce79324ca | -7.04791 | -42.78931 | 2025-10-04 05:04:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| e0b61214-9f48-392f-825e-f74021423d25 | -6.59131 | -44.62281 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 78c468d9-f0d7-36d1-9d30-6938db7049e9 | -6.45966 | -44.57912 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 67a23f89-ed3e-32e2-a6ba-b4f1f54bd519 | -6.73238 | -45.97499 | 2025-10-04 05:04:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 810cfb86-d0e1-31a1-8261-bcbc7df1491b | -4.27562 | -48.87428 | 2025-10-04 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7628b5bc-56e5-3b6e-b5b3-871eed0a17ab | -3.49864 | -50.27214 | 2025-10-04 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87347a52-8a5e-38ac-8a3b-5629cc87d8cc | -8.96397 | -50.69896 | 2025-10-04 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e5f7a2b-f90a-3aa0-8dd4-5186a14e3607 | -6.99019 | -42.7985 | 2025-10-04 05:04:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 515e7f2f-213f-37cc-a927-6349ec5f30ed | -9.45986 | -45.53717 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c46cafe2-461c-3633-b866-171799c070eb | -9.94228 | -50.2294 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6a8a19b6-207b-3bfd-a44a-02728e9910e0 | -6.65851 | -42.81161 | 2025-10-04 05:04:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| b7f74d51-8bd0-3d2c-a9c6-65be2fdb3e0d | -7.77424 | -42.61036 | 2025-10-04 05:04:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 52e63547-79e7-30d3-813e-7b7c56aac470 | -7.70823 | -42.56664 | 2025-10-04 05:04:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 9339897c-4f2b-388b-b56e-af428c4d4edd | -2.92767 | -48.31049 | 2025-10-04 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf84d794-b0bb-390d-92ea-956bef35067c | -5.94211 | -42.89358 | 2025-10-04 05:04:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| fc43ff1e-790c-3c7b-9a31-e9e91c2d4c65 | -7.86507 | -48.20591 | 2025-10-04 05:04:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 75bac0b9-69df-3f45-b3aa-5574cae62636 | -6.25039 | -45.33746 | 2025-10-04 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b3456790-2860-342a-abd8-3c7c91c802a8 | -3.11876 | -59.11745 | 2025-10-04 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8e3482bb-1f4f-3c1c-a3b1-d2778bdb1428 | -2.89542 | -50.72543 | 2025-10-04 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7124087-b5a6-36c5-aea6-0ca7670bdf23 | -8.9147 | -46.60588 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67da5b6c-a469-3572-a8d9-d5c43877d3c4 | -8.62844 | -54.98358 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0437b304-6ca1-32c9-95ce-4dcf7a653c8b | -9.33591 | -45.65357 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc18ce74-6a50-3c07-bee3-7e3f9b948dec | -7.55465 | -42.3931 | 2025-10-04 05:04:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d55a61fe-2495-3a29-8eaf-be6a76b53a3b | -5.1956 | -45.07075 | 2025-10-04 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| b904238b-7b37-33dd-9198-06ff53a504f9 | -7.71562 | -42.57734 | 2025-10-04 05:04:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| fd998937-5a67-310c-8b79-88d0f4f6d1c8 | -6.43889 | -44.45238 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d36d667-e19e-30f9-a888-1728f64ee4f4 | -7.85876 | -48.19789 | 2025-10-04 05:04:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7a8d24c8-dbfd-357f-8679-0d2e6e7812e3 | -6.673 | -44.20871 | 2025-10-04 05:04:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 22859545-2a9a-340e-96ea-d3567c2353c9 | -7.8609 | -48.19966 | 2025-10-04 05:04:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f2365d98-84db-35ed-bfb7-96bb7cac0e1f | -4.44958 | -43.24555 | 2025-10-04 05:04:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 6a7c7271-adf3-3b28-adb0-d6ea1e0c1c3a | -9.92597 | -50.89469 | 2025-10-04 05:04:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7fe9e647-65fa-36d1-849a-5f8759afe568 | -9.33666 | -54.52115 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f83cd89-0b0a-32e1-8450-82ad2c586a18 | -8.61276 | -54.97383 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e00ef23-1dbf-3e62-8959-5f3f052c97ee | -9.93663 | -50.23932 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 268759aa-d93d-349f-a5f9-17fd3b4a0094 | -8.22889 | -46.80867 | 2025-10-04 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1dd1940-4586-3d6b-b525-d7be46294a66 | -7.5467 | -42.39917 | 2025-10-04 05:04:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bc8d23ea-cd81-3b00-9caa-fb577901956e | -6.04782 | -42.52236 | 2025-10-04 05:04:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| b8190b43-bdac-37ba-a3d3-fa3c265d3270 | -6.16676 | -44.61165 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cb17b2f-5e82-37b2-9ba4-ef72bb9a9608 | -8.62056 | -54.96766 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5189ab5-15b3-3438-bd51-d0d1e39e59c1 | -7.46856 | -46.84776 | 2025-10-04 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9a40e9d8-5169-3b49-8f9e-7a94f0a592d7 | -8.62236 | -55.00099 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 85f13386-a59f-3c1a-be22-64675631088a | -4.25477 | -49.07335 | 2025-10-04 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d5b00ca-ae4d-33de-a51e-28b70c6280b2 | -7.74918 | -42.52405 | 2025-10-04 05:04:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| ea0ae51d-93bd-3393-9ac4-b2fb4e96bd2b | -9.33219 | -45.76302 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f9e86ddb-1f97-3bec-93dd-d3d6b645a463 | -9.90603 | -43.73579 | 2025-10-04 05:04:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6e39070f-a82f-382f-8274-a0fa36c164eb | -6.22137 | -55.63994 | 2025-10-04 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8518e29c-befa-39d6-aa90-46864adc0986 | -7.79768 | -55.03801 | 2025-10-04 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b637caaa-64be-3b6b-9660-95a7e1484417 | -8.10924 | -55.08986 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50827eac-7c59-3b09-ae61-a4f200eae2a6 | -6.86939 | -63.13227 | 2025-10-04 05:04:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c606c53a-2cd0-34ad-be0a-64f65416e0ce | -6.36416 | -43.89808 | 2025-10-04 05:04:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| db5334e2-51d9-3158-999e-0af41cded522 | -6.37049 | -43.89939 | 2025-10-04 05:04:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 85c8b6b8-aeeb-3e85-8e90-47ae5d581dfa | -7.87587 | -61.68024 | 2025-10-04 05:04:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cb3c232-02fe-3b9b-9c4f-4f538ac2b4cf | -9.93916 | -50.89252 | 2025-10-04 05:04:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a6c1f47-5d0b-3b09-9229-3be2a68b61c5 | -6.20123 | -44.64065 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 037d449f-3185-31f4-a1ce-9b3b3476cb39 | -2.82862 | -49.19917 | 2025-10-04 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c886e539-6804-34a9-b32a-bb5e397e4df2 | -7.78373 | -42.59158 | 2025-10-04 05:04:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 3fa4f7cb-5751-3437-9097-44f355806727 | -9.32927 | -54.52386 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 689ecfce-914c-35bd-b80c-56419c9fb8a3 | -6.17409 | -43.92374 | 2025-10-04 05:04:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ddd1b121-4ca6-3f7f-9a2d-5840646b4331 | -3.0473 | -51.10172 | 2025-10-04 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08b10b99-e745-37e3-bdac-991270918f3d | -4.51464 | -50.47915 | 2025-10-04 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 381943c0-514a-3d4a-a0a4-9c291b069a55 | -2.96982 | -53.0914 | 2025-10-04 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1db8d848-5151-3ccd-b48e-699bcb9cc93d | -2.92315 | -48.3098 | 2025-10-04 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 335f9413-c069-3b31-b49c-4076bcc04110 | -8.17716 | -44.13628 | 2025-10-04 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b75ccc72-631b-3fd0-9e0b-fc84959f6b4f | -4.62442 | -47.45496 | 2025-10-04 05:04:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2419f01f-d1ae-3708-8076-00c9f2401b64 | -6.22977 | -44.65881 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d60d8da9-b5fb-3e43-a7b4-5a6c28995709 | -6.24422 | -44.21933 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf4d6392-fae9-3241-924b-1a49e59627ac | -6.65128 | -42.80297 | 2025-10-04 05:04:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| bf1323db-b80a-30fe-b280-4eefb87a03ce | -9.11751 | -44.39881 | 2025-10-04 05:04:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9ff24236-a48e-3e59-818c-ff3c43cd277b | -7.04874 | -42.78301 | 2025-10-04 05:04:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3be4454e-a821-3b38-9f71-4a2ae27d02e9 | -7.73855 | -46.31245 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 036179a8-e072-3882-a220-98dc89c5ee34 | -5.61138 | -45.19597 | 2025-10-04 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e730533-0761-3054-a916-f2a7b0bc604c | -7.54176 | -42.40179 | 2025-10-04 05:04:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a19926d9-4d2a-31f6-a020-b8e7d3a05db8 | -4.25254 | -48.56301 | 2025-10-04 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f53d79ef-7219-3555-a52d-2b59a8471864 | -5.69382 | -42.83976 | 2025-10-04 05:04:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 911465e4-9f31-3af1-aa48-7e0a71f27f15 | -8.98888 | -47.48807 | 2025-10-04 05:04:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 742e7f16-c10f-3aa2-8fa5-ab89456c8925 | -8.87483 | -50.89502 | 2025-10-04 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0a2b4aa-3dd9-3134-9e31-3a4b713acfea | -5.83023 | -42.88874 | 2025-10-04 05:04:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |


[Clique aqui para ver as próximas entradas](README101.md)
