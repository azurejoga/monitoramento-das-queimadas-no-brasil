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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de1b528b-afcb-3e9b-b564-ff1f2cff1e34 | -19.7639 | -57.9607 | 2026-08-19 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.6 |
| b7d48aa9-7761-3365-bf90-cdd11ac0ce34 | -5.9198 | -43.6264 | 2026-08-19 01:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 258.0 |
| 3d754224-0bd0-3d0a-b298-46daa658d58c | -7.5487 | -55.5829 | 2026-08-19 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| faf4e04b-04af-3866-a42b-ddbc06e60a3d | -6.8593 | -59.0318 | 2026-08-19 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| d7b18f86-939f-37d4-a095-5740cd3cd2c5 | -5.9995 | -57.8444 | 2026-08-19 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 78db6259-4ae0-35b8-b13b-4638a8294300 | -9.4256 | -60.4353 | 2026-08-19 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| dab1b60b-bc8e-3ffa-8920-fa6f4a1afa3a | -9.3875 | -60.5528 | 2026-08-19 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 9ef3eb63-e9a5-3c32-b02b-4a96c26f111c | -6.6938 | -58.942 | 2026-08-19 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 055d0839-ca02-3740-a1a4-20a9d924f17b | -6.0912 | -57.9187 | 2026-08-19 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 5b772b00-b262-3f14-960c-9a28e31f7baa | -9.4257 | -60.416 | 2026-08-19 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| d0ec4e43-ea08-3da5-b4a5-c4bad4b897ce | -5.4317 | -48.4212 | 2026-08-19 01:50:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 135.5 |
| 38e24b42-6308-39df-80b4-55110e2afb14 | -9.406 | -60.5711 | 2026-08-19 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 434b4587-ff6d-30a9-a49b-f4d5758ddaee | -9.3873 | -60.5721 | 2026-08-19 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| ce023e16-cc45-37b6-8c38-3bab7c13c80f | -9.4061 | -60.5518 | 2026-08-19 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 58442b81-4b86-3981-b200-6a11a24c7f32 | -6.0178 | -57.8631 | 2026-08-19 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 43806919-eaac-3f79-a330-89dc8164ecc6 | -19.7442 | -57.9425 | 2026-08-19 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.4 |
| 2eccb504-b8ce-3986-9892-a76dd54b8590 | -5.9011 | -43.6279 | 2026-08-19 02:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 4a360cc0-6e97-36e1-a1a9-acadec489bf7 | -9.3875 | -60.5528 | 2026-08-19 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 6e8c9965-0a7c-366a-a614-f261bf2378f4 | -9.3873 | -60.5721 | 2026-08-19 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 52e0eba0-08f1-39f6-ad2f-e993ba408855 | -6.7123 | -58.9412 | 2026-08-19 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| fab5440f-d7ac-3146-a766-aa671510eba7 | -5.4317 | -48.4212 | 2026-08-19 02:00:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 121.3 |
| a2380c90-25db-36af-ad29-845e819318ba | -9.4061 | -60.5518 | 2026-08-19 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| d7291fa7-c293-3f79-b7da-9ca256fe35e0 | -19.7639 | -57.9607 | 2026-08-19 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 6f3fb45d-eae6-33be-b7a1-9eabfd96eab3 | -6.0728 | -57.9194 | 2026-08-19 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| ad8ba786-6a24-3d9d-8967-fe00b525bba3 | -6.3496 | -54.9068 | 2026-08-19 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| f94d1edf-f114-3e73-b310-ce6b44314266 | -5.92 | -43.6032 | 2026-08-19 02:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 5abc3f5c-be64-3656-81a1-c38817a51490 | -5.4319 | -48.3996 | 2026-08-19 02:00:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 9bb4eb4b-589a-3eba-bf12-b19a8598e829 | -6.6938 | -58.942 | 2026-08-19 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 5d095fc6-d4f1-3cbf-b3b0-c13c6dfa4621 | -5.9994 | -57.8639 | 2026-08-19 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 15463059-b475-336f-bae2-4991255b9f72 | -5.9995 | -57.8444 | 2026-08-19 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| ce9870ef-ce97-3821-b2a9-8b4b90da0471 | -9.4256 | -60.4353 | 2026-08-19 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| be6ff2a1-cb9c-3789-b429-6b4b0e7fc620 | -9.406 | -60.5711 | 2026-08-19 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 34575968-ccf4-3fe3-9fe4-15dd077a0f08 | -6.0913 | -57.8992 | 2026-08-19 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| a9185b39-7ee6-343d-a58d-90b9e1d5014e | -6.0178 | -57.8631 | 2026-08-19 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 9e5535c5-0d21-3d77-a876-631275f47c97 | -6.8593 | -59.0318 | 2026-08-19 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 3cd75941-1ae0-357d-bbad-d7baaf90fb68 | -19.7442 | -57.9425 | 2026-08-19 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.9 |
| f1564ac0-2d6f-3840-9654-8ae05efef944 | -5.9198 | -43.6264 | 2026-08-19 02:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 231.2 |
| 0d165327-59d2-3229-a4a4-15e2512d14de | -6.0912 | -57.9187 | 2026-08-19 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 2be02ce7-5726-36f4-bf59-05a53d181186 | -6.8593 | -59.0318 | 2026-08-19 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| e8513990-4fef-3219-b263-25fa41f4a44a | -5.9995 | -57.8444 | 2026-08-19 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| ed0defe8-381f-3123-bc08-7bacf223fe2c | -5.9011 | -43.6279 | 2026-08-19 02:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| e40988e2-2cd8-3432-be7b-ece67ff2f27d | -6.7123 | -58.9412 | 2026-08-19 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 961ee8b2-27a5-3a91-9380-47ab38d1a58f | -6.6938 | -58.942 | 2026-08-19 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 7d44ef54-4891-3b58-9ce1-040eb3eaf65d | -6.0913 | -57.8992 | 2026-08-19 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 77884278-a41d-3e73-801e-9139fb493a65 | -5.4319 | -48.3996 | 2026-08-19 02:10:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 853c2402-69fb-30bf-a788-24a7c353f866 | -16.345 | -49.4851 | 2026-08-19 02:10:00 | GOES-19 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 5a6012f3-27c6-3a7d-b023-7a477f211af3 | -9.3873 | -60.5721 | 2026-08-19 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 19d14c8f-4846-3c7f-bccb-c8e839361e1c | -9.3875 | -60.5528 | 2026-08-19 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 930f43c2-587c-34dd-a1ac-7b9d2e5464a7 | -5.4503 | -48.4201 | 2026-08-19 02:10:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 7a9cd49c-b1a0-3905-bd34-7a06bb15e5a9 | -9.4257 | -60.416 | 2026-08-19 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| bb137708-3e6c-3ed0-9036-69fdc925cf37 | -5.92 | -43.6032 | 2026-08-19 02:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| a827071e-8678-302c-92c6-c69549ac0da4 | -19.7639 | -57.9607 | 2026-08-19 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 2a303545-b1d5-3e5c-8a52-0e2eb78d3864 | -5.4317 | -48.4212 | 2026-08-19 02:10:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 128.7 |
| 4f729cf2-c22c-3c7b-af05-bb6a338938d6 | -19.7643 | -57.9399 | 2026-08-19 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.6 |
| 9fd51aa7-9540-3889-b524-fdfcaca20399 | -7.5487 | -55.5829 | 2026-08-19 02:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 1a48e143-243c-3056-9efe-fd3971cdb795 | -9.4256 | -60.4353 | 2026-08-19 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| a1b7bb96-1f56-3de3-9e9d-108c5fcfa2d9 | -5.9198 | -43.6264 | 2026-08-19 02:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 222.0 |
| 95d83dca-e596-3bcf-9237-7266930a59bb | -5.9994 | -57.8639 | 2026-08-19 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| ba460c1f-b57d-3f4c-8106-78ef06765018 | -19.7442 | -57.9425 | 2026-08-19 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.8 |
| 0242e64a-f1dd-3eed-8c2e-c0ba6c13ebde | -6.0178 | -57.8631 | 2026-08-19 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| de442390-c5ba-3603-aa69-abdabeadf19c | -21.4442 | -48.5236 | 2026-08-19 02:10:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 55.6 |
| fdb6c518-d0bf-3f74-9963-45e94ea88a0a | -9.406 | -60.5711 | 2026-08-19 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| e7f85a2a-b805-3681-a827-aa0bec51b7ad | -9.4061 | -60.5518 | 2026-08-19 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| a6a7e512-6957-3b6f-bdc8-8e802d39d9ce | -6.0912 | -57.9187 | 2026-08-19 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| ebab6a39-d7e8-3e72-8f7a-e20e1931f9cd | -5.92 | -43.6032 | 2026-08-19 02:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| c1c36f81-677f-3961-a7eb-cc722002cc6b | -9.406 | -60.5711 | 2026-08-19 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 13d6ce31-0f5d-3e80-ae91-0d9f1f8ba65d | -6.7123 | -58.9412 | 2026-08-19 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| f2fbc17d-f41d-3ff1-92a1-d4c4d27a3ae7 | -5.4319 | -48.3996 | 2026-08-19 02:20:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 848ae1d4-040c-3e6d-836e-46159eeee6a9 | -6.8593 | -59.0318 | 2026-08-19 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 26b0bb75-e86d-3728-83c0-f6c3c7dc8e66 | -9.3875 | -60.5528 | 2026-08-19 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 254070a1-51ef-380a-8fc9-967fc4fe147f | -19.7639 | -57.9607 | 2026-08-19 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.4 |
| 44cbbc53-24ea-3877-ab12-acd38f97d596 | -6.0178 | -57.8631 | 2026-08-19 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 5d041df5-7876-3def-ba27-2fa210906c50 | -5.9013 | -43.6047 | 2026-08-19 02:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| dd619503-ae7d-34a7-8546-31d6059a5c35 | -9.4257 | -60.416 | 2026-08-19 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 654f4b06-9cd4-3c3f-a853-965f60825caf | -5.9198 | -43.6264 | 2026-08-19 02:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 670322c2-bc88-36a3-ac30-95446190f626 | -5.9011 | -43.6279 | 2026-08-19 02:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 5d0856b9-74ea-3338-859d-bf9ca6fea7f7 | -9.4256 | -60.4353 | 2026-08-19 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| e9a17bb6-7406-30d5-b365-62a3cbb0bcf4 | -6.0913 | -57.8992 | 2026-08-19 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 7ca82ac3-6346-381c-941d-b30cfa277cc1 | -19.7442 | -57.9425 | 2026-08-19 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.1 |
| 602e3d83-0b83-3b53-a6bb-18f2d12624a4 | -5.4317 | -48.4212 | 2026-08-19 02:20:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 791ccec6-7d3b-36ae-afa2-7c6231b6a726 | -9.3873 | -60.5721 | 2026-08-19 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 4a53e47a-8e87-3abb-b0e2-910c8a323d8e | -6.0912 | -57.9187 | 2026-08-19 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 124.9 |
| cec8b011-1074-3bc7-89fa-4fc816cdfebd | -5.9994 | -57.8639 | 2026-08-19 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 0b6852c6-b5b0-3399-bf98-f7cf222ba73f | -6.6938 | -58.942 | 2026-08-19 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 498e961f-4f7b-3691-8a4d-218d7334fbe3 | -10.4272 | -61.1905 | 2026-08-19 02:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 0b608849-e854-3d4e-bd37-0398550bda30 | -6.8593 | -59.0318 | 2026-08-19 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| d6eaaae0-4e60-3b6f-8f53-6b757ba6e661 | -9.4256 | -60.4353 | 2026-08-19 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| e72eb6ad-6077-390e-8cf3-a42784e1866b | -5.4317 | -48.4212 | 2026-08-19 02:30:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 8400f1a0-134b-3f8d-9864-bb53e0b17197 | -6.0178 | -57.8631 | 2026-08-19 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 367a3f82-4aaf-3790-b6b2-ad9382b36011 | -19.7442 | -57.9425 | 2026-08-19 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.1 |
| 8fcd9ed6-e65b-37c5-9205-90dae8a12245 | -6.6938 | -58.942 | 2026-08-19 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 47217a28-601c-37f8-9ecb-15a2825204e5 | -5.4503 | -48.4201 | 2026-08-19 02:30:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 6788080b-e831-36f0-80ef-30c49f70a621 | -5.9011 | -43.6279 | 2026-08-19 02:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 9a99d8e9-4cb6-3756-9966-922039ff590c | -10.4271 | -61.2097 | 2026-08-19 02:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 1ceaf592-ef05-3f24-9ba4-185d1f15d28f | -6.7123 | -58.9412 | 2026-08-19 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 24ca154d-8761-32ca-b38f-5e039c0bb67f | -10.4084 | -61.2108 | 2026-08-19 02:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 65073b19-1b16-35f8-abd1-0c91dc9f880b | -10.4085 | -61.1915 | 2026-08-19 02:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| d94d5d3a-e7d4-385f-8922-e0b53e90fd5c | -9.4257 | -60.416 | 2026-08-19 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 2c011d4a-0b14-36f8-b237-d629f8cd3fe1 | -5.9994 | -57.8639 | 2026-08-19 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| a418d3c7-c947-3670-8d10-3980e2fe9ab8 | -6.0913 | -57.8992 | 2026-08-19 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |


[Clique aqui para ver as próximas entradas](README17.md)
