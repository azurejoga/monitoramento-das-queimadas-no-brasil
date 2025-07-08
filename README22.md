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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12ba2040-f9f7-3cf8-ad16-4d27947fb711 | -11.4397 | -45.0923 | 2025-07-08 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 5291c2ab-ff7f-37d6-a87f-a1378ab6aacc | -11.4393 | -45.1154 | 2025-07-08 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| cce99617-63d6-3953-a830-fbb4488c7cad | -10.6299 | -49.4504 | 2025-07-08 13:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| c0787d47-63e5-374f-9a3b-19131462eb8c | -10.6049 | -52.7952 | 2025-07-08 13:20:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 118.3 |
| c6a17487-7920-35d3-af47-0b6d4f9d1b50 | -11.4584 | -45.1126 | 2025-07-08 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 04533e5d-0dee-343a-b60a-a2a94241685a | -11.4588 | -45.0895 | 2025-07-08 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 8192bb8a-3eab-3a90-ba17-4b571edc33b4 | -11.4588 | -45.0895 | 2025-07-08 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| b49fa366-09c4-3825-883e-06c2bf9d2af7 | -10.6299 | -49.4504 | 2025-07-08 13:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 77da799a-0632-38b4-8e35-4d6b1da2bc0a | -8.1469 | -47.6318 | 2025-07-08 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 4861c697-1c10-334c-9578-6c36d3a8415c | -11.4393 | -45.1154 | 2025-07-08 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 0f7dd847-c6bf-39b5-a3e8-dab71fd7c28b | -11.4584 | -45.1126 | 2025-07-08 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 172.4 |
| 9c40f1ed-aec3-31ce-b5b3-fab4fe5f46f0 | -11.4397 | -45.0923 | 2025-07-08 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 7d1c9452-d107-3652-af01-609c4dd76d82 | -5.2575 | -44.4581 | 2025-07-08 13:40:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 39b0d1b0-c2c7-3f9b-8daa-7e29b2e0c60e | -11.4393 | -45.1154 | 2025-07-08 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 124.0 |
| ede7dd63-4c0a-39ba-874d-062d670f2491 | -11.4588 | -45.0895 | 2025-07-08 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 63e38651-a1fd-3000-8ac2-ba44c80732b1 | -11.4584 | -45.1126 | 2025-07-08 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 157.3 |
| e9729873-afd7-3bd6-882d-c21e4836cd90 | -11.4397 | -45.0923 | 2025-07-08 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 0734cf08-93c0-3abb-98c8-c5b298ea1bcf | -10.6299 | -49.4504 | 2025-07-08 13:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 6896b136-b38d-32d9-9d3a-8a59e8e82a11 | -7.8302 | -44.196 | 2025-07-08 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 909010ea-153f-3032-a7e5-54d035e79c00 | -6.3158 | -45.3366 | 2025-07-08 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| beef8393-596f-32fd-a661-ae5400ee7328 | -5.2575 | -44.4581 | 2025-07-08 13:50:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| ce23eebd-5c11-3346-8960-b49089cd4b49 | -11.4397 | -45.0923 | 2025-07-08 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 2c8201c7-47f8-380b-817d-dfc286c4c250 | -15.2502 | -51.533 | 2025-07-08 13:50:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 125.2 |
| eef7ab84-2425-3418-a31a-54f88b7ad7bd | -11.4588 | -45.0895 | 2025-07-08 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 3ab86500-ea4e-383d-ac5f-d3c938d1fc9b | -8.1469 | -47.6318 | 2025-07-08 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 4547a80d-41f9-3b2c-9835-8b1197a95f92 | -10.6299 | -49.4504 | 2025-07-08 13:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| b56f1abd-7438-30c2-92e8-85c6061df9bd | -11.4584 | -45.1126 | 2025-07-08 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 166.9 |
| 1acffdfc-269c-3ec7-bc1b-e2676a78f2b5 | -11.4393 | -45.1154 | 2025-07-08 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 85344dc4-47a1-33cd-b8a9-c2042f55ce99 | -8.3802 | -43.9527 | 2025-07-08 13:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 9c1534f6-3bd2-31b0-a6ff-f268147a44fa | -10.34 | -49.9118 | 2025-07-08 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| b4512d7b-88f6-37a8-be72-21630496368d | -11.4393 | -45.1154 | 2025-07-08 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 154.9 |
| e801fcc6-1189-37dd-821d-5b1d1f2cbb9d | -6.3158 | -45.3366 | 2025-07-08 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 5a93811f-8610-3e76-b8b1-017bcf946817 | -8.3802 | -43.9527 | 2025-07-08 14:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 0b4dba51-7ed0-3f29-8b2e-7c8d64913b83 | -15.2502 | -51.533 | 2025-07-08 14:00:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 139.2 |
| db5e028c-908d-3cb0-ba3b-c7735b9bf59e | -7.0079 | -43.6963 | 2025-07-08 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| f66fff87-25a9-3230-8240-ab900d3c82d4 | -11.4584 | -45.1126 | 2025-07-08 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 165.7 |
| f14d1b6b-53c0-33af-9038-12f0531e09ba | -10.6299 | -49.4504 | 2025-07-08 14:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 24146952-df36-3e59-8965-c52f0ce1caa6 | -6.9888 | -43.7213 | 2025-07-08 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 549606d9-5155-33c3-974e-f101daa86e86 | -7.0076 | -43.7195 | 2025-07-08 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 561f5630-9c09-3ee9-a203-c5ab8990dd3b | -8.1469 | -47.6318 | 2025-07-08 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| b1d29f74-1ada-3d3a-af18-baf21f740be3 | -11.4397 | -45.0923 | 2025-07-08 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 096a37c1-100e-34c7-87b1-5d8a5a7f4d77 | -11.4588 | -45.0895 | 2025-07-08 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 2eb378ab-5952-3091-af3a-3c09c83c55a4 | -5.2575 | -44.4581 | 2025-07-08 14:00:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 7d9975e3-897a-39c9-b7c1-489c35daeca6 | -10.3589 | -49.9098 | 2025-07-08 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 5f2f1c89-4042-387b-8197-66512875112e | -5.2575 | -44.4581 | 2025-07-08 14:10:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| cd06d1d3-cb98-3cd6-aaa2-6c74a87222ea | -15.2502 | -51.533 | 2025-07-08 14:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 41eb48ce-7d0a-32e8-8ad2-8be51daa5d87 | -11.4393 | -45.1154 | 2025-07-08 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 187.3 |
| 84f18305-348f-301c-8083-957e90048fa2 | -10.6299 | -49.4504 | 2025-07-08 14:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 9a90efbb-68b4-312b-bb15-1c6fe06ac6c2 | -6.3158 | -45.3366 | 2025-07-08 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 70ee9207-54a7-3bc0-a288-39579cd45217 | -6.9888 | -43.7213 | 2025-07-08 14:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 033b7d2e-0f48-37c0-be9b-a0a1ccac89ff | -5.6065 | -45.1852 | 2025-07-08 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| de2a50cd-a688-327f-8f62-02e11ac8e12e | -10.34 | -49.9118 | 2025-07-08 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| c8c88f1d-6548-379b-9ec5-2ed0b3baa7be | -8.1469 | -47.6318 | 2025-07-08 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 8b8f70b8-836e-384c-acf7-2cc62a22916c | -11.4397 | -45.0923 | 2025-07-08 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 680528b9-7f35-32e5-83bb-3e0f2d038102 | -11.4584 | -45.1126 | 2025-07-08 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 79e2fb70-498d-3fc1-81ca-e6517c532687 | -11.4588 | -45.0895 | 2025-07-08 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 28b485f1-ae63-3268-b9b4-fdd830ee3d7e | -6.6376 | -43.1698 | 2025-07-08 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 9457de0e-b57d-353a-b817-b1dc5b39022c | -15.2697 | -51.5302 | 2025-07-08 14:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 001ca8ee-84ff-3981-a80a-0d02b7f31d12 | -11.4397 | -45.0923 | 2025-07-08 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 0471a295-5829-351c-9285-c5316e47af06 | -11.4584 | -45.1126 | 2025-07-08 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 212.1 |
| c682c5c3-f51c-313b-a5d2-8ab7f0342d5f | -11.4588 | -45.0895 | 2025-07-08 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 63e0b44b-17b8-3945-acce-8be1d2b8235a | -5.2575 | -44.4581 | 2025-07-08 14:20:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| f8c05e50-cf9c-30d4-a5ca-c692a44b2543 | -6.9888 | -43.7213 | 2025-07-08 14:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 57b0ff89-1b6d-3956-af26-78f8ca91d3fb | -5.6065 | -45.1852 | 2025-07-08 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| a09d228c-86f9-33e2-890d-2c75bf76f5d4 | -15.2502 | -51.533 | 2025-07-08 14:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 99.5 |
| b5c9f907-7e33-3403-9000-4d6ea19c7ff8 | -10.34 | -49.9118 | 2025-07-08 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| e228abda-a6de-33f0-a601-03b68785080a | -10.3589 | -49.9098 | 2025-07-08 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 6b73465d-6e23-388b-b7f0-e6d6b596cf44 | -10.6299 | -49.4504 | 2025-07-08 14:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 8b571b48-2595-3404-b2fb-7eb70676b7fa | -6.3158 | -45.3366 | 2025-07-08 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| fb7097bb-9e6d-3384-b512-f57402caf97d | -8.1469 | -47.6318 | 2025-07-08 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| aa446f52-5fa6-3a41-999b-69abe684c8ef | -15.2697 | -51.5302 | 2025-07-08 14:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 68.4 |
| b1aec180-5cfa-3332-a713-9f98f87007d9 | -7.4702 | -44.3928 | 2025-07-08 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 7493e868-3501-3184-af7a-0d8ca6f41a48 | -8.1469 | -47.6318 | 2025-07-08 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 97084eac-cc04-3994-a179-20d16f969420 | -11.4397 | -45.0923 | 2025-07-08 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 4a421801-036a-36cd-9434-45ff5a2e319a | -15.2502 | -51.533 | 2025-07-08 14:30:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 95.2 |
| c0b2bac8-0dcc-343f-a310-8483d681fae6 | -11.4588 | -45.0895 | 2025-07-08 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 138.5 |
| a93114e3-805a-394d-ad13-c1afe7c532b7 | -10.6299 | -49.4504 | 2025-07-08 14:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 114.5 |
| b2ae2323-0d3f-3f93-be10-df97c457cc4f | -10.34 | -49.9118 | 2025-07-08 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 4141af08-2e08-3608-8774-f60b92a637a1 | -5.2575 | -44.4581 | 2025-07-08 14:30:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 086a3fd6-f4ce-355f-a545-df8c2edd6a63 | -10.3589 | -49.9098 | 2025-07-08 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| caff32b7-2d0e-362e-8b70-9de186ddd951 | -6.9888 | -43.7213 | 2025-07-08 14:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 7f0d2472-04d6-38ba-b86b-fb6807d2b5a8 | -5.6065 | -45.1852 | 2025-07-08 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |


