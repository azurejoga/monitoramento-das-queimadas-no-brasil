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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2fc41480-a430-32c4-84cf-4e7a7ebf30f8 | -2.825 | -46.722801 | 2026-08-08 00:12:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ddb3f61-20a3-34a5-96d4-e9f1805fe434 | -3.9581 | -48.122101 | 2026-08-08 00:12:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5b67f2e-7a98-3193-bfb9-fe9fb09b298c | -7.1632 | -44.060902 | 2026-08-08 00:12:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 18773a3b-4d21-352b-a7ca-003d073029a9 | -7.165 | -44.068901 | 2026-08-08 00:12:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c6b358fd-0cc9-31a9-a537-15bc3c0b1e06 | -12.5561 | -46.930801 | 2026-08-08 00:12:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ddb91ea2-fd9d-38f4-a37a-b0ad7cb30652 | -6.7263 | -48.1171 | 2026-08-08 00:12:00 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 44b841c2-a1b1-361b-8964-8bf50d4cc3d1 | -6.9783 | -41.493698 | 2026-08-08 00:12:00 | METOP-C | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 58dced96-f86d-393a-a4f8-d09d15014a1f | -14.9298 | -48.270699 | 2026-08-08 00:12:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 634d4fe4-36cd-3de0-bd09-6fade5f812f2 | -8.1205 | -45.905102 | 2026-08-08 00:12:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1fb84f15-1762-330a-bd2e-1789126ffca6 | -9.3736 | -40.330101 | 2026-08-08 00:12:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4d601d9e-264f-33a7-aae3-8c6f30b82694 | -7.1806 | -42.3419 | 2026-08-08 00:12:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 72ed317d-acfa-35f0-b55e-4b20817fd50f | -13.9586 | -41.876999 | 2026-08-08 00:12:00 | METOP-C | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ea98b989-a281-358d-b2ef-a00820d11d64 | -4.2621 | -48.201 | 2026-08-08 00:12:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cdf7d72-0e61-32d6-bd3b-225b1e167b4c | -4.2663 | -48.173599 | 2026-08-08 00:12:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d412c46-b970-3503-b5dc-da5be23ecdc1 | -11.3106 | -44.840099 | 2026-08-08 00:12:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eca97727-9017-3ed2-a21c-ab84f326ee91 | -4.164 | -48.775501 | 2026-08-08 00:12:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec31fb88-eed1-3aa5-9e60-20e117107a96 | -20.057199 | -40.8946 | 2026-08-08 00:12:00 | METOP-C | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ae00f6cf-878c-3e45-91ab-eeb2f0dfb963 | -4.6382 | -43.126801 | 2026-08-08 00:12:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ee959ae-55f8-3fec-b9d3-079464bc1ab6 | -13.3928 | -41.353199 | 2026-08-08 00:12:00 | METOP-C | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 02470f47-7d08-3c40-9d18-c8945680c873 | -14.9263 | -48.251999 | 2026-08-08 00:12:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 901fc7e8-73b1-3989-bda7-9b6c884783d1 | -11.0278 | -44.279099 | 2026-08-08 00:12:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5f7283f6-3e25-3782-9f88-6412022c1cc9 | -2.878 | -40.298901 | 2026-08-08 00:12:00 | METOP-C | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 837dc449-6333-3f07-b088-a8cc29f7d4fa | -11.0376 | -44.277 | 2026-08-08 00:12:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 89ef5652-dcd5-32f3-a41f-d1e7c6506324 | -11.1537 | -45.944698 | 2026-08-08 00:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 92fca99a-549f-3704-b612-f558a3dfbae4 | -6.922 | -42.428799 | 2026-08-08 00:12:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ad9c26a5-0a49-3854-b901-c55ed2f8e5a9 | -3.0509 | -39.930801 | 2026-08-08 00:12:00 | METOP-C | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 0ece6f9e-8b34-3d72-8a13-934519fe474c | -6.9783 | -42.908401 | 2026-08-08 00:12:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2134c9a9-f5ad-3815-968e-192e4013d940 | -12.5464 | -46.9328 | 2026-08-08 00:12:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bf0a3596-4ec2-3f11-b606-3d0df3c3252e | -13.383 | -41.3554 | 2026-08-08 00:12:00 | METOP-C | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7c4d79cb-2b69-3643-81b7-77c58a2000ad | -3.9651 | -48.1077 | 2026-08-08 00:12:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a70fa0b8-ee24-3b1f-899f-47cdef299ac6 | -11.2851 | -55.862 | 2026-08-08 00:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| c4353ff4-298d-3f63-94c4-4cefa605f1e0 | -4.2634 | -48.2016 | 2026-08-08 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| f73892e6-efa7-38ec-b752-beb0d4f64b1d | -4.2635 | -48.1799 | 2026-08-08 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 96d766c5-847b-3684-88ac-de3b72d6170c | -11.2662 | -55.8635 | 2026-08-08 00:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| fa1defc2-cb65-326d-bb8a-4b6d90dd2435 | -11.0334 | -44.2696 | 2026-08-08 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.3 |
| f9ea074b-1421-3eb0-ae73-fbdf5e01ba83 | -11.0526 | -44.2668 | 2026-08-08 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 45.2 |
| c037b807-5504-3a8b-8819-b3313255f171 | -3.9671 | -48.1283 | 2026-08-08 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| c6682b18-f4cc-3bd2-96dd-b73a3b753147 | -9.3817 | -40.3252 | 2026-08-08 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 99.4 |
| f27d26b7-1cbe-30b7-bdc9-92a82be8e3e4 | -11.2662 | -55.8635 | 2026-08-08 00:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 47b2e45c-8930-351b-8192-d8926b65da05 | -4.2635 | -48.1799 | 2026-08-08 00:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 839e7ee8-c4ef-3d45-b1ac-da4b08d55eba | -11.0334 | -44.2696 | 2026-08-08 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| ac51f6a7-eaa4-3237-ace4-1e92c5920eee | -15.748 | -49.9586 | 2026-08-08 00:30:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 14c6b007-d518-3887-a6dc-f517eadfe3f5 | -15.7475 | -49.9806 | 2026-08-08 00:30:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| c433d481-7108-317b-a524-edbcb3801983 | -4.2634 | -48.2016 | 2026-08-08 00:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 249607f2-1356-3bdd-9619-10c457d08db9 | -4.2634 | -48.2016 | 2026-08-08 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 0fd3a2ea-cb60-3e7b-9964-6ec481d06aca | -4.2635 | -48.1799 | 2026-08-08 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 4a6c4c2a-99df-3720-b0e6-89255731ed9b | -11.2851 | -55.862 | 2026-08-08 00:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| e59249a5-c04c-3b09-9af0-90a65e4df303 | -14.3617 | -54.9701 | 2026-08-08 00:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 0688ec3e-9d2f-3fd4-87b3-9d9123085429 | -11.0334 | -44.2696 | 2026-08-08 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 5570d153-2c9a-3c73-910a-eb42ead55d76 | -11.2662 | -55.8635 | 2026-08-08 00:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 9dee9877-3432-34f1-9ba0-9ccf5f9cf3a2 | -14.3617 | -54.9701 | 2026-08-08 00:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 8e0272d0-60a4-3c4b-8994-6e0b924bdfa3 | -4.2634 | -48.2016 | 2026-08-08 00:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| a3529e36-559d-3760-ade4-32fda4068e81 | -4.3774 | -47.7627 | 2026-08-08 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| c0cc0a94-4514-39ee-8423-6b4d6c5bb27c | -11.0334 | -44.2696 | 2026-08-08 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| a9e34036-fdf3-35a4-b849-94db47d14ee8 | -11.2851 | -55.862 | 2026-08-08 00:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| cc352cd5-e7b8-339e-8395-2f75e45fd788 | -11.2662 | -55.8635 | 2026-08-08 00:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 4f64176f-be2a-36d4-bbee-eeb1b1249e74 | -4.3588 | -47.7636 | 2026-08-08 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 181be11c-5e09-3681-abb3-20c81ee377e9 | -4.3774 | -47.7627 | 2026-08-08 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 708de987-0714-3b00-a7ef-039bc735fb8e | -4.3588 | -47.7636 | 2026-08-08 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 5ebee1cb-fe00-37a9-a5c6-c621dc72bba3 | -11.2662 | -55.8635 | 2026-08-08 01:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 327997d1-63f8-38ce-afcd-beb0318a1046 | -11.2851 | -55.862 | 2026-08-08 01:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 66fc7ec0-81e2-3e0a-8ee5-b4bab1b1947c | -4.2634 | -48.2016 | 2026-08-08 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 88402374-ab6c-3082-8df3-111582f70005 | -10.2662 | -45.7979 | 2026-08-08 01:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 43.3 |
| e72f1fdd-7e79-34e7-8275-0d2cfe9777e8 | -11.0334 | -44.2696 | 2026-08-08 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 8a25779e-4f4c-3fbd-8055-66d63a5894fe | -9.3817 | -40.3252 | 2026-08-08 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 64.6 |
| 3bf32b9a-6f75-3dbe-aa7d-69411683665b | -9.6254 | -40.5875 | 2026-08-08 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 4bbda2eb-dce2-3dc4-8f45-db9a4eca22ec | -12.5562 | -46.9357 | 2026-08-08 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| a3ce13f6-395c-3e12-b74a-00d0b2a3f3e1 | -15.38599 | -53.81532 | 2026-08-08 01:09:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 1729a828-0943-37ce-8d68-935bdd464885 | -14.15256 | -53.98048 | 2026-08-08 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 0dd44673-6f4f-3e67-ae28-1694b904b2c0 | -15.38829 | -53.80964 | 2026-08-08 01:09:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 9960698e-c8e3-3580-9088-a19450d3bb38 | -14.15201 | -53.98604 | 2026-08-08 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 3da0cdd6-6ef2-30e7-86ff-72d7e834a683 | -11.0334 | -44.2696 | 2026-08-08 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 9e5e0f76-3d89-3fb4-8436-9ec5bf65f584 | -9.3817 | -40.3252 | 2026-08-08 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 71.6 |
| 1d55ddc9-0be4-3f04-8007-8d3043076ebe | -4.2634 | -48.2016 | 2026-08-08 01:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 81245bb7-f40f-3783-8089-34d37170a680 | -4.3774 | -47.7627 | 2026-08-08 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 143e7fe4-7b52-3205-9bf3-436e698fb90a | -4.3772 | -47.7844 | 2026-08-08 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 198a2528-877b-39c7-a586-8b65eb3b0566 | -11.2662 | -55.8635 | 2026-08-08 01:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 15f87b3b-5945-3a59-b762-ce6c547342e1 | -11.2851 | -55.862 | 2026-08-08 01:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 12587bb8-0dbd-3b15-b21e-1be015e8059f | -7.55218 | -61.16133 | 2026-08-08 01:11:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 80ae3dd1-c001-349d-84b6-eded53397e47 | -11.27412 | -55.88163 | 2026-08-08 01:11:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 3691e13f-6676-35b5-807f-58bca95384c5 | -11.26789 | -55.84689 | 2026-08-08 01:11:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 3f9f4299-9f98-3e2f-9477-41205156d6a9 | -11.28224 | -55.88701 | 2026-08-08 01:11:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 401d9db1-c6aa-35f5-9223-3b41a2f41022 | -6.89274 | -59.89645 | 2026-08-08 01:11:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 9c8882d4-1ec7-3949-b6ac-8caef54af6e2 | -6.7192 | -58.9396 | 2026-08-08 01:11:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| fd85798f-7ed4-331e-ab6c-599e312629b5 | -8.78338 | -64.21149 | 2026-08-08 01:11:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| f9506c57-444f-3586-9d8b-1bb834d1bfa1 | -6.89304 | -59.90195 | 2026-08-08 01:11:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.9 |
| d58e3546-efc4-3511-8627-781d2fa8b741 | -8.78474 | -64.22105 | 2026-08-08 01:11:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 29a496df-d806-31ad-8e44-c72b3149aef5 | -11.26027 | -55.8554 | 2026-08-08 01:11:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 4ca035e6-23e0-3924-8856-a52ff3954e08 | -7.55283 | -61.17007 | 2026-08-08 01:11:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| f5ce2749-0520-39a4-a205-8cc48e8ed28e | -6.2856 | -64.15367 | 2026-08-08 01:11:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 35.8 |
| dc8518cc-f929-3f78-81c1-2144f47c6b00 | -8.6815 | -62.86905 | 2026-08-08 01:11:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 22.7 |
| b8ec48a0-ad7c-3555-abe5-10ae457269db | -6.70546 | -58.94209 | 2026-08-08 01:11:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 2519a2b2-d091-36f9-9246-8f9e3a551e0a | -7.55049 | -61.15497 | 2026-08-08 01:11:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 6b959cf6-8e50-3c79-8167-cdb4b0d7155b | -11.27638 | -55.85284 | 2026-08-08 01:11:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 3d510609-9108-3c2c-a2bb-5cc07f1d5d7a | -8.7628 | -64.06725 | 2026-08-08 01:11:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b8df93c8-1945-3838-83cb-78d841c6d870 | -10.82556 | -65.09418 | 2026-08-08 01:11:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d2fc1b72-8b33-38be-94c4-f4a2c5982769 | -6.70909 | -58.96539 | 2026-08-08 01:11:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 3c82e95f-ea53-384b-ae1f-a68ad29d112c | -4.2635 | -48.1799 | 2026-08-08 01:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 21c985c4-b641-3ef5-988b-dca655e06672 | -11.7205 | -50.1241 | 2026-08-08 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 89d035f7-6b64-32fa-8fab-0804869ce8ee | -4.2634 | -48.2016 | 2026-08-08 01:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |


[Clique aqui para ver as próximas entradas](README3.md)
