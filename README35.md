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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b3e2a07-dfac-35df-b567-1ed1015fdee7 | -4.28206 | -40.70341 | 2025-10-24 04:38:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 7c90b509-fc4d-353b-9b9f-1cc7d8cbede6 | -9.87161 | -47.46922 | 2025-10-24 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d787d940-7258-3d59-badf-4cdcb3ef9e44 | -7.69015 | -42.23766 | 2025-10-24 04:38:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| cc0e1102-ed85-3dcd-ad03-525faca96009 | -4.47252 | -49.09998 | 2025-10-24 04:38:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef36219c-9103-3f0a-b074-3c9f924640e0 | -6.46938 | -44.12323 | 2025-10-24 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22572cc2-bbee-333a-bc29-5b98527b79b0 | -4.27264 | -46.99219 | 2025-10-24 04:38:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1f53fc4-bbb7-336f-8b6b-eb5fdaaa013c | -6.91726 | -44.0176 | 2025-10-24 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e18df8a1-8b46-371a-a482-11817fa5f71d | -6.29872 | -41.8862 | 2025-10-24 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f6d5b863-91aa-33ae-b055-0ccab4ad766b | -9.93256 | -51.61377 | 2025-10-24 04:38:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58baa438-8e5e-399d-a99f-3ba7dfb0e6a0 | -4.46922 | -49.09946 | 2025-10-24 04:38:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4efefe1b-01d2-3400-934f-6e5c87fcdf10 | -3.13539 | -49.51776 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5d319564-8fb6-3613-b804-76eacc4a2719 | -9.26559 | -46.451 | 2025-10-24 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32b097d2-66a4-3e98-ab01-cae269c6b732 | -3.02537 | -49.48226 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d950fb5-4e94-34f4-acbc-9696523226ce | -4.22176 | -48.36203 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0704a8cd-a702-3aa2-8aaf-35a97f45c6f4 | -4.80311 | -48.22963 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a616676-a979-38c8-80b2-3c88da9e6e77 | -9.30169 | -45.19593 | 2025-10-24 04:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79b5421d-a289-3ebb-8d20-094fdbe6caab | -7.54845 | -47.36911 | 2025-10-24 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 53e5595b-fcc6-39f1-ae14-2d35e7396a9e | -9.60193 | -46.90392 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3a416ae0-d65c-343f-919d-2e7492d8b2c9 | -3.0237 | -49.44975 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| ac4c24b6-f0d3-3676-ba5a-dbbabc5cc6cc | -3.92472 | -47.69931 | 2025-10-24 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 724281b0-edb4-3254-b982-82f917965b6c | -8.20204 | -46.9872 | 2025-10-24 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 043ee842-89a8-3dc2-9165-8bdb7e135baa | -2.92568 | -48.30699 | 2025-10-24 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0303ad53-411b-3dc2-896e-f0e462d13bf8 | -7.15888 | -49.51524 | 2025-10-24 04:38:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| accd69db-3e96-3213-b7b9-0c277d39d765 | -6.66861 | -49.47997 | 2025-10-24 04:38:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e7a8c252-9098-30d4-be94-33cbb31f596b | -10.8747 | -45.08169 | 2025-10-24 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31317abc-771b-362a-b242-316582016784 | -2.86427 | -50.71852 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc30096f-b666-3534-b45f-6a8cdaad3a32 | -6.30347 | -41.88678 | 2025-10-24 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b9f6a42e-cd12-33a2-87b1-c7eabb36a9fd | -7.9792 | -47.237 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30482ff0-35d2-33f9-b7d5-97bcb30f3a84 | -10.00926 | -47.10454 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5ec6c493-7dbc-35d9-93f1-6d278243cfa3 | -6.02495 | -48.90778 | 2025-10-24 04:38:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 06ebc2ef-4a67-3062-96d2-c906acd2d75b | -6.77676 | -45.48053 | 2025-10-24 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56c84dac-d0a6-35bf-9f9b-a23d1718c179 | -8.17491 | -47.76289 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1315ac2-87ea-392a-bd11-4bd53ec372f6 | -3.24856 | -50.13146 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 279633fc-4e2d-3a37-aa82-a28a71019c79 | -3.01931 | -51.36303 | 2025-10-24 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a07a457b-4d1f-37ff-a1f1-b034200b1c00 | -8.70652 | -47.60184 | 2025-10-24 04:38:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d3e480d8-b093-39d9-9bf0-5cac0447d754 | -6.43499 | -45.66888 | 2025-10-24 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9428945c-f6ba-3bdd-a4c6-ea1b9408d59b | -4.20715 | -48.60687 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 05661800-02ae-3648-8ebc-3a274cf2a98e | -3.24097 | -48.7648 | 2025-10-24 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bfc04518-90c1-3a05-a7b6-f215094e642d | -5.5838 | -41.31808 | 2025-10-24 04:38:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8a81a2b4-271d-35ef-8270-b15c48a52edc | -9.8687 | -47.46473 | 2025-10-24 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10f1b53f-47d5-3b84-af2b-75d03724c966 | -9.60714 | -44.62357 | 2025-10-24 04:38:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0f8272bb-84e5-3420-bdae-5d2076341b40 | -6.7294 | -42.68214 | 2025-10-24 04:38:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| e9b8f42b-2b6c-35b1-ae10-be98417768ad | -4.27641 | -48.33874 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a55144be-b05d-3f98-baf9-ef9f89e328fc | -3.79144 | -50.37563 | 2025-10-24 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b48c2f31-4ac1-37c2-bc74-3176442e67dd | -7.63459 | -44.56968 | 2025-10-24 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2143390-2feb-3d34-a67d-c8ff4af302a0 | -5.47805 | -46.47141 | 2025-10-24 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15924d8b-8f4c-3a5f-a41f-154e014d22d3 | -10.27538 | -47.87951 | 2025-10-24 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4277099-18fa-3042-ab5a-2f41f1c54b86 | -3.29183 | -50.19357 | 2025-10-24 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| baa2535c-8bec-36c7-9c96-1ba91b9ed31c | -11.05359 | -45.39883 | 2025-10-24 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 32c0b3d8-89bd-3317-85bd-39a10a13ba4d | -5.54982 | -41.34689 | 2025-10-24 04:38:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2e19e33d-0a59-31ff-a819-f74c2ff90ec4 | -9.60492 | -46.90861 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a466f02f-5ab7-3d6a-8240-7683ed2dfbb4 | -9.60255 | -46.89977 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 46cae06b-a642-3e00-b397-70075d0f3fd4 | -7.82832 | -46.92561 | 2025-10-24 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3727739c-7900-35c7-908f-6036362fb7ae | -3.2873 | -50.19315 | 2025-10-24 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b19b17b0-187b-34c3-ad08-af43865b7297 | -7.7853 | -45.405 | 2025-10-24 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0549076b-5189-3441-b362-70539fdd3a9f | -7.69765 | -49.35275 | 2025-10-24 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66df920c-e375-38d2-9185-3dd22b8e96d0 | -6.92608 | -44.01498 | 2025-10-24 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 247bb0cf-826a-3f82-a7c9-97957be7236b | -5.91385 | -49.99652 | 2025-10-24 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ca1bd4a-d953-35bb-bca4-e01a3220ea59 | -9.23504 | -51.82255 | 2025-10-24 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e6edb2a-008b-33b8-9e1f-f8a604aecf85 | -7.6322 | -42.20393 | 2025-10-24 04:38:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fd9b7cdd-529e-38a5-be0a-ccaed2aa14b7 | -7.90825 | -48.94014 | 2025-10-24 04:38:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 70cbe0a4-b49d-3111-958e-960da6a6a940 | -9.35649 | -47.70135 | 2025-10-24 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e0e9d477-3c39-363a-b40b-e79a32d60d2b | -4.91719 | -47.32907 | 2025-10-24 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cae99389-f5a4-398f-9a99-f8ad6afc37fc | -6.90141 | -43.59433 | 2025-10-24 04:38:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04e01afa-d8de-31a1-b022-3e31e5c9a0a0 | -3.99994 | -43.75737 | 2025-10-24 04:38:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ead643b-ebfb-320b-81a5-ec1ed2684f68 | -10.01223 | -47.10917 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7f2fcd55-c1e4-30f9-8189-f21e2cb60708 | -6.30342 | -41.87975 | 2025-10-24 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 31fff06c-ce23-3135-99d2-12b97c202ee1 | -4.87491 | -47.53304 | 2025-10-24 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 42a6589e-b3fd-3038-8646-772ce89ca2a3 | -3.98655 | -47.00565 | 2025-10-24 04:38:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d326461-482b-32cb-a386-29b644991751 | -8.20558 | -46.98772 | 2025-10-24 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8e0db699-d74b-30bd-b598-0e75b0041cd3 | -4.46635 | -43.23631 | 2025-10-24 04:38:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9045a0a8-b569-3db2-a030-2529676275b9 | -4.23965 | -48.20544 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ac19e30-1160-316a-9098-166ce383cf81 | -8.44728 | -49.57496 | 2025-10-24 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 97a5ff30-69e6-3cc2-bece-0e54ff15582c | -7.38787 | -46.53828 | 2025-10-24 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f78a6c2e-bf1c-3761-b031-2a275519b5c9 | -2.80438 | -51.34775 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e426abf5-1312-3671-9880-290812680813 | -4.90946 | -47.6558 | 2025-10-24 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c5c15ce3-eb2d-34e0-be26-f6327c21a1c1 | -8.17604 | -47.75545 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2efce4d1-c394-3ba3-9cc2-689f888e97eb | -3.13534 | -50.62115 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91b20691-f740-3535-966b-a67701d3dcaa | -8.06841 | -47.13003 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e5aa58b-50b9-3637-aae5-43a167d0c00f | -8.31068 | -49.73104 | 2025-10-24 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ddfc43c4-1b76-3205-9d19-9fec2b3b3b20 | -7.3352 | -49.04305 | 2025-10-24 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f07f0f87-9ddd-3610-a56c-a4d9ce48b85b | -6.77881 | -45.46676 | 2025-10-24 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eff34adc-0ea9-32a8-980e-16c46ce46c9e | -5.56415 | -46.5242 | 2025-10-24 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2d668c2-eb88-38ec-b953-f6fecbc5179d | -5.94397 | -46.47748 | 2025-10-24 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f57bc23d-2f14-3538-95f1-91e4b9ae2208 | -6.30489 | -41.87667 | 2025-10-24 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e854be38-f7eb-321d-bc83-85da337d4aa0 | -9.18605 | -48.8438 | 2025-10-24 04:38:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 514558c3-4650-3bbb-b4b0-bdd7017c6968 | -6.27656 | -47.01529 | 2025-10-24 04:38:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1da627c8-6ed3-3d79-8ca5-827eac1cc718 | -3.02037 | -49.44923 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 91841b9f-263e-32a5-8086-54c7f116fe28 | -5.40839 | -46.40879 | 2025-10-24 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9e028c3-5528-38a3-8e58-d37832fc9435 | -9.8139 | -45.72254 | 2025-10-24 04:38:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4358a0ff-b641-39b5-beba-c0e7690f1a2f | -2.68834 | -54.77056 | 2025-10-24 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af31ec7c-283b-3ef6-90a3-42e11c323603 | -7.03444 | -46.6292 | 2025-10-24 04:38:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1b4da03-fe2b-37c8-9e34-d5ca1e5de61e | -4.9138 | -47.32856 | 2025-10-24 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6ffb669-02bd-3b6e-a72f-982f8e2eda0f | -5.22221 | -48.00414 | 2025-10-24 04:38:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 341f3a9d-9bf3-3035-b7df-072c7c2f01ca | -3.55254 | -49.43678 | 2025-10-24 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4440d82b-5785-3f2e-84c6-8537294df70d | -4.79311 | -42.75292 | 2025-10-24 04:38:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdd98c90-0740-339a-9389-292f7c7793ff | -3.29914 | -49.12692 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1beb9849-2fb5-32fa-b200-a4081ba7252b | -9.23723 | -51.83054 | 2025-10-24 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbd6af2a-40d9-3004-acc3-9f54fcfa9d5b | -4.24665 | -48.54956 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f6cf362-3ab7-35e6-9556-6d31bde9c098 | -7.83449 | -45.38101 | 2025-10-24 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README36.md)
