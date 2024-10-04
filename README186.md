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

## Dados Diários - Página 186

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72e91157-c3f4-37df-b6f5-a3f8d6fd197f | -10.2571 | -47.7017 | 2024-10-04 11:46:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 194aaf96-de03-314a-8fd9-b88151c23a38 | -10.7445 | -45.6002 | 2024-10-04 11:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| d813401b-eb88-3e92-8165-d42c9b4c3276 | -10.8996 | -46.6216 | 2024-10-04 11:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| fa187451-db51-3b08-afa6-e8a4928b57b1 | -10.8992 | -46.6442 | 2024-10-04 11:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 39ea5bc4-3566-3a96-a9ff-3a18296620b7 | -11.2178 | -46.9622 | 2024-10-04 11:46:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 2ebdb5bd-b19e-3e89-a97d-ff132c7bf33d | -11.2369 | -46.9597 | 2024-10-04 11:46:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 369.4 |
| f3de872e-8262-3522-920f-d7ae092876f9 | -11.404 | -47.2287 | 2024-10-04 11:46:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| ced18f87-210b-3de8-8f55-274d8223c9f4 | -11.3849 | -47.2312 | 2024-10-04 11:46:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 2f5d6aea-8572-3cfb-866e-89be0c34c658 | -11.3536 | -50.5304 | 2024-10-04 11:46:10 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 2ebe3f60-4891-3db1-bc6d-e1791de99e98 | -13.1443 | -46.3261 | 2024-10-04 11:46:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 177.3 |
| f694e686-4e5d-3834-90f6-3b5de5a5c17f | -13.1779 | -48.6737 | 2024-10-04 11:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 94.5 |
| a1448ca3-3980-3604-8126-bdeb3db99824 | -13.1791 | -48.6073 | 2024-10-04 11:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 93.1 |
| cd5a2586-410f-3f45-af89-7a150f8c0d59 | -13.1787 | -48.6295 | 2024-10-04 11:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 3fc7b00a-9de9-3b31-ba5d-a6e490d53f3a | -13.1587 | -48.6764 | 2024-10-04 11:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 90835d9f-0cb5-331a-b01c-7384bee8d313 | -13.1595 | -48.6322 | 2024-10-04 11:46:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| e828d832-bd92-38e8-b53a-285940cc7111 | -13.1447 | -46.3033 | 2024-10-04 11:46:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 104.3 |
| e99d1124-1b4d-3f17-a6bc-724e5a0c91c1 | -13.1636 | -46.3231 | 2024-10-04 11:46:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 63255dd0-5fc3-392b-9483-3d75b68e30af | -15.6304 | -47.2063 | 2024-10-04 11:46:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 3f9e186e-e36e-3542-b441-3f45d7e2b8e6 | -16.5938 | -57.1783 | 2024-10-04 11:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 221.3 |
| 5660db4f-2768-3ec3-9d08-d06c5d8a1921 | -16.613 | -57.1965 | 2024-10-04 11:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.4 |
| 08eda608-3a5a-3fea-9c73-224da56b302b | -16.5935 | -57.1988 | 2024-10-04 11:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.5 |
| a2c48284-a026-3587-8f1d-ef60340f63e0 | -16.6133 | -57.176 | 2024-10-04 11:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.8 |
| 6a2c15a9-c1db-3fb3-8103-0ab34d511bb5 | -18.7952 | -46.6393 | 2024-10-04 11:46:50 | GOES-16 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 138.6 |
| c872c0c2-31ca-352d-87fe-cbdf21caaa6c | -3.51583 | -43.28411 | 2024-10-04 11:55:00 | TERRA_M-M | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 2f22bdc8-64f3-3aa1-b597-1f5d94b40320 | -8.8362 | -45.1688 | 2024-10-04 11:55:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 1149285d-3c26-3dae-a94b-55666e617e3e | -9.8353 | -46.7502 | 2024-10-04 11:56:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| c13d1256-bab6-3914-b994-65b66ed9ef1f | -10.2761 | -47.6995 | 2024-10-04 11:56:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| cf770cbb-054c-32ef-99b4-9c8e1aa5bdf2 | -10.2381 | -47.7038 | 2024-10-04 11:56:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| a2a06944-3374-3771-ac2e-c0638abdea0a | -10.2571 | -47.7017 | 2024-10-04 11:56:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 16b3bdb8-7a17-3d91-8f54-46803cf654e2 | -10.2378 | -47.726 | 2024-10-04 11:56:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 2082dae6-518e-3455-97d8-6d2611bbfb58 | -10.7309 | -47.7126 | 2024-10-04 11:56:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 1dd284e2-df60-39e6-84f7-d266a2752a00 | -10.8992 | -46.6442 | 2024-10-04 11:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 13dd5a51-e322-3978-863a-fbf559ec8fde | -11.2369 | -46.9597 | 2024-10-04 11:56:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 241.4 |
| 3371e690-a413-3529-81f0-c3fff81c066a | -11.2779 | -43.4118 | 2024-10-04 11:56:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 03bbe510-5166-3a4a-8c7d-c8e192c8321c | -11.2783 | -43.388 | 2024-10-04 11:56:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 255.0 |
| ab2d067e-79de-3d08-925c-6c7d8d56a356 | -11.2971 | -43.4088 | 2024-10-04 11:56:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.0 |
| b584bf88-1327-33d3-b1a5-7310442b70bd | -11.404 | -47.2287 | 2024-10-04 11:56:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| a2ab8fe4-e252-3be3-b2cf-76d5b6710db3 | -11.3341 | -46.8349 | 2024-10-04 11:56:10 | GOES-16 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 3f023a8b-eaf8-3c28-b053-256b7e99e14e | -13.1163 | -51.1765 | 2024-10-04 11:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 1c7e6082-ea5c-3a2d-8bde-a201e423041c | -13.1595 | -48.6322 | 2024-10-04 11:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 167.4 |
| edac4685-9a49-357b-9f47-89e4825a6b3b | -13.0598 | -51.1195 | 2024-10-04 11:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 400.5 |
| 7e954a85-d3f8-3d3a-9115-812b45ad93a2 | -13.1587 | -48.6764 | 2024-10-04 11:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 8f70aaf5-ef43-368a-890a-ced83cfa40bb | -13.1787 | -48.6295 | 2024-10-04 11:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 89cdc859-7ebf-3087-b008-13e4211b5bea | -13.1791 | -48.6073 | 2024-10-04 11:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| d71327bf-7b44-3655-b537-20b173af785c | -13.0594 | -51.1409 | 2024-10-04 11:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 2fb8fa95-a64f-3dfd-a9ca-bf497512f5e5 | -13.1591 | -48.6543 | 2024-10-04 11:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 45bd113c-c01c-3017-a1aa-9a18f31073ae | -13.0786 | -51.1385 | 2024-10-04 11:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 367.5 |
| 86c7d88d-5d39-362f-a512-0197adc16b7e | -13.1779 | -48.6737 | 2024-10-04 11:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 3ec04bb4-c1f4-344d-804c-8615e48e21a0 | -13.1636 | -46.3231 | 2024-10-04 11:56:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 1f072989-f39c-331c-9a33-281497c154e5 | -13.1599 | -48.6101 | 2024-10-04 11:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 43d949cb-55d6-3f97-8464-be9e5355d861 | -13.1447 | -46.3033 | 2024-10-04 11:56:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| b7afd531-6eec-33e4-b675-78e83e885c32 | -13.1443 | -46.3261 | 2024-10-04 11:56:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 35e542d1-a5cf-37f0-b014-0c45a8326dea | -16.6133 | -57.176 | 2024-10-04 11:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 142.3 |
| f279c216-fa6c-3bb5-8420-08d923ff7073 | -16.5935 | -57.1988 | 2024-10-04 11:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 175.5 |
| 0f6c7554-8702-3f60-b080-037eaea63783 | -16.613 | -57.1965 | 2024-10-04 11:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 140.7 |
| 142c3d2d-7891-370b-a4bc-ff1988b08702 | -17.1574 | -57.3993 | 2024-10-04 11:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.1 |
| f6a57ca6-aeb9-3dee-970f-fe296dd4f112 | -17.1378 | -57.4016 | 2024-10-04 11:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 4e83764b-a779-3a47-8ce8-d3ac67329f89 | -18.7952 | -46.6393 | 2024-10-04 11:56:50 | GOES-16 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 7c6a99a6-8fe6-3d88-89d6-a40d0b7a7a59 | -10.90046 | -46.61806 | 2024-10-04 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 2468cad1-59d9-3b04-abe5-6511b30486da | -10.75476 | -45.59595 | 2024-10-04 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 07f312d2-8cac-30ba-b46b-47ab85233f64 | -7.33975 | -35.02201 | 2024-10-04 11:57:00 | TERRA_M-M | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 54.4 |
| 739b3b0d-3191-3b90-be83-0a6710152c65 | -7.2644 | -34.96861 | 2024-10-04 11:57:00 | TERRA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 38.5 |
| b5b48e8d-397c-365f-8594-b5931ff87612 | -7.26312 | -34.97749 | 2024-10-04 11:57:00 | TERRA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| aa247c17-bb5e-3330-9a94-583d5a48e943 | -7.25553 | -34.96735 | 2024-10-04 11:57:00 | TERRA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 150.2 |
| 97d2da8c-14ee-381f-a70b-5253f9454259 | -7.25425 | -34.97623 | 2024-10-04 11:57:00 | TERRA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 183.0 |
| 5e8de635-655a-3e85-a742-ea20da0b4380 | -8.62258 | -35.13683 | 2024-10-04 11:57:00 | TERRA_M-M | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 2ed5bc9c-9c2c-3de5-a516-5caa3c8796ca | -10.03981 | -36.41718 | 2024-10-04 11:57:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 4f48777d-25f6-340a-90ef-f25c02fd366f | -7.42575 | -37.25514 | 2024-10-04 11:57:00 | TERRA_M-M | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 63f0b0fc-a3fe-365e-8f6a-e11dc5311dbf | -8.64806 | -36.90965 | 2024-10-04 11:57:00 | TERRA_M-M | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 8.2 |
| fdd629ba-8387-310c-95f9-5482ca533722 | -11.65322 | -38.0938 | 2024-10-04 11:57:00 | TERRA_M-M | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 6c7bd212-808a-3e50-a1d8-940ea2ba4c07 | -6.72973 | -37.59418 | 2024-10-04 11:57:00 | TERRA_M-M | VISTA SERRANA | PARAÍBA | Brasil | 2505501 | 25 | 33 | nan | nan | nan | Caatinga | 34.3 |
| 3165163c-e8f3-3b39-a977-49d99be6326d | -8.86685 | -40.98737 | 2024-10-04 11:57:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 48.8 |
| 483221a1-bc56-3176-b281-8bf17bf4930a | -6.65443 | -41.99862 | 2024-10-04 11:57:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 57.1 |
| d1ad8b18-4fb9-39cd-b615-a25261d6ec53 | -6.64692 | -41.99038 | 2024-10-04 11:57:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 661.7 |
| db993408-3a78-31c7-aad3-bd3ad298162c | -6.64455 | -41.97437 | 2024-10-04 11:57:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 85.2 |
| 912112b6-01f4-3154-8c20-594295c7f5ce | -6.64348 | -42.0126 | 2024-10-04 11:57:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 242.5 |
| 19277ca4-9d9c-3b6b-bcf2-740c05cf5b79 | -6.64096 | -41.99637 | 2024-10-04 11:57:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 985.8 |
| 98c89945-8994-31ef-a9b6-ae58f82d1c95 | -6.63344 | -41.98825 | 2024-10-04 11:57:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 340.7 |
| 1e415ddc-950b-3dc1-8657-943c059fbfd5 | -6.62996 | -42.01057 | 2024-10-04 11:57:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 106.1 |
| ff80f439-84db-3359-a0cf-089bb584abeb | -9.99113 | -42.08199 | 2024-10-04 11:57:00 | TERRA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 221c840d-779a-3d83-8e4e-bb7a00b28847 | -9.98777 | -42.10257 | 2024-10-04 11:57:00 | TERRA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 66.5 |
| bf67d76e-0d7d-3e43-9284-caa346257b52 | -12.30464 | -42.25887 | 2024-10-04 11:57:00 | TERRA_M-M | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 64.0 |
| 3946d3bc-598e-348b-a228-1884f28a7290 | -12.30278 | -42.25174 | 2024-10-04 11:57:00 | TERRA_M-M | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 52.8 |
| 52e24b05-384d-3f5f-af7b-883c89888ee8 | -11.66937 | -42.66751 | 2024-10-04 11:57:00 | TERRA_M-M | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 33.5 |
| 541b93b7-dacb-3dce-896d-0944e735dc46 | -11.66701 | -42.67444 | 2024-10-04 11:57:00 | TERRA_M-M | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 32.0 |
| 839d1110-a755-343e-afcd-ab0c8f224ae9 | -12.70732 | -42.02959 | 2024-10-04 11:57:00 | TERRA_M-M | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 470a97d7-5801-33b3-aa54-595468a75cb8 | -12.33038 | -42.64427 | 2024-10-04 11:57:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 77241c77-78f6-30d3-8881-5433e450bde2 | -12.3239 | -42.60853 | 2024-10-04 11:57:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 0e2c636b-22c1-3c0e-b721-62c16f2c22ca | -10.63235 | -45.20028 | 2024-10-04 11:57:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 7a0e8c04-9cd2-393a-91f3-9f57304e6136 | -11.2952 | -43.38628 | 2024-10-04 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 383.2 |
| 2b072d67-88f3-33f5-b40d-54b15bee4943 | -11.2911 | -43.40999 | 2024-10-04 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 194.6 |
| dba636bd-4f37-3d28-ae13-7d6df2d4ccfb | -11.28946 | -43.37906 | 2024-10-04 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 254.7 |
| 8da7de1f-d556-34cd-b29d-b41d92ef7fa5 | -11.2855 | -43.40296 | 2024-10-04 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 404.1 |
| e61ac9ad-49c9-3e05-9351-b320d6ff765f | -5.72232 | -43.81313 | 2024-10-04 11:57:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 213.9 |
| f7ad1531-25d8-32be-bc0c-8912ff65f554 | -5.72095 | -43.78591 | 2024-10-04 11:57:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 552.7 |
| 99c5becf-10fa-364b-8bda-86c4cf339d54 | -5.71566 | -43.81808 | 2024-10-04 11:57:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 161.1 |
| 4acca394-bf9d-3e57-98c1-fb8fbf177f98 | -5.71159 | -43.77847 | 2024-10-04 11:57:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| e44d5f2b-807e-32bd-a813-42c98c52af0d | -6.19638 | -44.13169 | 2024-10-04 11:57:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| e1f8edcf-0391-3f71-835c-0fc9e503f37b | -7.8509 | -45.33688 | 2024-10-04 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 183.5 |
| 8698f418-4963-3448-9473-9af19154b404 | -7.6743 | -45.22155 | 2024-10-04 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 98.3 |


[Clique aqui para ver as próximas entradas](README187.md)
