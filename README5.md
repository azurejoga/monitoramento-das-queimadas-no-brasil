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
| 3bd8e23b-5e68-3fbe-b59a-72285813c124 | -13.33163 | -45.18758 | 2026-06-19 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e37d968-c45c-3c5b-a040-6bb7c17e222a | -13.96798 | -47.37712 | 2026-06-19 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b1c22de-42c6-35e1-91c2-58380ba8fdb7 | -9.80632 | -48.91684 | 2026-06-19 04:27:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a07b3d2b-63ab-3d84-b7c9-f23370623ffd | -14.21474 | -54.70155 | 2026-06-19 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46c14ef5-76e7-3fb2-a2b2-90653878776e | -8.91061 | -46.95377 | 2026-06-19 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e73e171b-99de-3b22-92f3-1c0ea222c70f | -9.74561 | -47.87389 | 2026-06-19 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57bc249f-4b9c-3952-97a6-e0197af8caad | -13.93534 | -53.56907 | 2026-06-19 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 678dd14a-998c-34f7-8115-f920d533d029 | -9.5679 | -42.96072 | 2026-06-19 04:27:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 548b6e3a-fe3a-39f6-9efc-d54b8291092e | -11.35899 | -55.82478 | 2026-06-19 04:27:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55df7fe6-3d38-3504-af94-07b7ab7ebd7d | -7.63468 | -50.02075 | 2026-06-19 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5fcd61f-6bbb-3410-a8be-d5761a8194fc | -12.88954 | -50.16338 | 2026-06-19 04:27:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2f32c30-2cac-3ee3-83d4-c918a35ff75a | -9.68765 | -43.26275 | 2026-06-19 04:27:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b24881f0-c723-3614-aba3-6becf889d87e | -10.04529 | -48.1081 | 2026-06-19 04:27:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bae2ba0e-1db8-3c00-bf14-fb2044b2465b | -13.97459 | -47.37818 | 2026-06-19 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d472183b-5e75-3d71-a25b-b765a7ae54f1 | -10.06205 | -48.08881 | 2026-06-19 04:27:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e837325a-5280-3bdc-a7cd-071c44dcfb33 | -10.98435 | -47.74646 | 2026-06-19 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0014cbe7-d02e-307c-a6f3-0ec0c6f5e587 | -10.25215 | -47.34043 | 2026-06-19 04:27:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a37189fb-add7-352b-8387-2725c7a65017 | -10.05425 | -48.09483 | 2026-06-19 04:27:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 40e36765-ae1d-35ea-9a25-c7dc58f3b68d | -9.15807 | -47.24302 | 2026-06-19 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 484f555b-79e9-3dab-a69d-090f6a87c448 | -12.84011 | -44.36742 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a4195fa3-261e-3f24-963d-25c1897333db | -10.54552 | -53.73385 | 2026-06-19 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b928bd8c-fd4a-32fe-a2a7-08ad8e717f55 | -10.75214 | -50.21129 | 2026-06-19 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2490c7bd-a2fb-3b9d-8e2e-0e3dfbc7b1f2 | -10.54034 | -47.71335 | 2026-06-19 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 09a16dc9-f5a5-3e37-a07e-7228b6f27150 | -12.45581 | -46.5278 | 2026-06-19 04:27:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f80cf334-9c68-38c1-b792-63099881a863 | -12.91638 | -49.48376 | 2026-06-19 04:27:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27d15559-8f5a-3fab-9f54-ee984ddc5811 | -12.4985 | -43.77538 | 2026-06-19 04:27:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 793647e6-3923-3857-a9cc-1fbf8202b400 | -11.3097 | -51.41683 | 2026-06-19 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18ae1f37-80f7-3f85-a5c7-39d968b496fe | -11.78419 | -57.00028 | 2026-06-19 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8292576e-a24d-36d6-a6a3-1d126badb24f | -12.87028 | -44.37413 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 3e5e9bef-8695-3438-a764-2c1a56c30ce5 | -12.86307 | -44.37305 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 54577953-d801-356e-ad2d-0026a0640aeb | -8.91278 | -46.9399 | 2026-06-19 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 30dc5a5d-d1af-3c4c-ac3e-cbcc6e0c18d1 | -11.90222 | -54.83469 | 2026-06-19 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85e134d4-d373-3074-96fa-e5e65d57991d | -11.82789 | -47.09724 | 2026-06-19 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 620f4652-4ca7-3b00-bed0-200d47bb1b70 | -13.32114 | -45.1616 | 2026-06-19 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09882901-8101-30bf-b75b-716b20b14c10 | -11.66516 | -56.76528 | 2026-06-19 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 965b412b-a791-3056-a27a-e8d82e791e0e | -13.33919 | -45.20903 | 2026-06-19 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c4b405c-8701-3507-8474-7f805e2197f3 | -12.8775 | -44.37518 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e1cb331c-09af-334c-9d53-8881ad578c27 | -12.87389 | -44.37466 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 707ea3ad-957a-3d7c-a103-c21ac486bced | -12.79415 | -44.50677 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e0185a5-0eee-3fe9-a522-87083803d31b | -10.2549 | -47.34445 | 2026-06-19 04:27:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 43cab38b-a0d0-369e-aaed-582d6d089937 | -11.06808 | -52.46034 | 2026-06-19 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7bc29d8a-3b91-3f37-8527-fd1d5679908a | -12.86667 | -44.37359 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 0f49b376-2b17-3413-b215-e09a76bb6479 | -8.78701 | -46.63192 | 2026-06-19 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 523a3dd9-18c3-34c7-b57c-aeeb3d1d3ecc | -11.21102 | -46.57503 | 2026-06-19 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e4ce0215-a2e0-3b36-820d-f56ac5000606 | -12.49656 | -43.77223 | 2026-06-19 04:27:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ba9cc2e0-78df-38c2-8821-a03cb61bcb40 | -12.78458 | -44.52237 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5f1f094-51da-3d33-9cc8-357ee10666cc | -11.06403 | -52.45959 | 2026-06-19 04:27:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c40cb40-a648-31a9-ac1c-6b6db9adbd12 | -11.31348 | -51.41748 | 2026-06-19 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f59372dd-1ce2-3d79-91f5-42e99cc076e0 | -12.78639 | -44.50988 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f927ec0-1b01-325f-b39c-35531b37fd5e | -12.49722 | -43.76772 | 2026-06-19 04:27:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 6aabee80-7f1a-375c-86c2-5ac556bc0c2d | -10.16281 | -56.61691 | 2026-06-19 04:27:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1921f565-19a4-3607-8486-637d30d31775 | -11.88585 | -46.54366 | 2026-06-19 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 61e2173b-769a-3593-a861-0e0c943c21fe | -8.91608 | -46.94042 | 2026-06-19 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 42b25b7a-f544-3621-9b27-aaf3c93d81f4 | -14.73871 | -52.6818 | 2026-06-19 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63519cc0-3067-3ad5-ae4f-20f3c3cf9469 | -9.21585 | -47.92999 | 2026-06-19 04:27:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9c88b6c-b3de-362d-9da6-eca2c6c61232 | -12.79057 | -44.50624 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d49d92ee-87d1-3d24-838e-328ae78ddf1a | -12.15252 | -48.44994 | 2026-06-19 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88b1ef22-f341-3816-a97e-09b420f1f659 | -13.33454 | -45.19207 | 2026-06-19 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88626226-8265-33aa-a993-9671c450cd40 | -8.91115 | -46.9503 | 2026-06-19 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa8cfc2c-72ee-38a6-9b09-cc2c3317f90c | -12.89302 | -50.16399 | 2026-06-19 04:27:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08061bdd-0e96-363a-9c2f-b769693a4524 | -9.68333 | -47.03823 | 2026-06-19 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3289fa8-30ab-38f8-8328-8b15fcfdd42b | -9.68663 | -47.03875 | 2026-06-19 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31cf5006-a23b-39bd-8460-a0823590cd82 | -12.44683 | -44.75589 | 2026-06-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1e7d46e-e951-3489-b7a3-30bd8c8b62e2 | -8.57096 | -45.98599 | 2026-06-19 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 529fac0c-dd09-38af-8052-8bb73bd629a3 | -13.96744 | -47.38067 | 2026-06-19 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6ec17d1-4b36-3f4f-a8be-1d06b6d1f45d | -11.26249 | -53.95671 | 2026-06-19 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11cf8ed9-7185-3c7b-8302-543dbd68a1bd | -12.84143 | -44.36977 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3f54b359-b9cb-32b8-850b-10a625b8ee7d | -10.75066 | -50.19827 | 2026-06-19 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04ecdb0f-7cb1-3bb1-80c7-379aa0299b57 | -13.49626 | -47.50357 | 2026-06-19 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c4ee40d-2d6f-3506-be69-4c4045292adf | -9.56688 | -47.92833 | 2026-06-19 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d99b91e-f702-356a-80b0-1957edc05dac | -12.49975 | -43.76636 | 2026-06-19 04:27:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 44666b5b-2917-38a5-888f-4d616c9fbdad | -12.79476 | -44.5026 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78bc6d14-e588-324d-9bbc-bff419f1e596 | -13.31822 | -45.1571 | 2026-06-19 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eec6b2a2-0ab2-3eb3-a2f3-efdb3431e263 | -12.50092 | -43.76827 | 2026-06-19 04:27:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b090d5c9-9fe5-305e-afed-5c20b6e98390 | -10.16388 | -56.62049 | 2026-06-19 04:27:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0ab604d-4397-32cc-a9bf-2ceb8df5b03c | -10.15303 | -56.61846 | 2026-06-19 04:27:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c60b87e4-85e0-3d21-a845-8e0acdecee4c | -12.49604 | -43.76581 | 2026-06-19 04:27:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b5cdb47-660e-3875-9f02-1e6689ec5bb0 | -11.91568 | -55.91443 | 2026-06-19 04:27:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 239acf8d-3460-3e1c-9dcb-22e94a0a4bb3 | -13.33105 | -45.19156 | 2026-06-19 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b201c439-c669-34c8-bb3c-84afe615ef7c | -10.05368 | -48.09843 | 2026-06-19 04:27:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e763fda8-923d-3103-935d-8555e0d61097 | -13.96413 | -47.38014 | 2026-06-19 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff6c2d14-824e-3198-833a-34b97e9b5246 | -12.92038 | -49.48058 | 2026-06-19 04:27:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16998a6d-60f5-3dc1-8fe2-b1f2e5786293 | -12.8751 | -44.36615 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| faefcbba-ea01-3eaf-9d29-fcf831f84938 | -8.46676 | -46.41788 | 2026-06-19 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16577ddf-6947-3baf-8293-d066231e1254 | -11.78487 | -56.99669 | 2026-06-19 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 485d590b-c92d-3f88-893b-d6a99acf9d4d | -11.83503 | -47.09478 | 2026-06-19 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a5f6989-40f7-3853-b103-7644162e30d0 | -10.74926 | -50.20655 | 2026-06-19 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79212cfe-ae23-3d42-aa4b-79836ee0f961 | -12.13745 | -48.26766 | 2026-06-19 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f9aaf4a5-a0fb-3c3d-8c5a-934de7b471ab | -9.69219 | -47.6953 | 2026-06-19 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad350aa6-e187-33bf-b42b-b3cdd69c620e | -13.32581 | -45.17857 | 2026-06-19 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b0206045-a920-3877-bd5f-7bd51b685fac | -8.79085 | -46.62897 | 2026-06-19 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a50c02a1-bd5b-3e8c-b2d2-9cc587c5c811 | -8.9117 | -46.94683 | 2026-06-19 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 04a088fa-d86b-3b2c-b86a-9b72ecae6ef3 | -10.90792 | -46.33565 | 2026-06-19 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0ae3fa4-4d24-3fd2-873d-e6cfdb4b8fd4 | -10.24885 | -47.33991 | 2026-06-19 04:27:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 807ca178-c6c7-3169-9b1f-5139cf7b0fe4 | -12.13526 | -48.26001 | 2026-06-19 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8e006282-b5a5-3068-b7b0-fda2c98de0f1 | -16.03246 | -43.41862 | 2026-06-19 04:27:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 0b713492-64f1-352b-ab1a-9962c73c7bec | -12.8757 | -44.36189 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eaa35d9a-8eb5-3eae-9169-7e466bdd8bf4 | -8.90568 | -46.96365 | 2026-06-19 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d3396dc8-acfa-349e-b56f-1a3c21772b77 | -12.50284 | -43.77142 | 2026-06-19 04:27:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 1e923e35-1bce-3c88-b780-29a223b1802f | -12.83651 | -44.36687 | 2026-06-19 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |


[Clique aqui para ver as próximas entradas](README6.md)
