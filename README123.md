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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abdca174-bc95-3b05-b592-480530705d2d | -12.2116 | -50.3881 | 2025-10-17 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| e85dfa89-a73c-30c0-9af2-ba4751d6cc3b | -10.2748 | -44.0247 | 2025-10-17 13:20:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 1bd94bb1-5ba6-3c16-8a27-b065256d63a9 | -11.5921 | -44.0472 | 2025-10-17 13:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 253412d3-b274-3953-baea-d238645cd123 | -10.6169 | -45.2512 | 2025-10-17 13:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 527ad035-0f36-3fac-ab6a-2cd0118a920e | -10.534 | -49.5471 | 2025-10-17 13:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 1feafb18-4947-35e6-9526-4e4aea851d6f | -11.3603 | -45.2646 | 2025-10-17 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 414ee824-f239-34de-970d-97edb488b179 | -11.3992 | -44.1229 | 2025-10-17 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 088c5f6d-98f2-36c1-9752-1187cba1f1ac | -12.4264 | -51.3027 | 2025-10-17 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| a0e2afc8-ecba-3d1a-b9aa-742db273e6ea | -9.9828 | -47.0234 | 2025-10-17 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| b5d87312-6df8-3c60-b2be-820e837ff7eb | -11.3996 | -44.0995 | 2025-10-17 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 6ae91387-cf34-3cee-8ddb-c99592940267 | -11.4748 | -44.1819 | 2025-10-17 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 229.5 |
| 82803425-f5ec-313c-b3a9-f2a109aa9da8 | -11.9257 | -46.845 | 2025-10-17 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 7416806b-11e5-3a98-844a-7321a968602d | -11.496 | -44.0617 | 2025-10-17 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 135.1 |
| a22ece20-64dc-3929-ae70-d64ca6bb83f5 | -14.1754 | -47.9252 | 2025-10-17 13:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 6c4dbdcf-2496-3dfb-891f-54da4e72cc36 | -12.2747 | -50.0144 | 2025-10-17 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 73fc1c83-9ec5-33de-83e2-d0aa21f70864 | -11.1403 | -45.8665 | 2025-10-17 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 250.9 |
| 688749d2-12df-32bd-b39a-959058a283a4 | -11.4743 | -44.2053 | 2025-10-17 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 621.7 |
| e5a7c3ef-8509-3ab2-b504-aa1d67cccbbb | -11.5152 | -44.0588 | 2025-10-17 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| eaa8cde7-d15c-3254-8ebb-b90f2e9c6a34 | -11.9709 | -45.3603 | 2025-10-17 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 138.4 |
| d08e682c-577b-3ff2-894a-b855c9e2ce9e | -10.938 | -45.4146 | 2025-10-17 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 4bff40f5-231b-32e8-b912-f4d66e42dada | -12.1678 | -45.0771 | 2025-10-17 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 8ca8213e-3776-37c9-bc7a-8028fd71ea95 | -11.4551 | -44.2082 | 2025-10-17 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 161.1 |
| 69c25a22-2568-3446-aeac-87e91384af93 | -11.4939 | -44.179 | 2025-10-17 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 6c0f7ab2-65ec-3ffb-9fbf-734b127bf1bc | -11.7435 | -51.1472 | 2025-10-17 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 342dda1b-c01e-3909-aea5-7350cdb9782b | -11.1399 | -45.8893 | 2025-10-17 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 315.5 |
| 4024b8f1-98e6-3a8a-8a1a-1798933c3146 | -9.898 | -47.6758 | 2025-10-17 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 682f0860-7f28-3c8e-adfc-444c4b08c7e1 | -11.4556 | -44.1847 | 2025-10-17 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 7b1c73be-7a3a-32da-b8fd-19c57045195b | -11.9516 | -45.3632 | 2025-10-17 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 1eb11294-5f34-3325-8316-a7cca0b94a4f | -10.5132 | -43.4289 | 2025-10-17 13:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 15c5cdf5-21be-331e-a8a1-9959a1e0afcd | -11.4935 | -44.2024 | 2025-10-17 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 187.9 |
| f7d9ce45-cfaa-3879-8765-48d2b8446d3f | -11.4547 | -44.2316 | 2025-10-17 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 141.8 |
| f6bdbb82-2fa6-3588-b0ee-cf72b28fb17c | -13.4412 | -47.9483 | 2025-10-17 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 76.2 |
| bb68fc11-7a78-3d14-81d3-8db9819d624b | -11.1021 | -45.8717 | 2025-10-17 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| b9a80d6c-82f3-3c33-94ea-0b25a9ac1012 | -9.9638 | -47.0256 | 2025-10-17 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| ad25f2ef-d478-301e-957d-4e35a17bc770 | -11.5921 | -44.0472 | 2025-10-17 13:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 643717fb-d20e-3874-9e46-0e628b9cada2 | -11.1406 | -45.8437 | 2025-10-17 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 12179d4f-1693-3665-bba5-0d824ac5f844 | -10.9472 | -49.782 | 2025-10-17 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 9a0e17fc-a0e2-3a4b-9377-3df0088e5399 | -11.5917 | -44.0707 | 2025-10-17 13:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 203.1 |
| ddc4552e-545d-3589-a3de-703cde49dfdb | -11.5729 | -44.0501 | 2025-10-17 13:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 80234ec5-54b0-34bf-8fb8-18a1c44d7003 | -10.4941 | -43.4315 | 2025-10-17 13:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 62d9f9ba-ff3a-39b4-abf6-0163dcef3b88 | -13.4219 | -47.9511 | 2025-10-17 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 3dbcd595-eed3-3d6b-9774-82b777a1e892 | -10.1063 | -47.6525 | 2025-10-17 13:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| e7a5b272-ae8c-3785-9e11-b232177b40c1 | -12.9607 | -47.9294 | 2025-10-17 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 02ccfaf1-a587-3007-9f37-337cddb8114a | -13.4416 | -47.9259 | 2025-10-17 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 20e29eaf-9b3d-3fec-900c-18ba44f3bf9d | -11.1212 | -45.8691 | 2025-10-17 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 157.8 |
| 57cb9ddb-44e7-36b5-a7b0-83a8747a7676 | -11.4193 | -44.0731 | 2025-10-17 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 9bf2b8ea-2812-3f87-82dc-75c4c5c48f30 | -14.0905 | -43.6235 | 2025-10-17 13:30:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 7e7f3a63-e85a-3db6-a816-712bd9c68fb4 | -11.9521 | -45.3401 | 2025-10-17 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 66db9a4a-7111-3bda-8adc-8bda2151433f | -11.0626 | -51.009 | 2025-10-17 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 814ba1fd-38c1-32b2-b3c9-05568fc4e92d | -10.9185 | -45.4401 | 2025-10-17 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| dbe2049f-9337-350a-a1ae-0b45437ee67a | -10.2939 | -44.0221 | 2025-10-17 13:40:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 0894039f-68c0-367a-970c-4db6c330c55c | -9.898 | -47.6758 | 2025-10-17 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 476bdde4-7ab3-3dc9-89ed-19c984e98fd5 | -12.4264 | -51.3027 | 2025-10-17 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| a3f5ec79-58c7-360a-a17c-0a579a588e88 | -12.487 | -45.4664 | 2025-10-17 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 8953a13f-9198-375a-b1f0-0fb6cd2a84c0 | -10.938 | -45.4146 | 2025-10-17 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 169.5 |
| a1cc4e1e-a402-3a86-b917-c086fd480a69 | -10.9748 | -47.9042 | 2025-10-17 13:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 86d37581-924d-3038-b25c-343af5c39303 | -12.1678 | -45.0771 | 2025-10-17 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| cb364cf6-3afa-3bb5-b32c-33e667818d07 | -11.0024 | -47.3467 | 2025-10-17 13:40:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| fb42194e-366c-3a6b-a3b5-9f687f95576e | -15.9847 | -41.5179 | 2025-10-17 13:40:00 | GOES-19 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.4 |
| b3163899-af39-38d6-a2a6-27026d88ccbd | -3.7439 | -41.7217 | 2025-10-17 13:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| ca477502-32be-3aec-802e-bb5e2eff7905 | -11.1021 | -45.8717 | 2025-10-17 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.9 |
| ac14c032-fc5e-3058-ad68-97b12e7179fb | -10.1063 | -47.6525 | 2025-10-17 13:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 4a30475f-f43b-3594-9c75-912fff646dac | -11.7435 | -51.1472 | 2025-10-17 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 55eca416-3e56-3bf4-af27-c64c4e0353c4 | -10.2745 | -44.0481 | 2025-10-17 13:40:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 110.6 |
| a0c102bb-75a0-3c01-b14c-71b7de74c929 | -11.0214 | -47.3443 | 2025-10-17 13:40:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 7b9f40ce-dbde-3852-88e2-8edaa6a1ebda | -10.2748 | -44.0247 | 2025-10-17 13:40:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 00026f79-1c46-36e9-b6a8-62c49aa4e486 | -10.2935 | -44.0455 | 2025-10-17 13:40:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 7730f472-5127-383e-b94b-d341ec99a67c | -11.1212 | -45.8691 | 2025-10-17 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 4d36c0cb-377b-3494-b018-041e0af4bde9 | -10.2558 | -44.0273 | 2025-10-17 13:40:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 165.0 |
| ba8b5a64-c4eb-30ff-97c6-8a9b8099042a | -11.5921 | -44.0472 | 2025-10-17 13:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 195.9 |
| 42a723c5-5c0a-3404-acca-a68b9cac82f2 | -11.4543 | -44.255 | 2025-10-17 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 7e526f57-6ba8-3287-9905-74459a2748c3 | -11.1406 | -45.8437 | 2025-10-17 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 27e9a81a-1bf3-35a2-bdfc-9ade0db863a7 | -11.3603 | -45.2646 | 2025-10-17 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| a7015166-0308-333e-a667-128098e8d272 | -11.1204 | -45.9147 | 2025-10-17 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 0734ef90-ecbb-39da-8b40-a95be8a3e2fc | -3.9822 | -42.4924 | 2025-10-17 13:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 133.1 |
| f1441045-cb61-3ea0-bbbc-908d0b6ecf81 | -4.1525 | -42.1989 | 2025-10-17 13:40:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 101.4 |
| cdc1509b-99b8-3966-875b-cbec70ff5b1c | -10.6028 | -47.3955 | 2025-10-17 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 861478ac-71b8-34b5-8572-ec58ca5f8d8c | -11.9257 | -46.845 | 2025-10-17 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 2b1228a6-faae-3c7d-8ca4-69c6c21af86b | -9.9831 | -47.0011 | 2025-10-17 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 4ffce078-efca-37be-a391-9cf34cf64121 | -9.9828 | -47.0234 | 2025-10-17 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 397567be-86ed-3e17-9589-8ace3cb4f382 | -11.4193 | -44.0731 | 2025-10-17 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 940f6e03-f48b-3d0e-b3ed-b0dee4eea8db | -13.9127 | -45.5808 | 2025-10-17 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 66dbd37a-9590-35bc-8c22-afe5832bd04b | -10.4941 | -43.4315 | 2025-10-17 13:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 4197c070-283a-3c0f-8127-e7419aefc5ce | -12.4678 | -45.4694 | 2025-10-17 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 0ef6ad25-7b6d-3c17-a041-2c5fb0f2c4a7 | -10.534 | -49.5471 | 2025-10-17 13:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| e54290d1-6054-3db8-b37e-d69d4709dddb | -13.4219 | -47.9511 | 2025-10-17 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 55184f04-7f29-35c9-aa5a-fe46bb312a30 | -10.6726 | -45.3355 | 2025-10-17 13:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 91ad0e3e-9402-30c6-b774-1c6d8b9e94fd | -12.284 | -47.1544 | 2025-10-17 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| da693900-6e4e-396c-a067-39c890ccb484 | -11.4919 | -44.2961 | 2025-10-17 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 2f2f2138-74aa-3178-a35a-7a6477de2d82 | -11.1403 | -45.8665 | 2025-10-17 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 167.0 |
| c8680b24-796b-3ed3-9b5a-b50b190a6d03 | -11.5729 | -44.0501 | 2025-10-17 13:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 160.1 |
| f56d34f9-6370-3601-b5c4-05322b3bd7be | -13.4412 | -47.9483 | 2025-10-17 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 3830f7c8-0e3d-3033-8565-e321de0bef5d | -11.4735 | -44.2522 | 2025-10-17 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 207.3 |
| 08e72a4c-fce0-3acd-8ffc-9707be641d49 | -14.1754 | -47.9252 | 2025-10-17 13:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 6e8bed17-a44d-37be-99b3-049b7456aec6 | -3.9635 | -42.4934 | 2025-10-17 13:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 97.3 |
| 0f250938-4fd3-30de-8520-bdb23b200e12 | -10.5136 | -43.4052 | 2025-10-17 13:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| cf7d062c-d7f5-3818-9b17-1eb6eac83407 | -11.5917 | -44.0707 | 2025-10-17 13:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 211.3 |
| 4c2100d6-624d-3f22-a108-9e3933020466 | -10.5128 | -43.4525 | 2025-10-17 13:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 90750329-8c1f-30c7-9130-a25ca8b8ed24 | -11.496 | -44.0617 | 2025-10-17 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 43500c52-67d0-320c-8761-ce84320ca9c1 | -10.9189 | -45.4171 | 2025-10-17 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |


[Clique aqui para ver as próximas entradas](README124.md)
