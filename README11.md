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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03ec2883-ef26-3829-912d-bf8ce41c1cad | -6.60856 | -37.88713 | 2026-10-05 03:19:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ddd7a9fa-fb10-311a-af41-c2b8465dca2b | -16.67424 | -41.85211 | 2026-10-05 03:19:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 58299a34-6dff-384c-b837-64b4f5894925 | -6.60852 | -37.89011 | 2026-10-05 03:19:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 50aaa1eb-38e7-3b9f-9a07-23d65e287164 | -6.60911 | -37.88689 | 2026-10-05 03:19:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4fe6264c-803c-3a0e-b1bb-8b6587015ab4 | -12.86072 | -39.92541 | 2026-10-05 03:19:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 1a0be7b2-880d-3ef9-963e-a3549ec4547d | -12.85986 | -39.92967 | 2026-10-05 03:19:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| bc3cee4a-c9a7-34bc-a03d-9c4e1a92dd01 | -6.60799 | -37.89033 | 2026-10-05 03:19:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3fb93b73-7891-3599-8a47-d01f4fa2f172 | -17.0514 | -40.23318 | 2026-10-05 03:19:00 | NOAA-20 | ITANHÉM | BAHIA | Brasil | 2916005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e9fa642f-4081-368e-97f6-4e13d3fa40e8 | -6.914 | -43.6816 | 2026-10-05 03:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 2e5b7de4-3b75-3e4f-9d24-75509c01fde6 | -7.4442 | -63.5589 | 2026-10-05 03:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| ef5b2c9b-a398-37fa-836e-7f1df865999c | -2.6859 | -49.0325 | 2026-10-05 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 0f7b84a6-707b-337f-ac23-00279356f356 | -2.9817 | -54.089 | 2026-10-05 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| d0f4fff5-f2b7-35c7-9673-94c7a770bd02 | -3.2717 | -50.4102 | 2026-10-05 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 521eabc6-5778-3772-8035-8170bcdc5acf | -3.4577 | -54.5977 | 2026-10-05 03:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 9e3c411c-db52-3e8f-b40d-0671e45e472e | -2.9632 | -54.1497 | 2026-10-05 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 53238ca6-8e23-38ee-910d-85e896b20673 | -6.1781 | -52.9328 | 2026-10-05 03:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| da676800-9def-3ba8-bf70-5bcfe3ba02fd | -2.9449 | -54.13 | 2026-10-05 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| d5c19569-1c65-373f-b363-21432b91041d | -6.8952 | -43.6833 | 2026-10-05 03:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 8a591831-6256-3903-96df-e9e975c8d5b6 | -2.9448 | -54.1501 | 2026-10-05 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| f6fb55ea-86fd-38ea-9549-c076c5449664 | -2.9817 | -54.1091 | 2026-10-05 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| cd19e254-4d30-39aa-bad3-df88361ddb49 | -6.0074 | -53.5325 | 2026-10-05 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| ab22e05f-ba2b-3e09-85c0-28c33755359f | -3.0548 | -54.2277 | 2026-10-05 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| c6dab3f3-6695-339b-8cef-0e0570178e98 | -3.0001 | -54.1086 | 2026-10-05 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 0b972f0e-41ad-3e96-a69c-5ea00016683a | -6.0075 | -53.5122 | 2026-10-05 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 16e7c846-6e52-344b-9328-8af26194a3e5 | -3.9032 | -49.7137 | 2026-10-05 03:30:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| c1fceebb-3094-3091-b6b8-a5a0473e7470 | -3.0548 | -54.2277 | 2026-10-05 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 1e033b1e-4776-3352-9bf6-6d405f0b677a | -3.8447 | -50.3273 | 2026-10-05 03:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| b88c2faa-a75d-36fa-a8b4-0221fcf1e107 | -2.9449 | -54.13 | 2026-10-05 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 5af418d0-d3e8-3894-8a18-b7d950eb9f4d | -6.0075 | -53.5122 | 2026-10-05 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 5c9162dc-2db9-336d-b870-0e01fb0fef3f | -2.9448 | -54.1501 | 2026-10-05 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 138.4 |
| 2d4d1676-902b-3e2f-8694-2950d36a3ccb | -6.1781 | -52.9328 | 2026-10-05 03:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 8f56a71a-6abc-3682-9a67-b24336cd266c | -3.0001 | -54.1086 | 2026-10-05 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| d83f2441-4034-324b-a63e-d17494ad10f9 | -2.9632 | -54.1497 | 2026-10-05 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 680b9f44-d9d8-3b4f-858c-049d34827ca2 | -7.4442 | -63.5589 | 2026-10-05 03:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 569df81d-f107-3aa2-9df2-36b9e20aea82 | -6.8952 | -43.6833 | 2026-10-05 03:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 61.6 |
| fd77758d-7a2a-3e77-8ba1-422a6e3f6784 | -2.9817 | -54.1091 | 2026-10-05 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 2005fffe-06eb-3db4-b675-6526d03d5879 | -3.4577 | -54.5977 | 2026-10-05 03:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 356ed839-a87e-3fe3-a48c-65e638e636c5 | -3.0001 | -54.1086 | 2026-10-05 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 40c15b6e-e10b-307d-bcf7-298894225857 | -2.6859 | -49.0325 | 2026-10-05 03:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 289dbc3f-43c4-3625-83fc-1f9c32de0970 | -2.9632 | -54.1497 | 2026-10-05 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 3df9634c-9a1f-382f-bf7c-7ad38d13cbeb | -6.1781 | -52.9328 | 2026-10-05 03:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 28281458-30f9-36c9-a488-153cbfb86de6 | -2.9449 | -54.13 | 2026-10-05 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| abe3bed0-a152-367e-8842-5298ff314821 | -3.0548 | -54.2277 | 2026-10-05 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 8676b270-68ab-3919-b7e6-ed8ffa8c0205 | -2.9817 | -54.1091 | 2026-10-05 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| e1d705e1-dc56-392e-9622-35ae6cf46ebb | -3.8447 | -50.3273 | 2026-10-05 03:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 8c6ac2c9-ea07-3cb8-8112-dd1a28137862 | -6.914 | -43.6816 | 2026-10-05 03:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 4a22a5cf-e1e0-34b7-8250-dfa2783313f9 | -6.178 | -52.9533 | 2026-10-05 03:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 19cc1d2f-3c00-31b7-b055-c13d8d8e3f9b | -7.4442 | -63.5589 | 2026-10-05 03:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 0284b238-deb6-3de5-83aa-adb2664c1627 | -6.0075 | -53.5122 | 2026-10-05 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 6e4bcf0b-ea5b-3186-9ff4-e1ddfca6ea4c | 1.8583 | -55.8216 | 2026-10-05 03:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| fea8d2f3-92be-30f8-a3cd-b39a3c893468 | -3.4577 | -54.5977 | 2026-10-05 03:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| d7ec2703-264f-362c-937a-f44f64afb4e5 | -6.2527 | -52.8675 | 2026-10-05 03:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 171f06ac-e125-31db-946c-efde37459586 | -2.9448 | -54.1501 | 2026-10-05 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 3e55ef7c-9000-3667-aaa1-3cb51d286adb | -6.2159 | -52.8285 | 2026-10-05 03:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| a77195e3-252c-3bbf-99a4-90352bf92829 | 1.8399 | -55.8218 | 2026-10-05 03:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| fd90e5a3-99f4-3c14-898e-3352dbc43815 | -6.1781 | -52.9328 | 2026-10-05 03:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| babf6271-1eb1-3307-91da-93e62f3d2d59 | -3.4577 | -54.5977 | 2026-10-05 03:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| f4a5ccf2-ab87-36d7-9285-56eb4cc67e87 | -7.4442 | -63.5589 | 2026-10-05 03:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| e2848570-7336-3225-91da-ad86a17f3f3f | -3.0548 | -54.2277 | 2026-10-05 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 87e42b70-4818-3e3f-b656-9a1d722433dc | 1.8583 | -55.8216 | 2026-10-05 03:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| b3bf9a9d-f110-38cf-98dc-d69e8a9982be | -2.9632 | -54.1497 | 2026-10-05 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| d8f6afaa-46d1-31ad-a0f8-7dcdc4090681 | 1.8399 | -55.8218 | 2026-10-05 03:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| a915b1ce-b00d-3037-9757-4045b994f46d | -2.9448 | -54.1501 | 2026-10-05 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 2a836e1e-0bfd-3ef6-af02-b47dc760b8d5 | -2.9449 | -54.13 | 2026-10-05 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 10e4ec96-ee23-3e75-91a0-38015b46d9e5 | -6.1974 | -52.8295 | 2026-10-05 03:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| eec5a77e-176f-308d-b81e-ae514f64b259 | -3.0001 | -54.1086 | 2026-10-05 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| e749e9c1-8e72-35b5-a72a-abd70ccea087 | -6.2159 | -52.8285 | 2026-10-05 03:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 4e20b475-d758-36de-a112-0edc610b63fc | -2.9817 | -54.1091 | 2026-10-05 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 33130656-7b15-3c49-b47f-d731d1039a48 | -3.0917 | -54.1666 | 2026-10-05 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 126.4 |
| a13af5e2-9b96-392f-811e-2d64745e87b5 | -2.9449 | -54.13 | 2026-10-05 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 092cda26-09e0-3e46-81b2-9b15cebcd043 | -3.055 | -54.1675 | 2026-10-05 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 761e53c4-b08e-360e-b505-b94cea0376b0 | -2.9632 | -54.1497 | 2026-10-05 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| bafd69f9-9022-381e-9b30-18d9e8de296c | -6.1781 | -52.9328 | 2026-10-05 04:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 15d19f3b-651f-377d-ad27-eb563330b4e7 | -2.9817 | -54.1091 | 2026-10-05 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 9fa74e78-07ec-3bb0-af9b-bfb85dbbcb1b | -2.9448 | -54.1501 | 2026-10-05 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| d528f8b1-7d32-3e0a-a2c3-5dd1ab5770e8 | -3.0734 | -54.167 | 2026-10-05 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 367.2 |
| f9c987b6-88f7-34dd-a54c-aa4f9623f164 | -3.8447 | -50.3273 | 2026-10-05 04:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| b3efce67-17d8-3808-a860-9eb9e5a9e66f | -6.2159 | -52.8285 | 2026-10-05 04:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 2595eff5-7b0d-3cf9-936c-c5287cc1f840 | -3.0733 | -54.1871 | 2026-10-05 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 256.6 |
| 3fc795fb-265d-378b-8911-1e4e110342ba | -3.0548 | -54.2277 | 2026-10-05 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| bbe88f1e-f276-31ce-b0ff-c42c3e484376 | -3.0734 | -54.147 | 2026-10-05 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 76956210-078d-3646-8738-5a0888875aeb | -3.0917 | -54.1867 | 2026-10-05 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 64926a84-bdd6-3925-87c0-f74406a2939e | -7.4442 | -63.5589 | 2026-10-05 04:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| fb6a5ee2-cc72-344c-a9a7-81b45a233c19 | -1.16896 | -49.24957 | 2026-10-05 04:00:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b29ff613-9529-3567-8972-745357ec8f2e | -1.86563 | -50.60901 | 2026-10-05 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 57baa5c3-27ad-3d86-be8d-d6fc867555cf | -2.47626 | -48.03789 | 2026-10-05 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4096c3f-98a8-37ed-a402-7f76084b3aa8 | -3.60585 | -38.92506 | 2026-10-05 04:00:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c149f349-32d2-3293-93ae-695987d0f4d1 | -2.47106 | -48.03703 | 2026-10-05 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5e2a290b-05db-31cf-89aa-1f4d8d574860 | -2.47056 | -48.04015 | 2026-10-05 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 027f4393-00d5-3a88-93fe-9760b0145b0b | -3.26641 | -42.54049 | 2026-10-05 04:00:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0cca5eae-508b-3780-8384-c5259fea1625 | 0.43141 | -51.06121 | 2026-10-05 04:00:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b11013eb-0316-38f3-8ac0-6078ed5f512e | -1.86677 | -50.61148 | 2026-10-05 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ebf176a-5b3c-367b-bb98-a527a518599d | -3.1695 | -41.39662 | 2026-10-05 04:00:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5c024448-9d81-35f5-8e3a-eef0b64dc727 | -1.17472 | -49.25047 | 2026-10-05 04:00:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0430370-9e18-370b-9e19-6187c706ed5a | -3.71404 | -40.34542 | 2026-10-05 04:00:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 659ce2ab-38c7-3587-aff8-503757822619 | -1.86646 | -50.6041 | 2026-10-05 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 07983051-1328-35a9-a00d-16b546d3511b | -2.59865 | -48.95323 | 2026-10-05 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed4da867-b702-3f2d-bdeb-0c3a80d91819 | -3.11478 | -45.19077 | 2026-10-05 04:00:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e090ec9d-331e-39a9-89dc-01d5c4c782f2 | -2.27547 | -48.74685 | 2026-10-05 04:00:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 330a4dff-22d3-35be-82cf-208d872fcaff | -1.17407 | -49.25447 | 2026-10-05 04:00:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README12.md)
