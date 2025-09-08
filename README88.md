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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 162d3316-ec67-33fa-843f-5cdcae45f73a | -16.2897 | -58.11911 | 2025-09-08 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e4c10aeb-b2b5-3e76-a2fe-553cc68a1e70 | -14.51381 | -48.79416 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5c5f94a2-6f1c-3cd3-9b18-659fbe3adfbd | -14.46705 | -48.79532 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8e2bdde-ad87-3758-910d-2432ad756883 | -16.32875 | -52.9357 | 2025-09-08 05:23:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 56e015fb-4ae2-3b98-9c3e-43b89a32a31e | -15.24771 | -53.82242 | 2025-09-08 05:23:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0850e14b-20ea-3d2f-a7c7-d4a81894f3cd | -19.52804 | -47.88544 | 2025-09-08 05:23:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| adca943e-0d2f-3353-b8dc-6007e4e99963 | -15.2536 | -53.81319 | 2025-09-08 05:23:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b914e86-d747-37e7-93f7-4b0a715c330f | -15.75025 | -53.53925 | 2025-09-08 05:23:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 19c2c6f3-aedb-3c07-9215-d65dbadc2cd5 | -14.99385 | -48.01511 | 2025-09-08 05:23:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d3a4c0d7-27d0-3f00-ae24-e701e3cf65cd | -15.83258 | -52.29792 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1cf2dd35-8bc7-393c-88fc-4b8301c0ac9e | -14.87796 | -55.82285 | 2025-09-08 05:23:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0692cedf-0645-388e-9898-1d186e997170 | -15.18745 | -47.9648 | 2025-09-08 05:23:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 84389cf6-1248-3fd7-b5e4-083a3afca35b | -14.53011 | -53.98507 | 2025-09-08 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5fa65ab8-0ada-34d0-8e6c-c8ede1b69992 | -14.45472 | -56.80925 | 2025-09-08 05:23:00 | NPP-375D | ARENÁPOLIS | MATO GROSSO | Brasil | 5101308 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8666129d-eefd-3f72-ba64-5fec39041119 | -15.50267 | -52.76983 | 2025-09-08 05:23:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0224841e-cb46-3b3b-8d67-fd12909fd54a | -15.7152 | -53.55028 | 2025-09-08 05:23:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab578c1d-44bd-3d9f-9f51-4fddc6a7b7c3 | -15.19087 | -47.97879 | 2025-09-08 05:23:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f6ac1c91-ee95-3f68-9e81-93dfdb6b20ca | -15.83153 | -52.26241 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fcf23159-d301-366a-9638-b72c846f4e7f | -16.3294 | -52.93039 | 2025-09-08 05:23:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bc6736e1-1ba5-31fc-b4f2-f89297ec6e60 | -16.33818 | -52.93951 | 2025-09-08 05:23:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 581da694-6e01-3101-9ec4-171ca2fe0bf5 | -15.69205 | -53.57389 | 2025-09-08 05:23:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11e5c0aa-21ab-3adc-a976-a7ebe27b898b | -12.41608 | -63.90105 | 2025-09-08 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee407373-bd5f-36fa-b71b-16ace52c355f | -12.41683 | -63.8966 | 2025-09-08 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea90b548-0ed9-3d93-a20d-a795ace89ce4 | -14.50589 | -48.80809 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 99c6b4e8-d5b1-37e3-94c9-1f5ccbf6111b | -14.68905 | -48.19439 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c8e81111-4934-3fda-8e3b-30f27aa6e7e2 | -15.08133 | -50.07801 | 2025-09-08 05:23:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b54fa68-a3dd-37b7-b879-da8e153c4b25 | -14.59527 | -48.08592 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10ae4a3f-5041-3018-9741-0660897669fd | -15.2654 | -52.38432 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c3f965d9-b552-313a-afbd-b5e388599f71 | -15.69003 | -53.55163 | 2025-09-08 05:23:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 709711a0-4560-363d-b755-55141bab1d57 | -14.80756 | -48.18533 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ec14565d-82d5-3a67-bb1a-f1208078355f | -14.517 | -48.76439 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3deb1f7e-db45-30ab-b126-a8c8659593cb | -16.33369 | -52.93667 | 2025-09-08 05:23:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 345154cc-7522-3a76-b54a-e7ac7c4f1a3f | -16.34179 | -52.95197 | 2025-09-08 05:23:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e8ac4d8c-8f04-3f44-a951-b4ba8854da44 | -14.35529 | -60.31849 | 2025-09-08 05:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1086d6a3-3cf2-3150-8488-37530fe88278 | -14.71002 | -60.25413 | 2025-09-08 05:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e45b3fae-bf1f-3bfd-9e5c-9d7e286c53ec | -15.25621 | -53.82131 | 2025-09-08 05:23:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96d0ce91-8f2c-322c-8e09-00c3dbbe7a37 | -14.59368 | -52.1279 | 2025-09-08 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a95de58f-bf28-30c1-a767-a48da13c95bd | -15.08173 | -50.07441 | 2025-09-08 05:23:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6f1d1096-96c6-3c3a-b88f-e5253c84f7f4 | -15.25487 | -53.8034 | 2025-09-08 05:23:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7c591ad-bbd2-37bd-b34c-2302be4f71f0 | -14.71335 | -60.25469 | 2025-09-08 05:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1225a8d7-e14d-3ec2-99b2-be5876eaceae | -14.35862 | -60.31907 | 2025-09-08 05:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64bd2e6e-eefd-316e-9157-8e01d7b22a5d | -16.33522 | -52.92131 | 2025-09-08 05:23:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dc1840ae-dd81-33a7-8f19-b7e3ecdd63fc | -16.33935 | -52.93184 | 2025-09-08 05:23:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 394953d9-1d4d-3f5c-86da-7723624d4d3e | -15.25158 | -53.82079 | 2025-09-08 05:23:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07d94df9-b1ab-391c-9bd3-fcc64fbadae7 | -14.58856 | -52.12717 | 2025-09-08 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d2e213c-bd35-3328-8eff-7a7d41e56fc7 | -15.82541 | -52.26975 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 456bf073-ce7f-32da-93f7-b2bc14a06748 | -14.885 | -55.83133 | 2025-09-08 05:23:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5bf8cc6f-9b9e-37ba-ab69-9f4b0731c647 | -16.29521 | -49.55099 | 2025-09-08 05:23:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9284d66f-951a-3eaa-b04b-3345bf09c097 | -16.3532 | -52.94078 | 2025-09-08 05:23:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| aa259361-0802-383d-9101-a9236662b0b2 | -14.52677 | -53.97509 | 2025-09-08 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81a8fd7e-70a0-3015-9f19-86a346dde313 | -15.82957 | -52.27896 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6127b008-3d86-327a-9c8b-6d6a743dffec | -12.79093 | -60.18499 | 2025-09-08 05:23:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f201ff92-bad0-3d81-b94d-96a8f7395a80 | -22.34468 | -51.91736 | 2025-09-08 05:25:00 | NPP-375D | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7e568004-b764-3443-bf0a-34cddc769443 | -22.35579 | -51.9226 | 2025-09-08 05:25:00 | NPP-375D | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| edbb0805-8e7b-3a72-b817-7152784f96d2 | -22.34437 | -51.91604 | 2025-09-08 05:25:00 | NPP-375D | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1c911573-6295-3fb5-8f22-7ae3869b1f3a | -22.35042 | -51.91792 | 2025-09-08 05:25:00 | NPP-375D | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 16d0b8d8-0012-3065-ac11-8cdf39914d77 | -22.56502 | -54.91674 | 2025-09-08 05:25:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c4a98dbe-53a5-3e82-9070-098196b23374 | -22.35546 | -51.92122 | 2025-09-08 05:25:00 | NPP-375D | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3e859f27-1ca5-3d1d-86db-58d64a061875 | -22.34973 | -51.92059 | 2025-09-08 05:25:00 | NPP-375D | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ffc3f0ab-2702-388b-8399-7cb2e3c8731b | -22.56976 | -54.91743 | 2025-09-08 05:25:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cf1da400-8895-323e-9f40-f05a77a74229 | -22.35007 | -51.92194 | 2025-09-08 05:25:00 | NPP-375D | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 882b63b6-b25b-3d77-ac5d-df1c0ec676da | -12.6343 | -56.9725 | 2025-09-08 05:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| f3ff6345-2cc0-36de-94ad-6e034aa22be2 | -7.3983 | -61.6346 | 2025-09-08 05:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 666e8e68-05c5-3b81-97de-4aa0f353926d | -11.2007 | -54.9992 | 2025-09-08 05:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 1fa47b82-8473-3357-82bc-415b715accf8 | -11.4128 | -50.374 | 2025-09-08 05:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 70200675-2315-311b-9c78-110f5d5e78f2 | -7.3983 | -61.6346 | 2025-09-08 05:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 539a8068-bf47-39e4-882f-7b46a0065bb1 | -11.4125 | -50.3955 | 2025-09-08 05:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| e15c75d5-a980-3e3b-acce-6517e45273fb | -11.8586 | -51.0705 | 2025-09-08 05:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| e00b6712-5192-3276-b0be-02c8642b06d7 | -5.76899 | -56.52072 | 2025-09-08 05:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15175ab8-dde7-3910-9338-27e0cfc46d5a | -6.62392 | -53.35025 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b863dde-875a-3394-b6bd-1fbbafeee562 | -6.63457 | -53.36113 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 20b254e5-5fea-3c5f-8e03-2297886e10e9 | -6.62896 | -53.36176 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 24530af1-164b-3a8c-8549-5c1fadb6de3e | -4.42835 | -55.16642 | 2025-09-08 05:40:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3c299fe-2609-3d1d-9b28-bbac27547748 | -6.62668 | -53.37081 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cc6f4aa8-0d3d-3e35-85a7-8063ef898a80 | -6.6296 | -53.3497 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1149a78c-ea04-359e-90d7-37ed3233a051 | -6.20313 | -53.2724 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 629a3931-fe43-35ce-8ee7-240dbc945b7c | -6.27554 | -53.4196 | 2025-09-08 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d6070d52-6832-37a8-a61f-2c2598eaba14 | -6.64111 | -53.36889 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ba488ec-fe32-32a7-bfde-cc0d95e77a09 | -5.25496 | -57.12607 | 2025-09-08 05:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4ea596fc-5b5a-3c6f-8df3-7d90a048046a | -6.62245 | -53.35401 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f42604a9-a830-3da5-970c-218a4d2973b7 | -4.42783 | -55.16995 | 2025-09-08 05:40:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fda5d63e-4aa8-34e1-8d6f-5c3a1e87d122 | -6.64026 | -53.3673 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ae7fc4c-7936-3a18-85d9-63b8d6d5255f | -6.62461 | -53.34499 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7fb075d-bea7-312c-83c6-f7e4da1d9858 | -6.19822 | -53.26765 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b46b7aa3-84bc-36ec-9a95-a61b7ff27ce2 | -6.2764 | -53.43023 | 2025-09-08 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f06a8e9e-0167-3bd9-a5b1-33b44fc8872e | -6.63237 | -53.37693 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 91ad5002-ca89-3985-b5f3-2ad111913a1e | -3.32876 | -54.91087 | 2025-09-08 05:40:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37a00216-4d69-3bf9-9e10-b5efdc20831a | -6.27708 | -53.42504 | 2025-09-08 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6174e0aa-99b1-3ad0-abcb-f3204576506a | -6.2812 | -53.42563 | 2025-09-08 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17d09fe1-63a5-39b5-937d-2001106fd9ea | -6.6333 | -53.37849 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96c7d182-20f8-3006-b679-d4a0138a4a85 | -6.62174 | -53.35921 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39c4487b-848b-30fe-b7fc-093d1bc1908e | -6.27411 | -53.42998 | 2025-09-08 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 44b30cb2-9c06-3cf7-9259-5e9174efd871 | -6.62757 | -53.37233 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e45b7dff-69d7-3d25-bd09-86e576f943af | -6.62255 | -53.36069 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11350408-8b83-3c81-b01d-026ded43ebed | -3.32797 | -54.91112 | 2025-09-08 05:40:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e719558d-cb32-3374-99a4-2d53bff043e1 | -4.73646 | -55.72327 | 2025-09-08 05:40:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39530cd9-05bd-3a36-a7f5-a5ea6131ff90 | -6.28192 | -53.42048 | 2025-09-08 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47e7ed2b-af96-33d3-9faa-4528a559f03b | -6.63309 | -53.37176 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 858bb07d-3e8b-38a7-a8b3-fd6f09cfec98 | -6.62596 | -53.37599 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 89e44da6-f856-3092-8b54-33809587897a | -4.9916 | -56.25685 | 2025-09-08 05:40:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README89.md)
