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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a7a3116-8dbb-321b-a641-431ade6c422e | -13.88035 | -53.98004 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16035f48-1c8b-3af8-82da-14e6cd363025 | -17.92008 | -44.41304 | 2026-08-22 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| efb86fb4-7472-3204-b1d9-34ed48a06c1e | -15.744 | -56.53961 | 2026-08-22 04:29:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13ac80c2-b716-34de-9fab-c0cf1864497e | -18.34076 | -42.46334 | 2026-08-22 04:29:00 | NOAA-21 | JOSÉ RAYDAN | MINAS GERAIS | Brasil | 3136553 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| de2f084e-c853-3dbb-a0e3-471221a839ce | -18.75924 | -43.80762 | 2026-08-22 04:29:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7f15ca77-2e9c-3f83-9198-a39396114f79 | -16.0315 | -52.17175 | 2026-08-22 04:29:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| faca266e-ff54-3c7b-88ad-6edaf210e198 | -14.55913 | -53.00596 | 2026-08-22 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45820735-5405-3fd8-96fa-959dc1b8a0ba | -16.31101 | -53.1641 | 2026-08-22 04:29:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31c3f637-3395-39fc-9274-8b37d381d084 | -13.82037 | -53.99835 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 94a37275-6915-3ee3-9c46-e7ffb0863130 | -17.00981 | -46.68177 | 2026-08-22 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf96e506-2173-3ec4-9eb6-9b6e0f6ea2d7 | -16.66577 | -49.14709 | 2026-08-22 04:29:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 743e67ea-fd26-3f61-8a61-b085dfd577f9 | -14.55822 | -53.01115 | 2026-08-22 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7473d8d-3b9d-3848-9ab3-f6cfbfa6f674 | -19.74958 | -45.10662 | 2026-08-22 04:29:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3265d40a-0c35-3bdd-8a4a-3c5e54c28d07 | -16.60412 | -50.79615 | 2026-08-22 04:29:00 | NOAA-21 | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c4556fa-bebc-3acb-8942-fa1c6f07fb01 | -14.01188 | -53.70584 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d51d43dd-bb2b-374b-a611-9d88a7527e4b | -16.03073 | -52.17621 | 2026-08-22 04:29:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5b204205-2463-3fe2-b440-ab01f408b79d | -18.534 | -48.25205 | 2026-08-22 04:29:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 426418f8-4e27-3ff2-86c5-a207457282e2 | -19.74642 | -45.10106 | 2026-08-22 04:29:00 | NOAA-21 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fdf23b01-6167-3948-8cf7-36dd6010b86f | -13.8787 | -53.98865 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b11be5e4-ea60-3661-aa13-81e08a555e2d | -14.56098 | -52.9955 | 2026-08-22 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5df27df8-8b65-3302-99b6-0084e88d76bf | -18.69574 | -52.25154 | 2026-08-22 04:29:00 | NOAA-21 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c78db093-ce91-3072-8ae8-eea811c9728d | -20.43848 | -46.48681 | 2026-08-22 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f5ee9c75-f6bc-38c7-bdb0-d59b64117a5a | -14.39929 | -51.80381 | 2026-08-22 04:29:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 6a750055-36da-3752-8a74-52d485915711 | -19.6707 | -46.04144 | 2026-08-22 04:29:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0efc9940-de82-3a10-8ecc-485d2022867c | -14.43263 | -52.92273 | 2026-08-22 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3444d131-7b79-3d21-9867-745909fe9e59 | -16.49784 | -55.18786 | 2026-08-22 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7342afef-66d0-3b83-a579-926344f1ed3b | -13.9961 | -53.67503 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b78d7711-d886-3986-8e5a-40809d980dfc | -15.24873 | -52.84836 | 2026-08-22 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71ab9d20-b3a2-3b9a-ad64-4e0cecae1c6b | -14.01119 | -53.7097 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 27aa5e3b-c55f-30f0-90e4-a6435c46bd1e | -13.82108 | -53.99444 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 96c3606d-ecdf-3482-9f01-2a5b81a7dcea | -18.52733 | -48.25095 | 2026-08-22 04:29:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea5681d9-7985-3d65-8a5a-4e2253205309 | -20.61217 | -47.0599 | 2026-08-22 04:29:00 | NOAA-21 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9e5f0159-93d8-3191-b643-005b000d2f6c | -15.18471 | -48.74807 | 2026-08-22 04:29:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5591ba88-fe3a-3cc2-8c1c-7510d93db207 | -17.97096 | -44.35798 | 2026-08-22 04:29:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e51adad-3272-3063-a966-5b487cd8c2f0 | -18.26821 | -43.69709 | 2026-08-22 04:29:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ee96cb5-5ac2-3d63-beef-a6fa72c9ffea | -16.74258 | -49.34939 | 2026-08-22 04:29:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e72fa51b-f7c4-35bb-a252-268a8e190ac5 | -15.17921 | -48.73984 | 2026-08-22 04:29:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 76049f33-30e1-321a-a2e5-ce4ddded647a | -15.84157 | -48.96048 | 2026-08-22 04:29:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c213c48-7072-3db2-810b-c1cfa4e10511 | -20.63752 | -47.44674 | 2026-08-22 04:29:00 | NOAA-21 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7eeddb2-38b9-37b7-bba6-2ce196c10219 | -15.06499 | -45.32957 | 2026-08-22 04:29:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aba79550-e061-32c8-9f03-6f98b57631e2 | -17.84835 | -44.46838 | 2026-08-22 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fec46036-49a3-3815-8a4a-bf7e822296b2 | -15.91981 | -43.52306 | 2026-08-22 04:29:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c019f00-e20c-3ced-aaca-44387c9729ca | -15.23598 | -52.83078 | 2026-08-22 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd7bd12b-59b6-39c7-9190-dd816e0c27f0 | -17.81418 | -44.4581 | 2026-08-22 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 638af4f1-61b6-3f09-a6d2-8ff491b61b41 | -20.63519 | -47.43824 | 2026-08-22 04:29:00 | NOAA-21 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 40.0 |
| a3226853-bddf-3672-85ed-88322fa98907 | -15.17978 | -48.73627 | 2026-08-22 04:29:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a549a844-112f-3ef0-a568-bd33a76e6124 | -16.95403 | -46.11833 | 2026-08-22 04:29:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f8d325c1-faf9-3dd5-92e5-825a4a4a258f | -13.83733 | -54.00097 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c321cbd-f1c4-35b3-a013-409c9bd4b13d | -18.27404 | -43.31398 | 2026-08-22 04:29:00 | NOAA-21 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e839d1e-735f-33a3-bbee-5726bfb8b2ba | -13.82531 | -53.99516 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dd6da973-639f-3d4c-a026-4ba8c26fbd09 | -13.99059 | -53.68203 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c578da15-3e6f-341b-90a1-0b66bcfb2eda | -13.8246 | -53.99908 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4e1504a8-0ced-34ba-801b-380e8b4b41f9 | -15.33008 | -53.80859 | 2026-08-22 04:29:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aae0beaa-0cbc-3926-9733-90b8208d835b | -15.67936 | -53.77934 | 2026-08-22 04:29:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9758317c-201d-3702-bd4b-a9679a96d06f | -19.88929 | -43.96958 | 2026-08-22 04:29:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b1ed1c62-fda3-3e85-936b-c6a8c30fd0df | -17.91812 | -44.39758 | 2026-08-22 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 487ac50f-76d1-3989-9455-225ff9bd08f2 | -15.81186 | -38.90968 | 2026-08-22 04:29:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| b8b6e653-b935-3b81-b2d0-33257d266573 | -18.52789 | -48.24726 | 2026-08-22 04:29:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2a296cc-348e-33d6-9a61-e5865306e9d1 | -15.20676 | -52.79473 | 2026-08-22 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 48f0035c-5daf-3143-b3cc-75eaf7a6254f | -15.06857 | -45.33012 | 2026-08-22 04:29:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1037426e-3d18-3afd-92c9-2c8de59e34d5 | -16.28234 | -57.6711 | 2026-08-22 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2ff1ddc2-b68e-3710-aaeb-77ef465f7bc9 | -14.2408 | -52.13185 | 2026-08-22 04:29:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06108adb-bdc3-3360-b8dc-43e08b72ffe3 | -15.18196 | -48.74396 | 2026-08-22 04:29:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 907f153e-74dc-36dc-b1f7-52bb5a2019fa | -14.55726 | -53.08572 | 2026-08-22 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8a4dc3a-4ec4-3bc1-a5fe-5db194bd50a5 | -18.63636 | -43.92986 | 2026-08-22 04:29:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7ab8f4f-0fbf-391d-83ab-edc673b852fc | -18.69647 | -52.24734 | 2026-08-22 04:29:00 | NOAA-21 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3296ad6-ff0c-3b55-b173-a6792d5999c8 | -20.41308 | -43.61034 | 2026-08-22 04:29:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6da6a69d-67d2-322f-b3e9-867002cd6d27 | -13.98646 | -53.6813 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7068cb23-7f09-3e76-9431-0c41956376be | -18.03881 | -43.80596 | 2026-08-22 04:29:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 074d7f71-78b8-3071-82a3-bc1e375644eb | -20.43983 | -43.60251 | 2026-08-22 04:29:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 20634163-0b9e-395b-b06a-7f576828aa11 | -16.62186 | -43.41875 | 2026-08-22 04:29:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e5da98d6-0d13-3383-9010-3024d4ba5ed0 | -16.712 | -47.70173 | 2026-08-22 04:29:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff78c959-6544-3580-8d88-dda51691ba14 | -14.98223 | -52.66001 | 2026-08-22 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce808689-1ce0-3043-be58-3ffdb0467133 | -14.97842 | -52.65932 | 2026-08-22 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56208c45-39a6-37c7-a843-faceed79e647 | -18.91823 | -43.59703 | 2026-08-22 04:29:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| 3cc1905d-7d21-3521-a17b-4b771a4f9d77 | -15.00582 | -52.69758 | 2026-08-22 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 816d824d-2526-3b9e-a39a-45b3c8aed85f | -19.74888 | -45.10269 | 2026-08-22 04:29:00 | NOAA-21 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9702bf67-e0c7-373e-b356-25c9387c0f3b | -14.00022 | -53.67576 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 268bbaad-4958-3d7d-a6b0-11af6fc1cef6 | -18.61831 | -48.20892 | 2026-08-22 04:29:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 089ac8c4-ccf4-310d-8e0e-bb2041ee1f3b | -15.16872 | -48.74176 | 2026-08-22 04:29:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3681b5e6-c9f5-3270-94d6-fd287ff19d05 | -15.06437 | -48.71302 | 2026-08-22 04:29:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5d917c8-5ae8-33f0-af50-ce153e852ce1 | -18.27877 | -43.31008 | 2026-08-22 04:29:00 | NOAA-21 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7419ebc-3811-30c1-b0a0-1f6a87802cb0 | -15.98854 | -44.80634 | 2026-08-22 04:29:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a199924-be51-3ce0-93f4-740bc48a13e0 | -15.06557 | -45.32538 | 2026-08-22 04:29:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d055303-4fc6-3f49-b70b-55bbe89cf59d | -20.47292 | -43.40082 | 2026-08-22 04:29:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 23f3e6aa-cd47-3c31-ba43-1a656bf7223d | -16.71869 | -47.7028 | 2026-08-22 04:29:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9f0eb10-f626-3b07-a9a4-824c2e5a6cd0 | -13.98234 | -53.68055 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ac0fe73-c516-3a5f-b253-59afb6da0109 | -14.54735 | -53.00402 | 2026-08-22 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da43603a-29fb-3f95-a8ee-3ef74a50079f | -20.62428 | -47.44046 | 2026-08-22 04:29:00 | NOAA-21 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17dde2e5-b4b7-313e-be0a-2fabeb0ef609 | -13.82179 | -53.99051 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ae7f6af4-94d3-3920-8f30-952e7daa83e3 | -15.17203 | -48.74231 | 2026-08-22 04:29:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca397bb8-8baa-3182-a253-68c8e4776211 | -17.97346 | -44.36916 | 2026-08-22 04:29:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42b8c150-8a7b-3e22-8453-f778101c8a48 | -17.96407 | -42.72556 | 2026-08-22 04:29:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 99a29ef4-50a8-319d-988b-352d26a6a951 | -15.5204 | -45.86053 | 2026-08-22 04:29:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5a2923b-9f32-309d-8491-9db5ae8ed061 | -16.03515 | -52.17244 | 2026-08-22 04:29:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1ff37c1e-05c3-3942-8702-33e8666a316c | -18.3402 | -42.46785 | 2026-08-22 04:29:00 | NOAA-21 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f12b6650-db45-3e44-87d1-fa659f926029 | -20.08188 | -44.22412 | 2026-08-22 04:29:00 | NOAA-21 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 906da98b-58ca-39e3-a866-41518d1ac949 | -13.87941 | -53.98465 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8fdc07e1-23d8-3bda-9ac9-f96b9b480b46 | -17.98885 | -44.40294 | 2026-08-22 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf826587-a6d2-3470-87ab-e9d4f7b8169a | -13.98785 | -53.67358 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |


[Clique aqui para ver as próximas entradas](README32.md)
