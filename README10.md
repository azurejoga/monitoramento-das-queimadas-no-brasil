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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 514731d1-e6a9-3b47-9f09-518abadf0da5 | -4.47906 | -48.3088 | 2025-06-29 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef425cf1-ef38-3b35-b34f-6315d57b8bda | -4.54627 | -48.02191 | 2025-06-29 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ab14e793-56de-34f9-8b96-0bbc88b1d908 | -4.554 | -48.00385 | 2025-06-29 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9915c87-6991-3fbe-a4c1-71ffcfeaa309 | -5.08917 | -48.35498 | 2025-06-29 04:08:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b9fd61cd-fa54-3ae8-a7cb-cddda60d0a4c | -3.42192 | -43.16441 | 2025-06-29 04:08:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acce2d67-a5d4-3da6-b39a-82672af3f54f | -5.78117 | -43.62537 | 2025-06-29 04:08:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f45c31c1-9f18-31fe-b437-7fb5d636b9ff | -5.57321 | -45.22157 | 2025-06-29 04:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c89115c1-c0a4-3bd3-8e0c-b379e2cdbaa1 | -3.42055 | -47.60784 | 2025-06-29 04:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21866fe9-dc69-3727-a6f4-b6a64e8abd11 | -5.57469 | -45.2125 | 2025-06-29 04:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c03dfe2-c598-3d52-a8d1-c91a616ff399 | -6.38373 | -43.26993 | 2025-06-29 04:08:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 827d3437-3330-38af-8f92-6df363e19de2 | -4.17567 | -42.03049 | 2025-06-29 04:08:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a6fcd7c3-026d-3786-8bff-6292ca1c3593 | -5.57395 | -45.21704 | 2025-06-29 04:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86aa58a4-0b2a-3083-8828-d0eae61b0c71 | -4.5578 | -48.00931 | 2025-06-29 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b11cb8d-11fb-3001-96ac-77e335e20a2a | -5.57092 | -45.21189 | 2025-06-29 04:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7fdbbf0e-d99f-3ac4-aff4-fd05cc6a35cd | -4.45557 | -48.99615 | 2025-06-29 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 16604d39-9cb2-3089-9c5b-8a7199d659a3 | -5.08656 | -48.35781 | 2025-06-29 04:08:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e472f88b-0393-365c-bdef-1196f16fed6d | -4.17232 | -42.02997 | 2025-06-29 04:08:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3695fb3d-949d-3d73-8766-90dcc81e3e77 | -3.77967 | -41.67711 | 2025-06-29 04:08:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0a0acc5f-fd5d-3e7f-8d17-98d75307173e | -5.08736 | -48.35294 | 2025-06-29 04:08:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 491b0adb-3f9f-3165-9339-527dc5e82b2f | -3.77578 | -41.68008 | 2025-06-29 04:08:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ee3d3d35-95d4-3f41-a2fb-7b3386ecca9e | -5.08453 | -48.35415 | 2025-06-29 04:08:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ab04558d-bc8c-3b4f-b5d9-338ecefb3a61 | -5.7497 | -46.25976 | 2025-06-29 04:08:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 835facbb-71a2-3650-9241-1e5161078939 | -5.1612 | -46.0966 | 2025-06-29 04:08:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdf9467e-be8d-36ae-889f-75bd6e7eb717 | -5.19057 | -47.73679 | 2025-06-29 04:08:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7468199-04d2-37fb-9e83-0e7df64477c3 | -5.57018 | -45.21643 | 2025-06-29 04:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9162fad9-d517-333f-bc4a-d2f83ced9729 | -5.55215 | -46.29531 | 2025-06-29 04:08:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5a4c352-a950-361e-81b3-db49f3b6210c | -3.77912 | -41.6806 | 2025-06-29 04:08:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| faf46a85-bce7-3df4-ab66-6170534cbfac | -2.54868 | -47.70107 | 2025-06-29 04:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59c5bc37-6f4e-33eb-8bd8-4c6cc0b56f9f | -3.62726 | -47.5498 | 2025-06-29 04:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbc06203-a0a8-3696-b35f-069816097a2f | -4.38148 | -41.91504 | 2025-06-29 04:08:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 45163f7a-6911-34b0-a227-f9b9819952a7 | -4.38482 | -41.91556 | 2025-06-29 04:08:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1cde5458-ff72-32e1-95e7-ce5e5d003089 | -4.42226 | -47.66659 | 2025-06-29 04:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d0a3fdd-0441-3f83-ba8f-64f0a55dbf65 | -5.06193 | -43.25322 | 2025-06-29 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26033658-8d7b-35c7-b621-e0588091fe6f | -5.74868 | -46.25703 | 2025-06-29 04:08:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e352cd5c-519c-35eb-b2fc-45e8bc02ef86 | -4.55858 | -48.00461 | 2025-06-29 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b3354de-fd4f-3c9d-936b-80694ba4075c | -4.32175 | -48.07664 | 2025-06-29 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b1f3f334-03a9-3c36-b56b-e321205f4190 | -5.7457 | -46.25914 | 2025-06-29 04:08:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae3b9691-8424-34b2-89dd-637cf43a10ca | -3.62801 | -47.54531 | 2025-06-29 04:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 360fa649-c79b-38d0-97b2-1a69c904d5e0 | -4.17175 | -42.0335 | 2025-06-29 04:08:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 275510c3-f480-389b-8aa7-7cde522f467d | -4.81592 | -47.32254 | 2025-06-29 04:08:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f99952f8-7ec4-3bd2-b4a0-021057e8230c | -11.5502 | -52.7659 | 2025-06-29 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 5ce36a59-b24d-3dc4-a352-ad62b2a01f8a | -11.5499 | -52.7867 | 2025-06-29 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 167.8 |
| 9457c6eb-0d8a-3b75-9962-82c376a83995 | -11.5312 | -52.7678 | 2025-06-29 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| b05eb906-d932-3a0d-a511-8ee13d69bd6f | -11.0356 | -56.2644 | 2025-06-29 04:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| d3eb85e3-6b2f-3cc4-af62-4569c3e4b23a | -10.5579 | -52.0289 | 2025-06-29 04:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| d937611b-754d-3d6a-bf1c-13977a5dc35d | -11.5309 | -52.7887 | 2025-06-29 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 8d2f3811-1e60-3e0b-aa5c-6d5e47af728f | -10.5576 | -52.0499 | 2025-06-29 04:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 137d134f-fe25-3ebc-ae5d-df9e4edbfd22 | -10.9811 | -45.1104 | 2025-06-29 04:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 9d20a41a-709f-3423-a748-062779010339 | -7.55409 | -45.83635 | 2025-06-29 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34284bbe-cc3e-362d-9db6-9dfeb5fcda26 | -9.27683 | -40.44574 | 2025-06-29 04:10:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 49590ac2-a8aa-3011-9201-a3eea01df0f5 | -10.85361 | -53.75989 | 2025-06-29 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c91f8437-42e9-3978-9761-93c13c7853a5 | -6.90548 | -43.99263 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 882506a3-4aaf-3ee6-bce4-1a89a931b6eb | -7.26096 | -43.14013 | 2025-06-29 04:10:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 656923c9-9148-3fa6-a7c5-1c5294ecd6e3 | -9.4387 | -47.95134 | 2025-06-29 04:10:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b8c8db7-9434-36d1-81e1-1c8056d212e6 | -11.26195 | -52.74792 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 363759a8-d13d-3982-8ef9-9227f60c4498 | -6.81378 | -42.85534 | 2025-06-29 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c658eb99-e050-362d-a4e1-f5313d531c25 | -7.18675 | -43.428 | 2025-06-29 04:10:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3370d279-1e96-3537-9637-227b217d55d7 | -8.85818 | -47.95445 | 2025-06-29 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 831bf6b2-204b-3fd6-bbb9-fc2959a68123 | -11.02496 | -56.26178 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e056b718-d8b4-3838-a391-78bb4b02b00d | -7.1892 | -43.43159 | 2025-06-29 04:10:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0b72c441-a829-3043-bedf-904a628aa1e9 | -11.545 | -52.77525 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 4ed4ca64-9872-3a43-a888-38779120a279 | -11.01583 | -56.22911 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8cb8a48f-4a80-35a6-8133-ca42611eb3b1 | -11.82372 | -47.51022 | 2025-06-29 04:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 555584e5-3e1d-3d58-bb69-5398dd5356c3 | -10.62189 | -51.7974 | 2025-06-29 04:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a24de76-b73f-3b3c-9982-bbdcb113c8e2 | -13.27654 | -48.42789 | 2025-06-29 04:10:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebba8ca1-4d19-3665-8517-6eeeb20b52fb | -10.54869 | -52.03281 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7c94f415-26b7-3cd3-992e-66ffa2588fd5 | -11.04157 | -55.37571 | 2025-06-29 04:10:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0413aa1c-77dc-3e44-8fcd-c4b2c38ad479 | -10.56247 | -52.04325 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7fa81086-b925-39f6-8693-165c971bb73a | -12.12645 | -45.57437 | 2025-06-29 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 552f2954-90af-31f9-943f-1f2737a838d6 | -11.57637 | -52.11044 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7c92349-f3c8-31a6-9521-6d79abd435ee | -10.97914 | -45.10899 | 2025-06-29 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 8da71deb-9af4-36ac-9f0a-495d98287851 | -10.86649 | -53.75048 | 2025-06-29 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f65fb0c-117c-3176-8a7c-4041d087f4cc | -7.19016 | -43.70635 | 2025-06-29 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f48b0075-3863-3775-8c2c-6d5b1c08c772 | -7.40221 | -44.57683 | 2025-06-29 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| afe87691-534d-3cee-b902-8611a0137faa | -10.55275 | -52.0409 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 93ebc756-b057-3a33-baec-f568454be657 | -7.1898 | -43.42791 | 2025-06-29 04:10:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 50d44077-8187-3dec-9133-2f9cf2268485 | -7.55185 | -45.82656 | 2025-06-29 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9c186bc-19a0-37fc-97d4-b832fe6c3203 | -11.03479 | -56.28475 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 71f92362-78ee-3ab0-9372-bc2f39c0be3b | -7.55603 | -45.82972 | 2025-06-29 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8c4cf24-2752-3429-adcf-2cd68736a457 | -10.87421 | -53.74284 | 2025-06-29 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1ac5124-6734-301e-b18d-1154c563c5a2 | -10.55069 | -52.05153 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b477965a-8319-3017-9282-b3f0dacf0589 | -8.08955 | -46.86189 | 2025-06-29 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8d18c55-b8bc-33c9-a603-a94a2033feb0 | -11.02975 | -56.26626 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b9a312bf-2919-35a4-97b1-c15fbe079fcc | -11.01862 | -56.28484 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 147ccf3c-c944-34f2-a2bc-39b0a5052a65 | -12.76585 | -44.40392 | 2025-06-29 04:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d91ce06-c889-37fb-9910-3b76d1ed4af0 | -10.84588 | -53.76012 | 2025-06-29 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9f7fbf8-07ce-39ec-bb87-181643f0dbaf | -11.79036 | -48.29305 | 2025-06-29 04:10:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13a44e69-0231-38b3-97cd-e066e0368f2c | -12.10076 | -54.66609 | 2025-06-29 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80f3b8fc-76d4-3f65-b20c-a63ed78afc83 | -6.90611 | -43.98878 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b17d745e-6633-332f-8891-d838e5bc4b5e | -11.03056 | -56.26989 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b342eeca-3db8-31ea-8339-5a34c586e638 | -10.8674 | -53.7535 | 2025-06-29 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf3e7e68-473d-3c07-838c-44d64a96024a | -10.87335 | -53.7473 | 2025-06-29 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 02e2da35-3362-35f0-98bd-6f1ad0d5ddc1 | -10.55885 | -52.03843 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b83dbf46-0103-3678-a585-3416302eb87f | -10.97782 | -45.11694 | 2025-06-29 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| eddf4af7-8ce9-30ab-8379-42be03ab3ec2 | -12.05647 | -48.47294 | 2025-06-29 04:10:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6cc5ff2-6209-3de3-8538-d23699e483d3 | -7.55679 | -45.84893 | 2025-06-29 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8af69c5-249b-334d-b0a4-51c566da2312 | -11.53866 | -52.778 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 26.3 |
| b4b17569-3420-3374-aec4-20145da38a02 | -11.0292 | -56.27657 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 18d9c26d-379c-3c12-b738-4e6047a45015 | -7.26492 | -43.13705 | 2025-06-29 04:10:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6282ccfe-4d46-3098-a762-ba9bcf0c6835 | -11.59418 | -44.66561 | 2025-06-29 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README11.md)
