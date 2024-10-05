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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 002895e9-6c47-30d7-b4d0-b56daa837179 | -4.9451 | -43.7888 | 2024-10-05 01:25:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 7c03704d-efea-32ed-aa0e-8da212012714 | -4.9452 | -43.7657 | 2024-10-05 01:25:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| ea22f909-bd81-373a-af6d-9146fd34df41 | -5.8214 | -44.1426 | 2024-10-05 01:25:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| a74f2a43-8e3a-3214-a504-b663f445e6c8 | -5.8216 | -44.1196 | 2024-10-05 01:25:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 68aacf52-469f-334b-97ec-7aa5db697707 | -5.9155 | -53.4356 | 2024-10-05 01:25:40 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 73fa7c61-d4b3-3672-b204-3b5caef7b649 | -7.0233 | -59.3918 | 2024-10-05 01:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 2f898367-fe00-375a-91b1-a16628c7d909 | -7.1346 | -59.3099 | 2024-10-05 01:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 62eff98d-aed2-3d7f-befc-27aca83b19d1 | -7.153 | -59.3092 | 2024-10-05 01:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 9b6d6b19-fd75-3b11-8a18-b3dec1b43d45 | -7.7362 | -49.2297 | 2024-10-05 01:25:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 94.2 |
| c476e64a-d2a5-3b8a-b27a-36c69d10ec1e | -7.7364 | -49.2082 | 2024-10-05 01:25:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 95.2 |
| a4c09f06-a368-35e7-931a-d89be3012413 | -7.7549 | -49.2282 | 2024-10-05 01:25:50 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 1afe56a5-213b-35bf-aeda-e09910643b67 | -7.7551 | -49.2067 | 2024-10-05 01:25:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 904c0c41-367c-38dc-8cb5-c411d57cf130 | -8.6555 | -49.1083 | 2024-10-05 01:25:55 | GOES-16 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 43e0b1b0-20cf-31f4-ba29-dd6c2b4e649c | -8.7957 | -49.9747 | 2024-10-05 01:25:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 687039c6-6ca6-35aa-9295-5293baae9fa4 | -8.7959 | -49.9533 | 2024-10-05 01:25:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 598dc201-9556-3411-9c38-a49d9581be59 | -8.653 | -62.0979 | 2024-10-05 01:25:56 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 5ff1cb68-1f97-3c2d-afcb-7d74c8f91270 | -8.6716 | -62.0971 | 2024-10-05 01:25:56 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| fa47363f-1dff-3999-ad33-9813c85dcafe | -8.7772 | -49.955 | 2024-10-05 01:25:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| a1397f58-3fc0-330c-8e18-21cf785609bb | -9.2839 | -65.4283 | 2024-10-05 01:25:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 3a56fa49-8604-326f-a2cf-b7c3c5435a46 | -9.284 | -65.4096 | 2024-10-05 01:25:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 3de71f1e-d1df-3533-b167-89398e3879c9 | -10.3126 | -50.5554 | 2024-10-05 01:26:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 3d8d006d-5977-3429-9dd2-3ae01279d39b | -10.3129 | -50.5341 | 2024-10-05 01:26:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 3adecf35-f397-3ec7-a6da-953333d5e448 | -10.3315 | -50.5535 | 2024-10-05 01:26:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 640a0f2f-b928-3aed-b93a-42339fc2b010 | -10.3318 | -50.5322 | 2024-10-05 01:26:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 89c79a91-f36b-3df1-aa72-27c5970fb00a | -10.4424 | -50.7336 | 2024-10-05 01:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 282b0333-ab3c-312f-8de1-c95801a6b688 | -10.5943 | -64.024 | 2024-10-05 01:26:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 9fe25f55-b82a-3aa1-b613-3b97053b4bfd | -11.1155 | -54.2319 | 2024-10-05 01:26:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 3e90e7de-9667-30d0-840b-c513ff04608c | -11.0966 | -54.2336 | 2024-10-05 01:26:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 70a396d5-dc57-36eb-aeea-217e1d3ca539 | -11.0969 | -54.2131 | 2024-10-05 01:26:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| b1031294-1f90-3b42-9fc9-510563693ff9 | -11.1158 | -54.2114 | 2024-10-05 01:26:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| da7c1936-5f5c-3507-b17d-833e826c26b5 | -15.5597 | -57.4553 | 2024-10-05 01:26:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| e1f99674-2994-388f-bae4-785f3ba121b7 | -15.5791 | -57.4532 | 2024-10-05 01:26:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 9aa8e4ff-d0c3-3299-929c-77a68edf2bd0 | -15.7151 | -57.4184 | 2024-10-05 01:26:35 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| c0034c87-5eaf-34f6-8b92-9c71d9001d4f | -16.0938 | -50.2543 | 2024-10-05 01:26:36 | GOES-16 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 68.3 |
| ca03eace-8fc5-3fd7-9614-24e1d8d8ea8c | -16.0942 | -50.2323 | 2024-10-05 01:26:36 | GOES-16 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 417b702e-e7e2-30b1-ba64-1415b5631b4d | -16.1134 | -50.2511 | 2024-10-05 01:26:36 | GOES-16 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 5ab7564b-e20d-3761-b721-419f76d842e4 | -16.1138 | -50.2291 | 2024-10-05 01:26:36 | GOES-16 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 0fb5dc4a-feee-3d44-8be5-efa6776942dc | -16.6598 | -55.5219 | 2024-10-05 01:26:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| daa3d66f-d084-3219-9b5c-dac7ec30063d | -16.6871 | -57.4536 | 2024-10-05 01:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.5 |
| c303aff3-dfb8-37e0-951b-a68c85379ca4 | -16.7452 | -57.4878 | 2024-10-05 01:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.4 |
| 0daccfea-f138-3928-ae3a-4038c26b49f4 | -16.7647 | -57.4856 | 2024-10-05 01:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 165.0 |
| 2a9ffaa7-7c49-3240-8be3-15d98187b9bf | -16.7843 | -57.4834 | 2024-10-05 01:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.1 |
| c69ffb08-63d9-3689-8ae6-81210e37b7f4 | -17.0888 | -56.7915 | 2024-10-05 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.7 |
| b9848341-f2f2-36ee-aa05-e5962ca88041 | -17.0892 | -56.7709 | 2024-10-05 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.9 |
| 43076ae5-9c56-36b7-893c-c9b063f49488 | -17.1178 | -57.4244 | 2024-10-05 01:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 167.7 |
| 2aab5fbf-e678-3de2-9ae5-b699e820e26b | -17.1182 | -57.4039 | 2024-10-05 01:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 214.8 |
| a9d91aa9-61da-35a3-90eb-eabe6452aecd | -17.1185 | -57.3834 | 2024-10-05 01:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.6 |
| 28cffe64-ded9-300d-8ebd-eae10f69c59d | -17.1375 | -57.4221 | 2024-10-05 01:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 157.3 |
| cdfc7b3a-6a39-35e0-a816-851b80da3e1b | -17.1378 | -57.4016 | 2024-10-05 01:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 211.5 |
| 482fa6b9-92ca-3142-94fa-3831beedac10 | -17.1381 | -57.381 | 2024-10-05 01:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.4 |
| 5bdb8e83-984b-38ed-ae1f-b3d00e4949d8 | -18.8809 | -43.6032 | 2024-10-05 01:26:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.9 |
| 4e9e9c17-cb79-39cd-860d-8025e48d4c49 | -18.8816 | -43.5785 | 2024-10-05 01:26:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 57.3 |
| f7509498-7caf-3a1f-8c52-fa4a5d194d19 | -18.6582 | -57.2967 | 2024-10-05 01:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 808a2775-def6-3b17-9a8a-00eb3c2423b8 | -18.6586 | -57.2759 | 2024-10-05 01:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.4 |
| 2de61ddc-7263-3eee-aeb9-5d90f397c291 | -18.6782 | -57.2941 | 2024-10-05 01:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.9 |
| 6c4f610b-abf9-3c0d-ab87-c0a5f3941014 | -18.6785 | -57.2734 | 2024-10-05 01:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 136.2 |
| 5438c64e-51a6-30b7-92a6-1f6976406707 | -19.0944 | -48.2415 | 2024-10-05 01:26:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 7c094381-2b74-3eef-ab59-3271a6e39e80 | -20.5904 | -51.3907 | 2024-10-05 01:27:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.1 |
| f5999b52-8ea7-35af-9f77-9bf6417cf08b | -1.0626 | -47.9269 | 2024-10-05 01:35:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 81af61ae-3c2a-337e-9e74-62de0ccf3898 | -2.8829 | -50.7147 | 2024-10-05 01:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 878e7f5c-279f-3929-a466-5e90c466e778 | -2.9014 | -50.7142 | 2024-10-05 01:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 5be4f132-1427-3ea9-93d6-fd09ef62c77b | -3.1432 | -50.2254 | 2024-10-05 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 1cf751aa-7b08-3a84-a11d-c284cbabb706 | -3.2349 | -50.3695 | 2024-10-05 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 86465324-d0b7-31ec-b4a8-fadff9dd5fcd | -3.2899 | -50.4725 | 2024-10-05 01:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| df498326-9bbd-3c16-9dfb-8dc50f30e0dd | -3.2899 | -50.4516 | 2024-10-05 01:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 0fc08a01-1496-3c4d-b6c2-680747b0f695 | -3.3083 | -50.4719 | 2024-10-05 01:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 0cae89ac-e2e7-35d7-8297-b7780f53f1cd | -3.3084 | -50.451 | 2024-10-05 01:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 2caa7d46-ec77-3fe6-b87f-bcb75088f5a1 | -3.3268 | -50.4713 | 2024-10-05 01:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| adbd8474-e7e9-32ed-838a-d836a6728b55 | -3.3269 | -50.4504 | 2024-10-05 01:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 833cdf35-e38f-3b16-83bd-ef14fa05074d | -3.618 | -47.5352 | 2024-10-05 01:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| d5fb0cfe-fb4e-3c16-8153-c282c6524550 | -3.6181 | -47.5134 | 2024-10-05 01:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 83cb34a5-7239-3ab4-b9f7-859290ad4609 | -4.0148 | -43.2408 | 2024-10-05 01:35:29 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 4801e375-bfd6-394c-9fd8-f851cc2ad234 | -4.9451 | -43.7888 | 2024-10-05 01:35:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 5f5868a6-ba0f-3f74-8411-7ee91ee4ca22 | -4.9452 | -43.7657 | 2024-10-05 01:35:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 559161e9-55b3-3bc1-b9a2-d65de63b414c | -5.8214 | -44.1426 | 2024-10-05 01:35:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 3df75cca-69ae-3932-b099-5c8855e3248d | -5.8216 | -44.1196 | 2024-10-05 01:35:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 2e22c593-416f-360e-9a32-2b8333cccd02 | -5.897 | -53.4365 | 2024-10-05 01:35:40 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 49293f84-1693-3f85-ac8a-6f6ee47c0783 | -7.1346 | -59.3099 | 2024-10-05 01:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 46011eeb-6615-33a4-9718-9313953f496c | -7.7362 | -49.2297 | 2024-10-05 01:35:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 933ce43a-14e9-3297-8590-d37668abc697 | -7.7364 | -49.2082 | 2024-10-05 01:35:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 49375090-2e92-3033-8168-73da69787a83 | -7.7549 | -49.2282 | 2024-10-05 01:35:50 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 5eabfe5d-b22b-3c15-aabe-b141406be751 | -7.7551 | -49.2067 | 2024-10-05 01:35:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 939e14d3-8de5-3eb2-904b-f398fe689931 | -8.7769 | -49.9763 | 2024-10-05 01:35:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 177d3bfa-94d6-38b9-a4d8-89d233349d4c | -8.7772 | -49.955 | 2024-10-05 01:35:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 4921c152-012f-3258-b439-b71a57dad042 | -8.7957 | -49.9747 | 2024-10-05 01:35:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| be654f95-9139-3847-9cbb-e7cec8d84446 | -8.7959 | -49.9533 | 2024-10-05 01:35:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 8929b759-04f8-32d1-923b-12afa4b0e701 | -9.2839 | -65.4283 | 2024-10-05 01:35:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| e435d4c2-f7d7-34d2-a861-330c4f72826b | -9.284 | -65.4096 | 2024-10-05 01:35:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| a1716fab-a171-3076-bb03-83fc2b028859 | -10.3129 | -50.5341 | 2024-10-05 01:36:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 56bccef8-d223-3592-82e3-c055a962c0ac | -10.3126 | -50.5554 | 2024-10-05 01:36:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 6f192ed3-b9bf-38b0-a8b4-c7c783b1da00 | -10.4424 | -50.7336 | 2024-10-05 01:36:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 3cce5405-6c71-368d-a1e2-65648b8c392c | -10.5943 | -64.024 | 2024-10-05 01:36:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 7431bb1d-731f-3e2e-b26f-aec6117c86ac | -11.0966 | -54.2336 | 2024-10-05 01:36:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 9ede9e9a-3825-3070-bd6e-af758dec92a3 | -11.1155 | -54.2319 | 2024-10-05 01:36:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 2bbc488c-e037-37b9-aefc-2348fdf1db0d | -11.1158 | -54.2114 | 2024-10-05 01:36:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 5f950354-19fe-3828-87f2-736d9c2df995 | -12.7623 | -50.5782 | 2024-10-05 01:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| ff4bc8ff-6114-3de3-b3eb-faab1e827f5c | -12.7627 | -50.5567 | 2024-10-05 01:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.1 |
| f7d0d6e7-ebfb-36c1-8bf2-33cb95e5c56c | -12.7815 | -50.5758 | 2024-10-05 01:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| cc81fe61-121a-3284-a1cf-77db7a32268a | -12.7819 | -50.5543 | 2024-10-05 01:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 165.0 |
| c780acc1-21d0-3d61-a845-fe06c3ff6f93 | -12.801 | -50.5519 | 2024-10-05 01:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |


[Clique aqui para ver as próximas entradas](README24.md)
