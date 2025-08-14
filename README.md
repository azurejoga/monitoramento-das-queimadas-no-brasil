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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20270279-9a67-373e-9e29-f563700b750a | -7.6287 | -63.5154 | 2025-08-14 00:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 790cd5e9-6890-39d7-adb0-820f2c523900 | -18.6278 | -43.2993 | 2025-08-14 00:00:00 | GOES-19 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 51.9 |
| a4165f07-fa8f-37aa-a742-1f53a7523fea | -8.5211 | -43.3063 | 2025-08-14 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 6bdaa3d2-e5cc-36a0-84e5-f958f8e6a2d9 | -6.0808 | -59.9274 | 2025-08-14 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 5be76323-3e2f-30aa-97f7-0b8a0a31bfa5 | -8.5208 | -43.3298 | 2025-08-14 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| c23c0886-48a8-3d49-afc3-62d342de3ff1 | -5.9899 | -44.1528 | 2025-08-14 00:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 97aee25f-ad6b-3566-9f51-f977d17be3bf | -9.152 | -59.6772 | 2025-08-14 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| b894cedf-ec53-3e84-9bf7-9f38a1880a4c | -6.9422 | -44.5562 | 2025-08-14 00:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 6ff55063-6d81-39df-af5e-32e814286348 | -6.0807 | -59.9465 | 2025-08-14 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 158.6 |
| 96b092ca-973b-333b-ba0b-f85954ea4b40 | -7.8774 | -61.8253 | 2025-08-14 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 463d7188-86e6-31dd-850e-c0c6e66202ce | -9.1706 | -59.6762 | 2025-08-14 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 18d74607-5a25-3298-bdc9-a6463bc377c7 | -8.4783 | -49.8529 | 2025-08-14 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| a097c014-1f4b-3ec4-9b2f-eaad6a1dcb95 | -8.1028 | -61.2069 | 2025-08-14 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 66b9efcc-6a13-3799-80af-00b2b73cfc36 | -18.6285 | -43.2746 | 2025-08-14 00:00:00 | GOES-19 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 52.0 |
| 84f8e448-7951-3705-b417-2f742b3a7465 | -9.1708 | -59.6568 | 2025-08-14 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 668395f9-36e0-36ec-8e7a-fd4d407a31c9 | -9.1522 | -59.6578 | 2025-08-14 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| b17a10d7-ece0-316c-8142-7aa4030956c0 | -9.4992 | -60.547 | 2025-08-14 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 114f918a-c38e-36ce-a485-10cc871460d6 | -6.0992 | -59.9267 | 2025-08-14 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 0e2dea8d-5ce3-3c5b-a80f-53b2d126ccd4 | -9.1336 | -59.6588 | 2025-08-14 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 02ba0fc7-a5fe-3658-a576-f8e0eff7c079 | -18.5303 | -46.0414 | 2025-08-14 00:00:00 | GOES-19 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 62.4 |
| e080a562-8314-3442-865b-ec5829cdd1f6 | -7.6103 | -63.516 | 2025-08-14 00:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 5982fc04-e401-3105-a224-5c04ecc18721 | -6.961 | -44.5546 | 2025-08-14 00:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 4234c2a5-5dde-3409-9341-d067c3764c5f | -9.4994 | -60.5278 | 2025-08-14 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| ee1bc992-717a-3ec2-9a9b-307c5e6cb83b | -18.5505 | -46.0369 | 2025-08-14 00:00:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 54.8 |
| fe99e641-95ec-3665-93bd-f82f409b1790 | -8.1029 | -61.1878 | 2025-08-14 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| ff398ad3-695c-3b19-9a83-fb0cdd3a93a1 | -7.1299 | -60.1182 | 2025-08-14 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| d7394812-8951-35ac-aab7-089d30b7f8c8 | -6.0991 | -59.9459 | 2025-08-14 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 147.8 |
| 6ee310ad-e890-39b7-896b-4e698a9cc4fe | -7.8775 | -61.8063 | 2025-08-14 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 307df171-675c-394c-b163-54725ced36cf | -6.0992 | -59.9267 | 2025-08-14 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 8b3c7290-9e47-3c5a-afd7-a64547010565 | -6.0808 | -59.9274 | 2025-08-14 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| ceb3de3f-bdc6-39cf-8e21-190c647fa381 | -8.1028 | -61.2069 | 2025-08-14 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| b794ed03-e34f-3b5b-bbd8-c548b888ee00 | -7.8774 | -61.8253 | 2025-08-14 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 133.1 |
| cfc24d33-6955-38fd-8e79-c24958bc48ae | -6.2655 | -53.6817 | 2025-08-14 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 14fff7de-a0a2-3655-99f0-dee0024b0783 | -18.6285 | -43.2746 | 2025-08-14 00:10:00 | GOES-19 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.0 |
| 53ac576d-1315-3a61-bd34-5bf0d9d6b285 | -15.087 | -55.4438 | 2025-08-14 00:10:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 787176c1-d9b8-3aa2-9ebd-d6cfddbd3591 | -18.6278 | -43.2993 | 2025-08-14 00:10:00 | GOES-19 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 48.4 |
| 6b2381c1-9c8c-3b3b-b546-af5129ed4308 | -7.8775 | -61.8063 | 2025-08-14 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 4d19c1d1-7993-34d8-8b3c-97d940dbc9da | -14.485 | -46.0586 | 2025-08-14 00:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 5a0e0ec4-24c1-3e9a-b6fe-3963163546ca | -5.9899 | -44.1528 | 2025-08-14 00:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| b6e6ee8f-df38-3211-bbcc-859dd3675a24 | -18.5505 | -46.0369 | 2025-08-14 00:10:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 68c1f6f1-0a13-3a9e-8cd6-b8799964a472 | -6.0991 | -59.9459 | 2025-08-14 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 130.9 |
| f93ae9f6-6691-383b-9542-9324299b949b | -9.1892 | -59.6752 | 2025-08-14 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| d26b10c6-0fcf-351a-99c8-023f9f1e4643 | -6.0807 | -59.9465 | 2025-08-14 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 143.2 |
| 47a3bdee-866f-3a5c-9368-fb257b9efa01 | -5.9711 | -44.1542 | 2025-08-14 00:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 3812b85f-545d-37b1-bba4-f28480836cd2 | -9.4994 | -60.5278 | 2025-08-14 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| cba65080-b5d6-36ea-93c2-9c4a599ff6c2 | -23.676 | -51.8192 | 2025-08-14 00:10:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 48.8 |
| 86526979-815d-3a67-8464-8043b423da24 | -7.6103 | -63.516 | 2025-08-14 00:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 100.5 |
| e7bd7dcf-4cdf-31b7-8d4e-e65b8d82d534 | -8.5211 | -43.3063 | 2025-08-14 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 56.2 |
| fd530da5-67a7-3be4-9c6e-6727947c7daa | -15.0873 | -55.4231 | 2025-08-14 00:10:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 3cdc3e8f-0a6b-3a85-ae80-c30768d9ab86 | -7.6287 | -63.5154 | 2025-08-14 00:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 83a0826d-e75d-35ae-8ab3-8832a630e7e3 | -9.1522 | -59.6578 | 2025-08-14 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 43231727-81da-3391-b50d-3791f66c3431 | -9.1706 | -59.6762 | 2025-08-14 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 4d1b0f3e-8af5-3893-b5e2-f5329d1e7862 | -7.5918 | -63.5166 | 2025-08-14 00:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 66b4f76b-01e8-3a95-93a8-3e8badec0fe6 | -9.152 | -59.6772 | 2025-08-14 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 33387bda-abbd-324f-8d60-2441c174a65d | -17.0436 | -51.7799 | 2025-08-14 00:10:00 | GOES-19 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 5c93f12b-a925-3096-9623-3896921b1682 | -8.5208 | -43.3298 | 2025-08-14 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.2 |
| b2c5c528-a297-323a-8859-20914f6e9d36 | -6.9422 | -44.5562 | 2025-08-14 00:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 03d796ec-f49d-3b43-9272-f99d9a968a35 | -17.0432 | -51.8016 | 2025-08-14 00:20:00 | GOES-19 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 43.2 |
| f5321aea-e749-3032-bb4e-30bc16e3dee4 | -7.6287 | -63.5154 | 2025-08-14 00:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 1c2b2dfc-aee0-37ba-92b3-2a712fcdc490 | -6.961 | -44.5546 | 2025-08-14 00:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| c6d97f62-b7ff-3edc-ba96-a873efe77ab3 | -6.0992 | -59.9267 | 2025-08-14 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| f42bf8b7-8c45-32d1-8501-c6f8b9ecb895 | -6.0991 | -59.9459 | 2025-08-14 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 144.3 |
| db0cca4a-86bc-36d2-b4c3-d4090cef1ad8 | -6.9422 | -44.5562 | 2025-08-14 00:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| bd5df420-a577-3ee2-ba35-c11f9f16ef16 | -7.6103 | -63.516 | 2025-08-14 00:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 7b0b8b81-0067-30c7-80b4-d34cc4a8d64d | -14.485 | -46.0586 | 2025-08-14 00:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 711f16c7-7520-31d1-9208-33cdd4dcd878 | -6.0807 | -59.9465 | 2025-08-14 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 124.0 |
| ac2cff6a-4c6f-3377-aaea-d6a7cfc97da8 | -22.6767 | -47.4647 | 2025-08-14 00:20:00 | GOES-19 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 4810f400-876d-3359-bfbc-f69a8d652162 | -8.5397 | -43.3277 | 2025-08-14 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 39730b26-502d-39ff-abce-f7e4a10b9e12 | -6.2655 | -53.6817 | 2025-08-14 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 0af16178-a03f-36fe-8175-27f8d11bf325 | -7.8775 | -61.8063 | 2025-08-14 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 0f373c5a-4be2-3115-8e63-924738332a5f | -9.4994 | -60.5278 | 2025-08-14 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| b4168d1a-b58c-3b0d-8390-989d0a4f3dd3 | -8.5208 | -43.3298 | 2025-08-14 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 49.1 |
| df77420b-1c9d-3a41-b8a6-48b4e36b7b39 | -9.1708 | -59.6568 | 2025-08-14 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| ea78711b-c2f0-3fe5-ad92-00466bf91266 | -5.9899 | -44.1528 | 2025-08-14 00:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 694f0414-1c0b-3a10-b788-9e4e4fd1593e | -8.5211 | -43.3063 | 2025-08-14 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 7e49fba4-1a51-30fc-a5cb-6aa1bf238097 | -7.8774 | -61.8253 | 2025-08-14 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 0c573abb-cf23-35ff-961f-2067b37e122c | -15.087 | -55.4438 | 2025-08-14 00:20:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 2c31d27f-9aa2-387e-8ba4-cf96e570d94d | -9.152 | -59.6772 | 2025-08-14 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 13b6d025-c61e-3c99-8af0-d0800d222e6f | -9.1522 | -59.6578 | 2025-08-14 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 6e342f93-ae12-345e-ad67-5fa7803a580a | -9.1706 | -59.6762 | 2025-08-14 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| be5b5fcc-c68c-33db-bf9f-7891186c2e4d | -14.4845 | -46.0817 | 2025-08-14 00:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 3f883dfb-c010-3aca-b777-535e80a6ae11 | -6.961 | -44.5546 | 2025-08-14 00:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 7f5d6544-e255-3a19-a646-9d23c253b8b5 | -6.9422 | -44.5562 | 2025-08-14 00:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 6961c3ec-3819-3b1c-b085-0bc3dd535cb5 | -7.8774 | -61.8253 | 2025-08-14 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 8649689d-3002-3719-bc3e-8533123fea08 | -22.6774 | -47.4407 | 2025-08-14 00:30:00 | GOES-19 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 49.0 |
| bd9907c7-3a00-3e46-89a2-d3e2091ab8fe | -6.0991 | -59.9459 | 2025-08-14 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 115.2 |
| ddca2173-a772-31e0-9c86-376a777eefba | -8.5211 | -43.3063 | 2025-08-14 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 0a7b3685-2cd5-3d77-b347-366d0166359f | -17.0629 | -51.7984 | 2025-08-14 00:30:00 | GOES-19 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 0240f818-beaa-32ac-b3ec-ef04fd9ca9f8 | -5.9899 | -44.1528 | 2025-08-14 00:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 83566bbd-6406-3e85-9b5b-7902fc032a45 | -7.6103 | -63.516 | 2025-08-14 00:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 6bae6f14-04ac-32ab-a085-b3fb062429d1 | -6.0992 | -59.9267 | 2025-08-14 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 79e5f686-a95c-34e4-8438-bef8167e14ca | -7.6287 | -63.5154 | 2025-08-14 00:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| e477caa8-c103-35dd-82f7-9d75be0bb410 | -6.2655 | -53.6817 | 2025-08-14 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| b7a3c6ad-b849-302b-94af-3db8019b4252 | -22.6767 | -47.4647 | 2025-08-14 00:30:00 | GOES-19 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 3d90142b-b5c2-352d-a172-cbdddb461bb0 | -9.1706 | -59.6762 | 2025-08-14 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 805785ed-ae16-3966-a5de-673f88fc8c62 | -9.1522 | -59.6578 | 2025-08-14 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 9307f980-4116-357f-bb81-a4ac548adee7 | -8.5208 | -43.3298 | 2025-08-14 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 44.9 |
| 42cc2dbf-c1c8-3a7f-9271-1d22b286061e | -9.4994 | -60.5278 | 2025-08-14 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| feb990ec-e2bc-332a-ac17-fc49db9cf75d | -8.1029 | -61.1878 | 2025-08-14 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 24ae9aac-cc42-34b7-83e6-ff649f501983 | -7.8775 | -61.8063 | 2025-08-14 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |


[Clique aqui para ver as próximas entradas](README2.md)
