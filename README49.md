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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ed3f0a4-53d6-3431-9df5-944228301458 | -11.80011 | -50.57193 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 071c1b64-55f0-3654-8008-9c78f8c0038c | -15.80804 | -41.64334 | 2025-09-12 04:06:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 459d0e76-bf70-3bdd-ace1-586b367060ee | -18.06037 | -45.43368 | 2025-09-12 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8276857-cfee-33e3-9162-b378b0613c57 | -12.00239 | -47.77184 | 2025-09-12 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d0a3faf-31b3-3236-8649-5bb086ad4b34 | -14.32909 | -54.13528 | 2025-09-12 04:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 67c46d3e-12ba-357f-a7ab-14dad45b6c8f | -11.64248 | -50.58936 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7236cb79-c47c-3b33-a273-ce37705ec1cc | -17.71822 | -46.14047 | 2025-09-12 04:06:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f021432-56df-33fb-beed-6b28c52cbdc0 | -15.08784 | -48.00792 | 2025-09-12 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e938b83-0e70-3e63-90c0-4a26cdbbc5de | -11.90371 | -46.5232 | 2025-09-12 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1b03554-45d4-32f3-9aea-b55fd8253213 | -12.82009 | -47.97131 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c9b1ab71-12c7-3415-b0ae-c8a3559f442d | -12.88381 | -47.94953 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0917233c-eec3-32cb-9cb6-f95ed4ccef40 | -14.16374 | -46.19229 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 46c83b12-e584-3487-9dd3-1ed48f92594b | -12.89351 | -47.97165 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 11200183-e5f5-3172-9114-4c03c89bfc52 | -15.08706 | -48.0122 | 2025-09-12 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3474486b-9605-3f28-a440-e84b2ed29f02 | -12.82443 | -47.97264 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 86cff5d2-4d7b-301f-8537-39c875cd9c78 | -13.90358 | -48.26399 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 5ebf56db-5234-3d25-a7d3-4ce913081569 | -11.114 | -50.71508 | 2025-09-12 04:06:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 815e269d-ffdc-3636-b363-17b2f9d60e47 | -14.43336 | -52.938 | 2025-09-12 04:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0ae21e7-eb0e-307b-a417-86a849334025 | -18.05402 | -45.42816 | 2025-09-12 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b247ddb3-2048-3d62-9783-2255b4f05a9f | -15.22905 | -44.03939 | 2025-09-12 04:06:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c7f442f-2bd8-3bd8-a4c4-5af5d81b0ad0 | -17.27275 | -46.08944 | 2025-09-12 04:06:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21c22c61-6dab-354e-be7d-8cd332a46df0 | -15.68328 | -47.01604 | 2025-09-12 04:06:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 44e5822f-fd93-3ebe-91b5-bc88d7b2d7f6 | -18.02336 | -46.86112 | 2025-09-12 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 18f0e7e2-3e10-3430-b84c-f3c4380c18c7 | -17.35409 | -46.68203 | 2025-09-12 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| feb4bd6d-6878-3f15-ba82-5a2e3e9aaec6 | -15.64984 | -41.83049 | 2025-09-12 04:06:00 | NPP-375D | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| aa3cdcfb-57dd-3dea-8113-8e702fd8c2c6 | -12.08801 | -47.59029 | 2025-09-12 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7b30a8e2-be6a-3012-9061-23b66fe9c5c9 | -12.93469 | -47.99774 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6f58ddc-ffa2-362c-bfb7-f1e2afb876a1 | -14.36998 | -47.28797 | 2025-09-12 04:06:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebe89888-0337-3965-9c31-659a45e9c7d7 | -11.9943 | -47.562 | 2025-09-12 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 560d7ad8-d78d-3014-b0c5-7d66ce51cd44 | -12.82468 | -52.96392 | 2025-09-12 04:06:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e5cc42d-cc42-35c2-961f-3a76360f4ba7 | -12.09238 | -47.59121 | 2025-09-12 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3f532665-90eb-3d70-bf5a-5a667f0f8499 | -13.35564 | -41.92439 | 2025-09-12 04:06:00 | NPP-375D | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 045b08d6-b45b-37bf-988e-345747bf7621 | -11.48617 | -49.2697 | 2025-09-12 04:06:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 07ca17e7-fe4c-344a-b870-1928cdef22b4 | -18.05683 | -45.43302 | 2025-09-12 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4702158f-85b2-3448-9221-5882cd3fcc9b | -15.78726 | -52.24932 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cdae172a-9d2e-36c9-b206-eaef2794c876 | -15.22236 | -44.0582 | 2025-09-12 04:06:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee7404bf-8239-3269-aa5c-4f7df90119b1 | -13.89765 | -48.24646 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f9bfbcb9-fd60-3d23-aa28-7d48ef760545 | -13.8948 | -48.23714 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3713f457-1a61-3530-a22c-2b0c75c5c781 | -11.77691 | -50.56539 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 733f3eb2-ce42-3553-8b70-5c15e65f35de | -18.61341 | -43.96379 | 2025-09-12 04:06:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 051609dc-f106-3600-9ec2-2bc3520059d3 | -14.42117 | -47.33605 | 2025-09-12 04:06:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d79ad00-c5da-3eba-a437-fe8b13155de4 | -15.79262 | -52.24608 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 97c281c3-06e9-3202-9138-bce09ca55de7 | -13.9022 | -48.24675 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 17673db3-9181-3530-bebf-1394e9b03207 | -17.20977 | -48.69641 | 2025-09-12 04:06:00 | NPP-375D | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07eb0763-093e-3c0f-9a8c-3cba45aeb257 | -13.89648 | -48.22816 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7d908841-7085-33a3-b490-a8740e222ea3 | -15.57603 | -54.77207 | 2025-09-12 04:06:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f0f9112b-775f-3478-b1d0-e4818dc385b0 | -16.2835 | -45.68413 | 2025-09-12 04:06:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d7c733d8-cb90-324c-b6be-92edb2aa49eb | -11.51975 | -50.60812 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f314dde-94bc-3c77-811d-e3fa1826c3fd | -15.0936 | -48.013 | 2025-09-12 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 444d2981-037f-37fd-924c-c45c7ff359d9 | -11.81084 | -50.5741 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93f06754-0176-346c-8957-ee4cd359ce45 | -15.12424 | -48.61389 | 2025-09-12 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bd63b27-8f6e-30aa-a499-8470f0bdf80d | -17.91014 | -45.90503 | 2025-09-12 04:06:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 027408fb-9089-3756-87b1-eb43aa62aeb4 | -15.24287 | -44.04183 | 2025-09-12 04:06:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67f29cfb-0ecc-3833-ad67-95a518656af4 | -15.87785 | -48.18421 | 2025-09-12 04:06:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 61899e9f-977e-3aac-bb5a-c5e096dbe7a9 | -11.52103 | -50.38745 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 0bff3422-51c9-3223-ac66-ecf784fb6707 | -17.35057 | -46.70171 | 2025-09-12 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2306a981-4794-314f-abad-b4036cff8dd0 | -17.95957 | -45.28905 | 2025-09-12 04:06:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1784f343-e73b-3adf-be2f-ca9190fb31f8 | -11.09609 | -51.98057 | 2025-09-12 04:06:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b2bec99-e715-39c6-8e0a-eef52d021f7c | -15.21781 | -41.80415 | 2025-09-12 04:06:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| befd651d-782e-366e-bb3e-a6d3995ea3ed | -15.44529 | -43.63965 | 2025-09-12 04:06:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 208fc1d0-7b13-38a8-ae97-e3ffab2e51cb | -14.38464 | -52.95367 | 2025-09-12 04:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c899510a-0b27-3857-9c83-1306289df548 | -16.9562 | -45.81816 | 2025-09-12 04:06:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 4d98d9f6-098c-3ec4-a8fb-cb5656c8c621 | -15.56127 | -41.79412 | 2025-09-12 04:06:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4335402b-2a13-35b8-bd6c-b76ca2e1f20d | -13.30867 | -42.38744 | 2025-09-12 04:06:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| df6aa900-7170-3f1e-8778-bcaf2619d5f5 | -18.40959 | -44.45928 | 2025-09-12 04:06:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aea0e208-0c7b-3716-b6bd-707f7e9eea38 | -12.82634 | -47.96248 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f6b447a0-1aba-38a8-9834-8c036c9c539a | -17.47824 | -43.73435 | 2025-09-12 04:06:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b9ca9740-fd44-36d9-9f3c-8846312a7709 | -15.78713 | -52.24458 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 83defaf9-8ee8-348e-a1a1-0ca033bd1553 | -18.11858 | -45.32963 | 2025-09-12 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 89fe0643-6cec-3f7e-9c9b-93288cfb0bda | -14.1787 | -46.17566 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 297a3cb4-face-310e-951e-8b1c3019fa9e | -12.46942 | -47.50061 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebb380eb-45e9-3bd0-8d1f-9a0a5d8143a5 | -15.86718 | -48.33706 | 2025-09-12 04:06:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7caefde-9695-3e70-864f-e5b1192434e3 | -14.32671 | -54.11937 | 2025-09-12 04:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c2845381-1a28-3ea1-9812-f1f5cb2147f1 | -15.15207 | -52.40237 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 070f7d42-25c8-3475-b7a2-32c0a465583d | -15.08542 | -52.43745 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6cb5f8da-3763-3b66-b2e3-a4627453ba24 | -15.54632 | -49.74683 | 2025-09-12 04:06:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7597f334-81c4-3320-90ad-d38290fb01e7 | -11.5231 | -50.59069 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cabdc0d8-9cf2-3ef6-85ff-fc6078b76e16 | -15.64098 | -41.82164 | 2025-09-12 04:06:00 | NPP-375D | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e58d12da-c30a-3c06-9a2e-0762b2087bd8 | -15.2325 | -44.04 | 2025-09-12 04:06:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 235c1840-3ff6-3d21-b862-55fcad8c64e6 | -13.17364 | -47.26499 | 2025-09-12 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 452e0838-796d-3a6d-828f-715fa3b8f4b1 | -14.43409 | -48.42282 | 2025-09-12 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2862df22-2390-3a8e-bd15-4256e7c84144 | -11.81799 | -46.73009 | 2025-09-12 04:06:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eef36354-fd4e-39f5-af21-af6d53af10f9 | -16.42221 | -45.68521 | 2025-09-12 04:06:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b251413d-5f17-384b-b594-28c9028068c9 | -12.09318 | -47.5868 | 2025-09-12 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7d43e51d-80a7-3474-97c2-a770b7052c3a | -11.03296 | -51.51894 | 2025-09-12 04:06:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b4f414b-44b2-3fc9-a9c0-d7ec05bfb64c | -11.96539 | -51.17952 | 2025-09-12 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4ad8cb2-90aa-334a-9d59-1dc978deb0e4 | -15.5585 | -41.78999 | 2025-09-12 04:06:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f607d518-607e-37a9-8415-d781b0fa1017 | -17.13387 | -48.4986 | 2025-09-12 04:06:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 86715b08-6c9a-3e9b-b521-e3cefb72cb97 | -13.89564 | -48.23263 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| beac6c7c-8204-3a55-b34c-4fc85f390f0c | -14.39844 | -41.44576 | 2025-09-12 04:06:00 | NPP-375D | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1d45e925-4d73-374e-ad9d-f50f7917abd4 | -11.86455 | -46.76352 | 2025-09-12 04:06:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1be98d24-e27e-308f-967f-4fbba0933f31 | -11.18324 | -55.07953 | 2025-09-12 04:06:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 67b66224-1dcd-3114-a82a-21c54553f0a3 | -11.53122 | -50.60684 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c846880a-c25c-3fb0-981e-ff2dcda48d7e | -18.05388 | -45.44987 | 2025-09-12 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e2e8fa0-79bf-3b52-9bf9-64fb06b93b16 | -15.80471 | -41.64278 | 2025-09-12 04:06:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 68fde515-bda7-3736-8838-c74100f07c02 | -17.93605 | -46.92986 | 2025-09-12 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e0bc5a3-0e63-379e-8913-34d2d43fef3d | -13.17657 | -47.26809 | 2025-09-12 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e29950a3-5843-36ad-ac5e-e7286f22cc58 | -15.91983 | -51.79802 | 2025-09-12 04:06:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 47019deb-a986-367d-862e-24c3d6fdc851 | -17.4761 | -43.72628 | 2025-09-12 04:06:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f028dff5-0c8f-38f9-a222-1dd798eb5f3d | -17.35234 | -46.69183 | 2025-09-12 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README50.md)
