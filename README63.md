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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afc138dc-4023-3ca5-9d82-c3269481b4be | -5.86511 | -52.05088 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df6db587-4796-36bd-aa09-6818a4bd5e71 | -10.94052 | -53.05717 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 014f32f3-3ebf-391a-a5fa-87b7531e54d2 | -13.25485 | -46.91451 | 2026-09-18 04:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c341d7e8-5960-38c3-a0a9-10372e3b5ce2 | -10.88013 | -54.004 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 505abc30-b2f7-3fcc-8b00-ea6356598157 | -11.02295 | -54.15213 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc72810c-a7d9-3be0-8c30-ec2d2089e088 | -10.49707 | -46.28402 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f296ed2-9dc2-3b7d-ad90-c496b89b3de0 | -6.66231 | -50.90987 | 2026-09-18 04:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ba10ff3-7c0b-332d-8a3f-058c14493674 | -7.0893 | -46.15195 | 2026-09-18 04:57:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c84eff63-2ba4-3284-9cdf-d80ad4e17dd7 | -7.10925 | -55.12563 | 2026-09-18 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 300fbf52-3e25-3070-8f7e-09608d208fee | -10.67808 | -50.28466 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f8e15bc-3151-3e14-817b-dddf652e96fa | -7.80068 | -44.90026 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b707d47-813b-3c36-82b0-ca791f01ade6 | -10.51765 | -46.71859 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a526f93e-9ae9-34aa-98a0-6ea3dc3c31dc | -7.01887 | -44.65516 | 2026-09-18 04:57:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f99d7ed3-d578-3db8-98fe-aee1312b3399 | -10.53873 | -44.84563 | 2026-09-18 04:57:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a89606dd-283a-33f6-ad56-f084d6c8302e | -8.54001 | -44.55411 | 2026-09-18 04:57:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f8f557ee-5ed0-3e28-9396-40b348700049 | -9.09125 | -45.72177 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 52228dee-d1df-3f74-a006-5ac784e88b8e | -9.91248 | -46.52995 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e9b2921-b9c2-39b2-84e3-b85ae1bf1f9d | -7.0571 | -47.47382 | 2026-09-18 04:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7dbc2b8e-8cc7-36ae-b463-77042f461c47 | -9.92373 | -46.56897 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6f9e79e-e36e-3372-a084-72d8d2b7d423 | -9.71371 | -54.81431 | 2026-09-18 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a02e8e3f-f34d-3e8b-86f6-1c85ca2a7f88 | -8.88641 | -45.89366 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4816b190-82e5-3f83-a008-ef588d50e506 | -4.88582 | -56.06327 | 2026-09-18 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad05b51c-3d0d-3f50-8a79-32acd674d302 | -12.41934 | -50.70535 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 40b278ef-bc01-31b5-b7f5-a90738002e7b | -4.87986 | -56.07364 | 2026-09-18 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7981ae7d-f712-3694-b853-665dd0a91610 | -5.85888 | -52.06828 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05bae7d6-0d66-307c-90d8-d1b300060d89 | -9.83877 | -48.34543 | 2026-09-18 04:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1e88187d-0a69-39eb-a2d6-3b67fbee93b6 | -10.67067 | -50.26442 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| e34c8980-2c98-3424-9cc6-e85b29ce733d | -9.86679 | -46.51162 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| acf76780-6feb-3b38-afef-4bd14fdfc309 | -8.4948 | -45.64856 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 636cfd86-e104-3fc8-a689-9d2df05edd2f | -9.94367 | -45.29451 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 30d26f26-e4f5-30bd-8bed-21ba6a711377 | -10.67124 | -50.2607 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d70eb0cb-d21d-3d1e-a7e0-96ae525818c2 | -10.65184 | -50.25002 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| af2da864-b1a3-357b-9051-eb3cf973df56 | -12.53078 | -47.09316 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa4d835d-d548-35b6-a292-68f25146673d | -9.71252 | -48.15118 | 2026-09-18 04:57:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9a15f17-622c-3d73-a728-11dbfaa1fc7d | -9.75577 | -46.08731 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ccc709bd-1f55-3e1c-8ccf-703c0d845a8f | -10.64098 | -50.2292 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c3d45223-2019-3f22-9e1f-a64cfdd74166 | -8.65624 | -47.467 | 2026-09-18 04:57:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 064426ae-9780-3321-a0d2-823296b601b6 | -11.47413 | -45.7164 | 2026-09-18 04:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e4348ec4-a136-3004-a144-b5bf89d064c4 | -11.28024 | -43.37117 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fb25f19-91d1-3c5a-8a59-c38b17d696bb | -10.67637 | -50.27295 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 5b6631ba-0022-37a2-a8a0-8be136ccf077 | -7.82352 | -44.89975 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2e02985-c504-3730-baa8-d292d8efe8c2 | -10.40312 | -46.6217 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 389b7c85-beaa-3a6c-ae36-b8b0d78ceb99 | -7.74881 | -44.67686 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e7f5160-ac41-3fb4-81e6-061ddb9f3d4b | -11.30813 | -46.77425 | 2026-09-18 04:57:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 999521cb-abd0-3dab-b339-222b52430bd1 | -7.00422 | -43.86449 | 2026-09-18 04:57:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6c19cf22-4299-3496-8a60-d8ec18c9671b | -8.45799 | -44.50032 | 2026-09-18 04:57:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86b66894-d74b-352b-aed6-f13f53562bac | -12.31304 | -50.73834 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7cab3095-0d14-31e0-9c38-4b0851e580d8 | -5.86003 | -52.06108 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa8bb082-51cf-3669-adec-dfe8f73b0e01 | -10.13157 | -45.57228 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6545f1b-9c6c-3618-93d2-df5141a5e3c0 | -10.0196 | -45.50684 | 2026-09-18 04:57:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e3af1f90-8dbf-300f-9c9a-ba7b265f8db1 | -9.91562 | -46.50778 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0e429bb-37f0-316a-a99f-65b59d1aed7f | -12.30565 | -50.74099 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eaed6e94-e9f6-3051-8305-ee8b27aa1970 | -6.45673 | -46.00801 | 2026-09-18 04:57:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abbbebae-f759-3439-beb0-0021036f38e5 | -12.38913 | -50.69676 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08337e93-40d1-3f61-b046-51baed316745 | -8.23434 | -50.65607 | 2026-09-18 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67c70915-177f-3a25-a49f-ea710882a90a | -9.94033 | -45.33718 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4aac15f-a422-374f-bba6-80c3711a7655 | -10.71314 | -54.01533 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf81ddd2-d4fa-3f3b-a401-4c7988bf1fd0 | -9.91086 | -46.54137 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 076cc6a2-1014-3a70-ac77-0746e8495529 | -8.95206 | -51.46701 | 2026-09-18 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58f4c8f4-bf00-3889-b89a-3ab16d36f0fe | -11.76839 | -47.42865 | 2026-09-18 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16d38d08-6ea3-3490-9a3a-75ffd05816f2 | -9.19276 | -46.76481 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 469bad44-92c5-3a1e-a8e3-8aecc609b8b2 | -11.9848 | -52.46036 | 2026-09-18 04:57:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 318c291f-1296-3376-80a2-8582cfb673c6 | -11.55822 | -46.89568 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a2010a7-7947-3e66-b4bc-b2fd877328b5 | -9.778 | -48.36059 | 2026-09-18 04:57:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 464c1888-96f8-3c39-bf02-d284ddd3d107 | -6.66621 | -50.9283 | 2026-09-18 04:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| caa822ae-02c4-3a31-be59-1e35c9d9d7ef | -6.61401 | -44.20511 | 2026-09-18 04:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c155389a-b239-347f-90a7-1cf4ac5430a9 | -12.17798 | -46.97957 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77b0c2c3-019c-3fbb-93ee-c7b29440af70 | -11.53715 | -46.88165 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd6b3764-2bf5-3ebb-bbbd-3e8358c6c4f0 | -13.25063 | -46.91394 | 2026-09-18 04:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a854dd35-c9a7-30b7-95ed-5284011dc4e2 | -7.80575 | -44.89667 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a1548fbe-3af4-389c-9f77-7fcb3ba6336e | -10.61728 | -46.06421 | 2026-09-18 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f162cead-3b68-37d2-9466-0b18c31d9693 | -9.9134 | -46.55305 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e723b9fa-bc65-376e-a4b8-a9d1c1a51347 | -11.52392 | -46.85644 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69acd7f1-731d-3e00-bfc0-eddc699dd864 | -9.60293 | -45.36437 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1403e00e-c23e-33ee-bb10-309ee2845d6a | -12.4448 | -49.59038 | 2026-09-18 04:57:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74030a93-88a6-387b-8a7b-076fa8cef418 | -7.09079 | -42.09024 | 2026-09-18 04:57:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c9e8b5c9-200a-3048-a3a5-d2c91a7fa66d | -11.31624 | -43.42082 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8d37e6d-db3e-3001-848c-02a75040b131 | -11.52178 | -46.87151 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 629ca535-8483-3f98-b76e-6ff4f84491d7 | -7.67129 | -46.10918 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69aaa6d3-a92a-3930-868c-3345304d96bd | -10.11736 | -46.29594 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 81cbf3de-95a7-3bfc-8c3c-a3a8182c201d | -7.75249 | -54.748 | 2026-09-18 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10c0a6e4-0381-317d-a70e-04bf13b2efba | -8.6768 | -45.30643 | 2026-09-18 04:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3914a449-c14b-35ab-9b31-a404b31e77ca | -13.47455 | -46.90298 | 2026-09-18 04:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0e01ba1c-67d2-3bc6-a334-1a3704a7f791 | -6.30116 | -45.69179 | 2026-09-18 04:57:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33bcd8bb-84db-3343-bab5-5cbc667cb255 | -9.93982 | -45.3214 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b0633a07-e833-3893-8667-2b065a0767d9 | -12.9983 | -46.93904 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a363725-b2b8-3423-9b27-dcc7ba2db408 | -12.25925 | -47.14164 | 2026-09-18 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e679064-cde5-31b3-8bc3-d984300f1a20 | -8.77526 | -46.90473 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bff5a1f8-9212-3ffe-b13a-3207a65ebed3 | -6.52195 | -49.89149 | 2026-09-18 04:57:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fecc11d-141d-35ef-bf4d-d2dcc0eb4dc3 | -5.86224 | -52.06883 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a163a6e1-4d83-3817-9d8a-db7ea3218c6a | -9.5993 | -45.85895 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fb4ae512-377d-30e9-8c71-0a8e27b9a5df | -8.45178 | -45.83815 | 2026-09-18 04:57:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbd6455d-6f6d-31c8-a677-ab3ea36c34df | -11.53499 | -46.88116 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50479bd1-5e77-3286-985c-b288a5e70307 | -9.39707 | -46.86208 | 2026-09-18 04:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 566753c1-3ed5-3ca4-8f9f-fb71ab92e009 | -6.96207 | -46.95082 | 2026-09-18 04:57:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67609b6d-f278-3b4b-bc12-256d6ccb4b14 | -12.26075 | -47.1306 | 2026-09-18 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9f55f7e-3097-313f-bd9a-3929475ce341 | -10.64327 | -50.23721 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| cfa38f48-7aaa-38f8-b4ee-3fce9f482c5d | -7.47984 | -45.29889 | 2026-09-18 04:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe4ad7aa-5a0e-3360-be8f-ef7e8102a7ed | -11.27147 | -54.13035 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e6bd85d-cbb9-319a-9149-e813c31f5334 | -7.01273 | -43.63595 | 2026-09-18 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |


[Clique aqui para ver as próximas entradas](README64.md)
