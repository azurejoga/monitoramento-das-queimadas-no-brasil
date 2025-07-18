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
| 0be4cb46-1217-3f72-acab-a68dc50e2c32 | -5.6569 | -43.6929 | 2025-07-18 00:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 45638488-7601-3e51-82f4-60a312ccc4dc | -3.3957 | -47.5003 | 2025-07-18 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| d27042ef-25c8-33cf-adec-9b875efccf23 | -8.1072 | -43.1646 | 2025-07-18 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.4 |
| b94a3ed8-639c-3cff-b3a2-43b058fcdf7e | -3.3958 | -47.4785 | 2025-07-18 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 172.1 |
| 3ad4fa31-a8a5-3864-97b1-7d95c9d8b722 | -7.3588 | -49.6013 | 2025-07-18 00:50:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 94dd67a7-ab09-33b2-a8c1-160ee92bce5c | -21.0795 | -50.5961 | 2025-07-18 00:50:00 | GOES-19 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 118.4 |
| ac2d2bd5-45fa-3714-a34c-a9bbb12ea3a6 | -20.896 | -49.0653 | 2025-07-18 00:50:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 48.7 |
| 35866299-a62c-3a28-b3dd-21d69307ff84 | -11.5782 | -47.0717 | 2025-07-18 00:50:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| eeeb40d6-f13f-37dd-a709-6bd55df91701 | -5.6567 | -43.7161 | 2025-07-18 00:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 409.4 |
| 18472e92-1a9d-34f7-b861-7f0b877702d8 | -3.3772 | -47.4792 | 2025-07-18 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 5b29e51c-ea10-3fd4-ba1b-be4e835ae8ba | -8.1075 | -43.1411 | 2025-07-18 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.3 |
| 594d7db9-9697-3b46-802e-2275d17900a8 | -8.0693 | -43.1687 | 2025-07-18 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.6 |
| 551d4bc3-a3fa-3cef-b487-f6c13253a567 | -20.916 | -49.0838 | 2025-07-18 00:50:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.7 |
| 988745e4-7435-3527-936f-d3e8a431abc4 | -20.9172 | -49.0376 | 2025-07-18 00:50:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 48.3 |
| 92b5db95-88f4-35f4-9f6c-c4460efe1ebe | -5.6379 | -43.7175 | 2025-07-18 00:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| f124bf97-ca86-3914-92bc-6f2e8e0e3158 | -8.0883 | -43.1667 | 2025-07-18 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 195.2 |
| 204b7a42-48a0-322a-aa02-01e84672c7ea | -21.0789 | -50.6188 | 2025-07-18 00:50:00 | GOES-19 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 325.3 |
| 6c0f480e-9587-35e5-97cf-c8846bc63892 | -11.5778 | -47.0941 | 2025-07-18 00:50:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 0c20c8fc-700f-3316-ae9f-d5780a312352 | -8.0886 | -43.1431 | 2025-07-18 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 297.5 |
| de5e3838-4873-319e-8740-bc9c3e03702d | -8.0696 | -43.1452 | 2025-07-18 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 115.9 |
| 804f01f4-131a-335d-ae10-723e29c77871 | -3.1198 | -47.0075 | 2025-07-18 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| ceb4c06f-1e5b-35fd-a8a7-fa8e516ec5b6 | -21.1001 | -50.5918 | 2025-07-18 00:50:00 | GOES-19 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.6 |
| 7cec96ee-2ad3-3cc8-9979-a664aeab7fc9 | -4.301 | -48.1133 | 2025-07-18 00:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| b6da6ebd-6002-38d7-bf7c-7b150894da8b | -21.0783 | -50.6415 | 2025-07-18 00:50:00 | GOES-19 | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 51.9 |
| 04a3145a-4ef0-3d27-b1cf-2a969be98620 | -3.3958 | -47.4785 | 2025-07-18 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 148.9 |
| 612770b1-2814-3b08-ae40-5ff5e3d3b2d1 | -11.5778 | -47.0941 | 2025-07-18 01:00:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 87c06315-f01e-332d-8b42-3bb565830a35 | -3.1198 | -47.0075 | 2025-07-18 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| cda24dbb-67dc-372c-bd81-f12f8800d0f5 | -3.3772 | -47.4792 | 2025-07-18 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 27a8888f-d228-3edd-85d3-b4a71af764b0 | -20.9166 | -49.0607 | 2025-07-18 01:00:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 101.3 |
| 2c4661e0-a27a-3048-a959-25fc3cd12947 | -11.559 | -47.0742 | 2025-07-18 01:00:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| f356ae85-1852-3da9-8942-b8d6cf9daba4 | -5.6379 | -43.7175 | 2025-07-18 01:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| e3715558-f2a0-3f26-9bb0-08f2a7597925 | -5.6565 | -43.7393 | 2025-07-18 01:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 038a2cdf-0969-3bdb-80f9-9733217e990a | -5.6567 | -43.7161 | 2025-07-18 01:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 324.4 |
| 0b32c5ee-a421-3709-b9d8-f939c8452950 | -11.5782 | -47.0717 | 2025-07-18 01:00:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 45b69cd2-8dc0-35de-a3e3-f4155c3bde9a | -8.0886 | -43.1431 | 2025-07-18 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 366.1 |
| 47a22f3d-41cf-3ded-8155-0e72f608621f | -21.0995 | -50.6145 | 2025-07-18 01:00:00 | GOES-19 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 152.7 |
| a300b4fe-37df-3876-99a7-5c1d4013db94 | -8.0883 | -43.1667 | 2025-07-18 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 170.2 |
| 67453c54-e6a5-3377-b1f6-e98d260b841b | -21.0789 | -50.6188 | 2025-07-18 01:00:00 | GOES-19 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 330.1 |
| dbfd91e5-5708-3e4b-a073-5906d0cd9d9e | -3.3957 | -47.5003 | 2025-07-18 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 5d22b4a0-9ca5-375c-ab24-9bdc2c99bf9f | -5.6569 | -43.6929 | 2025-07-18 01:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 7e7d0573-9864-3507-9f7f-34e5bf483939 | -4.301 | -48.1133 | 2025-07-18 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 308bcdcd-5c5b-3d40-862d-8fd26fa2dfde | -8.1075 | -43.1411 | 2025-07-18 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.2 |
| b6971bf4-041b-3789-a2ba-6620d2489be6 | -8.0696 | -43.1452 | 2025-07-18 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 141.9 |
| b112de72-f646-329b-8aed-e4dff11cbea0 | -8.0693 | -43.1687 | 2025-07-18 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| fe1ec0a8-042b-3cb7-bc8b-de1e1babbd63 | -21.1001 | -50.5918 | 2025-07-18 01:00:00 | GOES-19 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.3 |
| 824ebffd-88cf-3c93-a6ab-e2245bde7fd7 | -11.7317 | -48.1849 | 2025-07-18 01:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 19eb5a7f-8402-3a1e-af6e-2ab9678e702e | -21.0795 | -50.5961 | 2025-07-18 01:00:00 | GOES-19 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 129.5 |
| a73694f2-187e-363b-bb84-7315930e4c24 | -23.92522 | -50.47231 | 2025-07-18 01:00:00 | TERRA_M-M | FIGUEIRA | PARANÁ | Brasil | 4107751 | 41 | 33 | nan | nan | nan | Mata Atlântica | 30.1 |
| c6282eef-bb21-31a1-b7b0-259fc9bb55f9 | -20.91432 | -49.05314 | 2025-07-18 01:02:00 | TERRA_M-M | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.5 |
| 08c64095-26f0-38b5-a701-1e78fc147cc1 | -20.91581 | -49.05875 | 2025-07-18 01:02:00 | TERRA_M-M | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 230.1 |
| 258da54b-0f63-328e-bd03-6376fa18e391 | -21.08981 | -50.63137 | 2025-07-18 01:02:00 | TERRA_M-M | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 73b5886f-78bb-378b-850a-8e8923d6b9e8 | -20.91774 | -49.07101 | 2025-07-18 01:02:00 | TERRA_M-M | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 221.5 |
| d5f9f6f9-a06f-3fd7-9ab8-fdb41d17a57e | -18.66078 | -55.73863 | 2025-07-18 01:02:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 280e6447-397e-337d-8bed-497771a5167a | -21.04088 | -55.97969 | 2025-07-18 01:02:00 | TERRA_M-M | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 8e143f6d-095a-3948-b542-0bc224841e57 | -21.07749 | -50.6125 | 2025-07-18 01:02:00 | TERRA_M-M | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 128.9 |
| 3415893b-6339-33d8-a44f-fcdeb43e7249 | -21.08826 | -50.62112 | 2025-07-18 01:02:00 | TERRA_M-M | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 267.6 |
| cac3e020-c55a-375d-bacb-bfb77142674c | -20.91634 | -49.06549 | 2025-07-18 01:02:00 | TERRA_M-M | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 626.8 |
| 9c449dec-624c-3b8e-b7ae-06961417c90d | -20.91833 | -49.0777 | 2025-07-18 01:02:00 | TERRA_M-M | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.4 |
| 827b8906-6c86-353b-96c8-e498c28f928d | -18.22461 | -54.54859 | 2025-07-18 01:02:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| aad6fdd9-d9e7-3f27-8d64-1da151eecdce | -22.24888 | -49.92563 | 2025-07-18 01:02:00 | TERRA_M-M | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 607b0364-4e4a-318e-ab28-6dd008bb9567 | -18.87514 | -47.98535 | 2025-07-18 01:02:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| ab647d7f-c9cd-3d97-97fa-7c84fe05e230 | -20.90579 | -49.06061 | 2025-07-18 01:02:00 | TERRA_M-M | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.5 |
| ed6d795c-6ac2-3474-9b79-8ac41fea9d42 | -21.07905 | -50.62277 | 2025-07-18 01:02:00 | TERRA_M-M | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.6 |
| ffd5435d-51ff-36f5-99da-49d751b064cb | -23.07672 | -50.03611 | 2025-07-18 01:02:00 | TERRA_M-M | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 20.3 |
| b284b7ef-8425-3e68-a356-eb81fdc5f052 | -23.79914 | -51.97129 | 2025-07-18 01:02:00 | TERRA_M-M | SÃO PEDRO DO IVAÍ | PARANÁ | Brasil | 4125803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 30.0 |
| df8dda9a-780a-39a0-82d8-e75808b91bac | -18.65941 | -55.72759 | 2025-07-18 01:02:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.5 |
| d670d9d4-e89b-3327-9c2c-38869963a959 | -21.04237 | -55.99197 | 2025-07-18 01:02:00 | TERRA_M-M | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 70193f57-f3e4-31e3-a383-9dbc6e642962 | -16.4171 | -53.16617 | 2025-07-18 01:02:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| bfb1f42a-44a0-3303-85c6-9a821cc8f92a | -20.90771 | -49.07279 | 2025-07-18 01:02:00 | TERRA_M-M | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 36.5 |
| 4a27e81a-f1a8-3b2e-ab99-886e4a8eee2a | -21.0867 | -50.61083 | 2025-07-18 01:02:00 | TERRA_M-M | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 429.9 |
| d6a9e9f2-1e05-35fc-b335-82623491a0a8 | -9.49625 | -64.11995 | 2025-07-18 01:05:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 51e20978-9fb8-3deb-9e61-b8d22f652494 | -9.76053 | -48.75269 | 2025-07-18 01:05:00 | TERRA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 69806dd0-a91a-3302-a243-89faa25561f2 | -11.73554 | -48.20381 | 2025-07-18 01:05:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 67feea09-fc9c-38e7-9bac-651465c6adf9 | -9.87719 | -65.17107 | 2025-07-18 01:05:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 5f0e3689-7b02-34b0-b653-3df3b5107b7c | -11.74819 | -48.20163 | 2025-07-18 01:05:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 61278466-ce21-3bb0-8f52-5a606dc1fd7c | -12.66667 | -47.0904 | 2025-07-18 01:05:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 32.4 |
| f3d79d1f-3ba2-3d37-b256-fab6632c3636 | -11.73221 | -48.17832 | 2025-07-18 01:05:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 5ce6e05f-20dd-38c8-9b8d-787426e0439a | -12.65968 | -47.09735 | 2025-07-18 01:05:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 40.6 |
| aae06b89-ccda-3a2c-94a7-4d9ea98fb321 | -8.04661 | -50.07732 | 2025-07-18 01:05:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| ed81f6e7-af29-363f-ac20-69feea7aa921 | -10.81357 | -49.28584 | 2025-07-18 01:05:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 289e6751-ec21-3cf8-b8a9-57c1bb487f85 | -11.74505 | -48.1818 | 2025-07-18 01:05:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 83e5a470-0b9e-368f-9bc6-a6a2c0bb2a23 | -11.55396 | -47.07804 | 2025-07-18 01:05:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 51eab86a-7be5-3150-8078-5b8714094387 | -15.09088 | -49.4594 | 2025-07-18 01:05:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 1948e7ca-324a-31ad-b9ac-f6e1dab86ecd | -9.76357 | -48.77185 | 2025-07-18 01:05:00 | TERRA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 0ecbb294-5bd2-31b8-b4c5-631d37246221 | -12.5787 | -56.97896 | 2025-07-18 01:05:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fde9d30d-5204-3d2e-a80b-8b08f16ee0e8 | -11.56782 | -47.07551 | 2025-07-18 01:05:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| e44bd7f0-7119-321d-9631-aa0ac316761e | -8.87386 | -50.14827 | 2025-07-18 01:05:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| b4a9943a-b39c-314d-8ca2-f8c22c03a491 | -10.82236 | -49.29594 | 2025-07-18 01:05:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 15fc99b3-c04f-333c-a99b-b99e588be470 | -9.80384 | -47.7398 | 2025-07-18 01:05:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| e778e6b2-80db-3166-9847-c8c6f07e5fe9 | -8.03481 | -50.07822 | 2025-07-18 01:05:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| c9d84498-ffcf-3c93-82b3-605aa21bb552 | -10.81612 | -49.30243 | 2025-07-18 01:05:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 948b02ba-2996-314c-afb7-c3fd55a14e63 | -10.67558 | -56.54681 | 2025-07-18 01:05:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2ea9f10a-bccd-3283-8493-f8c5a0a4df32 | -8.64794 | -47.75465 | 2025-07-18 01:05:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 525c472e-84bf-36d0-b401-46d0e55b7f5a | -8.87622 | -50.16368 | 2025-07-18 01:05:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 0d499304-413a-35b5-9cdb-1bc7c611fcd5 | -11.55796 | -47.10252 | 2025-07-18 01:05:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 5a6cda23-acd6-3b49-98b7-94ce73a6d5ea | -12.48154 | -46.91887 | 2025-07-18 01:05:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 27a1ce53-93a2-31d1-9d25-59cc872b1c11 | -11.57176 | -47.09988 | 2025-07-18 01:05:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| f009320b-1b0c-3477-86cf-5c21c9192516 | -11.74817 | -48.19595 | 2025-07-18 01:05:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 944109ec-9648-368f-bb5e-7edb93e5f41b | -14.14871 | -51.02883 | 2025-07-18 01:05:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2f332a2a-8b44-30d5-9ea6-07ba50b72c5c | -11.57695 | -47.09334 | 2025-07-18 01:05:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |


[Clique aqui para ver as próximas entradas](README4.md)
