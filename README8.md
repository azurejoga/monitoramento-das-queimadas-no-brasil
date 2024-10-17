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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d485065a-a61d-37a1-9e08-b42088c08983 | -12.1533 | -40.8694 | 2024-10-17 00:36:14 | GOES-16 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 93.0 |
| e38d9daf-92cd-3536-bf5f-873f4ea8355e | -11.8812 | -64.9513 | 2024-10-17 00:36:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 76.9 |
| daaafff8-42b0-3c27-9d0e-13f565f3e2e6 | -11.8814 | -64.9323 | 2024-10-17 00:36:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 28e3ec26-16ed-3bf3-a1a3-2fef70a85115 | -11.8815 | -64.9134 | 2024-10-17 00:36:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 54f0f99d-e0ad-30d9-999f-e8229e335109 | -11.9002 | -64.9315 | 2024-10-17 00:36:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 38b3dec6-3fad-3db4-b6d6-879c5fb80372 | -11.9383 | -64.854 | 2024-10-17 00:36:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |
| e68fbc48-43ef-3346-b955-194243c9e300 | -17.9036 | -57.4534 | 2024-10-17 00:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.4 |
| 86e7f5a0-253e-3b4a-9d20-25aa52bec951 | -2.6147 | -48.2629 | 2024-10-17 00:45:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 69cd75a9-443a-37ab-b328-b5cf219f32f4 | -2.8979 | -51.6896 | 2024-10-17 00:45:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 042fd413-69b9-3ab2-ac62-bf0d5de391bd | -2.9674 | -47.9931 | 2024-10-17 00:45:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| a18924b5-aa31-3638-89fd-698c6185f454 | -3.0581 | -53.2395 | 2024-10-17 00:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 6141330c-ecb2-393c-906b-c3eed77b4d7d | -3.2225 | -48.9306 | 2024-10-17 00:45:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 115abd90-1835-3dd0-83f5-84d2a329c0bd | -3.2226 | -48.9092 | 2024-10-17 00:45:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 95bcaffa-a67b-3eb7-a2f5-a3d0709a1707 | -3.4902 | -51.1129 | 2024-10-17 00:45:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 0e8a9672-6929-3085-82ee-28358ff09299 | -3.5086 | -51.1122 | 2024-10-17 00:45:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 1c8c76ba-7133-3a0e-a0b9-aa2583ffd743 | -3.6941 | -43.7904 | 2024-10-17 00:45:27 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| bc7ab918-bfa0-38ad-a280-30361a3e1685 | -3.7128 | -43.7895 | 2024-10-17 00:45:27 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 4237f6d2-6342-31c8-ba02-8bd523b966b2 | -3.7007 | -45.9223 | 2024-10-17 00:45:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 121.0 |
| da29082e-6243-3de5-aec9-c1d802865ed7 | -3.7009 | -45.9 | 2024-10-17 00:45:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 01716bd0-374c-341d-aeb5-95d321a5c03f | -4.4845 | -42.8631 | 2024-10-17 00:45:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| f875233c-cea0-33c8-b063-922657a87124 | -5.9788 | -45.3621 | 2024-10-17 00:45:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 524a41e7-77c6-3747-af42-b263f2032f6a | -6.7274 | -43.5589 | 2024-10-17 00:45:44 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 882b828a-9f0b-3919-a669-997ff05bae60 | -7.8539 | -45.3611 | 2024-10-17 00:45:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| a495c52f-2c75-3809-ab36-4d4e5a3a1a83 | -7.8727 | -45.3593 | 2024-10-17 00:45:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |
| e8a9f216-0032-38d3-90b8-e40e20a721a7 | -7.873 | -45.3366 | 2024-10-17 00:45:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 14e6f707-3859-3c1b-b713-e996ac061fa8 | -9.4761 | -40.3862 | 2024-10-17 00:45:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 83.5 |
| dd46e666-bfa4-3bc9-9074-e9d3b7bfb110 | -10.1288 | -56.7921 | 2024-10-17 00:46:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 0ae710e7-5a95-358b-8dcb-caeeec3b66dd | -10.129 | -56.7722 | 2024-10-17 00:46:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 153.1 |
| d689cba5-3633-339f-b560-d797542507cb | -10.1292 | -56.7523 | 2024-10-17 00:46:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| e4d1d908-fa2b-3fae-92da-d70683006304 | -11.7308 | -64.9769 | 2024-10-17 00:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| ed66bb0b-e677-3975-945b-f58e345c1e31 | -11.7309 | -64.9579 | 2024-10-17 00:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| c512320c-f46f-3efe-8338-8b99687cbb6a | -11.7497 | -64.9571 | 2024-10-17 00:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 5b235a40-07e0-308e-83d7-a341aeaa4d53 | -12.1528 | -40.8943 | 2024-10-17 00:46:14 | GOES-16 | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 76.6 |
| eb2602a1-cf9c-3f50-8d37-284383dec3db | -12.1533 | -40.8694 | 2024-10-17 00:46:14 | GOES-16 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 83.4 |
| b40dbeeb-c7df-3fe0-a897-5c0fd9f312a2 | -11.8812 | -64.9513 | 2024-10-17 00:46:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 6f916827-f684-300e-828a-17eddfe72485 | -11.8814 | -64.9323 | 2024-10-17 00:46:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 140.9 |
| bfc744be-1175-3707-9066-904e471860d3 | -11.8815 | -64.9134 | 2024-10-17 00:46:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| fe132ad7-f3ca-34ff-bfbc-db5e5aca96b5 | -11.9 | -64.9504 | 2024-10-17 00:46:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 0dd52e11-daed-3f53-af99-01be96c892f7 | -11.9002 | -64.9315 | 2024-10-17 00:46:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 80.9 |
| dfcd3af5-052c-3c50-874f-e608608ef19e | -11.9383 | -64.854 | 2024-10-17 00:46:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 648f5a86-708d-380b-9b09-65fd0df2bf56 | -11.9571 | -64.8531 | 2024-10-17 00:46:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 37e03079-f651-3b91-851b-5ceb90e7fb62 | -17.9036 | -57.4534 | 2024-10-17 00:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.1 |
| cc62bb13-03c1-3062-a95e-863c6114ca82 | -17.904 | -57.4328 | 2024-10-17 00:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.7 |
| d3e08c59-7efb-359b-bd35-f6ea98b53c64 | -17.8049 | -57.4655 | 2024-10-17 00:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.6 |
| ec36ba88-9dea-3afd-82e3-55991155ef98 | -17.8052 | -57.4449 | 2024-10-17 00:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.7 |
| 2efe33b5-d4bd-3e9b-9f0f-8bcee1c966a2 | -17.8055 | -57.4243 | 2024-10-17 00:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.9 |
| dba63f97-ff5f-3eac-9472-9301ccbf4b59 | -17.8246 | -57.4631 | 2024-10-17 00:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.7 |
| cf20545c-7b72-34ab-b232-2904e73a5576 | -17.8444 | -57.4607 | 2024-10-17 00:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.2 |
| 9ff24ba6-529f-3cc8-959a-5da4c66e7e1b | -17.8641 | -57.4583 | 2024-10-17 00:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.4 |
| 81ddf7d7-10ce-3467-a52f-21e60253c503 | -22.6458 | -42.2355 | 2024-10-17 00:47:09 | GOES-16 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 106.5 |
| 6073aa5a-ce02-3b53-bc55-d5faed697ea3 | -2.5962 | -48.2634 | 2024-10-17 00:55:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 87aa1909-3a0c-30a7-bcfa-d0960a992165 | -2.6147 | -48.2629 | 2024-10-17 00:55:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 2cb8600b-09a2-3400-a722-83637a101eb7 | -2.8333 | -49.1562 | 2024-10-17 00:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 90f81af5-dba6-3423-8542-2fcc24336457 | -2.8979 | -51.6896 | 2024-10-17 00:55:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| bc8bf349-cdb7-34c9-b1eb-ba3201fc34b9 | -2.9673 | -48.0147 | 2024-10-17 00:55:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 7b49737b-8ffe-34aa-9b64-28963636d947 | -2.9674 | -47.9931 | 2024-10-17 00:55:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 5c438e4e-9632-3d37-9abf-ca93e19cf283 | -3.0581 | -53.2395 | 2024-10-17 00:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| cf80990f-86e6-37a7-87fd-aff89d29c2c5 | -3.2225 | -48.9306 | 2024-10-17 00:55:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 1a969704-cd31-3ab4-8a95-224c008cbf1d | -3.2226 | -48.9092 | 2024-10-17 00:55:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| ffa54294-1ff7-34b7-9cdb-f9fda3891cb7 | -3.5086 | -51.1122 | 2024-10-17 00:55:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| daebe11a-1bec-3dc5-9767-e283dd121940 | -3.7007 | -45.9223 | 2024-10-17 00:55:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 2b3dbf8a-b8d9-3f37-bd66-802950e07f3a | -3.7009 | -45.9 | 2024-10-17 00:55:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 95770a57-6077-3cf4-90f8-24be3b151beb | -4.58 | -48.0132 | 2024-10-17 00:55:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| fb0bf4f1-e943-3ea7-b7ec-e2e05cb86368 | -5.9788 | -45.3621 | 2024-10-17 00:55:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 262cdcc7-88d3-3a79-9ae6-38bf8750b01b | -6.7274 | -43.5589 | 2024-10-17 00:55:44 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 117.1 |
| d784cb0a-939d-3c47-afff-9f3c0f523e33 | -7.8727 | -45.3593 | 2024-10-17 00:55:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 40d3b26d-44af-33f6-8158-c8dee5d314b7 | -7.873 | -45.3366 | 2024-10-17 00:55:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 0afa9151-2308-3412-91f3-4196d7d00ef8 | -10.129 | -56.7722 | 2024-10-17 00:56:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 158.6 |
| 01727b82-d1ec-3a59-85d9-2f7bceefae34 | -11.7308 | -64.9769 | 2024-10-17 00:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| e6c7d07b-b108-312e-a826-cc75a5518a94 | -11.7309 | -64.9579 | 2024-10-17 00:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.1 |
| b3e58649-2f1e-3986-bb4b-43154e31497f | -11.7495 | -64.976 | 2024-10-17 00:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 64582e52-cc2f-3350-ae25-4966c074759f | -11.7497 | -64.9571 | 2024-10-17 00:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 7fa76458-b94c-3cab-95e3-bdc8b22afb43 | -11.8812 | -64.9513 | 2024-10-17 00:56:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 83.6 |
| be3e3923-1298-3d0f-815c-48fad17210e5 | -11.8814 | -64.9323 | 2024-10-17 00:56:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 119.3 |
| e8dc200e-21a3-331c-9c99-c282bcda7b9e | -11.8815 | -64.9134 | 2024-10-17 00:56:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 7848d464-132b-33e6-8863-b6ac177d3266 | -11.9002 | -64.9315 | 2024-10-17 00:56:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 7239639a-af3a-32d3-a70a-155099a64e5d | -12.3613 | -53.1396 | 2024-10-17 00:56:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| f2db1168-6a0e-3670-b234-2efac5f20c71 | -17.1664 | -56.8439 | 2024-10-17 00:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.8 |
| f19085c5-fdfc-32bb-8d5c-2479d2c0a9b2 | -17.1667 | -56.8232 | 2024-10-17 00:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.2 |
| 3a4999c2-612b-30a7-8241-0c846115963c | -17.2177 | -57.3102 | 2024-10-17 00:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.5 |
| c77d72d0-267d-3c67-bafd-a3cd10f30017 | -17.2373 | -57.3079 | 2024-10-17 00:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.9 |
| 543687eb-2a45-3019-bebe-e9d3bc7d5bec | -17.9036 | -57.4534 | 2024-10-17 00:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.8 |
| 577e0d53-94e3-3832-86fe-bb74d5c56136 | -17.9234 | -57.451 | 2024-10-17 00:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.7 |
| 65d80a3e-888f-3b82-a800-fbf7f991be04 | -17.9237 | -57.4304 | 2024-10-17 00:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.2 |
| f563d189-cd2c-36ba-a16f-a709d5a32d6c | -18.254 | -56.6029 | 2024-10-17 00:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.9 |
| 157ee3f1-e366-3ca6-a6ef-dc6625ccd0e4 | -2.5962 | -48.2634 | 2024-10-17 01:05:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 2f0153f7-d5e5-3f76-9891-af5ce54bd428 | -2.6147 | -48.2629 | 2024-10-17 01:05:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 38ebf983-d94e-348a-803d-63069e21f649 | -2.8333 | -49.1562 | 2024-10-17 01:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| ddce8f53-0661-328f-a281-52341fefe509 | -2.8979 | -51.6896 | 2024-10-17 01:05:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 121d173c-92e9-30fd-83a8-a902a3e1c437 | -2.9673 | -48.0147 | 2024-10-17 01:05:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| bb61e16e-4aea-33d0-b6d2-efd3c3a0459b | -2.9674 | -47.9931 | 2024-10-17 01:05:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 203.2 |
| 0c6d3662-16a5-3bd6-ab02-773d016b803e | -2.9859 | -47.9925 | 2024-10-17 01:05:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| d5d1a509-76ff-31cd-8917-6e54e01d83a9 | -3.0581 | -53.2395 | 2024-10-17 01:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| ffeb05ba-1b03-3e4f-8204-51cf86e3fd95 | -3.2225 | -48.9306 | 2024-10-17 01:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 848b2e35-4aec-3ce2-8d4f-eff91cbc0628 | -3.2226 | -48.9092 | 2024-10-17 01:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 8a9705dc-5e8b-3815-88bb-2721c7df5672 | -3.2945 | -45.402 | 2024-10-17 01:05:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 87.4 |
| ecbb2626-f821-388f-97e0-d7ae3591660a | -3.3131 | -45.4013 | 2024-10-17 01:05:25 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 56.6 |
| ad40f6db-9a7c-3edc-931d-2151aca81738 | -3.5086 | -51.1122 | 2024-10-17 01:05:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 75baeb7b-2617-3399-bcf0-801dd73cfdfa | -3.7007 | -45.9223 | 2024-10-17 01:05:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 123.0 |
| ea8e6f37-afc9-3d5d-a741-f1e0d15b607d | -3.7009 | -45.9 | 2024-10-17 01:05:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 105.9 |


[Clique aqui para ver as próximas entradas](README9.md)
