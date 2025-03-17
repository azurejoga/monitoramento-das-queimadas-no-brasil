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
| b0cbc7f2-42bd-3990-83c2-e6c0bea45ab9 | -22.53954 | -48.81403 | 2025-03-17 04:38:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cc256ef-570d-3388-a12d-936f3594e1b7 | -28.71969 | -52.60799 | 2025-03-17 04:38:00 | NOAA-21 | SOLEDADE | RIO GRANDE DO SUL | Brasil | 4320800 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 582f9bde-57af-335f-873a-15369e879e82 | -23.98292 | -48.91639 | 2025-03-17 04:38:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 203aa05b-8c70-392f-8b3e-1bf7b2939325 | -28.58557 | -49.43982 | 2025-03-17 04:38:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ca4ba7ac-4865-32cd-bbd6-67f60a4ddce1 | -27.33785 | -50.57352 | 2025-03-17 04:38:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 4e466375-a0ae-3580-8edd-8d507cdf4c2a | -21.23099 | -56.25905 | 2025-03-17 04:38:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a48b03ef-a022-3212-853b-9d4a2d9ae97c | -28.71637 | -52.60734 | 2025-03-17 04:38:00 | NOAA-21 | SOLEDADE | RIO GRANDE DO SUL | Brasil | 4320800 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e5468c46-9cf1-35ec-8cb9-0e346cbebfda | -27.33727 | -50.57774 | 2025-03-17 04:38:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| c4cd8c5b-63b1-3bde-8fd4-e23786690337 | -29.25175 | -56.55547 | 2025-03-17 04:40:00 | NOAA-21 | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 8c416d6b-dccb-3f44-8d04-89181f3ef75d | -29.25093 | -56.55998 | 2025-03-17 04:40:00 | NOAA-21 | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| ca2d02cf-f88e-3d1c-abe7-666606a9e00f | -8.10625 | -43.1343 | 2025-03-17 04:44:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 48.5 |
| f72b4bf1-a94d-3b1e-a650-11d31dbc4f93 | -8.11209 | -43.13276 | 2025-03-17 04:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 193760cd-a2f8-3852-b19e-3912b0b861f9 | -8.10653 | -43.12701 | 2025-03-17 04:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8a2acd27-5722-3325-8a3d-fe5e72580b4c | -8.11272 | -43.12793 | 2025-03-17 04:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 026e2c06-df0b-38a6-b87d-7478678e3146 | -8.1059 | -43.13187 | 2025-03-17 04:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 543ddcea-436d-3211-a28f-90e465b7dea5 | -8.11147 | -43.13759 | 2025-03-17 04:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 6e5a7688-4fce-32c8-9c5b-9d55f78f5398 | -8.10527 | -43.1367 | 2025-03-17 04:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 833b889c-5fec-3c65-9788-f945e47889c9 | -13.26851 | -53.88985 | 2025-03-17 04:59:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18e14a50-537c-3b07-a5c4-208e8552bdaf | -14.53805 | -45.52555 | 2025-03-17 04:59:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd7172b5-8bde-3a8d-a7e3-c042cf32437a | -14.53777 | -45.52341 | 2025-03-17 04:59:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 783fe325-4967-3dba-915e-cff5c656d2a2 | -13.26794 | -53.89361 | 2025-03-17 04:59:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cce53fe3-c804-35d4-a281-e6cd645c5b3a | -14.53362 | -45.51237 | 2025-03-17 04:59:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83849a1b-4acd-314f-bf68-03a13f8166af | -14.53317 | -45.51654 | 2025-03-17 04:59:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f5c890b-1e82-379c-a3fa-3a2296999e83 | -14.53272 | -45.5207 | 2025-03-17 04:59:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e5964a7-49ef-3624-9e47-e60ce862b20f | -14.5385 | -45.52139 | 2025-03-17 04:59:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4244e588-96a2-3e84-9c35-c74ed28d0274 | -14.53198 | -45.52274 | 2025-03-17 04:59:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1faa7ce-a65f-3cff-ad93-5af4d55dd661 | -14.53247 | -45.51858 | 2025-03-17 04:59:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0af8fc1-ce98-3158-a2cd-ad67cced3737 | -14.53826 | -45.51926 | 2025-03-17 04:59:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b75f4bc-4108-34a2-b301-f7b04e257a68 | -14.53295 | -45.51441 | 2025-03-17 04:59:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d79b810b-26f7-3e17-bd19-2acbe6e01123 | -14.53896 | -45.51723 | 2025-03-17 04:59:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3712ed0-625b-3c16-b251-52b15f03d781 | -21.23072 | -56.26088 | 2025-03-17 05:01:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f689fc92-599f-3408-9caa-cfd76414aa5b | -22.54185 | -48.81258 | 2025-03-17 05:01:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc5e3bde-1f57-3d2b-8395-81b8a7bd07ca | -22.53769 | -48.81126 | 2025-03-17 05:01:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7bc2585-2a4d-3e61-9358-dddb8758b166 | -27.33901 | -50.57354 | 2025-03-17 05:04:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a5a04351-955c-33fb-a16c-2a591412e9d0 | -29.2501 | -56.55757 | 2025-03-17 05:04:00 | NPP-375D | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| b1bf4f5b-5ff9-3f8a-9092-72a542311c03 | -27.33411 | -50.57292 | 2025-03-17 05:04:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0b4f480f-5512-3685-9b62-3d718d16b655 | -28.58676 | -49.44264 | 2025-03-17 05:04:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2b2b6315-1489-3954-9b99-b6e0bfba2fa1 | -27.33639 | -50.57716 | 2025-03-17 05:04:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 01edac5a-c9fe-35de-804d-8438839b04c4 | -13.2672 | -53.88961 | 2025-03-17 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b31b3221-2838-364e-b484-081a48705462 | -29.25228 | -56.56009 | 2025-03-17 05:27:00 | NOAA-20 | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| a42fc2a9-be1a-3e87-b976-14da73f3715f | -29.24748 | -56.55613 | 2025-03-17 05:27:00 | NOAA-20 | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| bce0f8bd-0063-3f18-9c56-47812017a6db | -18.1205 | -44.1802 | 2025-03-17 10:10:00 | GOES-16 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 21b48abc-ebca-3287-8dba-79deadf8a8ab | -12.823 | -44.9975 | 2025-03-17 12:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| cc2d9cf1-e19d-35dc-8525-faa9797e3eb9 | -12.823 | -44.9975 | 2025-03-17 12:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 467a49e2-c26c-3fa5-abf1-ae8a68f55b50 | -11.70739 | -48.40557 | 2025-03-17 12:44:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5410d963-f090-3145-9888-24867c0410bc | -11.74549 | -45.43512 | 2025-03-17 12:44:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 9088b15f-93d4-3e44-b667-96b114e9d6b1 | -11.70577 | -45.46441 | 2025-03-17 12:44:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 3d192e78-97ff-3c1e-be3d-1abfea58af06 | -12.61184 | -48.37103 | 2025-03-17 12:46:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 468bda56-873b-3ac9-91de-e5c324eb54e9 | -12.85138 | -43.83008 | 2025-03-17 12:46:00 | TERRA_M-T | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 93ee22a0-271c-3c84-9b52-2b601f59ebde | -12.90212 | -45.05103 | 2025-03-17 12:46:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| b5841bdb-cd0c-305f-acb4-d0a376704c06 | -14.11566 | -45.69381 | 2025-03-17 12:46:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 0ac277b1-f370-31d2-876e-0dd42290fa96 | -12.83167 | -45.00358 | 2025-03-17 12:46:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 89ecf310-a891-3540-8725-90df7a8018df | -13.68646 | -43.01211 | 2025-03-17 12:46:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 42.4 |
| 29b21184-ef60-32f8-8b55-01ae10fdf876 | -13.0111 | -44.46074 | 2025-03-17 12:46:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 160a987a-51e5-307b-b39d-741697b57497 | -12.90443 | -45.03201 | 2025-03-17 12:46:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 6706a2d6-695e-388d-b833-65de035cbf74 | -13.13269 | -55.10609 | 2025-03-17 12:46:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5f6bf084-a5d2-38b2-a708-0e4d8e3f428b | -16.37591 | -45.09745 | 2025-03-17 12:46:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 10ca91c0-7133-3acf-9bed-a1605f270082 | -12.82767 | -45.01657 | 2025-03-17 12:46:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| fdbee0bb-a9c1-3036-8ccf-1c0f69b4c3f4 | -13.68938 | -42.98404 | 2025-03-17 12:46:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 52.4 |
| a1f9a047-419a-3311-8085-bf0d188d8daa | -13.69011 | -42.97766 | 2025-03-17 12:46:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 0edbb128-8260-380c-a357-4b0e1407d338 | -12.82996 | -44.99788 | 2025-03-17 12:46:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| d8b04ed2-68c2-33f9-93ea-b2f72795f2f9 | -16.37324 | -45.10374 | 2025-03-17 12:46:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| faf60e8f-084c-34c2-a907-1acadf45b64f | -13.68704 | -43.00516 | 2025-03-17 12:46:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 63.6 |
| 669e82ad-4bd1-3220-83ad-cf528f5b3ac7 | -26.86596 | -50.67429 | 2025-03-17 12:49:00 | TERRA_M-T | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 2748ab28-c5d2-3e32-a3c8-a3f5d26c1ff9 | -12.823 | -44.9975 | 2025-03-17 12:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 3f982d06-4a81-3765-80f9-5265bc345e90 | -12.8462 | -43.8223 | 2025-03-17 12:50:00 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| fa6f99df-16de-3891-96eb-3fbaf64c8772 | -12.823 | -44.9975 | 2025-03-17 13:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 83f90cad-11a4-3081-9f75-9e7b358dfdd0 | -12.823 | -44.9975 | 2025-03-17 13:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |
| ca92586e-e307-35b9-a25e-3ca27a175d68 | -12.8424 | -44.9944 | 2025-03-17 13:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 5ec4b032-c49d-3c2f-b3b6-67f7033b351c | -12.823 | -44.9975 | 2025-03-17 13:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 153.0 |
| da11ec27-84f4-3136-b991-028b10090823 | -12.823 | -44.9975 | 2025-03-17 13:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 4bf8b839-17a6-3bf1-9a45-dfcad0a1efe6 | -12.823 | -44.9975 | 2025-03-17 13:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 10287072-65dc-37ce-8013-4b63720e4a8f | -12.899 | -45.0549 | 2025-03-17 13:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 206.5 |
| 001ea5f6-963d-3618-b950-60860db03c1f | -12.8995 | -45.0316 | 2025-03-17 13:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 212.1 |
| 5653842a-67e1-39ef-9420-50305472fac9 | -12.823 | -44.9975 | 2025-03-17 13:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 159.7 |
| dbac2bc3-e2e2-3c19-bafc-328284c11b52 | -12.8995 | -45.0316 | 2025-03-17 14:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 239.0 |
| 91b1601e-37d0-34c0-865e-6cb8ac5f8613 | -12.823 | -44.9975 | 2025-03-17 14:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 61f6941d-9762-3fc2-b7b5-3aeb3a97947d | -12.899 | -45.0549 | 2025-03-17 14:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 225.9 |
| 49f21763-d0c7-3266-b75d-4ad7255aca23 | -12.8995 | -45.0316 | 2025-03-17 14:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 288.3 |
| ae368e46-fd7a-34ec-af37-7772e683b1f9 | -13.6959 | -43.0028 | 2025-03-17 14:10:00 | GOES-16 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 88.4 |
| 60f334e5-f484-3b4e-8cae-05d3d1839aa4 | -12.823 | -44.9975 | 2025-03-17 14:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 152.8 |
| da5cb0ad-8dcb-33cc-a018-b0405d15d822 | -12.8995 | -45.0316 | 2025-03-17 14:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 300.8 |
| bf68e609-2863-3d90-857f-53e2fddc9175 | -12.823 | -44.9975 | 2025-03-17 14:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 7482fce1-6851-3afd-a0b9-c624ffb0226f | -12.8424 | -44.9944 | 2025-03-17 14:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 127.4 |
| cc91c085-2ea6-3c43-a156-58685e686a52 | -12.823 | -44.9975 | 2025-03-17 14:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 4343b117-0008-3c05-ac0a-1d0be63dde58 | -12.8995 | -45.0316 | 2025-03-17 14:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 292.4 |


