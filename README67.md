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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d24e56ba-3eff-32b1-8456-45687ebfd798 | -10.5085 | -50.0228 | 2026-08-17 12:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 1d8bc44b-a232-3966-b729-d14363470878 | -7.4055 | -46.8368 | 2026-08-17 12:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 88234070-0150-3037-9b12-580a604831eb | -12.7009 | -48.5195 | 2026-08-17 12:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 48eb24de-cd21-3b8d-8f93-05f55f6739b4 | -11.1487 | -46.5219 | 2026-08-17 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 580.9 |
| 5097861e-69b9-39b4-b66e-050e7696724c | -11.17 | -46.52 | 2026-08-17 12:15:00 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 86624862-fdaa-30f1-b9a4-5f11e3f84cb4 | -11.14 | -46.52 | 2026-08-17 12:15:00 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a67eab8b-d277-3c1b-83ce-64c2b63e2945 | -11.149 | -46.4994 | 2026-08-17 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| f544cefa-b7ac-3a50-b7fc-af50c439c462 | -11.1487 | -46.5219 | 2026-08-17 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 436.2 |
| 05e6d247-7d79-396f-964a-4687b98dcfe6 | -7.6053 | -45.7238 | 2026-08-17 12:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| f27eb631-61ef-3f69-9ba5-745ae6c456af | -10.5085 | -50.0228 | 2026-08-17 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 176.7 |
| 08be2949-8ec2-36f5-9e78-ba9e148d2844 | -7.8071 | -47.8372 | 2026-08-17 12:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 63e33bae-2d88-321f-b3f9-73309e5300a9 | -12.7009 | -48.5195 | 2026-08-17 12:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 0c93a0ab-68ff-32e8-a186-a7620db9ff12 | -14.4871 | -51.9806 | 2026-08-17 12:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| bd9e37fc-adcc-3c35-af5f-fb67d7e60776 | -12.7009 | -48.5195 | 2026-08-17 12:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 989b3b48-9f1d-3961-970e-2325866fc3c6 | -14.8614 | -46.6581 | 2026-08-17 12:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 6096b7fd-a84f-3463-8c5b-b0602494b162 | -7.6053 | -45.7238 | 2026-08-17 12:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 5bd23d61-eb76-31ab-8e94-9b661dbbc480 | -12.7013 | -48.4974 | 2026-08-17 12:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 81ae7751-c5d5-3b8b-a608-a547661f306d | -10.5085 | -50.0228 | 2026-08-17 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 98b91f26-01ef-37ca-8515-f7f336c26313 | -13.5128 | -46.2219 | 2026-08-17 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 2e9c524a-78af-3c78-b613-76aa8d140935 | -12.6817 | -48.5221 | 2026-08-17 12:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 3863a09a-198c-36f7-9171-2e6374a42996 | -14.3722 | -51.932 | 2026-08-17 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 8fd6ad09-c6ef-3c27-addf-a5d3b18a1e7f | -11.4907 | -46.5892 | 2026-08-17 12:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 5f067ea1-27fc-391c-80d1-99d46c93cf0d | -11.1299 | -46.5019 | 2026-08-17 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| df93ed2d-3f16-3e00-b956-e473dc1fdb55 | -14.8614 | -46.6581 | 2026-08-17 12:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 909bf4f7-893d-330a-a89d-cbac94ab5965 | -10.6071 | -48.3873 | 2026-08-17 12:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| d8de40ab-e314-3b45-a3ec-35440f0d5a0e | -11.4911 | -46.5666 | 2026-08-17 12:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 917e1699-1b73-3795-8c57-1f49dae7c722 | -11.1487 | -46.5219 | 2026-08-17 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 938.4 |
| 2becee48-4b54-3c01-9f77-8744d5384da0 | -7.6053 | -45.7238 | 2026-08-17 12:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| abaead3d-86da-3c88-9ea9-4a4a7d6ff387 | -14.8619 | -46.6351 | 2026-08-17 12:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 9ebdf3f4-f8cf-3a6a-98b1-d8959663cb13 | -7.8071 | -47.8372 | 2026-08-17 12:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| f66660dd-c4bf-30d8-8db3-28b9ac60c9d2 | -14.2751 | -53.1287 | 2026-08-17 12:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| d6cebb25-6709-3e04-af11-3a3b59e667b3 | -9.7553 | -45.7237 | 2026-08-17 12:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 107.6 |
| daab9795-6322-33be-b275-8b69825c6b15 | -12.7013 | -48.4974 | 2026-08-17 12:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 36d1330c-92ae-3cfe-83f4-fe0a2a31707e | -12.7009 | -48.5195 | 2026-08-17 12:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 155.7 |
| f16b3382-4434-3963-af86-7a3a0720ea92 | -11.1296 | -46.5244 | 2026-08-17 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 131.0 |
| d2532c5c-cb65-3065-ad8f-d66065b9ab5a | -11.149 | -46.4994 | 2026-08-17 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 166.7 |
| e014161e-331f-3094-bd6c-ed3ecb1f3a1f | -6.6384 | -58.9636 | 2026-08-17 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| dbb5e25c-368b-33ff-818f-14ef99e0104d | -11.3235 | -46.3182 | 2026-08-17 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 9fadebe1-0315-3afe-8ea1-cb2d6878f154 | -11.4907 | -46.5892 | 2026-08-17 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 6e0ba1ce-dc54-3568-bb08-bcafb4da8280 | -11.3239 | -46.2955 | 2026-08-17 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| c25304f5-0ed6-3228-b55e-040d7536747b | -14.8619 | -46.6351 | 2026-08-17 12:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 82fb1a87-618a-3d74-bdf3-f0a19f69327b | -7.8071 | -47.8372 | 2026-08-17 12:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| a3ec77ca-0dd0-3d65-8b02-d59e26fe8d4c | -9.7553 | -45.7237 | 2026-08-17 12:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 833c1d93-c26e-3c13-ab3b-f0546bb21c54 | -14.3722 | -51.932 | 2026-08-17 12:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| d0c6d2c2-a451-33e6-95ce-dd783501b61d | -12.7013 | -48.4974 | 2026-08-17 12:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 6dd4eee4-ae63-3d3a-8a6c-91b5f3802b8b | -12.7009 | -48.5195 | 2026-08-17 12:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 124.2 |
| d1fb4d20-558c-3489-85d5-99007f6ddb08 | -7.6053 | -45.7238 | 2026-08-17 12:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 214.7 |
| f941e812-a6e7-3f13-9f80-b8cf33016802 | -10.5085 | -50.0228 | 2026-08-17 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| f3141ab0-0e1a-3bda-ae98-23554436d791 | -7.7881 | -47.8607 | 2026-08-17 12:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 45b9073b-3620-35b4-8df4-3a87d03d9233 | -14.8614 | -46.6581 | 2026-08-17 12:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 436bc15a-c40e-3bb2-8793-20f07d893eef | -7.8068 | -47.8591 | 2026-08-17 12:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 231.2 |
| 1313eddc-0a2e-3f05-bc4b-096603d75ecd | -9.3382 | -62.3344 | 2026-08-17 12:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 1d66476d-6e89-3626-bca5-9b484f7d4b45 | -2.17921 | -54.42321 | 2026-08-17 12:51:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| a1c71085-7bee-3506-9a65-bfdcbf5cf443 | -2.1812 | -54.41714 | 2026-08-17 12:51:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| f676a3f3-f0c9-31f3-b9dc-929bf6519d66 | -2.17719 | -54.44604 | 2026-08-17 12:51:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 61c63875-4d51-340f-beeb-e5b8adb926f0 | 0.4879 | -60.5912 | 2026-08-17 12:51:00 | TERRA_M-T | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ddd58553-55ed-3ce6-9878-7949da3e6076 | 1.67639 | -60.13533 | 2026-08-17 12:51:00 | TERRA_M-T | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7c90524d-d3de-3eb2-97d6-4ce24c314b73 | -7.40704 | -60.01136 | 2026-08-17 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 23c7bc5e-c8ec-37d5-b494-ff3c0dcf4cde | -6.78306 | -59.46983 | 2026-08-17 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 893729c5-1e07-3ded-aced-2b73655f1366 | -9.33818 | -62.34089 | 2026-08-17 12:53:00 | TERRA_M-T | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 5e1e3e37-2f38-380f-8cf9-d86e155e820b | -6.7775 | -59.75397 | 2026-08-17 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 3345db84-7483-3430-8b67-35acd900ab2d | -7.36958 | -55.48875 | 2026-08-17 12:53:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 1fa14b01-d6c3-34da-b8d7-311d193a0300 | -9.19992 | -60.7902 | 2026-08-17 12:53:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| c7b6debf-531e-31a3-9ea7-4678a4c2c385 | -8.09165 | -61.35925 | 2026-08-17 12:53:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 3f5edac8-8989-36b7-a6a3-07a8e6dc5c92 | -8.90421 | -60.54735 | 2026-08-17 12:53:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a0d93ffb-e643-3ce5-b3d5-46588592f5cd | -9.3289 | -62.33961 | 2026-08-17 12:53:00 | TERRA_M-T | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 78a9c361-7104-30a1-9ec3-716c6d6ed168 | -7.55504 | -61.1735 | 2026-08-17 12:53:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 8ed570e8-b0f4-32ce-961d-d14a1381d2ca | -7.58792 | -61.22173 | 2026-08-17 12:53:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f0802cf4-fe3e-3a98-84a2-44f3a5313d33 | -6.96757 | -59.29415 | 2026-08-17 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 7bad0836-d2bf-3d7b-818d-c70221dab334 | -9.33025 | -62.32972 | 2026-08-17 12:53:00 | TERRA_M-T | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 6f9f0226-da3e-3ddb-b8cd-545e286ff83e | -6.63063 | -59.06409 | 2026-08-17 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 60b36d4c-515f-3eeb-8479-74bef088bb9f | -9.2101 | -60.79153 | 2026-08-17 12:53:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| e20c05f7-6e54-308d-ae4d-18d475762c1c | -6.95656 | -59.29266 | 2026-08-17 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 5309f074-a560-346a-8698-cf17803a4785 | -8.90261 | -60.55968 | 2026-08-17 12:53:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 288c3f98-4534-3ff5-b911-bb14be4fab47 | -6.62873 | -59.0786 | 2026-08-17 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 0772c4d6-b049-3641-923b-bd5ce4e8168f | -7.87884 | -63.74712 | 2026-08-17 12:53:00 | TERRA_M-T | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fbe0af6a-3285-3abd-8994-1d0ee4038a65 | -6.65524 | -58.96302 | 2026-08-17 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 5a284112-f038-32e6-a388-51e5ee2c6583 | -8.09311 | -61.34847 | 2026-08-17 12:53:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 88eb4800-9f28-30f5-b8e9-0d3a10c9577d | -6.78671 | -59.44236 | 2026-08-17 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 38a92ded-df63-35c3-99ee-0a5e4000275b | -8.52938 | -54.88908 | 2026-08-17 12:53:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 7ba8098f-e794-3eec-993f-8eb77c8664bb | -7.5565 | -61.16272 | 2026-08-17 12:53:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8ae1b6a3-cc7f-3bda-9067-0cd430d8c03f | -7.45803 | -59.99805 | 2026-08-17 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 4d18e05b-caff-3956-90ba-790a1d16880a | -9.17613 | -59.66813 | 2026-08-17 12:53:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 48f77f9a-2179-304b-9678-c9d2cf5efc66 | -8.72664 | -62.90168 | 2026-08-17 12:53:00 | TERRA_M-T | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a8d955e2-9c95-3c5d-a541-25bcbb77cb90 | -7.88643 | -61.79515 | 2026-08-17 12:53:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a214b331-ca82-3fe2-b853-37dbda141299 | -6.65715 | -58.94851 | 2026-08-17 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| d0ec6e9c-1a60-3920-b3a9-58206375cd3a | -7.3829 | -55.49762 | 2026-08-17 12:53:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 6725e6ea-0fda-3bc0-a68a-08ac01750ef1 | -6.77574 | -59.76688 | 2026-08-17 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.8 |
| fa4b65f1-face-36a2-b658-c9cc914ef88d | -6.78489 | -59.45607 | 2026-08-17 12:53:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| ddb09fba-7c8b-3d6e-8ccf-2f50fb1bc28d | -11.72235 | -54.60111 | 2026-08-17 12:55:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 16a9a648-91a0-35e1-a072-5500c97cf864 | -10.94184 | -57.16026 | 2026-08-17 12:55:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 9f58ab60-d52d-3260-a142-801b67da837e | -10.94976 | -57.14267 | 2026-08-17 12:55:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 2da0f227-2cbe-3c53-a312-9517ec437c63 | -11.7083 | -54.6044 | 2026-08-17 12:55:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 419ccc04-7be8-3f78-bdd0-cc86725807b8 | -10.94479 | -57.13564 | 2026-08-17 12:55:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 734831f9-a7e4-3a0a-b3fc-93cbba03f615 | -10.91775 | -62.76787 | 2026-08-17 12:55:00 | TERRA_M-T | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 38dc6443-61b7-3c1f-940a-cfda0bae913b | -15.90869 | -55.51814 | 2026-08-17 12:57:00 | TERRA_M-T | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 42.6 |
| a4004b73-dd70-389e-829f-059905c0fa5f | -11.8294 | -51.7725 | 2026-08-17 13:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 949342ca-127a-3ab9-83ab-32ab3faef476 | -8.5212 | -54.9016 | 2026-08-17 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 81fd7db7-dc05-31eb-99c1-54fbe87cd6eb | -12.7009 | -48.5195 | 2026-08-17 13:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 645c2504-c22d-349b-b434-e032716f404c | -11.4907 | -46.5892 | 2026-08-17 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |


[Clique aqui para ver as próximas entradas](README68.md)
