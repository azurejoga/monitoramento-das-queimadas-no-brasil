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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e509ead3-365c-368c-9d1c-b991d16d55f8 | -5.62211 | -42.62311 | 2025-09-01 04:10:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dc9f15bd-005c-317b-869a-5343754fbe9e | -6.29458 | -43.30643 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d08ac920-6704-313b-8ef4-9333bd80bec4 | -6.16744 | -43.32105 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7dadde92-6fa0-3e52-9a93-f745b67faef5 | -9.66663 | -47.05202 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 142512f8-e588-36fb-8bca-65b0f17e4e0d | -10.60789 | -44.32537 | 2025-09-01 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bd0d33f8-ad72-3284-a209-d58297ef3a8e | -6.07206 | -44.40646 | 2025-09-01 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c33f9572-1c8f-3ea9-b806-134d9ffc8b12 | -6.84504 | -52.811 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a6396e79-3278-315c-af16-c157aafffaa3 | -9.22329 | -47.11056 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38a7e575-6f2a-3153-aa39-ac62d4a38ce4 | -7.08138 | -44.34813 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5944a01d-c584-3153-8d5f-29d261288980 | -9.27718 | -47.08706 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc68b69a-b2b4-3b7a-872c-a7becd7d3c28 | -8.19423 | -46.77839 | 2025-09-01 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 0021332c-129f-3f0b-b2ca-9aa9dda1d5a9 | -5.99163 | -43.36612 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 114b45fd-13a8-3566-8295-0ab0cbb85d6c | -6.76801 | -44.62664 | 2025-09-01 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a1ad22a-1ccd-3adc-b0b4-3f2e4152c5c9 | -9.67162 | -47.04068 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| df35a8cd-cc6b-3848-88a6-62d0d5aef47b | -11.07584 | -52.06625 | 2025-09-01 04:10:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa1fdac8-7771-3929-9c3a-9d0f1dcbf4c8 | -6.3346 | -44.47087 | 2025-09-01 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c2c3c84-89bf-3a88-80e7-963fd4b83dc7 | -8.19708 | -46.78303 | 2025-09-01 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 06d0cf97-70fa-3b34-9120-c8d8b336e429 | -6.15309 | -43.32251 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c96fa724-52f3-31c3-b8d6-b11e0c4b938a | -7.07912 | -44.33952 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70deecf7-ec0d-3cf6-9162-9117a07ef1e5 | -11.20623 | -45.03318 | 2025-09-01 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f69761b-c838-30d8-872c-12338dea505f | -6.30285 | -43.60499 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2ed0aa5e-04eb-353e-905d-f42e937b24b5 | -6.164 | -43.32049 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 891c5a73-72bb-3bce-8fe1-67c6b71e15fb | -8.33745 | -47.44358 | 2025-09-01 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0d8c91c-a1ad-3bc0-935e-e9e04fc75a9d | -10.24287 | -51.111 | 2025-09-01 04:10:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9b65aca6-7774-3bb1-850f-30348cf5d7ce | -6.83895 | -43.33151 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 558a3c2b-16f2-3bc0-9f11-022c674117dc | -6.57321 | -43.69793 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 04fe686d-4a90-3a07-ac4c-1a5c3e3c0cc8 | -9.66753 | -47.04688 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e53ff200-86ea-3a12-bb3f-a4df24628215 | -6.19475 | -43.3401 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3c8fc280-5ac5-38bc-8385-10c0f653ad86 | -6.10811 | -43.27325 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5fd6eb90-4718-3e0f-981d-29873ca37835 | -6.78248 | -44.62896 | 2025-09-01 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef5de6e4-b0a1-374a-b67b-518718f60801 | -9.21981 | -47.1067 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed2775a8-a5de-3497-916f-f64bf522a444 | -6.83721 | -52.81917 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 17af09f9-8b3f-3ab6-9e4b-0d65d71a5c5c | -6.81903 | -45.69859 | 2025-09-01 04:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d20dab36-c358-3c51-be35-9a105c6755f3 | -11.37372 | -43.61344 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7aae96c-ff27-3c9e-ad3a-ed86151b34e1 | -11.01375 | -46.94383 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de8f097d-2c88-3693-8750-6ef0d68273d2 | -10.04952 | -48.09493 | 2025-09-01 04:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7d31054f-0f1d-33f3-8541-0de8893ed38f | -8.07698 | -49.9424 | 2025-09-01 04:10:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b7a6739-a191-3f36-88bf-a701c114e838 | -6.46791 | -41.74528 | 2025-09-01 04:10:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0f141114-5f9e-3e95-a4d4-4c8fbc688bba | -7.2112 | -44.21296 | 2025-09-01 04:10:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4df7b6d2-e4cc-3c79-97d8-772f1ba31880 | -8.90355 | -45.12257 | 2025-09-01 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 102a4b9b-c6de-3392-a5f1-04254f599964 | -6.29732 | -43.63925 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d1ab895-d221-3db7-95f9-cb165680423f | -11.36933 | -43.59795 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8debbde4-ecdf-3d7e-a32d-02811b859741 | -9.57805 | -46.00385 | 2025-09-01 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce3178b8-1086-3718-9848-02515d9da508 | -10.03511 | -48.07756 | 2025-09-01 04:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bca50cf5-952a-3bc3-8d08-dd2579407409 | -12.0949 | -44.72057 | 2025-09-01 04:10:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 47aeb231-606e-378c-85a5-856d7f308707 | -6.82315 | -52.82906 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 709fd6f1-893a-32b2-bae5-c57d476e744b | -11.04378 | -45.14223 | 2025-09-01 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 83d6b0f5-6ec2-3075-89e4-4fb76f17075e | -10.36386 | -52.29141 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d40eecd-d60e-3e5d-9877-66aac07d3c9d | -8.4446 | -47.37645 | 2025-09-01 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a808e4d2-c87e-3148-9f5c-b065201e4219 | -5.75205 | -43.68583 | 2025-09-01 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa5db0ac-c127-3f28-b22e-2166c5faf980 | -11.35627 | -43.52959 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 793d6fa0-9ccb-3294-ac13-1589d412666d | -6.82586 | -52.81215 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 93fc9e6c-dd2e-33db-a62d-23e7d5ac7f69 | -9.63758 | -47.82897 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b656506-0cae-306b-933c-9484c73d1055 | -6.46708 | -42.4314 | 2025-09-01 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| df0ee6b0-5f39-33ec-bd65-34aea54f3a4d | -5.32555 | -42.86265 | 2025-09-01 04:10:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 85e26178-be0d-30a8-a8cf-5c6e4711e8f5 | -6.80911 | -45.68724 | 2025-09-01 04:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95f66975-1d2a-3362-a225-01efd6ca2ab2 | -9.38356 | -48.01638 | 2025-09-01 04:10:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e553e0e4-1795-3200-b0a3-91052a4a93ec | -11.4488 | -46.82003 | 2025-09-01 04:10:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4711e168-a1f6-3185-80f4-ce5e738f217d | -6.09674 | -43.19141 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 36bcb607-7ce3-3131-bdd0-a85f7e962b58 | -7.65846 | -42.70837 | 2025-09-01 04:10:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 976aa05d-7b67-3188-9420-7c88a8706ea1 | -11.68682 | -47.57259 | 2025-09-01 04:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aff06732-f2c6-318b-8946-e94bcf7dcad6 | -11.88735 | -46.74729 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99499a39-c9aa-3cc5-9a31-636088723783 | -11.334 | -43.68828 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46e0ad04-9945-3c0d-928f-7dd841ae5f24 | -7.41866 | -42.04655 | 2025-09-01 04:10:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5bf4ce1f-a9e0-3a13-9162-e74fac7566f3 | -7.08652 | -44.35241 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| efc8bdde-f9e8-3574-9fd3-605a566627de | -7.41854 | -47.43528 | 2025-09-01 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 998b8909-d476-3904-8982-7acf89319c25 | -6.26577 | -43.54833 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f83f7fdd-33ac-35e1-9f28-35429e0a53b3 | -5.48431 | -47.52352 | 2025-09-01 04:10:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc142b36-8894-3655-8768-4123828b3372 | -7.7035 | -50.27655 | 2025-09-01 04:10:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 98e4aaef-4f14-33af-be5a-dd5c1b50aedc | -7.0892 | -44.3363 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| c675fe37-f00d-3e15-8c92-b183b660c36f | -11.68283 | -47.57183 | 2025-09-01 04:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad857fa7-c451-30d1-a904-331d3fa4ca45 | -11.57481 | -44.65569 | 2025-09-01 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b736251f-8042-34ae-9444-10af3292ddfb | -6.81877 | -52.81814 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3223a50c-efe3-393c-8ec3-143741fe47e8 | -5.7568 | -43.67863 | 2025-09-01 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7f666c8-0f75-3dc0-9301-ebf90a9b29d1 | -6.54795 | -44.58029 | 2025-09-01 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 857f9d16-0f6c-3e1e-8656-18d1de50acd8 | -11.04151 | -47.01528 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f93c76db-d1bb-39cf-bfe8-a83b3e1ec1dc | -7.6189 | -42.65474 | 2025-09-01 04:10:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3b9c09a3-a019-36db-a1c7-5ee4f13c7228 | -7.08432 | -44.3437 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 92c6ee38-129c-3637-a9fa-59f1634778cd | -7.57589 | -45.20839 | 2025-09-01 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 500ac702-7897-3939-86c2-1a78458684e9 | -6.75755 | -43.78618 | 2025-09-01 04:10:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5560ec78-22b3-37a9-88d8-30d17c9ed846 | -6.57073 | -43.71316 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 58af2de3-2d69-3611-a5b9-ad7d5134e80d | -11.37649 | -43.61759 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b811fa84-29b2-3429-b2c2-238638aa0ace | -9.01521 | -50.12271 | 2025-09-01 04:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37145a94-7155-3fbd-b570-98f8b0e5862f | -6.97957 | -43.11251 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7fed2c0-e17d-3694-b07c-71b0a7543bf3 | -7.63286 | -42.65337 | 2025-09-01 04:10:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4acdb4b8-3e39-3579-8e29-79188a2718cf | -6.09052 | -43.25131 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b68a2d8f-4b34-32ba-8cc5-c17bbdd3905a | -6.36647 | -43.5718 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e35af7da-d1f6-32b2-92f3-9bf310097d12 | -8.19886 | -46.77236 | 2025-09-01 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1997bcf1-75b3-3b3c-af31-12f0820e862b | -6.81732 | -43.34022 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 904c076a-597a-3099-9fd5-a2eb801280f5 | -6.96521 | -44.30551 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a799b4f0-e23b-3f3d-8489-676c3d1825f1 | -8.46541 | -43.62402 | 2025-09-01 04:10:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc07677c-2312-3972-9da4-6297ead07f53 | -5.96541 | -42.96735 | 2025-09-01 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1e21782c-7f2d-3f30-93d5-0db0367c169a | -6.32884 | -53.43722 | 2025-09-01 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 670a6daa-5922-3279-b275-b1dae2492f4c | -7.63622 | -42.65391 | 2025-09-01 04:10:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3fb9a744-c9bf-36db-b4da-2b35a18da456 | -8.84657 | -45.73002 | 2025-09-01 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a007e350-742a-38d8-859c-7ce6b06b7363 | -5.43535 | -49.99235 | 2025-09-01 04:10:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cc32af7d-d1d6-3be8-a48c-ed8f09dab6df | -7.62225 | -42.65528 | 2025-09-01 04:10:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 26684c3e-1231-301f-b639-81121d01b01c | -6.30162 | -43.61259 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 55ea5c5a-e301-3890-b818-1456b6b5a6d7 | -6.51371 | -43.55225 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 951fd954-d763-3d31-b1c1-51222118d79f | -6.54607 | -44.6143 | 2025-09-01 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README38.md)
