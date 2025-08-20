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
| a89e49b3-f35f-3df2-b6b3-3b5baa9e9794 | -6.06958 | -44.11773 | 2025-08-20 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 363f6d58-f4dd-39cb-92e1-393eb182968b | -4.39638 | -42.14449 | 2025-08-20 04:34:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d6a39aff-3f53-309e-b9b9-42ad578628f1 | -6.63101 | -35.06165 | 2025-08-20 04:34:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9b16307b-72d8-34bf-8ac8-b0af0f00a7c9 | -2.35029 | -47.4685 | 2025-08-20 04:34:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85a4ca98-1227-3715-bd38-5944e736c7ad | -5.69126 | -43.66797 | 2025-08-20 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 842f16d9-eff6-3bb5-bbb6-e8f9c25164b7 | -4.90919 | -43.238 | 2025-08-20 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 63276c0c-e2c5-3126-9b56-97cda9c19669 | -3.83799 | -47.73478 | 2025-08-20 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acb83a97-219b-362c-a912-aaa2a93d2b23 | -5.00253 | -56.03876 | 2025-08-20 04:34:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a68da100-de8d-38b8-ad14-488eee9af1d2 | -8.02507 | -47.66334 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f84597b-0a79-3c1d-b627-26325ce30e86 | -8.90159 | -47.33236 | 2025-08-20 04:34:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef2f5be9-5a3f-35a8-856f-6ba7e8f6d695 | -4.8583 | -43.44332 | 2025-08-20 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fafd1224-bfc7-32e1-9a07-67b7bce205cb | -3.81732 | -41.55808 | 2025-08-20 04:34:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5add78f8-a354-38f7-a131-d4c4f10d77b7 | -2.5842 | -51.92295 | 2025-08-20 04:34:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e671fba9-0b58-3cad-9dbc-2f1347092d88 | -6.23342 | -46.24429 | 2025-08-20 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2623ce1-c51a-3ec1-893a-2d33dcd148bb | -7.96656 | -55.2976 | 2025-08-20 04:34:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e234dc9f-b0d8-3c8c-bd40-0d444547a525 | -9.5748 | -43.325 | 2025-08-20 04:34:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e5464266-2256-3814-b0ca-afa5c0b06980 | -3.81674 | -41.56192 | 2025-08-20 04:34:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b219097e-eeae-3f76-9d23-a1c14f405b35 | -6.13946 | -57.71515 | 2025-08-20 04:34:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd521990-04f1-3a5b-b25f-284fed34bca4 | -7.5907 | -44.39035 | 2025-08-20 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cfa7a468-1bf4-3ce0-b9fd-eaf155b0b937 | -9.37783 | -48.28583 | 2025-08-20 04:34:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49b9a981-1f33-3880-b40e-b8e945c4f3e0 | -9.53112 | -45.1754 | 2025-08-20 04:34:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 252c23c7-f231-397a-860b-7138fb4c5bc5 | -6.00638 | -42.84733 | 2025-08-20 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a9e155b6-0d16-3b72-90dd-2c0c610a1af6 | -5.99367 | -42.85074 | 2025-08-20 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| fae8cef1-2a4c-371c-8920-820b11e5fe7b | -7.64434 | -45.28708 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1677bb0-91f4-35c2-8a6a-799903a33e29 | -8.8257 | -52.06354 | 2025-08-20 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25b0efbe-4326-3cb1-8adf-7fe8997fa444 | -6.86404 | -43.60382 | 2025-08-20 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb1cf5a9-4c59-3498-9fc2-084ee5043457 | -2.44771 | -47.32721 | 2025-08-20 04:34:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f017759b-de63-3708-87ec-d7252e4da8d3 | -6.37208 | -44.74813 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ba66967f-806f-3a34-8c07-6938d41025e6 | -6.31848 | -43.74952 | 2025-08-20 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1ce08f8e-2051-3da3-869b-3cbc2bb801ee | -6.45261 | -45.49647 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d4f440d-a812-3fbf-a37a-60fb5942226c | -3.05141 | -47.01545 | 2025-08-20 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb61a151-97a6-3377-b4d6-a5eb1cc5a60b | -4.95951 | -47.59879 | 2025-08-20 04:34:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d6c3feb-d790-323b-b80f-9e94f76d9c1f | -7.74247 | -44.09034 | 2025-08-20 04:34:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e81c33a5-2b3f-3dc2-90ed-1a05eedbe108 | -7.14742 | -44.59516 | 2025-08-20 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0be2ece4-adda-3b7f-9c60-f7ce973d2e4c | -5.48265 | -42.16537 | 2025-08-20 04:34:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dd2bc740-b887-3205-a6d1-fc4c949153be | -5.65218 | -43.37128 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c95c88a-59c6-3fea-b65f-64f8cac9e8b0 | -7.64518 | -45.27782 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a486df7-98fc-385c-87db-e9c04854fb89 | -5.98456 | -44.14204 | 2025-08-20 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 56c78590-9137-39c5-ad41-b3ab136c180a | -6.68494 | -43.67333 | 2025-08-20 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c5dd3c9-bda6-3d61-809b-78784b6b9dbc | -3.03846 | -49.43811 | 2025-08-20 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb65a956-0593-3eb7-a390-65dec5b934bc | -5.48734 | -42.16222 | 2025-08-20 04:34:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 71dbaa36-5d01-3a2c-adc4-6e642c8b8531 | -6.32409 | -43.60859 | 2025-08-20 04:34:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 806205e8-3106-38da-8163-979b35be1a36 | -6.62595 | -35.06345 | 2025-08-20 04:34:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1aca6864-3410-3c63-a348-791c217a0f9a | -5.98941 | -42.82443 | 2025-08-20 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 909370df-8fc1-3b3f-977e-a3136299f8d6 | -5.88201 | -46.5049 | 2025-08-20 04:34:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12268b45-611f-3c01-b894-732e6fafac95 | -5.328 | -43.92811 | 2025-08-20 04:34:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d7a7f13-f8cf-3ac8-9d2e-23547074bdfe | -6.00713 | -42.84225 | 2025-08-20 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7d389f0f-f12a-31b9-a3e1-aabbaffe3b8d | -7.63498 | -46.22476 | 2025-08-20 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2e11ba2-7da9-33a8-9e8b-2c0ffae5d34c | -6.32225 | -43.75018 | 2025-08-20 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5c357ed4-649a-3243-80f0-91803ad8bb50 | -6.06221 | -44.11657 | 2025-08-20 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e6d4b566-6e4d-3c63-a473-336a91371865 | -5.79783 | -59.21779 | 2025-08-20 04:34:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0b004fe-3261-3d42-a6d7-90b682ad8018 | -4.29491 | -48.0713 | 2025-08-20 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a0d1b33-ed23-3750-b2a1-3d800f30794b | -7.64044 | -45.28527 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 110d406b-f9b0-35ac-8784-aa8ff825d8d9 | -7.57951 | -45.42712 | 2025-08-20 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af73a565-b37f-3374-ac49-bdbd2a418d3d | -6.62516 | -35.0695 | 2025-08-20 04:34:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a711ca8a-f0c8-385b-a161-c327018f70e8 | -8.02065 | -47.66979 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e5cf02ee-8a66-37da-9c06-7c348fbe17f6 | -7.63985 | -45.28927 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4505e0c3-beb2-3c72-83c2-9ec9de25fb72 | -7.14283 | -44.18362 | 2025-08-20 04:34:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1ff22eb-50e3-3cf9-a6b9-ed74eb3f00a3 | -6.06893 | -44.12202 | 2025-08-20 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6e0644dd-234d-336a-9917-ab5398770964 | -8.21106 | -47.31198 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8c6cc98c-755e-31c1-8e76-0ce8d5a9c505 | -7.14982 | -44.60405 | 2025-08-20 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42f4b91f-61c5-33fa-ad20-24ead6cbf414 | -5.66169 | -43.50379 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aa42aa28-c624-3caa-9d69-ae9c2648c072 | -6.8595 | -43.60793 | 2025-08-20 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a82365a-0aa0-3b27-b746-e3a7c9c3af35 | -6.5607 | -43.49434 | 2025-08-20 04:34:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0470615f-8ce3-3a47-9d71-158949337aaf | -6.1681 | -46.14568 | 2025-08-20 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cf6e185a-18ff-32cd-b26a-0046add7fddf | -7.63787 | -45.28197 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46ea4bd1-01b0-326a-9164-10719bb2a198 | -6.72494 | -44.33366 | 2025-08-20 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40b5629c-c015-3c5d-8f51-26556fd14be7 | -7.6049 | -44.39677 | 2025-08-20 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bed8bae-d1b1-3863-a03e-6934985d8b03 | -5.28368 | -44.19322 | 2025-08-20 04:34:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 476cd0b7-278b-3c83-9f79-c4dd7a79c9c9 | -3.27016 | -49.14342 | 2025-08-20 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9aaa3fc5-3f18-3bf7-a602-85189c6b8b04 | -6.86787 | -43.60445 | 2025-08-20 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6b48460-bb76-3cfb-b849-4124c6a3570b | -3.64892 | -48.32772 | 2025-08-20 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 163ba697-2212-37d6-aea3-cc24e0186121 | -5.87781 | -48.12486 | 2025-08-20 04:34:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f368c47-ab32-3d32-a22e-c3de86691fdf | -8.83325 | -52.04108 | 2025-08-20 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e182c7b8-56d8-3fc2-99ba-c560dd09914a | -9.50245 | -43.16687 | 2025-08-20 04:34:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c8104df2-7e55-3aa1-8e32-bc1ae7c54298 | -6.56671 | -43.00348 | 2025-08-20 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf6c7144-6393-3f4c-971a-c25ebc80ec25 | -5.99338 | -42.82509 | 2025-08-20 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5f498a06-b041-3845-8a0b-7683d9299cb2 | -7.84339 | -45.11218 | 2025-08-20 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08a0f70b-533f-3834-9ca1-72af8ea915a0 | -6.0021 | -42.82123 | 2025-08-20 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9080bfff-155d-3860-9022-c17ce42f440f | -7.14377 | -44.59465 | 2025-08-20 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a9035eb2-ac98-3539-902a-1c3f40e5d4f5 | -6.71454 | -44.32766 | 2025-08-20 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13b22560-ec9b-30a3-882d-ffac0ade4f03 | -6.73636 | -41.53645 | 2025-08-20 04:34:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1d71191a-f522-34b5-8abe-851d5c1869ce | -4.42974 | -47.76024 | 2025-08-20 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb4dc7f1-2cd2-3a3a-a6a8-7fe298e18818 | -8.80258 | -45.4383 | 2025-08-20 04:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eae800bd-6b01-3b4e-a964-21ed6907e4a3 | -5.68972 | -43.55032 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6990c497-319c-3179-b6ec-1d7b3e4e9102 | -8.14022 | -49.51429 | 2025-08-20 04:34:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e445a6b4-f3a9-3190-beda-565689a7728e | -2.77147 | -48.59495 | 2025-08-20 04:34:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f2f7062-ddf8-3e17-94b8-10d81aba9258 | -4.48948 | -47.68078 | 2025-08-20 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0197f68-8fce-32c7-9211-786262485f11 | -5.70271 | -43.38569 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29d63520-7140-3417-8ea9-15e29dc22606 | -6.27026 | -43.7095 | 2025-08-20 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d71c300-c0a5-3e21-96d0-527d56050363 | -3.49533 | -48.92163 | 2025-08-20 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 07e3c18d-4a3a-3159-ab28-3b332e003927 | -6.86162 | -43.59362 | 2025-08-20 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a06c21be-aa5b-3eae-8021-ea15a4278c08 | -6.85182 | -43.60673 | 2025-08-20 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb58d25d-ce80-357d-a7b0-573602db3049 | -5.98391 | -44.14624 | 2025-08-20 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1e3cc2c6-2c75-364b-a26d-7c672ec5b170 | -7.65286 | -45.27493 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98a5e932-38f9-3b08-98c9-0303c63c1fd5 | -6.56991 | -43.00918 | 2025-08-20 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03016c32-f1d7-36e9-811a-13362d99295b | -8.3027 | -47.61406 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31420933-32fe-3350-b1e5-ed75f9e5d5c2 | -7.63327 | -45.26469 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 911308a0-d0e3-39da-b43a-ec1d49102c1e | -8.78868 | -45.48174 | 2025-08-20 04:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 475a7faa-bc29-3b2c-a845-b7b80ced75ea | -7.22677 | -44.70959 | 2025-08-20 04:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README26.md)
