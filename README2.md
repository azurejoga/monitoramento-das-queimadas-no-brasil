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
| 938967ac-52c0-3ea8-be8a-83e453827d0d | -1.6239 | -53.672 | 2025-11-10 00:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 6bc9114c-f0e6-3615-b2d0-45d03e34165c | -1.6422 | -53.6717 | 2025-11-10 00:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 87600e3c-0745-37ce-8722-154c694be7d8 | -4.2128 | -50.6273 | 2025-11-10 00:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| a1798ffa-6a7d-3856-80a7-7f104c762d19 | -3.6015 | -55.4698 | 2025-11-10 00:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 2d2f312d-ef0d-36df-b1a0-28bf4dbe52f0 | -4.1203 | -47.2951 | 2025-11-10 00:50:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 0fb67c38-744f-353b-9409-491d1276fa07 | -4.1204 | -47.2732 | 2025-11-10 00:50:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 106.0 |
| ad32aa86-02bf-34c7-a0f3-1fc3d715afaa | -19.7625 | -58.0438 | 2025-11-10 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.3 |
| f559ff91-bcd0-3ac4-aa53-021a4f277cb9 | -4.1943 | -50.6281 | 2025-11-10 00:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| d1817c8b-a30d-34db-a70a-b4e604bb5665 | -3.6975 | -50.1857 | 2025-11-10 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 4351652a-face-37fe-97df-f1214575d119 | -4.2128 | -50.6273 | 2025-11-10 01:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| e5942e6e-c33a-3abc-a3c5-f51efc83279a | -4.1942 | -50.649 | 2025-11-10 01:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| dd0121c1-73c8-37cb-9035-62f71f6f0a0a | -3.6975 | -50.1857 | 2025-11-10 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 59d0c452-b39c-3e70-b597-f63300b1fab3 | -3.6015 | -55.4698 | 2025-11-10 01:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 0a810f01-1055-3430-b9ea-fcf279f399d2 | -4.1943 | -50.6281 | 2025-11-10 01:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 758e7146-fff5-3dc6-8862-b18f9c5f3852 | -19.78934 | -58.04063 | 2025-11-10 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 86da0fe5-8ab3-39c5-971b-49eb4a0df22e | -18.51003 | -53.49439 | 2025-11-10 01:09:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 9806559a-ef50-364d-b19f-edf985774e9b | -18.47718 | -53.39859 | 2025-11-10 01:09:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 96b52950-9537-39d4-8252-d5a7a8600b6c | -19.67448 | -58.07372 | 2025-11-10 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.9 |
| e34ac63f-8f7a-37a7-8274-f34d80e52c91 | -20.52253 | -57.47435 | 2025-11-10 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 3a7a0d3c-f9f1-38e6-8455-3188dcc1f27e | -19.7983 | -58.03927 | 2025-11-10 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| f27a7495-8e9a-3912-a8fa-2021798de109 | -17.12613 | -55.74577 | 2025-11-10 01:09:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| cc9decdc-bbef-359d-a82b-d733fc13c231 | -18.48479 | -53.40494 | 2025-11-10 01:09:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 060f07eb-db65-3ccb-bd7b-081a2027f268 | -19.6732 | -58.06416 | 2025-11-10 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.9 |
| 16add14b-1711-3677-8ff6-6c535abfd648 | -19.68344 | -58.07236 | 2025-11-10 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.5 |
| f5f13cc0-e7cc-3fd9-8e79-7149fdf1615e | -19.80833 | -58.04115 | 2025-11-10 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 26edfdf7-09ab-331f-8f6d-d515e6c105ff | -16.58269 | -57.53994 | 2025-11-10 01:09:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| fb198bb4-5834-31da-8d98-224e1e233bfd | -18.19678 | -56.70446 | 2025-11-10 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 1f01e0d9-e221-36ae-8917-b0ec1223350c | -18.47436 | -53.40668 | 2025-11-10 01:09:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 22.2 |
| bda27b50-0a17-3d77-b2d1-2bcae71e0cd8 | -19.3285 | -54.32345 | 2025-11-10 01:09:00 | TERRA_M-M | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 987fe6d1-0f4a-379d-a2df-79fc4a38c869 | -18.21862 | -56.72984 | 2025-11-10 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 91d1ed2e-15c7-3258-afde-29671b3c48bf | -18.19543 | -56.69504 | 2025-11-10 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| a296afb7-7050-3be8-a296-92e793de7297 | -19.65657 | -58.07644 | 2025-11-10 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.5 |
| 946a42e7-c049-3ee2-90df-5ca4d3be6fed | -19.81856 | -58.04936 | 2025-11-10 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| b4c30983-11fb-30c0-9551-3af77a027d76 | -19.64762 | -58.0778 | 2025-11-10 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.9 |
| e131fea5-12b9-3431-b756-e78deeb2538e | -19.75993 | -58.0256 | 2025-11-10 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 1bbd3897-e28f-3e4a-85df-3e47259af1d8 | -18.47922 | -53.41154 | 2025-11-10 01:09:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 163f49ef-70be-3265-9a64-78727d657ea3 | -19.68216 | -58.0628 | 2025-11-10 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 209.2 |
| 88fc4b54-8691-3e7e-8788-eca477d77c12 | -19.7612 | -58.03516 | 2025-11-10 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.3 |
| 58420adf-6ee4-3afa-a526-fb7eb2ebf25b | -19.77015 | -58.03379 | 2025-11-10 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 5c9eb068-3a04-3016-9a2d-01bfc402cb5e | -4.2128 | -50.6273 | 2025-11-10 01:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 122.4 |
| e82bb6bb-c818-360b-a309-8b8a54aae4e4 | -4.1942 | -50.649 | 2025-11-10 01:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| ba16e94b-8068-32d0-bc01-33cc0f377c06 | -3.0042 | -48.0568 | 2025-11-10 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 5f73ba12-6681-3287-ae78-117f22e81d30 | -3.6015 | -55.4698 | 2025-11-10 01:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| a6beff4e-1d19-300b-8b23-9bc6389ca598 | -4.1943 | -50.6281 | 2025-11-10 01:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 04c6ad2f-c0cb-3a16-96cb-6f108c4fe645 | -3.6975 | -50.1857 | 2025-11-10 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 27c2492e-c57a-3dd7-ac32-7acbe646219d | -4.2127 | -50.6483 | 2025-11-10 01:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 6d05d9fb-527e-39aa-89c0-432227e9de13 | -4.727 | -42.9652 | 2025-11-10 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 7d7f1bf9-23b6-375d-a537-334fca7e5df4 | -10.61109 | -52.18765 | 2025-11-10 01:11:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 8e20b4d3-d71f-3f2d-ab6e-2cf6578e0fca | -10.61196 | -52.1719 | 2025-11-10 01:11:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 07322294-6aa9-33d0-a821-6d5232b42674 | -10.61542 | -52.19351 | 2025-11-10 01:11:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 4a075448-249c-36e5-b3cc-c73877d4245d | -6.57876 | -51.1188 | 2025-11-10 01:11:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 98ed6a19-28a0-3bdb-b9bc-0a147dd9011c | -6.79493 | -59.14267 | 2025-11-10 01:13:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8b05703b-e83e-332c-b965-b23c87c29f56 | -2.93445 | -57.78769 | 2025-11-10 01:13:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c99affb7-d537-35bb-b9a5-e0e20bb25079 | -3.60121 | -55.47741 | 2025-11-10 01:13:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| c129ee7e-1878-3f41-af49-cba1fc24c0a0 | -4.29179 | -60.95456 | 2025-11-10 01:13:00 | TERRA_M-M | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9a3fe5a4-ef9e-31a8-a4db-2a090e4a3a51 | -3.59793 | -55.47139 | 2025-11-10 01:13:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| a415f6d9-5354-39cc-8b7a-708a0de1a9d7 | -1.62767 | -53.67099 | 2025-11-10 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| a1d02b7c-e489-3c79-a73a-5d1335d70572 | -5.99916 | -57.82159 | 2025-11-10 01:13:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8fb687fd-d2df-35cb-82ee-139edb6db337 | -3.69973 | -50.18667 | 2025-11-10 01:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| b08c1e83-dafb-3ad8-98a2-7674e6b7906f | -3.58735 | -55.46298 | 2025-11-10 01:13:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 5aed261f-b641-3692-8471-57cfb6fa9c6c | -3.1656 | -60.67357 | 2025-11-10 01:13:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c4fa37a0-e5d1-311e-8790-07b0551781f6 | -4.2 | -50.60581 | 2025-11-10 01:13:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 142.0 |
| 1b76c94d-e1be-345a-b781-c7c8ceb23db7 | -4.20382 | -50.60003 | 2025-11-10 01:13:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| dd4a5980-0e68-3a31-9dbd-419a7376ad2a | -6.0006 | -57.83165 | 2025-11-10 01:13:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 3a8a0091-ab1c-3191-9e7a-9d151c3501f8 | -4.20983 | -50.63735 | 2025-11-10 01:13:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 257.0 |
| 7088c061-0aaa-3077-91a5-6cb379987920 | -4.48757 | -61.10518 | 2025-11-10 01:13:00 | TERRA_M-M | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ca3b7110-4303-32a8-8296-2d7a197ee1a5 | -3.23188 | -58.89936 | 2025-11-10 01:13:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e9fc9fef-209a-3d2b-b376-b3ec5d17ba1a | -4.20579 | -50.64336 | 2025-11-10 01:13:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 293.5 |
| 2c94807e-6da8-355b-a40e-9192bb4dc737 | -4.29301 | -60.96342 | 2025-11-10 01:13:00 | TERRA_M-M | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 22a45277-e76b-35c0-a653-45e5665421cf | -4.30065 | -60.95332 | 2025-11-10 01:13:00 | TERRA_M-M | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1b53600d-338d-3e70-8854-58cc0e426449 | -2.9427 | -57.77523 | 2025-11-10 01:13:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 33cdca74-a5aa-30bd-8965-69bc95e01c9d | -3.59557 | -55.4555 | 2025-11-10 01:13:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 1d2beb0d-e9c6-30da-9554-7c7c848769e5 | -2.93287 | -57.77665 | 2025-11-10 01:13:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 1bbd309a-5dbd-3e82-8b09-841c20b83df4 | -3.69907 | -50.19387 | 2025-11-10 01:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| d81201cb-aee9-32f9-8eca-eab15e763b1e | -3.58961 | -55.47886 | 2025-11-10 01:13:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 0a92edb2-d1d7-3957-a367-29054e314e42 | -3.59897 | -55.46148 | 2025-11-10 01:13:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 4cd9374f-9571-32bc-bbd0-65778b82d38e | -19.6404 | -58.066101 | 2025-11-10 01:14:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 54bc8efd-8218-31e0-b73e-08fb27aa7e03 | -19.6427 | -58.0755 | 2025-11-10 01:14:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| afa1ce92-26c6-3cde-aa6e-0d50eb25ad40 | -19.7549 | -58.0252 | 2025-11-10 01:14:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 04a8f9b6-9f97-3014-8590-91d65018d108 | -19.677099 | -58.046299 | 2025-11-10 01:14:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f3e2dee4-f034-35b0-bbcf-c81d2c42779b | -19.7983 | -58.033401 | 2025-11-10 01:14:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9e352060-1a89-37da-89a0-3af484f6c24c | -19.764601 | -58.022598 | 2025-11-10 01:14:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 944f54f9-7d72-3d35-a488-d95247b2c215 | -19.667299 | -58.048901 | 2025-11-10 01:14:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 55a5975e-bfb3-3bab-b3be-c42f7aa6c3f9 | -17.115 | -55.730202 | 2025-11-10 01:14:00 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e8801612-2d8d-3eaf-81dc-fc7fe81c634b | -19.6306 | -58.068699 | 2025-11-10 01:14:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 654c7797-9bcc-3dac-98fe-c4802ef45833 | -19.7526 | -58.015701 | 2025-11-10 01:14:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a0ef260d-84e0-3b20-88ac-abd3e41cd486 | -19.786301 | -58.0266 | 2025-11-10 01:14:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a84f12b6-0592-38cf-8ad3-fbb19753e32e | -19.6793 | -58.055599 | 2025-11-10 01:14:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8d37e5d7-fe81-3d37-b388-2ed0af6288f3 | -19.6695 | -58.058201 | 2025-11-10 01:14:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d5ec1baf-3ce8-3cc3-8027-118186241891 | -3.581 | -55.457298 | 2025-11-10 01:16:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1cf2f56-e259-3f78-a5a5-940cc10f5311 | -3.5751 | -55.433102 | 2025-11-10 01:16:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0bd1c7a-5a49-3114-852e-996a4d51a750 | -8.0142 | -41.6024 | 2025-11-10 01:20:00 | GOES-19 | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 61.0 |
| 229db254-aed8-3f3c-8f7d-a4cbd42e1326 | -4.2127 | -50.6483 | 2025-11-10 01:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 5c60a49c-5c2d-3bcb-801f-594f2b5a07a7 | -3.0042 | -48.0568 | 2025-11-10 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| bdf0f655-e442-373f-853d-fba58db2cd8f | -4.1943 | -50.6281 | 2025-11-10 01:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 186.5 |
| 0de39f87-1c76-346e-b023-ba8b12529886 | -19.6821 | -58.0543 | 2025-11-10 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.8 |
| 9f3439ac-2b42-3674-99e3-a002c27350c9 | -4.2129 | -50.6064 | 2025-11-10 01:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| c1dd6f23-4b33-3a19-8993-e62e16c80a6b | -4.2128 | -50.6273 | 2025-11-10 01:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 275.9 |
| d3bba5b4-8071-3a35-b1b3-cfb883e2fe16 | -19.6818 | -58.0751 | 2025-11-10 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.4 |
| fceb897c-fa4c-319d-9e96-88d6ae660b47 | -3.6975 | -50.1857 | 2025-11-10 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |


[Clique aqui para ver as próximas entradas](README3.md)
