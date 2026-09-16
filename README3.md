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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8803747f-119b-3bcb-97e0-7afcc2fde562 | -6.69422 | -56.41462 | 2026-09-16 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| a3f2c53b-9494-3807-a1a9-5d2908f14391 | -11.80443 | -60.46761 | 2026-09-16 00:22:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 955ce177-6b97-307f-8dff-36b49cb0cefa | -5.12705 | -47.63039 | 2026-09-16 00:22:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 9bdb846e-cb2a-363f-b4d6-bf2b6a4cdd05 | -11.21799 | -49.95153 | 2026-09-16 00:22:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 26882ce4-e043-3c0f-91f6-f826b437f563 | -5.75749 | -57.59663 | 2026-09-16 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| af324762-dd68-34de-9104-88ccc003f34e | -5.81096 | -53.807 | 2026-09-16 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dab2e96e-bf5d-3b71-b4e4-46efa69fd66a | -6.71198 | -56.88139 | 2026-09-16 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 169455f4-6a01-3e98-8f4f-90c1fdbd04b3 | -6.3674 | -55.83962 | 2026-09-16 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 918500e0-766d-3a3d-b606-b5080e35cccc | -11.91272 | -49.73844 | 2026-09-16 00:22:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 32cbb8c0-cf40-329e-8263-fe8ada524610 | -6.15598 | -55.70731 | 2026-09-16 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 09dd1124-4b3d-32ee-a8ad-7ac6123cb601 | -6.61227 | -51.42994 | 2026-09-16 00:22:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 346a5aca-fa2c-32f4-9261-f3ecfc0bda23 | -7.56037 | -62.33206 | 2026-09-16 00:22:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 3cf10d9d-a6d1-30ba-8b05-5abd5bb1a1b2 | -8.40769 | -54.71666 | 2026-09-16 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 16c23b04-49f4-36a7-89da-78d1479232a2 | -8.4089 | -54.72551 | 2026-09-16 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f6371021-b87e-3bd2-9537-23ce4b036f5a | -7.86323 | -55.454 | 2026-09-16 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| e9930e32-fa77-353a-baad-8626f7b5fcfe | -8.32567 | -51.31085 | 2026-09-16 00:22:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 07636311-4f46-3000-8aba-901819fc5b78 | -9.47462 | -45.47456 | 2026-09-16 00:22:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 28.2 |
| a8b6fc6e-f82d-322c-be67-737cda71749b | -10.69279 | -54.1692 | 2026-09-16 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 3b232acd-00ea-329d-a4d0-85bf2f560bc4 | -10.7787 | -46.21475 | 2026-09-16 00:22:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 94a77de2-b48c-3c67-b214-91d11602e700 | -9.10647 | -45.74528 | 2026-09-16 00:22:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 246.6 |
| 36052eae-3cb2-3cfa-b5a6-13ab5efa7854 | -7.85434 | -55.45522 | 2026-09-16 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 24008f01-316b-30af-8778-ab6165c1d92c | -9.4734 | -45.45149 | 2026-09-16 00:22:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 9d1add00-1a3d-362b-b890-dc38f11e9f03 | -10.68155 | -54.15265 | 2026-09-16 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c74a36de-cb39-35fd-af86-57e2079bde0d | -6.72799 | -48.1298 | 2026-09-16 00:22:00 | TERRA_M-M | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 6b82ed77-b1ca-3227-a310-64e84411c1ae | -9.34794 | -50.17671 | 2026-09-16 00:22:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| c3e34208-bf89-3713-afee-a61f16149dda | -10.25435 | -57.69783 | 2026-09-16 00:22:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 4c7e4c88-4d63-325d-9136-2b3489a3ddd2 | -11.98553 | -52.47253 | 2026-09-16 00:22:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 29ca06c4-79d0-31c1-9e76-5bb25e998e29 | -9.38713 | -60.31905 | 2026-09-16 00:22:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 5f485c51-2f69-312e-bbd6-1a8d797ef6af | -5.80969 | -53.79789 | 2026-09-16 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d38ab912-a502-3b46-a4ea-0abfeadbadf4 | -6.85649 | -55.30657 | 2026-09-16 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 14b67e7c-88a2-381b-b17c-956491f636de | -9.21415 | -60.29638 | 2026-09-16 00:22:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 4205f63f-347d-32a3-925e-8fb9c1415cd8 | -5.81408 | -49.85698 | 2026-09-16 00:22:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| e75127bf-86b9-3bc3-b490-a2ed79fa4520 | -10.70159 | -54.16795 | 2026-09-16 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 4291cb97-8a80-370a-bc91-8d114bece2fa | -9.09319 | -61.0228 | 2026-09-16 00:22:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| c3e85569-708a-3208-95ef-e946bc299e3e | -8.37368 | -54.7305 | 2026-09-16 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| c38a4cad-4961-3b37-aee9-0b9f559701b6 | -9.39958 | -60.31757 | 2026-09-16 00:22:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 7f006ea4-de2c-3bde-aacf-d6293b4dbd1d | -6.38711 | -53.178 | 2026-09-16 00:22:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 94c627c3-6d10-3d15-ae72-a078f62146be | -11.19315 | -54.13038 | 2026-09-16 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| cf485542-0f4c-3fd5-97b3-b53198b142e5 | -9.23456 | -46.71333 | 2026-09-16 00:22:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 7fe5b69e-ea39-38b8-bb3e-583701cc0162 | -10.41983 | -48.65155 | 2026-09-16 00:22:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 8c9884bb-1ce4-3021-92b6-5062662b094d | -9.78454 | -60.47797 | 2026-09-16 00:22:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 07a31731-eae5-3ede-9adf-9c7fd89d5a34 | -9.46973 | -45.44544 | 2026-09-16 00:22:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 46.0 |
| ccca5b14-f252-37ce-9b02-86270f50702a | -10.4413 | -50.98981 | 2026-09-16 00:22:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| aaaee3d9-72fb-38cc-b985-42c146812b00 | -7.40435 | -49.72413 | 2026-09-16 00:22:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 80bae027-2666-3fd1-a82d-9d1750040e0e | -7.44682 | -49.47447 | 2026-09-16 00:22:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 5978bd0b-b180-37e8-bfae-ff4d7ca0178f | -9.87582 | -49.83279 | 2026-09-16 00:22:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c07c8078-a085-31d3-a75a-af4ec15fac24 | -6.3721 | -55.13453 | 2026-09-16 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d6ffa20b-7259-3ed3-b274-a170eeb45acf | -10.93743 | -54.0855 | 2026-09-16 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 73a209c5-227c-3721-b262-765116c26e0b | -6.36957 | -54.96757 | 2026-09-16 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 46f08ef9-58c0-33a3-8c3f-9dd31ec7b981 | -12.13803 | -57.1859 | 2026-09-16 00:22:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e7f147d6-2331-3c3e-b618-8690d48aa45f | -6.10949 | -57.69759 | 2026-09-16 00:22:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4a03271b-85db-31bf-84c4-747055ea39ce | -8.55184 | -44.48498 | 2026-09-16 00:22:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 63.6 |
| f12a260c-ff43-3fb4-ae47-3371c227c43e | -9.16267 | -49.99372 | 2026-09-16 00:22:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f20c4c4c-34dc-3ca9-b159-49699369a3d0 | -6.27539 | -55.29824 | 2026-09-16 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8dd0acb1-d3f7-3e8c-bddc-e50e15e4b5aa | -10.55055 | -57.45538 | 2026-09-16 00:22:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 92ca6470-c4c7-3def-b9f6-a89cd6cd6c32 | -4.30354 | -49.11914 | 2026-09-16 00:22:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 7b71d1e5-34cd-3b67-81bb-1cade440c255 | -9.85288 | -48.35834 | 2026-09-16 00:22:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ca4fa6ac-a986-36c6-a542-81e5adc964d8 | -9.79554 | -48.8065 | 2026-09-16 00:22:00 | TERRA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 326a599c-d187-323c-a809-1d54f471b0a8 | -8.55775 | -44.52103 | 2026-09-16 00:22:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 50.3 |
| c2e2fed9-0303-3a37-a14c-a155ae730485 | -11.19458 | -55.02311 | 2026-09-16 00:22:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8f89cde8-9dac-3ea1-973c-3c868b9eea51 | -10.87361 | -54.01289 | 2026-09-16 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9e6f35c6-2a3d-311f-8c34-455fb171a4bf | -10.835 | -46.20541 | 2026-09-16 00:22:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 379b9334-145d-39f5-8539-60cc88f58d20 | -10.41546 | -48.64699 | 2026-09-16 00:22:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| bd75d35b-d15d-3fdb-b7a3-4edfa1726dac | -10.59745 | -47.74777 | 2026-09-16 00:22:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1a4455c3-d539-3125-a40e-8ba8956eead2 | -8.71335 | -62.83226 | 2026-09-16 00:22:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 482ac257-a57f-347e-9ead-2e2b686d96c7 | -8.37247 | -54.72164 | 2026-09-16 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ca64d6cf-1f7c-3d1f-b4fc-c8b43e570283 | -5.10467 | -47.61491 | 2026-09-16 00:22:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 58de0eb9-9b35-3c3f-a9ef-7c67d066883d | -8.57672 | -48.5224 | 2026-09-16 00:22:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 779e1a0c-8098-3510-b4be-d7a72bb6cb18 | -6.27488 | -50.94786 | 2026-09-16 00:22:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a9e4e6e5-6bd8-3d56-9f2a-27db8b7bbef0 | -7.10836 | -55.12636 | 2026-09-16 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1a31fc62-8987-3a52-b102-873f3dd06e1e | -6.28466 | -56.04202 | 2026-09-16 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7b5e0f9f-2367-3e86-b2b3-dfca39f9dabd | -5.11864 | -47.61259 | 2026-09-16 00:22:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 155.6 |
| 8d84373c-04a8-39d0-9ad9-f2da450e12d7 | -6.0097 | -47.40473 | 2026-09-16 00:22:00 | TERRA_M-M | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| c7f71a13-7ea5-3dad-8561-5c292da5985b | -11.23127 | -47.60069 | 2026-09-16 00:22:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| a0bd5fc4-7fe6-34b1-be54-be47d36466c7 | -5.11306 | -47.63239 | 2026-09-16 00:22:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 961c1548-f604-3d30-8fec-3f70f732d98d | -10.6046 | -57.32245 | 2026-09-16 00:22:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 93fb835e-f748-3fd6-94bf-ec0969c2c8e7 | -5.81342 | -49.86757 | 2026-09-16 00:22:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 9910bed7-f6cd-35da-a2f9-113710960d3b | -9.10142 | -45.7156 | 2026-09-16 00:22:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 213.3 |
| 090780f7-b328-3434-9773-d765c59e3aee | -7.8298 | -50.2508 | 2026-09-16 00:22:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 90f294ff-e027-34d1-9b9a-086fd7430738 | -4.3063 | -49.13802 | 2026-09-16 00:22:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| b99e723d-0748-367b-befe-c522c2c33a95 | -10.39177 | -53.7949 | 2026-09-16 00:22:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d46c257e-e4dc-3082-8685-4efd83578a52 | -11.97656 | -52.47387 | 2026-09-16 00:22:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 5ad0ef6a-1c21-3ab8-b342-4c6d1829fd21 | -6.1572 | -55.71627 | 2026-09-16 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| df76aa03-e67c-3f8c-8255-e93d9b7ff68f | -5.00371 | -45.3559 | 2026-09-16 00:22:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 5573f009-6f13-33d8-9e37-a7574d3677b1 | -9.86508 | -49.83444 | 2026-09-16 00:22:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| c3d96d78-6856-33b6-ae46-525dbf579cc7 | -10.90124 | -54.018 | 2026-09-16 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a6103910-82cf-3729-93d9-f787995abaac | -6.37506 | -55.82932 | 2026-09-16 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d07825b8-4de8-3e23-9564-33400ea8f4dd | -8.68311 | -61.41156 | 2026-09-16 00:22:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 562c92f2-9012-3289-a045-7eae6dbf068c | -10.4056 | -48.63668 | 2026-09-16 00:22:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| aaa48833-82ef-3439-ae43-b79a97a5b973 | -12.11773 | -57.18864 | 2026-09-16 00:22:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 9db4f3bd-8522-3a8d-9c06-df7ba9053774 | -5.22575 | -49.31232 | 2026-09-16 00:22:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0926bba9-6218-3d95-898a-b103a5727578 | -6.26416 | -55.28181 | 2026-09-16 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 74e5e8d2-6b7c-361a-a6d0-bfe60f3a4abe | -9.10836 | -45.75203 | 2026-09-16 00:22:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 164.1 |
| a4a2b32e-903b-342c-8322-820dadf8fa3b | -6.4377 | -55.61312 | 2026-09-16 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 14b18356-5333-3dde-8058-b379a0bdcdbf | -10.70281 | -54.17686 | 2026-09-16 00:22:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 30.5 |
| e8b6d8f3-1831-3642-b014-35ae78e984a7 | -11.97524 | -52.46455 | 2026-09-16 00:22:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 24891f35-f2a5-399e-8929-6375f52d8b69 | -9.10352 | -45.7222 | 2026-09-16 00:22:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 281.4 |
| fc710b4e-2194-3f32-a7bd-893dc15a2711 | -10.45895 | -44.94694 | 2026-09-16 00:22:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 119.2 |
| d8b04a7c-e62d-3415-ba9f-770780b330d6 | -7.51353 | -50.15437 | 2026-09-16 00:22:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| a1fba90a-b0a2-3dec-a681-f013c592cdae | -6.43648 | -55.60417 | 2026-09-16 00:22:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |


[Clique aqui para ver as próximas entradas](README4.md)
