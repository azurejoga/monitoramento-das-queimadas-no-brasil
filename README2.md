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
| 8cb6143b-db9c-3de1-97b5-46a77119540f | -6.29472 | -44.23906 | 2025-06-17 00:22:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| fbc5bb65-f330-3101-ab5e-4fcb2af75560 | -9.20014 | -49.70478 | 2025-06-17 00:22:00 | TERRA_M-M | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 4a81e7a4-7081-3abb-96a3-be9da1dc5f7c | -8.78016 | -46.62508 | 2025-06-17 00:22:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2fa6a819-5b62-3c20-bb21-e526dc2478b6 | -7.24912 | -43.08835 | 2025-06-17 00:22:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| bc2f4067-4432-3677-82b5-c089ca2e15cb | -8.96705 | -47.97558 | 2025-06-17 00:22:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 46c43207-03f4-3ad4-87d2-2de8fbf9c6ed | -4.812 | -46.81841 | 2025-06-17 00:22:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9a62688e-f46b-3a54-ab3d-f645d7f767fe | -5.56984 | -45.20819 | 2025-06-17 00:22:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8fe8c43d-bdca-3752-b6bb-822dc325d5f5 | -5.29165 | -44.72369 | 2025-06-17 00:22:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9661f42c-2b24-3078-a596-0be4c461f0c6 | -6.84866 | -47.84337 | 2025-06-17 00:22:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 5ec0e7b4-a112-3045-9503-ae760c394437 | -8.70263 | -46.9678 | 2025-06-17 00:22:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4a4c0c8a-8418-3fa3-b517-217623024566 | -7.54444 | -45.63814 | 2025-06-17 00:22:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 995f5bef-55ba-38d8-9c39-cb1575836086 | -7.54575 | -45.64781 | 2025-06-17 00:22:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 91ed063b-c8b6-32b6-a0ac-6dc748be5ee6 | -7.46156 | -45.49958 | 2025-06-17 00:22:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 238dfa21-2bc9-301e-8ea4-309290f96cb9 | -6.07186 | -46.11266 | 2025-06-17 00:22:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 3f33cc63-08ee-3ccb-9266-93d36c3fe2be | -6.94022 | -47.76226 | 2025-06-17 00:22:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5119e525-b3ec-317f-b7fe-ce1f509027fc | -6.29946 | -47.01348 | 2025-06-17 00:22:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8d29b05f-d120-3ac2-adc3-6c9e979cec38 | -9.20145 | -49.69817 | 2025-06-17 00:22:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 8e8ed610-bafb-3289-b329-d96763a0c17b | -7.281 | -50.01725 | 2025-06-17 00:22:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 81b26810-d2a9-3c02-91a4-31921191084c | -6.23102 | -44.65663 | 2025-06-17 00:22:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 749e8d16-3d9c-3284-aaa9-fca974957eda | -6.15374 | -48.06384 | 2025-06-17 00:22:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b96ada69-15e1-350b-a797-293575836962 | -2.44942 | -47.50986 | 2025-06-17 00:22:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 90dea849-6049-3611-b25a-3f522ec4461a | -6.29351 | -44.23024 | 2025-06-17 00:22:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| ba4dc12d-ba40-3302-a396-7fe9d53aa848 | -6.29802 | -47.00247 | 2025-06-17 00:22:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| f441d0e9-174e-3f78-9e21-8f83dcd82cde | -8.54559 | -48.26247 | 2025-06-17 00:22:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0ac787fe-4d53-3991-a155-e0ff2313ad43 | -8.07373 | -43.11591 | 2025-06-17 00:22:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.8 |
| 040e6719-aedd-3a87-8f88-501e20d1b3c0 | -7.2504 | -43.09736 | 2025-06-17 00:22:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 8578556f-497d-3408-9071-b2f0d22b1a18 | -9.88501 | -47.80945 | 2025-06-17 00:22:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| e849fe2a-9d8d-343c-8ce5-f984a298adb0 | -6.12749 | -42.52482 | 2025-06-17 00:22:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| b566876e-aa78-3f17-950d-4884c3336fe5 | -5.07004 | -43.72724 | 2025-06-17 00:22:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| b30e4265-07c2-3767-9d63-f006e4e59f42 | -5.46715 | -45.33021 | 2025-06-17 00:22:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 59498518-1867-30a7-91a9-675366dd94da | -6.29634 | -47.00911 | 2025-06-17 00:22:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 24d50a4f-3a20-3e92-9826-90a06bc6acc6 | -8.34078 | -48.44864 | 2025-06-17 00:22:00 | TERRA_M-M | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| e892faff-3a3f-37f2-8d84-bd19f820ea46 | -7.27203 | -44.64579 | 2025-06-17 00:22:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8278abf0-7c4e-309c-9ebf-7f1bdb454831 | -8.61225 | -45.02377 | 2025-06-17 00:22:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 5386beae-5907-32b2-9316-6c6ca0ec79a2 | -9.67522 | -48.77542 | 2025-06-17 00:22:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 9f478fa6-8c68-3b54-864a-d4c9c1caf0b5 | -5.29043 | -44.71486 | 2025-06-17 00:22:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| b156de73-1f01-38a2-af34-98656a776a56 | -3.76709 | -41.60725 | 2025-06-17 00:22:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| d00dd3aa-aaa5-3d47-b6c4-6e5b9c4c84c6 | -4.55307 | -48.01818 | 2025-06-17 00:22:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 94a8ac53-5d87-3702-bdd8-5a32ea9c00dd | -7.19068 | -43.6004 | 2025-06-17 00:22:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cb4cc77e-0f23-3f7f-867d-921e7422eba5 | -7.27081 | -44.63682 | 2025-06-17 00:22:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 11217330-7c05-39f5-a446-55eda9f9f70f | -5.62518 | -43.99984 | 2025-06-17 00:22:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 93a03f58-7e12-3084-94ee-171bb45735a3 | -7.20239 | -45.35626 | 2025-06-17 00:22:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 4d4355e2-1dcf-3185-bb4e-7a0fa6589f96 | -10.9353 | -56.8522 | 2025-06-17 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 7f76f8ab-b1e0-329d-a167-ca8dda6255be | -11.1571 | -53.9206 | 2025-06-17 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 3f664cfe-2b03-39a5-8696-6f9cf2159bf2 | -10.3014 | -60.5421 | 2025-06-17 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 32.9 |
| d2844f64-898a-3aff-99e0-1c77b8e61db1 | -13.272 | -49.8859 | 2025-06-17 00:30:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| b9301d32-bf6b-35ef-8406-359df1992b14 | -10.9355 | -56.8322 | 2025-06-17 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 12d9b70c-429d-32d0-9d8b-021f5bf10879 | -10.1384 | -46.7374 | 2025-06-17 00:30:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 1eff69f0-45fe-3161-8b3a-e9997e0107bd | -10.9167 | -56.8336 | 2025-06-17 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 1b17c1ae-e89e-37c5-b900-ee564e302ff1 | -11.1379 | -53.9429 | 2025-06-17 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 07d9f294-7586-3024-a9fe-aa79bbf5d982 | -11.1568 | -53.9411 | 2025-06-17 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 5a7f39f9-eeea-31be-a9fe-bdadbc3f66f5 | -10.2827 | -60.5432 | 2025-06-17 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 7d7e85ad-4b6d-37ae-a5af-b28ab3498ecd | -11.1382 | -53.9223 | 2025-06-17 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 46950537-db19-3a90-9684-57f713db764f | -11.1401 | -53.952599 | 2025-06-17 00:38:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 29c1eccd-2d24-30f2-8d24-cb76619589f4 | -12.3428 | -49.299999 | 2025-06-17 00:38:00 | METOP-C | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f61b6ecb-c016-3115-9217-6ff569ff0070 | -10.9335 | -56.842098 | 2025-06-17 00:38:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5aac1ddd-373e-3749-bbdc-3300cc75cbb7 | -6.0737 | -46.114201 | 2025-06-17 00:38:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94495733-842f-3145-92dc-61d21ba7616d | -10.9874 | -45.101299 | 2025-06-17 00:38:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5ef45506-14a2-3f80-b25b-8f4f0d892118 | -13.2709 | -49.890099 | 2025-06-17 00:38:00 | METOP-C | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ae1fb074-7614-3052-9e70-e9242f956a7b | -8.5504 | -48.262501 | 2025-06-17 00:38:00 | METOP-C | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0656196-577a-33d1-bfea-a6dba0cebbe5 | -12.2107 | -49.636501 | 2025-06-17 00:38:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a17d7da9-854b-3cb7-9e2f-ada5cbbe4164 | -6.291 | -47.003201 | 2025-06-17 00:38:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5fb85415-a148-34e0-a580-88cdecae17fd | -10.9197 | -56.823299 | 2025-06-17 00:38:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c287b746-f60e-3232-a163-5ac440511483 | -8.6076 | -48.0611 | 2025-06-17 00:38:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08d5d915-0846-3594-8327-c91db6839eab | -10.7524 | -48.571999 | 2025-06-17 00:38:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64f609f3-185d-38a4-a2c6-1af88f27a937 | -13.2771 | -49.871399 | 2025-06-17 00:38:00 | METOP-C | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 36ae52ce-c3ad-357d-b2f6-2383de3b304e | -6.8449 | -47.837898 | 2025-06-17 00:38:00 | METOP-C | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83a54596-252d-3f2d-bfde-b8a869a92936 | -9.2031 | -49.698002 | 2025-06-17 00:38:00 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 967c3a1e-d11c-3f78-9cb6-5523a088a888 | -7.4578 | -45.503899 | 2025-06-17 00:38:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| edc4580e-b710-3e70-81cb-eadc7ea1b323 | -4.2482 | -47.580799 | 2025-06-17 00:38:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2f03f39-c2eb-348e-9e13-cb450789def4 | -10.9856 | -45.093601 | 2025-06-17 00:38:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b1effa25-f4f3-3b05-8d64-204147838169 | -8.6135 | -45.0201 | 2025-06-17 00:38:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b93fccc6-3da5-3316-a9f8-623c12ddeaf3 | -8.9589 | -47.974098 | 2025-06-17 00:38:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f874afde-c946-3fa8-943e-584e38649f1c | -10.7442 | -48.581299 | 2025-06-17 00:38:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 26fc4750-501c-3e40-809e-ee3e485d5d3a | -11.0372 | -44.6567 | 2025-06-17 00:38:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2cdeabc9-6fd4-3da8-8bdc-ec209b63fa48 | -8.0718 | -43.101299 | 2025-06-17 00:38:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d4ed6443-4172-3006-90a9-1c4fbc7863fa | -13.3922 | -48.4618 | 2025-06-17 00:38:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a722afdc-8c55-3ab5-9113-57d4640dfa9e | -9.8797 | -47.8083 | 2025-06-17 00:38:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d17ea557-2904-3fc5-adf5-ef0c0a6e1ded | -10.366 | -47.003201 | 2025-06-17 00:38:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f49d0a1e-2b7b-3b31-b135-3fc8802bc0e0 | -7.5537 | -45.648102 | 2025-06-17 00:38:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 895879bd-02f1-3b5d-a6fe-9679627920e8 | -14.0295 | -55.126701 | 2025-06-17 00:38:00 | METOP-C | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fef3ea7e-f9d0-3dae-b198-3b302b29b164 | -9.3301 | -47.839001 | 2025-06-17 00:38:00 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8aebe4a6-a467-374c-bc18-0e9de1163fa7 | -10.9238 | -56.844002 | 2025-06-17 00:38:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ecdac0d7-ed00-341f-8873-faeb52412754 | -7.55 | -45.632401 | 2025-06-17 00:38:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eda184c9-6e53-3a81-802a-d602bd031ab8 | -11.1472 | -53.937401 | 2025-06-17 00:38:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f290493-8128-3163-8b51-0b2f7709f1f1 | -5.2928 | -44.724499 | 2025-06-17 00:38:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8bd639ce-2753-3ba5-b493-14f9f083dc4d | -10.9598 | -45.116001 | 2025-06-17 00:38:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9d2f4cad-8818-3c13-a02b-36cfd5578732 | -8.3969 | -47.455399 | 2025-06-17 00:38:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bf68fc40-8cbc-3cf3-bbec-f1e11cb83ea1 | -7.2721 | -44.630699 | 2025-06-17 00:38:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e1e8247e-5e22-3c36-964d-975e4855f97e | -13.2673 | -49.8736 | 2025-06-17 00:38:00 | METOP-C | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 497f732a-fe42-34af-a178-a117636ac2cb | -13.2691 | -49.881901 | 2025-06-17 00:38:00 | METOP-C | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bf65808b-ca4e-32a5-85db-524a4b18126a | -10.7291 | -44.882198 | 2025-06-17 00:38:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2e38e9fc-63f4-3ab1-a7f5-37278c583a00 | -11.3969 | -47.637199 | 2025-06-17 00:38:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89057c18-53ac-313d-8015-f9ba62f06fd8 | -10.8793 | -54.316399 | 2025-06-17 00:38:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5b3a598-c9ff-39ca-bd8f-09c499b0d8e9 | -7.5519 | -45.640202 | 2025-06-17 00:38:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e6e2e33-3938-3c52-9b83-b143a120a8f0 | -8.0841 | -43.109402 | 2025-06-17 00:38:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6d710888-9b61-395e-bf48-a2eb785ccab4 | -10.1384 | -46.730999 | 2025-06-17 00:38:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3acbf5c-491d-315d-a0d8-caf26b745e85 | -7.114 | -47.842098 | 2025-06-17 00:38:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 435197b4-eb25-3037-8731-3c8a95cbad08 | -4.8157 | -46.825199 | 2025-06-17 00:38:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0511f91a-90b7-37a7-995c-f5cafd5929cb | -8.9702 | -47.978802 | 2025-06-17 00:38:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
