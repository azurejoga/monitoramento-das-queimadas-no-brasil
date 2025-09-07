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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e1a7f13-3854-3761-909f-c69efbc620f1 | -12.80382 | -48.0158 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 8adc24af-62b6-3fa8-afaf-18c963a2f687 | -13.00891 | -54.8239 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f46c2144-2d3a-36a4-afb7-0cb4764a9cf3 | -12.77206 | -52.94702 | 2025-09-07 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2fd45c46-d974-34d8-938b-c52329cfb465 | -11.11183 | -52.03115 | 2025-09-07 05:12:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b42938b0-ab2b-3d73-8972-63363b3a8c4d | -11.64242 | -54.53638 | 2025-09-07 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 262663a9-7e88-3a94-a294-d9ec24c1e108 | -12.94314 | -54.76535 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a0468512-fe0f-3346-9ebb-e3a06623598b | -8.37924 | -52.53723 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 285fb2b9-09e5-3d0d-8c76-a83780bb1bb3 | -12.61611 | -56.98549 | 2025-09-07 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd13552a-fdca-3c95-867b-cd5d98dd0a0e | -11.3205 | -46.55916 | 2025-09-07 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 012d2579-f8e6-3e24-a8f2-429551ab7f6c | -10.45677 | -53.60613 | 2025-09-07 05:12:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 067b3371-57c8-39b3-a16f-ee07a6052e3f | -9.93233 | -60.1022 | 2025-09-07 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e3121ec-8d2e-3191-a04a-eadfac408a8c | -12.19166 | -53.90638 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cdef831-865a-393e-95f6-94c4d6980964 | -10.3512 | -46.46477 | 2025-09-07 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54722e31-e9ba-319e-9842-f2fa290f1943 | -9.46178 | -56.05292 | 2025-09-07 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3f1c12b3-892a-3339-aba4-e4ebc19772c8 | -8.46173 | -47.33604 | 2025-09-07 05:12:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ad2c481-35d5-301b-864e-da0c61a3247f | -13.03721 | -48.07137 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 772184eb-fd44-3fe9-92be-fc3c0d076aaa | -8.34851 | -52.55663 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e62d1060-39ca-3508-a221-f55cda5bc1a0 | -8.36139 | -52.55494 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4ec8f6e-5395-3b2a-a10d-9b3b3fd9b5c6 | -9.97712 | -51.66373 | 2025-09-07 05:12:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 761e79dd-1681-3dfa-8704-151d47766f5b | -11.22071 | -55.02208 | 2025-09-07 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f816420-0bda-3701-a556-9de90c6d85cc | -9.94699 | -60.14605 | 2025-09-07 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e30f215-e22a-3a7d-aff4-3b8c676964e0 | -11.00992 | -52.05547 | 2025-09-07 05:12:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 80af8015-b114-3c9b-b851-a835786dd15d | -12.78387 | -52.92354 | 2025-09-07 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e94c581-74b8-3abe-a9b7-01a1d0dc21f5 | -13.03683 | -48.07478 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3dfed86-2bb0-3eab-9371-4ee6f3131cd9 | -10.45779 | -53.62738 | 2025-09-07 05:12:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 350d2833-f123-38a8-9d87-4ae20ec158b6 | -8.51199 | -51.31678 | 2025-09-07 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed340c13-65b7-3671-a9ba-8967f560aafd | -10.73195 | -48.59605 | 2025-09-07 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae274e31-b2c5-366c-93d6-621805fd6786 | -11.25943 | -51.12169 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d4c4464-4bb4-3022-a74d-82ff24518581 | -10.81063 | -47.73652 | 2025-09-07 05:12:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6dac9011-41eb-3a0e-a8da-50ab2c3aa516 | -9.45803 | -58.80465 | 2025-09-07 05:12:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7cbc52a-0d7e-347a-a5ea-034b43c189fc | -12.80053 | -48.02014 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 1e1333db-cf47-336b-ab05-013b2608a1de | -12.19662 | -53.89983 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dabc3999-7ae5-3064-b14b-b9f1441eb347 | -13.55371 | -48.11227 | 2025-09-07 05:12:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 421a1c23-b277-3c40-9fea-1a9ed354a19a | -11.58118 | -47.75964 | 2025-09-07 05:12:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 77d312eb-1867-3668-aad1-fee00775bf09 | -11.64174 | -54.54112 | 2025-09-07 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 893181a1-2411-3afa-88e2-8240e4de1433 | -8.35214 | -52.56064 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b37d53bd-0d5a-301e-83c7-949bc720f95c | -12.78381 | -52.95709 | 2025-09-07 05:12:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f9996d9-845e-3452-a4bd-32aa1be4d57b | -12.61897 | -56.98981 | 2025-09-07 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3757b6b6-3901-3b54-8e4f-501a25646290 | -12.01518 | -47.78183 | 2025-09-07 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e54e59be-5378-37ad-ade0-aadcb4c74698 | -12.61269 | -56.98494 | 2025-09-07 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c31ab55b-43bd-3f2a-8db5-386a47a10c33 | -11.20028 | -55.05947 | 2025-09-07 05:12:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7cde48f-91d5-3820-bd03-924f83a37c7f | -12.95709 | -54.77717 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d3b3c2fb-9ca2-3bff-9c3d-db929cd219a8 | -8.34546 | -52.54865 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 408d6756-39bc-3c49-adf5-2b1a1c5ef701 | -10.88721 | -55.72134 | 2025-09-07 05:12:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4485abcb-4cd9-3716-8156-d075356f98e8 | -12.81283 | -48.01814 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 0ff0a360-dfa0-339d-8a23-ab8ec6ec4d9c | -11.14595 | -48.38609 | 2025-09-07 05:12:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4bb739db-79b5-3dea-aaa0-7e2270918436 | -10.57121 | -61.24832 | 2025-09-07 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 7b539a97-1568-3f46-8e64-a341bc903075 | -12.80097 | -48.01609 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| a10606b3-9b76-30d2-ac4a-1163c83e43d2 | -8.6948 | -54.6776 | 2025-09-07 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 475c6c62-7bfa-3ded-8aad-bcb2962bf578 | -13.24621 | -51.80336 | 2025-09-07 05:12:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 297b0e7d-e5e7-373c-a9b6-ea3b1eacf87f | -11.16099 | -48.37741 | 2025-09-07 05:12:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c8b5ea46-98d2-3212-ba42-921992bc503c | -12.94109 | -48.03688 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19923191-53fa-385f-aa99-8163dc2bef32 | -13.03327 | -48.07555 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95855849-8116-3e2a-aa8a-7abbe6f0f61a | -11.21766 | -55.01712 | 2025-09-07 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1bbc9dc-b511-341a-b5da-c57d1a8cbe8a | -9.94358 | -60.1455 | 2025-09-07 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 421ffa8f-3abc-3d06-924c-660fc6646dec | -11.77821 | -47.55745 | 2025-09-07 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fbb00804-111c-35ea-b264-c083b8937dad | -10.35411 | -46.46204 | 2025-09-07 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 77a8c1a6-00c9-3a97-aa13-8920a3ce1686 | -11.16438 | -59.16064 | 2025-09-07 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c3eb5c4-e0d4-3cd9-864e-0fcf0adc9d0b | -11.49692 | -55.51142 | 2025-09-07 05:12:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d79efe32-a491-325e-b0a8-79e6989ab587 | -14.44523 | -48.45903 | 2025-09-07 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e551c6b8-b0db-3272-b30d-8e574050a764 | -12.26852 | -59.34543 | 2025-09-07 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb3ef7a1-6e00-37e1-a16b-3e9ebbdce32a | -13.00401 | -54.80359 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6bfa214e-8d90-3ae2-b5e7-07dca9c25cf8 | -10.15777 | -48.74329 | 2025-09-07 05:12:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70dcbc27-c774-3631-a5fa-cbf466953ea4 | -11.15878 | -48.37601 | 2025-09-07 05:12:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fea3cc92-f531-3a2a-9877-2d2303907217 | -11.60012 | -47.16362 | 2025-09-07 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c7a72f6-faeb-3769-ac36-83a95094e299 | -9.71223 | -49.49084 | 2025-09-07 05:12:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfe319cb-6077-35f6-9d94-23479c000467 | -13.04244 | -48.07851 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0fd644d0-c9f4-3ce7-bd6f-fd9f7957d28e | -12.80006 | -48.02443 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 6d9f569d-d4ff-3470-95ac-745f33f2b807 | -8.37976 | -52.5335 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d393bd3f-7051-3eea-959b-99c9cd9a07f7 | -10.15184 | -48.74594 | 2025-09-07 05:12:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 616cdbf4-1005-3c2d-973e-7616fed6a081 | -10.72758 | -48.58525 | 2025-09-07 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f6d6729c-4f8a-3f81-b131-de5becc9b41a | -12.95575 | -54.78683 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3ea20b42-10c0-38f6-9717-c25ed8edf4d7 | -13.03366 | -48.07231 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff1e4291-148e-31fe-9da6-4a2b9f6357ba | -12.47859 | -53.83595 | 2025-09-07 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f12d2e3-1973-3049-88cc-92b4281e3f28 | -12.84579 | -47.994 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c128f732-d164-398d-a616-9b7c53c7017f | -11.22439 | -55.02261 | 2025-09-07 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c72b4af-82bd-3abf-bc05-3608bb0fd7f3 | -11.16058 | -48.38088 | 2025-09-07 05:12:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 06b56a7c-865b-3759-84f5-7e4453f4af29 | -8.68351 | -45.3085 | 2025-09-07 05:12:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3d553205-b7f6-3af7-b6ed-507570b92818 | -13.66514 | -46.9596 | 2025-09-07 05:12:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ad6ea0fd-9413-38ff-8952-479095fcfd40 | -11.20459 | -55.05564 | 2025-09-07 05:12:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 163a1780-e4e5-3cbf-96bc-57278903d928 | -13.85491 | -46.24454 | 2025-09-07 05:12:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 781ff1f9-10d2-3c51-bd5f-31f85c52302c | -13.83272 | -46.26151 | 2025-09-07 05:12:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0c3f437e-5ca0-32f8-8e91-921056e4220a | -8.06733 | -52.39011 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 962a7525-23ec-3bbd-a8ea-44bd34a47a3b | -12.81777 | -56.51842 | 2025-09-07 05:12:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b58725cc-e7e1-3565-8ab5-0f32ce3402e1 | -11.11244 | -52.02668 | 2025-09-07 05:12:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 934c97e3-c1c2-3d54-a6d9-0c4e7a112b73 | -12.82069 | -56.52288 | 2025-09-07 05:12:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 50fab6e9-74f1-3f5b-a94d-5dbe615fa363 | -12.9526 | -54.78145 | 2025-09-07 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f9ebfc70-b567-395b-be41-941981da6b72 | -10.15278 | -48.7387 | 2025-09-07 05:12:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7266495-db3c-3e0a-82b4-fb11664fd225 | -12.54794 | -48.07909 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 667657c4-b206-3575-b59a-c7396886b421 | -9.98226 | -51.65961 | 2025-09-07 05:12:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b2d62112-c853-3946-a204-99fbfdc3e377 | -12.85226 | -47.99027 | 2025-09-07 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 841b6913-d2f8-37b6-9fb4-8bce69fbef2c | -8.06828 | -52.38339 | 2025-09-07 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f9c8b17b-55dc-3c0b-bdc6-86ef94b6ec52 | -9.69234 | -51.07362 | 2025-09-07 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a185c7de-3b95-3e8a-828f-02b9e620cb20 | -13.77539 | -52.78403 | 2025-09-07 05:12:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 75261416-85ec-3672-b199-9bc11d8f7909 | -13.85435 | -46.24969 | 2025-09-07 05:12:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 50dfb5a8-2a4c-3f55-be15-a07dc9c95941 | -11.20661 | -55.01546 | 2025-09-07 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fb05dd9-71dc-3bb6-9f7a-fa7dbe82aced | -11.2183 | -55.01269 | 2025-09-07 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3e07aae-8aaf-342e-a13a-ced165871d89 | -9.45662 | -56.04045 | 2025-09-07 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 995af6f4-8f43-36be-84d9-68e4b7460e55 | -9.6098 | -47.89334 | 2025-09-07 05:12:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6c3e55f-0e64-342e-a020-2700c39a4ece | -11.58556 | -47.18076 | 2025-09-07 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README73.md)
