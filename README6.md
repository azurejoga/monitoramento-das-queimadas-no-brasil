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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01a480a3-d27d-3d2b-9d5c-cfb140304e4e | -12.7566 | -44.449 | 2026-07-08 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| a334f7ff-7e9b-3648-a405-4c4cc0fa7111 | -8.7267 | -49.446 | 2026-07-08 01:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 7eef944e-5060-3aed-b649-091c96fb6ecd | -12.7373 | -44.4521 | 2026-07-08 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| a497051c-275d-3155-83bc-6dbaafdf0f51 | -9.5534 | -40.3254 | 2026-07-08 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 77.8 |
| 2db558e6-00f9-3a60-977e-e326a424b7aa | -21.3642 | -49.1664 | 2026-07-08 01:50:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.4 |
| f6968da9-391e-352d-a00d-3aa8bf4c2664 | -9.553 | -40.3503 | 2026-07-08 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 71.4 |
| 40bfae4a-cbbc-3650-947b-64b4971c01dc | -12.7566 | -44.449 | 2026-07-08 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 549dd92d-a6de-320a-a02d-00bdf75394fd | -5.6701 | -44.3147 | 2026-07-08 01:50:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 24d9d2bc-3fbc-3b42-a2b3-2052e278fb5c | -12.7373 | -44.4521 | 2026-07-08 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 85598e91-fff7-31a8-bad9-647dbd680b55 | -21.8033 | -56.2729 | 2026-07-08 01:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 2f0f0bb2-cb96-3d7f-9cc1-61a0b6e0f13e | -9.2258 | -48.5782 | 2026-07-08 01:50:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 4c8b9680-2665-324a-afdf-e9013964bec6 | -12.7566 | -44.449 | 2026-07-08 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| b7f91042-e496-3d33-8206-091267f6004e | -12.7373 | -44.4521 | 2026-07-08 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| f367b6a6-0256-3c48-a358-9c796fa4ca27 | -21.8037 | -56.2514 | 2026-07-08 02:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 46.7 |
| d36f2b5a-9144-3d8f-abd2-d0d52bfc2e75 | -5.6701 | -44.3147 | 2026-07-08 02:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 0db33d71-0b62-336b-99f8-6b5bfbb4555c | -21.8033 | -56.2729 | 2026-07-08 02:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 1548168d-ff7f-3f9e-99f6-78848549a862 | -21.3642 | -49.1664 | 2026-07-08 02:00:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.2 |
| 47d57359-cc4c-3644-ae13-ff2b39fb0325 | -9.2258 | -48.5782 | 2026-07-08 02:00:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| aa17434b-6c22-38dd-a4dd-3be33b4c9940 | -5.6701 | -44.3147 | 2026-07-08 02:10:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 3cfed746-6f20-37ba-ae54-f5098e00f324 | -9.2258 | -48.5782 | 2026-07-08 02:10:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 1bb8dfb0-4a20-3e9c-b2bf-f7e41ecb0a89 | -21.3642 | -49.1664 | 2026-07-08 02:10:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 56.9 |
| 4e68556c-3472-3dbc-80b8-aa7c2141164e | -21.8033 | -56.2729 | 2026-07-08 02:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 67.7 |
| b76740ee-2a29-39ca-bfbb-8292ae80bc3d | -12.7373 | -44.4521 | 2026-07-08 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 024a9bda-6b09-30e5-92c0-6363ee2523f1 | -12.7566 | -44.449 | 2026-07-08 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| e63b58bf-74a2-366c-aacb-ce92d2c62efd | -12.7566 | -44.449 | 2026-07-08 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 28747016-3230-381b-b1de-1c0c31df67cf | -9.2258 | -48.5782 | 2026-07-08 02:20:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| b84667c4-aa83-3eff-985b-4c2ffe2b41fe | -21.8033 | -56.2729 | 2026-07-08 02:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 865b24b0-bd9c-357e-9bf4-6b3c99985676 | -5.6701 | -44.3147 | 2026-07-08 02:20:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| ea877422-6a99-32c6-abfe-1994612efe71 | -9.2258 | -48.5782 | 2026-07-08 02:30:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 0b44dc38-2707-3561-a0dc-0b0a616de510 | -21.8033 | -56.2729 | 2026-07-08 02:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 2e784e3a-e268-3a6d-98f9-0d08e8bb810d | -12.7566 | -44.449 | 2026-07-08 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 03768142-661f-39be-97c8-e46f4302669a | -9.2258 | -48.5782 | 2026-07-08 02:40:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 040ca1b3-ad7c-3fda-b98c-69f8b1958d24 | -12.7566 | -44.449 | 2026-07-08 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 03a5d2b2-f120-3e94-a6b5-b2265cb509b4 | -12.7566 | -44.449 | 2026-07-08 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 5141e750-d49b-30ac-97d9-d001acb6789f | -5.6701 | -44.3147 | 2026-07-08 02:50:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 4daf6b62-6ad1-350e-aeec-3fbb60459b4b | -21.8033 | -56.2729 | 2026-07-08 02:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 939be257-163c-315a-8c15-f0a600741b91 | -9.2258 | -48.5782 | 2026-07-08 02:50:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 4f1665ea-0bcb-33d6-bf10-f11b91a7ecdc | -12.7746 | -44.5162 | 2026-07-08 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 9d30d7f7-5517-31c0-83fc-36fadd62270f | -21.8033 | -56.2729 | 2026-07-08 03:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 7c3769e3-2ce3-342b-aa1e-f56581f757b0 | -9.2258 | -48.5782 | 2026-07-08 03:00:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 650ba0e3-5ee4-35f6-8fca-7cd79ef5889b | -12.7553 | -44.5194 | 2026-07-08 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 055737e5-43b6-38f1-b256-bba71eb75f13 | -12.7566 | -44.449 | 2026-07-08 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 495271ee-1d6f-3467-966c-94a6bee6eac4 | -12.7548 | -44.5428 | 2026-07-08 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| beddfcb5-2f16-3101-b9a2-4edfd270c347 | -12.7566 | -44.449 | 2026-07-08 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 2d7dd5c1-53be-3539-bf6a-ff33f04d1633 | -9.2258 | -48.5782 | 2026-07-08 03:10:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 5b23b77a-4310-3a8a-982b-0db3cc3e3379 | -12.7553 | -44.5194 | 2026-07-08 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| eb6f3e5a-b473-37da-a223-d069e073bd68 | -12.7548 | -44.5428 | 2026-07-08 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| b3635648-f4e1-376b-9129-2f5fc0b33ed3 | -21.8033 | -56.2729 | 2026-07-08 03:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 50.7 |
| bffc1a20-5f0c-3d27-a885-0556fdc0c22a | -9.2258 | -48.5782 | 2026-07-08 03:20:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| d220cee9-106c-3c7a-801e-5c794b0f7573 | -12.7566 | -44.449 | 2026-07-08 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| e5a3d3f2-5423-32a2-92a7-2a437a989d04 | -12.7949 | -44.4661 | 2026-07-08 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 006e856f-fb50-3360-a005-dd28ba7c255c | -12.7553 | -44.5194 | 2026-07-08 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| c50434a5-6c4d-3668-8d04-b48d84276b69 | -12.7953 | -44.4426 | 2026-07-08 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 9cf1b601-028b-3e3d-8fd1-af1d86acc0cb | -12.7953 | -44.4426 | 2026-07-08 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.0 |
| ce83b783-f788-3ddb-9633-9f0c1bc493d6 | -12.7746 | -44.5162 | 2026-07-08 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 509e1ecc-f868-30b7-96c8-cf4d1213eb64 | -9.2258 | -48.5782 | 2026-07-08 03:30:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 6fb1d938-3c38-3b91-8c72-f4dd170ce721 | -12.7566 | -44.449 | 2026-07-08 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 95f6fbb4-9235-380f-8598-1b45839b1785 | -12.7553 | -44.5194 | 2026-07-08 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 27ab335a-0d6e-354f-bc97-a744b6dd9c06 | -5.46969 | -45.42659 | 2026-07-08 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ef62ef96-986d-3dc5-ade3-1c6bf5b53de7 | -7.00617 | -42.77108 | 2026-07-08 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e3fc4b24-8431-3256-bf59-c96d0a825210 | -6.93044 | -43.696 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c99315ca-0605-395f-bae3-3ea5d2164dd5 | -6.93419 | -43.70123 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c222887-c848-37b0-8dce-4fa607ca8dee | -4.83402 | -44.06626 | 2026-07-08 03:30:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 58c96b93-e781-3ef8-b5cb-07b06984f42e | -6.9466 | -43.70358 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 01917f6d-7198-3e18-86e2-c925b092d457 | -6.94821 | -43.70424 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3689f670-9838-39cf-8571-187184971d03 | -5.98149 | -43.62151 | 2026-07-08 03:30:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d087cc9b-cc48-3ff7-a906-2ab70bd1f0c8 | -6.93493 | -43.70665 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4e5470e3-88a0-31d9-9cad-f7853d29895b | -5.66247 | -44.30333 | 2026-07-08 03:30:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ac3f1d28-a816-32aa-b2ae-0ed4b61f67e7 | -6.94113 | -43.70786 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 54ae1696-b278-39b0-a5c0-e1baea5eb9be | -6.49652 | -42.21464 | 2026-07-08 03:30:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| a31a7443-4230-377a-91b0-2cfae22e60a5 | -6.92958 | -43.70076 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 80e8f77e-130a-3d90-be6f-947d4947e134 | -5.6615 | -44.30882 | 2026-07-08 03:30:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 003716e7-59d8-3357-9e10-d89d271a0079 | -7.01051 | -42.78693 | 2026-07-08 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8fce7a73-082c-3566-9c3f-cc188d592d12 | -5.66345 | -44.29783 | 2026-07-08 03:30:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b8afa299-5d7b-38b6-bc05-f066c29aa604 | -5.66529 | -44.31682 | 2026-07-08 03:30:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2832198a-0687-3502-962d-436fdd6c2141 | -7.00772 | -42.76857 | 2026-07-08 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7c97d8a0-f99e-3db0-8cbc-079159633d19 | -5.79942 | -43.8004 | 2026-07-08 03:30:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 450f7935-ff83-3834-8770-611804c9745e | -6.92784 | -43.71037 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9bd08713-5971-3b86-96bf-d84fc98e1cef | -6.64997 | -43.91547 | 2026-07-08 03:30:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53a63e09-69d2-39dc-a175-b22acc97f38f | -5.80038 | -43.79508 | 2026-07-08 03:30:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8c327812-4b89-3559-b55a-a300c8b14457 | -6.92073 | -43.71411 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5a88cfa0-659a-3f13-803c-7a85eefc1e5e | -5.83125 | -43.48058 | 2026-07-08 03:30:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 146b9d74-e015-3bed-986d-ba3e6b899aee | -6.90918 | -43.70696 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cb3bb69d-85e5-3884-b437-5f7957f07ed6 | -6.50295 | -42.21158 | 2026-07-08 03:30:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| ca9a92c3-bc90-38c8-902e-38a56362a0e5 | -7.01129 | -42.78257 | 2026-07-08 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 95b15718-beec-36ce-b29f-5336638a6030 | -5.66051 | -44.31441 | 2026-07-08 03:30:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 714bf049-8931-37e7-9301-6642f080c91d | -6.94201 | -43.70303 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 02a91c29-fe95-3c91-9fb6-5e0290aa004d | -5.79847 | -43.80568 | 2026-07-08 03:30:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1f2257b4-ead9-309c-8def-762922fcbdea | -6.93329 | -43.70601 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef959b5b-3d89-3c70-81ee-66acc58953f0 | -5.98399 | -43.62303 | 2026-07-08 03:30:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 48466793-a358-3171-ab02-270a22571978 | -6.92871 | -43.70553 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 88cc287d-625c-35c9-968e-1eed04f95345 | -5.65974 | -44.31007 | 2026-07-08 03:30:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 34c1ad97-63c5-3082-8f74-da6535bb05ec | -5.46738 | -45.42655 | 2026-07-08 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f7bf84df-b0d9-36bc-b728-be3e2dbc853e | -6.94569 | -43.7084 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f85d0cca-3224-3edd-9015-16775cb06fd8 | -6.48935 | -42.22181 | 2026-07-08 03:30:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4743d897-2d04-3994-a975-a4d164b14e9d | -6.92797 | -43.70014 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99b2136f-8b1b-316c-8667-07d5e6c2a810 | -6.91983 | -43.71906 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b74d7628-01d5-3d78-be9d-bc8c5404e02c | -6.94751 | -43.69869 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3a8ac6a3-0d07-328b-a5de-77d4ce5d79df | -6.9358 | -43.70184 | 2026-07-08 03:30:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 439595b8-a4db-31b2-979a-12adee0506c3 | -5.66075 | -44.30456 | 2026-07-08 03:30:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |


[Clique aqui para ver as próximas entradas](README7.md)
