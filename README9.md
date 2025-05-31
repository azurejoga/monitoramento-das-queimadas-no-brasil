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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d19da613-443a-3f69-8beb-d09bcb5cc767 | -12.54733 | -48.49855 | 2025-05-31 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fde9ca81-f85e-3fd1-80f2-ec3bf4da193e | -16.11675 | -46.82432 | 2025-05-31 04:27:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b21def8e-b4a4-3589-b49e-6ab8dc0a26a2 | -12.60138 | -48.3729 | 2025-05-31 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3175a54e-bfb1-3c94-8cbd-7ff71502f964 | -11.82895 | -51.27747 | 2025-05-31 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| efc00be6-c31b-36a4-9abb-f5c5bd37e4d4 | -13.09751 | -45.27697 | 2025-05-31 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92dcb1e0-9001-3317-a0b2-6170af09d7fb | -13.20007 | -47.90054 | 2025-05-31 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 421bd756-6495-39f4-895f-727678c5986d | -13.10275 | -45.28999 | 2025-05-31 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed64a7d1-902f-38eb-8059-db644c0d8883 | -11.91486 | -54.4228 | 2025-05-31 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6998cd0d-e777-32a8-81c2-c18e0e98275f | -10.83292 | -56.9515 | 2025-05-31 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 056d6fbd-cc97-341e-977c-7e4206efa30b | -11.78533 | -54.77246 | 2025-05-31 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b68866a-154f-357c-8ffe-d66878fb14d9 | -10.82684 | -56.95404 | 2025-05-31 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e21bd049-5dc2-3b57-87f4-ed013d3b9859 | -13.14178 | -44.0827 | 2025-05-31 04:27:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fff28ba9-b9a3-3f00-9630-7df3f3af5193 | -14.61858 | -47.96616 | 2025-05-31 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1df1bc25-5836-3874-a469-c13f54049308 | -13.63433 | -47.447 | 2025-05-31 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 591b0924-f929-34bc-8698-abb943d357df | -16.12409 | -46.82164 | 2025-05-31 04:27:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a23f5a73-5e4a-3020-b66d-c2ff3c9841ca | -11.72904 | -56.42466 | 2025-05-31 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1cf37f1e-3323-3900-abf1-9718d4c484df | -13.09984 | -45.28547 | 2025-05-31 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a33c9476-e926-34db-acb6-c1453e2074b2 | -10.65134 | -49.43145 | 2025-05-31 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| dd31afb9-c2c7-30bb-bae0-6f46d32fd57c | -14.02217 | -55.14 | 2025-05-31 04:27:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a1b2a177-96bc-3e67-beca-4e924a810096 | -10.46718 | -47.94372 | 2025-05-31 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e442d2c4-5a4f-3b6c-97ac-ea26e04e374a | -13.25129 | -50.13136 | 2025-05-31 04:27:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8e68d7f1-3826-352a-8686-b47de8c540b8 | -13.10101 | -45.2775 | 2025-05-31 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4d138df4-b256-3207-92b6-18519534d866 | -11.45047 | -49.09827 | 2025-05-31 04:27:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 13a101f9-8bdc-3613-8cba-e6749f2554f0 | -12.60461 | -48.18153 | 2025-05-31 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f60675ec-3ce2-3b60-b898-2a646726c9c7 | -11.68997 | -48.25924 | 2025-05-31 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0495c1a3-efe2-362c-92e6-ba2942527e85 | -9.13535 | -49.65124 | 2025-05-31 04:27:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 950aa672-9428-3b6d-ae4a-ec5f65763dd2 | -9.26971 | -47.91554 | 2025-05-31 04:27:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fad869ba-8add-3efa-a41c-e8a93b578759 | -12.27505 | -44.58731 | 2025-05-31 04:27:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1545896-bbbf-3b91-8a90-f315a968613d | -12.1864 | -54.25178 | 2025-05-31 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc387ecc-cbc5-34fb-b707-1e9a9931cbd0 | -13.09117 | -52.04793 | 2025-05-31 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b2949b86-317d-3892-9953-5389713c26f5 | -13.63764 | -47.44755 | 2025-05-31 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13d8ffb7-c6e3-369c-92fd-19d1219ca13f | -8.81089 | -49.83607 | 2025-05-31 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4722f6b5-2d92-3ee3-a440-56f1a0653646 | -11.14272 | -53.92784 | 2025-05-31 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ad9713f-15a8-3ad6-b206-2af877f8cfeb | -13.64094 | -47.4481 | 2025-05-31 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 975ee46a-dca6-3691-b921-ef3fadae68eb | -12.01682 | -49.53123 | 2025-05-31 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 95351218-aae7-3a68-82e8-8c3570cc3c39 | -13.09343 | -45.28042 | 2025-05-31 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c0ecd4a-f892-341c-9311-c5b0315de2d5 | -12.01123 | -49.52259 | 2025-05-31 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ac96860-6eb4-3a80-b7ce-5f0dd46e7b93 | -12.37423 | -54.16625 | 2025-05-31 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00bc799c-1013-3f16-81e7-a9b7c4da22dc | -14.83629 | -48.09663 | 2025-05-31 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 00d49899-9fd2-3e42-bc4f-a438a6db5da6 | -9.39817 | -48.41608 | 2025-05-31 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d24f3a6b-808f-32d2-9973-51dfd746c65a | -10.65217 | -49.42826 | 2025-05-31 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b0cee05c-2f71-37c9-9f3e-7c7ed53473a9 | -8.81445 | -49.83666 | 2025-05-31 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4ce5da4-a012-32ac-9397-cc76dcb4f873 | -16.11731 | -46.82053 | 2025-05-31 04:27:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fcab6bb2-2c1f-30a3-81b9-cfd5b9a12c1b | -11.45385 | -49.09883 | 2025-05-31 04:27:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6adf74be-f773-3a63-b311-c2c239ad34bc | -10.45612 | -47.94915 | 2025-05-31 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| caabe8c0-4b47-307c-b0bb-fc4930a36506 | -9.13118 | -49.65465 | 2025-05-31 04:27:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6eafb05c-4648-3567-bdac-b598945746d1 | -11.7878 | -54.78035 | 2025-05-31 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f2d7f85-912a-302d-ad10-7cbb2602e4bd | -11.14035 | -53.94115 | 2025-05-31 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 55869c37-97fc-313d-a495-dbc303c42252 | -10.64751 | -49.43527 | 2025-05-31 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a05024e8-440f-34ec-b5cd-8f17d84f83f5 | -10.8288 | -56.94354 | 2025-05-31 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8e6363f8-896a-3008-8b6e-2d9f09a11538 | -11.50705 | -48.233 | 2025-05-31 04:27:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c22585a-e49e-3347-abb2-0d869a596d61 | -11.90951 | -54.81803 | 2025-05-31 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 856902f9-b2e8-39f2-a99e-36422160bdd2 | -9.60705 | -49.02273 | 2025-05-31 04:27:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e696e753-0e62-3b7f-9ad4-ba958e059c22 | -11.90818 | -54.82127 | 2025-05-31 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4061482-53ef-3e21-b894-630358e79e49 | -15.37253 | -45.67639 | 2025-05-31 04:27:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 958ab6fb-a036-3f91-8014-6d63c779377d | -9.59144 | -48.73096 | 2025-05-31 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e589d2bd-f6d9-3401-877d-4ad793fd72fd | -11.83046 | -51.26855 | 2025-05-31 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 41f0635a-1479-38ad-ba52-e11906965b22 | -9.72509 | -48.32846 | 2025-05-31 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 648e96b4-554b-3985-b288-94a1ab3e0c41 | -14.9972 | -48.3087 | 2025-05-31 04:27:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3088cb9e-99ae-3b38-be0b-cfd073e5052c | -13.63995 | -52.18436 | 2025-05-31 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbf87851-dee1-3920-a41a-79412391efb8 | -10.7741 | -47.55186 | 2025-05-31 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6eebf99b-6575-35e9-8a23-6e588608d3b8 | -15.88275 | -43.45366 | 2025-05-31 04:27:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dad5ce8d-73d9-3029-b4ca-c61deb81415a | -12.90808 | -55.04488 | 2025-05-31 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd58f373-3c5d-31f9-90f8-41ece00779ef | -11.13956 | -53.94558 | 2025-05-31 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b16110d9-46ae-3882-9361-4b58d6a88080 | -15.88626 | -43.45782 | 2025-05-31 04:27:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 1cee2675-5467-3f65-a8f9-7e46d06cfe63 | -8.80956 | -49.84424 | 2025-05-31 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a45fd743-4a97-38d0-aea3-dd5d147c85ce | -9.52613 | -54.76466 | 2025-05-31 04:27:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2be49b8d-5ccc-3d8f-bae9-38d14879506b | -15.13743 | -49.56421 | 2025-05-31 04:27:00 | NOAA-21 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7c65c31-65d1-3fd4-83f3-6b7d526b62e2 | -10.65477 | -49.43202 | 2025-05-31 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 13a3f825-fa0f-32e9-bde6-3ffaab84d335 | -12.63195 | -51.6834 | 2025-05-31 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2d464a71-6be6-30e7-83cc-04cedebc9287 | -11.02264 | -45.23677 | 2025-05-31 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a31f8de-58a2-31bd-b2d1-6dce3628b7a6 | -13.93995 | -54.49102 | 2025-05-31 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e0bcf32-ad0c-3fd7-87f8-a2774b8d954a | -10.65155 | -49.43204 | 2025-05-31 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b4c1b223-4458-377a-9688-4f57b4a26f70 | -13.10625 | -45.29051 | 2025-05-31 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4aa6c365-022b-3769-b11d-f70131fe5151 | -16.68069 | -43.88321 | 2025-05-31 04:27:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 291fccfa-cf21-3bd1-9cd3-2128d10b2890 | -13.62773 | -47.4459 | 2025-05-31 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 148283c7-1f18-3b3d-9730-c542a0bb9260 | -11.68665 | -48.2587 | 2025-05-31 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6cc84c38-8d67-3e93-8efe-e9ee4698d527 | -9.27304 | -47.91608 | 2025-05-31 04:27:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4adbc028-215c-3606-a943-ef38405c760d | -13.94944 | -54.4884 | 2025-05-31 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2735488f-431f-3d73-9fe1-a25d97c8e0d7 | -14.07454 | -47.65601 | 2025-05-31 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de0f2e1e-dc43-3ce2-8c40-df6485c3e7cf | -11.07747 | -55.057 | 2025-05-31 04:27:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f0dbf6ce-301f-32dc-9426-691712851720 | -13.10043 | -45.28148 | 2025-05-31 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a405593c-af18-3143-9d16-3bc5d583b378 | -14.82914 | -48.09907 | 2025-05-31 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b34ba4b5-8512-3294-9c33-919f2d5b11e1 | -11.82601 | -51.2724 | 2025-05-31 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| eea22fa8-85a6-3b19-aa11-783a09ef3510 | -11.8334 | -51.27362 | 2025-05-31 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 1619df94-34f9-3084-bf2f-22dfc744138f | -17.0949 | -43.80405 | 2025-05-31 04:27:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6e4dfcf-89c6-3415-84a3-9c6cfa57bd76 | -13.09872 | -52.04937 | 2025-05-31 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e75a5269-c0a2-393f-948f-0c3d5d6a35c0 | -11.12992 | -54.21957 | 2025-05-31 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d851cb59-a11f-3f34-ac62-7b6b6b1bb6cb | -10.65071 | -49.43524 | 2025-05-31 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 20a43164-1515-3e4a-83cc-431aad7dc6e8 | -14.02703 | -55.13365 | 2025-05-31 04:27:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d5835dd3-96a4-33b8-8fbb-77083ec7c898 | -12.02485 | -49.52488 | 2025-05-31 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a4e4b452-8496-3fbd-bcfb-a724a168767e | -13.85649 | -43.52297 | 2025-05-31 04:27:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9431b1e1-7fa8-359d-abff-8b3c4305ef18 | -13.09955 | -52.04461 | 2025-05-31 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49c81fd3-f8d4-3d18-bf28-7ce5282efe09 | -11.13186 | -54.22196 | 2025-05-31 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebe4084b-178d-34ed-adc3-9ef6a646a362 | -12.02947 | -49.51797 | 2025-05-31 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7ccae9b9-c015-3efd-99a6-7074bf664460 | -12.12409 | -54.5975 | 2025-05-31 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f56b4a35-e7ff-3826-bb52-1a9cd5822449 | -9.31728 | -49.49004 | 2025-05-31 04:27:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b76ce75d-e045-3f54-a251-4616f6827f48 | -10.69028 | -57.64745 | 2025-05-31 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c1621a2-5db7-318a-881b-7e42d95c3bfb | -12.08592 | -54.57611 | 2025-05-31 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5f96aa74-878c-32d9-8e6a-b0f6251e6c1c | -11.91934 | -54.42368 | 2025-05-31 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README10.md)
