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
| f3eb5236-99cb-3eff-9839-a44a2a4fee61 | -10.40646 | -46.655 | 2026-05-13 05:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 34efbd15-034a-3f50-bbce-eb088278711d | -11.1838 | -55.9229 | 2026-05-13 05:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 960a6b35-ab36-397c-993a-2a09d42d9390 | -11.17973 | -55.9263 | 2026-05-13 05:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 44b77c9a-3b14-38dc-884b-324e51c8b87c | -8.70807 | -47.98011 | 2026-05-13 05:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54160939-3e16-3f63-a6c6-89469c8af92f | -11.30692 | -54.03107 | 2026-05-13 05:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2137a5e-fb15-3f77-8f7d-c90edc956339 | -11.74349 | -54.23413 | 2026-05-13 05:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81202479-dcc9-3b1b-9e61-34a7cea8afe8 | -14.11624 | -45.31528 | 2026-05-13 05:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3cfab32-348b-3173-a09d-0e5e582e92f9 | -11.40703 | -48.44315 | 2026-05-13 05:14:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 185e30d7-32a7-3e8c-aad4-2cea30d8489c | -11.73832 | -54.24319 | 2026-05-13 05:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de1081b2-ac5e-3acf-a867-76b3d883e9ed | -11.18322 | -55.92683 | 2026-05-13 05:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d51ded61-10dc-360c-adfc-a53764af2bf2 | -11.97217 | -46.7824 | 2026-05-13 05:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5717e8a6-b02e-3b89-bdab-37e0d32dd328 | -11.84039 | -49.44244 | 2026-05-13 05:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e615fc22-d34a-3ee4-aa5e-f7118bfa1cc6 | -9.45031 | -47.79006 | 2026-05-13 05:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 299ed732-14c3-3156-a8bf-fb31e53750f3 | -10.40451 | -46.65897 | 2026-05-13 05:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3c7d0fa0-cbb3-3d7f-b189-f1967853cbe5 | -10.48333 | -49.36105 | 2026-05-13 05:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8ff137d-debe-3ad5-a3a3-2b86975168de | -11.73559 | -54.24552 | 2026-05-13 05:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7ae0111f-3460-33cb-902d-f7001d6e17de | -14.12393 | -45.30925 | 2026-05-13 05:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a2fd837-4291-3d31-a1ed-08e4cb8e3366 | -10.48395 | -49.36162 | 2026-05-13 05:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 39a71de7-d6fe-37b0-ab0f-65d39ffd68a9 | -11.92938 | -54.1005 | 2026-05-13 05:14:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aede4c37-02c0-35fe-9d8f-811b175f38ed | -11.29287 | -54.0192 | 2026-05-13 05:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33297351-7df6-3e12-aabe-3e7026eda042 | -14.13411 | -45.41998 | 2026-05-13 05:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8793a43f-af39-3547-9b88-ea25bf43719b | -11.26389 | -55.79394 | 2026-05-13 05:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf36181c-ecfb-3912-87aa-18d6921fc48d | -14.11779 | -45.31945 | 2026-05-13 05:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 67a972b5-e0bc-333a-8d91-d44f10a5a312 | -11.73942 | -54.24606 | 2026-05-13 05:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f2e2814-a7e4-3688-94f7-a5c54b98247a | -14.12552 | -45.31344 | 2026-05-13 05:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d4f85c8-e869-373f-af15-ee4afa20c781 | -11.73765 | -54.24796 | 2026-05-13 05:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fe398ec-80b0-3ec2-abab-a4dd245f6db3 | -9.45601 | -47.79087 | 2026-05-13 05:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb040043-749f-31c0-8696-02c1c44f2de6 | -11.2674 | -55.79448 | 2026-05-13 05:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5427fbb5-e4f0-3476-985e-88378b60bef5 | -18.49499 | -55.51979 | 2026-05-13 05:16:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 14b6c6f8-fa6d-39bf-b336-158741289c45 | -21.33501 | -47.02774 | 2026-05-13 05:16:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 29c06bcd-e341-3d75-8983-da6fba330e2a | -16.06694 | -59.69179 | 2026-05-13 05:16:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 304c1694-cd9d-3e23-906a-18214a16c8b3 | -21.97383 | -57.58914 | 2026-05-13 05:18:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be6f502f-693f-3fe1-a6f6-0c847e067717 | -21.9749 | -57.5876 | 2026-05-13 05:18:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a391dc7-564d-3935-bb6d-e20c61af2463 | -10.67688 | -42.15203 | 2026-05-13 05:55:00 | AQUA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| b580f606-63fc-3d19-81ad-47ecdf468bdf | -14.1487 | -45.4242 | 2026-05-13 11:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 00634d56-46b4-3f05-8e16-08e19ceeffab | -11.9305 | -43.3812 | 2026-05-13 11:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 6d9a4219-9075-32d8-b52d-0379b32945df | -13.9615 | -46.0334 | 2026-05-13 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 1aecbe28-ce77-3a9c-8f98-b1f4c903758b | -11.9305 | -43.3812 | 2026-05-13 12:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 126.9 |
| a8696390-3c0d-3416-acbd-0c909416bf22 | -14.1492 | -45.4009 | 2026-05-13 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 0ba85991-fd60-34e8-8d2c-3b20366a2a16 | -11.9305 | -43.3812 | 2026-05-13 12:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 133.0 |
| f3231315-85e3-3fd5-bbb0-45d9e75824d1 | -11.9305 | -43.3812 | 2026-05-13 12:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 9649e369-be1b-35d7-870b-86db2b4e6e5c | -11.9305 | -43.3812 | 2026-05-13 12:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 0f6e9203-4c25-3bc5-b5d1-f6c54136e324 | -8.5374 | -51.57809 | 2026-05-13 12:36:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 82b13160-983a-3682-a3ae-312c607921b0 | -9.46173 | -50.88894 | 2026-05-13 12:36:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 950765c4-1df4-372c-bac1-a47b6c901a21 | -10.39514 | -54.49372 | 2026-05-13 12:36:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 8ca2c32f-4c54-3657-a704-ad5b776ee261 | -8.54286 | -51.56594 | 2026-05-13 12:36:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| d8238800-46d3-3283-b26d-4d8b44693e51 | -13.15739 | -56.81851 | 2026-05-13 12:38:00 | TERRA_M-T | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3ea0b0bb-5d73-3499-865f-99097d66746f | -12.54071 | -57.21731 | 2026-05-13 12:38:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 39.3 |
| e9b2d6d6-3aa6-3e1a-93d1-6724bb99e9fc | -11.26518 | -54.70597 | 2026-05-13 12:38:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8cf76004-1744-3887-a541-9a336dc3717c | -11.18233 | -55.92203 | 2026-05-13 12:38:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 26de29d0-77ae-3670-9f8f-e231ee5686b3 | -12.5279 | -57.1775 | 2026-05-13 12:38:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e5c5205d-e8d4-31b3-a65c-4dad6ba6e78c | -12.542 | -57.208 | 2026-05-13 12:38:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 25.0 |
| d1851f0e-8bf0-337d-8d11-a870938f5974 | -16.43733 | -54.9062 | 2026-05-13 12:38:00 | TERRA_M-T | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 1811b9d9-b279-3ae5-8e7c-2bec27c899a1 | -11.63148 | -54.15506 | 2026-05-13 12:38:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| fb04d937-54da-3dc3-a386-aa7e23c16353 | -16.43565 | -54.9199 | 2026-05-13 12:38:00 | TERRA_M-T | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 81b40f36-3a6f-38ff-b993-6a36f2b74587 | -11.73369 | -54.24016 | 2026-05-13 12:38:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| eb3918f9-9f24-3eef-8777-58bb15bf6097 | -11.26635 | -54.70027 | 2026-05-13 12:38:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dea0a081-84a9-34b2-a015-3b91f4d4852c | -13.69893 | -55.67467 | 2026-05-13 12:38:00 | TERRA_M-T | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 6627fb16-740b-3981-a005-045d4f96ab52 | -11.74419 | -54.24142 | 2026-05-13 12:38:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 25.0 |
| d4090eb3-5ba5-3a2a-9b4c-7fcc111e8271 | -11.9305 | -43.3812 | 2026-05-13 12:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 03df9421-9eef-3454-b539-36cc2bba9805 | -11.9305 | -43.3812 | 2026-05-13 12:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 7d769971-8dfa-30d6-a669-7d1572898615 | -11.9305 | -43.3812 | 2026-05-13 13:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| f182aa0a-03b5-3e6b-ab7a-8580c37206a4 | -12.6205 | -44.5179 | 2026-05-13 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 97c62336-1815-3a64-a090-2e85c115a1b4 | -11.9305 | -43.3812 | 2026-05-13 13:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 150.4 |
| abca9d93-6da9-3cfc-90e7-7175f2695f23 | -11.9305 | -43.3812 | 2026-05-13 13:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 202ad84f-c390-38d5-98b4-de9724b74cb8 | -12.6205 | -44.5179 | 2026-05-13 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 621bb216-5773-37b2-b6ed-d156291a2c52 | -12.6205 | -44.5179 | 2026-05-13 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 2255d12f-d19e-37b1-8000-a2cfb4030a42 | -11.9305 | -43.3812 | 2026-05-13 13:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 122.9 |
| d55d66b9-b5f6-3bd7-bc56-8bf65a18b2ae | -12.6205 | -44.5179 | 2026-05-13 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| cacae5b1-e348-38e9-98c5-d4208b197bff | -11.9305 | -43.3812 | 2026-05-13 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 74da6659-0080-3690-90ee-78a81256b9b4 | -11.9305 | -43.3812 | 2026-05-13 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| cc3458b9-c274-331b-9049-097cabcd39f4 | -11.9305 | -43.3812 | 2026-05-13 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 158.6 |
| 4c69fb65-f521-3e13-b389-6235c498fa62 | -12.6205 | -44.5179 | 2026-05-13 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 8f2c6395-4360-3a37-9599-db119bb6b1fa | -11.9305 | -43.3812 | 2026-05-13 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 174.1 |
| fb2c6268-6a4c-377e-bf51-7ccdc4da61e8 | -11.9305 | -43.3812 | 2026-05-13 14:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 390c96b3-d7d0-36fd-8862-ec138f5c085d | -11.9305 | -43.3812 | 2026-05-13 14:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 170.4 |
| 33fd50ef-4a20-33db-9e12-2bce135384ce | -11.9498 | -43.3781 | 2026-05-13 14:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 05cc3a4f-b47a-3ef9-9365-43f8bfebafb6 | -11.9305 | -43.3812 | 2026-05-13 14:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 180.6 |
| b4633050-fd8a-330f-84c5-bf169b4fa9d7 | -11.9305 | -43.3812 | 2026-05-13 15:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 139.4 |


