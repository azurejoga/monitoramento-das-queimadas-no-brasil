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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 941af107-f7fe-3536-989c-c5b2a98895ee | -14.98383 | -50.76073 | 2025-10-01 04:51:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf18d9f8-632d-368c-8b9c-e5ae6ac28664 | -15.29017 | -46.40641 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 395974d4-9328-326d-9dbc-9fb3b27fd3e7 | -13.97529 | -44.88461 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6a0a8a1e-066b-3647-91c5-9c83352df8a5 | -14.02259 | -46.3199 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 953ccf0f-dc5d-3b53-9df3-25bdd679c329 | -13.29924 | -48.70289 | 2025-10-01 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1fd72830-f739-3d17-b8ee-3826bbf2e20e | -8.75066 | -50.81495 | 2025-10-01 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2293ce4d-925e-3ff9-a4fc-bf5642926c92 | -12.29127 | -55.14433 | 2025-10-01 04:51:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55f27b19-7f15-3772-982c-e84116d7f6fa | -13.06011 | -47.06775 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9349737b-1692-3814-a3ed-06ce9d3330c1 | -11.08198 | -47.83541 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3fa6e637-293e-3b1d-97f4-2339f92a8dba | -14.85399 | -48.33546 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 505ef992-f8de-3562-84a1-bd90a9798f17 | -11.63967 | -47.48672 | 2025-10-01 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 778598cd-fe58-36f9-b6f8-622434ec2743 | -12.23911 | -47.81506 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9a3e0466-fa07-3144-9af9-d6a4985fc9d5 | -11.62573 | -52.2462 | 2025-10-01 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48745db8-60e1-321c-824f-9c229acffab5 | -15.174 | -49.08289 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c8420a16-7016-30fb-b6cd-8a3fb13a39b6 | -12.79619 | -46.89857 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed7b2472-a35e-3090-bf27-7e7ad6b0a0ec | -12.97414 | -48.42287 | 2025-10-01 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e3719a71-f75b-35e0-b4a8-0c0e5096e319 | -15.48762 | -45.90034 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3dd22892-2b29-3719-ba51-8a4502adbc79 | -13.1684 | -47.38639 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33d9352d-7cf6-3b8c-8cd3-5e3282e894e6 | -15.84054 | -46.24574 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb8406b0-7fcf-35f5-8318-bd91894ee4c9 | -13.91653 | -48.08357 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fda251ed-3faa-37f6-815c-14234af40c5a | -14.6051 | -48.32 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aaa7e3f3-b41e-3483-a08f-a16c0f4b0867 | -13.36087 | -47.2857 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15c3c35d-b2a6-36dd-acd3-1aed936214f8 | -14.89785 | -47.21401 | 2025-10-01 04:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc314cb4-0569-3b44-a523-0778c9cc3ac3 | -14.68557 | -45.28769 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6d9c50a-aa5b-3681-a64d-2e695067cf2b | -11.46593 | -45.08991 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4600d54c-446a-3d89-82b3-da387e45bed1 | -10.90866 | -46.55374 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24cdb715-3c33-38a6-a4f6-70495f217404 | -16.06448 | -51.01342 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ddd7a04-4bea-35b6-bd88-eb66095da28d | -14.71417 | -48.13393 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 68a0216f-a3e6-3563-bcb1-e9e03761ce9b | -12.37956 | -50.20204 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4d2ec20e-3a70-3f91-9500-b27fab46340d | -14.41273 | -44.91272 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5814ca6-cf3f-3a92-a43b-9f0d5fbe8ec8 | -14.7123 | -48.26559 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6f04c6d-e04d-3ebf-9d01-73335fa10c6a | -9.93417 | -43.67555 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19e40da8-7c82-310b-9093-af375256e300 | -9.40885 | -54.69717 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1672ac38-3b0a-3e6a-9d83-d7306fca6c40 | -14.73164 | -46.83192 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 11683e8c-e93f-374a-b5f4-fab3160042cf | -13.37258 | -48.11166 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 104a299f-d45c-30d8-8f61-34afec36624e | -16.0851 | -51.04762 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9608bc75-b88c-3a36-8b15-5f98cca74522 | -16.0197 | -50.88028 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b07f10ee-0ec1-303f-937f-6594e3294a72 | -14.70374 | -48.26927 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa9b69b6-242d-3793-a479-edf60b04ae25 | -13.71732 | -48.65453 | 2025-10-01 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ca7749f-b8ad-353d-9a63-2fdcc24c356e | -16.37743 | -47.06311 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fc9aa84d-a160-3692-a9d7-91c8a84d9427 | -13.92231 | -48.08308 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38befa92-01ee-36b7-aec5-961818c42075 | -11.46037 | -44.97061 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f72115a2-d4ad-39f6-931f-4c0c5136481a | -9.51649 | -54.74424 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4db7f1f-b416-3647-90fc-113a1d92b2f8 | -15.49457 | -45.92114 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e238890f-0746-3ac5-9c5a-b00e90f4fa6a | -12.71291 | -54.9738 | 2025-10-01 04:51:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f20875d-9f02-34bd-adf2-db58f13a0815 | -11.76604 | -46.86847 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5345c91e-dac3-3197-ae4f-f08a160b118d | -15.3943 | -44.97593 | 2025-10-01 04:51:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9037c1ad-03c3-34bc-8241-2a24601c362b | -11.33585 | -48.31684 | 2025-10-01 04:51:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d7d315a6-4ca2-3f1e-8bb1-172a4dbabcda | -12.24186 | -47.80304 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b603c60f-1f57-389f-b0ac-538b57880072 | -12.82086 | -56.55202 | 2025-10-01 04:51:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4682380f-5d14-37ac-bdf4-95f258fadc13 | -12.78294 | -46.87072 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8b04f915-4e0b-3613-a553-829a96354945 | -15.16952 | -49.0898 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b681ebcd-2506-3f9e-a72d-8ef55dae53bb | -14.90134 | -48.12731 | 2025-10-01 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e41208dc-fdb4-3196-b3b6-1efeba4f5fc3 | -10.98038 | -46.52898 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8b12bcc-e357-324f-a050-dd01a5991cdc | -15.60805 | -46.91159 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7bbdabb1-fedc-354c-9558-0bda41b0b839 | -12.92414 | -54.72734 | 2025-10-01 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f19daeb5-52c1-31fe-a835-a33c6be51743 | -11.94733 | -47.88314 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57a6cdb9-4046-362c-bcde-0be46457a6e0 | -11.08012 | -47.82072 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f750b9e5-6d49-35ae-9ba0-005f8f197f47 | -9.92294 | -43.68477 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 358fafd5-9aa0-3d5a-b931-86099e3e8d37 | -12.78556 | -46.88277 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e356575f-e1ea-3a1f-8f69-6a0995a908a7 | -15.48028 | -48.55192 | 2025-10-01 04:51:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1840d4ab-dbee-3fda-82c6-1ff2cc071ee6 | -14.89737 | -48.12656 | 2025-10-01 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7e04d636-164a-3fa7-b9a6-5135ce9a5319 | -13.32955 | -47.84262 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| df3e665c-4185-3419-946b-e29b8e6e131e | -10.63538 | -48.52563 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c71b470f-ba62-32a0-8789-99c0efb665c6 | -11.84665 | -48.055 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8f98bcde-be37-3268-8d2a-96cc4d9c00cf | -15.17543 | -46.3992 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 09ed6be9-76d1-3343-8a66-2a59820737a5 | -11.05878 | -47.83213 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8662055b-8639-3b43-86dc-8cd08d028ff4 | -11.78593 | -48.44887 | 2025-10-01 04:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02c86eef-23cd-3858-b7af-1d67fbc8997a | -15.2851 | -46.41022 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5299c09c-d5eb-3855-ba67-67c94b608c30 | -10.90454 | -46.5196 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f396b78a-b4f8-36a7-ad84-11c0b8db9c02 | -13.06635 | -47.08405 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b5e2e46b-dbd7-3bf3-822e-aca209350b3e | -10.21034 | -48.20282 | 2025-10-01 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee28e671-00da-3491-ab5e-ac697c9702df | -13.85505 | -47.95557 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 528392a2-615e-360d-aeef-07ba1536ab6a | -10.03686 | -52.09475 | 2025-10-01 04:51:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90697d19-d522-3456-8e4c-214e9348323a | -11.44633 | -43.50788 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f93bc44-5319-3c86-b237-2f426b30a6be | -11.4256 | -43.50503 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38093f4a-7deb-35e3-ab62-69023c89e432 | -12.90588 | -46.81775 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 936742fc-1402-3dab-aca7-e7ed01bed27a | -16.07723 | -51.04753 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1ee6b3e-31fb-375b-b0bb-2f83d520cb5e | -11.15146 | -54.31309 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ce8dd225-788c-3910-be23-b165f036a181 | -14.75866 | -45.75909 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e35664a4-abb8-3157-a16d-03463ce11dca | -9.45003 | -50.89817 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1cc35146-2d2e-376a-a8d6-f95aa0b6d17a | -9.35517 | -46.33316 | 2025-10-01 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e65c69f4-f83d-3012-b1ba-250ec445cbb1 | -11.91522 | -47.99877 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e283224a-f072-3cbf-ad06-716152bc93e5 | -15.13884 | -48.01602 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30adc5f8-9bfd-381b-a9f2-357bc22abb5a | -12.77819 | -46.87408 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e9875f6-af73-369d-afdf-fde762eff2cd | -12.97351 | -48.42734 | 2025-10-01 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8f392ed1-8c6f-3904-9d7e-769f8a4b241c | -11.19149 | -47.20224 | 2025-10-01 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b2712b2-2a05-38cb-8b24-44aca9ed8d3e | -13.56203 | -48.06522 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce8b4117-d4f1-3fd5-b46c-dc0c5827c9a1 | -15.54144 | -42.66018 | 2025-10-01 04:51:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ccfe59cf-4b9d-35a8-8d81-ce08a53f5841 | -14.84914 | -48.33633 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f12dab3e-2a8c-3624-a737-7d9c57636473 | -11.83932 | -44.97549 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6290d374-9c04-31f0-bc7c-fc20789c10c2 | -8.21935 | -55.20412 | 2025-10-01 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b2491b8-c509-3d13-a30a-5b2b97d74623 | -15.33445 | -46.27735 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c409a043-e372-3996-a131-884c9805dcd9 | -14.55206 | -48.24819 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fbaba588-2636-3707-b971-5eadb1a620eb | -13.23379 | -48.44074 | 2025-10-01 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f82b1f89-3853-35f2-8244-725a7bde4165 | -13.33025 | -47.83753 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4eb6fbbb-5eec-309f-b52c-962b0fe22850 | -11.11759 | -49.78723 | 2025-10-01 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd0e4e99-02fa-3278-8d63-cd435e735bf6 | -15.22633 | -50.08688 | 2025-10-01 04:51:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8eb7c5c1-feb4-3b01-a01b-f80b93cd733c | -15.38093 | -49.19854 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d8107673-8acc-3d42-b91f-0a16155d7cf5 | -9.9503 | -51.37924 | 2025-10-01 04:51:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README91.md)
