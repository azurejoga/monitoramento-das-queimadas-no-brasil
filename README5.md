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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61f858d8-a301-328b-b3b5-f5a216136d3b | -17.6251 | -46.66444 | 2026-02-18 04:29:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8091a920-f84b-3d27-abe4-dfdd83b70c4a | -18.80792 | -51.60593 | 2026-02-18 04:29:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8cd1a7b6-ea0a-3963-87b2-0cd8c345d30c | -15.47725 | -59.59428 | 2026-02-18 04:29:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ea43bc0b-9bfa-3047-9300-3aff4ffdb7b9 | -19.11755 | -40.59885 | 2026-02-18 04:29:00 | NPP-375D | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 95a38632-7f37-333b-bced-3d50d8c2f42a | -18.81081 | -51.61132 | 2026-02-18 04:29:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7f103fbf-72d0-3bb9-a2ae-f89262c0a9ee | -18.7044 | -54.98777 | 2026-02-18 04:29:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58d5448b-a2b7-337b-a2c7-ab3137e79276 | -18.51729 | -44.5531 | 2026-02-18 04:29:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cadb8360-6cad-3cc2-b645-9f63458140b0 | -18.80706 | -51.61064 | 2026-02-18 04:29:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 870d6c25-8d11-3f29-ab55-d0f3990c66d0 | -18.97247 | -52.92802 | 2026-02-18 04:29:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 674e55de-8b27-3a0d-beda-d94d4ebfc6ec | -18.70543 | -54.98262 | 2026-02-18 04:29:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 183bd710-a367-3952-8216-ea158f7731c9 | -18.81166 | -51.60662 | 2026-02-18 04:29:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e3e094fc-8646-33a2-b275-840757ea1e2b | -18.51569 | -44.55433 | 2026-02-18 04:29:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 71dd0659-6620-3acc-99b1-ff5a1dc02f58 | -18.97647 | -52.92889 | 2026-02-18 04:29:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0a446ebc-2ca1-3a0b-9f0e-895fc9892fc6 | -19.11297 | -40.59814 | 2026-02-18 04:29:00 | NPP-375D | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 96c44371-7fb6-32d6-93b8-bac45452f1d3 | -17.62566 | -46.66077 | 2026-02-18 04:29:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 27625763-4a22-3a7e-b266-eb20a243f74f | -18.17426 | -44.97357 | 2026-02-18 04:29:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 72100872-f4bd-3f31-85c4-3ff7b82ce2e6 | -15.47081 | -59.59274 | 2026-02-18 04:29:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4e606e2f-725b-3f1c-ad35-547be6cf2db7 | -17.56247 | -50.44038 | 2026-02-18 04:29:00 | NPP-375D | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a1a37d4-4917-381a-8f82-b7eac9c12177 | 2.6905 | -60.2211 | 2026-02-18 04:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 49.5 |
| dc44af65-b950-32a2-98ed-0e9e54715637 | 2.6724 | -60.1453 | 2026-02-18 04:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 62321d5e-50ee-3ee2-93e7-0ac7ce0940dc | -26.98765 | -52.35892 | 2026-02-18 04:31:00 | NPP-375D | XAVANTINA | SANTA CATARINA | Brasil | 4219606 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 469a02a9-d757-3a2f-b9a1-6500fc182ad3 | 2.6724 | -60.1453 | 2026-02-18 04:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 51.1 |
| e4a7c0c7-eb13-323e-b451-a2b8a80dea9f | 4.05847 | -61.14426 | 2026-02-18 04:44:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 760ebd02-9955-38c7-8ce5-805cebc3e37f | 4.19316 | -60.45538 | 2026-02-18 04:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57013611-4e98-3645-a0ba-16e0cfa32dc2 | 2.68745 | -60.21807 | 2026-02-18 04:44:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 069c9330-6efb-3daa-84d2-eca1ec238c49 | 2.68814 | -60.22267 | 2026-02-18 04:44:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 12.6 |
| fcc67f04-956b-384a-b831-bd9caca72f4a | 2.66445 | -60.1467 | 2026-02-18 04:44:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 52424159-134d-389d-bd29-97ed109cd5da | 2.69146 | -60.20328 | 2026-02-18 04:44:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e57cb494-8a4e-35dd-8d01-926ba23453f7 | 4.19377 | -60.45967 | 2026-02-18 04:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2dddc1f9-e9e3-3bc6-9324-a035c2fd44fa | 2.67721 | -60.14931 | 2026-02-18 04:44:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4fe5d7ad-2947-3f7c-8b1a-edfcf6d2a483 | 2.68608 | -60.20888 | 2026-02-18 04:44:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3585670-53bc-394c-ac76-7d8b60978b84 | 2.68393 | -60.15292 | 2026-02-18 04:44:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1cf62905-c56c-3c34-8966-40bf0c209eb7 | 4.05901 | -61.14127 | 2026-02-18 04:44:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61157ae6-7445-3274-a061-16f6df902ec0 | 2.68677 | -60.21349 | 2026-02-18 04:44:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7dd640c5-c824-33a9-938a-a1987454f377 | 2.67857 | -60.15841 | 2026-02-18 04:44:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc8159f7-9c43-373b-8a65-fe4c13356ec3 | 2.92168 | -60.81794 | 2026-02-18 04:44:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08fa0b4e-e6e9-3f0c-9e79-7164af34bd7d | 2.67788 | -60.15382 | 2026-02-18 04:44:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 350ba89b-b3c0-3c99-b964-5c566bec3b56 | 2.68462 | -60.15748 | 2026-02-18 04:44:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 993f35a5-0cef-38f6-93db-8b2ae4976539 | 4.05977 | -61.14644 | 2026-02-18 04:44:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b3efe22-8603-313d-90df-f2812aae117f | 4.05775 | -61.13913 | 2026-02-18 04:44:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a0967f7-9223-365c-948d-973e5953f46b | 2.67049 | -60.14573 | 2026-02-18 04:44:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 18349207-018d-31da-b715-e5b6b56986e4 | 2.68325 | -60.14837 | 2026-02-18 04:44:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 50c5571c-6d6a-373d-b077-ac7b026e4616 | 2.67654 | -60.1448 | 2026-02-18 04:44:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1362622c-f4ed-3b2a-af22-a19107445ede | 2.91614 | -60.82415 | 2026-02-18 04:44:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0902c9b-ac71-3261-a17b-09ca4c3031fc | 2.67925 | -60.16302 | 2026-02-18 04:44:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79d6d0da-061a-36d1-b9b5-436677153467 | 2.68139 | -60.21907 | 2026-02-18 04:44:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54fa6500-f078-335a-958d-e8a1d1c30873 | 2.91538 | -60.81911 | 2026-02-18 04:44:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86d34d92-ee2e-32a5-92ed-a66184604284 | 1.0588 | -60.56885 | 2026-02-18 04:46:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe7268ec-26d2-36b7-b4da-fe1f94e9e529 | 1.06486 | -60.56786 | 2026-02-18 04:46:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8addf19c-2f5c-3fab-8505-a79471093cb6 | 1.06557 | -60.57241 | 2026-02-18 04:46:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4b64ba7-c8f5-33a5-85c3-92e583893e7c | -11.88708 | -45.28432 | 2026-02-18 04:48:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aba206ac-1abf-3be4-996b-eece7631b024 | -11.89568 | -45.2814 | 2026-02-18 04:48:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5fccbb5-4161-3244-b13a-c45ef0b5546a | -12.48664 | -43.64659 | 2026-02-18 04:48:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 34c23892-21dc-3a05-8836-091cc28180c5 | -12.42601 | -47.17805 | 2026-02-18 04:48:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d610a088-d63d-3e80-83d9-1f7f1891277a | -11.89505 | -45.28628 | 2026-02-18 04:48:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 01512a69-416d-39bf-b535-833bd59781d4 | -11.88643 | -45.28007 | 2026-02-18 04:48:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ba39a7ae-032a-3c28-a06b-11ae1be839d6 | -12.68946 | -46.69922 | 2026-02-18 04:48:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7c55b702-16e5-3f93-919e-9fc1c22d8cd4 | -11.88246 | -45.28358 | 2026-02-18 04:48:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61f57211-ecc6-3c3b-8436-aa4cdaf57680 | -11.8818 | -45.28841 | 2026-02-18 04:48:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c8a6295f-a337-3fc5-ad41-67158216507d | -12.42394 | -47.88181 | 2026-02-18 04:48:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c905734c-e5dd-39f0-9c51-7cccfc1c421c | -13.01673 | -45.04939 | 2026-02-18 04:48:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ada07ba7-ecda-3baf-b157-026257bcb72d | -12.48623 | -43.64983 | 2026-02-18 04:48:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 45f2d67b-52c6-3528-83c2-0aee22beab27 | -11.88118 | -45.28417 | 2026-02-18 04:48:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c8bdc53-ac71-32fd-897c-a8b3bf4c7fc8 | -12.48705 | -43.64336 | 2026-02-18 04:48:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2c473891-1c36-3b8c-8730-93eb42f83fb1 | -9.51685 | -46.1466 | 2026-02-18 04:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe84a513-b28d-3332-a3a7-2520d925eae3 | -11.88979 | -45.29047 | 2026-02-18 04:48:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2021cd1c-d72d-339e-9c35-9cc9c122807e | -13.01539 | -45.05993 | 2026-02-18 04:48:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f2db7137-7d97-3b7b-90c8-a7d45d0270f0 | -11.89042 | -45.28562 | 2026-02-18 04:48:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9e94548c-f9ec-3fd3-8138-c5e6d50abdc9 | -12.48182 | -43.64271 | 2026-02-18 04:48:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbac2ca1-4c8d-3d33-a2dd-35f5f8bc7667 | -11.79248 | -44.13525 | 2026-02-18 04:48:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2b8222d1-35e3-3fdf-867f-cc01d8aea6fd | -13.01606 | -45.05465 | 2026-02-18 04:48:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 12403292-4a92-300f-ac0b-94070cca2e06 | -12.49186 | -43.64728 | 2026-02-18 04:48:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 480633c6-991d-3c41-b8b4-2188d9edecbb | -11.89442 | -45.29113 | 2026-02-18 04:48:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 55d64fd6-c02d-3f68-87c2-9686bc0c005d | -11.88312 | -45.27874 | 2026-02-18 04:48:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d17a42c-718f-3dac-83d5-5b445a77bdea | -8.44186 | -45.13588 | 2026-02-18 04:48:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3dc9fe79-589e-360a-8f98-e1ed7ee91280 | -13.02085 | -45.05526 | 2026-02-18 04:48:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ce800bf0-361d-3a61-b272-f951b17a47dc | -11.88517 | -45.28975 | 2026-02-18 04:48:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 723bd58b-181b-375c-a0a3-7ebd7eb68f91 | -11.88641 | -45.28916 | 2026-02-18 04:48:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8785477d-81fd-3638-93b8-f9742c79b1bf | -12.42549 | -47.18176 | 2026-02-18 04:48:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98f613e9-da7b-323b-b30a-dc21616acdcf | -11.88774 | -45.27947 | 2026-02-18 04:48:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5eddbee-1baf-34df-87b9-b191dcebed8e | -13.01061 | -45.05929 | 2026-02-18 04:48:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f668fbf3-0255-3f70-88b2-c3a87788588f | -10.9904 | -53.98446 | 2026-02-18 04:48:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d53a0ff2-4f71-38f5-9b09-491033305013 | -10.73929 | -59.22577 | 2026-02-18 04:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91b0f997-4024-3926-8c13-c1de0fcb360f | -12.49145 | -43.6505 | 2026-02-18 04:48:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d92edec7-bd6b-39cc-bb91-4e0b3adfdba0 | -12.48582 | -43.65306 | 2026-02-18 04:48:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0e95bc6a-54db-3505-9536-faf2cbb302c0 | -13.01128 | -45.05402 | 2026-02-18 04:48:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96299601-2147-3db5-a728-69d6356f7e72 | -10.74013 | -59.2211 | 2026-02-18 04:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8258fa97-9c56-3c28-be01-f7c644e16d7b | -13.02152 | -45.04999 | 2026-02-18 04:48:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ce0a2b37-479b-340d-9a49-c0e63aa6564a | -10.73557 | -59.22018 | 2026-02-18 04:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e76259c-4fac-3a04-9bc3-7044282e3323 | -12.4219 | -47.17747 | 2026-02-18 04:48:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a473912c-6a83-3abb-969a-eefe655f0fc9 | -11.8858 | -45.28493 | 2026-02-18 04:48:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 412cdf63-b2b3-3338-bf78-7b9e65f0be70 | 2.6724 | -60.1453 | 2026-02-18 04:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 53.4 |
| a4743822-609c-3d43-8b32-bd49784607ce | -15.47744 | -59.59219 | 2026-02-18 04:50:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f22e4af4-4563-37a8-a946-808d1daf18e0 | -18.8131 | -51.60487 | 2026-02-18 04:50:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 272b17ed-d5fe-318b-b991-0a90caeb2c05 | -18.70344 | -54.98899 | 2026-02-18 04:50:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d04e3bf7-010d-3c82-a820-fb72fc8304e8 | -16.54856 | -52.77057 | 2026-02-18 04:50:00 | NOAA-20 | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fb416628-ad08-34ec-acc8-600f4803d012 | -12.20936 | -57.79283 | 2026-02-18 04:50:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e031fac9-a1ff-367e-80df-e18eb7f6a018 | -17.56139 | -50.43868 | 2026-02-18 04:50:00 | NOAA-20 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 939b11dc-616d-31c8-8cd9-9ca89d98068b | -14.4183 | -44.59309 | 2026-02-18 04:50:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bfbc5968-e0b0-36b4-b34c-88698b641cdd | -18.80904 | -51.60832 | 2026-02-18 04:50:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README6.md)
