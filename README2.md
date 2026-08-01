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
| 3e573c35-1e6c-315c-bcc5-14a993104e6e | -8.1939 | -55.427399 | 2026-08-01 00:31:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe1446b2-6d2b-3fc5-b7db-b9591cdf412d | -9.8683 | -48.7155 | 2026-08-01 00:31:00 | METOP-B | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 87091ca2-5e73-3bc0-8af0-39c79ae5872a | -7.6445 | -45.046398 | 2026-08-01 00:31:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6cdc57f2-94ea-3e7b-b222-383a2897532d | -4.3604 | -47.772701 | 2026-08-01 00:31:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 263fdd49-b77a-35ef-a51c-5c73cd0a7e56 | -11.2184 | -54.036098 | 2026-08-01 00:31:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6bbf7921-8f75-3d0d-a9b5-e08c21f2c4e2 | -1.6481 | -54.444599 | 2026-08-01 00:31:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65c12f0f-2603-3cb6-8e6c-efd3bc128c0e | -5.8078 | -44.749599 | 2026-08-01 00:31:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4b499dd-7613-38df-8938-aa525026dc55 | 1.0983 | -60.498001 | 2026-08-01 00:31:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7903b9c7-6377-3473-bf3b-9f9e950b6267 | -10.8735 | -50.549301 | 2026-08-01 00:31:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9f69c226-6d66-3d49-b276-fe9bb7874fec | -14.342 | -48.035702 | 2026-08-01 00:31:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2229fa1e-d2cc-3cf6-a245-6b1e85c4fda0 | -14.0683 | -46.229801 | 2026-08-01 00:31:00 | METOP-B | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0e62940c-b976-316a-9d33-589ed95d9ba0 | -4.6087 | -49.035099 | 2026-08-01 00:31:00 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff792f74-280f-38af-a62d-4d2b8a9626a2 | -17.0515 | -45.8647 | 2026-08-01 00:31:00 | METOP-B | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bd5466f2-7382-3e56-8764-10b1c369c9a4 | -20.5445 | -57.259899 | 2026-08-01 00:31:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| eb8e0927-38d8-3d14-9042-cf87732109f4 | -14.3297 | -48.027599 | 2026-08-01 00:31:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0402e005-b52c-39e0-af94-29748d023aee | -11.2346 | -54.852299 | 2026-08-01 00:31:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8d41a8be-e78b-3694-ad2f-fe849a4395c9 | -20.6096 | -57.283501 | 2026-08-01 00:31:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 976b39a9-2e98-3f58-a80a-05da0899319d | -8.6219 | -50.0168 | 2026-08-01 00:31:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44747ec1-62a5-3336-a46d-5c9135333bd5 | -6.1049 | -55.7962 | 2026-08-01 00:31:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25ab19ba-3f51-3998-a697-43d9f8fb4c19 | -20.5467 | -57.271801 | 2026-08-01 00:31:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 44050e29-367e-3c4c-9245-03d816745e24 | -6.5651 | -56.521999 | 2026-08-01 00:31:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ece1c6f-ac25-34de-a3a1-16f4ff63dd8b | -11.22 | -54.833099 | 2026-08-01 00:31:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ff7a823f-bb5a-395b-9178-bf0ad90798f0 | -11.2361 | -54.859402 | 2026-08-01 00:31:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eab67bdb-b21c-3bb1-90e5-972225635a67 | 1.0942 | -60.516201 | 2026-08-01 00:31:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| daabec8f-e0e7-3e00-b309-69812f19b4c1 | -11.2557 | -54.855 | 2026-08-01 00:31:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1f4906b7-7d69-39ac-bdd2-7d93f1ce4ac1 | -10.8715 | -50.540798 | 2026-08-01 00:31:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9089b6e-9627-3dac-82b9-b62e597e3069 | -20.509001 | -48.8536 | 2026-08-01 00:31:00 | METOP-B | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cb3e6985-d41b-363c-964e-204197722c22 | -18.045601 | -51.307701 | 2026-08-01 00:31:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 546aefe9-2b20-3d24-bf53-cdf72a91a3c2 | -14.0621 | -46.246201 | 2026-08-01 00:31:00 | METOP-B | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b0349548-83e0-3a8d-8929-846b3a183d2f | -21.668501 | -56.321701 | 2026-08-01 00:31:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 71498192-70f7-318a-92b0-12a39e45649c | -13.0644 | -52.7136 | 2026-08-01 00:31:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84627645-c2a8-3a14-824e-8c637b205a16 | -11.4309 | -50.592602 | 2026-08-01 00:31:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 48f6d6a5-7ed1-3614-83fd-98d783f68a02 | -18.044001 | -51.3004 | 2026-08-01 00:31:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dab5c62c-3240-326c-a82b-200283e4cecc | 1.1004 | -60.488899 | 2026-08-01 00:31:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 98563125-4c62-3f23-8d99-d46fc261b8df | -9.871 | -48.726501 | 2026-08-01 00:31:00 | METOP-B | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 732b849d-1d68-38df-bdd2-a6f8a2220054 | -6.5667 | -56.529301 | 2026-08-01 00:31:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 847e0486-d63f-3e1d-b178-76ac68d62ff0 | -11.2283 | -54.823799 | 2026-08-01 00:31:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 34b99540-d922-3efb-9985-8ffde5e2cfa3 | -20.560801 | -57.293499 | 2026-08-01 00:31:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a9b83b76-7341-3703-81be-ce5beb460814 | -6.5603 | -55.164501 | 2026-08-01 00:31:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d6d95da-a99c-3bf5-8ec0-2ee26e69cdd9 | -14.3368 | -48.014599 | 2026-08-01 00:31:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 51869f73-498a-32d7-ad4c-f9e9e2853994 | -5.5456 | -43.983799 | 2026-08-01 00:31:00 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f9181d5-6d82-3a3a-8dd9-71c939340845 | -3.8373 | -44.083302 | 2026-08-01 00:31:00 | METOP-B | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 967b2378-8eb8-32cd-924d-2dbcd674aaa7 | -12.1999 | -52.855301 | 2026-08-01 00:31:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c7ff4b7b-4f60-32ed-95c0-05856fcb5286 | -6.5685 | -55.155399 | 2026-08-01 00:31:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2de305aa-fb93-3c99-9c69-ddc05c7a6e9e | -11.2572 | -54.862099 | 2026-08-01 00:31:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c6d90d3-c37e-3228-be9a-199b0582511d | -6.5587 | -55.1576 | 2026-08-01 00:31:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3863002-aa89-33a8-a8cc-847999225d08 | -2.8811 | -48.021702 | 2026-08-01 00:31:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f4b516e-f07d-309c-ac1a-af9997ceebdd | -20.8785 | -48.973999 | 2026-08-01 00:31:00 | METOP-B | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9668a094-99f6-3c88-9750-bb5696af86e4 | -8.197 | -55.441399 | 2026-08-01 00:31:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a096f871-5ce0-3261-a3c1-c22dab485421 | -4.3567 | -47.757198 | 2026-08-01 00:31:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05e12cfb-4e36-328d-b41f-92efdcf362ae | -11.4328 | -50.600899 | 2026-08-01 00:31:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2f7defd3-7a43-3ade-a178-4113bcf5df32 | -18.515699 | -47.364498 | 2026-08-01 00:31:00 | METOP-B | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 52dd0a32-3c04-3eb8-a4fc-7a349a13fbb6 | -10.0756 | -60.4813 | 2026-08-01 00:31:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46425060-6804-3bfe-9ef0-8f78d212a966 | -11.2525 | -54.840801 | 2026-08-01 00:31:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 845e4d9a-49b8-38d1-bfc5-8b9b4d42134c | -11.4348 | -50.6092 | 2026-08-01 00:31:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b2435898-f595-3bdb-a150-98c186104a47 | -7.6349 | -45.048901 | 2026-08-01 00:31:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9ba574e3-a974-33e5-ae23-57989420aaee | -4.2647 | -48.190498 | 2026-08-01 00:31:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75113cec-5cc6-3d4a-83d7-11a8be9f1077 | -7.2936 | -55.312801 | 2026-08-01 00:31:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81db0ef5-a18a-354d-902f-c0d4727e1e32 | -2.8871 | -48.003799 | 2026-08-01 00:31:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6dc8318-a8a5-3c03-919e-ba1d5510d83a | -5.5485 | -43.9543 | 2026-08-01 00:31:00 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48236fc7-32fc-3b70-be11-0314aac1ce27 | -21.6665 | -56.310902 | 2026-08-01 00:31:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f530ab1c-5957-33f3-aba2-bea7dafba984 | -6.1064 | -55.8032 | 2026-08-01 00:31:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70eba6b5-74fe-3d03-b625-7f1127d99c71 | -11.2377 | -54.866501 | 2026-08-01 00:31:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa806ac2-4804-3cd6-b47b-dad0494eebaa | -11.2314 | -54.838001 | 2026-08-01 00:31:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bd0333e0-ddca-3764-9360-1ce3142114f0 | -6.5458 | -55.146 | 2026-08-01 00:31:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26fa20c4-82c7-37ca-8b72-720e38c69f7b | -1.6498 | -54.451801 | 2026-08-01 00:31:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e59ef3fd-48da-3f84-bf30-c1e7aaaef37f | -11.2443 | -54.850101 | 2026-08-01 00:31:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3385069e-5963-32d9-a5c7-dbfa32c7ad99 | -18.482901 | -51.698299 | 2026-08-01 00:31:00 | METOP-B | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d70fd3b9-f1e8-3cea-9fff-eb856b89dee8 | -6.5654 | -55.141602 | 2026-08-01 00:31:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07d16a27-f570-3bb1-995a-2fde1e632275 | -4.6117 | -49.0476 | 2026-08-01 00:31:00 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36537a3b-8330-34d7-9c2c-d49e4be9afc4 | -11.2541 | -54.8479 | 2026-08-01 00:31:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 402a9926-9e72-3fd6-b0db-79d59bf881eb | -14.0718 | -46.243599 | 2026-08-01 00:31:00 | METOP-B | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e939d4b6-1d2b-3500-9f73-4e0a9bd863b2 | -6.5572 | -55.1507 | 2026-08-01 00:31:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1cbb156-6dc7-346e-8a7a-d4ebc0d42553 | -11.2474 | -54.8643 | 2026-08-01 00:31:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a89abfd7-222c-3ac2-b07e-bf53740a792f | -18.4813 | -51.691101 | 2026-08-01 00:31:00 | METOP-B | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3050f41f-bc56-3ee1-ad6d-3061e70e66fb | -4.2613 | -48.175999 | 2026-08-01 00:31:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f0f2a52-66f9-39f9-9207-4f3026912fce | -18.5352 | -47.3703 | 2026-08-01 00:40:00 | GOES-19 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 49.9 |
| c4d5d6e0-456a-3740-84e5-b397f1b9a891 | -11.4284 | -50.6075 | 2026-08-01 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 990acb7a-591a-3a41-a5c1-0f87442510b0 | -6.5699 | -55.156 | 2026-08-01 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 9a06aae4-f8b1-38a9-8d2f-cfeb176b131f | -2.8932 | -48.0171 | 2026-08-01 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 899c1495-837f-3084-bf0d-a01a896b7adc | -1.6591 | -54.4543 | 2026-08-01 00:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 7ddaa930-065a-3c19-848c-bc5eb06bab32 | -6.7744 | -41.0084 | 2026-08-01 00:40:00 | GOES-19 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 63.4 |
| e184aaed-dfe2-3079-9da9-42f1ccbaa875 | -11.2404 | -54.833 | 2026-08-01 00:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 3e7e1b90-db01-32ab-8667-f741e18fc3ed | -11.2399 | -54.8737 | 2026-08-01 00:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 456.0 |
| 363e48af-cfb1-3788-8dc8-abb3c56e6bdc | -11.2588 | -54.8721 | 2026-08-01 00:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 351.3 |
| 128dcf6b-c018-3fb9-b494-61252b143571 | -6.7555 | -41.0103 | 2026-08-01 00:40:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 95.6 |
| 110f61f7-287d-3a3f-9800-75cf1dc8c625 | -14.0735 | -46.2439 | 2026-08-01 00:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 6523193b-f3ac-31df-a1ce-bfb471d7643b | -11.2402 | -54.8534 | 2026-08-01 00:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 548.8 |
| e9dcca7c-8282-3dfe-9924-c0f72233bb53 | -11.2591 | -54.8517 | 2026-08-01 00:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 413.0 |
| ea7d36cf-617a-36ba-90a0-af91800b516a | -3.0612 | -39.9346 | 2026-08-01 00:40:00 | GOES-19 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 66.0 |
| 13747963-70c9-3958-814d-288b51ed3f3d | -2.8932 | -48.0171 | 2026-08-01 00:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 9624b8ee-d19a-3a4c-90ca-e02b6be5653c | -11.2399 | -54.8737 | 2026-08-01 00:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 375.4 |
| bcd0775c-04c1-378d-9a82-b349ff4c0872 | -3.0612 | -39.9346 | 2026-08-01 00:50:00 | GOES-19 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 52.4 |
| ecaedbb7-e446-3ea8-9ba2-11e1990f677c | -14.0735 | -46.2439 | 2026-08-01 00:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 6f4144b6-38a5-3b9f-9368-4fffe07eac5a | -14.073 | -46.2669 | 2026-08-01 00:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 80.0 |
| cdaf772c-1b2e-306e-a70d-9134d80d8562 | -11.4284 | -50.6075 | 2026-08-01 00:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 530c6116-5e56-3eaa-9e8f-3ddea59460de | -6.7555 | -41.0103 | 2026-08-01 00:50:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 125.0 |
| 4059399e-67fb-3c15-a5c3-a00a0f969bc3 | -6.7744 | -41.0084 | 2026-08-01 00:50:00 | GOES-19 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 131.9 |
| 76600f8b-16ca-37ce-a815-ada1793d40d2 | -11.2588 | -54.8721 | 2026-08-01 00:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 280.0 |
| 0ee96385-0800-3e78-866e-0bb8027c7ddf | -11.2591 | -54.8517 | 2026-08-01 00:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 274.4 |


[Clique aqui para ver as próximas entradas](README3.md)
