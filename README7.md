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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 438c6ad6-2f57-3688-815d-a361ebc22ef5 | -14.485 | -46.0586 | 2025-08-23 01:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 36a1c73d-473f-34f1-a613-de77a209a70c | -9.5177 | -60.5653 | 2025-08-23 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 151.6 |
| e09fe6a1-f5c1-3824-b98f-2a7747663655 | -6.6044 | -44.5624 | 2025-08-23 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| eedf19e6-ed50-3fcb-9332-e1ab922a42d0 | -9.1895 | -59.6364 | 2025-08-23 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| e2d857c4-9cba-3624-b9d2-f76f165fa952 | -5.7615 | -57.5807 | 2025-08-23 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| ec45a7ac-2652-351c-baae-c72326377366 | -12.9921 | -45.2252 | 2025-08-23 01:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 90c28fb2-4893-3cf1-8db5-f29728954710 | -9.5366 | -60.5258 | 2025-08-23 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 50b431ec-a72a-3c8e-a7fa-832efd74d078 | -6.4327 | -41.2114 | 2025-08-23 01:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 132.4 |
| fed7339c-e61e-3d61-b265-acb014e4883f | -9.1712 | -59.5987 | 2025-08-23 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| f910abcb-2c42-32e6-93d3-181f0603caaa | -5.7614 | -57.6002 | 2025-08-23 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| fa577921-7700-3b64-a09a-cdc74e37b38d | -19.7497 | -45.7074 | 2025-08-23 01:00:00 | GOES-19 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 48.0 |
| d98b45e1-04be-3c5d-884f-43e0bb2957d9 | -19.7504 | -45.6834 | 2025-08-23 01:00:00 | GOES-19 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 45c6fcc5-bb42-3181-9711-16c3d80f278c | -17.2751 | -46.777 | 2025-08-23 01:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 87.7 |
| b3602a5c-f0f2-32cb-a5b6-7d1f2018f68c | -14.665 | -56.5952 | 2025-08-23 01:00:00 | GOES-19 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| f81a0c1d-756b-3b36-beeb-705f2b33f9d7 | -3.444 | -49.0297 | 2025-08-23 01:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| dc3b3946-21dc-3b12-a9f1-2da3ac54d505 | -7.0164 | -44.6413 | 2025-08-23 01:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 109.8 |
| d8e06f5d-22ec-30c6-8bd5-dd62f73bd0f5 | -16.2925 | -50.1121 | 2025-08-23 01:00:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 3577f043-e07e-346e-9a3a-5cc12671eb05 | -10.6122 | -55.413 | 2025-08-23 01:00:00 | GOES-19 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| f5ed4850-b77d-3850-85d1-ae74f1003944 | -14.684 | -56.6136 | 2025-08-23 01:00:00 | GOES-19 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 0e2c3b76-3dc2-34d3-b209-e774f88e16b5 | -6.5781 | -59.871 | 2025-08-23 01:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 194b5076-94aa-321e-a61c-acb2397c1892 | -9.1712 | -59.5987 | 2025-08-23 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| e8c468db-bd30-393b-80d1-31e985949536 | -17.2757 | -46.7538 | 2025-08-23 01:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 256368a2-51f9-399c-b245-0a87b227ddf5 | -5.7429 | -57.6009 | 2025-08-23 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 25d977e7-c72c-3c3d-97cb-3c4505802c4a | -17.2751 | -46.777 | 2025-08-23 01:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 201.3 |
| ce3d7e16-4954-3b7f-8cbd-b1d2430d6dc2 | -13.3781 | -46.1979 | 2025-08-23 01:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 32bf5713-7f87-3630-9bf0-831415c58431 | -6.4138 | -41.2132 | 2025-08-23 01:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 125.8 |
| ba06b7c2-f2e2-3202-9d21-8423f651ca6d | -17.5985 | -46.5481 | 2025-08-23 01:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 122.5 |
| eafd4f4b-8271-3fbc-a42c-11ac349587a7 | -3.444 | -49.0297 | 2025-08-23 01:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| f17d61a8-5b57-3444-af94-ccdc9ab0962f | -9.2083 | -59.6161 | 2025-08-23 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 75eed29b-15e8-3d58-aa36-0c83ddd753cb | -7.813 | -63.5656 | 2025-08-23 01:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 102.4 |
| b7b2fb26-bdd7-3813-a370-ba585fdc8857 | -7.0164 | -44.6413 | 2025-08-23 01:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| d55a73e3-6f7f-31b6-9e1c-40a5d7c97835 | -9.1897 | -59.6171 | 2025-08-23 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 61e2a88d-4ce3-3c55-acc3-862d52013de5 | -5.7615 | -57.5807 | 2025-08-23 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| e0e04f3b-0371-3df5-9ccf-1d709a41c9c2 | -9.1711 | -59.618 | 2025-08-23 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 789131ee-8966-3594-8111-607c591dc607 | -7.8131 | -63.5468 | 2025-08-23 01:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 4e6c36cf-89dd-3472-881f-d3fd186cf9b8 | -5.7614 | -57.6002 | 2025-08-23 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 831d84c1-1558-318b-bd21-250cf51e3e88 | -8.8921 | -62.4297 | 2025-08-23 01:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 125.8 |
| c7f1010d-297c-3967-8eb5-178f47e3ea76 | -17.5979 | -46.5715 | 2025-08-23 01:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 03a509db-05c7-3292-9452-a3bcc372734e | -13.3777 | -46.2208 | 2025-08-23 01:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 638374bf-31e0-322b-9189-96ba37ce3bb0 | -15.0186 | -54.8735 | 2025-08-23 01:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 8b7273b6-074d-3e61-9034-08817609d788 | -9.4449 | -47.6585 | 2025-08-23 01:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 2e8e1690-8302-3b1d-8a91-4ee2238e04d0 | -20.097 | -47.7676 | 2025-08-23 01:10:00 | GOES-19 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 39.3 |
| aa845e8f-6087-3942-9f3f-a81982bed778 | -6.4327 | -41.2114 | 2025-08-23 01:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 110.8 |
| eb0926c4-61f8-3a95-b51d-5f29c997ae72 | -8.9106 | -62.4289 | 2025-08-23 01:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 068bf8b9-a3fa-356d-9b9e-554a47bd22d0 | -3.4439 | -49.051 | 2025-08-23 01:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 5f91f280-78bf-3655-89c2-76038f966f16 | -11.2005 | -55.0195 | 2025-08-23 01:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| cee1f0c2-10cb-3e0c-909d-58c26882f098 | -5.7431 | -57.5814 | 2025-08-23 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| bcc09f38-1801-3127-ac4b-e4b972faf70d | -9.1895 | -59.6364 | 2025-08-23 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| d1f755c5-ac59-3036-83b2-aa30821e8de0 | -7.0352 | -44.6396 | 2025-08-23 01:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| d0ef5fe7-ef88-361d-88b4-d6a4679d5751 | -17.8273 | -52.065 | 2025-08-23 01:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 2a493fee-54a6-3fbd-b407-5be52469f3fd | -17.2552 | -46.7811 | 2025-08-23 01:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 45.5 |
| c2d91d2a-c7d2-3359-8feb-1eba83601bfc | -17.5785 | -46.5523 | 2025-08-23 01:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 19dcbf53-ff38-31d3-9e19-78c9e677cd54 | -12.9921 | -45.2252 | 2025-08-23 01:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| ab859092-8042-3686-a469-786aace45384 | -9.9695 | -55.845 | 2025-08-23 01:20:00 | GOES-19 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| abdbbaff-8711-3c7b-ac3d-3904764398fc | -9.1895 | -59.6364 | 2025-08-23 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| f5d8eb36-3c5a-3fdb-a8b0-96a82b5950d5 | -9.9493 | -60.1947 | 2025-08-23 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 838.4 |
| d79037ab-7fd9-3871-8148-026e1fb36c6e | -9.5181 | -60.5075 | 2025-08-23 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 9d1930b4-30bd-374f-b772-e5424af57e4f | -9.9681 | -60.1743 | 2025-08-23 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 181.3 |
| f73afd23-1006-386a-b8b7-089353ec5b49 | -9.968 | -60.1937 | 2025-08-23 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 366.2 |
| 4a4b2538-07e5-3e2d-babf-341a574cd9d8 | -6.4327 | -41.2114 | 2025-08-23 01:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 107.3 |
| f0352f5b-2271-3184-91df-5bd48735590a | -17.5779 | -46.5756 | 2025-08-23 01:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 96989007-815b-3ed3-ac25-c907680a4b72 | -8.8921 | -62.4297 | 2025-08-23 01:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 775bc103-5203-3af0-8aab-cc9b4cde7d01 | -17.8278 | -52.0433 | 2025-08-23 01:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 6b06f982-d8c5-3b87-a87e-f2980f67c1b8 | -7.813 | -63.5656 | 2025-08-23 01:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 107.2 |
| f2c70270-67f0-31cb-b52c-a8f6151391cf | -9.1712 | -59.5987 | 2025-08-23 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| e2d464b6-944c-3e3b-bc67-128716a070b1 | -6.6044 | -44.5624 | 2025-08-23 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 60572674-96b6-3537-8d44-e002d7be48e5 | -17.8075 | -52.0683 | 2025-08-23 01:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 12b27b42-2440-3a0e-b727-8de70ff9dc8e | -7.8131 | -63.5468 | 2025-08-23 01:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 27999178-ca53-3558-9409-d17feead0e1b | -17.5785 | -46.5523 | 2025-08-23 01:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 9f6a68aa-dfba-3ab9-8e83-e6e1e183873f | -17.8273 | -52.065 | 2025-08-23 01:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 9b5cbec6-063a-3d0b-8b3c-61e113615161 | -17.5985 | -46.5481 | 2025-08-23 01:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 2171af27-86d4-3f14-a4b1-53558d35c31a | -9.4449 | -47.6585 | 2025-08-23 01:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 4cf6970a-3a59-38db-a647-e100e468b22d | -9.4991 | -60.5663 | 2025-08-23 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 7e795da9-a526-34f7-8602-eec32a094d19 | -14.684 | -56.6136 | 2025-08-23 01:20:00 | GOES-19 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 05f672fe-83d4-3188-a864-ce705268d32c | -9.5179 | -60.5461 | 2025-08-23 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 127.2 |
| be2610f5-3b48-3c7e-b2c8-00135d9fb78f | -9.518 | -60.5268 | 2025-08-23 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 155.4 |
| f36cf4f9-689e-34ac-ad75-715201574341 | -7.0164 | -44.6413 | 2025-08-23 01:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| a4eb1bd7-246b-3630-9a8f-4d326f38e8bf | -12.9921 | -45.2252 | 2025-08-23 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 44e1b39a-017b-3237-8ab3-bbb2b287d79b | -14.37 | -52.06 | 2025-08-23 01:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| f2d2b6e3-c748-3e8f-9548-7f5a099cb73d | -17.8079 | -52.0465 | 2025-08-23 01:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 89.5 |
| e674c015-92fb-3caf-bc72-46ebebc00477 | -13.4155 | -46.2604 | 2025-08-23 01:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 63.4 |
| b6b7d211-3531-3167-8a8b-15601b70c0b4 | -17.2751 | -46.777 | 2025-08-23 01:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 122.4 |
| e17f881b-d98b-3486-8fe2-a10b34dc8707 | -8.9106 | -62.4289 | 2025-08-23 01:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| ebd7205e-6ba3-3b69-a0ac-9aec1710916a | -9.1897 | -59.6171 | 2025-08-23 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| fa0f400b-9059-3070-942a-90aacd5e6a4c | -13.3777 | -46.2208 | 2025-08-23 01:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 68.4 |
| eb99f667-c20c-3563-a84d-da0fd602d09a | -9.5177 | -60.5653 | 2025-08-23 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 128.9 |
| 39f8f814-bf45-34d8-8338-c2fd89e2376e | -9.5366 | -60.5258 | 2025-08-23 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| c4f074b5-bdd3-3c37-bba8-77c59072525f | -6.4138 | -41.2132 | 2025-08-23 01:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 137.0 |
| 75e852f0-2788-31a4-a604-c670700dea8c | -9.9495 | -60.1754 | 2025-08-23 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 377.8 |
| 5da0a3d5-08a8-38cc-a38d-395d71a124e3 | -9.9678 | -60.213 | 2025-08-23 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 2af25558-7398-3a6f-9548-cf54978c9b7f | -9.9883 | -55.8436 | 2025-08-23 01:20:00 | GOES-19 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 8b4ed555-e27b-32e4-a2bc-5c321662a302 | -17.2757 | -46.7538 | 2025-08-23 01:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 103.5 |
| e0d87e41-199f-3f5a-b84f-bb42663b3c5e | -9.9492 | -60.2141 | 2025-08-23 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 128.0 |
| e2fb0a37-67ba-3ee9-a05f-ef08e27ebd7f | -7.0352 | -44.6396 | 2025-08-23 01:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| f88ad87b-a8c4-3351-847b-c99da554a5dd | -9.2095 | -59.4609 | 2025-08-23 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 041c9c3d-4a3f-3efe-8a9a-ec2829a22ce6 | -17.5979 | -46.5715 | 2025-08-23 01:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 79.2 |
| a3af8b52-65fe-3ea7-b2ee-b00b6dbd5679 | -3.4439 | -49.051 | 2025-08-23 01:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 502979e1-8b81-3d37-be35-b3f7c9fd4f74 | -5.7614 | -57.6002 | 2025-08-23 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 48eb3963-674f-3e88-82e5-b66d73c97029 | -7.0164 | -44.6413 | 2025-08-23 01:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 7cd0459a-21ed-3aa5-a505-29d2744a3c06 | -7.813 | -63.5656 | 2025-08-23 01:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 102.2 |


[Clique aqui para ver as próximas entradas](README8.md)
