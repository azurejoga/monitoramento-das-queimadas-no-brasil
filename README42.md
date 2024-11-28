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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e25edf1-b3c3-3599-9539-e360b6f45eab | -23.40383 | -46.55464 | 2024-11-28 04:04:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8673fbfe-f7a6-3add-8b03-71f7bc3e1a54 | -19.20709 | -45.38145 | 2024-11-28 04:04:00 | NPP-375D | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59354a31-1639-3c83-aef5-fc2226e83433 | -19.62944 | -44.01897 | 2024-11-28 04:04:00 | NPP-375D | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abbc1b45-f173-38d9-9737-4add634fc30b | -16.83675 | -46.12996 | 2024-11-28 04:04:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d13ccdf6-fdaf-39ec-b567-d877d62166df | -22.11994 | -49.60903 | 2024-11-28 04:04:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ea832071-c402-3d7d-a637-2b27822024a3 | -17.09307 | -44.97459 | 2024-11-28 04:04:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc11ace0-8217-3858-b75a-f3736d09d7f8 | -19.52172 | -47.33263 | 2024-11-28 04:04:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31bb5801-3449-3ca8-ade7-0ae64a4a2d32 | -23.37057 | -47.05783 | 2024-11-28 04:04:00 | NPP-375D | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 34315d80-8d7d-3557-bbc5-de79e5e7b9c9 | -18.95244 | -43.70781 | 2024-11-28 04:04:00 | NPP-375D | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7589cd10-6c1d-3cb2-8544-428a45090650 | -19.33619 | -46.32515 | 2024-11-28 04:04:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f51a8908-d2fd-3ec6-84e3-8303f983e3d9 | -19.53059 | -43.91701 | 2024-11-28 04:04:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47d5682f-9ce6-3204-bd6f-c2803fd753e4 | -23.70767 | -50.55508 | 2024-11-28 04:06:00 | NPP-375D | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 23d149f0-426b-3740-a166-9b4ee9287454 | -23.71205 | -50.55569 | 2024-11-28 04:06:00 | NPP-375D | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 5c11bc7f-db60-3829-992f-b182a385c530 | -23.71111 | -50.56031 | 2024-11-28 04:06:00 | NPP-375D | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 676720f4-ed5d-37f9-bc06-616961865978 | -23.46435 | -47.51978 | 2024-11-28 04:06:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7760b945-5316-3ecd-917a-36915ec082e3 | -23.71727 | -50.55212 | 2024-11-28 04:06:00 | NPP-375D | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 638ab248-be01-340a-b83e-a44b58b23dd5 | -23.71637 | -50.55653 | 2024-11-28 04:06:00 | NPP-375D | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 007671ca-7229-3c61-927b-5b485b5239b9 | -23.72159 | -50.55298 | 2024-11-28 04:06:00 | NPP-375D | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a055ac91-503f-3f8f-bcff-7f27362c714f | -23.72067 | -50.55753 | 2024-11-28 04:06:00 | NPP-375D | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 176ff443-bcd0-3fa7-9227-44af110124ed | -5.9788 | -45.3621 | 2024-11-28 04:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 227.4 |
| a66365b2-5ef3-3d41-92f5-c5b2b09404b1 | -3.2939 | -45.5144 | 2024-11-28 04:10:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 0225eda1-5d09-3153-8860-4c415ca6c52e | -3.3837 | -50.1125 | 2024-11-28 04:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 344c4dab-2279-3807-a47d-d5f2578d3877 | -1.5897 | -52.271 | 2024-11-28 04:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 64134384-2a7c-3e05-854c-f2b178c3b596 | -5.9975 | -45.3607 | 2024-11-28 04:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 38b32587-2ffd-3bb4-98ae-715f5416e2e5 | -5.979 | -45.3395 | 2024-11-28 04:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 7f7ffa74-2ec9-360c-87c1-bfde561d69d2 | -5.9788 | -45.3621 | 2024-11-28 04:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 230.5 |
| 81a57b7e-c908-3ddb-a0ad-0e7051f98bb3 | -5.979 | -45.3395 | 2024-11-28 04:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| c1225b96-4f37-3065-98fc-05be86e62491 | -3.1113 | -53.8242 | 2024-11-28 04:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| e116c243-e2b4-3b70-a02b-fae43e10e389 | -3.3837 | -50.1125 | 2024-11-28 04:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 05b0f11a-6795-31eb-b49f-8bb7e1866059 | -1.5897 | -52.271 | 2024-11-28 04:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 4784f611-df4f-38ce-a65b-1b4c7aeb4bc6 | -3.2939 | -45.5144 | 2024-11-28 04:20:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 160.1 |
| ae6981a3-a9bb-37a1-8046-c5513cd15ba6 | -3.2938 | -45.5368 | 2024-11-28 04:20:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 13666921-c4ea-3a2d-96ae-430a7057d78a | -5.95994 | -43.37584 | 2024-11-28 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6ddd90bd-a362-39b4-800d-04b91a2cbfdb | -1.66934 | -52.43728 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b36fa9b2-030c-3a2f-94a8-e0b3b924c0de | -5.97114 | -45.35776 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d4aab62b-2846-3f6b-9aaf-b885c478e4dd | -1.23097 | -51.80036 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1f6bb12-b51b-30fe-8c45-732786a3f3b8 | -1.19006 | -51.76559 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c6cacd0-69ef-3847-a75f-61d65d90e07f | -2.59414 | -46.26617 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88dfa4c5-f27f-3340-a725-71f9280805aa | -7.22107 | -39.06065 | 2024-11-28 04:23:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6e284f24-c717-3eab-a6d0-c350c2cb7c62 | -1.08615 | -53.38725 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d9dd416-3b7a-3178-af17-efe3fe336f4d | -2.38669 | -47.16835 | 2024-11-28 04:23:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c8c9fd0f-7942-34f4-897a-763d530b1ff9 | -8.12353 | -47.98657 | 2024-11-28 04:23:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 647b7281-b7eb-38f9-9cf7-0a276212533b | -1.08897 | -53.64491 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee6bdb82-7f78-3b69-97ae-12db6a376518 | -2.12597 | -46.39438 | 2024-11-28 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57802530-16f5-3a37-854a-7d1b8217a844 | -2.55477 | -46.41061 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df5118a7-b3d6-31a1-b86f-69ec89575bc2 | -2.59059 | -46.20447 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74c5a872-9fb0-3cfd-8255-1afef1076b42 | -1.66587 | -52.73577 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9aa2885b-0fcb-3257-bc62-6130d148a9e7 | -0.26339 | -51.62464 | 2024-11-28 04:23:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40a904c7-c538-38c2-bcc3-fa98e2181cc7 | -5.75454 | -46.263 | 2024-11-28 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 685a072a-ee17-3cd3-90ed-0ed9d6dd2f11 | -5.97669 | -45.36578 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fa31c2ad-eb29-31c7-805c-09e114c55473 | -6.37068 | -45.69101 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 422ffc1e-d88b-377a-9ea5-624c11fa061c | -2.71734 | -46.23898 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2476e432-3bbd-3244-ad70-e14ef70363c8 | -2.54524 | -46.34076 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a9782c7-1d9e-3f72-920a-d651c67a33eb | -6.124 | -46.59067 | 2024-11-28 04:23:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3af3ad40-9ba8-3577-a8a1-feda1ef197fd | -1.35796 | -54.65656 | 2024-11-28 04:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6564ddc0-9061-349d-b281-73e8dfab83e7 | -2.52051 | -47.40577 | 2024-11-28 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0e44154-3159-3941-b6c8-339a8498402c | -0.23861 | -51.59876 | 2024-11-28 04:23:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a56b8e17-58f4-3dd2-821f-a1be5867871f | -2.69887 | -46.18608 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2eca75b8-fd49-3495-b976-fe291296c17c | 0.98818 | -50.26264 | 2024-11-28 04:23:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ca8ca9e-43ae-36e1-b1f9-fdc6f3f586d4 | -6.36139 | -46.50797 | 2024-11-28 04:23:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb92dd79-93fc-3ffd-86e0-2c6b567f7879 | -1.66272 | -52.72448 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2acc51a-f7af-3ff7-9314-3f4aaee2932b | -1.47404 | -51.54556 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 497927a1-1dca-309b-8d9b-1db90b33e9e5 | -1.36528 | -52.13429 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92a00a95-d55a-34fe-ae9d-e2a925e13feb | -1.28911 | -51.72568 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eaf4bf9d-1c3b-3743-839a-d67a8b487d88 | 0.1731 | -51.22836 | 2024-11-28 04:23:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 033c0926-0daf-39f9-8e4a-c9e56fc95250 | -1.35795 | -54.65714 | 2024-11-28 04:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c7240e8-f80e-38ed-adbb-68b74d9a2b6c | -6.37676 | -45.69551 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8227c5b6-6a8c-3d55-9868-b9a989ba1ed7 | -7.26474 | -48.50287 | 2024-11-28 04:23:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13cc298b-331a-39a7-a7c5-25e8cb298fac | -5.4988 | -47.16605 | 2024-11-28 04:23:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44dd5a72-8b44-36f3-9d2a-0b79a1bcd4d7 | -1.5928 | -52.27032 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3aea0bec-8b43-3683-bea1-6ddde580f80b | -2.14722 | -48.88493 | 2024-11-28 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fac08682-c2db-3a5d-9d1f-96270e5bd3aa | -1.3509 | -51.96171 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11dfa811-a172-3839-a91f-443f7ef898f8 | -1.36683 | -52.12471 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55fc8c37-5f93-3de4-89c3-b153d06306cf | -1.52512 | -47.297 | 2024-11-28 04:23:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b579508-2a1b-3203-841f-3d242dbe531b | -6.09007 | -41.94385 | 2024-11-28 04:23:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3214d22a-1572-3fa5-a7de-3fa404c9d171 | -0.54482 | -49.52407 | 2024-11-28 04:23:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd68cd92-323e-301a-8829-10b331eb749a | -1.7812 | -47.67268 | 2024-11-28 04:23:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5451e3cf-3010-3080-b20f-2db0828f1591 | -1.68652 | -52.48121 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0246e3f5-e3dd-30a9-9362-dd3af15efb25 | -1.37501 | -53.63263 | 2024-11-28 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68550545-68b6-3285-8b4f-9e5ddb0734cd | -6.43953 | -47.0441 | 2024-11-28 04:23:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ffbab58-217e-3263-bbf9-f2696b384c99 | -2.52936 | -47.33121 | 2024-11-28 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba8e9cd2-0b7d-33a5-a3af-fc32ccede321 | -7.82727 | -48.18951 | 2024-11-28 04:23:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| acffa0d6-592c-3dfb-b48c-6a0a324f0202 | -1.29865 | -51.73489 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| feaf6e55-f015-32da-aea5-c9cd89a1f61d | -1.72035 | -52.4816 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 60bfe3e8-9b67-3766-b92f-9fdef10a13d2 | -5.9811 | -45.35933 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| ae301e82-07bb-3472-b11f-1fe6de647a3e | -2.12263 | -46.39385 | 2024-11-28 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de9c3d32-38e7-3679-b8f4-a05c81ac44b1 | -1.03833 | -51.74065 | 2024-11-28 04:23:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0bf441ae-f639-379d-b40f-f0a172bc4b69 | -2.71457 | -46.25642 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05d902d9-cfff-3ce2-8cca-fe0efec644e7 | -6.6029 | -39.19904 | 2024-11-28 04:23:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9833b3f2-2f95-3412-bfe4-d765c797dcd5 | -5.24127 | -46.13608 | 2024-11-28 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6678a8af-8aa4-35dd-b6d5-7e06c6030bc7 | -8.49771 | -43.28555 | 2024-11-28 04:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 125d89ae-5be7-340e-8a89-32b32baf6888 | -2.12393 | -48.53437 | 2024-11-28 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b91e034-f087-31de-b170-777676a1b974 | -1.642 | -52.11018 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 78ef7f42-5a3f-304a-a3f6-94aa9ebfabb9 | -2.59581 | -46.25568 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93e07c4f-8ec3-3d18-9f15-3f56e449562d | -5.20508 | -46.81644 | 2024-11-28 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b2de714-ff9e-3456-8ef1-978d60c5d82d | -7.83158 | -48.18921 | 2024-11-28 04:23:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97d703db-1651-3ad6-a191-a7ed8511ba75 | -6.09998 | -43.96645 | 2024-11-28 04:23:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 014b27c3-b842-38cc-a8b8-32a5fd8766ef | -2.54072 | -46.23959 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f3a8e1e-cc7f-3e4f-b4ec-df37577d9cac | -2.05411 | -47.12159 | 2024-11-28 04:23:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c642f04e-118f-3fa2-9d0f-2652752de33b | -1.30071 | -51.92371 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README43.md)
