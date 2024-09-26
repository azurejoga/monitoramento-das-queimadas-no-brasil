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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f5130b7-8dfa-3575-8e62-bb758e6815eb | -11.94161 | -60.36978 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| deb01c15-1a2a-3ca8-a195-f0387b3a8ebd | -11.94101 | -60.37325 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8f1de59c-8a4e-3ef1-8e73-d29484ea4872 | -11.9398 | -60.38013 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7486685b-1213-303b-9b22-69118e1dcc74 | -11.93765 | -60.36906 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6112206c-5fcd-3a43-b0d7-a6301c22fbe2 | -11.93704 | -60.37255 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 758a2ec0-3334-3263-86b2-deb1d616f273 | -11.93583 | -60.37947 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9fca2e46-0a51-3789-9a64-c305c65caee2 | -11.93522 | -60.38292 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dcb62002-4322-3222-bb35-3509564357b7 | -11.93401 | -60.38981 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd6a371c-fc9b-3837-ae53-e2b0dad0c04b | -11.93341 | -60.39329 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e604c131-849f-38a6-8429-5c7a47dd6a2b | -11.90847 | -60.23413 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 753ca688-c954-3acd-8e15-17906426574a | -11.90637 | -60.22314 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6d6de37-074b-321b-a5ed-1d5f85c071b7 | -11.90628 | -60.22643 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0759ffd-e929-3eb9-9040-02038f48b00a | -11.90546 | -60.22824 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 296c3b04-67f3-3138-93b1-2c4789f405fb | -11.9054 | -60.23155 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 882c623d-ff6b-38f5-8b06-c61452c6d5fd | -11.90454 | -60.23337 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c1d6a8b-bb88-37b9-9136-9e6aef93b16c | -11.90365 | -60.44576 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ea9bbaa-c30f-38c4-88a3-780e6deca31b | -11.80896 | -60.29472 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa77067f-4d12-31cd-827a-82e104b5bb25 | -11.73337 | -60.33816 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19c19876-ad91-3c49-ae4f-096589df2bde | -11.6721 | -60.22762 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 674a969d-be43-3ae7-ab30-cadd5fecb704 | -11.66905 | -60.22172 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12d13770-2e2a-3245-91a4-b19c7bb2c7df | -11.66075 | -60.1991 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 62343fe2-382e-3c9c-a744-ffcab4e814c7 | -11.66007 | -60.27386 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fecf6897-95d0-37f8-b95b-521f93567e0c | -11.65931 | -60.27825 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a737b0fa-bb89-3f45-8083-187a8f6446d6 | -11.6568 | -60.19844 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9e258ec1-796d-376a-8f1a-8cedd908d4e2 | -11.65535 | -60.27754 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0a55606-1468-3979-b066-777dbe0937db | -11.65474 | -60.28104 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7410cda5-39b4-306b-8c44-cf9bfdd3f533 | -11.65153 | -60.18194 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4eca944a-725e-396f-bd6a-2e7635f396ac | -11.65078 | -60.28033 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4d0065a-e5cc-3306-ada1-01bfc2a36cc6 | -11.65018 | -60.28381 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 973103d7-54c1-334c-a494-f21924ef9c40 | -11.64622 | -60.28307 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b49920c9-089d-342c-8219-122a66ce5d1b | -11.64167 | -60.28575 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d56f963-9153-3cda-a3e3-c60f8c384d55 | -11.64107 | -60.28923 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2a52102c-c8de-3440-b3fb-594df98d58ae | -11.64021 | -60.31777 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9fa4f4cc-c6af-35c1-bac4-8cf85a3b4620 | -11.63625 | -60.317 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d907956a-c000-3478-bc36-bd945eb59df8 | -11.63376 | -60.33131 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8775521-ded4-3f99-95c8-a36b41abca32 | -11.62917 | -60.33415 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4930f49-6012-3a07-aaa2-70ac7beb44b5 | -11.62859 | -60.29039 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee2568ae-1b55-3eb4-be49-4e7f15f78c64 | -11.62737 | -60.39185 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f58be64d-0abb-3cf3-a48c-e456839ea4b7 | -11.62676 | -60.39535 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af35ca8d-62eb-3e83-b539-0411491dde4a | -11.62462 | -60.28972 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 016156be-a0be-329e-bf58-7c27db9b15eb | -11.62338 | -60.3911 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e06b1fd-bff8-3741-af76-05fd121ec482 | -11.62125 | -60.28557 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25d507e1-7fee-379f-a0c5-16e15c4dbe71 | -11.61999 | -60.38694 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33607324-0d8d-3fff-aaf0-2011f1320400 | -11.61938 | -60.3904 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44c913e5-996f-3bb9-a383-69da225effa7 | -11.61877 | -60.34675 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a13d934b-654f-38d0-81c6-9002b8ea2064 | -11.61598 | -60.3863 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fffa1186-49a3-3024-b7d5-ce712994dbc1 | -11.61544 | -60.34228 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9012e08-9437-3755-9c44-1e0d8274adf8 | -11.61538 | -60.38977 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dcf80109-9664-3db8-a9e6-a9f2e892f771 | -11.61482 | -60.34583 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a0cbca1-4e53-37ff-bd5b-6eaa8d7689f3 | -11.61421 | -60.34933 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6adb5a9d-9d6f-36e9-8a8b-91047d36176b | -11.61392 | -60.28071 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8152299-0b7b-3223-b08f-52b49a282d81 | -11.61149 | -60.34139 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac381e74-2e93-30ef-8424-0899213b3e04 | -11.61137 | -60.3891 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d321a73a-bd40-3fc7-88a1-5f48040dd495 | -11.61087 | -60.34497 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 849c2013-0ec2-33cf-ac13-987d01994fe9 | -11.61077 | -60.39257 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c5137877-b3b9-38e0-938c-e499660fc133 | -11.61026 | -60.34846 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e063ee24-8cf1-3581-ad75-66f7b6ada628 | -11.6069 | -60.34414 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92c10de5-2fb3-3983-a9d0-3fdd6f0f0831 | -11.60629 | -60.34763 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34d1f925-5c43-3651-858d-e67506403d96 | -11.60569 | -60.35107 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4393f32e-b30b-3cc3-bd40-19d3f6258efe | -11.60508 | -60.35455 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 46219280-0849-3c4d-a5b1-d429628d6170 | -11.60445 | -60.35816 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 77a7e40d-889a-329e-b7fa-912e40c2cc3c | -11.60381 | -60.36181 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0aaa415a-c951-3274-a2de-64a8544c955c | -11.60293 | -60.34338 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab6b82fa-cd38-3c5e-90f3-5ee6533f35d7 | -11.60231 | -60.34691 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ea22989-b9cd-3645-b2ae-dd16b4ed3b56 | -11.60171 | -60.35037 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 188c703a-72f1-3dfc-bfcd-a9f9bde4c3d8 | -11.6011 | -60.35384 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5d14ab02-4848-3e9d-a72d-5d4ccf7463a5 | -11.60046 | -60.35748 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b3e42139-5152-3463-abcc-79c66aa1f6b6 | -11.59981 | -60.36117 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f5bdf887-f351-3b0f-a41e-b7062d4c40f0 | -11.59894 | -60.34275 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 957e18c1-9b07-38d1-a10b-1f1e1cfba604 | -11.59806 | -60.27789 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14357499-297a-30b3-bc16-79c64a275758 | -11.5971 | -60.3532 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4935ffc1-1a91-3f6d-b726-ad02e72f83dc | -11.59432 | -60.34562 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9e1dd39-ba5d-3110-a349-899fa9385e55 | -11.59408 | -60.27723 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a03b77f9-6218-3f34-8702-cfb13f7d2b27 | -11.59371 | -60.34907 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| baf73a35-16df-3591-918a-a73cdd91f560 | -11.59311 | -60.35252 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8fcf4d7f-5bd9-3409-97b0-1da51268e794 | -11.59056 | -60.36699 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b97dcaea-b7d4-3f6f-b986-78617809097c | -11.58992 | -60.37059 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40e81aa4-4be0-3ab9-9a45-28c0bfe5b77b | -11.58973 | -60.34838 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 722e00c5-0e71-3275-8271-cb35e47644e9 | -11.58071 | -60.37616 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| edb14fd3-8ef1-3700-9d67-40abb6110ed2 | -11.57672 | -60.3754 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ccdc1b85-acb6-3235-a4c1-6026a856f965 | -11.57208 | -60.37837 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5341ac3-211c-3872-a6b0-4d8dce4ad932 | -11.57097 | -60.3017 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c18242eb-0d01-3dc1-b1d8-afba8943f43b | -11.56926 | -60.30171 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c80f6135-ff7e-3751-b050-20240de5091d | -11.56665 | -60.2791 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e5be28ff-7d19-38ee-a71b-0695f8a64a4a | -11.56026 | -60.17392 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 75f7704b-aea7-3468-8600-93818b429add | -11.55455 | -60.18339 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 64cf3e79-6338-3e7d-8cc6-be92f98e2bb9 | -11.5533 | -60.1671 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8a3bfb94-c7c5-3d3d-bdda-5752525afb5f | -11.55241 | -60.17229 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f6808147-c4cb-3956-a272-94dc51dad2cf | -11.55151 | -60.17749 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b8512d82-73db-39b7-af90-405f94b2a58d | -11.54938 | -60.16629 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ccbd5f2c-7f66-36c5-ba63-252566948830 | -11.54545 | -60.16552 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14d8879f-35c0-39e9-894c-9cebcf2f32da | -11.54151 | -60.16483 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f202c049-2893-394d-bd3c-1dabc63d9e20 | -11.53756 | -60.16416 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e66573a2-8d9f-38ed-94ce-c3983029441c | -11.53505 | -60.41529 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c6b18bc3-5c52-3d52-9001-05371a91c207 | -11.53444 | -60.41887 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e98c8d0b-347e-306c-b05c-4051c29186d6 | -11.53362 | -60.16344 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| abd44835-42d5-3ff2-b2c0-41e89f19cb2f | -11.52485 | -60.16714 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 93a8f975-0635-32ff-a567-16412e1cdf82 | -11.524 | -60.24203 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7833110b-4950-36d4-9344-f30270abd2ff | -11.52394 | -60.17231 | 2024-09-26 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 74e48482-12e4-3d6b-b29a-69bd40c4c2f8 | -12.14729 | -60.91435 | 2024-09-26 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README138.md)
