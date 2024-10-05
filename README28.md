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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83522a87-a0ad-3ff2-9472-daa52b1a67df | -17.08049 | -56.79987 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| fb4ecb12-f47d-3a01-9919-1324c6f6168f | -17.07879 | -56.78871 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.8 |
| 77452b77-9c31-33e2-acf6-3ba07aa36739 | -17.07709 | -56.77754 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.7 |
| 30736083-4f5c-3111-bd02-2fb0961dff0a | -17.07538 | -56.76636 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| fcd8bf3c-c218-3e2b-b88b-d1ec2baef3a3 | -17.07082 | -56.80151 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 95e20c96-cb05-3cfd-98a9-246e9bc0bb61 | -17.06114 | -56.80317 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 6c7f9b91-d915-302b-8c56-4c83e1fb0d4c | -10.13711 | -56.76239 | 2024-10-05 01:49:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 47516784-a552-3499-8f0c-4eb6f8e10956 | -10.12627 | -56.76407 | 2024-10-05 01:49:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 72814a49-0e69-3143-8ff8-793615b09183 | -14.80865 | -58.57901 | 2024-10-05 01:49:00 | TERRA_M-M | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d9435a24-fe9a-3742-9381-9bc3a036e486 | -14.92612 | -57.93609 | 2024-10-05 01:49:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c1d5ec09-cc26-3c7f-be8b-cb8056680cde | -14.86636 | -58.02555 | 2024-10-05 01:49:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 930d4c74-36e6-310a-8fb0-76882efcf67a | -14.86481 | -58.01505 | 2024-10-05 01:49:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b504bd17-537b-3361-b777-ef26b304ed6d | -15.10966 | -58.36236 | 2024-10-05 01:49:00 | TERRA_M-M | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4932a1b9-f636-38c0-a149-3965cd01f797 | -15.38945 | -58.14116 | 2024-10-05 01:49:00 | TERRA_M-M | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 7c0f9aad-1e76-34e6-8486-babe3ed7282e | -15.26928 | -58.19286 | 2024-10-05 01:49:00 | TERRA_M-M | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 904facee-2e04-32b2-954b-4be597b0af6b | -16.54577 | -58.22272 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| ca5ff8e0-1c61-3cfe-a44a-47475054691e | -16.54435 | -58.21299 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| fd2b3f64-4d1a-37a1-90e9-1c01b4a58b97 | -16.53667 | -58.22422 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| cab9e44f-0dad-3aa0-99d4-599f8a55cef2 | -16.53524 | -58.21447 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 9f9ae8f8-0620-35f3-b722-629a110c2f7b | -14.78453 | -59.43265 | 2024-10-05 01:49:00 | TERRA_M-M | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 43e2b047-7030-38f3-b35c-ee9cec97c72c | -9.27774 | -60.83201 | 2024-10-05 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 815fb374-308b-3861-90cd-8c44d8adf3f7 | -9.26929 | -60.5049 | 2024-10-05 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 119254db-df98-3dfd-8d54-a4990eee4326 | -9.268 | -60.49583 | 2024-10-05 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0d7b7198-74c5-3128-aba7-42a3d0b16015 | -9.2667 | -60.48675 | 2024-10-05 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 42a1be0a-c7e1-356b-82bc-f1fa825f853b | -9.26541 | -60.47766 | 2024-10-05 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d936487b-ac53-399d-8677-112a07d50ba6 | -9.24986 | -60.50485 | 2024-10-05 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7267014d-91da-3803-b589-5729953a3d16 | -9.16831 | -60.50758 | 2024-10-05 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4d8486a4-fa1d-3f6c-a18a-681cb3bb8e06 | -9.15918 | -60.5149 | 2024-10-05 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6e8e3d58-239b-35e6-80d6-ea1ebd30ef12 | -9.95072 | -60.11263 | 2024-10-05 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8a253d5f-f66d-33e5-9696-2315d4ecea01 | -9.48375 | -60.39624 | 2024-10-05 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fab71ba0-fc1a-37a9-bad4-2589e2f94baf | -9.42627 | -60.37683 | 2024-10-05 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f8f68fa3-d967-36b3-8b35-4fa95f3ed1db | -10.37829 | -61.18187 | 2024-10-05 01:49:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 53b9958d-bfd5-3372-9b62-c838f9840270 | -10.37705 | -61.17293 | 2024-10-05 01:49:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ddc14635-dbc1-345a-9897-a524f731f0b0 | -11.33118 | -60.55441 | 2024-10-05 01:49:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b9d14e78-5ec6-3111-ace6-2a5d270a1d85 | -11.27584 | -60.62387 | 2024-10-05 01:49:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5c33747a-86d1-36a4-a46b-4ae1ac9f285a | -11.2708 | -60.58798 | 2024-10-05 01:49:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 14.2 |
| f1a3ca8f-6dcb-3d6a-991d-0d7bc965ae8f | -11.26195 | -60.58931 | 2024-10-05 01:49:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 8c7c6a2f-959c-378d-bec4-48b9850e0ee1 | -11.26069 | -60.5803 | 2024-10-05 01:49:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 434e0ebc-867b-3799-bf9b-3736470bf25b | -11.25437 | -60.47098 | 2024-10-05 01:49:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 128d2222-94e3-3a02-98c1-a22d1e2c6ed9 | -11.25055 | -60.37953 | 2024-10-05 01:49:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c18fc1cb-249a-3434-a2b2-b257d6db0558 | -11.24928 | -60.37053 | 2024-10-05 01:49:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ca309b8e-46e4-3cd2-8e7c-359acb38be77 | -11.24424 | -60.59186 | 2024-10-05 01:49:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9286739b-aca4-39de-9d54-d0cd88f0b51d | -11.24298 | -60.58289 | 2024-10-05 01:49:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 3365094f-0e8f-3537-941e-1d671f0bbfbd | -11.20501 | -60.50583 | 2024-10-05 01:49:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 75adeeac-7b3b-39c4-bba6-b00115c1880a | -11.20446 | -61.22594 | 2024-10-05 01:49:00 | TERRA_M-M | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e6a45d5c-38bb-329e-901b-ce724936fec4 | -11.19326 | -61.28883 | 2024-10-05 01:49:00 | TERRA_M-M | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3e736268-d208-3dc8-9915-308aec982a6d | -11.1844 | -61.29012 | 2024-10-05 01:49:00 | TERRA_M-M | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b58055fd-4583-3b32-a3ce-fe3067d0aa0e | -11.00017 | -61.42081 | 2024-10-05 01:49:00 | TERRA_M-M | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fb9e50c5-6f46-3b04-8e28-0b6c57696f2c | -9.17951 | -61.57718 | 2024-10-05 01:49:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 6fb36b84-0aaa-3f54-bb74-0f2b1b1d96c7 | -9.17783 | -62.29866 | 2024-10-05 01:49:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d0364540-38cc-31b3-bd79-a46b115b1889 | -9.17066 | -61.57846 | 2024-10-05 01:49:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 22.7 |
| a4fbbf7b-d403-3bc7-a092-ad7570b8d104 | -9.16943 | -61.56954 | 2024-10-05 01:49:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 3e08caf0-79d9-3c25-a0c5-45d2d23babbd | -9.09092 | -61.13592 | 2024-10-05 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 60aa0923-85b9-39ac-9226-1f6c558a950e | -9.07924 | -61.38866 | 2024-10-05 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 40cae900-f08c-31bc-92e3-7273c385e28f | -8.84706 | -61.49789 | 2024-10-05 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 058970c0-131d-3cdc-8da3-ac72d7772237 | -8.2266 | -61.2224 | 2024-10-05 01:49:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 8c7de768-bc99-35c6-821e-7910fea9576b | -8.22536 | -61.2135 | 2024-10-05 01:49:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 064aa2e5-72f3-3023-a344-5e0aefc6d982 | -12.85333 | -62.80925 | 2024-10-05 01:49:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 994c3fc7-b86f-3e5d-883c-2bf1578ce7e9 | -12.85198 | -62.79898 | 2024-10-05 01:49:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 19.7 |
| a2c791a2-6e98-337b-bcb0-6bd3cfa5ff9f | -12.84257 | -62.80029 | 2024-10-05 01:49:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9a754ed6-a63f-3160-ae88-80c4233c4799 | -12.72209 | -62.9491 | 2024-10-05 01:49:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 66d77388-0b68-3299-8672-35884416c7f4 | -12.71779 | -62.95601 | 2024-10-05 01:49:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| cffc6965-e514-3fa3-9422-6d135b6b3643 | -12.7164 | -62.94561 | 2024-10-05 01:49:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 88993a59-d91b-3cb1-bf33-9e0be352309c | -12.71502 | -62.93523 | 2024-10-05 01:49:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5bb3a43b-d211-30d0-b17a-e849a8205e50 | -12.64511 | -63.09988 | 2024-10-05 01:49:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 289e5b30-7d97-33a7-afe1-7766a023902c | -12.63558 | -63.1012 | 2024-10-05 01:49:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 933a1230-6cd0-3a0b-8089-81285ef38a1a | -12.63418 | -63.09067 | 2024-10-05 01:49:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b4aa5fbe-8707-3f8c-be6b-a99a0dae6165 | -12.62883 | -63.12366 | 2024-10-05 01:49:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 558fcbf5-0b44-3a6f-92fd-72fc7eb22936 | -8.83582 | -63.03231 | 2024-10-05 01:49:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 43c96da8-9e8d-3e98-a43d-1db1ac0d7f84 | -11.99073 | -63.53838 | 2024-10-05 01:49:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c784dda8-de02-3c2b-9022-99b5b4e24b66 | -11.98932 | -63.5274 | 2024-10-05 01:49:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 564ebbc2-c203-350b-b1d5-c88b2a5590f3 | -9.28376 | -65.42059 | 2024-10-05 01:49:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 7b91eb1a-25a5-36e6-a60a-a241cfc4cd9a | -3.83865 | -52.36483 | 2024-10-05 01:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 2dc7372f-59c6-3723-8dae-c7b05bfcf22b | -3.81048 | -52.40834 | 2024-10-05 01:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 44604bcd-5131-31cc-9f8f-56938690ddc2 | -3.10178 | -59.3694 | 2024-10-05 01:52:00 | TERRA_M-M | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 33c61a57-2847-366c-84ae-9a8d5bb9457c | -4.28805 | -60.01867 | 2024-10-05 01:52:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| f4185f6c-77c8-37ad-ae2b-4550dd801da2 | -3.87059 | -59.74094 | 2024-10-05 01:52:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ae3a7282-b4f1-3d2e-adfd-d574c73d4a17 | -6.95124 | -59.89038 | 2024-10-05 01:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d666dd32-2b32-3c53-9db2-c1bb5c926659 | -6.82727 | -60.06318 | 2024-10-05 01:52:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a2bfa3a2-959d-3acf-9eed-1f71ab05e91a | -6.81807 | -60.06451 | 2024-10-05 01:52:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| e191b78a-1647-3b4e-9df4-e5f0f354edde | -6.81667 | -60.05482 | 2024-10-05 01:52:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| f74451c0-d6f0-3d02-aaff-2971def12c4d | -6.71297 | -60.10593 | 2024-10-05 01:52:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4909d561-b677-3629-ae83-9fa59c799cda | -6.70497 | -60.10312 | 2024-10-05 01:52:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5792ca57-ab7a-33ad-a73c-6214aca82460 | -6.65066 | -60.05183 | 2024-10-05 01:52:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0eb5ed45-42ae-34ea-b6ca-03a0c1d2e499 | -6.64004 | -60.04349 | 2024-10-05 01:52:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 427f1ae1-a72b-38e9-8194-d1f3bbfbfe9d | -7.20444 | -59.61586 | 2024-10-05 01:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8c485081-50ae-3bf4-9ccd-9a0f02532c97 | -7.14857 | -59.30134 | 2024-10-05 01:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 90129b0f-ee7a-3879-bad9-23b78783b98c | -7.01842 | -59.40693 | 2024-10-05 01:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 6a0b2430-ba4e-3344-95d6-beceb2836c55 | -7.01693 | -59.39666 | 2024-10-05 01:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bd49a1c3-a481-39c5-ae4f-247f02a8a5b8 | -7.01544 | -59.38636 | 2024-10-05 01:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 93a1e6f2-8918-3fd7-a023-82f2751f904f | -7.97431 | -61.39486 | 2024-10-05 01:52:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 01c994ef-a4cc-3bab-8e01-780533918007 | -7.93161 | -61.28316 | 2024-10-05 01:52:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 71921acc-6eb6-396d-ac85-83e2c8ad3090 | -7.93036 | -61.27427 | 2024-10-05 01:52:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.9 |
| dddb85db-0124-36b8-8642-53ae5605c7a1 | -7.92151 | -61.27554 | 2024-10-05 01:52:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dc2f0adc-9522-36b0-ba5c-e034e786c16d | -7.89222 | -61.46729 | 2024-10-05 01:52:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 3d7c6a7e-8128-3a6a-a2a7-1a98041c86e6 | -7.89099 | -61.45841 | 2024-10-05 01:52:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 1da7fbcf-26e9-3952-8c79-5b8b2c5aac89 | -7.52388 | -63.27162 | 2024-10-05 01:52:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8e862806-6dd0-3c4a-a2c5-ffc5c5e043bc | -7.5226 | -63.26214 | 2024-10-05 01:52:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| ed8d3444-313b-302b-b06f-abf6dabd6e44 | -6.97891 | -62.91981 | 2024-10-05 01:52:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 04d7405f-2710-3221-b9a7-164dbed1df6a | -6.97765 | -62.91066 | 2024-10-05 01:52:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README29.md)
