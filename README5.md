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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57e55537-95e8-379b-98b0-2a3e713f1224 | -19.42097 | -43.49674 | 2026-01-11 04:12:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b62ff29a-6aa4-3cc0-80f1-07f1143ccef1 | -17.75667 | -43.42843 | 2026-01-11 04:12:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6e6ed83d-0996-3190-844f-7a12f7d38589 | -20.24198 | -46.4826 | 2026-01-11 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c18ccca3-4942-3c1c-972e-c3a461a8179e | -20.23253 | -46.47683 | 2026-01-11 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec0e1626-3f2c-3464-b65d-5d108cecc241 | -18.82786 | -51.62314 | 2026-01-11 04:12:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f000a789-cb8f-3822-a716-71d0254b8218 | -20.24233 | -46.39691 | 2026-01-11 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ecab7c07-8067-3e07-8119-5e062defb2b4 | -19.40981 | -43.5026 | 2026-01-11 04:12:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ecc227a0-9bb5-34ca-8262-9907b057cda1 | -20.25164 | -46.50807 | 2026-01-11 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32281073-3c46-3f9a-8fdb-0c40d94f4c7b | -19.69353 | -44.92767 | 2026-01-11 04:12:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9f9eab46-70f5-3e00-811c-32a1c03561b1 | -20.86886 | -43.1566 | 2026-01-11 04:12:00 | NOAA-21 | BRÁS PIRES | MINAS GERAIS | Brasil | 3108701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 78212786-6cbc-31b6-9274-c6b555fd8558 | -20.24408 | -46.49088 | 2026-01-11 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9645fdbc-a288-396b-973f-2c667e796d65 | -20.24954 | -46.4998 | 2026-01-11 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2a606b86-8179-375c-8000-d0e7ca7b7e67 | -18.82232 | -51.61474 | 2026-01-11 04:12:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| dc6b418a-3fef-3122-87d3-df277d6303b9 | -18.8207 | -51.61194 | 2026-01-11 04:12:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6fd51266-4f5e-3f82-9099-07b9e7506c78 | -18.81981 | -51.6166 | 2026-01-11 04:12:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 93eebd34-6cc8-3db3-aa2f-caeb097e0b25 | -20.23525 | -46.48129 | 2026-01-11 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| bd921333-f054-3bf8-8368-e97f7d6d40cc | -20.24617 | -46.49917 | 2026-01-11 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ec1b2ee4-e420-343e-b89e-500973b2764a | -20.13053 | -46.85327 | 2026-01-11 04:12:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4d0b37ae-03f2-38e7-b312-b8183084ad78 | -18.81972 | -51.60443 | 2026-01-11 04:12:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 94777d54-2f5e-3ed0-b07b-4ec6ab358eac | -18.81713 | -51.60633 | 2026-01-11 04:12:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 4a3d30e4-a3d6-3f4d-92f3-6ec1a03f6e3f | -20.25437 | -46.51254 | 2026-01-11 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 39addd4b-9dee-303b-8656-5e175aa4ad62 | -20.23862 | -46.48194 | 2026-01-11 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2cd09056-e3c4-3dd3-bb03-9c1795eafa86 | -19.40648 | -43.50201 | 2026-01-11 04:12:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4652200-49fc-3952-8823-bcfa45e689b2 | -18.81783 | -51.61385 | 2026-01-11 04:12:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8aabb833-93d2-3d56-8fe5-097999761209 | -16.09879 | -56.75718 | 2026-01-11 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2457a0e1-bcc0-3549-9c9f-ee51d6642783 | -18.82325 | -51.61008 | 2026-01-11 04:12:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5603f977-5a1d-324d-a6fc-12c73f69d2d5 | -22.896 | -43.65744 | 2026-01-11 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5c513e45-e835-399f-82c4-da651499fbed | -20.24471 | -46.48706 | 2026-01-11 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0e70df7d-953a-3435-b044-9567ff269c4d | -20.24744 | -46.49152 | 2026-01-11 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cf502264-78e4-30fb-8d46-4ceb54015b97 | -22.9247 | -43.653 | 2026-01-11 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 71327881-a538-36b3-b772-f9eae259b2dd | -18.71046 | -40.00625 | 2026-01-11 04:12:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d017f5e2-14e0-3ec2-ad68-caef79d23272 | -18.81531 | -51.61576 | 2026-01-11 04:12:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 87b75a0a-c954-3b97-b7ed-81ac34b84017 | -18.82428 | -51.61753 | 2026-01-11 04:12:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5f3bc9fe-8f5e-3c64-be67-b269f1c6bf46 | -18.59748 | -46.55381 | 2026-01-11 04:12:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2631b544-8622-3465-b713-03f28513fb53 | -20.23925 | -46.47813 | 2026-01-11 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7e69eae8-7de9-3c76-865a-50abcdf1e202 | -20.25501 | -46.50871 | 2026-01-11 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35e0b3e1-5b73-3305-a8a0-28c3bac3af18 | -20.24135 | -46.4864 | 2026-01-11 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 548b138c-acc9-3aae-8560-cdbd855fda39 | -21.17854 | -47.58706 | 2026-01-11 04:12:00 | NOAA-21 | SERRANA | SÃO PAULO | Brasil | 3551504 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 148107dd-abad-3327-b6ca-d070c0ae4e16 | -20.23653 | -46.47366 | 2026-01-11 04:12:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bbdf20a9-89af-3297-b489-66b3718f29b0 | -20.13093 | -46.85246 | 2026-01-11 04:12:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc0fb7ee-d683-3a50-8981-0051661c80b9 | -18.82139 | -51.61937 | 2026-01-11 04:12:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 282be6e5-430f-33b4-b84d-9da9e9c33980 | -20.14316 | -46.84252 | 2026-01-11 04:12:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a461e13-2835-3593-aa06-4f7753541e97 | -18.82339 | -51.62218 | 2026-01-11 04:12:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 30641f2b-b6ae-328d-b18b-74211ec2ff39 | -17.6226 | -50.35406 | 2026-01-11 04:12:00 | NOAA-21 | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84786f5f-309b-3f96-8849-255feb9e0715 | -24.85598 | -49.23161 | 2026-01-11 04:14:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dcb4318e-5f7d-3053-b2c0-208d8eb229b7 | -23.39809 | -45.37745 | 2026-01-11 04:14:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 23d6921d-b956-3ecf-a996-00978013d939 | -24.85415 | -49.22752 | 2026-01-11 04:14:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e373d8b5-3005-30be-ad3c-3e79081f1022 | -23.39867 | -45.3737 | 2026-01-11 04:14:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8675b10c-23be-3a68-9214-e73077c64e46 | -23.3942 | -45.38058 | 2026-01-11 04:14:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2daf650a-84f0-3f0f-a8d1-6f1d326b3dd0 | -23.40644 | -45.36741 | 2026-01-11 04:14:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5d8a95a9-9f1e-37e2-97b6-4199819155c4 | -24.85679 | -49.22713 | 2026-01-11 04:14:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d0eebaaa-92bc-3a98-8fe8-cab79dbc8063 | -6.5631 | -51.1126 | 2026-01-11 04:30:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| ab5c2074-86a7-3349-9238-5260fa5c2c45 | -1.65171 | -45.91418 | 2026-01-11 04:36:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f5c61ee-118e-3f37-a980-d5b38336e8fa | 0.73112 | -51.4155 | 2026-01-11 04:36:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e34b90d5-6c44-33ff-bcc5-49c06c5bffb8 | -0.06091 | -51.65687 | 2026-01-11 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 241cd902-08b8-389e-aaeb-a450e1345bdd | 0.72707 | -51.41616 | 2026-01-11 04:36:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fb76ae79-4cec-3bb3-be53-cb29c1aed078 | -0.05628 | -51.65979 | 2026-01-11 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47935837-0bd3-3362-a889-e19a31d705ca | -0.09078 | -51.28127 | 2026-01-11 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 35673476-4611-395e-97d0-85c33256e7bd | -1.08296 | -46.77482 | 2026-01-11 04:36:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e6c2e1a-7405-3da4-a272-6fd19966a332 | -0.97675 | -47.57391 | 2026-01-11 04:36:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 999ff26a-f11e-3076-a5bc-ec7eedbfe4cb | -1.0835 | -46.77137 | 2026-01-11 04:36:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28c0bb5b-b814-3ee3-ad67-daa470ab4899 | -0.02359 | -51.0981 | 2026-01-11 04:36:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 090111ba-bd82-33c0-b95e-8f0ca10cb502 | -1.02705 | -47.68935 | 2026-01-11 04:36:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ace1a2fe-c817-3769-9259-b7ed19c37793 | -0.08681 | -51.28066 | 2026-01-11 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 2df637a8-1d9c-354a-8e53-fbe26d20e8c4 | -1.26634 | -45.74235 | 2026-01-11 04:36:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9172698a-d5b5-36f9-ae21-1e966ea97a3c | 0.69444 | -51.44653 | 2026-01-11 04:36:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 13b23682-a3ab-3e15-8f89-1f64ef3bc86e | -2.62012 | -43.09911 | 2026-01-11 04:36:00 | NPP-375D | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e878b20-f583-3c38-acb2-3d42db2319b0 | -1.2669 | -45.73882 | 2026-01-11 04:36:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d5a58895-17b1-35ac-af3c-fba987e91178 | -2.52217 | -43.26 | 2026-01-11 04:36:00 | NPP-375D | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6a464ed8-a020-39d9-922c-d69976981540 | -0.0876 | -51.2756 | 2026-01-11 04:36:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e24ed7f9-61ad-395d-a72c-32f8571c6c47 | -1.16257 | -46.74488 | 2026-01-11 04:36:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a84d0eee-2da4-3f67-a8ab-84975fd45a9b | -0.13241 | -51.38876 | 2026-01-11 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52630d4a-63e4-3432-83ed-953197494652 | -0.09158 | -51.27621 | 2026-01-11 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 56ffd644-959a-30b1-a0d7-d27d6de32893 | -0.2714 | -48.78733 | 2026-01-11 04:36:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91fded7b-c0eb-3026-8423-e2edf849bc6b | -2.30611 | -45.77178 | 2026-01-11 04:36:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7384eb30-8687-37b0-856d-6269ae0b6df0 | -0.27199 | -48.78354 | 2026-01-11 04:36:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ef6c97d-ce4d-3c3c-b39f-2f4ebeb724b3 | -1.65226 | -45.91066 | 2026-01-11 04:36:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68db34e6-f6a6-3400-b3ea-3f8eb040185e | -1.05717 | -47.13121 | 2026-01-11 04:36:00 | NPP-375D | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d1e2983-cf47-3f02-b985-d06093f032a7 | -2.62066 | -43.10175 | 2026-01-11 04:36:00 | NPP-375D | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 19e10249-e366-3223-9939-60f511b96e14 | -2.52147 | -43.26453 | 2026-01-11 04:36:00 | NPP-375D | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 47f8a902-0f70-3da2-bd16-b0b72b159aaa | -0.26852 | -48.783 | 2026-01-11 04:36:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33665cc3-ddba-35a1-8735-241996e206cd | -2.46658 | -45.12476 | 2026-01-11 04:36:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c6d82a9-dd0f-3d53-86c0-5c1d44f85237 | -0.26793 | -48.78679 | 2026-01-11 04:36:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69ae6036-14cb-3bc8-8cc3-6cba85c50ec5 | -2.24008 | -45.87854 | 2026-01-11 04:36:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 342718d8-bb04-3bc8-85ca-e725df99a62b | -2.62393 | -43.0997 | 2026-01-11 04:36:00 | NPP-375D | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58762ce7-e8f8-311c-8fc9-399a48d1eba5 | -2.30527 | -45.77201 | 2026-01-11 04:36:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3dd83aed-dd06-3140-b897-70a258a5e9c8 | -1.79861 | -47.7029 | 2026-01-11 04:36:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4b7f798-fbf2-3f8a-acd8-2350cfe196a1 | -1.01552 | -48.89264 | 2026-01-11 04:36:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae3df680-78ed-3906-a29c-96e8c7648663 | -1.4968 | -45.91565 | 2026-01-11 04:36:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58fa09a2-9600-3c45-88ff-02f78e1ebf6f | -4.71043 | -44.47918 | 2026-01-11 04:38:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11fc09d2-7962-3812-b497-ac8de82d93f2 | -1.84105 | -54.31243 | 2026-01-11 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e7689798-c08e-3a81-8386-481fea221779 | -2.7167 | -54.54934 | 2026-01-11 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25ef80a2-5d56-35ee-b023-4163d3b5f4d6 | -7.5993 | -45.88763 | 2026-01-11 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96d83e57-7f2f-389f-b785-8b6b1c576bc5 | -4.70979 | -44.48335 | 2026-01-11 04:38:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4e760df-7e20-3ca0-86b4-361233cb0e57 | -4.2638 | -48.84231 | 2026-01-11 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6138ff7-be25-3b3a-9e0d-9aa318b65798 | -2.19117 | -52.01212 | 2026-01-11 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b0a606ca-dae8-395c-ac25-e8342dee8cf6 | -2.89145 | -45.21904 | 2026-01-11 04:38:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9194a67b-6db4-33de-8383-7c42860b25f9 | -5.46217 | -45.28277 | 2026-01-11 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bbe92227-e2e4-3e87-b8e5-3d008947533f | -5.96275 | -46.15082 | 2026-01-11 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c95526a1-e55e-339e-b142-755057c25ecb | -4.7598 | -46.70987 | 2026-01-11 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README6.md)
