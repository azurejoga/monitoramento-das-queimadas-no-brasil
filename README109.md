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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b656442-c10e-366e-a548-40b4ffe8d8bb | -7.4365 | -61.4051 | 2026-09-01 15:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 871b7007-7d5d-3cb9-87d3-a681ae5a49cf | -13.0704 | -45.1661 | 2026-09-01 15:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 331.8 |
| c2e55286-5320-361a-a2f1-fc60f5698557 | -11.0744 | -51.5365 | 2026-09-01 15:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 147.0 |
| b03df4ce-07f5-383b-ae82-048beec686b3 | -7.603 | -61.3415 | 2026-09-01 15:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 36405547-6210-394c-8330-51e5882a8f59 | -13.0897 | -45.163 | 2026-09-01 15:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1078.2 |
| a0fe1506-737f-3ce0-8407-3ac4fc92f491 | -5.9452 | -57.6711 | 2026-09-01 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 28256b99-fd8c-3bf2-a155-6f5104622b6e | -8.7631 | -46.4418 | 2026-09-01 15:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| d8647eea-5ae2-32ef-a483-89e1afcc11e5 | -8.4988 | -55.3252 | 2026-09-01 15:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| d93eacb0-ed74-3cd0-8b1a-9e1fda6e49b4 | -17.1146 | -46.8556 | 2026-09-01 15:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 171.9 |
| 493daa87-919b-3ca6-95e6-59db6ce3ac3e | -3.4185 | -61.3461 | 2026-09-01 15:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| c6986262-f7eb-374b-89d5-f95cba2e099d | -7.4549 | -61.4044 | 2026-09-01 15:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 139.9 |
| 87f9d835-2875-3df7-a326-2ed4fe658d83 | -10.7409 | -54.0196 | 2026-09-01 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 159.3 |
| 89a235e1-c4f4-3435-8de0-1b92b272c77b | -6.9112 | -59.6467 | 2026-09-01 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.0 |
| cc589cee-73af-3991-b1e2-153426b18359 | -11.213 | -53.977 | 2026-09-01 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 17473597-a238-3b64-b243-1d5d46e0de69 | -10.3583 | -49.9528 | 2026-09-01 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 87ba6872-f2bb-3252-b5c2-07e436882ef7 | -6.6233 | -58.383 | 2026-09-01 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| cf6ddf0a-fe22-3b70-9312-6d1d3af82ed1 | -3.1267 | -61.1811 | 2026-09-01 15:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 5e390468-f9a8-34ce-8d70-8233bfc3cf36 | -8.3718 | -62.697 | 2026-09-01 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 91ef697e-67f8-3b7e-bd4d-d343e26018a5 | -8.9242 | -63.2804 | 2026-09-01 15:50:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 59.3 |
| fc1f25cb-cf4b-3e3d-a6fc-1130c2bb1c8d | -7.272 | -61.1067 | 2026-09-01 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 1e0b8062-9e63-3947-917d-aed2be47e213 | -6.0726 | -57.9583 | 2026-09-01 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| c6249b3d-94ee-3a06-b31d-8c0d2a76d123 | -14.4007 | -52.5226 | 2026-09-01 15:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 101.8 |
| ccaeb023-ad90-3deb-99ef-c544383e9b3b | -11.1939 | -53.9993 | 2026-09-01 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 4e1b48dc-f0d2-31d4-bd86-17768542cd0c | -5.9636 | -57.6704 | 2026-09-01 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 72e85a95-43e4-315c-a71c-cc88849bf951 | -13.3946 | -51.7382 | 2026-09-01 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 131.0 |
| d00a406f-d381-375a-ae7e-2220ee66b7fc | -7.4735 | -61.3846 | 2026-09-01 15:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| b8159742-009a-31c7-bb22-5da32079a525 | -10.7856 | -50.5066 | 2026-09-01 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| a8d62863-46cb-3ae6-a7be-2318535e57cc | -7.4365 | -61.4051 | 2026-09-01 15:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 5330132d-ffac-33ab-b9f5-4dd582ee7888 | -7.4803 | -63.7267 | 2026-09-01 15:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| e4b9afde-a080-3ca0-8fe5-591df3764b23 | -13.3751 | -51.7619 | 2026-09-01 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 9aab5973-fd7c-322a-8c5e-c5d1ff5592b8 | -9.5424 | -65.7002 | 2026-09-01 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.8 |
| c7db8786-e09f-36b1-9959-78e33bb7a8d8 | -3.1266 | -61.2188 | 2026-09-01 15:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 143.3 |
| 58ee9925-f7d8-3937-9bff-6c1c585aa32d | -3.4002 | -61.3276 | 2026-09-01 15:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 1ba351b6-3da6-3611-b602-f2524a559a56 | -8.7803 | -62.5103 | 2026-09-01 15:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 245e2ca9-8d87-344c-ae02-2f1cb6e806ce | -7.3663 | -55.1734 | 2026-09-01 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 0f2b27b1-78f8-3b7e-a4b0-b1fb40eb87b9 | -11.0437 | -49.6635 | 2026-09-01 15:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 8594013e-8f39-39a6-bc9d-a9692929103b | -11.2638 | -45.3241 | 2026-09-01 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 90185ca4-f818-3622-8c8d-7308a8b6258f | -8.4374 | -46.8979 | 2026-09-01 15:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 1a0e427d-fdde-3605-a48c-f52e7450af4c | -10.8017 | -50.7178 | 2026-09-01 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 4b629704-9f86-3394-8632-3042246b5337 | -5.9452 | -57.6711 | 2026-09-01 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| f3b2bb06-d0a5-387a-b008-953a8e51fdbd | -5.9451 | -57.6906 | 2026-09-01 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 2a4efe6f-f035-3200-ab6d-633932700132 | -10.1087 | -50.2776 | 2026-09-01 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 4607af4e-20d6-30e6-8b2d-378e2b566c2c | -11.2128 | -53.9976 | 2026-09-01 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 2e72b34d-4de5-30b1-9983-676aca6fd3d1 | -7.4802 | -63.7454 | 2026-09-01 15:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 16875d1f-fd43-37ce-be54-e90694710361 | -8.7804 | -62.4913 | 2026-09-01 15:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 59.2 |
| f84a1378-b5a2-3cfc-887c-5d608e51c66c | -11.2319 | -53.9753 | 2026-09-01 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 834d137b-0708-3bf6-b12a-12fa7414231b | -7.5526 | -60.4651 | 2026-09-01 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 627048b8-fb82-3020-97e9-07684f1250ea | -6.369 | -54.7655 | 2026-09-01 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| e97aeffb-24ab-3293-93c8-bd0715e9e8d6 | -3.4185 | -61.3273 | 2026-09-01 15:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| be344c6a-80cb-3dd7-82e0-51de43e6c371 | -3.79 | -59.3031 | 2026-09-01 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| d38211b7-4e53-31c7-b962-06bfe3baf76e | -11.2317 | -53.9958 | 2026-09-01 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 448a8195-7416-30de-856b-f0cde60d7aea | -6.8009 | -59.5742 | 2026-09-01 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 73b7a644-ba4e-384f-9001-e2bf87477c0e | -6.1845 | -57.72 | 2026-09-01 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 5f00c6d2-1ff8-31e8-8ebf-206e9ee64384 | -12.1457 | -44.196 | 2026-09-01 15:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 28c13410-7994-32b8-88c4-9d7e73edcef9 | -8.87 | -66.8935 | 2026-09-01 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 1ebd1905-c6ea-35df-84cd-e7cf2ddcc853 | -14.6732 | -53.5408 | 2026-09-01 15:50:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 132.9 |
| fb6193fb-31b8-3871-92e4-4c5182af6c9a | -12.3814 | -48.1655 | 2026-09-01 15:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| d175e018-2217-37a3-a065-5c4121516649 | -3.2623 | -58.2367 | 2026-09-01 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 051f2504-1698-3f40-a19d-6ab1f39c01cf | -3.1449 | -61.1808 | 2026-09-01 15:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| d4edd009-de1a-353f-8e02-d2cdf5f957ae | -9.0802 | -65.3789 | 2026-09-01 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 235caa34-5d0e-33a3-8848-a3145e077897 | -11.0434 | -49.6851 | 2026-09-01 15:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| b318cb5c-6245-3f8b-8bff-c72642642fe9 | -14.6535 | -53.5642 | 2026-09-01 15:50:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 141.0 |
| dfb0ff69-53c8-39c6-97db-56c90972fd35 | -7.7522 | -61.0878 | 2026-09-01 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| d31e1dee-8f6b-36f7-a57c-a0515f0b1e62 | -15.1827 | -46.2336 | 2026-09-01 15:50:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 23b1f3ec-c7a5-3410-ad8f-97b3fae6713e | -7.3488 | -60.5691 | 2026-09-01 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 62659fc2-2148-346a-9879-0434ffc5f8b9 | -8.3717 | -62.716 | 2026-09-01 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 8a3af661-5c02-30c0-b009-a0b30ecbb2c3 | -11.269 | -54.0334 | 2026-09-01 15:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| eb13e942-41b8-3ddd-a62a-612c9a38d26f | -10.3205 | -49.9567 | 2026-09-01 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| f7612d5d-641a-37ca-b824-f84f26478d30 | -10.7407 | -54.0401 | 2026-09-01 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 296.9 |
| af1b2501-1fb9-3879-826a-cc04cddea577 | -10.7271 | -50.6405 | 2026-09-01 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| a8619235-3229-3850-a6b0-8943fe5af4e0 | -14.6732 | -53.5408 | 2026-09-01 16:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 2a96b352-b040-3084-a893-704c6c846d00 | -3.1083 | -61.2191 | 2026-09-01 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 8821b953-dc3f-3433-9235-b39f0b8f0b68 | -7.3662 | -55.1934 | 2026-09-01 16:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| f47b8b6c-47b0-3260-a10d-751e9c371f05 | -1.4578 | -54.1966 | 2026-09-01 16:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| c72b05a5-d366-3e06-9742-ca1ee4f3804c | -11.1931 | -46.1319 | 2026-09-01 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 04d9ba56-30c6-36a5-8d1f-011b021b19ab | -7.4549 | -61.4044 | 2026-09-01 16:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| a0efe36c-22fc-3b80-a880-129a08f25adf | -5.5649 | -60.193 | 2026-09-01 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 339.4 |
| 33bbafda-7b27-38d2-be28-ce7125721e96 | -3.4002 | -61.3465 | 2026-09-01 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| ba8267d5-de38-3a7a-b6f9-d272e764a302 | -6.7514 | -55.6654 | 2026-09-01 16:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| e111574d-9e5f-3e7d-8b0f-ac11b0b6213b | -7.4364 | -61.4241 | 2026-09-01 16:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 105.2 |
| c9844759-1b63-3910-8c20-621e0742a827 | -3.1267 | -61.1811 | 2026-09-01 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 87a93eb7-e774-370e-9e67-cb8c8dc7084d | -7.5289 | -61.3825 | 2026-09-01 16:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| ca11012a-a4ba-347c-bc28-abc1b219d4c2 | -13.4184 | -51.4586 | 2026-09-01 16:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 54.8 |
| ad75e130-c6a7-3bc3-83c3-ecfe3c2193da | -7.4735 | -61.3846 | 2026-09-01 16:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 4071c055-8675-3125-9a14-4c41fdecfddd | -3.4002 | -61.3276 | 2026-09-01 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 5477174b-2452-32b2-893e-1a03436187d1 | -8.9242 | -63.2804 | 2026-09-01 16:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 57.5 |
| b2676b7e-83c7-327f-9fb3-9a0abaf0a0bc | -5.565 | -60.1739 | 2026-09-01 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 42e02637-cece-3d51-8609-61c739ac38e7 | -7.4365 | -61.4051 | 2026-09-01 16:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 95345af7-8fc8-3357-97b8-09d030df7f32 | -6.77 | -55.6445 | 2026-09-01 16:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| fa8d5749-522c-3f14-ae6f-8f9b18d98ad1 | -15.1827 | -46.2336 | 2026-09-01 16:00:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 1baf0401-78ae-376f-bb6b-c411181fbbb3 | -9.6588 | -55.0834 | 2026-09-01 16:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 58913371-5f9b-32b4-b64d-604b5a1df46a | -6.6233 | -58.383 | 2026-09-01 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| f62e48b0-6d1e-356c-97c6-0efe070fe4c6 | -6.9113 | -59.6275 | 2026-09-01 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.9 |
| cb4645e7-1678-3688-bee7-314389211cce | -3.1449 | -61.1808 | 2026-09-01 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| ea5c6939-670d-3d0e-820e-59bde2c58a47 | -11.1939 | -53.9993 | 2026-09-01 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| e4bd9198-7caf-30c9-bc56-5d8484f7054d | -3.3872 | -59.3692 | 2026-09-01 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| db7c945d-2a2c-3369-b71d-6f15d1775368 | -3.4185 | -61.3273 | 2026-09-01 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 4862311e-45c7-314a-bcc6-57e0affc9156 | -6.3875 | -54.7646 | 2026-09-01 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| cbcd0349-2efb-3989-bc7a-8796cf218de2 | -10.4961 | -59.6195 | 2026-09-01 16:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 5fe50a2a-51fe-36f1-b92e-ae8f18142f02 | -3.3504 | -59.4274 | 2026-09-01 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |


[Clique aqui para ver as próximas entradas](README110.md)
