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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acd13db0-edf7-39aa-82b7-cd2a8a643af7 | -7.20169 | -44.94545 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7502ada9-0477-3e50-a04d-7177ecbdfaa6 | -6.17749 | -41.06902 | 2025-09-11 03:55:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f77777b7-6f1f-3daa-a5d9-163b72d9420c | -7.84732 | -45.40457 | 2025-09-11 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2bbbe108-82ec-364d-b547-2d6ac386a4a7 | -7.20452 | -44.95507 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7d6cfc72-1644-382b-af77-aef13b321dde | -9.06786 | -47.0765 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3755d930-35aa-3e3e-8fb0-7035e0481b72 | -10.31537 | -48.80411 | 2025-09-11 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 230ae1c7-6560-3bf8-948e-bfd3d79cb85b | -7.66054 | -49.84367 | 2025-09-11 03:55:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5cd429b-d86a-3688-aef2-ec353f37cb96 | -6.67314 | -44.12224 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 207d51b7-11ef-3169-a3ce-50f6e8cf0327 | -7.10743 | -50.76125 | 2025-09-11 03:55:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| df7cfa0a-b0c4-39ac-8ca4-0249e4546dca | -9.04208 | -45.79276 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c4038bc7-4ebb-3e2e-ae76-03eb0703510b | -6.54378 | -42.44407 | 2025-09-11 03:55:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c98149fa-e978-3b97-a11b-c0c2968c31f0 | -6.56791 | -43.14942 | 2025-09-11 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b3ddb10a-4683-34a9-a704-835b944f92b2 | -11.4633 | -43.60705 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8f7adf78-35da-3cf1-841d-f0df355c5bd5 | -12.04348 | -47.61203 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7da26062-71e9-355b-ada7-e9d36a57c6a7 | -6.83534 | -45.59066 | 2025-09-11 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 647080ea-49fe-3270-8a1a-5c7c9a53aa0b | -11.36037 | -46.52642 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 528cc009-42bc-32df-8c48-0e99d111e6c0 | -12.10197 | -51.01599 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b13f2af-3ac6-3fe2-854c-c4bcf2d7f1c5 | -10.17287 | -46.18475 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2b419295-9480-3f60-9c38-f2fc1902e4eb | -8.7476 | -47.11733 | 2025-09-11 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3897cbef-db81-32a9-a263-c74eb80d7f01 | -9.1277 | -46.19474 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b69b5116-4b17-3a65-8aa4-2faccdd80ba2 | -8.80088 | -48.09416 | 2025-09-11 03:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cbfcf4a-d899-3101-87db-ba7ccffb07f6 | -6.80331 | -43.42787 | 2025-09-11 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 724593ae-5e5f-3aab-9431-5ee213a0dc6f | -11.50622 | -50.39491 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 34e4ff09-2b84-39b4-93fa-c25ebf9b425d | -7.84357 | -45.39971 | 2025-09-11 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3673fd51-7837-3329-a2bb-10f03fa9a282 | -6.85243 | -44.89425 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0a5eca9e-a7c4-3b2b-853b-1c92c2047b92 | -11.56787 | -43.23708 | 2025-09-11 03:55:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0751c6b4-4e9d-335d-b822-b63a732ee19d | -9.59175 | -48.06401 | 2025-09-11 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11b3ee7c-1bc4-31ed-acea-3536d7566dbc | -11.10815 | -48.42558 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fbb5f9a-ccd6-3717-9d5a-740ff5faf37c | -10.06445 | -50.376 | 2025-09-11 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8cff8221-323a-3e48-8520-db34a478f26a | -7.53932 | -44.67896 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 324b96fa-1768-3b84-a241-6077020d1bb1 | -7.24434 | -39.88791 | 2025-09-11 03:55:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1a96e0dc-c37a-3d9d-a12c-59bf5153e591 | -9.01615 | -49.76565 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| afb13c85-aed8-3ebd-9da3-937c8014481c | -11.14983 | -48.45913 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3481f2e8-8c9a-32c0-991b-7f80ac79ff42 | -11.4967 | -43.66053 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c3a1961-cf69-35a0-bc7c-c2be416b47db | -9.72171 | -43.52821 | 2025-09-11 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7659d12d-04ee-3cbb-bdcf-92bd2f06dbf8 | -7.03395 | -42.13498 | 2025-09-11 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c56fae16-b2de-3436-b95d-9f6207a6f60a | -12.47598 | -47.48944 | 2025-09-11 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 6c861b14-7a4b-31af-9713-2f3b865d1d68 | -11.65697 | -48.32121 | 2025-09-11 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e22bb9de-4cf5-3a62-91e5-cd93e5a5b3ef | -11.34914 | -46.50217 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7b8f1ad7-f88c-3829-9d93-3ff44a50352d | -7.16477 | -48.88646 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa01efe1-8be2-3122-83d0-5019f0de8504 | -8.58422 | -45.58471 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 69b8bbf4-3fe5-3df4-8fb7-60f09c9d92bb | -7.65746 | -50.27122 | 2025-09-11 03:55:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a0bd1a44-f169-365c-b4c0-ece34f4078e1 | -8.16741 | -46.068 | 2025-09-11 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d44fb2a-e424-325e-9193-ae0ab8721a37 | -11.37335 | -43.51776 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1803ae47-75fe-3ada-b75a-facf1cb16bf1 | -6.24745 | -43.42601 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd7d24d3-b266-394b-9a54-e214b1c546ea | -6.36974 | -45.1612 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b890374d-7c1d-3de7-9001-3e334e928cab | -11.3026 | -38.94029 | 2025-09-11 03:55:00 | NOAA-21 | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7247299e-b281-3343-9e95-cca4bca56395 | -11.3446 | -46.4855 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b7c40c06-4cdb-3e6e-b93a-2c07b6eb28aa | -11.48537 | -49.25306 | 2025-09-11 03:55:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97aa18e8-f450-3935-8d11-ded8511d7cdf | -6.35719 | -43.05955 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 204b6874-9c4e-3d67-acb1-0c6378dea709 | -7.83908 | -45.3992 | 2025-09-11 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6267cf10-40d4-3e3c-9b9c-74c6ed72257c | -6.31432 | -43.41919 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f5962e0e-1505-3345-8423-0bd1eea6007a | -13.2356 | -41.35224 | 2025-09-11 03:55:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d27fe1a7-77cd-3787-9db1-7f699c04816b | -11.40915 | -43.53323 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dbff59c2-3ce4-39a8-9f79-aeb3307ea1c7 | -8.65871 | -45.7255 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 09b2607a-5efe-3494-924f-df94c4a5a25f | -10.2008 | -46.83852 | 2025-09-11 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ef06e46b-9580-33f3-9d5b-274a3c843ad7 | -9.45569 | -46.69978 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8685edb0-65a2-30a8-91e8-99442c1f6304 | -10.3818 | -50.52026 | 2025-09-11 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f1543d2a-aa92-358d-bafe-7eabddff8a5c | -12.12594 | -44.85949 | 2025-09-11 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| df1faa09-29b5-3bf1-ba08-f24c1f17f931 | -7.99281 | -45.79864 | 2025-09-11 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6fb41c7e-46f4-3edb-a1e5-e7dcc23493af | -9.05645 | -46.97073 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 77ede735-f935-3918-a278-c028cab9f51e | -8.16393 | -46.09486 | 2025-09-11 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d6f54ad0-99cd-3809-a6c2-f17ea64b2318 | -11.42157 | -43.71466 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ce6e302-c634-3636-b053-4770a00d795f | -8.73531 | -47.09078 | 2025-09-11 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| e112313c-c432-3648-8790-f6318f9320c3 | -11.48324 | -43.6487 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 23adb8c0-138f-3e46-bfe4-26e348a2ea24 | -12.53261 | -45.33533 | 2025-09-11 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85770e26-3f06-3896-b0ea-c82e4406277c | -11.36429 | -46.55601 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 1c347e17-e0ee-3c42-8c5b-b88340a91d72 | -7.80444 | -41.24413 | 2025-09-11 03:55:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 94902ddb-72f6-3e96-8eb6-26b16214eb85 | -12.01946 | -47.58324 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 316d03cc-35fe-3337-8756-eae691e5190b | -12.01467 | -47.58232 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fc1f7917-03d2-3536-82d4-0f15df0f154f | -11.10198 | -48.42072 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ad589b1-5cfe-351f-82d7-3b9996607f37 | -11.41509 | -43.54366 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b01590b-8222-37d5-8218-6b95a09170ee | -6.39193 | -43.50752 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96638c6f-6d9e-3dd9-afb4-be05dadb9bd7 | -6.38557 | -44.42977 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a497c689-d69f-38d0-b25b-effcdc2aaf36 | -11.47949 | -43.64803 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| e8aaad16-5de4-3b6c-a388-69610d896300 | -11.34515 | -46.47211 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0315b642-31c7-3450-87f7-fa0d1f431bf3 | -6.38246 | -44.42904 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 745601b0-9bbc-36ce-b57e-6b122d2d7805 | -6.80168 | -43.27131 | 2025-09-11 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 557cc3b5-d92b-3cd5-9166-b1073665337f | -11.48228 | -43.67719 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0578813e-6376-3465-8e7a-47b702ccac06 | -11.50209 | -50.38538 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4a6aece6-065b-3097-8c1f-2d88f36a52cb | -8.31866 | -44.89841 | 2025-09-11 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ecc2421-56f9-3399-a91f-e6358f8792ec | -7.20231 | -44.96794 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 462b0f96-6d8f-3dc7-a2fc-400a5cd32182 | -6.85884 | -47.86217 | 2025-09-11 03:55:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 02701d33-f144-36f9-a451-ab8fdc8cb8f2 | -7.24029 | -44.03485 | 2025-09-11 03:55:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b543180-3bdd-371c-88fa-0f0dbbaf33ec | -6.24488 | -44.79858 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7793889-7d80-3f07-9e5c-6668b22ab5fb | -12.02717 | -47.54084 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df004ffa-3435-3dc1-a8bc-69c40147d1eb | -8.04439 | -49.05335 | 2025-09-11 03:55:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 32452ed8-5f7c-38a7-ae7c-9ae36088196b | -11.79951 | -50.5832 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bea7683-915a-30bb-a047-fe3ef20f85c1 | -6.18513 | -43.49368 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| befb4fc7-895b-364c-a193-e20d749de4fa | -11.0242 | -44.64711 | 2025-09-11 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bcec8db-16dd-3d52-96bf-b13fe16c413c | -6.31145 | -43.4117 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2b257c6-42a1-3d64-9217-8d76d8801976 | -7.18409 | -44.96935 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d3716b01-0b50-3122-8e19-7d859bfa4e71 | -6.53533 | -44.60344 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4f403c0-bfb8-3378-b4b2-89776ab65dd8 | -11.15498 | -45.30337 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44296970-baee-3c01-9bde-9e34d4b2f518 | -7.85179 | -45.40526 | 2025-09-11 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 025b0c62-516c-3961-b700-00f6fe68aa1a | -8.72945 | -47.09529 | 2025-09-11 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| bd46270d-b186-30f7-9551-4e0c4a3cf720 | -11.10048 | -48.43777 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d086c287-7cb7-3f07-a2ff-b45da8499fce | -7.39152 | -47.3778 | 2025-09-11 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac759894-5cc8-3a82-b6f8-386467fe40ad | -11.03169 | -46.04134 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec4dcc2b-3e53-3904-a12e-1b6f494f18ef | -6.17581 | -41.0737 | 2025-09-11 03:55:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |


[Clique aqui para ver as próximas entradas](README26.md)
