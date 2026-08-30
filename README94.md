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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6cc0026-3c5c-3c77-80b0-e9d0e69164e0 | -8.5925 | -66.9379 | 2026-08-30 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| d6f5e75d-2117-3bdc-9bb5-2253cc91ac82 | -9.9282 | -60.5049 | 2026-08-30 15:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 113.3 |
| c06d9492-8661-3681-9e45-e57e4eb5c219 | -15.2478 | -53.8666 | 2026-08-30 15:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 376.7 |
| b27419f7-2f84-3222-a101-973ccbd402fd | -10.9932 | -50.5484 | 2026-08-30 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 46bd4289-400e-383c-9401-ba22d5c2d6eb | -7.5662 | -61.3049 | 2026-08-30 15:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 7306a254-e97a-39ac-bbf9-3a724e0f3fe8 | -7.9169 | -61.3671 | 2026-08-30 15:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 1765f31a-ebbb-3316-bcea-18dd138c9550 | -13.3991 | -51.461 | 2026-08-30 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 8fa1c294-adef-322a-8179-05ca1e44306a | -9.0058 | -65.4373 | 2026-08-30 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 0047ec9c-8670-3def-9c09-8deabf5d1bac | -13.4379 | -51.4348 | 2026-08-30 15:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 109.9 |
| e7eb5811-dbe2-364d-a9ce-46c0e57a1b7f | -5.7197 | -52.28 | 2026-08-30 15:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| c31ad4fc-0a72-3f43-9c39-95c9d77c6bd5 | -8.5739 | -66.9754 | 2026-08-30 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| b546ba15-d5e9-36d9-8dc8-54e0a62a2a97 | -11.1441 | -50.5961 | 2026-08-30 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 927e9656-a6b6-3241-93af-a173551f6080 | -6.9363 | -55.6958 | 2026-08-30 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 9e35e473-0500-3030-a6a4-6ab62ebd38e6 | -13.3995 | -51.4397 | 2026-08-30 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 5c89fd74-3e35-384b-9758-18f1ffbfcd21 | -9.1662 | -60.2752 | 2026-08-30 15:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| f44a61fe-fcc7-304a-b4e6-6b51e3f2ca2e | -8.5925 | -66.9564 | 2026-08-30 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 194.5 |
| 9c18c1ab-6424-34cc-be8b-13ef132a6b11 | -10.8025 | -50.6539 | 2026-08-30 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| a4701fd1-e068-3a77-b89e-ef30424d4ed5 | -13.4187 | -51.4372 | 2026-08-30 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 190.5 |
| f694ddd6-942b-3afc-a1f2-fcb6e1083354 | -6.6397 | -53.173 | 2026-08-30 15:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 2825978c-8ed9-3958-bd20-a499924ac427 | -10.899 | -50.5159 | 2026-08-30 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| c036dce4-dfa6-39aa-90e4-7ca739199a63 | -11.0247 | -49.6656 | 2026-08-30 15:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 99e2bb53-1b65-3096-855a-aed90dcbae74 | -11.2443 | -45.3497 | 2026-08-30 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 238.3 |
| 4260ae3b-30d4-3b02-b5ab-771cd3a0e6bd | -15.2482 | -53.8456 | 2026-08-30 15:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| ec4ccdf3-da0e-3069-b127-41544c80abe5 | -5.4876 | -57.1416 | 2026-08-30 15:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 153.0 |
| 67fed1cc-a964-3728-b850-fc375a3668d6 | -8.3679 | -57.6737 | 2026-08-30 15:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 845dcc69-d124-3d25-9a18-e9248b736f87 | -11.3431 | -45.1521 | 2026-08-30 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| d1e657b3-6bae-3376-8e3e-e6cd26c2acf8 | -10.7598 | -54.0179 | 2026-08-30 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| be6df088-e7e6-31d3-bd20-1ea548c7bbe5 | -7.5478 | -61.3056 | 2026-08-30 15:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 5e0ac0a5-84f2-3336-80b4-95859da98002 | -11.1821 | -50.592 | 2026-08-30 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 36e91683-74a5-3cf3-b12f-3d5728136af6 | -7.1312 | -42.7708 | 2026-08-30 15:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 133.5 |
| 338d9fe4-95fd-3ef1-8798-b0232201efe0 | -11.2294 | -45.099 | 2026-08-30 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 560.9 |
| de542169-8b68-3788-a7c7-4fa756e61bd5 | -4.1699 | -60.6874 | 2026-08-30 15:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 1c7c6780-4287-3403-8efd-12b9e88a9221 | -10.7649 | -50.6366 | 2026-08-30 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| f04bf1ce-1f74-3fad-9d3c-62223a05b5d3 | -11.2314 | -54.0164 | 2026-08-30 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 164.5 |
| 565138c8-57ac-356f-b11a-aa42baa6d91d | -10.7409 | -54.0196 | 2026-08-30 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 8e560663-b5e9-3802-b3f9-ad9f7ef88197 | -3.1815 | -61.1613 | 2026-08-30 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| db72a588-c733-3e7d-9ad7-cadb9547784c | -6.8568 | -59.4757 | 2026-08-30 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 489.7 |
| cd16f6e5-62fb-3a8b-8198-b31c5d6599d5 | -7.3294 | -55.1555 | 2026-08-30 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| acb41119-1e9b-326e-9fbc-1afa61d44e69 | -21.0172 | -57.8313 | 2026-08-30 15:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 69.0 |
| cdf6c23f-7f54-3d2a-b4a8-dbf59631d6b9 | -11.3619 | -45.1724 | 2026-08-30 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 236.1 |
| 96df3435-3d13-3c96-bf74-97cc99a8016e | -9.0723 | -60.4148 | 2026-08-30 15:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| ca6b99f5-0814-3361-bf8a-75d7f37fa7dc | -10.8611 | -50.5199 | 2026-08-30 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 861f4673-4fb8-3f29-b895-359b740ce3f6 | -6.8019 | -59.4008 | 2026-08-30 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 7b61f4c3-b35e-3b48-a745-95e6954ad7a0 | -10.9364 | -50.5545 | 2026-08-30 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 40.9 |
| f276543a-946b-3815-b1b1-f1fceb823f66 | -8.2229 | -54.9412 | 2026-08-30 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 1e7ecba4-b097-3fc9-b243-52d7ed5e19c0 | -9.1661 | -60.2945 | 2026-08-30 15:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 118ae63c-72e7-3639-856f-1cff69e5e77c | -15.3655 | -52.6703 | 2026-08-30 15:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 13d6b058-08af-3c9d-a490-ae4c7ed77c83 | -5.9635 | -57.6899 | 2026-08-30 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| f8e34d3e-c23c-3658-8ffb-78ccf52e0150 | -9.874 | -60.2762 | 2026-08-30 15:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 1598b8e4-b93c-3861-81ff-228ba43c6409 | -11.1349 | -49.9117 | 2026-08-30 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 5735f9e9-8d90-31a5-8408-de8c842fd8a5 | -7.3302 | -60.589 | 2026-08-30 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 3d9c7b29-6c45-356b-91d8-f4c8148149e7 | -4.9605 | -55.8226 | 2026-08-30 15:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 2e5c4a12-7353-3a28-896b-6985b6215227 | -5.982 | -57.6697 | 2026-08-30 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| f7534b12-130c-3bf9-8b75-65bea521a94f | -6.7884 | -55.6635 | 2026-08-30 15:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 95450ec9-353f-3087-be45-066b557c0971 | -8.6158 | -54.7541 | 2026-08-30 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| f83e73f3-9ee3-3d4e-8c69-5a09d51fd5ba | -10.5412 | -50.4042 | 2026-08-30 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 7e8059bf-9761-30be-93ba-2d6ff8397d3b | -6.9022 | -52.8304 | 2026-08-30 15:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| c677c8c1-7b59-3a50-ab45-d2defb71cbfa | -14.4197 | -52.5413 | 2026-08-30 15:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 176.9 |
| e92feb6b-fa87-35c6-8d0f-a979a26d2514 | -10.7839 | -50.6346 | 2026-08-30 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 004dd7f5-7110-33fa-b94d-6879956c0c2d | -21.0172 | -57.8313 | 2026-08-30 15:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 84.3 |
| 8a44ddc4-7e73-39e4-84db-5a46753dc741 | -11.1821 | -50.592 | 2026-08-30 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 3171e6de-0f22-35e3-a2d9-fb8d0d42241a | -3.4943 | -54.6567 | 2026-08-30 15:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 6661575d-273e-3da0-b4d1-006772e2630a | -5.9819 | -57.6892 | 2026-08-30 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 4ccee1d2-7e76-35b8-80a3-a1768ef65c83 | -7.3302 | -60.589 | 2026-08-30 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| a782a13d-903b-38d9-b2f5-f1af801ea8a8 | -9.1525 | -59.619 | 2026-08-30 15:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| f98ffe06-6578-3ea7-9b1b-19fdf463be8c | -7.917 | -61.3481 | 2026-08-30 15:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 50a4666e-7994-35b1-b6d5-f546c9631423 | -10.8463 | -50.2224 | 2026-08-30 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 179e02e4-cfb1-362b-a140-040a49995960 | -11.1723 | -51.294 | 2026-08-30 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 38.5 |
| a91cffef-1278-33de-9512-322ce5ae93e3 | -9.0429 | -65.4361 | 2026-08-30 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 1bacd81c-6fe0-3daa-bd2f-af95b08e9a61 | -10.7647 | -50.6579 | 2026-08-30 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 1b6a5efc-b6f6-3e8c-8abc-423c98e8fc51 | -13.4187 | -51.4372 | 2026-08-30 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 164.9 |
| b49d3fae-1cd6-3996-af2f-2b937591fa8f | -10.1348 | -45.7006 | 2026-08-30 15:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| c693adb3-5754-3105-99e7-59baaab0577d | -9.9281 | -60.5242 | 2026-08-30 15:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 23fa74c4-94b8-3f84-b441-696a864dbe16 | -11.3622 | -45.1494 | 2026-08-30 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| b0b03219-4cc0-38b3-bcbc-a1723082eda7 | -9.2262 | -65.8784 | 2026-08-30 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 229.6 |
| 0720f4b2-a74f-37bc-b5ef-eb2acb9e1083 | -21.0176 | -57.8103 | 2026-08-30 15:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 60.1 |
| 49d81161-0713-397b-8759-435d039daec2 | -10.8249 | -45.3382 | 2026-08-30 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 2d2b73b2-093e-3e10-a60a-5a1ee861acca | -10.4774 | -59.6207 | 2026-08-30 15:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| e2a448cd-e25d-3a49-bc55-9f22d1c79c0a | -6.0 | -45.0889 | 2026-08-30 15:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| cc9c92b9-1496-34fb-94a2-c287f6cafe6a | -7.7863 | -61.5818 | 2026-08-30 15:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| d036d394-8a65-3a60-b807-08244032ac1b | -6.9363 | -55.6958 | 2026-08-30 15:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| d0841f1c-eb20-330a-8501-205c200cc9a9 | -10.3226 | -58.0847 | 2026-08-30 15:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 6347521d-eac3-3f00-989d-3c00840411ae | -10.5409 | -50.4256 | 2026-08-30 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 905f1943-d63b-3cd6-bd93-1a1cf5040e8d | -5.9636 | -57.6704 | 2026-08-30 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 02210c42-fe4e-3eab-83ba-893791817d79 | -8.5739 | -66.9754 | 2026-08-30 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 084dd8c3-4bf7-3360-ad97-3225734cc2cf | -10.9216 | -50.2571 | 2026-08-30 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 92ce1b12-14e2-360f-9d48-5128af76935d | -9.7213 | -60.7472 | 2026-08-30 15:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 6f480386-3c2d-3e64-993d-0a2e5020c8f9 | -10.5601 | -50.4022 | 2026-08-30 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 56fe47f8-5113-3fc1-b43b-2ced4ec3c842 | -8.631 | -66.5473 | 2026-08-30 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 21208432-a90e-3c4c-8986-3e10e4a40577 | -11.3431 | -45.1521 | 2026-08-30 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| c32036dd-b6f5-3269-bfc0-23835c746d23 | -3.1815 | -61.1613 | 2026-08-30 15:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 9c61a63b-9c3a-3125-8f4e-8fa0dba9ee92 | -10.358 | -49.9742 | 2026-08-30 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 2f1bfb61-4196-334a-b4c1-303951d6b132 | -5.4876 | -57.1416 | 2026-08-30 15:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 192.4 |
| 09f84688-25f8-3f57-89d7-31d2514134a2 | -10.7649 | -50.6366 | 2026-08-30 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| f173e9c1-935f-337a-9155-412512192fba | -13.4191 | -51.4159 | 2026-08-30 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| f577914f-9e36-3ec7-8114-4f8e071834d9 | -7.1312 | -42.7708 | 2026-08-30 15:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 158.7 |
| 29db14c7-baf6-3665-b3b0-b7e3a9abf6e9 | -11.3619 | -45.1724 | 2026-08-30 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 284.2 |
| 0a6e3d29-64d7-394b-aa80-0a098bcfd3eb | -10.8046 | -50.5046 | 2026-08-30 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| da64060b-31ea-3255-a2d6-bbc0770ac1cc | -5.871 | -57.7715 | 2026-08-30 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 150.8 |
| 18d56c29-eac5-38cd-96c5-a9d2124d65fe | -5.9635 | -57.6899 | 2026-08-30 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |


[Clique aqui para ver as próximas entradas](README95.md)
