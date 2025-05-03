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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25496b23-60f9-33e0-85cd-b3625bf62bd6 | -23.52012 | -46.97293 | 2025-05-03 04:04:00 | NOAA-20 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| a616a786-95be-3c44-a66f-0630bc49bed9 | -20.71865 | -54.41251 | 2025-05-03 04:04:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 342fd84b-6e20-3be9-834a-885cac8f2314 | -20.81679 | -55.53286 | 2025-05-03 04:04:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 620aac3a-6320-3611-80cd-ae6d7ca28df9 | -24.24084 | -50.74101 | 2025-05-03 04:04:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6e172db2-aac8-3081-b2c0-207d4a6519c7 | -20.76296 | -46.76966 | 2025-05-03 04:04:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 91622c22-25bc-37d0-95d3-898e8ee0a352 | -21.63211 | -48.34269 | 2025-05-03 04:04:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27c3d523-3e07-39bb-98f8-b2c2b02fc4e1 | -21.02545 | -55.64972 | 2025-05-03 04:04:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c52f7274-279b-3703-b559-bb0af23246f6 | -23.78891 | -54.85216 | 2025-05-03 04:04:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8c8b9909-283c-386e-9071-acfa23677e80 | -23.98234 | -48.91941 | 2025-05-03 04:04:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26fdac77-7d0d-3883-bb35-dfa6c4727bc8 | -19.94983 | -49.82391 | 2025-05-03 04:04:00 | NOAA-20 | RIOLÂNDIA | SÃO PAULO | Brasil | 3544202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 418f0a92-4faf-3e00-a490-b473bb5361ad | -20.81655 | -55.52923 | 2025-05-03 04:04:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63c83ec8-8082-3757-873b-4615020448a4 | -23.78801 | -54.85608 | 2025-05-03 04:04:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1c1ff337-fe89-3969-bfd6-735e879ceffd | -22.24506 | -52.97786 | 2025-05-03 04:04:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 52b1f5af-4fc9-3056-b6d9-e0a04fdec63d | -23.78428 | -54.84679 | 2025-05-03 04:04:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b537ddc9-3131-3717-b56b-636507684582 | -21.26978 | -43.0444 | 2025-05-03 04:04:00 | NOAA-20 | PIRAÚBA | MINAS GERAIS | Brasil | 3151305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| df2e9ce8-60f8-3de9-9a68-8d8cab4c28e5 | -20.71994 | -54.40765 | 2025-05-03 04:04:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a55cc431-ad09-343b-a181-b9a684cca9e2 | -20.99232 | -51.79398 | 2025-05-03 04:04:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 16c73007-7e2d-3a75-92b6-aaf4b7487c45 | -23.79188 | -54.85575 | 2025-05-03 04:04:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6f77a8b0-0a77-3a0b-890b-b05f89314930 | -23.78824 | -54.84632 | 2025-05-03 04:04:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3c123103-eb50-3a35-a2be-645b4565050e | -21.17955 | -43.97944 | 2025-05-03 04:04:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4d986cc4-8811-3a53-9be7-90980478aa52 | -21.13637 | -48.61634 | 2025-05-03 04:04:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| edfc3563-4050-37ce-bfda-a28cc38446d4 | -21.14972 | -48.61158 | 2025-05-03 04:04:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 802b7b6a-d661-3ba3-89a1-6db013ac4f63 | -21.98351 | -46.82038 | 2025-05-03 04:04:00 | NOAA-20 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f48f2562-f3e6-318d-b1f1-a1727031bb64 | -25.08764 | -50.53021 | 2025-05-03 04:04:00 | NOAA-20 | IPIRANGA | PARANÁ | Brasil | 4110508 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9ee8b371-1968-34b8-a6c2-12fa3e307826 | -30.79972 | -52.88745 | 2025-05-03 04:06:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| f98fbf2e-0b8f-3284-82dc-6eac8b7e4859 | -6.7053 | -42.1234 | 2025-05-03 04:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 63.0 |
| 16fef2df-915c-32e5-89fb-b883e4583526 | -6.7053 | -42.1234 | 2025-05-03 04:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 68.3 |
| 3a3205e8-acc4-3232-bf80-5daa8f6b2177 | -6.7053 | -42.1234 | 2025-05-03 04:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 58.2 |
| 97e49511-4898-3c6d-aaab-907171458940 | -6.69808 | -42.12617 | 2025-05-03 04:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 4aa40343-0aea-3251-9006-68c0d1f346f2 | -6.70391 | -42.12699 | 2025-05-03 04:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| ed70d6aa-2465-3172-987e-c4b067cb089b | -5.79217 | -43.61909 | 2025-05-03 04:49:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06a07acc-8f8e-32ed-a69f-a834b84025fe | -4.10477 | -47.72813 | 2025-05-03 04:49:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d4c0b4b-3b3a-3885-b221-78d69bc1013d | -2.36663 | -51.86454 | 2025-05-03 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb26df63-5b76-3c7b-a54e-cc95fb6ccecf | -5.79263 | -43.61583 | 2025-05-03 04:49:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 049ec9e4-309b-3610-a2ca-315a893fcd70 | -6.96419 | -42.79725 | 2025-05-03 04:49:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1ccac41c-34e1-35a0-9a80-2043344af5ba | -6.71545 | -47.59501 | 2025-05-03 04:49:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 176b9575-0299-3291-8e42-512a5c1aea9f | -2.65168 | -48.79654 | 2025-05-03 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c8f9df43-e921-3a45-bb53-70cfdca693b1 | -2.65524 | -48.79707 | 2025-05-03 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1229e40e-481e-3af2-a3d6-4a360937bc21 | -6.69835 | -42.12479 | 2025-05-03 04:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 19.7 |
| b580c806-7936-3f87-a57b-26a26f57a49b | -5.17001 | -45.10637 | 2025-05-03 04:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 459430a5-aa2e-394f-a2dc-229a505707bc | -6.70359 | -42.12977 | 2025-05-03 04:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| e286c3f1-0f95-3c7e-a9e0-ecbd35d51088 | -6.49643 | -44.72862 | 2025-05-03 04:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fea19657-fd46-33c2-a01e-32a3853a3cd3 | -5.16535 | -45.10575 | 2025-05-03 04:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b36c3e33-a699-38aa-bab2-1fbd1b3bbf45 | -6.96471 | -42.79341 | 2025-05-03 04:49:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8a5b8c82-92e7-3f82-9f20-3c00c996ec68 | -6.70336 | -42.13116 | 2025-05-03 04:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 23a34401-701c-3bdb-b6d6-42a584ee140c | -6.69719 | -42.13313 | 2025-05-03 04:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 4125178a-b881-3fe6-92b7-87189cc355b0 | -6.70302 | -42.13391 | 2025-05-03 04:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| b1f56f01-fa41-3bd3-be5b-1aedf1f42759 | -6.71946 | -47.59571 | 2025-05-03 04:49:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e88640f-fede-37fb-bd95-55278ce5eeef | -2.6523 | -48.7925 | 2025-05-03 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eaaefb2b-e263-3a95-a37e-9671e7128bad | -6.69753 | -42.13037 | 2025-05-03 04:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| ec6c84b5-7dc9-3db9-ac4b-55cb2f150c4a | -6.69777 | -42.12898 | 2025-05-03 04:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 42d2475a-f82a-3939-9d4f-07dcb9a94979 | -2.65586 | -48.79304 | 2025-05-03 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 650439c8-8a9c-3c65-b9e1-be89a7e2ff85 | -12.55675 | -57.70677 | 2025-05-03 04:51:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7160fd8d-f672-36b2-be6c-31e098d2789e | -13.04171 | -53.72961 | 2025-05-03 04:51:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9f4a557-f79b-3cc3-b7df-0ceaf58b7ae2 | -7.68667 | -42.98884 | 2025-05-03 04:51:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| e7c12303-d8b8-38b2-8bd7-44b00df23eeb | -7.18332 | -44.87991 | 2025-05-03 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1636c4c-0553-3c5b-8673-2364489c0ac8 | -12.66416 | -58.10187 | 2025-05-03 04:51:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9f9950e9-4448-3b94-888d-03ee72d2c38f | -13.05148 | -53.71289 | 2025-05-03 04:51:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f8fada2-3bb5-351e-8926-5baa27e54b9f | -12.51611 | -57.64073 | 2025-05-03 04:51:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58eebb0a-c9e6-3b80-82cb-7e35643f2259 | -13.69521 | -45.20189 | 2025-05-03 04:51:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ef7ee95-11f5-3f78-9398-01385a02bc29 | -13.17429 | -53.24529 | 2025-05-03 04:51:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afddd0f6-2f7b-3dd1-963a-e3f99d37367b | -13.69482 | -45.2053 | 2025-05-03 04:51:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7eb8b241-abe9-36f6-a478-c163e01db4c4 | -7.1853 | -44.8786 | 2025-05-03 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d74520e7-8445-361e-9703-342e498ac6b7 | -13.70083 | -45.19925 | 2025-05-03 04:51:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04025b9e-7bc4-3ae6-9fff-6ab091f57957 | -12.35383 | -54.51647 | 2025-05-03 04:51:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dfde6c2d-1f8c-3e52-8be7-224fa59d05c8 | -7.67553 | -42.98706 | 2025-05-03 04:51:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| f6c135e9-b687-3eed-8f76-c727c6ea8237 | -7.6811 | -42.98798 | 2025-05-03 04:51:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| a21aff42-31da-30e2-8ff8-39c3d237fe6f | -12.68123 | -58.09292 | 2025-05-03 04:51:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 722c09ea-73bd-34e2-834d-000ce103cef7 | -7.68158 | -42.98432 | 2025-05-03 04:51:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 5e32d2e0-cc61-3972-b97c-1fe8c66fcbdb | -13.05093 | -53.71642 | 2025-05-03 04:51:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56396848-2ded-34d0-b785-28b0bd0cf42e | -13.70004 | -45.20603 | 2025-05-03 04:51:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93c4e354-9797-31b5-a0b8-7441f3e1b332 | -12.66336 | -58.10661 | 2025-05-03 04:51:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1c9b0f88-e826-3936-904d-891a65c620c9 | -13.17097 | -53.24476 | 2025-05-03 04:51:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd69fc69-d5a1-3413-b9dd-f33c194c21f8 | -12.66449 | -58.09966 | 2025-05-03 04:51:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4263ce95-bdad-3d84-aab1-8e32fff736f9 | -13.69403 | -45.21209 | 2025-05-03 04:51:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa0daea2-40cb-3a6b-b9e1-7c4b5502ce9a | -13.70044 | -45.20264 | 2025-05-03 04:51:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5795bfe-3edd-3b1c-b081-319f5a114765 | -7.68715 | -42.98516 | 2025-05-03 04:51:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 258e1147-5350-31fa-948e-b141a3fc1df1 | -7.68063 | -42.99152 | 2025-05-03 04:51:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 2564f87d-a0f1-35ab-beb5-31d606403939 | -13.04557 | -53.72661 | 2025-05-03 04:51:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4af440d9-4644-32f0-b013-a108571d1f45 | -13.69442 | -45.20869 | 2025-05-03 04:51:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c9e0b65-e354-3a18-bf57-739a93f1366c | -12.66284 | -58.10909 | 2025-05-03 04:51:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d2fa8d59-2369-3b43-ab44-3c77975f7a8c | -12.66366 | -58.10437 | 2025-05-03 04:51:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 44d2ff9e-9c60-3f98-8a63-82dd20b9ccec | -18.94788 | -52.3838 | 2025-05-03 04:53:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 311b11b0-f388-3aed-8fc2-71b3ab001863 | -16.31417 | -53.82025 | 2025-05-03 04:53:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ca0e4af-df8c-363b-b731-86f20c81fa46 | -18.26053 | -53.01132 | 2025-05-03 04:53:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 401818e1-185c-3842-8d0a-e3046bc7996e | -18.25815 | -53.01144 | 2025-05-03 04:53:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e7fa2ac-bf22-3eeb-95ac-a346f548b16b | -16.67981 | -43.88511 | 2025-05-03 04:53:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ced45d1a-cb0d-316b-8708-45353e0041c1 | -19.95588 | -49.82712 | 2025-05-03 04:53:00 | NOAA-21 | RIOLÂNDIA | SÃO PAULO | Brasil | 3544202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7408857c-819c-3e5d-9982-3d418b1b2def | -18.2524 | -53.00239 | 2025-05-03 04:53:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48b04273-f044-3aa9-af1a-742c7e79197b | -16.31308 | -53.82755 | 2025-05-03 04:53:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0597415c-71e6-3c98-8b08-108938fc722d | -18.59746 | -51.04112 | 2025-05-03 04:53:00 | NOAA-21 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5d8f7cc4-14a0-36aa-a25d-f3f660c9f316 | -17.62278 | -50.91529 | 2025-05-03 04:53:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bd3cbfe2-0087-30e8-923d-2a4977163873 | -16.31363 | -53.82389 | 2025-05-03 04:53:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6fe2edd-f5f7-3f52-b9eb-43213f152dc4 | -15.29002 | -53.20751 | 2025-05-03 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 305dd72b-0a48-34cc-b7bc-54d6b72626dc | -16.31084 | -53.81969 | 2025-05-03 04:53:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 176c4d9b-0eb3-39d7-847e-b3077bcbee94 | -18.25298 | -52.99842 | 2025-05-03 04:53:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6cc6cdaf-6267-370e-8ddc-52f5208c5e59 | -16.31029 | -53.82335 | 2025-05-03 04:53:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3956089a-9479-3444-a81e-0d02dcb2cdea | -17.62657 | -50.9159 | 2025-05-03 04:53:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d32190bb-27c0-3526-88ac-2024ee7df857 | -16.68391 | -43.88623 | 2025-05-03 04:53:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0397169c-ac74-3574-90f7-b228e0fa2d09 | -18.25997 | -53.01528 | 2025-05-03 04:53:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README5.md)
