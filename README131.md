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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdbbd482-1a69-387e-b19d-fc64a65b506f | -15.23288 | -49.29576 | 2025-10-05 05:16:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df1556cf-4522-33fd-a5a6-0a31924702ea | -11.76204 | -64.93021 | 2025-10-05 05:16:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca299421-2256-3dae-8412-1b2c8bad6c6b | -14.68182 | -48.35759 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| adb81543-53fb-318f-8aec-b2f407a762d0 | -15.37876 | -47.94105 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e0e11a2-951e-370f-aa2b-f1da60550af1 | -14.3224 | -47.69828 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 231d2a16-c949-3e1f-8c4a-6cfee11dc646 | -12.59826 | -48.14677 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| af779186-b7bd-38f5-8380-416015b4adb0 | -13.14938 | -47.975 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97c1b996-77c8-3c32-a12f-274d45f63895 | -12.31521 | -55.13786 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a7967d9-a0a9-3f61-83b1-e0de02792984 | -15.3776 | -47.93707 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a53dd45c-135a-34db-8a5d-a2c8f3dbda89 | -14.58758 | -52.46245 | 2025-10-05 05:16:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 27e3b131-5a3f-3fc2-a6bd-f98c685ae52d | -16.38113 | -52.1633 | 2025-10-05 05:16:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 91086a8f-0eef-399c-8016-c0bd8a8c10c6 | -13.32072 | -47.5671 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e7b3fc0-4ffc-38a2-9863-9816e1e11a7d | -17.84935 | -57.63657 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 12616d91-24a3-30d5-950d-1b2ae3c34aa2 | -16.07206 | -50.9227 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 34b5bce7-4f14-3d02-b36f-53db06da39f1 | -13.57311 | -48.16814 | 2025-10-05 05:16:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8619d34d-6f11-35a2-b748-a833564f17fb | -18.24619 | -53.3582 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 96c247ff-48e9-3616-8682-ca9dc8dec465 | -12.27068 | -49.19122 | 2025-10-05 05:16:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 28960857-b235-3de8-9713-9986b25e299c | -16.91707 | -52.04932 | 2025-10-05 05:16:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cc21b7d-bdec-3e97-b47a-c15e1354fe38 | -15.98333 | -50.90443 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4680c43-1bd0-3728-a0fd-bcd73256f6d6 | -12.98613 | -46.84239 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 165bc5b3-04f7-3a34-b756-ddfa146e1b92 | -13.32118 | -48.10397 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 891a5899-8909-3806-a459-a06495e58b50 | -14.68591 | -48.33996 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c9bfcf5-024f-36d1-94b0-d511fb7940df | -15.2277 | -49.29059 | 2025-10-05 05:16:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 3e40894d-eba8-39bd-b5d6-569ea76b6016 | -12.94974 | -54.73159 | 2025-10-05 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 925fe433-99a2-345d-a191-bcd924a3734e | -17.92538 | -57.60945 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1a985c00-b19e-354e-8c06-2af65dc81ac4 | -13.74018 | -47.96919 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80cb8961-5de6-34fa-a3ba-a33925757895 | -16.38173 | -52.15828 | 2025-10-05 05:16:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2b00bf60-918c-3f14-b27c-151941dc2df9 | -14.62067 | -48.12575 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0e278ab-9a5e-313f-9383-5a9db6efd2c0 | -12.32265 | -55.13895 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f204ba6a-ab9f-3789-98c9-81b58f4521ba | -15.1293 | -45.74607 | 2025-10-05 05:16:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05343910-dadc-338b-a976-976d35753394 | -13.35365 | -47.24314 | 2025-10-05 05:16:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca8d5051-7044-3f93-b525-527a9ce7cf89 | -13.13678 | -47.97861 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 05dd8c9c-3f3b-3327-b923-28c074052af7 | -15.6956 | -46.27797 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24ebf5f6-183a-3cc4-bebc-5cb3c1d105c7 | -12.24658 | -47.85026 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c7cfaa1-76d9-39c9-8bba-75374800213a | -14.33361 | -52.97346 | 2025-10-05 05:16:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0c0bf19-24e0-3d36-898e-ff858c68d2ca | -18.22439 | -53.37093 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f915029e-46e6-3580-91e7-a7e150f83ef8 | -15.58155 | -52.49412 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 53e53b01-5f17-3599-af4b-dbacc41a9ac3 | -14.61179 | -52.5299 | 2025-10-05 05:16:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d4e527e-9132-3afe-aee1-9197de3c51cf | -15.98689 | -50.91818 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1844a770-e150-31eb-aca0-4089a958d8a0 | -17.91717 | -57.61667 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 373cb535-2823-30ce-92cf-f417726d2061 | -15.90984 | -48.83358 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d2f9aee9-6ca3-3d88-8a89-722a057cdd02 | -14.97306 | -49.97374 | 2025-10-05 05:16:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dfd394e2-e7f0-3854-9e34-608d024cea65 | -15.54263 | -46.82918 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fbefdf77-9d61-3096-bbd4-a2cf2366cc3e | -16.0355 | -51.05578 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 779cf617-76fd-308b-91f4-47ffcef4b7b2 | -18.33271 | -45.88047 | 2025-10-05 05:16:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 0ac10bee-ecf3-3e6a-9423-9d9b6d714b72 | -16.91229 | -52.04834 | 2025-10-05 05:16:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1915f769-be88-35b0-8d61-4bb89e1b8342 | -12.3194 | -55.16108 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cb79682-9f1c-3495-99ad-1718015fdcb5 | -13.25268 | -47.23337 | 2025-10-05 05:16:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 848679e7-e793-398a-81d7-d8636594b5e7 | -12.59442 | -48.1496 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 684cf3fc-f3db-350b-b008-155eac1d7c5a | -16.38585 | -52.16334 | 2025-10-05 05:16:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dba55105-bea0-349e-807d-f2fb47231767 | -16.0776 | -50.91996 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c17139a-d892-3c64-94e4-34b82dc5a2a9 | -17.86452 | -57.63084 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 274d975f-a0ca-3dea-8e54-a3c8d626f645 | -12.98526 | -46.84519 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33bee164-d896-3f9e-a11a-77a54ffe707f | -15.52457 | -46.87569 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8c9c7d92-a8e0-319c-b29d-9f7f0177f08d | -12.92498 | -54.72519 | 2025-10-05 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4780217b-902f-3ca0-ad8b-7ba0a7efe439 | -13.0849 | -47.95367 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5de229fa-db18-3760-9e58-2167533db839 | -13.35544 | -47.59196 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0eae9f52-f888-3704-aead-fc7e3172e058 | -14.68942 | -48.30693 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d11f5dd6-a334-340f-ae91-33e8653b5d93 | -13.54854 | -47.23178 | 2025-10-05 05:16:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eb68cac7-17d0-3913-a346-ec51ffed79bc | -16.04334 | -50.94513 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dddf660f-91c0-3be7-b923-59282bc6c817 | -14.68381 | -48.34003 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 065e36bb-c0a1-38ae-8996-05a68b06c9f5 | -12.42846 | -54.50071 | 2025-10-05 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 778c514e-cc92-33df-9827-1986fbfebee8 | -11.39865 | -55.17326 | 2025-10-05 05:16:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8714c1cc-74f8-3f98-be3b-32aa5ba16c25 | -14.87833 | -48.15721 | 2025-10-05 05:16:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a11dd2dd-585d-3c7a-8fa2-b3b49cced98d | -10.05054 | -62.46188 | 2025-10-05 05:16:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd6aa83a-efd4-368c-baa7-668b7c6fab16 | -18.25902 | -53.36573 | 2025-10-05 05:16:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 60567da2-753b-336b-a771-2e31a3708e87 | -14.65917 | -48.34388 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db638725-adf3-3cbd-b4db-01fbe41d93d5 | -14.69161 | -48.27125 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff3e447d-32b9-374e-8cbe-3600a2c7bdd1 | -15.7592 | -46.26439 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecfabe6f-77c7-3ca6-85e2-29de74657ea1 | -15.30297 | -46.31366 | 2025-10-05 05:16:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 15c9e6ac-8233-3f45-b0d0-e540065d2e19 | -13.72857 | -48.07148 | 2025-10-05 05:16:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8927bbcb-b425-344c-be48-70387d65d4ed | -15.19593 | -56.83147 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca9683a3-8627-3e58-8c26-4cd1b892c623 | -14.68799 | -48.30322 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e13bce02-00c3-3609-86e1-a1b75da7e82d | -14.33276 | -47.6618 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 10e43cee-ea11-3895-92b1-725794b75d97 | -16.34559 | -51.47245 | 2025-10-05 05:16:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 69eb6dd6-866a-3637-b7ab-d03f02cbbef6 | -13.35664 | -48.06013 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba261ffd-5e9d-31aa-a288-f1a804c1f390 | -13.27199 | -47.62214 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 47cb7255-3a37-372c-8451-8b0919007667 | -19.0193 | -50.60813 | 2025-10-05 05:16:00 | NPP-375D | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 8e47bba6-5aaf-3f4f-aec1-88c3b6cce86a | -15.71845 | -46.25686 | 2025-10-05 05:16:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5836cb57-2383-3b1b-8e5d-ac5fca162849 | -14.85108 | -60.06789 | 2025-10-05 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 775ebf24-4cd3-3bd3-aca1-594d85edc3f3 | -14.6582 | -48.35249 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e6c93a3-b9a6-3c3e-8ed9-e5bc2ccd429d | -14.65429 | -48.33341 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d87e2767-ba87-3b02-97bc-ff8f96fa6bc8 | -16.07797 | -50.91689 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bab65dac-aabe-3287-b936-b4cff1510c4f | -12.69567 | -45.84683 | 2025-10-05 05:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30709578-5f0d-31f2-b7c8-2490f694668e | -17.94883 | -57.5963 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 2188f727-1cb4-349c-a240-beee464fdb85 | -13.34932 | -47.59088 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7fef4f1f-3887-3069-9463-8727d1983b1f | -17.8874 | -57.64609 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 19e5058b-fdb0-3aa8-a869-6d2a6132eb2d | -12.27103 | -49.19049 | 2025-10-05 05:16:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 65476645-5e41-320b-918b-793b5cc828f6 | -16.07242 | -50.91968 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b1515191-f88d-3d37-8650-7c5e8c8a5c29 | -13.34897 | -47.59393 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf1ef8b9-f052-33c1-abec-7b17797f9507 | -13.12994 | -50.87215 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b439b51a-9cc6-3153-8c52-143d96e26778 | -12.27026 | -49.19474 | 2025-10-05 05:16:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 479d3dc1-9bb1-3e17-a5ce-d0a187875ef5 | -12.31763 | -55.14727 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da4c3c93-ef15-3573-bd20-8f61e0624426 | -15.38996 | -47.95278 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0db83bab-b43e-3e4e-bc2f-2143d7a986ac | -13.14883 | -47.97963 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41ee725d-0962-3ef1-bdfc-8ccc40b2ed3d | -12.70107 | -45.86042 | 2025-10-05 05:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 719d5942-d0a8-3578-b128-d4a736ee102c | -16.12749 | -53.97949 | 2025-10-05 05:16:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fdeb0e82-8661-37e4-ac6a-bfc5c37c42ea | -18.26178 | -53.36425 | 2025-10-05 05:16:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d3d178e7-ae2d-381b-bdc6-5917e89a935a | -18.20534 | -53.37732 | 2025-10-05 05:16:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 21088a2a-dd72-3c1c-9583-784fa1d9ff92 | -14.58431 | -52.45197 | 2025-10-05 05:16:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README132.md)
