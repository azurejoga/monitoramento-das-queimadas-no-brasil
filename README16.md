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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3650562b-5e15-3052-9a07-9372efa9ea1a | -19.16024 | -54.83768 | 2025-07-02 04:55:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae214213-f99b-3aed-8c59-fe37a4aca91e | -19.52147 | -43.60434 | 2025-07-02 04:55:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ce86e5f-5b8e-364a-9190-052e8b446789 | -13.40969 | -47.8204 | 2025-07-02 04:55:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e878a22-a0f7-3c69-afa2-993a6123f71c | -19.2214 | -55.37558 | 2025-07-02 04:55:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 802ab6b1-88db-32af-b4c3-bd0178cb149e | -13.38386 | -47.85335 | 2025-07-02 04:55:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 933c71c2-8fbe-3c72-b79c-fc9493e06cab | -19.16302 | -54.84194 | 2025-07-02 04:55:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55cc5c89-5910-3240-934c-4b7040b6e9c1 | -16.42774 | -44.52353 | 2025-07-02 04:55:00 | NPP-375D | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35c03fb3-7649-3e86-b40c-f7806f1a26a8 | -18.65652 | -55.7442 | 2025-07-02 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 86168e57-3ad2-388c-8b81-188f447d0216 | -13.38776 | -47.8513 | 2025-07-02 04:55:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8cef1326-68a1-358e-93e1-d79382469768 | -15.89172 | -43.46257 | 2025-07-02 04:55:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9b33538-b4fb-315e-a080-63faf1c45dba | -15.22073 | -47.15337 | 2025-07-02 04:55:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c137d812-bd05-3dfa-b7cb-753f3547a950 | -18.65926 | -55.74843 | 2025-07-02 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 0cd2c118-f6ca-37b3-9cf6-43469a09db1b | -15.89221 | -43.45793 | 2025-07-02 04:55:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9ae44eb-c440-3df2-b15a-a1554c9df2ee | -14.90308 | -45.14094 | 2025-07-02 04:55:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c957054-f543-323a-8477-240c894c083e | -16.38145 | -54.57645 | 2025-07-02 04:55:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c1035cb-27ee-3881-9f71-5b5211c497a2 | -18.66259 | -55.74901 | 2025-07-02 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 73fbd06b-b5ad-32f9-be24-3b61c8484ccc | -17.48857 | -46.74337 | 2025-07-02 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a6a42556-f0a3-32d3-a4bf-b46b7e2763ea | -18.08543 | -54.2785 | 2025-07-02 04:55:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99886987-1a80-3f19-937d-865e8c71e58b | -13.36378 | -46.1976 | 2025-07-02 04:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b6d52a1f-d584-3538-9032-57dc09659d2d | -15.92354 | -43.52125 | 2025-07-02 04:55:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 35ecf78b-a0e1-3b91-914d-f7bab0a3d4ff | -19.15967 | -54.84137 | 2025-07-02 04:55:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 864d9e08-effa-3794-8498-1efd0e8ace7d | -19.52229 | -43.59521 | 2025-07-02 04:55:00 | NPP-375D | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4559f9dd-a96f-3e20-b4ad-80308d63d867 | -13.40915 | -47.82451 | 2025-07-02 04:55:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bbcf1a79-6825-3bf2-9f86-805ae44dd035 | -18.66201 | -55.75266 | 2025-07-02 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| fe653773-0131-3ba1-99d0-b5784ae0df19 | -18.65593 | -55.74785 | 2025-07-02 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| bb1d0b18-35f8-3ce8-b1dd-487019fb705f | -13.39219 | -47.8517 | 2025-07-02 04:55:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 695697e5-b67e-3c43-a4b2-f1f1d53ff305 | -16.07279 | -51.56285 | 2025-07-02 04:55:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 85628f63-5042-3fe3-8e73-a39180b76584 | -14.90529 | -45.14077 | 2025-07-02 04:55:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 701e0b1b-8c95-309e-95c0-8a142c266b0e | -16.06907 | -53.75282 | 2025-07-02 04:55:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6223db41-38b3-37f6-9157-033d577914e6 | -15.89781 | -43.46332 | 2025-07-02 04:55:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 836185a3-d448-3e55-9302-efff1db070d3 | -19.43464 | -48.54835 | 2025-07-02 04:55:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fa652313-d848-34ae-ae9d-37804bcec5fd | -15.57 | -47.85779 | 2025-07-02 04:55:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61ad0b0a-dccf-3bb7-8905-a0cc9b8515d3 | -13.42348 | -47.81797 | 2025-07-02 04:55:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c6bfce7-cee4-3441-91b6-c7a189fbbae7 | -17.87421 | -55.99932 | 2025-07-02 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 34153567-478f-3697-8b53-3199cd182124 | -13.42791 | -47.81848 | 2025-07-02 04:55:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e03497c7-fad5-355e-bb65-809fa3cf79da | -19.43864 | -48.55383 | 2025-07-02 04:55:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a5186b17-7fe1-35ae-8027-ceafcb0b2ac1 | -16.06915 | -51.56228 | 2025-07-02 04:55:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5b8e687-be1d-3ca1-8067-f8ce1deaf014 | -13.41464 | -47.81684 | 2025-07-02 04:55:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c0cb73c-fa75-3cee-8ae9-7acad9b41e4b | -18.08474 | -54.27544 | 2025-07-02 04:55:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06764e60-8460-3474-9b4f-5b311332c893 | -18.42929 | -54.5585 | 2025-07-02 04:55:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac7274ae-50a2-31e6-b31c-d8533075013b | -17.48931 | -46.74143 | 2025-07-02 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aec43c20-5b2e-3570-8ff7-1c8aaadfe9c0 | -15.92276 | -43.51759 | 2025-07-02 04:55:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 702aa285-a98b-3ef7-8bb7-f438d77de690 | -13.38886 | -47.84953 | 2025-07-02 04:55:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b8c1c09-3333-3794-983e-7a2fd64e5713 | -19.52187 | -43.59985 | 2025-07-02 04:55:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3107d90-ba34-3419-b917-cc0072bba315 | -21.85649 | -46.69861 | 2025-07-02 04:57:00 | NPP-375D | ÁGUAS DA PRATA | SÃO PAULO | Brasil | 3500402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ddf9a37e-ff15-3b8d-b532-71c3f995255e | -20.32754 | -53.05201 | 2025-07-02 04:57:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bfdd42bb-d7b1-38b4-9034-2c763d93d298 | -21.50693 | -48.81646 | 2025-07-02 04:57:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 852c5777-8412-3bc9-8305-65a3291af363 | -20.54135 | -48.74733 | 2025-07-02 04:57:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| bd2b5a29-aa06-3601-9a3b-dcf519529a04 | -20.66543 | -48.44139 | 2025-07-02 04:57:00 | NPP-375D | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e62326a6-28c4-33eb-a9c4-14501db348b9 | -20.5408 | -48.75226 | 2025-07-02 04:57:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 94ad346d-1fe8-3660-bdc6-9f6d8ec8cbfe | -19.71081 | -54.61525 | 2025-07-02 04:57:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 03487e75-6959-34f6-bf0d-57426763f25a | -20.32292 | -54.90042 | 2025-07-02 04:57:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 531a79d3-8ba9-3955-b225-131bb2902d7e | -21.61419 | -57.56776 | 2025-07-02 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2140f1a6-0727-3f58-810c-75e5ea8237f5 | -21.85692 | -46.69416 | 2025-07-02 04:57:00 | NPP-375D | ÁGUAS DA PRATA | SÃO PAULO | Brasil | 3500402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c710c23a-fad3-3df4-8ce5-dff644c5bf07 | -20.4764 | -54.38914 | 2025-07-02 04:57:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47938720-19da-33ef-a5a1-182f76c7b97c | -20.72864 | -56.65113 | 2025-07-02 04:57:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 71f45ea9-fa65-38e1-8ebc-0445632b90fa | -19.86027 | -54.38479 | 2025-07-02 04:57:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c058fc7a-e065-3722-a373-c9aec8c53d00 | -21.12334 | -57.52995 | 2025-07-02 04:57:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| c3463bf5-50e8-3e1e-ad82-9aa7687eac6f | -20.53676 | -48.74678 | 2025-07-02 04:57:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d8a39de0-4d68-35a6-a987-25954d108e76 | -20.53621 | -48.75169 | 2025-07-02 04:57:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 8fb1bd2c-0331-3e44-8337-84c042c13029 | -20.47614 | -53.67709 | 2025-07-02 04:57:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e72b77d-54ea-3e33-a509-803844bf0649 | -20.54182 | -48.74986 | 2025-07-02 04:57:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| dbc51ea7-eb04-365b-9466-8fa4bf65862b | -19.93822 | -54.49417 | 2025-07-02 04:57:00 | NPP-375D | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8e80c893-8478-32bb-9b6d-d61eabca197b | -20.66073 | -48.44091 | 2025-07-02 04:57:00 | NPP-375D | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c264c7ec-4b93-3ea5-97a7-f9f294401e01 | -20.53724 | -48.74929 | 2025-07-02 04:57:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 1e6825fe-f6b2-32e6-9dfd-54487d1466c9 | -21.51029 | -48.81938 | 2025-07-02 04:57:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc65159c-8b5b-3b0e-af07-505a850eeaf6 | -20.47583 | -54.39299 | 2025-07-02 04:57:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1917f892-9a03-3524-9e0c-838de486d9c3 | -21.04564 | -55.99921 | 2025-07-02 04:57:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b99bb8a-f65c-3556-892e-eedb11ff8579 | -20.72804 | -56.65483 | 2025-07-02 04:57:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c6bb1c0c-9b65-3dc9-aed9-bcb4496eb59f | -7.7947 | -44.0145 | 2025-07-02 05:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 48ac54e3-e4d9-3d7d-9c39-9fee37ee7164 | -7.8133 | -44.0358 | 2025-07-02 05:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 6c918ec6-7712-303a-ab08-7181dd5bbce0 | -7.8135 | -44.0126 | 2025-07-02 05:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 147.4 |
| c57bb098-9809-3e54-8dc1-8481e5a4bb8e | -7.8135 | -44.0126 | 2025-07-02 05:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 116.2 |
| ede28550-26ca-3960-9a35-5d2dc886a760 | -7.7947 | -44.0145 | 2025-07-02 05:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 1af25dd7-dba0-33c5-b827-899bbb2a4153 | -7.6051 | -45.7464 | 2025-07-02 05:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 9159ddf2-2290-36ed-a747-49257a1405e5 | -7.8133 | -44.0358 | 2025-07-02 05:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 26844e9c-dc2f-327a-b8ef-4412c32fe817 | -3.03313 | -49.43709 | 2025-07-02 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96642625-b69c-3501-87b5-87d4d02dfe30 | -3.03923 | -49.43199 | 2025-07-02 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36c81b5e-2e42-386a-8ed3-7a4042cee755 | -3.03783 | -49.44155 | 2025-07-02 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 645a6148-eda3-35a7-9027-e0e788f5d3a9 | -3.31296 | -48.71641 | 2025-07-02 05:14:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57d9705a-f8a6-355b-aca9-50c82d6782d1 | 0.69215 | -51.44791 | 2025-07-02 05:14:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 33a7a89d-68a7-3fc0-bc0a-d1c3474703ad | -3.03264 | -49.44027 | 2025-07-02 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ff7959c-d3f1-33a5-8d93-279f74083349 | -2.58512 | -51.9233 | 2025-07-02 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 923c0ff2-fcd5-3407-b617-09a5d597aa60 | -3.03258 | -49.44078 | 2025-07-02 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e2f46a36-0d6d-336f-9f88-542a204c7de5 | -3.03215 | -49.44345 | 2025-07-02 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 41b3e73c-577c-3d3e-90bb-bb1b4f5fdc71 | -3.03837 | -49.43787 | 2025-07-02 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 552f1f33-30b1-3fcb-aba7-cf3915a87b88 | -4.31641 | -48.07787 | 2025-07-02 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1727c924-bfbe-3658-ac11-9777abb8aee0 | -4.10577 | -47.93749 | 2025-07-02 05:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6743ced2-151e-374b-a581-51c919d29baf | -3.31903 | -48.71362 | 2025-07-02 05:14:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c509c13d-dacf-319e-8380-c0bb79f36bbf | -3.03887 | -49.43468 | 2025-07-02 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05900ab9-5a61-3ece-8b79-7560249d7039 | -4.28754 | -48.19169 | 2025-07-02 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba51b5d0-1980-3708-96c6-cc6c6c4d512e | -2.989 | -47.45107 | 2025-07-02 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c62fe92f-0534-3a01-9ea3-ed915f51b312 | -3.03789 | -49.44103 | 2025-07-02 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d40999e2-f5f0-30e9-9233-97068a6887cf | -3.03876 | -49.4352 | 2025-07-02 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ad396702-835f-3ee8-b1a3-d2d7aea92b53 | -3.31849 | -48.71725 | 2025-07-02 05:14:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 88377851-af09-3a3b-8cf8-a62caf494134 | -3.03829 | -49.43839 | 2025-07-02 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f7eb47e5-74ad-39e7-b7a7-eff8a0e493de | -4.31577 | -48.08214 | 2025-07-02 05:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82d0a8c0-3319-3230-a759-8f4caf578ef0 | -3.42952 | -52.79818 | 2025-07-02 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 201ba075-a991-366a-8011-3330bd6e321f | -3.03352 | -49.43439 | 2025-07-02 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 217d2379-28b4-38bf-8fb9-58845a7b3a8a | 0.69645 | -51.44725 | 2025-07-02 05:14:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README17.md)
