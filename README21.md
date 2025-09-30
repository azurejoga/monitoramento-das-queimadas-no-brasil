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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a503218a-85d6-3ea9-b91a-1f1f05b67e95 | -18.46585 | -40.57024 | 2025-09-30 03:30:00 | NPP-375D | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 38ef3631-b546-3374-ad39-4210fc58bc9b | -20.62077 | -46.17952 | 2025-09-30 03:30:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80971eac-691d-3407-a514-849c0fe2aa75 | -15.37871 | -47.08018 | 2025-09-30 03:30:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a00f4fb9-52ec-3557-9f86-8b48459db227 | -16.41307 | -43.12296 | 2025-09-30 03:30:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfc3396f-c843-329a-b506-04da79e1bf60 | -19.60494 | -43.83823 | 2025-09-30 03:30:00 | NPP-375D | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29f5e5cc-d6dc-3aa0-9494-a4a6c9e99d46 | -18.48196 | -44.02254 | 2025-09-30 03:30:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 26870e88-6d00-3749-af09-b9714b955dd5 | -17.41684 | -47.13344 | 2025-09-30 03:30:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 990254bd-5f62-3366-ae50-42b06de0f83a | -17.3901 | -47.13292 | 2025-09-30 03:30:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dfac0ee8-d01a-3920-b350-d2c8ec14e356 | -15.85831 | -46.24415 | 2025-09-30 03:30:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47c57e70-63c7-3175-8a21-21ed044f8309 | -19.55783 | -44.9558 | 2025-09-30 03:30:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e4553be-899d-3bcc-a5a3-ab69e7f36d12 | -15.86091 | -46.23281 | 2025-09-30 03:30:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 65c9c4a6-cc9c-3d83-abb7-23118f6290ed | -20.6194 | -46.1853 | 2025-09-30 03:30:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06355ecc-9ac2-3809-8005-121d2ac26dfe | -15.8519 | -46.23932 | 2025-09-30 03:30:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d549ef1c-f41d-3c12-b1ef-abd25a2384d2 | -19.86195 | -44.5644 | 2025-09-30 03:30:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| d1409f53-a1f9-3c86-bc0a-089593894cfb | -18.7745 | -39.76803 | 2025-09-30 03:30:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7bcbd2cc-45e2-31f1-ba55-69a9c39417f5 | -21.04408 | -45.68811 | 2025-09-30 03:30:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cb8dacff-e606-35dc-a000-349d30f31dd9 | -22.02318 | -42.20876 | 2025-09-30 03:30:00 | NPP-375D | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2e45b93d-0906-3a62-ba8f-03cab1289e74 | -16.7278 | -43.11524 | 2025-09-30 03:30:00 | NPP-375D | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d6ecf9e1-4ccf-3bc4-8d78-a6a3c6bc28e1 | -16.38565 | -47.03847 | 2025-09-30 03:30:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dfe9f5fb-3422-37a1-aea5-87442373f9ab | -19.22715 | -45.82065 | 2025-09-30 03:30:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| adbc91b7-ee15-3820-a7bc-f366a3db61a1 | -18.30603 | -42.89087 | 2025-09-30 03:30:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7d633ea6-b545-3978-9b19-90e6f91bd400 | -18.47079 | -43.80109 | 2025-09-30 03:30:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7817c3ca-b589-3ea3-a7b3-89e4f183ac5d | -19.3071 | -43.8116 | 2025-09-30 03:30:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ebf9bb49-9e10-3677-890a-d269ca44479e | -17.7151 | -46.65835 | 2025-09-30 03:30:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 69d7c32c-2438-3ae2-bd0c-dc2224bf2991 | -19.30631 | -43.81516 | 2025-09-30 03:30:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f6f151fc-332f-3c66-b148-4ef7a78f1575 | -18.12155 | -47.79062 | 2025-09-30 03:30:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 477b8f3c-c43d-3b41-b997-0da701f92862 | -20.61977 | -46.19627 | 2025-09-30 03:30:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a613bb1e-d61d-357d-ae42-56f470314710 | -19.85447 | -43.81967 | 2025-09-30 03:30:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 314e8147-8b9f-36ff-bcb4-f55587179d8e | -21.40848 | -43.89811 | 2025-09-30 03:30:00 | NPP-375D | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ec17ba6f-5998-37ea-99b3-8f0b02bac542 | -19.85072 | -43.81039 | 2025-09-30 03:30:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 5351ffe8-44f4-37dc-a4c2-f3247dae72e7 | -19.59561 | -45.88756 | 2025-09-30 03:30:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d845b34c-d706-3145-9ba3-e70277d64cd6 | -19.85413 | -42.58938 | 2025-09-30 03:30:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7088d2a8-b05c-38c4-92c6-934ba28ea4d2 | -17.39454 | -47.14535 | 2025-09-30 03:30:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8f8b9c9a-9ee6-3bb0-87aa-8068eecc9bb5 | -18.02022 | -44.37191 | 2025-09-30 03:30:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f1a635c-194b-34e3-8282-582056e724f8 | -20.39762 | -43.68173 | 2025-09-30 03:30:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 40f32077-356e-3cde-bad9-ca63210a2542 | -17.17282 | -42.83519 | 2025-09-30 03:30:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 884c2f42-285e-34bb-856c-dbe74e620c0a | -18.0193 | -44.37605 | 2025-09-30 03:30:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea14f47f-715d-3173-973c-968a9de2c57f | -16.73339 | -43.11634 | 2025-09-30 03:30:00 | NPP-375D | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64bc15f6-8c57-3605-91d8-e27e2b205852 | -19.86923 | -42.59332 | 2025-09-30 03:30:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| dd441c5b-c863-3432-a414-fdcfe2816e67 | -23.2315 | -46.7872 | 2025-09-30 03:32:00 | NPP-375D | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ac1a78b7-5ce1-3ff8-bff4-69cddbf337b9 | -22.84753 | -45.45025 | 2025-09-30 03:32:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4d63aa12-e560-389a-b4c5-394909cc2e43 | -22.5149 | -44.61275 | 2025-09-30 03:32:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 3495fec1-0b45-355f-88cc-8bff8c7a2b38 | -23.15638 | -45.73149 | 2025-09-30 03:32:00 | NPP-375D | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 794cf628-e2c8-3399-b266-cf1ff9050f61 | -22.1669 | -46.7457 | 2025-09-30 03:32:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2940fcb9-c8c2-301d-85db-3ccb13a09746 | -23.32803 | -46.86343 | 2025-09-30 03:32:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a5f6d9df-6c80-36dc-b915-2dde134d36b3 | -22.84849 | -45.44614 | 2025-09-30 03:32:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 32dbf8ba-fc0f-392e-8e1b-bc34b13299dd | -22.51154 | -44.6002 | 2025-09-30 03:32:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 105195b9-14c0-315d-a7ed-b73813fcb848 | -23.2328 | -46.78184 | 2025-09-30 03:32:00 | NPP-375D | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b3e24188-d193-3ded-b005-14fe44875d42 | -22.51759 | -44.60057 | 2025-09-30 03:32:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 00718918-cdba-3af8-a885-1394287c5ef5 | -22.51988 | -44.61395 | 2025-09-30 03:32:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 3bd107ed-e86f-3296-a70c-26e95286d332 | -22.51582 | -44.60858 | 2025-09-30 03:32:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| d376656c-37d0-32a7-9526-84bed163b74c | -22.51244 | -44.59629 | 2025-09-30 03:32:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b88baf54-6072-30b1-8f9d-f79cb7736d89 | -22.51524 | -44.60912 | 2025-09-30 03:32:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 8bb33d53-fe12-316f-aecc-e63d854f224d | -22.06339 | -45.64647 | 2025-09-30 03:32:00 | NPP-375D | CAREAÇU | MINAS GERAIS | Brasil | 3113602 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 85d511bc-48c3-335e-82da-c079913760b9 | -22.51708 | -44.60106 | 2025-09-30 03:32:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e937d9fb-1115-3d8c-8072-51adafcd47e6 | -22.84699 | -45.44763 | 2025-09-30 03:32:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4d3e8222-e0f4-3d53-b695-21d8e20c04d6 | -22.17432 | -46.74211 | 2025-09-30 03:32:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 455bcd0e-8f1c-3fef-95c8-ab80a4dc27af | -23.3269 | -46.86808 | 2025-09-30 03:32:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 257f9446-cfbd-3d4b-872f-72ba329626f7 | -22.52084 | -44.60973 | 2025-09-30 03:32:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 24724303-e07a-32e2-9198-ef6422a4aa60 | -22.51293 | -44.59576 | 2025-09-30 03:32:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6e6ff0b2-e0fa-3ba8-9b63-b703b2013632 | -22.17304 | -46.74746 | 2025-09-30 03:32:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| e214c624-8f42-32da-993a-fadb9e3e7325 | -22.51673 | -44.60446 | 2025-09-30 03:32:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| be0d88e7-4afd-3820-af04-35e2a053cc85 | -22.06448 | -45.64186 | 2025-09-30 03:32:00 | NPP-375D | CAREAÇU | MINAS GERAIS | Brasil | 3113602 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 304f5739-58db-32fc-9b77-463872b8d75e | -22.16818 | -46.74035 | 2025-09-30 03:32:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 74e40185-2306-3d7f-afcc-4ae02309fe59 | -22.51794 | -44.59729 | 2025-09-30 03:32:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f020d1a6-9eb3-34c7-ae22-b0d5a8ee76dc | -22.51329 | -44.59254 | 2025-09-30 03:32:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4662ed24-2d36-321f-b426-587d5e748027 | -23.1574 | -45.72713 | 2025-09-30 03:32:00 | NPP-375D | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| edebfd85-c2dd-3979-ae36-0759f4827d41 | -22.51619 | -44.60498 | 2025-09-30 03:32:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 2588dc9f-cada-3b47-81d2-325859e2c077 | -23.15537 | -45.73579 | 2025-09-30 03:32:00 | NPP-375D | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| eb616c7a-8e52-3939-a2ba-42043a255fe3 | -22.52176 | -44.60571 | 2025-09-30 03:32:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| adb77121-7f86-34d8-8c0b-5af7867f6bbd | -22.5143 | -44.61326 | 2025-09-30 03:32:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 469f9043-4380-36f8-9d57-02559d6ef4cd | -23.14969 | -45.73417 | 2025-09-30 03:32:00 | NPP-375D | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c564fbee-dfb7-3e97-a770-d78d0d3976f2 | -22.51206 | -44.59967 | 2025-09-30 03:32:00 | NPP-375D | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3a83a3e4-db52-3c96-98f1-23d0738e1ed9 | -11.7519 | -44.7461 | 2025-09-30 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 43.0 |
| c50fa945-9676-371e-920f-bd40fa4b844e | -13.7511 | -54.7286 | 2025-09-30 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 6c643c68-42e4-327c-bfc2-3803c286cc37 | -11.1543 | -54.1465 | 2025-09-30 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 8ee2ca2e-e731-33cd-a19c-180fce5a0088 | -11.1546 | -54.126 | 2025-09-30 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 205.7 |
| 5ba42ebd-64a4-3148-9892-2146a5c43088 | -10.1851 | -44.8939 | 2025-09-30 03:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 235.9 |
| 960e7015-e7da-36f3-80d9-e2839164d96f | -11.2707 | -47.2236 | 2025-09-30 03:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 53297b2d-6dd9-317d-973e-e7130cca24e5 | -10.1855 | -44.8709 | 2025-09-30 03:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 67.1 |
| df45669d-6f4b-3d3d-9bc4-6bf1c5103cf8 | -13.2161 | -50.9286 | 2025-09-30 03:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 43fea15b-3a98-3e3e-bb19-b1a8f9ac3ea0 | -5.5241 | -43.8878 | 2025-09-30 03:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| ea357c3e-555d-3e75-ac2a-0fa64a78c3c6 | -10.2041 | -44.8915 | 2025-09-30 03:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 5fa4619d-bee6-31aa-94ee-b7ad4f0abb1e | -12.8429 | -47.0063 | 2025-09-30 03:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| b8b23dc3-9a45-37bc-a98d-f995687e8f79 | -4.9102 | -43.4666 | 2025-09-30 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| a1406eb8-6e5f-3be1-994d-e91672208f9b | -4.8915 | -43.4678 | 2025-09-30 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 69ed00d2-d051-3869-b212-5cb0485f3aea | -11.2516 | -47.226 | 2025-09-30 03:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 131.6 |
| c571a6c7-ac57-3d77-ae2d-771aa2dfa4ae | -22.5205 | -44.597 | 2025-09-30 03:40:00 | GOES-19 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 66.5 |
| 158cc874-e4a8-3e17-82b6-9091fef6d67c | -13.2158 | -50.95 | 2025-09-30 03:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 157.3 |
| f22cf763-83bf-3114-89dd-402dadaf1f7a | -11.1548 | -54.1054 | 2025-09-30 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 29916fd6-96a0-340f-ae52-d429ab3e38ed | -11.1735 | -54.1242 | 2025-09-30 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| aacf4105-91ba-3242-9eb5-4a573bb122b8 | -11.2513 | -47.2484 | 2025-09-30 03:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 48.6 |
| f2125fba-a8b4-33f0-a012-6b46adf4339f | -14.5137 | -48.4522 | 2025-09-30 03:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 685355d6-4ffa-3b56-8e5a-6633b06e52f0 | -13.4005 | -48.0657 | 2025-09-30 03:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 73.3 |
| e73075fe-f3f5-36c6-8ca8-eadcc844a029 | -13.2154 | -50.9715 | 2025-09-30 03:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 3e6b2b7a-7de2-3fdf-a0ec-c5a89d4564ad | -10.1847 | -44.917 | 2025-09-30 03:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| e1dd25ec-8b5f-34dd-ab62-27c8225c8a46 | -6.46174 | -35.08627 | 2025-09-30 03:47:00 | NOAA-20 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4d60fe79-2625-3fc5-baeb-81882321c538 | -11.23625 | -39.4117 | 2025-09-30 03:47:00 | NOAA-20 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7caffcd6-0208-3baa-abe6-974c40665b24 | -10.18443 | -44.88143 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd40f474-874a-3251-aaf9-b4552f85d0fb | -4.97568 | -43.21533 | 2025-09-30 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README22.md)
