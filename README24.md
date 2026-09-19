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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 464acaee-0e91-3659-a074-697adc58d678 | -8.4983 | -57.6271 | 2026-09-19 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 5ce67b82-1bad-3fbc-aa13-5e9f9c0d76a5 | -12.5952 | -49.1046 | 2026-09-19 01:30:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 06cbf189-747d-31db-ab10-9c1932fc2d54 | -3.3638 | -50.4492 | 2026-09-19 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| c91ebfb2-a6bd-3943-bc67-0757a17e9a42 | -3.2314 | -46.9376 | 2026-09-19 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 8c5f083c-dd96-38b9-bc7c-08e7c935b2b8 | -7.6386 | -46.103 | 2026-09-19 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 2b84e7c1-88d0-3867-940b-c39016b264d6 | -3.3311 | -59.8101 | 2026-09-19 01:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| d7e3b103-114e-3704-a4c8-1fbf28351e9b | -4.5774 | -42.9512 | 2026-09-19 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 0d79c2f1-1d16-3292-a178-b97c3f03bd55 | -12.5952 | -49.1046 | 2026-09-19 01:40:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 59152006-6eb5-3dbf-a479-a5c9c53dced2 | -8.4983 | -57.6271 | 2026-09-19 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 7850df6e-31a2-3d3e-99bd-1df528a2dea0 | -10.6928 | -60.7322 | 2026-09-19 01:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 4415402a-150c-3765-84a4-dbe3fb64f09a | -3.2499 | -46.9589 | 2026-09-19 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 7da2449f-c2a4-39a5-9a05-6ed363aa1d8b | 1.2608 | -50.976 | 2026-09-19 01:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 50.0 |
| e410291c-cdd7-35c3-b235-a2ac742183c2 | -4.5772 | -42.9746 | 2026-09-19 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 194c0f5c-fed2-32a3-b6a6-5f29e5ae37b2 | -6.9871 | -42.1917 | 2026-09-19 01:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 92.8 |
| 7da65633-b4db-38bd-912e-1e4636b49d36 | -4.596 | -42.9734 | 2026-09-19 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 3cbb431f-78de-33ec-bae2-6845052d306d | -10.9301 | -53.9618 | 2026-09-19 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| cb687dc5-55bc-3f68-8128-ac81249f0a88 | -6.9874 | -42.1678 | 2026-09-19 01:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| 1664e684-066f-3e28-9cc3-bb1758d2bbd1 | -7.7629 | -46.7389 | 2026-09-19 01:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| f5f71f5d-386f-304e-993a-928dd495fa54 | -3.2313 | -46.9596 | 2026-09-19 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 44abe99c-773e-366a-be0e-9fd4546626c4 | -2.8286 | -50.4444 | 2026-09-19 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 0ba4e446-0981-389a-a6fd-f9b70603b8cc | -4.5585 | -42.9758 | 2026-09-19 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| c839699c-0b40-323a-a36a-4126b1e6e20c | -10.7115 | -60.7312 | 2026-09-19 01:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 75a21d62-cc5a-363b-b299-d25c291fccb4 | -4.5961 | -42.95 | 2026-09-19 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| c0642c89-c76d-3816-b657-7ed366b89310 | -2.8101 | -50.4658 | 2026-09-19 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| e2178735-e9d9-39e9-8e66-b2213e5b5bc4 | -2.8285 | -50.4653 | 2026-09-19 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 142.0 |
| fed0e275-240f-3306-95df-218e261671b6 | -10.7115 | -60.7312 | 2026-09-19 01:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 369a1260-38b3-373b-8e0e-faa78dd3a904 | -2.8284 | -50.4863 | 2026-09-19 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| f94b70e6-bda2-3d24-b1a9-16d15f292136 | -7.7629 | -46.7389 | 2026-09-19 01:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 741e3af5-9bd2-3a3c-be39-06601d146797 | -7.7441 | -46.7406 | 2026-09-19 01:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| a4032bcd-aabc-3c1c-92d1-f67f8cc14afa | -2.8285 | -50.4653 | 2026-09-19 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 176.8 |
| 227f692f-c540-3523-af0f-dc836d100273 | -3.2313 | -46.9596 | 2026-09-19 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 670fe656-e8a7-3702-857c-6dde917a400f | -5.6246 | -45.2518 | 2026-09-19 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 1fdcf0a5-5d2f-3072-a1bc-92f4b15e10ef | -3.3311 | -59.8101 | 2026-09-19 01:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| e0d50267-8065-37f0-bd83-e5b497df8719 | -3.2314 | -46.9376 | 2026-09-19 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| d2ed4caf-eac4-3652-9b4a-beca55f74f82 | -8.4983 | -57.6271 | 2026-09-19 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 37868982-f15e-3440-97a9-3252437c9912 | -2.8101 | -50.4658 | 2026-09-19 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| d4ed7d0a-021a-3512-80ad-782120f90c65 | -7.6386 | -46.103 | 2026-09-19 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 583d2262-4e7b-3122-a567-3616f9648b74 | -10.6928 | -60.7322 | 2026-09-19 01:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| a3df9513-e068-3866-b66b-45978086ee88 | 1.2608 | -50.976 | 2026-09-19 01:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 86694335-7723-3c87-939b-e49cca775c89 | 1.2608 | -50.9552 | 2026-09-19 01:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 46.4 |
| f03971eb-2135-33d6-a9a0-735ae3c6295f | -6.9871 | -42.1917 | 2026-09-19 01:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 88.1 |
| 1155036e-283c-3c1a-9fb3-60120c5f0c28 | -3.3311 | -59.8101 | 2026-09-19 02:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 1e63524a-12a2-3270-b1e5-0ff8349cba83 | -10.6036 | -46.0955 | 2026-09-19 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 516ca894-496b-3fe7-a44e-cee7d0fc0e94 | -12.5952 | -49.1046 | 2026-09-19 02:00:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| bc81e886-04af-3510-882d-d29fa3545162 | -3.2314 | -46.9376 | 2026-09-19 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| a3389d42-1a6d-3d95-a766-b1161f95f691 | -7.6386 | -46.103 | 2026-09-19 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 5fae60a3-6687-3e5e-87d9-ab199749de55 | -2.8974 | -57.7987 | 2026-09-19 02:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 871d857b-60fd-389d-82db-0d23370b1eb6 | -5.6246 | -45.2518 | 2026-09-19 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 5eaba97a-ec58-302c-b19e-10ccb3492084 | -2.8101 | -50.4658 | 2026-09-19 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| a421035b-76c3-33c8-9f89-5667b7fd2277 | -10.7115 | -60.7312 | 2026-09-19 02:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 112.0 |
| ebdd7de8-53f4-3314-80a8-eed6e17b1728 | -2.8286 | -50.4444 | 2026-09-19 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| ac51b4b2-bdf4-37c1-8fef-52c2308ef579 | -3.2313 | -46.9596 | 2026-09-19 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 1cc8aab5-fcb7-3c37-9157-2df1aaa691ae | -5.6059 | -45.2531 | 2026-09-19 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 385439e2-a75f-3e43-affa-d0e4e0904290 | -2.8285 | -50.4653 | 2026-09-19 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 23e32d70-394f-3c83-8a44-800bcae7a60b | -3.2314 | -46.9376 | 2026-09-19 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 4fd71a21-96ca-3316-8d82-097feab2f835 | -3.3311 | -59.8101 | 2026-09-19 02:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 89d0522a-a4db-31e9-8aa5-cf9400b00a5c | -2.8101 | -50.4658 | 2026-09-19 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| abf58116-a285-38d3-9f26-9a2d2026808b | -7.7626 | -46.7612 | 2026-09-19 02:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 6cbe60e1-c36a-3805-8351-863c126eb0da | -16.7951 | -46.9879 | 2026-09-19 02:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 55.8 |
| e8bbc127-e6f6-38af-8600-589d33472c48 | -7.7629 | -46.7389 | 2026-09-19 02:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 6778eeec-c50c-336f-86ba-72be1b853442 | -2.9157 | -57.8177 | 2026-09-19 02:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 431e3b81-5914-367b-9516-001b604481db | -3.2313 | -46.9596 | 2026-09-19 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| ef95fed3-7810-3410-98e7-1bf9a4b764ab | -2.8974 | -57.8181 | 2026-09-19 02:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 18400f25-674b-34ea-ab54-89b7873a0bae | -7.7817 | -46.7372 | 2026-09-19 02:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| b2b80abe-6c07-3086-8445-7b07496823b8 | -2.8974 | -57.7987 | 2026-09-19 02:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 482c7c99-c141-322c-b3f5-1aeab03d8f65 | -2.8285 | -50.4653 | 2026-09-19 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 189269a6-c760-3121-bfa5-46d7b7fb6dd2 | -10.7115 | -60.7312 | 2026-09-19 02:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 109.6 |
| e661a3d8-e383-3b17-997c-11b21980d519 | -2.9157 | -57.7983 | 2026-09-19 02:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| a7749f18-2458-3e95-9ebc-d22f15966faf | -5.6246 | -45.2518 | 2026-09-19 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| e7fb793c-be87-330c-8473-0b8b9e61bb25 | -7.6386 | -46.103 | 2026-09-19 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| d1ca96b6-b69f-30c7-bb4c-d1e9a6a0a53b | -18.0274 | -51.0709 | 2026-09-19 02:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 032085ba-7352-37df-8252-ff98c17e2d8c | -3.3311 | -59.8101 | 2026-09-19 02:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| cbfe8494-5c46-39c8-b126-f623796cd2dd | -10.7115 | -60.7312 | 2026-09-19 02:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 479784ba-5e94-3107-a593-41f7a4db5937 | -2.8975 | -57.7793 | 2026-09-19 02:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 97fc1f25-fa62-3717-8b90-aad093469707 | -7.7629 | -46.7389 | 2026-09-19 02:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 8a40d67b-b031-3503-bce7-bb9ddd5f62b4 | -2.9157 | -57.8177 | 2026-09-19 02:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| a0476d2b-edff-314e-9665-ee672d99f380 | -2.9157 | -57.7983 | 2026-09-19 02:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 13e7e92d-e399-3046-ae5d-384c29243ff0 | -2.8101 | -50.4658 | 2026-09-19 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 5ff838b9-928b-3d7d-abde-2a9f6909336d | -2.8974 | -57.8181 | 2026-09-19 02:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 0d74a06f-13b4-3268-88a0-cd0c3b2d32ff | -7.7626 | -46.7612 | 2026-09-19 02:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| e59a0b30-aec0-3f46-9b17-797eff5fbef9 | -16.7951 | -46.9879 | 2026-09-19 02:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 3bc3b2c4-6071-3b0e-bb7e-72edbaaf523c | -2.8974 | -57.7987 | 2026-09-19 02:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 118.0 |
| ea2c5554-5362-34bf-a967-7fda144c646c | -3.2313 | -46.9596 | 2026-09-19 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 838610c4-64ff-3407-91bb-eb2c1683458c | -8.776 | -46.9088 | 2026-09-19 02:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 9172e36f-e0b2-385b-aa76-3a86ec78b7fb | -2.8285 | -50.4653 | 2026-09-19 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 3bcaa49a-2fd5-3ff4-ba42-a898fa321075 | -8.4983 | -57.6271 | 2026-09-19 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 6952d840-039b-3b6f-be31-5b6656ff01d5 | -10.6928 | -60.7322 | 2026-09-19 02:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 9c30473c-06aa-30f9-8d57-796207880bc5 | -3.2314 | -46.9376 | 2026-09-19 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 81ea1521-6a74-397c-bbbd-e39e1be50909 | -8.452 | -45.7092 | 2026-09-19 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 6e6188b9-25ca-3236-b2d2-cd87958422a2 | -10.7115 | -60.7312 | 2026-09-19 02:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 80ecb2c7-3959-37b6-b660-a0a822e67275 | -8.776 | -46.9088 | 2026-09-19 02:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 898ca096-cce5-36f9-9eaf-fd52f9a6d2d5 | -2.8101 | -50.4658 | 2026-09-19 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| bb690948-b205-3bbc-b933-d4184033a504 | -3.2314 | -46.9376 | 2026-09-19 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 5b0137fe-dae5-3f7a-bf28-9fb19f4c2f62 | -10.6928 | -60.7322 | 2026-09-19 02:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| fa1a2a93-ea5e-3f89-9586-70b51b419362 | -2.8284 | -50.4863 | 2026-09-19 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 8ca686ae-32dc-31a7-841a-55fbbd9f435b | -3.3311 | -59.8101 | 2026-09-19 02:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 946a6895-ce4b-3022-8184-692485beea18 | -19.5735 | -47.6534 | 2026-09-19 02:30:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 63.7 |
| b05f7b74-0e3f-3731-99b4-751086bf1d50 | -2.8285 | -50.4653 | 2026-09-19 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 1259cbe8-1ee9-3e4f-bcd2-e84e8d8f814c | -12.5952 | -49.1046 | 2026-09-19 02:30:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| c6142370-7936-3263-aae3-6c406a289694 | -8.7757 | -46.931 | 2026-09-19 02:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |


[Clique aqui para ver as próximas entradas](README25.md)
