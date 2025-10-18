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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8249731-2ef6-3cb2-af66-390842f679cf | -6.14285 | -44.29975 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b317b8cc-fe5e-3fbc-8f4b-2b5b5516f361 | -6.11785 | -43.66382 | 2025-10-18 04:29:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c72a59ec-22d2-3a74-9237-fd3969b9b267 | -6.20968 | -45.52793 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c30444e-31e7-3bf4-8485-a53304bad128 | -7.35291 | -43.85285 | 2025-10-18 04:29:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 010bc1d7-7c0e-3e73-9774-fb84368febbd | -5.12793 | -45.13312 | 2025-10-18 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 43a3a596-4a24-3a4c-8533-4ca11b41bbf1 | -10.82141 | -43.92966 | 2025-10-18 04:29:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b7781c3-f7d2-328a-8e5e-95d8daa51dd2 | -7.166 | -42.3695 | 2025-10-18 04:29:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 55d0e69c-be4d-3c43-9794-f790d62bd6d1 | -4.93728 | -47.30412 | 2025-10-18 04:29:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eec6f260-bc33-308c-85ac-55f87b044c1a | -10.4278 | -45.01742 | 2025-10-18 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 220250c3-d66a-3010-b48c-f442a254870e | -4.28114 | -49.9818 | 2025-10-18 04:29:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ac12617-8be8-3721-bf6a-43a189940428 | -10.29917 | -44.04224 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7f7c1de-c751-367f-b2e8-f55222d55747 | -6.52428 | -41.48889 | 2025-10-18 04:29:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 9dfda9e8-78e8-3a6c-9acb-b5a018da54f2 | -10.64663 | -45.32825 | 2025-10-18 04:29:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e9d08d9-28de-3ef7-970e-6b9074c61469 | -5.06244 | -45.85466 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6f947d8a-ff17-3189-9ba8-7322a041d7f5 | -10.64434 | -45.32008 | 2025-10-18 04:29:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30358230-1982-37b3-9888-996c563515d1 | -8.20333 | -43.96618 | 2025-10-18 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3df64f02-768c-3873-8321-1fd4b03cd43d | -8.38229 | -49.73328 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 560cd119-d8d8-3d31-bf5d-35fc51fb9c97 | -9.75707 | -43.96335 | 2025-10-18 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b7b8f98e-27c1-3702-a825-cda35bac22d9 | -7.45641 | -46.84175 | 2025-10-18 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c1aa422-f7ee-36b5-aca3-6267d3aac9bc | -6.36165 | -58.21146 | 2025-10-18 04:29:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4850e742-2bfb-3f8f-b578-664c8eae5b72 | -6.16648 | -42.59516 | 2025-10-18 04:29:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ea895f59-f2f7-3259-823e-7f9ec8933357 | -8.78637 | -47.93962 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ed5cc56-2f7f-3072-a4ee-4db701e48751 | -7.46929 | -49.31657 | 2025-10-18 04:29:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2a5a7ea-a15d-3978-9484-16de022ef244 | -8.38838 | -46.23594 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 332af315-c139-30b6-8d0e-320bffecee3a | -9.87833 | -47.65821 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a9563e8-b2c8-3d4a-917c-6b0e7812f61b | -5.96981 | -42.89393 | 2025-10-18 04:29:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 3f742611-34f7-3075-8c23-5f7fcedfd044 | -6.26312 | -44.33639 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82571711-4962-3b20-b200-a9102f982ccd | -10.24378 | -44.0402 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 969a1970-82b5-3124-88e8-06b230156b36 | -6.86939 | -44.70092 | 2025-10-18 04:29:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46925f98-582a-3d67-9fb2-44270fb81ac3 | -4.25332 | -48.37185 | 2025-10-18 04:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 890f87ad-3c37-34d5-a6eb-a389ccf3e0b9 | -5.78945 | -45.46951 | 2025-10-18 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7bc85dfe-bb99-3d26-86b1-71d8901407dc | -5.24638 | -50.96062 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f391c40a-1e8a-3d2f-8374-21686ca69571 | -8.20039 | -43.96159 | 2025-10-18 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 19406b3a-0189-3de0-b397-1f29759e989e | -7.74997 | -42.5117 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 270fb51a-e56d-31b7-91d2-5da315288235 | -4.94544 | -45.63062 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4606c8e0-c1bc-3f40-9da5-c6693a30dd4f | -6.23186 | -44.13601 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3bab8dcc-5012-3dd9-99e9-caec1c6ca228 | -8.17246 | -47.04208 | 2025-10-18 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89c950f6-a5e9-3580-adda-c03183862be7 | -6.52376 | -44.90318 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 505121fe-07be-3d36-a496-688d63a8f5f6 | -10.62625 | -42.30147 | 2025-10-18 04:29:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7ce675a7-e232-3313-9d9b-8ba41d1ce9b9 | -10.49148 | -43.41586 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eaf7aafa-f9e3-3cbb-82f8-708b562fe231 | -5.42208 | -45.65564 | 2025-10-18 04:29:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2ad7681-739d-3e76-931b-69aba2fa2751 | -4.0356 | -51.15762 | 2025-10-18 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 371bdf7f-ffdc-3a57-ba4c-75f15969708a | -6.23007 | -44.14747 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc528fc8-6548-3690-b5b3-bd4b48c88fe2 | -5.34028 | -44.99591 | 2025-10-18 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6dc9a65-4efb-36f9-a117-0374b5a2f780 | -3.5927 | -53.95948 | 2025-10-18 04:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 833e3af7-6e84-34fc-9016-9f4bb8a1707c | -9.08195 | -45.14334 | 2025-10-18 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46f5d77b-5a3c-378c-8ffc-bca61c9ddf08 | -6.21338 | -44.68052 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16bcc65b-c01d-3ef7-916c-4f3ac4fb619a | -5.59694 | -47.50097 | 2025-10-18 04:29:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b58f929f-41ad-373b-86ce-9f96b93e20a8 | -7.67452 | -44.6306 | 2025-10-18 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5314bab6-b64f-3a69-9198-0f66959eccea | -6.32198 | -44.31043 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c06e12f-5a02-3488-9ecf-fe4738e5c8cf | -10.98341 | -44.32357 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bdd80f94-a975-3bd7-bb50-6265f8cbed73 | -10.4871 | -43.41955 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68f8c279-109e-3aa0-ad61-883d7987e83a | -8.83154 | -44.90659 | 2025-10-18 04:29:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a99e1417-8d99-3be8-894e-6ae2823e564c | -6.19789 | -52.74239 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 757d836e-1454-373a-b112-08420725b896 | -6.41562 | -42.01615 | 2025-10-18 04:29:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c9f7ba88-9edc-3b4a-8711-5844e025f4c0 | -6.73595 | -43.81224 | 2025-10-18 04:29:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4096c77d-a791-3154-b0d6-3aeeaccaccce | -9.67584 | -44.5575 | 2025-10-18 04:29:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 87a2de96-6945-3bf0-8567-7964f1cdf690 | -5.3684 | -45.95289 | 2025-10-18 04:29:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8d50d91-48f5-314a-8412-19dd48d4bf83 | -5.91655 | -43.94102 | 2025-10-18 04:29:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29cb9c8f-f8a6-3b08-a704-f269453dc41f | -10.23987 | -44.06779 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 602b0022-641f-31dc-98a6-5f18cdc451d2 | -7.49138 | -47.02969 | 2025-10-18 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab4d43d6-8e65-31e0-a889-790a2e0ba352 | -10.24676 | -44.04505 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40e850f4-ca44-33d0-8e85-8788a8b1782a | -5.16849 | -48.60418 | 2025-10-18 04:29:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3876b8c6-bf69-3454-b390-5961d8a25e2e | -10.10737 | -44.55911 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 741d288f-a5dd-3f3a-baae-546daf57e8a2 | -8.7085 | -47.9231 | 2025-10-18 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb544749-9334-3f51-8cc3-ba4b953b1fe7 | -10.48205 | -43.42786 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 68381f90-19d1-34ff-80a9-2dee53984027 | -8.78694 | -47.93605 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c105910-30b1-3d8a-8880-e4352d4d6455 | -9.90873 | -47.67373 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f942f018-d9e7-3751-ad1c-0995b55746e0 | -5.70108 | -49.30241 | 2025-10-18 04:29:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7eff38b-c03c-3af9-9c05-f57c3ab89ffa | -7.14275 | -46.41093 | 2025-10-18 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6a437f8-1a14-3eb7-a3b4-84535eff31ed | -10.24612 | -44.04925 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49b7a72e-dd0a-32e9-85b8-de3f94b6f07c | -6.61213 | -43.61232 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d62e0f8c-2855-336f-a11d-40f18d458f14 | -7.58488 | -44.9894 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c82d6f0f-4e5a-3ad6-914e-7e92cca460e2 | -10.42563 | -45.02195 | 2025-10-18 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 851803a0-c616-31b8-a019-0a94225148aa | -10.24653 | -44.04748 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 012cac5e-d972-31d4-9f85-9d57e0aecacb | -5.86637 | -44.84626 | 2025-10-18 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9289858a-7829-36be-a0a7-250c0ae74aa9 | -7.36414 | -44.22701 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6cb67a89-5008-38f1-aa66-081a1724d557 | -3.95039 | -52.21709 | 2025-10-18 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcd1a94a-8deb-32a1-9005-f465db095006 | -8.44962 | -44.16881 | 2025-10-18 04:29:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a6a4aa1-9c82-3118-bb02-368a79d2817d | -5.01238 | -46.02063 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 38861b45-9a86-3a06-848b-6df06ecf087b | -10.68659 | -44.56016 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff8d95ec-bb60-3172-9a10-413fc0adcb6b | -6.98718 | -45.20216 | 2025-10-18 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94b62a72-ccea-3dc1-b9a3-dce21c39cc69 | -10.49708 | -43.43012 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 263f53c4-a383-34ff-8321-2f67c4a170e4 | -7.53444 | -43.93592 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a75c9ade-8e91-3890-800c-87ead2eb68d4 | -4.7833 | -45.3056 | 2025-10-18 04:29:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 058ca944-2243-3477-995c-0c0fa7daa8b8 | -10.49754 | -43.45329 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0dd3e544-258f-3c22-80c4-167c2e98c53f | -5.92578 | -45.44468 | 2025-10-18 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9765a3e1-7914-34d6-ac43-5329e6d92055 | -5.71297 | -46.51176 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e6a1871-d4e4-312c-a6c0-2ef8011704f3 | -10.14753 | -44.53254 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3c85c80c-f5de-3a2a-a3c1-0b9b38a096fb | -8.55155 | -50.08113 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 726b4178-8466-39d2-ba19-6a37f20a2cd7 | -6.3775 | -43.32566 | 2025-10-18 04:29:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f8d29fa4-e9fd-3e55-8e35-9066c03f18e8 | -5.92106 | -44.76256 | 2025-10-18 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 675773f1-908e-30fb-a77d-3c03416769e0 | -4.56666 | -48.39978 | 2025-10-18 04:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 984b106d-d160-3321-abf4-8f2c88be6efb | -6.30885 | -45.54348 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4580220-d9ef-31ef-9f69-26eddb648fe2 | -7.3523 | -43.85683 | 2025-10-18 04:29:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 13be6a9b-40a7-3de8-899e-31e84e86ee4b | -7.66454 | -44.6336 | 2025-10-18 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fd1ca6f-2aa4-320c-a451-4ab3313bdf49 | -5.10092 | -56.15536 | 2025-10-18 04:29:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19cf90aa-bc60-3220-acf0-bed1beb007ff | -4.71977 | -46.16234 | 2025-10-18 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cbc24d6-cfa7-34b5-9e9c-984ba1030dce | -3.81429 | -51.7002 | 2025-10-18 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1b48440-6b03-33ca-9111-fbc5bd58cd03 | -10.50637 | -43.44537 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README56.md)
