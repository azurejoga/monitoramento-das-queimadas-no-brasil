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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31a489dd-75be-3cf5-85d1-820456bcf716 | -2.1562 | -53.7039 | 2024-11-16 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 180.8 |
| 935d54fd-1623-35ea-8ebb-995990b36ff3 | -16.9384 | -57.6291 | 2024-11-16 01:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.9 |
| 526f782e-96c3-3ff0-bcd6-c305d86487d8 | -2.1575 | -46.5747 | 2024-11-16 01:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| b7f97cf1-dbd1-39b8-9074-b91fef0358b3 | -2.1562 | -53.7039 | 2024-11-16 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 159.7 |
| f53fb102-34be-396f-9d89-88955e07e316 | -2.1379 | -53.7043 | 2024-11-16 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 123.7 |
| aeaa91c5-1b83-3cd8-a5b0-2fe3a55f2458 | -2.1378 | -53.7244 | 2024-11-16 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 8a9ee153-f1f4-3514-921d-ca509747c5c6 | -2.1576 | -46.5527 | 2024-11-16 01:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 190.2 |
| 0a9ad7fe-20c0-3b75-b0dd-0064fc121e57 | -3.7393 | -45.6747 | 2024-11-16 01:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 62aca3cb-bab9-323a-8fe1-411543cc24bd | -2.5642 | -46.8938 | 2024-11-16 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 58c6d08a-ce7b-3388-bb83-eec097371a19 | -3.1501 | -53.2371 | 2024-11-16 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 38d4df44-7baf-3ec9-a1f2-46f77da6616a | -3.5851 | -50.5255 | 2024-11-16 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 1245d93e-7b02-3800-9a9f-d356bc913970 | -2.1562 | -53.7241 | 2024-11-16 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| c0807d42-6ade-3c29-a88b-d64662494173 | -16.958 | -57.6269 | 2024-11-16 01:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 126.4 |
| b3709865-1ab2-3cbb-99ca-13c33fec10f1 | -2.7986 | -48.5586 | 2024-11-16 01:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| af3867de-71af-38fa-bcbe-5a7ede3f5291 | -3.7394 | -45.6523 | 2024-11-16 01:20:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 47fb6b61-3f2a-3f39-847b-dbbc50a80b9b | -17.3126 | -57.5039 | 2024-11-16 01:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.8 |
| 1f02db4e-0475-35e9-a87b-100e368f8211 | -4.9971 | -44.3149 | 2024-11-16 01:20:00 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 7cadd6e7-9433-35a4-96fa-f4d882aa4660 | -3.5439 | -51.4844 | 2024-11-16 01:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 5b00d9c9-e771-3cb6-b74a-b9169fa15589 | -2.1391 | -46.5531 | 2024-11-16 01:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| e40c9cdd-d664-3c52-9639-4ef9c51de872 | -3.7208 | -45.6531 | 2024-11-16 01:20:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 28d4e89e-1879-3a4b-9a30-d5f29b051e34 | -2.9674 | -47.9931 | 2024-11-16 01:20:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 5f3853a8-8ecf-3e0d-9231-7316b965d367 | -17.5882 | -57.4711 | 2024-11-16 01:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.4 |
| 7d526e20-9744-3037-9ca5-f669dc665b0c | -17.5879 | -57.4917 | 2024-11-16 01:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.5 |
| 82419418-6a6d-35ea-898c-8c795dfd10bf | -3.7685 | -50.7908 | 2024-11-16 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 284eff47-31e6-3fbd-9469-80f49170814b | -2.651 | -48.477 | 2024-11-16 01:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| d1ea5b71-868c-36df-ad98-8cc40d8caeed | -16.9577 | -57.6473 | 2024-11-16 01:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.4 |
| e50c74ba-005f-35bd-ab15-9d099c9dc20a | -5.6796 | -35.6418 | 2024-11-16 01:20:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 61.4 |
| ad8a52d0-6e72-310f-9b3a-4cdb16717db6 | -3.6255 | -53.9912 | 2024-11-16 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| b50a8424-b7a6-33db-ae7e-d99b374e59b9 | -2.1562 | -53.7241 | 2024-11-16 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| bc82a664-1a19-3a64-a9bc-6fd4919cdb38 | -2.1562 | -53.7039 | 2024-11-16 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 133.0 |
| 8bf28545-3ddc-32c1-9984-f17c71d6fa69 | -2.1576 | -46.5527 | 2024-11-16 01:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 576f6b89-8de8-361e-b8a5-2f7af043dac2 | -16.9384 | -57.6291 | 2024-11-16 01:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 125.8 |
| e8fa7702-52cd-3335-b556-a552aa725cbf | -5.6796 | -35.6418 | 2024-11-16 01:30:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 62.5 |
| b4da477c-06f6-3d85-bdc0-e61ff141c349 | -3.7685 | -50.7908 | 2024-11-16 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| e5cc3896-b285-32c0-a65d-c77b16d5ea6d | -3.7208 | -45.6531 | 2024-11-16 01:30:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 157.7 |
| 795528ae-2d3b-300b-a435-3ef76b467842 | -3.7207 | -45.6755 | 2024-11-16 01:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 983ce262-f1e6-393f-bf05-11e11b7fe4bc | -2.9674 | -47.9931 | 2024-11-16 01:30:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 1b03c8c5-ec85-331a-9e62-ea1979f167a8 | -2.1746 | -53.7036 | 2024-11-16 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| af49c226-d94e-3362-9d6b-6f2a3548c7e2 | -3.1501 | -53.2371 | 2024-11-16 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| f7751427-cb52-3dfe-a9eb-96931a023d40 | -3.1273 | -54.5264 | 2024-11-16 01:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| ad0c54e1-10a6-3fbc-9f66-b37cf164aeef | -17.5882 | -57.4711 | 2024-11-16 01:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.3 |
| 3462ee82-cf4f-3405-a7f1-b0e8d2b46261 | -2.5642 | -46.8938 | 2024-11-16 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| d64ab7b3-0890-3135-9392-002e0a9f2a27 | -16.958 | -57.6269 | 2024-11-16 01:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 126.0 |
| ba80283c-9cd5-3073-b8a4-49a6f9afcbd6 | -2.5456 | -46.8944 | 2024-11-16 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 9b0813f4-ca90-339f-9027-930cbafc6eb8 | -16.9577 | -57.6473 | 2024-11-16 01:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.8 |
| 1f69a0bd-0c7f-3c9a-a9a4-336956313b21 | -2.1391 | -46.5531 | 2024-11-16 01:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 2f93cd34-93f6-33e6-b10c-e6076a9e85bd | -2.1379 | -53.7043 | 2024-11-16 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| dfbba3fe-8009-319a-b25b-a8b62ddd4850 | -2.1378 | -53.7244 | 2024-11-16 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| a9a53f83-7352-3774-919f-54cc7f53d7cd | -3.7394 | -45.6523 | 2024-11-16 01:30:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 243.4 |
| 50cf6bdc-c14c-3fc4-b458-eee0a055b60d | -4.9971 | -44.3149 | 2024-11-16 01:30:00 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 5448d8ba-ac7a-3332-bd95-a1f4a5bc743a | -16.9381 | -57.6495 | 2024-11-16 01:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.9 |
| 184e3c34-c8cf-3d2c-b275-80ce5f36c76a | -3.7393 | -45.6747 | 2024-11-16 01:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 122.9 |
| a574eed7-b4f1-3e40-ac5f-b79180b84407 | -17.6071 | -57.5499 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ca72b3b6-7ff4-38a0-9668-b6e6eff34921 | -17.6143 | -57.537201 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4be17c48-6801-331c-9d5e-38be0eee7d6b | -17.6532 | -57.526798 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5bff6e67-2cfe-3cce-a354-0262d6179949 | -17.5798 | -57.480999 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f0881d3d-c51e-3692-816e-a2ea0da8d151 | -17.587601 | -57.555099 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3385a188-c8e9-3e94-ac19-04c31ddd61fa | -17.558201 | -57.519501 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d80381fc-f075-3183-8446-6b7a8ba22103 | -9.6497 | -65.731201 | 2024-11-16 01:30:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d0fa56ed-ad4c-319d-86e7-2d74a0270216 | -17.5697 | -57.4398 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cd5c0bbd-057f-368f-8400-eadf2ea9686d | -17.5557 | -57.5093 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 93396f35-b8bc-3d56-9d33-989d5dc2e432 | -15.4711 | -60.044201 | 2024-11-16 01:30:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 897ba7f2-a123-3cec-985d-fb6b86e8e85d | -17.541201 | -57.534901 | 2024-11-16 01:30:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 09b3028f-1560-3050-b82c-7d15ac15ea49 | -17.253 | -57.458 | 2024-11-16 01:30:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a9781f5e-2f74-3daf-a05e-20b0e7cb97fc | -17.5681 | -57.560299 | 2024-11-16 01:30:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 66e03558-42a2-3805-8810-8c1fb55c9c0d | -17.5609 | -57.573002 | 2024-11-16 01:30:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eb417715-c870-3d38-b9f4-4d9440997d6c | -17.577299 | -57.470798 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e1b9d1f6-8ebf-3e46-918b-fb567bd91c19 | -17.2407 | -57.450199 | 2024-11-16 01:30:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2a5258fd-186b-3bb0-80c4-5cd9abba512d | -17.624201 | -57.577801 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 57b4934e-bbe9-3d85-9826-3b2fb9ef8755 | -17.694799 | -57.569801 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4133f918-2587-3a16-bc77-40943d4807fe | -16.1021 | -60.091202 | 2024-11-16 01:30:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 75f757f3-c6ef-380d-b778-cfdf843e948e | -17.572201 | -57.450199 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 84bd4721-0f5d-3560-82db-9cad65e24e3c | -16.945 | -57.638699 | 2024-11-16 01:30:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bc03419d-304e-31d0-80b2-a9d03b72489c | -17.5632 | -57.540001 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7770232d-52cf-3dc6-8010-3c3ecd704822 | -10.1221 | -65.0252 | 2024-11-16 01:30:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aa25ba4f-010f-32b2-b863-61a8e24d2241 | -19.7651 | -55.391998 | 2024-11-16 01:30:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2f0967f3-fbf2-34ae-97ea-1927bd569d9f | -17.5804 | -57.567902 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3497e48a-5109-31ac-b3b8-b60517ed8ef9 | -17.5679 | -57.516998 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0ed2c611-8997-390f-a28b-40ebbadcccd4 | -9.7009 | -66.960297 | 2024-11-16 01:30:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ce616f33-4979-3654-91dd-1d35e2ad0729 | -22.047701 | -55.996201 | 2024-11-16 01:30:00 | METOP-B | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d9d7ea62-df04-30c3-845a-2f7dcdb01573 | -9.0777 | -65.842003 | 2024-11-16 01:30:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af29bcbf-c1a5-36ee-895d-b1c363ae0953 | -17.587099 | -57.468201 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 20778e39-5964-33c1-90fb-cc1559c228ef | -17.5509 | -57.532299 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d79608b0-af30-3014-bc9e-6d8cda807551 | -17.558399 | -57.562801 | 2024-11-16 01:30:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 32e61289-7c5d-306f-a8dd-d766608cb257 | -17.6133 | -57.406101 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d16720d1-89d7-32ee-b2a6-ff8f49479fe9 | -16.9522 | -57.625801 | 2024-11-16 01:30:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d8808b64-2335-38b4-a837-d51cacae441a | -16.9548 | -57.636101 | 2024-11-16 01:30:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 815d4acb-d1cb-3762-a104-78cc1887b4b2 | -16.939899 | -57.618099 | 2024-11-16 01:30:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5fb3b0c2-aec4-331c-b850-69c4b5640f86 | -17.238199 | -57.4398 | 2024-11-16 01:30:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7f0c0096-29a2-3fcd-be1e-f008e8ff24da | -17.565399 | -57.506699 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2ca36b06-b177-32de-9666-983c7c874da9 | -17.5574 | -57.432098 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c300945a-452e-3aca-a090-8315680cc297 | -17.594999 | -57.585602 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 01f59257-ca7f-3b42-8937-6dd7a911d006 | -17.6168 | -57.547298 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7e8516d3-4b0b-32fe-ad20-83e6ad2afcd2 | -17.6362 | -57.542099 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4ce11723-ef9c-3b84-b7fd-522655293fa7 | -16.9573 | -57.646301 | 2024-11-16 01:30:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cff029f5-660c-359d-bf9d-c8a377ac448c | -16.9424 | -57.628399 | 2024-11-16 01:30:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ac44c88e-9f3f-3136-8928-6791c013ba23 | -17.6387 | -57.552299 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 167021cb-8d3f-3701-b1cf-eebd72ec3ec8 | -16.930201 | -57.620701 | 2024-11-16 01:30:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 36a7d8cd-1649-3e7c-9ab1-f91e2f55f870 | -17.5921 | -57.488701 | 2024-11-16 01:30:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0a0e017f-4f26-3e9f-9232-20d81ac75303 | -19.7684 | -55.4048 | 2024-11-16 01:30:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README11.md)
