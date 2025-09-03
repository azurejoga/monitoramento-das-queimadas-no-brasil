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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c83880e-2007-349e-ac1a-7b7669c78621 | -5.8828 | -57.722099 | 2025-09-03 01:17:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7049898c-d878-3196-bde7-2bd1fcee5547 | -5.8693 | -57.708801 | 2025-09-03 01:17:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82b84646-40f1-38fe-9261-dade48e5b054 | -20.841801 | -50.110901 | 2025-09-03 01:17:00 | METOP-B | MONÇÕES | SÃO PAULO | Brasil | 3531001 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 564f0d7c-4d4e-3732-9ece-64d510587db1 | -11.5447 | -52.114399 | 2025-09-03 01:17:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dc4215a5-eb83-35d7-a4d7-942fd979a89b | -18.085501 | -51.745998 | 2025-09-03 01:17:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 455f5345-c912-3a1e-bede-cf3f104b953d | -5.8612 | -57.760502 | 2025-09-03 01:17:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fbb654d-053d-37c0-9fcc-64e06813c39b | -11.5624 | -52.142101 | 2025-09-03 01:17:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 807f4c96-3bdf-373c-a6fb-aca618d589eb | -5.8478 | -57.7472 | 2025-09-03 01:17:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6dee03ae-e900-3c3a-8899-f10165c52137 | -5.879 | -57.706402 | 2025-09-03 01:17:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6220ade1-26f7-34a1-8d5b-67d70c7123ca | -11.5638 | -52.109001 | 2025-09-03 01:17:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3296ff67-59b0-36cb-b8a3-72dd6251efa6 | -12.8919 | -56.974602 | 2025-09-03 01:17:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9f4efcc4-fa6e-3479-adb4-4aaedc4dc01d | -5.8596 | -57.711102 | 2025-09-03 01:17:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fa66520-3082-31f5-affc-3acef0a4737e | -12.5968 | -56.993 | 2025-09-03 01:17:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3061369c-5e1d-3912-bd5f-fa0cf5b6059f | -7.6276 | -61.083 | 2025-09-03 01:17:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 781b1e92-5251-30d3-a2bd-aa2fa7d379fe | -12.8987 | -57.0019 | 2025-09-03 01:17:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6b7a7efc-22ea-3719-a2c2-fb23f5f04e4f | -12.8759 | -56.993301 | 2025-09-03 01:17:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 28b5a9cb-151c-3c81-b6a9-65aecbfe92e9 | -5.8575 | -57.7449 | 2025-09-03 01:17:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89ff7d66-64f3-3920-9667-9a7876866a75 | -5.8262 | -57.7854 | 2025-09-03 01:17:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5c61a7d-566a-36db-aa81-c481e16d5847 | -5.8672 | -57.7425 | 2025-09-03 01:17:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6e9ffb5-e786-32b5-a3be-7f184e8bfc5a | -11.5651 | -52.075901 | 2025-09-03 01:17:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 21693622-e28a-37a4-9885-967e912a5e26 | -11.546 | -52.0812 | 2025-09-03 01:17:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 918f9879-9e5d-31a9-8596-a5afe6439f73 | -5.8769 | -57.7402 | 2025-09-03 01:17:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1c9ef2b-5a67-3d59-b949-ca34fecc062c | -7.5092 | -61.327 | 2025-09-03 01:17:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3bab8119-2bb7-34bd-ae13-9c2475734da3 | -12.8982 | -56.958401 | 2025-09-03 01:17:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7e1e25b-5957-3aab-b1fc-d982a5432621 | -7.6318 | -61.101002 | 2025-09-03 01:17:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 22a8566a-ef34-3783-8aa4-97a03d14b331 | -12.8719 | -56.935902 | 2025-09-03 01:17:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 73e5680f-e0d8-336c-bff2-539cb23d6b36 | -5.8537 | -57.729198 | 2025-09-03 01:17:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cf2f627-3334-3c78-ad71-f2a006137eb8 | -12.8885 | -56.960899 | 2025-09-03 01:17:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 872247b4-b16a-3225-9ea8-89232a29b3b4 | -15.5652 | -48.4143 | 2025-09-03 01:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 27305a62-82e2-3dcf-94ae-be1ee3e7bc10 | -4.8936 | -43.1882 | 2025-09-03 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| da6c56ac-3049-3cf1-9f6d-bcb217f1835a | -9.3394 | -55.2277 | 2025-09-03 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| f2d69b99-bacf-3c5d-98e6-afade967df88 | -3.2305 | -47.135 | 2025-09-03 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 168.5 |
| 166b4f78-b0d2-38f0-8503-d555da019b3f | -10.0932 | -54.7667 | 2025-09-03 01:20:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 25.7 |
| d2b2fe00-3e44-33a7-8ecc-df337bdab49d | -5.6266 | -45.0252 | 2025-09-03 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 9ef59b24-d09a-378d-bd7e-9b1d97057ee6 | -7.5476 | -61.3437 | 2025-09-03 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 2a4b8bdf-a9ac-3e32-8014-a8408594109b | -11.1033 | -44.6548 | 2025-09-03 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 7beaf960-f8b6-3ead-a8ee-751d30829a47 | -7.5477 | -61.3247 | 2025-09-03 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 4c5360cc-012e-3eca-a51c-b3c54e86d0ac | -7.5291 | -61.3444 | 2025-09-03 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| d5cf7f75-984a-39e5-83b4-f845d52463f0 | -3.2306 | -47.1131 | 2025-09-03 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 065f41df-108b-39b0-a37f-e7b3a957c047 | -8.8842 | -45.822 | 2025-09-03 01:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 101d7ec0-e305-3acd-97ac-dce6a2008219 | -15.5656 | -48.3918 | 2025-09-03 01:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 85.0 |
| f89f0103-82c6-346b-8634-da6d2c556db1 | -12.6341 | -56.9926 | 2025-09-03 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 34f66d02-b7ad-33b7-b806-96ea2421867c | -11.1228 | -44.6288 | 2025-09-03 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 5759db86-118c-3295-83fe-d27c82bcb6ac | -10.4853 | -50.346 | 2025-09-03 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 434bb5f1-3f4b-39cf-bfcb-ecca995f4e95 | -8.3644 | -48.3116 | 2025-09-03 01:20:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 6430ef89-acbb-370d-83c7-2a38ba476b6a | -11.1224 | -44.6521 | 2025-09-03 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 88636b83-ecd8-31b0-8213-7f01452e9c4b | -5.6079 | -45.0265 | 2025-09-03 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 89b13a78-417d-3b2c-8cee-c4ca662b0de5 | -7.6783 | -61.0908 | 2025-09-03 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 1bad5344-1ac2-3b32-b759-45de40daaf82 | -7.5302 | -47.4443 | 2025-09-03 01:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 45.3 |
| f8895e32-1e86-3894-9708-29c9af16e8af | -4.912 | -43.2337 | 2025-09-03 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| c732917e-5abc-3645-8f30-a47730bb9008 | -11.122 | -44.6753 | 2025-09-03 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 782d68b4-7fa9-30b7-a858-29dfb257f38c | -5.6081 | -45.0038 | 2025-09-03 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| fca3c99a-fd7d-3351-b6c2-2a284f09d7d5 | -3.212 | -47.1357 | 2025-09-03 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 841c5ab0-a455-3578-97a3-f38b4fafb5c3 | -6.4648 | -49.5151 | 2025-09-03 01:20:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| ebc51edf-ce11-3728-988c-f48acf8cde7c | -7.7039 | -48.7371 | 2025-09-03 01:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 9a8dee11-a00d-3709-a50e-22e49e394414 | -4.8933 | -43.2349 | 2025-09-03 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 125.6 |
| fd2d7473-184c-3339-8420-2687a899ce59 | -4.8935 | -43.2115 | 2025-09-03 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 284.6 |
| 9a0322a9-75f4-39c2-9783-e757692811f6 | -4.9122 | -43.2103 | 2025-09-03 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 8454e8a6-3618-37a0-8529-6afa771c27f5 | -5.6268 | -45.0025 | 2025-09-03 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 2402eb21-ee70-306b-be04-3fd89bd5e094 | -7.7036 | -48.7587 | 2025-09-03 01:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 1295b1b0-72a3-3476-b2ad-f706de1e0ddc | -7.8975 | -46.4594 | 2025-09-03 01:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 2c6809df-8fe4-3625-9af0-1c797af128b6 | -4.1604 | -46.7881 | 2025-09-03 01:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 7c3ed55f-154c-3bde-9f62-d8244bf5efb4 | -6.4646 | -49.5364 | 2025-09-03 01:20:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 880830fc-350d-31e6-97e3-e30f9b91dd32 | -15.5656 | -48.3918 | 2025-09-03 01:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 79ab054e-08c5-38cb-880d-1f4ac89db9e7 | -12.9573 | -56.9839 | 2025-09-03 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 126.4 |
| b1bd0c28-71ee-3e0d-ab30-ee304772aad7 | -3.2306 | -47.1131 | 2025-09-03 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 8e0d12d7-fa24-3f5c-8703-76734b14c450 | -8.3644 | -48.3116 | 2025-09-03 01:30:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 2f0ec87b-6821-3592-adc1-e2810ee2be91 | -12.6341 | -56.9926 | 2025-09-03 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 2fcfa465-bcd5-3bcc-9afb-707d2d71fd96 | -4.9122 | -43.2103 | 2025-09-03 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 141.9 |
| b5733665-cd99-303d-bee8-01bc58fdf7d7 | -4.912 | -43.2337 | 2025-09-03 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 9b78815c-33c6-3739-b642-326e347be179 | -7.7039 | -48.7371 | 2025-09-03 01:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 64.3 |
| c2496436-c5a4-3932-8ca0-338479dde449 | -4.8936 | -43.1882 | 2025-09-03 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 340d4a5d-856e-3c45-aa2d-2c2738c9c8d5 | -7.5476 | -61.3437 | 2025-09-03 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 487c8edc-ffea-3ce2-b970-fdc702a039cb | -3.212 | -47.1357 | 2025-09-03 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 8bb11b5f-9f29-3255-8640-d0997669cd7b | -7.7036 | -48.7587 | 2025-09-03 01:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 9e667bad-8089-358e-a84d-892ee890b048 | -7.6783 | -61.0908 | 2025-09-03 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 05841bed-b84c-3ac7-84a5-b145670e7855 | -7.7226 | -48.7355 | 2025-09-03 01:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 643a827f-e9e7-3d1d-8473-c8f1ae84a276 | -9.3394 | -55.2277 | 2025-09-03 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 72660b77-b8f1-308f-8683-b03e1c1c2842 | -7.5477 | -61.3247 | 2025-09-03 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 1be74cf8-95c5-335c-9a75-939600a81c16 | -12.9385 | -56.9655 | 2025-09-03 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 148.4 |
| 8f24ce48-3c43-3663-9743-be904a92fb92 | -10.4853 | -50.346 | 2025-09-03 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 7da5ba11-6379-3181-b706-8dbe1b32c8b6 | -3.2305 | -47.135 | 2025-09-03 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 147.6 |
| b5ccd318-a15e-3f5e-8180-5f8b084a3434 | -4.8933 | -43.2349 | 2025-09-03 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 9391bf65-8b61-3090-98ad-5f5ac3ebddfe | -11.1228 | -44.6288 | 2025-09-03 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 7e4867c5-3752-3b8c-b6da-1475c3b70663 | -12.9382 | -56.9856 | 2025-09-03 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 219.7 |
| 94fae6db-e87d-3435-a6b8-004dd64c2b24 | -5.6079 | -45.0265 | 2025-09-03 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| f1c0d6dc-2f6d-3374-b6c4-476a5f994186 | -12.938 | -57.0057 | 2025-09-03 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| b3736aa5-3392-34bb-aa3a-e6e14281f96d | -3.2121 | -47.1138 | 2025-09-03 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| b887e7c6-d513-3889-bce5-7de6a843cf41 | -5.6081 | -45.0038 | 2025-09-03 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 4224d355-b4a1-32af-9a78-cd6ada7a3fb0 | -11.1224 | -44.6521 | 2025-09-03 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 149.0 |
| c9c726ed-766c-39f2-b397-cec6952802d0 | -15.5652 | -48.4143 | 2025-09-03 01:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 17fbe657-bb27-3073-9362-f157a0cee0f3 | -12.9387 | -56.9454 | 2025-09-03 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| dc78699f-6126-3fee-9536-04175f771f01 | -8.8842 | -45.822 | 2025-09-03 01:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 99bf1e99-4abe-3a0e-a278-1c08e59fd95e | -7.5291 | -61.3444 | 2025-09-03 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 79e41d1d-f06b-34ae-b040-3ad813f9b0e8 | -12.8436 | -48.035 | 2025-09-03 01:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| b9302911-62f2-311a-98d6-efeb6f9fdeeb | -4.8935 | -43.2115 | 2025-09-03 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 208.3 |
| 9cc645df-a3e0-31d9-b813-a22d5753588a | -4.1604 | -46.7881 | 2025-09-03 01:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 30ae899e-f34b-3a98-95b5-30c81afd57bd | -12.9189 | -57.0074 | 2025-09-03 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 963db317-8836-3d8e-a81f-7e2a79d566e9 | -7.7413 | -48.734 | 2025-09-03 01:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 67.8 |
| f88dc4a7-7a30-3022-97cd-8f841f83560f | -7.7224 | -48.7572 | 2025-09-03 01:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 82.0 |


[Clique aqui para ver as próximas entradas](README18.md)
