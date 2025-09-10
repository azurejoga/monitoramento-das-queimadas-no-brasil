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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 793bda52-ab46-32c6-8d9b-5cb3f490e206 | -7.59165 | -49.29323 | 2025-09-10 05:04:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 197a203b-7bcd-3cad-9c31-cc4da9b08a7a | -9.09753 | -46.96756 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b8928af5-8c87-37a2-a52b-48997e6c73d3 | -8.85806 | -47.2364 | 2025-09-10 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 507334c1-110c-3f60-92a0-353067d56330 | -9.06186 | -49.82446 | 2025-09-10 05:04:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ae3f47f-6924-3ff8-966b-03feb2ee9acf | -12.06973 | -51.0668 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c7dbaf38-5fb6-3ab4-84e5-6e6744b853f0 | -9.06021 | -45.73421 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 005635d0-55d7-36e1-a175-5a8ecedfb4f3 | -11.16749 | -48.35401 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de28a57c-cd8d-3493-a143-dbc238304fb0 | -7.88955 | -46.26454 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59b485b0-e0f1-36e1-850e-d21d21fddb51 | -5.80114 | -51.7309 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84e92b26-9d91-3c3a-9e9b-53473ef395fa | -5.72168 | -51.69394 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78f0ceb2-77ba-3df3-9696-cde9df9f6618 | -9.51508 | -54.63797 | 2025-09-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 2dea45c1-100c-3eb0-b7bc-f58ac48bf649 | -11.75284 | -50.63059 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9c797437-7586-30e8-9ae1-34b70010ec79 | -12.18066 | -53.87328 | 2025-09-10 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4076952a-da3e-3571-80ea-600e8c2be4d9 | -13.7934 | -46.29868 | 2025-09-10 05:04:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6a780944-5e8f-380a-805e-80a380f6693b | -7.73781 | -50.72807 | 2025-09-10 05:04:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38aa2b88-61f1-384d-892f-757ab93626f9 | -9.34468 | -46.75949 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d318f04-8c3b-3dbc-ba4d-16964b8bfe60 | -8.06975 | -50.1825 | 2025-09-10 05:04:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f6978f3e-9a39-3a43-b768-d78b98328693 | -7.5962 | -49.29381 | 2025-09-10 05:04:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14d7390d-ca19-3df4-93cb-fae737075be2 | -11.12034 | -48.4371 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f52d2ba-4bf1-3f79-ab88-552b23cfa9e3 | -8.07245 | -48.63499 | 2025-09-10 05:04:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 676b2d2a-7884-3ee5-9992-34ab7e17281e | -11.31731 | -46.52453 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4fc97c4c-7032-326e-9b1a-a6ea11dc053c | -12.06544 | -51.0662 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ca37e84c-84ab-35b7-82f6-a9849b41ecb3 | -10.38432 | -50.54329 | 2025-09-10 05:04:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9050db1e-0fa3-3587-a2c5-dbc075e92c9b | -9.06858 | -46.97714 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 47e9989d-9d0c-3dad-a7e6-dcaaef87be63 | -7.18182 | -44.93394 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a43703de-fd25-3c1e-ac6f-38a1cc9b22e8 | -6.84717 | -47.93394 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a74510fc-b04b-36fa-9b9a-65d0392c637f | -11.66782 | -46.90341 | 2025-09-10 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 623b349b-ebdf-31c6-a901-1cab3f03f8f0 | -9.09677 | -46.98699 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 091ee80d-13fb-3bc8-9757-15c7fa8bbead | -12.01902 | -45.85759 | 2025-09-10 05:04:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1462d98-b669-395e-9db7-c297cebb6927 | -8.42974 | -49.12152 | 2025-09-10 05:04:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9fe4425d-7da8-34e2-8b43-bf376046f963 | -9.97866 | -50.29818 | 2025-09-10 05:04:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3d59b9a3-671f-31e0-bb45-61caae793b4f | -8.06352 | -48.62911 | 2025-09-10 05:04:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ea63490-4fc2-3139-8466-0ede6f2fbdd7 | -11.11427 | -48.36468 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9f644ffb-2ac5-3db5-862a-8ef3ba96034b | -8.04295 | -52.38599 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ecc13d3-44f9-3821-aafb-a53aaaf9cfef | -11.67968 | -46.90031 | 2025-09-10 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 99efc083-6072-336d-988b-6c8bf98d23c7 | -7.23039 | -46.1947 | 2025-09-10 05:04:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4d9fbe6-d3f1-3a7d-979c-103ba8a2fb14 | -10.02325 | -51.6709 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1ad9f0da-ceaf-3a18-aad8-98c381239f00 | -9.51737 | -54.64581 | 2025-09-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16177f88-6d14-3bf1-935e-f12a6b082823 | -11.83838 | -46.75142 | 2025-09-10 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 557a94bc-7c83-3eb3-8db3-4c8d69a6643e | -10.86611 | -55.73203 | 2025-09-10 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83c54ca7-524e-3bc8-a034-8a50c7dc3366 | -5.80491 | -51.73147 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79ed5254-86bc-3ec7-80a8-258397b3b2fe | -7.78289 | -46.05367 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19cb17fd-2aa9-3a86-a0f2-b9688fd2b61d | -11.1249 | -45.11982 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3830b088-7c25-3f41-905e-4dfebc7defb2 | -9.44278 | -46.69807 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5059af8d-b579-33a1-8a87-a3a22b9097e6 | -7.25776 | -44.45934 | 2025-09-10 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 14161999-d3c0-3c41-b4d4-e015ff9f5608 | -8.05716 | -48.67504 | 2025-09-10 05:04:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a3432195-34ae-3489-bc9f-d429bc4a22c2 | -6.85021 | -47.91193 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b424997e-ea1c-3ff5-902f-e401c36381c7 | -11.21702 | -54.99897 | 2025-09-10 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6da9ff05-25d1-348f-afb9-8b518391a843 | -9.0485 | -50.47999 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 990f0aeb-f272-3dab-8a78-4132fc73011d | -8.7435 | -47.09441 | 2025-09-10 05:04:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d44a6736-0769-3823-bdb5-88261ee56b1d | -8.4971 | -45.66568 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74347044-396f-36c9-952d-9f4e65b8be77 | -7.76235 | -50.76219 | 2025-09-10 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 994b42f9-b8af-3432-847b-5ebff5693b07 | -9.44688 | -46.70173 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 302ea103-a022-3a62-ae62-8adf257244f8 | -7.54822 | -48.22215 | 2025-09-10 05:04:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12175474-7e9b-3903-afb2-53d844494294 | -10.65339 | -48.61605 | 2025-09-10 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0ee2ef3-8ccb-314e-b1ca-a9c66fa33775 | -5.63656 | -51.33437 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb8854ac-9794-3ada-a8bf-9955581d82a9 | -9.44085 | -46.71263 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff160d1f-4d24-30eb-b25c-8917300a59ee | -9.06227 | -45.76535 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4e1dd881-aeaa-30d0-a075-a78a61ed53b5 | -7.18727 | -44.93922 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b1f6851d-d3fa-380b-bb27-f00cfe895e97 | -8.83588 | -48.09668 | 2025-09-10 05:04:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 466fa41d-ae32-30d6-9f00-7f8a878d8a81 | -13.1509 | -45.29023 | 2025-09-10 05:04:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71739294-1a65-344b-adec-95216a19dcca | -12.83104 | -52.94029 | 2025-09-10 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f5706def-950a-37db-bbff-b1d6c8245396 | -11.13758 | -46.35236 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e08fd9ec-b358-3c70-9884-75f1d60aa3e8 | -8.06273 | -52.3293 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9735e4df-a08a-3837-a94a-aa9cc1b618eb | -11.45366 | -49.27066 | 2025-09-10 05:04:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc75749c-9b1d-34d2-bc72-29cfac1fd31d | -7.54686 | -48.2476 | 2025-09-10 05:04:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1816a69-5943-3180-8e07-15a0d28941f9 | -8.52093 | -45.71075 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8d45ae65-27c3-3ba5-ba39-738898a9ffd9 | -11.45296 | -49.27589 | 2025-09-10 05:04:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a07a14f5-dc08-338f-87a7-f00ab2034c1e | -8.18864 | -47.1629 | 2025-09-10 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9246c5ca-81bd-3e05-ac40-e48c22aebf78 | -9.08158 | -47.06265 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 431d9ee3-8f4a-31c2-aba0-fdd9e93f99e8 | -8.28123 | -47.46931 | 2025-09-10 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87990986-9ab4-3d6e-bb3f-537cdc079cde | -11.11694 | -48.42362 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d708b00f-fee9-3443-8772-569551c8a593 | -6.55671 | -47.49279 | 2025-09-10 05:04:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a30c8511-1660-307a-9182-aa5c01344079 | -10.01717 | -51.68487 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1f253dd0-5aed-3456-bc84-10e61fb0efd0 | -5.80045 | -51.73544 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7413eacc-199e-3897-8533-a1e85646eafc | -9.0811 | -45.71132 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f8b5ae4d-10f9-3a13-b372-c033f3bea6cf | -9.31532 | -46.72607 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e14081c3-95b3-32bc-9bc2-ad09e64451b4 | -8.05521 | -52.32833 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 04882381-fac3-3a4d-8029-5696e7573b7d | -11.34524 | -46.53564 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b2d8572-0f1d-3d13-abc4-374a829307f4 | -11.33944 | -46.53516 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 013e0283-42cd-3957-a83f-d124e0493169 | -12.17889 | -50.62535 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 186cfe17-a6e5-34b4-9257-7479aa95fe64 | -10.02075 | -51.65978 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1104d8cf-9b7d-30bc-aaf0-92ecc4a1e966 | -12.85411 | -52.9437 | 2025-09-10 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09c7f6d9-3203-32cf-894b-7ce11107ac8a | -8.41836 | -47.28043 | 2025-09-10 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c07be90c-b729-3245-a627-de0d61c80dd0 | -12.18003 | -53.87756 | 2025-09-10 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52516671-204f-324c-96e4-d6d2222a2d24 | -13.02259 | -48.03855 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cfd1e3cd-be3f-3826-ba50-79af231bb896 | -10.14439 | -46.17438 | 2025-09-10 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da79591e-044b-3b6f-8d4a-d06430cea860 | -8.63323 | -53.11563 | 2025-09-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9cc727ee-15d2-3a42-929a-0dd5937c237c | -12.02051 | -45.85609 | 2025-09-10 05:04:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2610d4c7-cb51-3dd9-8855-3b7b3b70d31b | -8.08189 | -54.75782 | 2025-09-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c6fb451-fa8e-3205-9d5a-8c2ab9a0b4e9 | -8.75418 | -47.09622 | 2025-09-10 05:04:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6b4289b-5848-3c97-a3c5-fcb98499650c | -12.02509 | -45.85835 | 2025-09-10 05:04:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1329e88-e58a-308c-a92e-0227d37a9808 | -10.56235 | -49.44328 | 2025-09-10 05:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76ebe989-283e-3c94-93f2-2a4f2077a923 | -12.02057 | -51.00946 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6dc1db92-f3b8-3ca0-8787-a967f0c065fb | -8.75324 | -47.10308 | 2025-09-10 05:04:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 60410055-6517-3a72-bb20-573001405400 | -9.05476 | -49.80979 | 2025-09-10 05:04:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 95fc7a96-de38-3b0f-ab96-7f1888d2be5f | -9.06335 | -45.75677 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e6d56073-3f7a-3879-ade8-09186a5a8214 | -6.38955 | -53.6082 | 2025-09-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57cca0fa-3c73-3338-a676-866aa62d43a1 | -12.17947 | -50.62094 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| fc911946-9cfd-30fa-82c5-8fbc676dba25 | -12.20426 | -53.86376 | 2025-09-10 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README89.md)
