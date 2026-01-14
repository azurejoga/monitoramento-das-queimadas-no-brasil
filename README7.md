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
| a1e23d92-1a2e-3f19-a731-e3be5778fb3c | -5.02312 | -42.49488 | 2026-01-14 11:53:00 | TERRA_M-M | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| dc6b2767-1d84-3dd6-9c54-a7785fb324ef | -2.91747 | -41.87136 | 2026-01-14 11:53:00 | TERRA_M-M | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 5508b06b-5484-3a48-84a2-0005d5a939d1 | -3.32937 | -42.08774 | 2026-01-14 11:53:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 27f89ba6-fb2d-3103-99fe-22fb949db3ed | -3.54183 | -42.15424 | 2026-01-14 11:53:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 9ec57f80-f00e-3492-a5df-ca87f06c3854 | -6.8639 | -39.11671 | 2026-01-14 11:53:00 | TERRA_M-M | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 14.4 |
| f9ea0c32-732e-36a2-a53d-c5a82fa3a873 | -5.75798 | -39.34023 | 2026-01-14 11:53:00 | TERRA_M-M | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 2d621f0a-b583-3b62-9461-4f9654a42888 | -2.97791 | -41.7095 | 2026-01-14 11:53:00 | TERRA_M-M | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 24.3 |
| fa83020d-dfca-3f60-8a19-3028741d09e4 | -3.68701 | -41.52004 | 2026-01-14 11:53:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| c98b0089-7916-39c2-b5b7-73abcbb7927c | -2.92117 | -41.20448 | 2026-01-14 11:53:00 | TERRA_M-M | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 7620614d-cbc1-3abe-b4ae-4f77651fee4a | -5.75252 | -39.34662 | 2026-01-14 11:53:00 | TERRA_M-M | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 30.0 |
| 0b85dc0d-77dd-3e62-a5e9-4a043bdda4ca | -3.61434 | -40.15727 | 2026-01-14 11:53:00 | TERRA_M-M | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| f93702fd-c563-392f-aa4d-c0dde9432ec6 | -5.10195 | -43.23294 | 2026-01-14 11:53:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 26ae1b35-e23c-3552-9208-1fe7b3110aa3 | -2.91877 | -41.86231 | 2026-01-14 11:53:00 | TERRA_M-M | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 3132d74e-797e-3c1a-a17f-46667eebc1ba | -3.23972 | -42.06937 | 2026-01-14 11:53:00 | TERRA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 94c57675-91fd-3f3e-8e8e-67ebe8f6f258 | -2.92806 | -41.21182 | 2026-01-14 11:53:00 | TERRA_M-M | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 28e2503d-aa96-3be9-be21-0b44bfd6380a | -5.43979 | -39.21859 | 2026-01-14 11:53:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 32.1 |
| 5b7a3152-7623-33e6-acc6-2732e72bfb53 | -3.32808 | -42.09671 | 2026-01-14 11:53:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 166902ae-169c-39fe-9f7b-c61cdffb9bc0 | -6.93766 | -38.81679 | 2026-01-14 11:53:00 | TERRA_M-M | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 37e817e3-2b35-30a0-8848-6aecc479fab6 | -2.9198 | -41.21399 | 2026-01-14 11:53:00 | TERRA_M-M | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 10.8 |
| a789ed2b-9344-3c81-babc-a4dbb8bf34a5 | -3.28857 | -41.99026 | 2026-01-14 11:53:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4494aa81-d909-3fa2-9939-3b7d3aa21c0c | -6.24249 | -44.15534 | 2026-01-14 11:53:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 815022bb-137e-3a60-aa76-3ce780400184 | -3.97815 | -43.41431 | 2026-01-14 11:53:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2e5261e0-5d63-30fe-812f-9d9823f95820 | -2.97661 | -41.71864 | 2026-01-14 11:53:00 | TERRA_M-M | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 35.2 |
| a9c501c3-663a-30a4-ad01-a9359a3ea61a | -5.04307 | -40.84816 | 2026-01-14 11:53:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 28cc833f-04ba-3199-ba8f-2ff7663e9f4b | -6.93772 | -38.82566 | 2026-01-14 11:53:00 | TERRA_M-M | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 0a907591-06a2-3cf4-96e0-227a493ddefa | -4.94839 | -40.79722 | 2026-01-14 11:53:00 | TERRA_M-M | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 65b9b95d-c425-362e-9aaa-2d8a37c5621f | -3.08013 | -43.18213 | 2026-01-14 11:53:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1bb196fb-4e72-30f5-b957-4c85a2c85b54 | -6.81705 | -38.00177 | 2026-01-14 11:53:00 | TERRA_M-M | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 843327b5-061d-3c4f-84ba-1bcf01db1f54 | -5.75622 | -39.3536 | 2026-01-14 11:53:00 | TERRA_M-M | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 760aff32-2c26-31a1-9d86-ad47d171f251 | -7.25919 | -43.04203 | 2026-01-14 11:55:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.5 |
| a15c3330-6fd2-3ae7-9409-24be53a102aa | -7.84801 | -44.59563 | 2026-01-14 11:55:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 04f9dbbf-b5b2-3bad-8517-58519dcc6db1 | -7.249 | -43.0498 | 2026-01-14 11:55:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 47.7 |
| 11a234e9-0c50-3b5e-97b6-19ebe6d4fe6b | -10.51512 | -42.41044 | 2026-01-14 11:55:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 4fc5e20b-20d9-351e-8a4b-9ec18f0ca01b | -10.07632 | -43.97396 | 2026-01-14 11:55:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 89adfca7-4978-3794-bba3-aec1446695dc | -7.26176 | -43.02402 | 2026-01-14 11:55:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 87bb05b9-465e-3f79-a26e-f9ee199e50a4 | -8.16208 | -43.17479 | 2026-01-14 11:55:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 040fc087-5633-3600-852a-6e65e98b4ea7 | -10.08646 | -43.96626 | 2026-01-14 11:55:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7932ad43-6e89-325b-bd2f-a8e07860a99b | -8.15189 | -43.18256 | 2026-01-14 11:55:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 141.5 |
| a2a11e38-f97d-306c-8a4b-dbfbb4e06da3 | -7.24773 | -43.05877 | 2026-01-14 11:55:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 4d880ce8-2af0-3a88-b485-e38664237311 | -7.25791 | -43.05104 | 2026-01-14 11:55:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 686.6 |
| fd904d27-42d9-34c9-8054-3130efda199c | -7.2681 | -43.04327 | 2026-01-14 11:55:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 126.1 |
| 660e7a80-f671-3c8b-928e-319dcb9559c0 | -10.51648 | -42.40039 | 2026-01-14 11:55:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 28.0 |
| 170c1044-1ecc-3a91-b872-29c5f3b049e8 | -7.32689 | -44.24765 | 2026-01-14 11:55:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| de50fe2c-c54a-3ae0-ba19-de43c65be08e | -6.86219 | -41.35511 | 2026-01-14 11:55:00 | TERRA_M-M | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| c772c7a3-6484-3ce7-8ade-0788f94865be | -8.1608 | -43.18381 | 2026-01-14 11:55:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 42.9 |
| 9fcf9001-35ea-3b92-a8e4-7c559057d0c1 | -7.0627 | -38.65062 | 2026-01-14 11:55:00 | TERRA_M-M | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 72162873-6a92-3383-874b-2877dd2f7e5a | -9.60065 | -41.61632 | 2026-01-14 11:55:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 298de40b-798b-3203-9cca-2c4d37e88907 | -10.08518 | -43.97521 | 2026-01-14 11:55:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 47000b32-5074-3611-87d9-584fd912e924 | -7.32818 | -44.23875 | 2026-01-14 11:55:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| ef80c3f7-123a-3d31-a6b7-63c8470baa8f | -7.25663 | -43.06001 | 2026-01-14 11:55:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 551e60f3-51c6-35f8-a38f-5e4a0aba022c | -8.15317 | -43.17354 | 2026-01-14 11:55:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 7642ae67-09cf-3d1c-9670-cc2862f998e0 | -10.09525 | -38.51202 | 2026-01-14 11:55:00 | TERRA_M-M | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 25.8 |
| 44fcd223-8538-3afb-a09b-d5cc6cf326b7 | -7.26681 | -43.05227 | 2026-01-14 11:55:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 312.8 |
| f9f3c1db-bd22-3307-848a-bbe8a8ea1de4 | -10.0776 | -43.96501 | 2026-01-14 11:55:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 26afba4b-4217-33e1-8c42-7628803c2b1f | -14.36981 | -40.7004 | 2026-01-14 11:57:00 | TERRA_M-M | BOM JESUS DA SERRA | BAHIA | Brasil | 2903953 | 29 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 6146c74f-8ecb-3f9d-8cac-6da5d8ef2ba4 | -12.11017 | -45.6054 | 2026-01-14 11:57:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 54d23768-eeb8-3cf5-8939-b84b3c652c83 | -12.1115 | -45.59628 | 2026-01-14 11:57:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 235.4 |
| 5f1177ea-03ae-3a6b-910a-b726ef8a12cb | -12.10261 | -45.59496 | 2026-01-14 11:57:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 435.5 |
| 4480b1a1-da80-3430-a48a-1d5a0b570889 | -13.42842 | -43.8549 | 2026-01-14 11:57:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 35629b80-cd2e-3f70-b868-0e97987295fa | -12.10127 | -45.60408 | 2026-01-14 11:57:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 485.4 |
| 0236a434-2d99-3e9e-82db-74e480d1fd4a | -12.10528 | -45.57675 | 2026-01-14 11:57:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 763e653e-119d-3aad-9d4e-620a8931c2d0 | -11.85502 | -43.71257 | 2026-01-14 11:57:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0b06dfd7-1ce9-30a1-8e85-bd9f74b890b0 | -12.11284 | -45.58716 | 2026-01-14 11:57:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 249.1 |
| fcbc32dd-ebfa-3a23-ae06-0b4f5ecaf72d | -12.00437 | -45.18925 | 2026-01-14 11:57:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4a74846d-9474-32bc-a3c5-67634ba7b2e6 | -10.83038 | -44.95571 | 2026-01-14 11:57:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 677d2ea8-4891-3bf3-b034-0c524b142043 | -11.85243 | -43.73108 | 2026-01-14 11:57:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| cae919bf-db26-393a-b76a-32a8c3218feb | -10.55977 | -44.33552 | 2026-01-14 11:57:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4ddd9c4d-fbe2-38f9-b51e-365e7d057750 | -15.31974 | -42.04149 | 2026-01-14 11:57:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| bf75783e-6ba9-3dc1-a376-39dc19130ad7 | -12.11417 | -45.57806 | 2026-01-14 11:57:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 38cb6987-d345-31c1-8c98-c6196e9ef4bc | -12.1155 | -45.56897 | 2026-01-14 11:57:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 34.6 |
| fcd52a8b-e916-333a-a4b7-b35b012c5980 | -13.06494 | -42.52029 | 2026-01-14 11:57:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 8821729c-bca5-3729-8e59-63977d422f27 | -11.85372 | -43.72182 | 2026-01-14 11:57:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| f7e22b74-ba5f-3c03-916b-a70a675e4898 | -12.37939 | -43.44992 | 2026-01-14 11:57:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c08f422f-e5f8-3cf4-a369-a59e6666a8fa | -12.10394 | -45.58585 | 2026-01-14 11:57:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 03a2de48-e24e-3fd5-9985-7efb9e541e60 | -12.08765 | -43.76363 | 2026-01-14 11:57:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| f0b32386-13b9-3204-86dd-a589b9fb986c | -20.79328 | -40.81052 | 2026-01-14 11:59:00 | TERRA_M-M | ICONHA | ESPÍRITO SANTO | Brasil | 3202603 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 45689f1f-0a25-34ce-ad09-9a71d3c2af25 | -22.46978 | -42.64882 | 2026-01-14 11:59:00 | TERRA_M-M | CACHOEIRAS DE MACACU | RIO DE JANEIRO | Brasil | 3300803 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 40066de7-f342-30d4-9fb7-317afc64f9b5 | -22.78021 | -43.70098 | 2026-01-14 11:59:00 | TERRA_M-M | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 19.4 |
| 8e0e90f1-44d4-372a-a64c-107c141a88e1 | -7.2599 | -43.041 | 2026-01-14 12:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 439.7 |
| 221f3c89-5c7d-3695-9340-a6da0dd07a57 | -7.2599 | -43.041 | 2026-01-14 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 370.0 |
| 487a25dd-4cf8-320b-80fb-57f883286e5b | -7.2411 | -43.0428 | 2026-01-14 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 393.8 |
| c3f3319b-4a4c-3bab-b738-a44442e2ecde | -7.2411 | -43.0428 | 2026-01-14 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 371.3 |
| 658f9072-bfdd-3591-a062-60287f996961 | -7.2599 | -43.041 | 2026-01-14 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 320.3 |
| f56954af-b8f5-3da1-a43c-2aa0abe39ecd | -7.2411 | -43.0428 | 2026-01-14 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 341.8 |
| abe888d1-667b-3f74-9651-b833e38cac5a | -7.2599 | -43.041 | 2026-01-14 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 266.5 |
| ce9aaa88-2135-34e0-a448-2e9417aea27e | -7.2411 | -43.0428 | 2026-01-14 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 324.6 |
| 88c2bf31-be6d-3bae-97b1-1eacfcf18e53 | -7.2599 | -43.041 | 2026-01-14 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 305.5 |
| f51913a7-df20-3323-876d-26ffe2f0a2c6 | -7.2599 | -43.041 | 2026-01-14 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 255.8 |
| 10887db1-7419-381c-aed3-c8cd4dc0b58f | -7.2411 | -43.0428 | 2026-01-14 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 275.7 |
| 9521f033-d8d5-3025-9632-2eaf15250eda | -7.2599 | -43.041 | 2026-01-14 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 223.7 |
| 8621fc64-6a8a-39cd-9f8b-5bddf98793fe | -7.2411 | -43.0428 | 2026-01-14 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 266.4 |
| a67f0dab-bcba-3245-8cde-c8ca29edd430 | -11.8473 | -43.7256 | 2026-01-14 14:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 79705037-6b53-3c6f-99ff-a0f004906997 | -11.8473 | -43.7256 | 2026-01-14 14:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 142.1 |
| ff87ea29-1290-3bfe-a600-e15ed4838227 | -10.1518 | -42.218 | 2026-01-14 14:10:00 | GOES-19 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 104.1 |
| 2d959d56-779a-3f88-b094-8122a1651fb1 | -10.1518 | -42.218 | 2026-01-14 14:20:00 | GOES-19 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 98.5 |
| e42eec54-5e93-38c4-b957-483f1c7d5003 | -10.171 | -42.2152 | 2026-01-14 14:20:00 | GOES-19 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 87.0 |


