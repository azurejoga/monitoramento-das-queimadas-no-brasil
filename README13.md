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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0f7e52e-60d6-3ae1-af06-4da18fb5e882 | -13.03958 | -47.81649 | 2025-07-14 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63e5d126-c8a6-386d-84c7-ded1df604ad6 | -8.04836 | -50.1001 | 2025-07-14 04:51:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ded6d9a-8261-3870-b441-45b17feb52db | -6.63012 | -56.28595 | 2025-07-14 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6670e4c-4a3e-32ae-8abe-fb42d52a5e31 | -13.03517 | -47.81593 | 2025-07-14 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0da0feb6-12c1-3552-8f0f-95fdc9873656 | -9.51156 | -47.57002 | 2025-07-14 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3369dc84-8ce0-3afa-86a5-6a0f9b8b6d07 | -8.51885 | -43.30378 | 2025-07-14 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 769443c4-e08a-3be7-a6ea-4f4c331a3312 | -10.56846 | -49.12801 | 2025-07-14 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8078030e-ee2f-32f1-9071-8072ee14481d | -9.02355 | -61.22989 | 2025-07-14 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6eb5704a-d503-39cf-b061-a8b4b1601622 | -10.98703 | -47.09234 | 2025-07-14 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38fb3736-f0ff-3bb5-af79-b5f30e3c8692 | -8.03836 | -50.09352 | 2025-07-14 04:51:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 318b4073-3b8d-3862-bd3d-6ec4b7f556d8 | -8.04546 | -50.09502 | 2025-07-14 04:51:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b98b8079-6b28-377a-af6a-2a438f4552ea | -8.04242 | -50.11531 | 2025-07-14 04:51:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 435afc54-9030-3f52-934e-46a8baf0342f | -11.71466 | -47.03757 | 2025-07-14 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af2dc791-597e-3f86-ace5-5fd83075ad7b | -8.87722 | -46.91137 | 2025-07-14 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e221839e-ca32-3e7e-a175-867c8066c77a | -8.59553 | -47.30987 | 2025-07-14 04:51:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 345e7f48-a372-394e-8728-411a38a31702 | -8.87331 | -46.90883 | 2025-07-14 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a799cab9-2030-3d6b-8465-867fef1fee2a | -8.50762 | -43.30228 | 2025-07-14 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 3254709f-b788-33e0-9226-8d459ad050cc | -8.5104 | -43.31048 | 2025-07-14 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 57d190b0-359d-37d3-83ce-da234f6399fd | -8.04481 | -50.09933 | 2025-07-14 04:51:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 304d8554-1d08-32dd-8a22-8d569242e408 | -8.50577 | -43.30206 | 2025-07-14 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 9dd3effd-d36a-3d16-8ae7-5436c4cd5e5a | -10.27733 | -47.61341 | 2025-07-14 04:51:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f2c9a033-39dd-3610-9801-d8c5d9917e82 | -8.51089 | -43.30666 | 2025-07-14 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 17dfa3fc-a99e-3621-8f63-0b5df1f7e121 | -11.02743 | -47.08088 | 2025-07-14 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bee0a13c-2f8d-3f51-8f4b-3bf7a7c16f82 | -8.87782 | -46.90693 | 2025-07-14 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c68437d1-708f-3357-bdd2-b05a6c892128 | -11.58225 | -47.32548 | 2025-07-14 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d1108672-41aa-3016-85e4-276685a8792d | -13.02208 | -47.81308 | 2025-07-14 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd0457fe-527a-3d60-b44f-2938ce315662 | -10.28591 | -47.61469 | 2025-07-14 04:51:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 062870dd-813d-3ddf-a15c-c206ce972b80 | -6.62645 | -56.28535 | 2025-07-14 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e46c37ef-2a38-343a-b444-6b36111dd612 | -8.5998 | -47.3105 | 2025-07-14 04:51:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ce6b8eb-c759-3fce-afe7-ab8dda18d19f | -11.03379 | -47.06753 | 2025-07-14 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb88a0f7-1898-3c02-81b4-756a2e99b7e7 | -10.56917 | -49.12306 | 2025-07-14 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 685bf543-2a1c-3f0b-8ebd-ea0eb137d1f7 | -9.49084 | -47.56281 | 2025-07-14 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7ed29b2f-2110-3b57-a721-78818caed9c3 | -8.87394 | -46.90439 | 2025-07-14 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2538923-179d-3e61-94a3-19610f982bce | -8.50528 | -43.30588 | 2025-07-14 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 84b23778-d04a-3dba-ba81-992e4a20fe0a | -8.04253 | -50.09016 | 2025-07-14 04:51:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| f9d465ea-b6d0-3acb-8e13-d5e88ad031e0 | -11.71735 | -47.05225 | 2025-07-14 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a772d174-50ac-332c-ab7c-58d1fea80d6c | -12.10576 | -46.43566 | 2025-07-14 04:51:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdd5e3da-ca0b-3be6-8ff7-fe327cea7b8b | -11.58286 | -47.32101 | 2025-07-14 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f9fe65bd-fd43-371e-8d2a-19789cb97fa2 | -8.04902 | -50.09575 | 2025-07-14 04:51:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 948a7742-9fa2-332a-b4e7-1104f757e1de | -10.27317 | -60.54847 | 2025-07-14 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f117a81a-b205-32fa-9e39-f90e700c2067 | -8.04658 | -50.11195 | 2025-07-14 04:51:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15c7e5d5-439d-3976-879c-537ddba0401b | -10.57237 | -49.12858 | 2025-07-14 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74dad2ba-5713-33b5-b91c-67eb72496f8f | -9.49936 | -47.56407 | 2025-07-14 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b1dfe545-c042-30b3-b62a-0332cc8d3a7b | -11.86356 | -58.70292 | 2025-07-14 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0be18036-494c-3cb5-9d63-546da44a5055 | -13.03901 | -47.82073 | 2025-07-14 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c02eb51f-8866-34f7-bb4f-f7ad2dc803a2 | -10.39482 | -46.67328 | 2025-07-14 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc725683-0ad8-351b-b049-7d4bbfb45506 | -8.86568 | -46.86749 | 2025-07-14 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77921f2b-209c-39d4-b7d8-ac8af93b408f | -8.51937 | -43.29995 | 2025-07-14 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 5df588de-27d9-3fa2-b442-e4592eb09966 | -8.90894 | -47.35099 | 2025-07-14 04:51:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 88a3d55a-28d0-3024-aa40-ff5843f2a6c4 | -8.51833 | -43.3076 | 2025-07-14 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| ddc3c744-46c3-3d38-9ad7-f9435915c59c | -9.82628 | -60.75759 | 2025-07-14 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6846bf9e-ea9f-32cb-96b2-c2f7a2fc6c01 | -8.50658 | -43.3099 | 2025-07-14 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| a5ef7d4f-41aa-3987-b377-1d08f24fed64 | -8.43937 | -45.8059 | 2025-07-14 04:51:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7cb85e1-4480-3228-af50-6e064a9dd802 | -9.4951 | -47.56343 | 2025-07-14 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cdf33008-f8d8-387c-a9b4-c0fb059c59d3 | -9.28831 | -63.46959 | 2025-07-14 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da103c00-f54c-333c-8af9-608ecf859d89 | -17.2277 | -49.55788 | 2025-07-14 04:53:00 | NOAA-20 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| be233cc6-502f-3d18-92a9-84d925498e82 | -16.73202 | -51.76424 | 2025-07-14 04:53:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99249313-5ca3-33ba-9e21-c0882bbe3f4e | -16.73339 | -51.75732 | 2025-07-14 04:53:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 029e6ddc-0a28-3839-85ad-19ca49e58402 | -20.13921 | -50.72173 | 2025-07-14 04:53:00 | NOAA-20 | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 504a5ef6-8103-3b62-b3b0-4847c103f0e2 | -16.72914 | -51.76119 | 2025-07-14 04:53:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6fde47b6-9f63-319c-87c1-a81b2d5b1dbf | -20.13874 | -50.72547 | 2025-07-14 04:53:00 | NOAA-20 | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6d7900b6-7710-3df5-b762-2b9380538895 | -16.27942 | -49.96363 | 2025-07-14 04:53:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7464afa-c8e5-37e3-8074-033cead3edc5 | -14.49866 | -58.59781 | 2025-07-14 04:53:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0790dd5c-0a45-3c2a-86c0-745ecd1d9668 | -14.49492 | -58.5971 | 2025-07-14 04:53:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e646fca2-ad1e-3539-abd3-cdb13d23acde | -18.99983 | -49.47682 | 2025-07-14 04:53:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6994adc-f312-3e54-b014-27d41b2955da | -14.53158 | -58.91774 | 2025-07-14 04:53:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f4da275f-ec6a-388e-8e29-09910e0cfe57 | -14.49119 | -58.59639 | 2025-07-14 04:53:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1942395e-62aa-330d-a64a-fa01eaaca30f | -16.73278 | -51.76174 | 2025-07-14 04:53:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0d92eeb2-e14f-3b85-a55d-41078f96d861 | -16.35493 | -57.73281 | 2025-07-14 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| fe865888-e45e-3acf-ba0c-7a0804955f75 | -14.52777 | -58.91705 | 2025-07-14 04:53:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ef47ad7-1da3-3d1c-8aa3-0a43fbfe6d6d | -14.50239 | -58.59854 | 2025-07-14 04:53:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b63f69f-30b9-35e6-9080-7a55154de39e | -16.72975 | -51.75679 | 2025-07-14 04:53:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0fdfea5e-19aa-3fcc-8eaa-979380744606 | -17.90984 | -54.11834 | 2025-07-14 04:53:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1bc60cbc-3c11-3875-b61f-d32c8f8a4d0d | -16.72902 | -51.75931 | 2025-07-14 04:53:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c2049775-c2d2-352b-80a2-d13183a2d576 | -20.4767 | -53.67662 | 2025-07-14 04:53:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d3f0e51-e41d-3e06-a117-fd0591769114 | -16.35424 | -57.73682 | 2025-07-14 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 3c02a889-1c6e-39f8-a295-b7eb7ea4351d | -16.73265 | -51.75985 | 2025-07-14 04:53:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 86ff2950-1198-38e4-b8ed-35244a00aa41 | -16.72839 | -51.76368 | 2025-07-14 04:53:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4213f52c-8c40-3fd9-85de-82ecce1c324b | -23.08244 | -54.19186 | 2025-07-14 04:55:00 | NOAA-20 | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ef475a9c-bbbe-3750-99b9-47eb66fde5c5 | -22.67256 | -42.85653 | 2025-07-14 04:55:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f0971fc3-c63c-3572-9ac0-5a74beae1d41 | -21.89388 | -56.73434 | 2025-07-14 04:55:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51c88fce-e1f9-35eb-b831-6fdd21566d60 | -23.08593 | -54.19241 | 2025-07-14 04:55:00 | NOAA-20 | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2ca9b496-e5b7-3655-8d84-1283e8f4aa8c | -21.49182 | -54.27071 | 2025-07-14 04:55:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 69918851-70fb-39a4-9678-783140e46041 | -21.48897 | -54.26614 | 2025-07-14 04:55:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ca7595fd-41d1-3153-9437-2c7c8104a99e | -21.48554 | -54.26556 | 2025-07-14 04:55:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fa618f16-921a-3c81-8a13-077f430a2365 | -21.48496 | -54.26954 | 2025-07-14 04:55:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8d739212-8874-3096-b182-734ef9327a74 | -25.1928 | -49.32815 | 2025-07-14 04:55:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c3992b7c-85f5-3835-a462-50caa554d142 | -23.08304 | -54.1877 | 2025-07-14 04:55:00 | NOAA-20 | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1c309c15-3481-30ba-8f2e-9731523d3837 | -21.48839 | -54.27012 | 2025-07-14 04:55:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b8cdb743-d18d-335e-9573-4e43f400f166 | -28.12826 | -54.93934 | 2025-07-14 04:55:00 | NOAA-20 | ROQUE GONZALES | RIO GRANDE DO SUL | Brasil | 4316303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9a9f6cd8-5ea0-3f1b-8155-125917adc6c1 | -21.04388 | -55.98782 | 2025-07-14 04:55:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 627b042d-d53f-3989-bb42-85a9b27341b5 | -30.05144 | -56.17281 | 2025-07-14 04:57:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 0.1 |
| 175cb6bc-3072-3eeb-b57f-ac0d5411da9e | -30.04738 | -56.17649 | 2025-07-14 04:57:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| da64d13c-45aa-35b7-ad83-8145228bc040 | -4.5112 | -38.53937 | 2025-07-14 04:59:00 | AQUA_M-M | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 14.2 |
| f6b95d75-b6af-38a1-bbbc-f05478a0bad8 | -5.15908 | -37.67962 | 2025-07-14 04:59:00 | AQUA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 52aad43e-6f77-3d57-aa18-aed0b3dd0e2c | -4.50903 | -38.55316 | 2025-07-14 04:59:00 | AQUA_M-M | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 10.7 |
| cf24b43d-bf16-3fcb-a2e2-4c431ace3a36 | -8.5211 | -43.3063 | 2025-07-14 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 8dfc28c0-6284-37db-bcf4-5a9bfe5d8d7a | -8.5022 | -43.3085 | 2025-07-14 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 51.5 |
| b6ac87e7-55a0-367d-8f45-a3a5e024cf9e | -9.48536 | -40.38716 | 2025-07-14 05:01:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| c79086f8-eb11-3e94-af4c-a852cafa8687 | -8.49896 | -43.31258 | 2025-07-14 05:01:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 30.4 |


[Clique aqui para ver as próximas entradas](README14.md)
