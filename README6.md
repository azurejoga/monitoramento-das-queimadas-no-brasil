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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d770982f-55df-39c9-b772-b551a44b7e6a | -6.8515 | -47.91816 | 2026-06-21 04:42:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| faa39ab7-5c7f-3a78-9b9f-6eba243eac71 | -4.45875 | -48.0234 | 2026-06-21 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3958b79f-e065-31da-b3fa-9857c026b1bc | -5.81392 | -45.07019 | 2026-06-21 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 094c9a2a-a3a6-3875-a728-c044e37cb3f4 | -3.98983 | -47.93626 | 2026-06-21 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 383d3b1c-47f6-3c2d-818f-01cd43400226 | -6.50448 | -42.21411 | 2026-06-21 04:42:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| df04ee24-9676-3a61-ae86-a2bc7f73ea91 | -5.81632 | -45.08022 | 2026-06-21 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 80097f2f-0cb5-3e47-bc5e-22e7069d0974 | -6.83735 | -47.91978 | 2026-06-21 04:42:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e27c444d-8831-3bd8-8fe9-543636a9360d | -6.33342 | -48.41224 | 2026-06-21 04:42:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a255645-c9b8-3170-8a8f-b36e4b3be906 | -5.81778 | -45.07069 | 2026-06-21 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9336c95-c5fa-3211-899b-694f093d66a6 | -4.45541 | -48.02288 | 2026-06-21 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c54c73d7-0af7-3dc1-82dd-11d99f5e4f57 | -6.8481 | -47.91766 | 2026-06-21 04:42:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f1447a49-5fdb-30b2-9dbb-9617e38811df | -6.96045 | -42.06557 | 2026-06-21 04:42:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d6da5bf7-49b0-3360-bf91-83cfa18263af | -5.82018 | -45.08072 | 2026-06-21 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f17652d-835b-3b30-af02-b55a509b83a4 | -6.8447 | -47.91715 | 2026-06-21 04:42:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11a69bc7-fdd8-3490-a99b-e3e0adabe0db | -4.35273 | -47.76486 | 2026-06-21 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 446a4a34-e280-30ab-8dde-5462d5966cf6 | -5.81927 | -45.07306 | 2026-06-21 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0a88a67d-3a22-30ff-a32f-73ba184bf26f | -4.4305 | -47.7294 | 2026-06-21 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb8b8aa9-e95d-361a-aeaf-a98b6b0c850a | -5.95892 | -43.48869 | 2026-06-21 04:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8951472-6a0d-33bc-ba81-dfdd5750cc0f | -5.81788 | -45.08259 | 2026-06-21 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 75c1a62b-28b4-3dc1-90cb-997fee89c3c7 | -6.84866 | -47.91401 | 2026-06-21 04:42:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c20e6422-b46d-393c-b844-7d1fa11158df | -4.06403 | -43.24355 | 2026-06-21 04:42:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d32791f9-c286-35cc-9b25-213123de9121 | -5.58798 | -46.37066 | 2026-06-21 04:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2175674c-2879-356d-8e6e-deba8f3b4678 | -6.85206 | -47.9145 | 2026-06-21 04:42:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6e3bc66-e3f2-3a04-8136-3f1ebbc55138 | -6.84074 | -47.92028 | 2026-06-21 04:42:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5e9fd55-5867-382d-b289-fccb291511a6 | -6.5092 | -42.21473 | 2026-06-21 04:42:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a1f6c21b-9ad1-3698-bc5e-fe347a88c9ff | -5.81559 | -45.08498 | 2026-06-21 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e640c94-0141-375c-ac12-4a81fc9d6f55 | -5.81319 | -45.07495 | 2026-06-21 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f62ab2fe-2698-3eff-bfbd-1581e3447a0e | -6.99686 | -42.89006 | 2026-06-21 04:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| f94c23ed-4130-3770-b1d3-8c888a31d360 | -5.81718 | -45.08737 | 2026-06-21 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d38680b6-0eff-3181-96ef-d048c3b72eba | -6.84018 | -47.92394 | 2026-06-21 04:42:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4a99bd2-573a-3a9e-ad58-f84d3ae2132b | -3.85288 | -54.22135 | 2026-06-21 04:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d1af3a6-7b92-37da-943d-709ca6022158 | -3.85227 | -54.22501 | 2026-06-21 04:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02ef3082-0d91-34a9-8f80-8e6a44d6bb0a | -6.84526 | -47.91351 | 2026-06-21 04:42:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 96f5ba1c-2e31-3771-b8fa-bce6a50f7ec0 | -6.15256 | -48.48499 | 2026-06-21 04:42:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df71dacc-a3d1-33c0-b381-b8e4478888f4 | -6.84922 | -47.91038 | 2026-06-21 04:42:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbb943b5-aea2-38e5-8dac-7d1479fd3d95 | -5.96213 | -43.48843 | 2026-06-21 04:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5534d0db-6222-35a7-82f3-9aac3844e135 | -5.95831 | -43.49269 | 2026-06-21 04:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d890be73-6041-398a-b3a8-a04026f38b2b | -5.81705 | -45.07546 | 2026-06-21 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 22064577-2bb7-3ae5-b482-069386f9ee53 | -5.81944 | -45.08548 | 2026-06-21 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 71dcc456-74da-3929-a86f-8d3fd8dd7a34 | -5.81997 | -45.06829 | 2026-06-21 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4dbb5f19-6fca-30cb-b075-5d4ba2286e45 | -11.65009 | -52.86766 | 2026-06-21 04:44:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67cf75e6-6635-3ef9-8c2f-0cd5cac1c6b9 | -10.76936 | -54.10528 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e916f80e-953e-3230-90be-31f8134bef8f | -10.24971 | -47.3447 | 2026-06-21 04:44:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f228bc6-e485-3b51-b15c-163cddfdff4c | -11.11153 | -54.14634 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| dd495c29-fdef-3a8f-8ab8-a1d2ad3a5927 | -12.83231 | -49.79749 | 2026-06-21 04:44:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 081eaacb-c89b-342e-a3df-8fd1ba51a3df | -11.10934 | -54.13688 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 5f97becc-0c0c-3f35-b33e-1af060ee8bf5 | -9.30781 | -47.6316 | 2026-06-21 04:44:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 09542f6d-963c-3ab2-8eb2-d5a71245d08b | -10.6925 | -47.69991 | 2026-06-21 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39991b7d-6cbd-3027-9867-38fc4a1fdfc1 | -11.09686 | -54.14368 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 28.3 |
| e0aab2df-418b-33c2-b0ed-5091a8928cd9 | -11.64125 | -48.5321 | 2026-06-21 04:44:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ca198bc-5f10-3cda-b9a5-294686b44d9b | -11.06914 | -52.47216 | 2026-06-21 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e316e62a-b931-36d4-b342-a4b2a8d7f729 | -8.65045 | -47.76654 | 2026-06-21 04:44:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f22be21-1a23-3d3c-a7cd-bfd87027702b | -8.43803 | -51.56594 | 2026-06-21 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6731d07d-f9e4-36fb-b4e0-2e4fef430ecd | -10.6878 | -60.75095 | 2026-06-21 04:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 35e8f7d9-6222-31c2-aafe-7ab4dfe608a7 | -10.27384 | -60.5509 | 2026-06-21 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a784d274-6f38-3978-9a90-92beba976f5b | -10.68606 | -60.74651 | 2026-06-21 04:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd6a1dd0-5922-348a-8c4d-2c7e318d1f7b | -7.91372 | -48.25133 | 2026-06-21 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cdd951f0-bd83-3649-99ac-58e72f4225b7 | -12.51391 | -48.30325 | 2026-06-21 04:44:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3541bc0e-d0cd-365c-affc-cb98b35648ea | -10.68459 | -60.75429 | 2026-06-21 04:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c05eb559-b25a-3696-b42a-5b43c3d6a5be | -12.45584 | -46.52447 | 2026-06-21 04:44:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db371e48-b0a2-38ce-a776-bae4f27ac8b7 | -10.68532 | -60.7504 | 2026-06-21 04:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 83d04cd7-8b12-32b4-9bba-a3dcf49ec759 | -11.03979 | -47.04556 | 2026-06-21 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 760e88dc-cb12-301a-ac8e-0e6b48daa686 | -10.53622 | -47.73109 | 2026-06-21 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 700db6f0-acbd-3a36-aa46-a8f6978ae710 | -11.06572 | -52.47157 | 2026-06-21 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fafd4357-e16b-385b-8472-f992f3c21b64 | -9.56267 | -48.66712 | 2026-06-21 04:44:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d92ee8e-bb7e-37f1-a0ed-c4ab2cf110e3 | -11.10641 | -54.13183 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 014b775b-3c95-3e1a-92c9-60db9eed18af | -11.09979 | -54.14876 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 28.3 |
| fba6158b-0a24-3c32-a050-5ab2ade91525 | -8.25798 | -43.92936 | 2026-06-21 04:44:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5060d71-1183-3a05-b5c1-a13bacf4871b | -13.51579 | -52.16288 | 2026-06-21 04:44:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38136b88-2182-3ae9-bedd-0d7f3915af8e | -10.2682 | -60.54988 | 2026-06-21 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 873ea35a-5891-3601-8218-84473d262103 | -9.68899 | -47.69489 | 2026-06-21 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4670e4ff-9df5-33e9-8609-1a96ce1133f3 | -12.41812 | -54.18279 | 2026-06-21 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 82cab1ef-5290-3561-84a4-8fd0b387ea9b | -8.00687 | -46.444 | 2026-06-21 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdbb9950-956a-3433-8678-916c5d2b63d4 | -10.68704 | -60.75484 | 2026-06-21 04:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1b8fc081-ebbc-3e86-a1ae-02dbf43fc292 | -12.82951 | -49.79333 | 2026-06-21 04:44:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a39a9fb-d0ba-35ad-90af-86bc61fd81fe | -10.76568 | -54.10467 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4959f8e-4bc7-3b55-bf5d-e91f279badae | -10.12425 | -52.19904 | 2026-06-21 04:44:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c093d3e-0b7a-3405-8a0e-1bb0cb4f6b9e | -12.42704 | -54.17839 | 2026-06-21 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 76600e0b-c52a-3ef7-abf4-c9345d607a76 | -11.63837 | -48.52771 | 2026-06-21 04:44:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 106edc15-269c-3bc7-831b-a3ae94922852 | -10.83336 | -49.12295 | 2026-06-21 04:44:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d30fe360-0d46-3187-8221-7a404866415c | -7.96079 | -47.4365 | 2026-06-21 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2f79523-6a30-3d79-ba54-b95ed2e672bd | -8.46364 | -51.53648 | 2026-06-21 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0859e89b-8fef-341d-b1fd-7cde0be9d863 | -10.51525 | -51.93718 | 2026-06-21 04:44:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d9cb1d7e-00f4-31bc-8356-082f768b2d77 | -12.06973 | -48.42462 | 2026-06-21 04:44:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 96ab1006-11c8-3901-9fef-9948ba37e7a8 | -10.25118 | -47.34631 | 2026-06-21 04:44:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f15f0b1-4272-37fe-a9c0-2c397afe92b1 | -11.88856 | -43.83251 | 2026-06-21 04:44:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 89e9b807-1c71-34b5-a44e-008e63895603 | -11.10638 | -54.15451 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db1b45a6-7238-3b78-b9de-a6af030c23c5 | -11.63377 | -48.53487 | 2026-06-21 04:44:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| accb873f-c9c6-3275-ab9b-bfe2cc463651 | -11.88669 | -55.13731 | 2026-06-21 04:44:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9959441d-e1f9-3e94-b875-ea12b9965663 | -9.80304 | -47.48607 | 2026-06-21 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba0e8530-c293-3426-89c9-bbd9cfd162df | -11.0617 | -52.47473 | 2026-06-21 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 737691e4-ce48-311c-b718-5efd175aa693 | -10.06023 | -48.08792 | 2026-06-21 04:44:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4c507bd1-e317-3f5d-b3ea-eb18a5c657a1 | -12.51801 | -48.29978 | 2026-06-21 04:44:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 78a70b4e-b5be-358a-8a9b-c09e8261a9c0 | -11.06511 | -52.47531 | 2026-06-21 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6a5e00a-3788-3261-8795-63ca122110ad | -13.82627 | -47.12266 | 2026-06-21 04:44:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36e2794a-71dc-32b4-9cb2-4b0ffce8b1ec | -11.06634 | -52.46782 | 2026-06-21 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c18b90c4-ac12-3c66-ad93-372f73ba7de9 | -10.51379 | -51.93697 | 2026-06-21 04:44:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fcffa6fe-d05c-3036-a536-533a56577bfb | -12.41741 | -54.18704 | 2026-06-21 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcf90116-67af-320b-a578-7d3fbe639c5e | -11.06695 | -52.46407 | 2026-06-21 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cad47256-e4ec-3257-a954-8f866a85830c | -11.10346 | -54.14942 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |


[Clique aqui para ver as próximas entradas](README7.md)
