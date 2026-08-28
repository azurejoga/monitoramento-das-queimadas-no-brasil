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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20d0b6a3-7f7f-3ce4-8f73-c67d70011cd8 | -14.2734 | -52.0726 | 2026-08-28 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 872dfa5a-2630-30c1-b3d3-fec5f8376df1 | -11.006 | -49.6461 | 2026-08-28 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| f962c59b-8e13-31ff-b00e-4c2b1e8083ba | -14.4838 | -52.1725 | 2026-08-28 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| f40c1076-4edd-38f2-bce7-9f6c7d1b719e | -12.3041 | -50.5701 | 2026-08-28 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 241.6 |
| 5d3d8763-4aac-3719-94f6-eeef8af53603 | -14.8627 | -52.6106 | 2026-08-28 14:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 1f1a4481-9198-36b3-a064-67d0ac26ac20 | -12.2093 | -50.5386 | 2026-08-28 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 4f951f23-ba9b-3bc2-bdf5-75bd33f64eed | -12.2277 | -50.5792 | 2026-08-28 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 60fbd606-b50f-3239-8b3f-cb7d808cd210 | -14.8821 | -52.608 | 2026-08-28 14:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 7ec8f29b-d66b-3662-a11c-a8156253a4db | -11.8243 | -47.1954 | 2026-08-28 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 205.7 |
| 9864b18b-18dd-398c-a7e4-a03acd624977 | -13.3254 | -46.9333 | 2026-08-28 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 117.9 |
| e6c08c3e-0666-31a7-a970-44e6e3843f27 | -14.3376 | -51.702 | 2026-08-28 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| d54b4fa4-7f77-33e8-9842-46fa716b2d73 | -14.2209 | -51.7602 | 2026-08-28 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 113.4 |
| fff35aad-ece4-3915-b216-4eedd19e8efd | -12.2281 | -50.5578 | 2026-08-28 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 223.6 |
| bc41856e-0f09-3d57-a277-bb12911f7ce2 | -11.6603 | -46.7239 | 2026-08-28 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| fd3d427d-43fa-3c08-9072-602ea8956dfb | -10.7407 | -54.0401 | 2026-08-28 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 8e8eceaf-1ffb-3f43-812c-c53fd419a8cd | -13.3789 | -51.5275 | 2026-08-28 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 81c09554-3490-3adc-9cce-90f4735c7a6c | -8.948 | -62.3894 | 2026-08-28 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 74737fa9-0b1e-3b9a-9473-c23f8ebabf41 | -14.9791 | -52.5951 | 2026-08-28 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 7c423408-61c9-3f6d-b18f-4ac4c41ca3e7 | -7.4953 | -55.2862 | 2026-08-28 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 181.7 |
| a00fe0d4-56d8-34b2-bf8c-7b87b6ef49ca | -10.8422 | -50.5219 | 2026-08-28 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| e27037cf-58fa-3942-ac3d-04615314c4f5 | -13.3985 | -51.5037 | 2026-08-28 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 4e3554cd-a576-3337-a03f-1bda0166b020 | -8.5783 | -54.7768 | 2026-08-28 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 89e56d8e-62b6-3d24-b06b-b7e02201f98a | -10.9589 | -50.2958 | 2026-08-28 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 3e701aa5-b4fd-3a49-b2fa-8b36d132f91e | -11.7786 | -47.6474 | 2026-08-28 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| c1a443fb-c01a-3942-bf77-888cbee3d409 | -12.0541 | -47.164 | 2026-08-28 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| c6e6d06f-7b31-3648-b668-3ce33ba2b773 | -11.8243 | -47.1954 | 2026-08-28 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 191.2 |
| 0ef5876b-29d3-3831-9287-75bd1f1dbcf0 | -10.8996 | -46.6216 | 2026-08-28 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 124.0 |
| d7758b25-428a-3d14-a8f2-40196ed5009c | -12.0733 | -47.1614 | 2026-08-28 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 71d5d1ce-5714-34bf-b01b-e1ed7574e8b1 | -9.2284 | -51.5219 | 2026-08-28 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 03f44ca8-1c40-3975-af19-6b3f617561ad | -14.4847 | -53.2707 | 2026-08-28 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| ffeec03c-22a5-3678-bcdb-1d60eafde9ce | -12.3038 | -50.5915 | 2026-08-28 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 156.8 |
| f4fdb084-3396-382f-9e83-39ae45f2471c | -11.8239 | -47.2178 | 2026-08-28 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 4a177edf-9364-340f-8cdf-f30c71d5cd09 | -14.9981 | -52.6138 | 2026-08-28 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 6fcbd1c4-38f9-3f4a-b065-d39d406ce89e | -9.4329 | -51.6926 | 2026-08-28 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| fb841ea4-c283-3639-9418-370f6052692e | -14.2402 | -51.7576 | 2026-08-28 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 2697e2f4-461e-3827-bb35-63baf8b7c27f | -13.3254 | -46.9333 | 2026-08-28 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 30433592-270b-371a-84c2-a54cff59be74 | -14.8627 | -52.6106 | 2026-08-28 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 3c9a3e56-eb11-3b4d-b74a-e903725f1d39 | -13.3988 | -51.4824 | 2026-08-28 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 1bf373aa-d44d-3b3a-b751-49f605c58a47 | -7.603 | -61.3415 | 2026-08-28 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 7952d240-6bde-3b62-84ad-067d42d7bd6c | -14.9985 | -52.5925 | 2026-08-28 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 114.0 |
| ba57e6c4-e579-3910-bbc0-8690b57a2b79 | -8.0742 | -45.8147 | 2026-08-28 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 7d40c5db-40d8-309a-808e-331189e7be57 | -10.498 | -64.5193 | 2026-08-28 14:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| a447cc02-d8ba-3ed3-b7af-42fd87cdf1e6 | -7.5846 | -61.3232 | 2026-08-28 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 3dc1b871-9610-3ec2-afdb-bad9e0aaf9fd | -11.2493 | -45.0501 | 2026-08-28 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 185.0 |
| 30f147e0-9086-37d1-9ec3-1bbedca98bef | -8.5969 | -54.7755 | 2026-08-28 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 65196980-c557-3835-93b1-d178d604317f | -10.3202 | -49.9782 | 2026-08-28 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 3bd8d9d5-a92d-3d61-b3fe-c2084a5c2b5d | -9.1713 | -49.9622 | 2026-08-28 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 3dea37d3-b8b3-3c96-99f5-2864de07b4e7 | -8.0739 | -45.8372 | 2026-08-28 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 9dc74920-0a1f-3a91-b1fa-ed0201cb5ba8 | -11.2109 | -51.2476 | 2026-08-28 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| e893145c-b2ab-3f90-b38a-1dd7c94a7f0e | -9.1711 | -49.9835 | 2026-08-28 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 23f83503-23f8-3839-9e44-3beaf2a1f070 | -9.1525 | -49.9639 | 2026-08-28 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |
| de7ee7a8-cfcd-36d3-89b9-55f7d6aa4c40 | -6.2692 | -53.1526 | 2026-08-28 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 150.7 |
| 4657fa2e-33c8-3ae5-904a-0be2afde35e3 | -14.4842 | -52.1512 | 2026-08-28 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 238.8 |
| 099215a4-0a32-3f53-84ac-6268718cdb0a | -14.2989 | -51.7072 | 2026-08-28 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 183ab804-2b00-330e-a159-9faf15cec1ab | -6.6167 | -45.1994 | 2026-08-28 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| c83f7790-b7b8-3074-a462-786a7063463a | -8.9478 | -62.4084 | 2026-08-28 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 90.3 |
| d46085d1-d454-321e-8144-aef7367c2066 | -13.8752 | -54.1153 | 2026-08-28 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| e69f513e-45b7-3565-a109-220ee4c76b2b | -9.9706 | -53.9624 | 2026-08-28 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 81068f8d-6bbb-399a-a079-5eadace91349 | -8.5175 | -55.324 | 2026-08-28 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| a5e8f9f9-9021-37cb-af1a-06471bfb4d08 | -10.8801 | -50.5179 | 2026-08-28 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 9320e664-c7fe-3e2d-88ae-16ff7a2ec7da | -10.4981 | -64.5005 | 2026-08-28 14:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 068fb16f-9053-3466-b31f-ecd2b6d72802 | -14.2209 | -51.7602 | 2026-08-28 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 3018318d-a8ff-3f08-bc7d-5976fd2c9e29 | -21.0372 | -57.8494 | 2026-08-28 14:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 71.0 |
| 1547deb9-8fb4-3fc4-9e87-92a5e16c2e45 | -6.7832 | -59.4401 | 2026-08-28 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 8f723635-c983-34b5-80bb-915a84282391 | -8.5964 | -54.8361 | 2026-08-28 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| e2bde4e5-6472-32e6-ade9-502d78f985b9 | -12.3041 | -50.5701 | 2026-08-28 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 7454c0e9-8159-35ed-a91f-c3b6f6a3e1c7 | -6.769 | -58.7066 | 2026-08-28 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| ad852c09-caea-3ea7-99f3-ea1bf2b4a723 | -14.2302 | -45.2472 | 2026-08-28 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| e2b8f4d4-177e-34c1-9a47-362dccc66db9 | -12.1507 | -50.6313 | 2026-08-28 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| cb796bf8-62df-361c-ad63-442e80837a53 | -14.3376 | -51.702 | 2026-08-28 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 2b72d0b0-ed50-3601-aa2a-861eed8d1515 | -11.006 | -49.6461 | 2026-08-28 14:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 1d829a45-c726-35af-ba9f-ac970cd01dea | -11.843 | -47.2152 | 2026-08-28 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 32dbb457-c734-3977-b535-a5ed11f1b8f7 | -10.9187 | -46.6192 | 2026-08-28 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 153.5 |
| dacc91b2-11c1-3a54-88cd-5923119e252d | -10.8993 | -50.4945 | 2026-08-28 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 8bc90251-f747-3319-b41b-60483004c174 | -10.9592 | -50.2744 | 2026-08-28 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 29f74006-20fd-3db3-8879-5db77dd380b4 | -14.3179 | -51.726 | 2026-08-28 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 122.0 |
| dbe7b312-15f7-3cb1-82cd-761e9e2d5419 | -6.2693 | -53.1322 | 2026-08-28 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 165.6 |
| 88598f46-247d-3e0b-9383-d27e7f627bc1 | -8.5779 | -54.8172 | 2026-08-28 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| dd428858-4e38-3f94-8809-fb330300f93c | -14.3182 | -51.7046 | 2026-08-28 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 275.2 |
| d47149f7-7ccd-3617-904c-a26e5bb0d787 | -11.8246 | -47.1729 | 2026-08-28 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 113f4416-b29c-3b84-9036-14da5abfe3f8 | -10.8992 | -46.6442 | 2026-08-28 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 59867391-b521-38c9-9293-0497f0c9d80d | -10.7975 | -54.0146 | 2026-08-28 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 42962b35-43d9-3bda-9455-78251296763d | -13.5797 | -45.7753 | 2026-08-28 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 4e601b00-fff5-321f-979b-941b80cb4652 | -9.2282 | -51.5428 | 2026-08-28 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 48a29d4d-1601-376b-8b04-ed8f8ab59d1b | -9.9708 | -53.9419 | 2026-08-28 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 321.3 |
| ece362ba-fe48-3fdb-bedf-7de575d185d6 | -14.4838 | -52.1725 | 2026-08-28 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| d782bd82-593a-3ad1-a983-5e9483a3be03 | -15.4788 | -53.9628 | 2026-08-28 14:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 5329cb33-08be-373d-9ba6-0519f38864c4 | -10.7598 | -54.0179 | 2026-08-28 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 7e3b959a-fa28-302e-8ca9-597ab1a0b3c6 | -10.7596 | -54.0384 | 2026-08-28 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 125.3 |
| e4c3d240-ae6e-3d6f-a791-9a0005e3deea | -10.899 | -50.5159 | 2026-08-28 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| a74b4880-bda2-38f6-8c6c-8defa33a7466 | -8.5968 | -54.7957 | 2026-08-28 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| acc9f46b-cd06-31ae-acf6-2d1aec612649 | -6.6396 | -53.1934 | 2026-08-28 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 4408706f-fdb8-389c-a89d-417bca07d380 | -7.5846 | -61.3232 | 2026-08-28 14:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 820b35e4-130a-3671-b1c6-cfeb1d6d388e | -12.2854 | -50.5509 | 2026-08-28 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 3611b73b-5c1e-37d5-9ac4-9f63de951325 | -8.5968 | -54.7957 | 2026-08-28 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 68607488-b053-3bf8-a4b1-9177795e3de6 | -21.0372 | -57.8494 | 2026-08-28 14:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 78.6 |
| a1ff609d-b62e-3a53-aa13-b981693e20c6 | -14.2102 | -45.274 | 2026-08-28 14:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 496ae1dc-5796-340b-934c-21be9980c25c | -11.7357 | -54.5227 | 2026-08-28 14:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| f35793c1-7220-3afc-82d9-90d23dc9a054 | -11.8239 | -47.2178 | 2026-08-28 14:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 134.3 |
| bd83fdb9-a692-3adc-95bb-5e75d81bae0f | -10.8422 | -50.5219 | 2026-08-28 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |


[Clique aqui para ver as próximas entradas](README80.md)
