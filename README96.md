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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c339bc4-ffc9-3f90-81e1-f184eb6e76a4 | -4.03269 | -45.35555 | 2025-10-08 06:29:00 | AQUA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 559953cf-4a95-391d-8ff1-0dd791a6d0d2 | -3.45704 | -50.08744 | 2025-10-08 06:29:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ddca930b-69ea-3e74-be2c-9b43fee354d0 | -3.11301 | -47.7947 | 2025-10-08 06:29:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a3e013d3-0dda-3bcf-8138-3fb5ae411926 | -9.1855 | -47.79214 | 2025-10-08 06:29:00 | AQUA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| a922b912-5f36-38cf-a6ff-2fa688d9395c | -12.49942 | -54.7171 | 2025-10-08 06:31:00 | AQUA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 72cfd067-fa1b-3528-a153-6eb94995047e | -13.19991 | -51.69677 | 2025-10-08 06:31:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 00e5fcc6-fda9-3c47-afa1-6ba4e299d504 | -10.67576 | -54.68539 | 2025-10-08 06:31:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 24e52d50-3bdd-3553-bf23-6cfc1db1f8fb | -11.76595 | -50.93012 | 2025-10-08 06:31:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| af28124c-7f24-340f-bee2-66697a842ad9 | -11.76599 | -50.92311 | 2025-10-08 06:31:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 8169ae21-6905-31dc-891c-5f51f6e0506a | -11.41278 | -55.07212 | 2025-10-08 06:31:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d6e99127-56b2-3702-9550-970b345cf19e | -10.67442 | -54.69438 | 2025-10-08 06:31:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0ad6f78c-4837-3998-90de-d17ab0f48ba4 | -12.50836 | -54.71844 | 2025-10-08 06:31:00 | AQUA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 675b5f45-0340-3c98-bd06-b9c922c44689 | -10.91681 | -51.00146 | 2025-10-08 06:31:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 5f7398c3-6093-3f46-8ad4-26d0ab64bd45 | -11.18139 | -54.89001 | 2025-10-08 06:31:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 59acbb5a-b228-3ba6-96f4-d4f79511dde0 | -14.61697 | -52.46322 | 2025-10-08 06:31:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3c675f9a-069b-3057-b69b-5444472a58ce | -10.87033 | -53.73525 | 2025-10-08 06:31:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b98260da-2c28-360c-9488-12691e2d3d39 | -11.7249 | -50.97694 | 2025-10-08 06:31:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| f89b1319-3d68-33b7-a5f8-fe6229e88554 | -12.39193 | -51.12542 | 2025-10-08 06:31:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 57395938-2d24-38c3-a015-6513e48aca38 | -11.16371 | -54.88738 | 2025-10-08 06:31:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 320f8744-5ded-350f-86b7-d72c373602db | -14.61529 | -52.47595 | 2025-10-08 06:31:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4b407073-0760-3d82-86aa-878e33fb1703 | -10.91489 | -51.01539 | 2025-10-08 06:31:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 661c9f2e-ed89-32e9-81cf-dc635a9dd2b8 | -11.18273 | -54.88102 | 2025-10-08 06:31:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 25.1 |
| afcaa4c7-cb10-3010-bf49-735a365a7718 | -11.76973 | -50.90075 | 2025-10-08 06:31:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 151dc36e-6428-39f4-9719-b2bdbabcdf6d | -12.25774 | -47.85749 | 2025-10-08 06:31:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 65f4480d-c0b5-3990-abcf-719149cc97d4 | -15.99085 | -50.95853 | 2025-10-08 06:31:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| f40cc407-2ee3-362a-9578-0c74a6360067 | -11.71385 | -50.97546 | 2025-10-08 06:31:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d781cf61-8919-3bb4-b631-71ecbc61546d | -11.75489 | -50.92162 | 2025-10-08 06:31:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 03c2b2e1-438c-3c09-8887-96d5ed044441 | -11.11249 | -54.04158 | 2025-10-08 06:31:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 281f0014-7544-3ce5-9daf-721e305de331 | -15.63553 | -52.55524 | 2025-10-08 06:31:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 70330f44-66fc-3612-af07-305a2a37fb60 | -12.24698 | -47.86267 | 2025-10-08 06:31:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 4bef9afb-ec39-31ef-96d0-ab6ddb8acefe | -11.76784 | -50.91544 | 2025-10-08 06:31:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 004b044f-166b-3c18-99ec-8d9462957ef8 | -11.16505 | -54.87838 | 2025-10-08 06:31:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 06241a0e-6314-3f68-9786-9fa129a48bfc | -11.17522 | -54.87071 | 2025-10-08 06:31:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| db6e535a-a157-3770-b13a-1443cc2ab79d | -11.38199 | -54.33905 | 2025-10-08 06:31:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d4314884-462c-3b57-a6bb-3e1aa8b89969 | -10.89505 | -50.99849 | 2025-10-08 06:31:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| b36457d6-27ca-34fb-8903-e9df59f569c9 | -11.38062 | -54.34834 | 2025-10-08 06:31:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 677ada5c-dbdc-3713-ab56-46f0dabc1aed | -11.76799 | -50.90845 | 2025-10-08 06:31:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| fee490ad-2d82-376e-9567-b23461b54932 | -11.17255 | -54.88869 | 2025-10-08 06:31:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 145.7 |
| 90625f53-e8ca-3a8e-94d5-a6311b1a982a | -14.6499 | -52.53149 | 2025-10-08 06:31:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 235b34fd-bd4f-3d20-99ca-c73dfacad088 | -18.0336 | -51.14901 | 2025-10-08 06:31:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 88998105-ca2c-3540-a866-d1675b24b710 | -11.11387 | -54.03212 | 2025-10-08 06:31:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| acaed3f7-c8cd-3853-9f5a-d2c3da4bdec5 | -14.62566 | -52.47708 | 2025-10-08 06:31:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ddbca0a8-d238-3357-a331-4141de143c38 | -10.90593 | -50.99999 | 2025-10-08 06:31:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 3aae113e-2ab0-31d5-bb40-bcd118190ac4 | -10.89316 | -51.01245 | 2025-10-08 06:31:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| cfc1eb9b-1dc3-3eba-ab5a-30bc44c0f437 | -15.63724 | -52.5422 | 2025-10-08 06:31:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cc012f1f-e682-310b-9851-c0c3275642a2 | -12.24318 | -47.85762 | 2025-10-08 06:31:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 143608b7-a6fc-3f7f-9dca-78796eae65f4 | -11.72684 | -50.96243 | 2025-10-08 06:31:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| a30515a8-2fcb-3ab3-a83c-8bcc58420b78 | -12.51729 | -54.71976 | 2025-10-08 06:31:00 | AQUA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| cb6042f0-7d0e-3265-b752-024386735c30 | -11.73986 | -50.94936 | 2025-10-08 06:31:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| a384c47d-fbe2-368d-857b-50f311cd1828 | -15.20327 | -56.77625 | 2025-10-08 06:31:00 | AQUA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e0636086-a555-3806-91a4-3df3776410eb | -11.75291 | -50.93625 | 2025-10-08 06:31:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 28.0 |
| bc7889b1-2e02-32bd-8359-5de0bdbb1e1f | -11.14604 | -54.88473 | 2025-10-08 06:31:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8c64b373-ef76-34de-87ff-6730c1ac00dc | -12.25007 | -47.8361 | 2025-10-08 06:31:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| a581fe7d-8629-3610-8f79-eb4c08144de7 | -12.39362 | -51.13107 | 2025-10-08 06:31:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 10881d53-d555-327b-b339-81d61315095f | -11.76999 | -50.89376 | 2025-10-08 06:31:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b8eb39b2-e906-3af6-b580-b68643800847 | -15.75344 | -48.71092 | 2025-10-08 06:31:00 | AQUA_M-M | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 26.4 |
| a1cf3f09-5d28-3e39-8117-c0d1666e00f1 | -18.02368 | -51.12944 | 2025-10-08 06:31:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 23.0 |
| dabf4e49-a7c9-3a18-b3b9-570001a52475 | -11.12153 | -54.04292 | 2025-10-08 06:31:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 06e0258c-d428-3789-b7ec-a6a4e005829b | -18.02151 | -51.1476 | 2025-10-08 06:31:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 89.1 |
| ce21915c-021c-3ae1-ac7b-c2e840f6a41a | -11.17389 | -54.87971 | 2025-10-08 06:31:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 584b9766-0187-3557-87fc-3168197f3068 | -11.33576 | -56.19925 | 2025-10-08 06:31:00 | AQUA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 7098d162-163e-3c97-885d-f690d3f8f80e | -15.63383 | -52.56816 | 2025-10-08 06:31:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 5e38a75b-c58e-325f-9625-d0933d260783 | -15.98666 | -50.94735 | 2025-10-08 06:31:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 3428fcbc-e48c-34d5-9272-f55573534bbd | -10.90403 | -51.01393 | 2025-10-08 06:31:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 601c1580-c113-338d-af4f-0ca51f8e2828 | -11.17122 | -54.89767 | 2025-10-08 06:31:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 4ade73e7-cbb5-37fb-b9f1-84668d6d4c27 | -15.19772 | -56.81266 | 2025-10-08 06:31:00 | AQUA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e43ae39d-49ae-37e4-a23c-29e6ac81bec2 | -17.82822 | -57.62275 | 2025-10-08 06:33:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 1536c05e-452d-34bd-bd94-2956da443d9a | -18.01889 | -57.51749 | 2025-10-08 06:33:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 82c32766-b83f-308f-aab6-98ae63dd48ec | -18.0559 | -57.52081 | 2025-10-08 06:33:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.3 |
| db0b08eb-b3c7-36e4-8329-7431e3d6c1d5 | -17.85162 | -57.58853 | 2025-10-08 06:33:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 43feec04-a78f-3831-89ed-d342f961464f | -17.82541 | -57.64101 | 2025-10-08 06:33:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.8 |
| 48c8db11-cddd-3b64-b316-ab4688b965ce | -17.9262 | -57.51535 | 2025-10-08 06:33:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.5 |
| 31dc0328-6ad8-32b1-8f47-366fc6091043 | -17.94544 | -57.52437 | 2025-10-08 06:33:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 1840faf4-b310-3e9a-91b4-c2b1bc0ad22d | -17.97757 | -57.49184 | 2025-10-08 06:33:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.6 |
| aabdb35f-6287-341c-a39b-4da39e15cf53 | -17.93943 | -57.50451 | 2025-10-08 06:33:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| e796a893-8ed8-328b-9ff8-16b6185ed417 | -17.93663 | -57.52286 | 2025-10-08 06:33:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.4 |
| 8a81f869-7c6d-3e2f-8180-f4b5173b9dbf | -17.94402 | -57.53364 | 2025-10-08 06:33:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| e20f7aa8-4b1c-30b5-a710-56b41cc774d6 | -17.8268 | -57.63192 | 2025-10-08 06:33:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.9 |
| 46b38bd1-3272-3372-bea5-d5881e80a0ee | -18.05311 | -57.53902 | 2025-10-08 06:33:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 11433dc8-9b90-3326-a549-78a8c8d466c8 | -18.0203 | -57.5083 | 2025-10-08 06:33:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 019817eb-6733-3207-88fb-3ee3159631ff | -17.86218 | -57.63773 | 2025-10-08 06:33:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.0 |
| b4f6550a-0e15-33c9-9867-56bad83be2a1 | -17.93521 | -57.53209 | 2025-10-08 06:33:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| bda3626b-fc28-3681-9293-4d9753f1a0ae | -18.05451 | -57.52987 | 2025-10-08 06:33:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 185a9b36-2245-382e-8858-d5473bdfbc17 | -17.92761 | -57.50623 | 2025-10-08 06:33:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.7 |
| c081bad0-0615-39a0-b54e-2c60735ba124 | -18.01325 | -57.55435 | 2025-10-08 06:33:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 319e4fe7-bd05-3261-b91c-410e181131e8 | -18.0259 | -51.1371 | 2025-10-08 07:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 232.7 |
| a121ba2b-029c-323d-8142-786393f73bd8 | -18.0458 | -51.1336 | 2025-10-08 07:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| fef8d334-f414-3fcb-a57f-d9d4d5f0269b | -18.0254 | -51.1591 | 2025-10-08 07:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 188.1 |
| e6ca20d4-e1db-3d3f-88ad-e3f9e388356f | -18.0453 | -51.1556 | 2025-10-08 07:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 4b5a9d16-fab6-3568-9bde-e77d45201ed2 | -18.0458 | -51.1336 | 2025-10-08 07:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 54185464-7e4e-3ebf-b67c-22678b6e243c | -18.0453 | -51.1556 | 2025-10-08 07:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 8ca91660-6131-3393-8a1d-9ff1dbfcf633 | -18.0259 | -51.1371 | 2025-10-08 07:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 236.9 |
| becbeebe-6715-35ae-b6cc-91ce7760f29e | -18.0254 | -51.1591 | 2025-10-08 07:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 164.1 |
| 274866fe-a00b-31de-8efa-636be1edb63a | -21.6049 | -51.6554 | 2025-10-08 07:20:00 | GOES-19 | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.8 |
| bff8f85d-d49c-35a8-8101-4748a80c1361 | -17.9421 | -57.5104 | 2025-10-08 07:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 1e5fc6ba-feab-3369-b93a-448f200e396c | -17.9224 | -57.5128 | 2025-10-08 07:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.8 |
| 0b2cd418-addb-3e82-96ae-531190eb85ad | -12.5107 | -54.7345 | 2025-10-08 07:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| a8667825-6f3e-3687-a8f2-cbb02ce7d8bf | -12.5109 | -54.714 | 2025-10-08 07:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 5acdcd4c-646e-3112-b53e-472cb7507e4b | -17.9224 | -57.5128 | 2025-10-08 07:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.1 |
| 26f176f1-282a-379a-8ca9-3001d9193fb7 | -17.9421 | -57.5104 | 2025-10-08 07:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.8 |


[Clique aqui para ver as próximas entradas](README97.md)
