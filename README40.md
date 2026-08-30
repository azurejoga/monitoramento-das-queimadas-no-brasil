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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09a1c227-e53b-370c-91b2-5b587e32449a | -10.7665 | -44.88478 | 2026-08-30 04:34:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86f231e8-e62f-3666-aba0-62c7b54e6d1b | -11.15689 | -50.58205 | 2026-08-30 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 62cc72e1-3eaf-32e3-bc13-31943b593704 | -9.8894 | -60.26826 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7a135cb3-c9ac-35b4-8e32-0e8fabb5be4f | -12.62212 | -45.08453 | 2026-08-30 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4486dcd4-2cbe-33fd-b019-26c13a933269 | -10.86188 | -50.50554 | 2026-08-30 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46fc9542-d360-3c5a-9097-2b52cf940d4a | -9.14566 | -59.5097 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db29c2cf-0dad-3130-bb6d-ab9b503ad237 | -10.48133 | -59.61381 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4c956591-8536-3013-931b-7a13991cf9a5 | -10.78833 | -45.3219 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| becdeea8-bcc6-3671-ab41-0d9af6dc0b27 | -11.20755 | -45.0741 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 232ff8ff-11a6-310b-b86b-2c0d00450f45 | -9.06771 | -60.49523 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1c1b48d-8ffb-3dfd-a16a-1ce5bb5d1f14 | -11.29673 | -54.03902 | 2026-08-30 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 39ea333b-3c86-3a6a-9362-c2854b47c3ca | -8.54867 | -54.71801 | 2026-08-30 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee11cc5a-5f3c-3206-824d-5435ef4c94ee | -11.21104 | -45.07465 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a12c6806-57a3-3274-aba7-4877b3408a6d | -9.17291 | -59.6133 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e5380081-37ff-3a4e-a89f-cc81e86f8f43 | -13.79803 | -46.47437 | 2026-08-30 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bfe7a72f-aeae-3bf2-8cbd-e2cf78c504cf | -10.76593 | -44.86452 | 2026-08-30 04:34:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2cbb1a65-ba12-392b-bc83-b2c316057fb3 | -9.89376 | -60.28148 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3d5e36c3-6ae7-3277-8cb1-71962d5d7349 | -12.38292 | -48.17653 | 2026-08-30 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4c235ef-183c-342a-bd8d-4cdd9b4b81ed | -7.32458 | -60.60212 | 2026-08-30 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c833ce2d-cd1a-309f-8de9-9e7c5cab7d6d | -9.15905 | -59.50962 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d84bd34f-9df8-3db3-abf1-623d73e41a26 | -9.66362 | -50.8451 | 2026-08-30 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff298ac4-b383-36c9-a641-7012b6490b38 | -10.763 | -44.86003 | 2026-08-30 04:34:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4c7a7304-c606-3d28-85e6-815c0d766737 | -12.36467 | -48.18437 | 2026-08-30 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 119717d5-0c44-3a00-9b31-e0a921b35ab3 | -14.39744 | -52.56573 | 2026-08-30 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4dde5931-dc2e-3f31-ac19-9dabe5bd1fad | -7.30063 | -60.61186 | 2026-08-30 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30f45366-b5f1-397d-b8f8-0fc288e8b87d | -13.82737 | -54.09609 | 2026-08-30 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f36728a-1a8e-3a56-9b1e-fb39528498fe | -14.91123 | -52.63287 | 2026-08-30 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84d41eb1-dcf2-3012-8e34-e31c9ab72788 | -10.56933 | -59.61169 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a26869f4-3cbc-3ee6-a497-f735190fac63 | -12.78528 | -44.61231 | 2026-08-30 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4df6b090-41d0-32e7-a0ea-8c83e500f6f3 | -11.83405 | -46.76595 | 2026-08-30 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa537c36-3b99-37e0-a139-5b1ba3310110 | -10.76886 | -44.86897 | 2026-08-30 04:34:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 884a6f12-df21-3e54-9e94-ea1ed9b775e2 | -9.43137 | -48.35484 | 2026-08-30 04:34:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 197ab4e5-9d27-36bf-83fd-d1fafa0c7662 | -9.67564 | -55.06772 | 2026-08-30 04:34:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2cc8139a-619e-3437-8f49-d82a995b23ab | -10.33787 | -45.36331 | 2026-08-30 04:34:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 940b8bd9-c3b2-3ef6-889a-c55129d9724c | -10.7895 | -45.33768 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17d81401-16e3-3d8a-b176-dc8d9e346105 | -9.8926 | -60.28736 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 42071df2-a6c1-35a6-bcda-e3156c3e336c | -10.7715 | -54.03936 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b66723f-c59d-35ef-9dcc-29fc0d463827 | -14.28115 | -53.18987 | 2026-08-30 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c2048c7-28d2-3846-89c4-4fff98612459 | -11.34024 | -45.15063 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b22de11-2e41-3731-9984-e8935892856d | -9.7083 | -60.75145 | 2026-08-30 04:34:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f74da3d7-a426-3a80-9a17-8a2205149516 | -11.80614 | -51.04573 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| ec793fbd-1930-3dc1-959a-58576439fcee | -10.99968 | -49.68008 | 2026-08-30 04:34:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3634e4b5-15be-3352-b3c5-242426caf40e | -9.4355 | -51.57079 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 70aac8b6-ff7c-3cad-bf95-fc54ce55f885 | -11.29378 | -54.0307 | 2026-08-30 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8394be49-c2cb-320c-abad-2b3025c2723c | -11.29316 | -54.03379 | 2026-08-30 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4159ac9c-3e00-38eb-ab78-c5cc826a796c | -11.35328 | -45.16681 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c0afafed-aaa4-3d6c-94c8-5248239e9db2 | -11.0191 | -49.69124 | 2026-08-30 04:34:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14aa91f3-44a7-3e94-be12-858de9eb3a29 | -15.38752 | -52.66395 | 2026-08-30 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d51d2e47-c9b8-3ea3-bf96-b7e313bfb14f | -7.24408 | -60.63731 | 2026-08-30 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea2d8b93-f127-39e6-b080-7b68b53a70f6 | -10.05482 | -48.68202 | 2026-08-30 04:34:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd72893e-ac27-38c9-ab0f-f9b61ebdf961 | -13.85895 | -54.1144 | 2026-08-30 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a6d5266-5342-395e-aca7-e748938c43ca | -11.03452 | -57.23219 | 2026-08-30 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a37aabe-bc0e-3d7c-85bd-e1e978f1f8d4 | -8.94392 | -50.17884 | 2026-08-30 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a62f5f5d-6de0-344f-b2a5-90325bb1e07a | -11.26355 | -45.06593 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90ca5b5d-80b0-3047-ad0f-649049c3aafd | -10.12882 | -45.70169 | 2026-08-30 04:34:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 24ea0a21-2368-322d-84a1-42e33fa6c70e | -9.65134 | -50.83545 | 2026-08-30 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16d93207-961d-3cc7-a36b-5a8210ca9ba8 | -14.23802 | -52.8474 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11a4d5e3-7481-3aef-a0b8-e1007eb67aef | -11.18278 | -55.10263 | 2026-08-30 04:34:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b511084-8676-31c2-88ed-dc5e62fc6b05 | -14.89842 | -47.74792 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 179b47ee-86de-36be-aec3-b25c7779a07c | -12.92316 | -45.89769 | 2026-08-30 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1791bd6c-23a3-3998-99ec-70a870890d7d | -10.14231 | -45.70425 | 2026-08-30 04:34:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74c371a1-db11-36d7-b2f7-36c9006a0652 | -10.35495 | -49.97938 | 2026-08-30 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| be1c9522-da20-377e-a8bc-4dbd5e4d4607 | -11.25713 | -45.06091 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e63df49-cff2-301d-b410-807b62a963c9 | -9.46952 | -51.58867 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57428029-71d8-3fec-8a65-7fc0734c70e7 | -11.53302 | -45.55749 | 2026-08-30 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98fbf0e9-07ca-3fef-ad55-39bf12b64ef3 | -16.34314 | -50.98009 | 2026-08-30 04:34:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5c3a449f-fae9-32a5-9854-244de00a0e11 | -10.75059 | -54.0037 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd28ad15-6132-38a6-bf55-e9299abbb3b9 | -14.77337 | -48.73637 | 2026-08-30 04:34:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe82a7a3-e86a-3601-aaba-b1be91cc5382 | -14.03386 | -54.01486 | 2026-08-30 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf457528-4777-358d-9908-ac41256e6131 | -13.86523 | -54.12801 | 2026-08-30 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0330ed7b-7bea-32fb-838c-3588088a56ba | -13.39206 | -51.79843 | 2026-08-30 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16803b3c-4c60-39f1-81ad-c61abb0d2fde | -11.15619 | -50.5862 | 2026-08-30 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 6f8bb1e0-58f8-3e88-abe3-35ab8461d069 | -11.26005 | -45.06541 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b9b4b89-8444-3921-ad81-f2f3ac18f256 | -11.03104 | -57.25011 | 2026-08-30 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 135560c7-5899-395f-986c-6f35a9d090e8 | -11.03541 | -49.67828 | 2026-08-30 04:34:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7da523b5-98f3-31d9-8ff6-8f9c7e8934b3 | -15.33887 | -43.66985 | 2026-08-30 04:34:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fb21c9f9-8286-397a-824b-6abed9cddab9 | -9.93128 | -60.5286 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f9bdeda7-6c6d-307e-ae0f-211fa5607f35 | -11.71461 | -54.53451 | 2026-08-30 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| deb1d51f-297a-3569-a44b-7952fe894e8f | -13.85124 | -54.10879 | 2026-08-30 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b924645f-e6b1-33d1-afda-682a394dbc37 | -11.83739 | -46.76647 | 2026-08-30 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dddca1aa-f7dd-38f4-832d-84adb7cad875 | -14.44881 | -58.4388 | 2026-08-30 04:34:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e3f22ce-9a77-37d7-9e1f-e28eb2978815 | -11.25772 | -45.05692 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ce09624-d7db-30ca-84ed-2b297d891fb6 | -14.41142 | -52.55341 | 2026-08-30 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c4060400-87b7-331f-801a-726900ae294a | -10.13894 | -45.7036 | 2026-08-30 04:34:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5689e4e3-79ae-336b-a35b-90b4f302d111 | -9.19618 | -51.56012 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f0c25e1-2df0-3855-9abf-cb206ad64db0 | -7.23702 | -60.6357 | 2026-08-30 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| de0b1367-00e1-305c-bc38-ff14bb61560d | -12.78466 | -44.6166 | 2026-08-30 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d02f713-3849-32cf-84c7-cca6f2b475de | -8.1806 | -54.93817 | 2026-08-30 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7a35f653-26d9-3419-9d84-3ce8e29ad9fb | -9.64727 | -48.26522 | 2026-08-30 04:34:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 255e2e0c-eac7-3ec7-8756-3cec97e50b81 | -10.75204 | -54.00149 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 474812e5-5c8b-3262-8107-f4fa7bdefb62 | -14.40675 | -52.55757 | 2026-08-30 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b565161-85af-3f4e-926b-a3e4c0ef3b33 | -10.75138 | -54.04935 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a96763c-46ea-35ad-b995-43b26999a9d7 | -14.39913 | -52.55626 | 2026-08-30 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e0d2f29b-0acd-37fb-a80d-4e79f73b8d1d | -14.39447 | -52.56039 | 2026-08-30 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0f5cbe93-e455-39a6-ac2f-1db306b244dd | -9.6063 | -55.12814 | 2026-08-30 04:34:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 31f67cbe-17ee-3825-927f-f2d66b353adb | -11.74805 | -47.6396 | 2026-08-30 04:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 526ebd0c-a58e-3f34-a9fe-a8d67c6ce03d | -14.41898 | -52.55498 | 2026-08-30 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a8714029-6065-3148-bead-44b2d3662c37 | -14.24214 | -54.65176 | 2026-08-30 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d18aac92-ca2a-3886-847b-e0bc4ec510b4 | -11.8011 | -51.05054 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e1ab67b8-d299-3491-934c-61fc5ab2eb89 | -9.7838 | -46.41729 | 2026-08-30 04:34:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README41.md)
