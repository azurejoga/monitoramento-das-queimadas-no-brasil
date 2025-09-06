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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b0130c9-c49c-3791-8b6d-9d72c8e5622b | -20.5397 | -46.46994 | 2025-09-06 04:19:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17a25a41-3db3-34c8-8013-e6d8bffb8e7d | -22.76686 | -47.4141 | 2025-09-06 04:19:00 | NPP-375D | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1ec6f616-b286-3094-944e-2cb87ccb567c | -17.76268 | -42.51718 | 2025-09-06 04:19:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 94fe3fcf-1658-359f-aa05-3110cdf6f7ef | -22.11971 | -45.78821 | 2025-09-06 04:19:00 | NPP-375D | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9075ba2c-902f-3eb3-ba38-fb2f72ce97e7 | -20.53031 | -46.46444 | 2025-09-06 04:19:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c7e248f-3ead-39e0-980e-b3ec364c91a7 | -12.94356 | -46.56645 | 2025-09-06 04:19:00 | NPP-375D | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| bda4ae38-6e6d-3f39-a693-d90c1a39f25c | -19.88829 | -57.92077 | 2025-09-06 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 8a91aea0-e961-33c6-8927-ce98fd85fcfe | -15.72037 | -53.57067 | 2025-09-06 04:19:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 72adbab1-1d16-32ec-be0f-5e2c368d3d78 | -16.3217 | -52.94378 | 2025-09-06 04:19:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f19da25-25e1-3a16-b450-fb9ffc0899bd | -12.52911 | -48.06239 | 2025-09-06 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9317ff6-a448-3988-a048-de09e0b497b4 | -20.90663 | -41.81328 | 2025-09-06 04:19:00 | NPP-375D | VARRE-SAI | RIO DE JANEIRO | Brasil | 3306156 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ab3dc84d-7f4a-3bab-9f10-2ce110dac2fa | -20.46536 | -48.78698 | 2025-09-06 04:19:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2bc250d6-4199-319b-b695-96ad8969f6e0 | -12.09313 | -45.68895 | 2025-09-06 04:19:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e04cb665-61cb-38a2-a884-ceecb67c5584 | -12.01352 | -47.78063 | 2025-09-06 04:19:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5d1282a-fe45-31ac-ba22-f718411d30d0 | -20.35518 | -48.64656 | 2025-09-06 04:19:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5d79e3d-6b22-35b1-a680-fbdb4916ac70 | -20.10747 | -44.31429 | 2025-09-06 04:19:00 | NPP-375D | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 66c89bba-d431-3839-b325-fd6073bd2b04 | -11.6312 | -47.80547 | 2025-09-06 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c326f2c0-1841-3b0a-8889-50b1ab3e00bb | -11.3224 | -55.21983 | 2025-09-06 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80c26803-2215-3103-b45e-7daf0c92eb9e | -18.4406 | -45.93475 | 2025-09-06 04:19:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e91bb13-2f51-3b6d-bb29-97856371e3f1 | -17.71351 | -44.49164 | 2025-09-06 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3724b549-373a-3d73-82eb-f68f0622f19b | -13.18601 | -44.48574 | 2025-09-06 04:19:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 688a205d-f2a8-326b-aeb7-88dda5e12ef7 | -22.23836 | -48.76168 | 2025-09-06 04:19:00 | NPP-375D | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 887fd0ac-f0a6-3e62-94ce-a4f7d84a175a | -20.91914 | -44.01612 | 2025-09-06 04:19:00 | NPP-375D | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2e357bae-c192-38d3-ba7a-e5b44409434f | -23.83969 | -47.7544 | 2025-09-06 04:19:00 | NPP-375D | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fe39ed69-34e0-3bc0-9f60-d30818884aa5 | -20.35239 | -48.64186 | 2025-09-06 04:19:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41542509-0349-3f93-ab39-9aa6c35a0d50 | -17.6939 | -44.50714 | 2025-09-06 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7fe038a1-f393-3a1a-bebb-929e4fc62bce | -22.25207 | -48.76447 | 2025-09-06 04:19:00 | NPP-375D | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f88edd0a-fa77-375d-842f-8a6e80ca602e | -23.3424 | -50.86889 | 2025-09-06 04:19:00 | NPP-375D | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a5d1bd6b-711c-332a-b040-a105d84c9dc9 | -12.73132 | -45.09576 | 2025-09-06 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ca01fab-dda2-3fe8-8ee8-af81b16d9852 | -10.79188 | -47.73255 | 2025-09-06 04:19:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| cf02a209-3fb3-3632-bd8a-84500dbec02c | -21.49358 | -46.19043 | 2025-09-06 04:19:00 | NPP-375D | DIVISA NOVA | MINAS GERAIS | Brasil | 3122405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a734cadc-692e-3d9f-8c85-9da0cba052e9 | -10.76964 | -48.27202 | 2025-09-06 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f44baf97-ea4e-34f2-ad42-578b92ecada3 | -20.85555 | -54.98684 | 2025-09-06 04:19:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b148495a-6a32-31e7-85a8-509347b00402 | -15.69016 | -53.59287 | 2025-09-06 04:19:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c3f587ec-0ea4-381a-8dfe-2d58bf37558b | -18.81521 | -53.27341 | 2025-09-06 04:19:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d92cf1dd-5889-30dd-965b-09891b749168 | -11.2132 | -55.01625 | 2025-09-06 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cebc909-c069-3a94-8ce3-64c6785e6707 | -22.25634 | -47.30619 | 2025-09-06 04:19:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 8d6a6b85-e8fb-3a76-bfe4-fe71ba66f311 | -12.0106 | -47.77563 | 2025-09-06 04:19:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 304230bb-39d9-3f87-8a8a-28f4c79f2ba2 | -19.40865 | -44.31408 | 2025-09-06 04:19:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c762af3-0678-34ed-9c7b-b93b803ebc51 | -19.77331 | -44.20268 | 2025-09-06 04:19:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ca168c5-c8ef-3bf0-a9d5-bbf3e6e05633 | -22.24727 | -48.751 | 2025-09-06 04:19:00 | NPP-375D | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f0323a2b-919f-3aa1-aa5c-a184249340c8 | -22.27003 | -49.56429 | 2025-09-06 04:19:00 | NPP-375D | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c9659a7e-6e24-3955-b42e-e815f09c3af4 | -22.26232 | -48.74586 | 2025-09-06 04:19:00 | NPP-375D | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 157eef57-dbef-3d96-a92a-1c379289e8d7 | -11.01048 | -45.91774 | 2025-09-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4694b2b5-68dd-376b-ba29-75a27a3746eb | -19.81202 | -57.95057 | 2025-09-06 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 35a1a2c6-4e3a-3d08-8906-1bb8b699d149 | -20.46487 | -48.78836 | 2025-09-06 04:19:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 90264c8b-b207-3479-9fe0-0ebaba117c24 | -12.0062 | -47.77924 | 2025-09-06 04:19:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e787e14b-93ad-3821-8132-ac025cf9f6d4 | -15.69129 | -53.58719 | 2025-09-06 04:19:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 160c4493-75d1-34fa-ac52-7227982fca8f | -11.54366 | -47.31429 | 2025-09-06 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e407e72-d6eb-3506-8844-d9ee6dab778b | -19.89913 | -57.92854 | 2025-09-06 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 644dca03-43e3-3722-ae36-e31eeaf3c2ef | -12.00253 | -47.77858 | 2025-09-06 04:19:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c3fbfb1a-3102-361b-9030-bc288bf83b3a | -18.44364 | -45.93124 | 2025-09-06 04:19:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 39eb9c6c-3c77-3f38-af54-3e0e47b10412 | -17.70959 | -44.49477 | 2025-09-06 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1d99994-9b93-3ee1-9c1e-2e8ca2b6da83 | -9.97419 | -51.63897 | 2025-09-06 04:19:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1fdb0b88-aa78-3162-9a8d-d1f96a3bafa6 | -11.38873 | -43.55464 | 2025-09-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 742e137c-8b86-357e-85b9-b3ebbdf5141b | -18.56148 | -44.03896 | 2025-09-06 04:19:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d25fa9b-59a8-35d3-8674-338613d16753 | -23.32963 | -50.87601 | 2025-09-06 04:19:00 | NPP-375D | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4a596b7c-722a-323f-9482-7a3407379ae6 | -16.60465 | -48.94841 | 2025-09-06 04:19:00 | NPP-375D | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80671f78-b684-3d5f-8c96-67d5bc97ff7a | -12.65314 | -41.2353 | 2025-09-06 04:19:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 04428525-21e3-32de-b19a-217dfcf651d0 | -11.62978 | -47.80175 | 2025-09-06 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f73379a-798d-3f3f-a402-2f6fd3652c1f | -11.00407 | -46.02106 | 2025-09-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eef0c5fa-5c1b-34ac-ab7d-6e7b488271c5 | -20.53422 | -46.46135 | 2025-09-06 04:19:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ef445c4-6601-35a8-834a-801837448b04 | -18.60846 | -48.20928 | 2025-09-06 04:19:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a17df33c-ce4d-3357-9028-4a433887f406 | -19.63291 | -49.38924 | 2025-09-06 04:19:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4be7bb0-a830-38a2-8019-70effe009578 | -19.21174 | -42.87541 | 2025-09-06 04:19:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 05c7bbdc-af84-3cb0-ad8c-1b03206aed82 | -20.91565 | -44.01549 | 2025-09-06 04:19:00 | NPP-375D | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 858ea499-4d1e-3545-bfd5-423e9f90953e | -19.83313 | -43.18607 | 2025-09-06 04:19:00 | NPP-375D | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f6f53620-6037-331a-a50f-a48c046c7d06 | -10.21615 | -49.72678 | 2025-09-06 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06339075-e6ff-357e-8775-a249f61a20cb | -18.14619 | -51.77607 | 2025-09-06 04:19:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ffd33b4-ca54-3106-871a-3bc1b4da192d | -20.52557 | -46.11066 | 2025-09-06 04:19:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2ffe43e-2eb1-3a18-ab71-78f80145faf5 | -17.69554 | -44.49631 | 2025-09-06 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b2671da-2330-3d31-bd76-5c6d76533006 | -16.33224 | -52.95976 | 2025-09-06 04:19:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b569467d-cb8e-3efc-a20f-e4c02153eba5 | -10.74551 | -46.34014 | 2025-09-06 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d380fef-5b6f-3982-a494-0b0f438e7280 | -18.11522 | -44.48341 | 2025-09-06 04:19:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ba07056-b0cd-32a3-bfa5-0a81f1fc0a03 | -12.29664 | -49.99638 | 2025-09-06 04:19:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 310fb72a-e4a2-32fc-92b6-1c9cd274697e | -15.72307 | -53.58311 | 2025-09-06 04:19:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4e947149-0655-3861-b0d4-02197df659dd | -19.8953 | -57.91766 | 2025-09-06 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| f1169c01-9a65-322f-9036-e09e65358e88 | -23.36641 | -47.17761 | 2025-09-06 04:19:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ce8aac61-4f6c-330b-a4b8-351f8b28bfc7 | -17.23768 | -46.71326 | 2025-09-06 04:19:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9abed81c-576c-3124-bb9e-d58705c3488e | -16.32949 | -52.94858 | 2025-09-06 04:19:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 512ad2f7-78f7-3993-b726-8c950827ff7c | -16.32072 | -52.94867 | 2025-09-06 04:19:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8ed764f-743e-34ec-a34e-7e9563913565 | -22.74318 | -47.03442 | 2025-09-06 04:19:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3a7a3d36-1c95-3e7c-aeac-2b39748f9f99 | -18.44118 | -45.93111 | 2025-09-06 04:19:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c3d27d3a-65a9-3903-a86b-87f931258f01 | -17.73082 | -48.64374 | 2025-09-06 04:19:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 561bbe60-9072-36ca-a94e-2b27e0c5542c | -11.21822 | -55.02183 | 2025-09-06 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6584b09-b276-37e1-9b98-56b201a32156 | -22.24932 | -48.75975 | 2025-09-06 04:19:00 | NPP-375D | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| cb2c7a29-735d-3aa0-8694-426bd99f406a | -17.64363 | -44.26288 | 2025-09-06 04:19:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 433b9886-15d1-3846-a4a4-9287e67e4ad5 | -17.0026 | -49.37381 | 2025-09-06 04:19:00 | NPP-375D | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ef0688f-ee7c-3c03-a9e0-8188ab41219f | -22.65447 | -46.82598 | 2025-09-06 04:19:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9bc93396-fa82-37b0-95f0-40976da01217 | -19.62417 | -46.01319 | 2025-09-06 04:19:00 | NPP-375D | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14031d01-a176-3ba5-ab36-cffdfff6cb04 | -1.45776 | -49.46431 | 2025-09-06 04:36:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3a6cd6f2-3482-3857-9ff2-93022a2b9261 | -2.77651 | -41.80388 | 2025-09-06 04:36:00 | NOAA-20 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d1ec95b-178d-35f7-9488-25e2c0b58c07 | -2.77194 | -41.80319 | 2025-09-06 04:36:00 | NOAA-20 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfe8d175-73cb-3eda-a5fb-47152d561e92 | -0.99224 | -50.99658 | 2025-09-06 04:36:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40a93d1e-a863-3d68-9833-91688ba643b4 | -2.02098 | -47.55339 | 2025-09-06 04:36:00 | NOAA-20 | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 818fa25e-2c2b-315b-8eaa-02429c985c3d | -1.44465 | -51.63153 | 2025-09-06 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1245fae-e8db-31da-aeca-f294a1465151 | -9.08446 | -47.01017 | 2025-09-06 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e8de37c0-46d6-34b8-b679-df4ab92de689 | -6.91523 | -44.68981 | 2025-09-06 04:38:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6a7910c-e3f8-3da5-9031-4bcc5c125ff4 | -6.30754 | -44.57874 | 2025-09-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2caa19cc-7a5c-35f7-9e0e-9404822b52da | -7.33656 | -48.49802 | 2025-09-06 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README52.md)
