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
| f176f2b4-fa42-3d4b-a33c-79a10780cbc7 | -3.3957 | -47.5003 | 2025-07-18 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 8ec15e24-b23e-3bdb-837a-5375579d9fba | -4.301 | -48.1133 | 2025-07-18 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| ce99c41e-7017-33e6-bfcb-c3c46ae2e156 | -5.6569 | -43.6929 | 2025-07-18 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| bcc13c2a-f443-3bfc-9fcd-ae843264374d | -3.3772 | -47.4792 | 2025-07-18 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| b45f1883-95fb-335f-ad03-bba89dbe03c8 | -3.3958 | -47.4785 | 2025-07-18 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 155.5 |
| bca43396-b113-32fd-999a-6b99db40494f | -3.1198 | -47.0075 | 2025-07-18 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 8b2e34f9-f799-3986-a30d-102a51b97461 | -5.6379 | -43.7175 | 2025-07-18 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| a03b3971-4463-3750-b75b-8090cd8beffd | -11.5778 | -47.0941 | 2025-07-18 00:40:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| f32fa353-bd9f-3300-9261-b377ea8f71c3 | -8.1075 | -43.1411 | 2025-07-18 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| 24fb8df5-06a3-3ea0-8d40-5c6ad6d6310d | -21.0995 | -50.6145 | 2025-07-18 00:40:00 | GOES-19 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 123.5 |
| 5d4b1589-3593-3de4-9325-64431b2a3ecc | -11.5587 | -47.0966 | 2025-07-18 00:40:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 41d8a736-f9da-3502-b935-c0cd70376f74 | -11.7317 | -48.1849 | 2025-07-18 00:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 52a7d2cb-105a-38f5-bd6a-fe728f3ff5e6 | -8.0883 | -43.1667 | 2025-07-18 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 123.4 |
| 00561765-2f8b-3b0e-b94d-8081df5a05ab | -9.77 | -48.7623 | 2025-07-18 00:40:00 | GOES-19 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 1cdb8634-fa52-3a7b-8f2e-cdb4983c5c2f | -21.0989 | -50.6372 | 2025-07-18 00:40:00 | GOES-19 | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.4 |
| ab2693bc-e683-33cb-b5fc-4fb0c5923d95 | -21.0783 | -50.6415 | 2025-07-18 00:40:00 | GOES-19 | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 106.6 |
| 6580075d-55b0-365c-b90b-cda6512e3cb4 | -4.3196 | -48.1125 | 2025-07-18 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| ea95c978-9093-3cb5-a97d-002b80f1b01a | -8.0696 | -43.1452 | 2025-07-18 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 122.3 |
| ddef0e97-0ef1-339f-9599-765132a7185f | -11.5782 | -47.0717 | 2025-07-18 00:40:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 0464ac74-de3d-3c85-a776-03da666dceed | -5.6567 | -43.7161 | 2025-07-18 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 363.5 |
| b699c228-804d-3db8-ab08-f5ba53615021 | -20.9165 | -49.055 | 2025-07-18 00:46:00 | METOP-B | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5591de86-8753-3689-b775-a07d673b7704 | -8.0313 | -50.069199 | 2025-07-18 00:46:00 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19f6ccf5-0793-3e94-8511-bc090894a483 | -8.0279 | -50.055302 | 2025-07-18 00:46:00 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1554ac35-b965-37b4-b31e-ebb6a006ea76 | -11.5525 | -47.088299 | 2025-07-18 00:46:00 | METOP-B | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b89feee5-6570-3740-be21-6baa028d393a | -9.0231 | -61.202499 | 2025-07-18 00:46:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4e7f33a-4dd3-379a-a164-ad9d5b84139d | -7.4846 | -63.787899 | 2025-07-18 00:46:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c3942f9a-318a-3abe-8a32-abe0e7ba90fd | -23.0718 | -50.035301 | 2025-07-18 00:46:00 | METOP-B | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b2b08350-db0f-3e78-8605-a728764e30c9 | -16.4149 | -53.155499 | 2025-07-18 00:46:00 | METOP-B | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c9cb29d7-5d35-33f4-aa98-0b45f1ae4336 | -10.6817 | -56.5331 | 2025-07-18 00:46:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b7478b7b-8c2f-3011-beaa-9844ba760096 | -3.3756 | -47.482201 | 2025-07-18 00:46:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1eca4a60-dce3-3bde-85d5-ef54c7fb25ca | -11.8837 | -58.705502 | 2025-07-18 00:46:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a0408198-a778-311b-a10e-1b7e9e3fee25 | -3.3792 | -47.455002 | 2025-07-18 00:46:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85699fb3-6e40-3131-b4cd-efadf45ab1dc | -10.7069 | -49.4617 | 2025-07-18 00:46:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 162df83c-647e-303a-8a63-94abc51fd1f2 | -3.0968 | -47.0 | 2025-07-18 00:46:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a352b4f-0d1e-3883-9f90-062a2cf51844 | -11.5522 | -47.046799 | 2025-07-18 00:46:00 | METOP-B | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5b9ae4b2-f1a6-3e68-9092-7849379636c4 | -4.2896 | -48.098801 | 2025-07-18 00:46:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66bee97f-c9b8-38b7-9881-aa975c3f1211 | -9.4849 | -64.070503 | 2025-07-18 00:46:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a326fbaa-5e89-3396-9fe4-cce9674603c2 | -11.5622 | -47.085701 | 2025-07-18 00:46:00 | METOP-B | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5ea58488-579c-30e6-98e0-f02cd96c7bdc | -11.5572 | -47.066299 | 2025-07-18 00:46:00 | METOP-B | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c68fe164-6716-3367-a743-e1cf47967e17 | -5.9924 | -52.182899 | 2025-07-18 00:46:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9a3d6a8-05b5-307b-ba6e-89d4963879b5 | -18.656 | -55.711399 | 2025-07-18 00:46:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 89e75da4-0ebd-3ae9-a42d-51cf613291d0 | -11.7315 | -48.194 | 2025-07-18 00:46:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fbc29ef1-13fc-3bbc-8700-10743050915a | -18.6576 | -55.718899 | 2025-07-18 00:46:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 32ca59d7-fd68-3e48-b475-de8701868302 | -10.8046 | -49.2729 | 2025-07-18 00:46:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f22e1db5-aa0e-334e-87d8-df436bbd1c07 | -3.1064 | -46.9977 | 2025-07-18 00:46:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e6fc6d4-f955-3280-bca1-e90b329ed076 | -9.7541 | -48.738201 | 2025-07-18 00:46:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b53d6f2-11c9-3f53-8c7f-4d7b19f25824 | -9.7581 | -48.7542 | 2025-07-18 00:46:00 | METOP-B | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ee86209-940b-33eb-ad6b-93afc14894da | -21.039 | -55.979698 | 2025-07-18 00:46:00 | METOP-B | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 66c942de-c4b6-3b87-b745-666b409911f8 | -3.7237 | -53.984299 | 2025-07-18 00:46:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1fe7a0a-c1da-3ecd-9c5a-7f2497b74bbe | -21.081301 | -50.596001 | 2025-07-18 00:46:00 | METOP-B | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0ac5a7df-b598-3a63-ac3f-7325c8083492 | -8.8751 | -50.149899 | 2025-07-18 00:46:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4986f0b-4c9d-3c43-861a-51f7504d0c46 | -10.6832 | -56.540001 | 2025-07-18 00:46:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 76589abb-1d33-3120-820d-21fa3b0b2ce3 | -12.6537 | -47.077301 | 2025-07-18 00:46:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e149a822-6a39-34ff-8565-3379bdf0d931 | -9.8618 | -60.282001 | 2025-07-18 00:46:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1cdfc164-0d4b-3417-bb85-aa38ff65ea99 | -21.0756 | -50.6161 | 2025-07-18 00:46:00 | METOP-B | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b9664593-9444-3409-98d8-eda5c3921940 | -11.7233 | -48.161499 | 2025-07-18 00:46:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 346dd1f7-1525-3ff0-a5ba-ecf51e70ead9 | -3.3696 | -47.457298 | 2025-07-18 00:46:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1958b6b6-a3e8-3536-841b-e90b4bc9bae7 | -10.8081 | -49.287102 | 2025-07-18 00:46:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4ab9d275-afdc-373f-9d42-88af119fdefe | -10.0573 | -59.085499 | 2025-07-18 00:46:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b65c617-49ae-3323-8c8c-c6ee3e78d6a0 | -21.0854 | -50.613499 | 2025-07-18 00:46:00 | METOP-B | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ac3dca81-5155-3755-bd85-2680fc81bbf5 | -4.2992 | -48.0965 | 2025-07-18 00:46:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1c99e2a-9c05-3c33-8ee3-267a02b6cbdc | -24.0058 | -50.486099 | 2025-07-18 00:46:00 | METOP-B | CURIÚVA | PARANÁ | Brasil | 4107009 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 31c951cc-0cbe-399c-8464-82a4c13d3b9a | -11.5476 | -47.068901 | 2025-07-18 00:46:00 | METOP-B | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 68aa7d0a-7979-3b46-844f-a4f9b09cad81 | -21.071501 | -50.598598 | 2025-07-18 00:46:00 | METOP-B | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fc15c5f7-bd64-3cab-ae3d-da1bb9aa9656 | -9.7638 | -48.735699 | 2025-07-18 00:46:00 | METOP-B | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 037595a2-45bf-38e9-af47-f8b564d604f4 | -21.0735 | -50.607399 | 2025-07-18 00:46:00 | METOP-B | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0aae666e-4e1b-3c91-a1d0-1f68bdfaa71a | -5.9949 | -52.193699 | 2025-07-18 00:46:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e07f9fc1-7300-3c59-b33b-122a1d290698 | -3.0999 | -46.970501 | 2025-07-18 00:46:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 638596f6-6270-3cf8-bb57-fa92bb83f802 | -3.7335 | -53.981998 | 2025-07-18 00:46:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10dd0283-0ddb-3c4a-9951-eee43edeef8a | -20.906799 | -49.057701 | 2025-07-18 00:46:00 | METOP-B | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f075b13a-13be-3dc6-be1f-f81c3597c046 | -10.8178 | -49.284599 | 2025-07-18 00:46:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bce97c65-adfd-3456-bd27-cccd73e4cce8 | -8.041 | -50.066799 | 2025-07-18 00:46:00 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c30fd84a-b287-3a95-b094-69c50bf1f10f | -7.3445 | -49.572201 | 2025-07-18 00:46:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d569de45-c202-3e2d-9471-d86c1de271d3 | -7.352 | -49.602798 | 2025-07-18 00:46:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a30139d-3ca4-37e0-8845-c8e7ac6ea3ad | -7.3482 | -49.587502 | 2025-07-18 00:46:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfc490b7-e7bf-39a5-8fa8-fc5b1e2d338b | -9.8829 | -65.143303 | 2025-07-18 00:46:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e160d719-b296-3d78-af10-cc7862b74be3 | -18.868401 | -47.965099 | 2025-07-18 00:46:00 | METOP-B | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3705c1b7-9982-3ae1-a9d6-9055d1e50046 | -11.7274 | -48.177799 | 2025-07-18 00:46:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 95fd5744-8bbd-338b-8585-9b79a807dce6 | -23.069599 | -50.026402 | 2025-07-18 00:46:00 | METOP-B | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3b8fcce7-527a-3cdf-a3b2-3fa72a5a0a4d | -20.909401 | -49.068199 | 2025-07-18 00:46:00 | METOP-B | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ac982dac-0b48-362c-a18c-f6a2018aa761 | -10.7104 | -49.475601 | 2025-07-18 00:46:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6a3e8326-a830-3cd6-a8d0-1f902d12e01f | -9.488 | -64.0858 | 2025-07-18 00:46:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 02aea80f-1f96-328e-95de-b0a3737ea3ba | -3.3852 | -47.4799 | 2025-07-18 00:46:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21e4ba7a-b403-38af-93e1-d6068b563e33 | -20.904301 | -49.047298 | 2025-07-18 00:46:00 | METOP-B | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5a96ad04-13a6-3cba-ab3a-75c98f9c311f | -10.8143 | -49.270401 | 2025-07-18 00:46:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e615f10f-3a9f-3977-8456-f3ae01f47f1e | -7.3385 | -49.589901 | 2025-07-18 00:46:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ff7554c-be86-38bb-bd80-cae0628d00e3 | -21.0833 | -50.604801 | 2025-07-18 00:46:00 | METOP-B | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 62a9b6cd-6b47-30ef-ab43-b64629ba9a86 | -21.037399 | -55.971802 | 2025-07-18 00:46:00 | METOP-B | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ed23aa8b-610d-3e9f-ae34-5d9aff9ab75e | -11.7371 | -48.175301 | 2025-07-18 00:46:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9e418a94-5761-3bae-9920-05e33ade3c97 | -8.8718 | -50.1366 | 2025-07-18 00:46:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d73549a0-edcf-3b2f-ac5e-aaff91823367 | -18.8717 | -47.9781 | 2025-07-18 00:46:00 | METOP-B | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3a35a5a9-5c36-38cc-86a3-0b6e7d57767f | -4.294 | -48.074699 | 2025-07-18 00:46:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6595ab84-810b-36cc-8092-7e9e970cda05 | -9.8792 | -65.124901 | 2025-07-18 00:46:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1ce4dec7-3aa0-3bbf-a219-88b129b7b00b | -8.0347 | -50.083099 | 2025-07-18 00:46:00 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8be49a3f-17c9-3ae8-8be5-e83c218d7b8f | -3.3888 | -47.452702 | 2025-07-18 00:46:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08cd3ef6-818d-36b9-8e15-4c3a23a35032 | -20.9166 | -49.0607 | 2025-07-18 00:50:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 334.9 |
| 8823aaa2-0b16-3a3a-a6d8-18d0a1705ba0 | -11.7508 | -48.1825 | 2025-07-18 00:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 32538030-50ec-3bc3-826c-05b5a60b75eb | -11.7317 | -48.1849 | 2025-07-18 00:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 0276e195-5a3b-3334-a9a9-81f3ab65a27f | -9.77 | -48.7623 | 2025-07-18 00:50:00 | GOES-19 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 91add148-c837-329d-86dc-0556fd0de682 | -21.0995 | -50.6145 | 2025-07-18 00:50:00 | GOES-19 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 162.6 |


[Clique aqui para ver as próximas entradas](README3.md)
