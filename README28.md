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
| 9a95e81d-8e30-3b15-b70e-118edcfd05d5 | -4.30889 | -45.49175 | 2024-11-10 04:14:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f8218e2-aff0-3d9f-844b-93498f9c83c6 | -3.57457 | -45.8184 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c9d7e7f2-31b7-31af-903d-38520fb9529e | -2.75797 | -49.35997 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 61458edf-b3f2-3c88-85e0-d4e41b02582a | -2.16001 | -46.67397 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf9702da-96a3-3170-8f6d-77459ba45174 | -3.1201 | -50.14281 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4aaf392f-b4ba-3aba-863d-b5fa497ec314 | -3.24016 | -50.27462 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 14a01a8e-ae55-3b59-a86d-f785a48d55a1 | -3.03233 | -50.35579 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c710774f-d9a7-3e76-ba00-46bf6be9087d | -4.16978 | -48.59795 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf37d06c-6de8-36a9-9092-be296ceb078c | -0.04672 | -50.77734 | 2024-11-10 04:14:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd5c6ae2-c469-3608-9ced-046fff717df6 | -3.94667 | -48.15852 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 89fbb13c-eafe-3dae-adb6-7d13172ebdf0 | -5.36035 | -47.91689 | 2024-11-10 04:14:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb234a4e-b6b3-355f-a674-79e8efe75f4c | -3.4087 | -50.29954 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1e10ca8a-63e6-3ff8-bfba-ced894f8a2fb | -3.34323 | -45.78825 | 2024-11-10 04:14:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a727413e-be47-33ae-91b1-2df155bc1e89 | -2.64381 | -46.79766 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 88695639-c4c1-3206-addc-7e19a75fc8e9 | -2.10432 | -46.46294 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 068e2373-b422-3fa8-8185-fad34aec9e59 | -2.17986 | -48.3176 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a296654c-2a1f-3bac-b10c-71c43b1403e2 | -4.56172 | -45.59011 | 2024-11-10 04:14:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91ed27c4-778d-31f1-bceb-b51dbb2f14c2 | -1.675 | -52.05497 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9ac5266e-c829-3d85-80eb-7fa89884c1b3 | -3.90071 | -50.29774 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 793f1a66-87c2-3c24-b8f2-4b495293f5bb | -4.10977 | -48.24232 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2b21453-e139-3242-82e5-e1be4434cbf8 | -2.57125 | -48.26176 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e5f048b-12a8-3092-ba86-e4936d898fdc | -3.09503 | -51.11498 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e8fd712-afc2-39de-9778-efaeb0a9b312 | -3.62318 | -50.61593 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| a1b56417-685a-30cb-91f9-6c8188c7e3d1 | -3.98835 | -46.42348 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 2e4f6d78-231c-3351-a990-75763d0e65ba | -5.30347 | -48.36604 | 2024-11-10 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9a5b936-6957-3ae5-8f6e-729198dfe5c2 | -5.25185 | -48.07573 | 2024-11-10 04:14:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| df11ed82-45ff-346e-8603-613414a88471 | -2.20252 | -47.74633 | 2024-11-10 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c471895-e0ee-3f42-8147-1d16ade6c6f0 | -3.58985 | -50.27274 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 93898e44-7616-37bf-8b0d-1f1077ba1a00 | -4.87111 | -42.96421 | 2024-11-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f3b350c-a31c-3ad9-8620-f497491f00fa | -4.63369 | -49.08885 | 2024-11-10 04:14:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4c3195e-1cb1-3b9b-9510-3f47894a20e5 | -1.52613 | -52.20807 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8a277ebb-75f8-342c-b39e-ebe2f4361c29 | -2.23614 | -53.78854 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 59b3a72b-e940-3b4d-9672-5c9077ca490a | -3.031 | -48.04503 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d074b492-b188-3b01-bf21-fb0a2a954b6a | -4.32234 | -44.39202 | 2024-11-10 04:14:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43545a22-48c8-380b-b53d-eefaf0833ff1 | -4.84835 | -48.48742 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0193a778-7fd7-3718-8b41-093564fc88b0 | -5.4516 | -44.82184 | 2024-11-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9399924-6342-3a98-b811-626a4debf4cb | -0.11131 | -51.75849 | 2024-11-10 04:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e73970bf-a84b-3728-b7d1-d1930bf9c8c1 | -2.89833 | -46.81274 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f900693b-0c2f-3e52-b1ca-ea3b7a69b64d | -2.3574 | -46.79952 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 437b7953-6be5-3ee6-a7ea-66e09cd3d918 | -3.95787 | -48.16794 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ad639d61-12f7-3bbe-895c-dbcd40a886d3 | -2.40206 | -48.50317 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7876dd3-896e-323d-850f-b94c807d841c | -4.0903 | -42.92899 | 2024-11-10 04:14:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c303e6f0-fa31-3e1c-95dc-66c116a3c51f | -3.57934 | -50.27641 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 605d7bef-aba5-30f9-b857-fbc8f5a61584 | -5.72206 | -42.67422 | 2024-11-10 04:14:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| a1a35f07-d79e-3728-a2ba-d379b6dad4c9 | -5.84458 | -44.49366 | 2024-11-10 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23b68331-022a-36df-beef-0bf81ae5197d | -3.38883 | -51.46313 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c37951bb-c53b-3551-82a5-2657765e8fd6 | -1.23549 | -54.15705 | 2024-11-10 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0d1aca30-6ea4-39e2-b3e5-78fc39adc73a | -4.05994 | -48.31252 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 103d5d45-b926-37ca-bda5-355b2af59a8e | -1.67914 | -52.05499 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f13c8640-aec1-3103-90b8-09e9314c7f6a | -3.2205 | -50.28025 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| a5cd0926-270f-3910-a412-9f19e0f1727d | -4.10424 | -48.97828 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 25f055d5-fc59-3bdb-8195-7bfef329245c | -3.04592 | -48.0319 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6885250d-0741-3627-844d-78515b16ddd8 | -3.23502 | -50.28267 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 2c28b917-4b21-3ca7-9fdd-a01a84ce8f57 | -2.39075 | -46.78979 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17f91ba2-d51f-3380-8864-405023fd842d | -3.55028 | -49.97971 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0b69d9e4-6918-3aa0-aaaf-02175422c01b | -4.19485 | -51.02109 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a7a47c3-c353-3ca0-95a4-5674cbbf2d22 | -3.6965 | -54.61603 | 2024-11-10 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e438b22-e4a0-3993-9279-bed28b451561 | -2.68636 | -46.80424 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 245acc4b-c4ee-34a8-bbc7-1d20eb04dad3 | -3.57844 | -50.28179 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 14a0dc3c-1de9-3e3e-a29d-28495a13d6bc | -4.20774 | -48.5504 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 883095c2-41a1-39c8-a6b5-6c73418d9c15 | -4.06493 | -50.0112 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3596798b-bfcc-3694-8a2c-16e680b5c400 | -2.71345 | -51.99877 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55d5315d-fe32-30ce-a10c-9ea1bea3369c | -2.25299 | -50.41089 | 2024-11-10 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| eda7df7e-9194-38d0-bf7b-4809700b69ed | -5.24708 | -46.66372 | 2024-11-10 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 32540233-7091-3945-8d46-fdb98b62c5d7 | -2.52283 | -46.36835 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6da1037f-fbb2-3e9e-ad07-fc5933929684 | -4.10512 | -45.70374 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85d61fe7-106a-3d53-a2ac-7dd4773fa2f6 | -5.3045 | -48.36647 | 2024-11-10 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15de2dc5-ecde-3065-b0f0-381d23880779 | -3.68776 | -45.81376 | 2024-11-10 04:14:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f577d708-7b09-3c57-b592-9fa1830a4a18 | -3.22984 | -50.31473 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a3d5099-a0df-35af-88b4-8f040f47a5d8 | -1.42749 | -55.27059 | 2024-11-10 04:14:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 63562f95-32ed-322a-a6ca-6ed836e6a505 | -3.62126 | -47.51944 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db82def4-a9b2-3db4-8c4c-d18ecba35ce6 | -2.24916 | -46.5004 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 484e25bf-8f31-3e4d-868b-03138227b976 | -2.37246 | -48.57576 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad6feed2-70df-305b-ab75-887e02a398ee | -2.24462 | -48.3823 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64d58b79-edde-31b0-b48f-3ff292fb47b6 | -2.52335 | -47.38035 | 2024-11-10 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e022ade3-6dcc-3ed1-b817-11ac32534f6c | -2.62762 | -46.77533 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6400468a-0ce2-3ec9-a9f3-d45326a5d0ae | -3.24357 | -50.31337 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 3a1e963c-b78f-35e1-8fe2-0b09fc5124fe | -2.3159 | -48.53257 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| f38b3654-e667-35d1-a4ef-248f4cf34638 | -2.73388 | -49.01845 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5605590c-f54c-3e34-92d8-51c9c66a99f5 | -2.08471 | -50.34244 | 2024-11-10 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4dfd69ab-6e58-3a80-b181-6439b0c4c486 | -2.2861 | -48.46813 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f13e5ad5-483a-3d41-a198-714eb549b4b9 | -4.90667 | -45.86034 | 2024-11-10 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae3f1e35-7e30-3068-a99c-2ed9f5f82784 | -2.38902 | -46.47747 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dc569c7-9c77-3885-b298-bd74ab5a5603 | -2.08379 | -50.34807 | 2024-11-10 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d15552f9-556b-303e-bfc4-7e2e8a004214 | -4.26693 | -46.91814 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b5adaf4a-b244-3a1f-923e-e5127b8a105a | -2.6524 | -49.40128 | 2024-11-10 04:14:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 288c84ba-1ca8-35ac-8f5b-af443bd0466d | -2.90513 | -45.15075 | 2024-11-10 04:14:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c90f93f3-5ba1-3ab9-a95c-52e6886d25ea | -3.34519 | -50.36265 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 05a0e86e-460d-324e-b4c5-e5e445950f45 | -3.24269 | -50.3278 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0f8975e6-a347-39dc-aa02-dcf901d80401 | -2.51979 | -46.36316 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 563e9bc4-52d3-3247-a143-3bb6e1b6999d | -2.76472 | -49.34906 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 877b80ff-d961-3608-83eb-dc2dc3a55424 | -3.80277 | -52.26512 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f04a58b-d913-3082-a56f-7095bd271dbb | -3.86308 | -52.37752 | 2024-11-10 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7421bb89-4c33-3461-af58-e6a94bf89788 | -2.64701 | -48.63385 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d5ddd77d-c2db-3296-8b6f-0e4fad709051 | -2.57057 | -48.18424 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ad3f877-d488-3c5c-9bf3-01607c6774a1 | -2.68402 | -46.79403 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c52026e2-e4fa-3b2f-9e87-fc98e3948edb | -5.1361 | -47.70904 | 2024-11-10 04:14:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 868899e5-43e2-3853-8e10-b620d0308997 | -1.6744 | -52.05875 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 93fc14d1-475b-3c17-9c8d-226dfec5fbd9 | -2.71404 | -51.9952 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec8b17b3-c81c-3603-b812-a7ba2cc8f155 | -4.05985 | -49.28212 | 2024-11-10 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README29.md)
