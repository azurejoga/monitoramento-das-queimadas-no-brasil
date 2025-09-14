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
| 05de502e-7bcb-34cb-8232-5bdce8f58480 | -13.92009 | -48.30447 | 2025-09-14 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8beb0474-2bfd-3e76-869c-aefcc7614410 | -15.20634 | -52.49105 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ea19b809-7a9f-33a8-b7fe-04caf5598589 | -15.19737 | -50.11849 | 2025-09-14 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 604997bc-15d2-32f2-bbc5-89ec88dceb30 | -17.27935 | -46.10068 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 62c45089-4047-3a5d-a14e-a825e2969fcc | -15.63916 | -51.34293 | 2025-09-14 04:42:00 | NOAA-21 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 517c77ae-539b-3d20-a588-0c6a0a363f7e | -17.79335 | -51.72521 | 2025-09-14 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8756e611-5b7d-3d9d-a20e-d320c48d8ac6 | -15.12192 | -52.48741 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8012ca5b-f345-3942-b44b-822891606823 | -15.766 | -52.22767 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b1d8b817-c197-3258-b3de-5c89f7a38e35 | -15.29456 | -53.77466 | 2025-09-14 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44cc6a14-2b25-3c0b-88ba-d3f827cbd1e9 | -12.65982 | -54.66174 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5a40f0cc-6d66-38b3-a5df-9a1d1460464b | -15.69114 | -49.91544 | 2025-09-14 04:42:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 08a2a4e4-c4b2-3260-b7f4-e50fe9405994 | -12.66782 | -54.68133 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9ff9281e-d2ce-3ca2-ac6c-c0c40840c6de | -15.76531 | -52.25331 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 186710b0-c448-38c5-8468-410b91610f3f | -18.08739 | -42.9376 | 2025-09-14 04:42:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 494b1a2a-ea70-3347-a2aa-dcbe956fbc74 | -12.70387 | -54.69234 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 4cf9365d-31ab-38b8-a4d0-d6b8384502c2 | -17.42134 | -49.23999 | 2025-09-14 04:42:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 508fa834-5b3d-3954-843d-427a415e2e35 | -15.67146 | -49.9015 | 2025-09-14 04:42:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 487edbcc-e43f-373b-b061-749acce828d4 | -14.63206 | -52.03761 | 2025-09-14 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff04c2ec-d652-3b05-9c88-2c582b33b8c1 | -15.55019 | -54.79695 | 2025-09-14 04:42:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0afa1938-e1fa-34eb-9e2b-ae853c4cdf7e | -15.17883 | -52.32346 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f5230b2-5165-39bf-9d99-df4c19cec061 | -17.36872 | -52.91213 | 2025-09-14 04:42:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f6bc73d3-d7b1-3395-8444-1eb1a5c16056 | -15.20359 | -52.4869 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d82c764c-af58-311b-90cb-cd8d40e55d03 | -15.1319 | -52.48905 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dff4f08e-5182-3ea6-939a-e79a2cff6563 | -19.09476 | -44.49383 | 2025-09-14 04:42:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 077cdee1-660f-3a91-b690-928bf775e4ce | -12.941 | -54.73557 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1a79ce82-1075-3fdb-a1ac-01738901dd71 | -12.68462 | -54.71627 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6764b675-cac7-3572-a0bb-d5eef0a3a0cf | -16.65984 | -49.77998 | 2025-09-14 04:42:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e320e7f0-efa3-382b-9de9-30dfaf8e7453 | -15.77939 | -53.48469 | 2025-09-14 04:42:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d8afb358-1112-3cfe-9872-f83683bebddb | -18.35723 | -45.02542 | 2025-09-14 04:42:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec014435-28f4-3616-8365-b378d7694a3a | -17.29969 | -46.10978 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cccecc9a-45b9-32fd-a9a4-6ebed3226f47 | -13.91593 | -48.30807 | 2025-09-14 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61f205e4-22df-3a62-8b7f-5acbdc157032 | -14.174 | -46.15734 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9d4fda76-eca4-3866-bb62-0895b204e30c | -15.60344 | -54.77954 | 2025-09-14 04:42:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 36f9847b-a930-36e5-b26a-2618a8639a49 | -19.72121 | -45.43343 | 2025-09-14 04:42:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5c5e071-7212-3982-964a-d63dfad33905 | -14.43701 | -43.2125 | 2025-09-14 04:42:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 63fb2562-5920-3a71-a325-b81bcde12ad0 | -16.25176 | -56.63132 | 2025-09-14 04:42:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c413fc11-07b3-3eb7-a0a5-c379f6b5adfa | -20.14343 | -45.64571 | 2025-09-14 04:42:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 939f88fa-2794-369a-b241-075823c28999 | -17.30818 | -46.11073 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5320b1e4-3e06-3df7-b865-c8d6be60e306 | -14.83666 | -48.33291 | 2025-09-14 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 413e726a-b513-3d7b-9801-eba2c6cc7d07 | -17.14908 | -48.50697 | 2025-09-14 04:42:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 590cd660-be18-3c1e-8738-8fc15927c98b | -18.95717 | -46.31094 | 2025-09-14 04:42:00 | NOAA-21 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ce889634-bbcd-3b3b-94b0-06a1ea4feb7e | -17.7928 | -51.72883 | 2025-09-14 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8efe7a79-94e2-3956-ab32-3ad24a818494 | -15.12915 | -52.48495 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| dc3197ed-cc80-309d-a179-fd2bb7ec0373 | -17.29403 | -46.12071 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0b5a799f-005b-3158-abc1-c6e6a3a44cb4 | -14.84445 | -48.32964 | 2025-09-14 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8fb0a70-bd7c-3c78-92fa-6338125771e1 | -15.6872 | -52.25146 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30c365a2-f7f9-3f42-bb9b-cb9e342052b9 | -12.45096 | -57.78811 | 2025-09-14 04:42:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 77e4941d-3929-398a-a093-8ac79e5ec822 | -18.29684 | -52.09862 | 2025-09-14 04:42:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a021c1f1-e2ea-3bd9-a171-d0e2b12eebff | -15.20027 | -52.48632 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28455051-69a4-37bd-a873-9eb7d96a5f53 | -16.10596 | -49.94815 | 2025-09-14 04:42:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac4adf20-2da6-3423-81c8-fec1a7f0f0dc | -16.54628 | -49.21809 | 2025-09-14 04:42:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 178ea564-ce01-3987-b692-e3b41b08556b | -16.30481 | -52.92419 | 2025-09-14 04:42:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d04a662c-bbad-3d7f-976f-624aaaabb579 | -12.94025 | -54.74001 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 957c475b-1b24-31d3-a61e-17f9d5a0ce19 | -14.48142 | -47.34575 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2bfd387f-5826-3d3c-a269-3e7a5d2bffd1 | -18.00086 | -46.96119 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4cd3983f-1562-3b8f-834b-f55067df15f3 | -14.75154 | -45.25837 | 2025-09-14 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a18c20db-24f9-3bd8-92d6-ce4823a5fd72 | -12.9476 | -54.74136 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 86185521-7e38-3e30-8542-9678273150b1 | -20.14009 | -45.64617 | 2025-09-14 04:42:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ac0bca7-d846-3b03-973a-e7daacb20a4c | -18.61354 | -50.40082 | 2025-09-14 04:42:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 4d1d14f4-1b9a-3105-b775-21290001b2cb | -15.68816 | -54.3455 | 2025-09-14 04:42:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45c29bd6-7e55-3e87-80b3-1a5588351ecc | -14.19683 | -46.17156 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 82965f6b-ae4e-3b5c-b3e3-fc0efdc417c8 | -18.26354 | -49.46588 | 2025-09-14 04:42:00 | NOAA-21 | PANAMÁ | GOIÁS | Brasil | 5216007 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5aae50dc-a230-3335-a6af-424e6d48956b | -17.44611 | -49.24397 | 2025-09-14 04:42:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3cf03e16-84b4-344b-aa3d-181ebe64f1dc | -16.99028 | -45.85963 | 2025-09-14 04:42:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f050ea7c-bec6-316a-b573-ecaac39c4891 | -14.16994 | -46.15696 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bf064919-c6a9-3a86-b5db-2bfffe5ebcca | -12.66999 | -54.69082 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| ca62065a-46e7-3234-9a94-2b98fce85581 | -16.50118 | -55.16057 | 2025-09-14 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 39f5f332-38c3-3383-a196-967bcc9b5295 | -13.88502 | -48.295 | 2025-09-14 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25128941-5729-3ca0-9935-5e404fca7eda | -14.27448 | -53.00946 | 2025-09-14 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f68911cf-d165-3756-b45e-663b870ab95e | -17.29102 | -46.11046 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a9a6ad9-35dc-3fac-83bf-ced78752521d | -14.61824 | -52.03896 | 2025-09-14 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 97d9d246-c8c8-37ca-be5a-f63b21470111 | -18.06485 | -50.73183 | 2025-09-14 04:42:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f7aaeda-81ed-3f96-894e-76174f13e479 | -14.41038 | -46.4024 | 2025-09-14 04:42:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9d1d329-1019-3dfa-9e16-f179bd3f640b | -17.44731 | -49.2354 | 2025-09-14 04:42:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4d212c7-975f-3de1-8a7c-11b3f659ddfc | -12.69718 | -54.70941 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4ced23c3-4efb-3dbf-8249-4738e7e50402 | -15.1797 | -52.46764 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfb6e6cb-6c87-3921-9812-c6d277c641c4 | -15.28119 | -56.02405 | 2025-09-14 04:42:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe9d393e-add8-38d3-9584-d1bb2d24c138 | -17.43901 | -49.21714 | 2025-09-14 04:42:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0cccd85d-7f45-3f88-93b8-aa257c135b6a | -15.68229 | -52.23961 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a5cfd5ec-619c-3d21-b1e6-fa7bfc9a8a11 | -17.41133 | -49.25993 | 2025-09-14 04:42:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5153900c-bfe7-32ec-ad8e-f2a45820b661 | -12.68321 | -54.70226 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| fd920a17-8880-3318-a546-85d28188e00d | -16.87013 | -49.35897 | 2025-09-14 04:42:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73d44dd9-4cd2-3d51-9e02-bdc95be05cad | -15.65206 | -47.04462 | 2025-09-14 04:42:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ddc6c1f-91f4-33d3-a004-7a737da550b0 | -18.01204 | -46.97031 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3ed08bc3-e1eb-313a-a26f-fad12ff79b78 | -15.78368 | -52.22332 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9704d5e9-3c24-35de-8d58-62dd4fd9d8f6 | -16.65584 | -49.78329 | 2025-09-14 04:42:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bb06245b-214b-3d6a-8161-669de0338e1e | -15.57789 | -54.73596 | 2025-09-14 04:42:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9ce6cabf-19c5-3db0-97a2-01987a4b8e30 | -17.26199 | -49.26865 | 2025-09-14 04:42:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 17309c11-beb2-3340-beb8-c309cfa9d625 | -16.36825 | -51.77175 | 2025-09-14 04:42:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ceb536c7-a667-3bf7-be42-9927dff8d343 | -15.77889 | -53.48136 | 2025-09-14 04:42:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 45b353f4-d6f6-3cba-87ac-bb70a5ef76dc | -14.19422 | -46.16022 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 714c5e83-fe62-3c95-9e84-a890ec4f7f7c | -16.18893 | -43.13171 | 2025-09-14 04:42:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad42ff18-c36e-36f5-bd71-d33d17fef605 | -17.32055 | -46.0806 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9968613e-a7c3-32c9-b040-d592799bbcbd | -17.08816 | -49.57571 | 2025-09-14 04:42:00 | NOAA-21 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f300c96d-b99a-3da9-a915-d8bb0be37df0 | -18.14646 | -49.19633 | 2025-09-14 04:42:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 927db19e-a783-3ede-959d-6c42e0dc4b6d | -15.65342 | -47.03417 | 2025-09-14 04:42:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48de1dcd-f426-3f20-b33f-6ddb7300a54c | -14.39713 | -47.34056 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f5d3528-8ff6-3836-abe7-6e729f45cba0 | -12.69283 | -54.69033 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 0a2662cf-3c62-36f8-8f93-82e3ced3737e | -15.16973 | -52.46598 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f4f130f-d67a-3f30-96e6-5247744788d5 | -12.67367 | -54.69149 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README50.md)
