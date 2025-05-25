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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79f45cb6-14f9-37c5-aa70-1c3d1bbc083c | -19.37062 | -53.21076 | 2025-05-25 05:31:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5267deee-f0dd-3cf0-907e-f8f305a25cb0 | -20.95675 | -56.59978 | 2025-05-25 05:31:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8649049-8a3c-3e67-8765-e0a16824e92a | -20.94473 | -56.5885 | 2025-05-25 05:31:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09235d67-1b13-3d3b-b74d-5106ced275ca | -19.36441 | -53.21022 | 2025-05-25 05:31:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9ddf5743-541e-3688-a836-d7f057a67148 | -19.1018 | -54.44873 | 2025-05-25 05:31:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fa8afe6-99c0-34f4-991f-ab91736aa41b | -19.87923 | -54.36898 | 2025-05-25 05:31:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cebca88c-9bf5-3315-890a-ca705688b09e | -19.10135 | -54.45324 | 2025-05-25 05:31:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13ff46a9-53c2-3c70-b7c0-2dba1a4b6bf8 | -20.93896 | -56.59407 | 2025-05-25 05:31:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 51792c3a-8834-38e6-bf63-881a52778b09 | -19.37684 | -53.21112 | 2025-05-25 05:31:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5019179f-1696-3d12-af66-84fe7b51ab21 | -20.94145 | -56.5978 | 2025-05-25 05:31:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 04c2f47a-7e76-3586-8ba6-c11c4dc6a9ac | -20.94405 | -56.59474 | 2025-05-25 05:31:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7954b3d3-7d93-3573-a605-92897295dbbd | -20.93929 | -56.59101 | 2025-05-25 05:31:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c3290fec-64e7-3aee-ab88-69723afc2a74 | -20.95392 | -56.59909 | 2025-05-25 05:31:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cdb5d39a-6d6d-369e-93bb-4dd3fb0dde6f | -20.95165 | -56.59908 | 2025-05-25 05:31:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fbf1e942-e617-3cb0-91f7-5bbd8e40dcc3 | -19.36293 | -53.21137 | 2025-05-25 05:31:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76ddee0b-caa7-302e-9608-ddb30612c154 | -7.6574 | -46.1013 | 2025-05-25 05:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 5d10c6bd-b763-375f-8e17-2dffab78965e | -7.6574 | -46.1013 | 2025-05-25 05:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 9d9ccc68-97ec-3047-91b6-89f77570050b | -7.6574 | -46.1013 | 2025-05-25 06:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| ca7cad59-750a-371b-865e-9d8997c5a7c7 | -7.6574 | -46.1013 | 2025-05-25 06:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 85dcd05d-b786-3624-9e57-8bf56b0f5677 | -7.6574 | -46.1013 | 2025-05-25 06:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 3c8c8fef-6c07-3982-ab7d-3ed28a9e2f57 | -7.6574 | -46.1013 | 2025-05-25 06:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| b693cf53-bd88-3320-a600-d501475f0661 | -7.6574 | -46.1013 | 2025-05-25 06:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 5da86df7-8ad1-38f3-b61b-96a2ebb2dc5c | -7.6574 | -46.1013 | 2025-05-25 06:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 938e1fa9-e728-3822-b2a0-2771e6d53f12 | -7.6574 | -46.1013 | 2025-05-25 07:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 0b7f9df4-7271-37b0-ae27-c454fdff64ae | -7.6574 | -46.1013 | 2025-05-25 07:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 44.2 |
| da057a1f-e0ca-30e0-a06f-5ec4d5d3d528 | -7.6574 | -46.1013 | 2025-05-25 07:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 078096b8-0bc3-348f-a68c-2e0e8eb6840a | -7.6574 | -46.1013 | 2025-05-25 07:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| e7bab092-578c-3195-aa80-91e541386401 | -7.6574 | -46.1013 | 2025-05-25 07:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 336da5a1-72b4-3392-8d23-ab7de68a8eae | -7.6574 | -46.1013 | 2025-05-25 07:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 02036ca5-a122-33b3-aee3-26fff1059919 | -7.6574 | -46.1013 | 2025-05-25 08:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 2e7e38fb-abc5-3603-88c5-efd7277fa616 | -7.6574 | -46.1013 | 2025-05-25 08:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 23af4b63-5f4d-3860-a84e-ee64d4da1d20 | -7.6574 | -46.1013 | 2025-05-25 08:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 90eaeba8-c5a6-31c7-857a-9348b3e1f24f | -7.6574 | -46.1013 | 2025-05-25 08:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| ddf28361-7893-33ff-bcc9-187a351c73c0 | -7.6574 | -46.1013 | 2025-05-25 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 1976df61-c297-30fa-8403-1552a34e0e15 | -7.90681 | -44.47592 | 2025-05-25 12:21:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 55196a32-c939-3d25-bbe2-f859d3edca3e | -6.81825 | -44.8054 | 2025-05-25 12:21:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 03c4bbc1-24e7-3b46-a492-a6a24fbdd63d | -8.90531 | -44.7772 | 2025-05-25 12:21:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 403163f5-0029-3000-a239-c630c10abd56 | -7.28273 | -47.07322 | 2025-05-25 12:21:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fa7e9a26-b663-38fa-931b-f7bea8e51aca | -6.68361 | -45.42919 | 2025-05-25 12:21:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 8fafcdd1-899f-394b-b047-a1b84e2d61fe | -11.0954 | -42.16328 | 2025-05-25 12:21:00 | TERRA_M-T | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 01732661-f178-3e0a-918c-95d56133f044 | -9.73936 | -48.34486 | 2025-05-25 12:21:00 | TERRA_M-T | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 44ea9aef-c30f-3249-9302-f9dbe91cf48b | -6.83499 | -44.62457 | 2025-05-25 12:21:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 71fb2379-35bd-33ff-b142-3d3b68d4b791 | -8.34717 | -47.36092 | 2025-05-25 12:21:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 1a52f7a5-6114-37d0-8e11-16373b518891 | -8.36944 | -47.08605 | 2025-05-25 12:21:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a10e4688-2cec-3978-a27e-b3fb47edc5cd | -11.83566 | -44.82419 | 2025-05-25 12:21:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 67ee6301-056f-30f3-90a2-dd1f8cd9e320 | -9.74099 | -48.33425 | 2025-05-25 12:21:00 | TERRA_M-T | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2a7246ae-1222-3439-8df5-dde9eb2616cd | -7.65564 | -46.09695 | 2025-05-25 12:21:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 5484c609-31f4-39c1-a810-8fc21e8318bf | -6.5208 | -45.97874 | 2025-05-25 12:21:00 | TERRA_M-T | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| baf006cd-c44a-3857-bd95-6c4aae6cf76a | -12.27226 | -44.59844 | 2025-05-25 12:21:00 | TERRA_M-T | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| eb3174ef-951f-34b3-8f39-683b76bbb75f | -7.47086 | -43.38208 | 2025-05-25 12:21:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| af8def60-2aae-35c3-bf78-86b0e4f6db0c | -7.59292 | -46.2794 | 2025-05-25 12:21:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0ea5b5a3-c9b8-30f0-b4cb-6f2bfbc24e0b | -7.57838 | -43.34043 | 2025-05-25 12:21:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| de402917-f33e-3e01-b4a3-d2b4963c8e08 | -7.34591 | -43.4811 | 2025-05-25 12:21:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7abdf073-e1d8-3f86-a24c-781c03766c0c | -12.25511 | -46.68497 | 2025-05-25 12:21:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 11de95ae-b551-35af-bbfa-34271638ad81 | -7.65435 | -46.10587 | 2025-05-25 12:21:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 667d2723-3bce-394f-9272-5511755d29f7 | -10.99032 | -42.18329 | 2025-05-25 12:21:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| a15fa28f-e600-3168-9cd6-b0738e636794 | -6.56005 | -44.48515 | 2025-05-25 12:21:00 | TERRA_M-T | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 160e288d-5c4c-3d97-b556-4887f7d9a0d8 | -8.05652 | -43.14127 | 2025-05-25 12:21:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 30c16459-1d07-33d2-aaf5-48b99c2ce23e | -8.34576 | -47.3704 | 2025-05-25 12:21:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| ce5331b1-bca7-3a61-b1da-bb7430c1f438 | -10.64618 | -46.72108 | 2025-05-25 12:21:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 46242597-473c-30f7-b2a9-02dd286bdaf7 | -7.64549 | -46.10461 | 2025-05-25 12:21:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d45e52b4-5a6f-3aed-a9b8-7111a2ae61ca | -7.64678 | -46.09571 | 2025-05-25 12:21:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 28e119d1-d251-32aa-bef9-37da136f5b27 | -7.66322 | -46.10714 | 2025-05-25 12:21:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| bf9b5bf9-ce77-3504-9e8b-2fb8c86b1d5a | -12.25638 | -44.91775 | 2025-05-25 12:21:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b0241b7e-2ab5-347c-9f2c-f64ab10b65ec | -7.52941 | -43.17085 | 2025-05-25 12:21:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 28821aaf-9c3f-3a9f-a13f-666d3d0c3324 | -8.46855 | -47.04034 | 2025-05-25 12:21:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b1cc513d-5438-316b-97cb-468bdccb91c9 | -7.66451 | -46.09822 | 2025-05-25 12:21:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| a557429c-02e5-37e9-875d-63d08758a5c4 | -8.73429 | -47.98591 | 2025-05-25 12:21:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 413a1b1a-775c-372b-9c7c-5054d49f7395 | -7.54785 | -45.83039 | 2025-05-25 12:21:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 66c26f26-b24f-3368-afda-0b2575c864fa | -7.59354 | -43.30101 | 2025-05-25 12:21:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 8747fcc2-f2a2-35e8-a4bf-b0cc5d8111ff | -6.51951 | -45.98766 | 2025-05-25 12:21:00 | TERRA_M-T | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| dd5ecdb2-568a-32f0-afb7-0747fea22de5 | -7.48169 | -43.37326 | 2025-05-25 12:21:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 52d9e77f-a852-3e53-8689-abf29f6f15e7 | -10.69981 | -48.60503 | 2025-05-25 12:21:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ab8a76b4-1113-390f-a470-4e7f4f8594f2 | -7.539 | -45.82914 | 2025-05-25 12:21:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e5407c78-7bd1-3cf1-9975-6217fef249f7 | -7.34729 | -43.47113 | 2025-05-25 12:21:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 49288cb2-e74f-3782-8666-273611708aec | -10.6983 | -48.61505 | 2025-05-25 12:21:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f133cda6-96cb-366b-9450-9ed1923ace80 | -8.45953 | -47.03905 | 2025-05-25 12:21:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b64ecb23-a5fa-3551-8de1-551101db0c30 | -8.4609 | -47.0298 | 2025-05-25 12:21:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7c57841e-b4b7-3122-a863-84dd35d068cd | -12.39493 | -44.83969 | 2025-05-25 12:21:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 99eb6bb5-e15a-3dd5-b66b-115131e530c0 | -12.17706 | -44.34142 | 2025-05-25 12:21:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 56c1de53-a202-3185-afed-e1d11c277e32 | -14.88088 | -47.83715 | 2025-05-25 12:23:00 | TERRA_M-T | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 7b14ff9f-8ac7-33a5-b926-1b7c6f15fdc0 | -13.83437 | -48.91433 | 2025-05-25 12:23:00 | TERRA_M-T | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ba379732-c6b0-392e-82fd-7c23af4104e3 | -15.51208 | -49.34943 | 2025-05-25 12:23:00 | TERRA_M-T | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 51.2 |
| c17daa14-55b9-30e2-8d33-b5fa0bc6104d | -13.68356 | -45.24556 | 2025-05-25 12:23:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 836cb532-3ba9-3c03-bdb4-4233812984d0 | -13.69055 | -45.25246 | 2025-05-25 12:23:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1cba8297-a98f-36b9-b714-a3c518add199 | -13.37119 | -43.64291 | 2025-05-25 12:23:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 6259541f-f58b-306f-8584-15ba1ec144d9 | -12.29955 | -52.47377 | 2025-05-25 12:23:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| b3348c4c-244d-37bc-9324-af6ab2ff0816 | -13.36969 | -43.65454 | 2025-05-25 12:23:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c95d4bad-5788-33a0-a957-dfcc0b795746 | -15.51365 | -49.33926 | 2025-05-25 12:23:00 | TERRA_M-T | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3037ea84-b1e6-3ea7-a3e5-c660290847cf | -13.69187 | -45.2427 | 2025-05-25 12:23:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5031550e-8fde-3d07-bfdd-0cf0b4442f5c | -13.56408 | -49.05971 | 2025-05-25 12:23:00 | TERRA_M-T | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c3a7e712-6aff-39c4-be52-bf130beda2ad | -16.40857 | -43.71471 | 2025-05-25 12:23:00 | TERRA_M-T | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 93e5d560-b4e2-3a0c-aeb4-97231330808a | -12.63623 | -54.0756 | 2025-05-25 12:23:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| a9f7b697-6037-31ec-ad98-45fae378950a | -22.58743 | -47.11632 | 2025-05-25 12:25:00 | TERRA_M-T | ARTUR NOGUEIRA | SÃO PAULO | Brasil | 3503802 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 422c3a73-fc12-3162-9c83-974f242289fe | -7.6574 | -46.1013 | 2025-05-25 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 143ae3f9-6ac9-3ba7-9958-737ca2ae2010 | -8.0507 | -43.1472 | 2025-05-25 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 105.5 |
| 55c4b093-4adc-3193-8179-4c18ec15c0f5 | -7.6574 | -46.1013 | 2025-05-25 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 5a4e822c-0d65-364b-b0e3-c02f601be89d | -8.0507 | -43.1472 | 2025-05-25 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 147.5 |
| 82e9c8a5-f067-3b01-99e9-4e0aa0c870a4 | -7.6574 | -46.1013 | 2025-05-25 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| acf41ac5-11ef-3de4-ae35-7cc32b571cb9 | -7.6574 | -46.1013 | 2025-05-25 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |


[Clique aqui para ver as próximas entradas](README13.md)
