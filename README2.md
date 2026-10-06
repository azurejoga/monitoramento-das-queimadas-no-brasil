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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c7b5bbd-d6d4-3e85-bff3-3b83f4100b3c | -13.88414 | -43.81167 | 2026-10-06 00:13:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 327d402f-a1c7-3f40-b657-ca6fcd5ebcc3 | -13.02147 | -43.12101 | 2026-10-06 00:13:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 29.7 |
| 027d2668-746b-3ae3-91c9-9c5478d12b78 | -14.058 | -44.2852 | 2026-10-06 00:13:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 206106e5-b017-3c18-9943-b9f572187826 | -3.06 | -54.24 | 2026-10-06 00:15:00 | MSG-03 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7002f76a-d056-3adb-a4ad-3c8699a6440d | -3.08 | -54.18 | 2026-10-06 00:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d282a5f-3b80-33a8-b6f6-d681fdbf5075 | -3.08 | -54.24 | 2026-10-06 00:15:00 | MSG-03 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95cf1dcb-cc56-36ea-af42-6c88c283d2aa | -11.68378 | -43.67459 | 2026-10-06 00:16:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 1985913b-605c-3792-a0df-a0ffe464fb32 | -11.68975 | -43.6787 | 2026-10-06 00:16:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 159.4 |
| ade5a0ea-5105-3c3c-961f-3b6651aa9305 | -11.26112 | -45.5331 | 2026-10-06 00:16:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 84b36c3d-b10b-32b8-b506-153af9e4f949 | -12.14076 | -63.14801 | 2026-10-06 00:16:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 46.1 |
| d05bee1b-4060-3038-a9ba-5032e859edb4 | -10.98631 | -45.45004 | 2026-10-06 00:16:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 22523c2f-0227-330b-aac0-5896bdcc05bb | -11.66239 | -43.64525 | 2026-10-06 00:16:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 05dbfa34-dd64-30b8-8169-0f4ff364d933 | -11.26729 | -45.52648 | 2026-10-06 00:16:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 62f197cc-bc65-38ca-b29c-e7b99cfe06be | -11.65308 | -43.65321 | 2026-10-06 00:16:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 866d4e08-226a-3e97-af8f-079b0194e985 | -12.76546 | -44.88147 | 2026-10-06 00:16:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| dac046c7-dca5-3f5a-8319-6cf6ee95ec10 | -11.52753 | -44.89126 | 2026-10-06 00:16:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 172b5378-0ba9-3aea-8817-8a278b61b126 | -10.97769 | -45.44511 | 2026-10-06 00:16:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 4d0d523f-6488-3cac-b3f2-d79089194f60 | -12.12341 | -63.14991 | 2026-10-06 00:16:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 5069e049-9bb4-3512-bbf4-f90ae5f2b941 | -11.64674 | -43.64838 | 2026-10-06 00:16:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| c1b6dff6-b5fc-38a5-b8e0-1ecd128af9c6 | -12.13893 | -63.15301 | 2026-10-06 00:16:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 8f4989c4-975c-35a7-b146-c50cca1d5e38 | -11.53961 | -44.89486 | 2026-10-06 00:16:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 3ea227e9-0965-38a7-a999-f63deb3d6a60 | -11.69943 | -43.67165 | 2026-10-06 00:16:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 1ed918c0-6c40-3847-ae36-d55308ad3df9 | -3.06708 | -54.14569 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0f10f1ee-9efb-32e2-9f3f-eadc012eb5ef | -3.01771 | -54.19494 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bc90ab3c-a28b-3709-9119-3fb2fffc3438 | -3.07714 | -54.15327 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| a1da76d9-b6b3-3311-8e76-f404d551a7c5 | -5.61139 | -44.86634 | 2026-10-06 00:18:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 708fae2b-4afb-3e8d-b2a7-a24bb7996050 | -3.18956 | -54.10458 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d2f1f2f2-bf8a-3855-ad10-b5f172b88c06 | -2.94461 | -54.20213 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ffeb93fc-6122-3549-80c4-4629df1c18bd | -3.07047 | -54.23516 | 2026-10-06 00:18:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| afa1951f-2473-3104-b94f-5e0cfa38db20 | -3.71668 | -48.88517 | 2026-10-06 00:18:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| b8dcce2e-0e80-3567-81ed-db334a44e6c5 | -3.11367 | -53.7524 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 29e2f5d2-940c-3328-baa3-d7b3092646ee | -3.63115 | -58.94453 | 2026-10-06 00:18:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| edd7723e-16bb-3e36-806b-45737188ed1f | -3.18834 | -54.09574 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b0653825-6fba-35f5-8066-3d95cacbbdfa | -3.28373 | -54.18407 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| b1ccba0a-1398-3449-9385-91a025f09449 | -3.88366 | -55.8055 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 17660c8c-e80e-3121-8a06-a1b71ec1108f | -3.32499 | -59.4943 | 2026-10-06 00:18:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 7cc05e46-590d-3258-880b-96ed83efc758 | -4.26198 | -50.80313 | 2026-10-06 00:18:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 53fcb601-9fd2-350b-ab5f-5e982fc3941e | -3.00033 | -54.13435 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| d9296e3f-2074-3786-9105-8a5dd8813ea5 | -4.77521 | -50.80855 | 2026-10-06 00:18:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 7aff6a12-9b66-3cc9-900c-d7c1fe35ed6b | -3.67183 | -55.94121 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| a04b5438-45c5-3a7d-b63d-d5ede1a6fc9c | -4.79763 | -47.33212 | 2026-10-06 00:18:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 21.2 |
| cb3879e3-75a1-318f-a35a-dea07bf717df | -6.2318 | -51.81366 | 2026-10-06 00:18:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 18a33b30-1a40-30d6-b845-9596db77ed7f | -2.96244 | -57.22614 | 2026-10-06 00:18:00 | TERRA_M-M | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 04b6547d-0894-3714-a3d5-bf0aa11f0097 | -3.57977 | -53.12954 | 2026-10-06 00:18:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 3b70fa65-7cea-30a2-9bd9-b6c99e4bccc5 | -3.03626 | -54.2642 | 2026-10-06 00:18:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| aa92708a-aa78-3a38-9bf1-5f0eb78b5f8a | -5.60615 | -44.83283 | 2026-10-06 00:18:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 06d92d3a-420d-36bd-a73a-0971ad57abc2 | -3.12382 | -53.76012 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| d4530341-7e6e-3422-bc67-854e29f29d26 | -2.86172 | -54.13887 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| e830b699-6eb7-3fd5-a6d1-c59ee87d7325 | -3.10743 | -53.70749 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 0e238859-77cf-3d55-946b-c97d30a4a86f | -4.72433 | -44.08614 | 2026-10-06 00:18:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| bde5c1e6-b767-34d4-8665-f9debd97edee | -4.15087 | -53.9204 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b89cfd5e-7d35-3ebe-a0a8-dee57906d9c1 | -2.93366 | -54.12259 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 7311e0ba-3ca6-3d9c-9169-5a65e640c903 | -2.78369 | -57.65014 | 2026-10-06 00:18:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 03d07739-2234-3527-a619-0f0ae51db286 | -4.96051 | -56.27712 | 2026-10-06 00:18:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7d70fc9c-8fb4-3618-b0b4-e1f9506de2d6 | -4.25173 | -50.8046 | 2026-10-06 00:18:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 94b6cad5-732d-3504-9876-da946030fe52 | -2.8833 | -54.08451 | 2026-10-06 00:18:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c929fbd4-4595-3d25-b360-945e313dd2e8 | -2.97898 | -54.1103 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e29a0eeb-ada5-3323-acdf-f52b55634925 | -3.52971 | -59.39357 | 2026-10-06 00:18:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8fc53da3-fd13-3d2a-b30c-d549a5bd1910 | -3.07413 | -54.26158 | 2026-10-06 00:18:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ed8ff79b-8bcb-37fc-8b2d-a4c0a05b6ad4 | -3.08295 | -54.26035 | 2026-10-06 00:18:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 863e1de0-48d3-37fd-870b-b38d25792d68 | -3.08934 | -54.2415 | 2026-10-06 00:18:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 7704b40c-cd41-3132-b06c-0e3bbf153760 | -2.98905 | -54.1179 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 86c12872-f7aa-315f-9086-224cce6f42cc | -3.51138 | -59.50898 | 2026-10-06 00:18:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 102ad720-1b09-3810-932f-25c2fca9a314 | -3.09604 | -54.15961 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 8d12c4df-d367-393c-b08b-73002864c4e7 | -4.46001 | -54.95984 | 2026-10-06 00:18:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| bb4baccb-273c-346f-a0a3-30ab729f852c | -2.8062 | -54.12861 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 499f39c2-b4a4-3e38-bb39-872c0b038239 | -4.13017 | -54.91306 | 2026-10-06 00:18:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cdd1f76f-d50b-3882-ad13-91126b3cb040 | -2.98998 | -56.6122 | 2026-10-06 00:18:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2e2845f7-e2e7-3ee8-8b3a-5af199e1c976 | -3.08965 | -54.17854 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 19cedaa9-e70c-375d-807f-76cbdccc2cfc | -3.07198 | -54.18102 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 62a42414-b2bd-3cf6-b402-9e22dd1ec6b3 | -3.05911 | -54.23409 | 2026-10-06 00:18:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 02271558-3c86-3af0-be3f-cb492e84e426 | -4.05827 | -54.04773 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a7622ef9-a748-3a70-b3d4-dc06c3a34223 | -3.26818 | -54.00614 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 98d130c3-b30a-32f9-9b9a-40d4a962f037 | -2.92238 | -54.10612 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a3a7a26e-c0c6-38e2-b34d-a75148142510 | -4.9429 | -49.09421 | 2026-10-06 00:18:00 | TERRA_M-M | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 29400992-0b90-3638-b13d-3a6f929c7573 | -5.8488 | -45.04541 | 2026-10-06 00:18:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| dcc43100-7eeb-3183-a55c-23ae897be426 | -3.68088 | -55.93994 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 9ceff451-fd92-3cce-937f-bc815f6c05e4 | -2.98688 | -54.03695 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| badd1109-dff9-3806-80be-3d509b46c2d1 | -3.22437 | -53.88548 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 93c7bc04-43f4-32ed-a746-b190515caa52 | -4.9227 | -55.86083 | 2026-10-06 00:18:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 12656751-cf81-3959-9e88-a6810bbe3d57 | -3.48236 | -55.43237 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c4ec18f7-684e-3a57-aa32-0d490c774a5b | -2.99545 | -54.09897 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 666dfc32-44bb-3978-9dbc-4c092255f001 | -2.7772 | -54.11461 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 670bfcc9-2ca3-35f7-867c-e9b14c4a7fe6 | -2.78482 | -54.10451 | 2026-10-06 00:18:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 569d489b-575e-3091-af0b-0aa945fcec0f | -3.15885 | -50.43865 | 2026-10-06 00:18:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 78f56f5a-a20d-3742-aa3b-fe0af6167139 | -3.26778 | -50.40374 | 2026-10-06 00:18:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 17cc0437-0cba-3adf-877d-4be0029e65a4 | -2.99196 | -51.00985 | 2026-10-06 00:18:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6f674e15-08d0-32a4-af58-b827e291619d | -2.7998 | -54.14753 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| d8c4f6c2-2458-38fc-bd5b-818b69b734a1 | -2.92726 | -54.14152 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| accfe7f9-82fb-3180-9b82-ed3e15fe5c46 | -4.81107 | -47.33031 | 2026-10-06 00:18:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 34.9 |
| bb554881-6c68-300f-85db-050d2dae8a98 | -2.93245 | -54.11374 | 2026-10-06 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 09952f45-6bbd-35e3-b11d-31ad27c67355 | -6.19601 | -55.33707 | 2026-10-06 00:18:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ce3b29cb-2c7c-399d-941d-fbaacf4c9b3f | -3.1113 | -59.17894 | 2026-10-06 00:18:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 70ea86c8-3121-3178-8c50-461381834181 | -4.81553 | -54.7327 | 2026-10-06 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 94536f5f-4199-376e-90a9-fd395eecc1f2 | -5.81613 | -53.83694 | 2026-10-06 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e44a1d5a-0852-369a-bcc1-f673e4a761f9 | -3.11616 | -53.77033 | 2026-10-06 00:18:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| a7e3ff75-12a7-3d7e-96bd-3c1eb054e8f2 | -3.9912 | -56.26351 | 2026-10-06 00:18:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e7574116-d9e1-381c-b335-a809d2b453e8 | -5.68516 | -53.49161 | 2026-10-06 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| a2f73713-9f90-3134-a2ed-dc5e5651f056 | -4.34067 | -50.41556 | 2026-10-06 00:18:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ae7650fa-0326-3060-86c8-d6ae3336a6c6 | -3.0793 | -54.23392 | 2026-10-06 00:18:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |


[Clique aqui para ver as próximas entradas](README3.md)
