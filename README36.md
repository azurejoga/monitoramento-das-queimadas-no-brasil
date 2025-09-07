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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73e9d678-2a89-3249-80ec-71b2ffebc347 | -17.10351 | -49.89365 | 2025-09-07 04:00:00 | NPP-375D | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6f5cd43-f892-3cf3-b3e2-c80ba337bd62 | -15.08954 | -44.00603 | 2025-09-07 04:00:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b430505-33e2-3be5-8745-bf3ae470ba82 | -16.97473 | -45.83187 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5185518e-73ce-3731-a919-2839aae14752 | -12.77942 | -52.96679 | 2025-09-07 04:00:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d3a1953-b2c3-335d-9199-ebfecf07ab3c | -16.58727 | -40.98923 | 2025-09-07 04:00:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d8374aa3-89c6-369a-9808-773df3360256 | -16.93389 | -45.77691 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 825a60fd-ad40-34e9-b4be-2e8b71e1ae75 | -17.38523 | -49.2328 | 2025-09-07 04:00:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f2089446-6fe9-3254-8523-28f5cd7b3423 | -14.24525 | -53.38028 | 2025-09-07 04:00:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 809ef8fd-bb54-3f8b-be9b-30a8142f95c1 | -12.774 | -52.95915 | 2025-09-07 04:00:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b08187c3-22d2-3f7d-84fc-aafde967722c | -18.2228 | -42.57581 | 2025-09-07 04:00:00 | NPP-375D | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ca3c8318-1293-3af8-a2e4-852e9f271ce3 | -13.91667 | -48.03062 | 2025-09-07 04:00:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 340c017b-3847-37cd-9249-52f86dc4853b | -16.29138 | -45.68668 | 2025-09-07 04:00:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fdb97eeb-7ddd-3ee1-ab47-330563b758af | -16.42986 | -40.55226 | 2025-09-07 04:00:00 | NPP-375D | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 13fd79e4-ecd8-30b7-b4fb-200605631d1b | -14.58048 | -48.07537 | 2025-09-07 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0e9b346c-460d-3d16-9055-bdfb6a40a1ab | -14.29347 | -43.55973 | 2025-09-07 04:00:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f227982f-d940-31ee-9946-a499f3ee4e74 | -17.67796 | -43.53778 | 2025-09-07 04:00:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f845fc91-cdc0-3834-95cd-41838edc19f5 | -19.88988 | -41.42973 | 2025-09-07 04:00:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e9b63253-9557-33d2-a693-68150af54125 | -14.44521 | -48.45157 | 2025-09-07 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d402f73-ef0f-322a-81ce-76fc48e367e8 | -16.82105 | -49.19062 | 2025-09-07 04:00:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 75deb098-fd28-3575-8baa-dea199f48a12 | -19.9048 | -41.44371 | 2025-09-07 04:00:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b5554a47-374b-3960-92f0-4307f8b47c49 | -13.55406 | -48.1158 | 2025-09-07 04:00:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 557404bb-11fe-3579-a05c-437eca0396d3 | -14.50253 | -48.76845 | 2025-09-07 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd68551b-a5f3-38f7-9856-84aa111cb207 | -18.63801 | -42.77031 | 2025-09-07 04:00:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a09acd9e-597b-38cb-84ae-fcc17c69991b | -12.81929 | -52.94817 | 2025-09-07 04:00:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0700961c-3ef4-3a0d-86a3-9f6311d2b136 | -15.36253 | -43.66373 | 2025-09-07 04:00:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a29711c3-8de1-3caf-9acb-c6516bfb2086 | -17.36542 | -42.64504 | 2025-09-07 04:00:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 17.2 |
| fecd9b40-fff7-32a0-b292-beb01df38f62 | -13.66952 | -46.95693 | 2025-09-07 04:00:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0dd23c0-eb2c-3cc8-9040-dc64ef8b9fe1 | -18.67141 | -43.79801 | 2025-09-07 04:00:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c3bdfb4-d2e3-324b-b674-9588cf96affc | -13.93106 | -54.03215 | 2025-09-07 04:00:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e868f9d9-d82d-320f-ad12-0455419d9008 | -19.48097 | -47.77155 | 2025-09-07 04:00:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0a463b9d-0aab-39f2-aae9-e697e9632bc7 | -15.23328 | -52.3633 | 2025-09-07 04:00:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a27d941-ae92-3d0f-ad41-757aaa503434 | -16.92299 | -45.7916 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c0b676f-eb2d-3177-8a66-74a148da527d | -17.71361 | -44.486 | 2025-09-07 04:00:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 135bc840-18b4-33fc-99f8-ab76422f7151 | -15.00859 | -48.00236 | 2025-09-07 04:00:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cce40738-3d12-3bad-aa86-03a532f688b9 | -17.95191 | -42.77482 | 2025-09-07 04:00:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6c68897-f459-3ea4-a29e-b842ec4e8ae9 | -12.82054 | -52.94232 | 2025-09-07 04:00:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66de0f1d-e8fb-330a-be8f-45d72e82b3b2 | -15.22706 | -52.36196 | 2025-09-07 04:00:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08df1362-e526-3cd0-aa57-bfd7c0338895 | -13.47523 | -46.83714 | 2025-09-07 04:00:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dbdfb517-d310-3ed2-9585-f58620201500 | -14.59373 | -48.0845 | 2025-09-07 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| acd45104-ea5b-36b7-b536-3a4b261dfac8 | -16.93492 | -45.75642 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e50d4dbc-a3d5-3d21-b163-598b05c7da07 | -17.95597 | -42.77158 | 2025-09-07 04:00:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80467e36-8aab-3e14-a142-6b919d5e10c9 | -14.448 | -48.46378 | 2025-09-07 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0d1cc49-2637-3e5d-b3bf-9aa58d67e270 | -17.70368 | -47.65229 | 2025-09-07 04:00:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c16f06f4-efaf-3c65-97e0-eadd86f61b7c | -19.6355 | -42.03269 | 2025-09-07 04:00:00 | NPP-375D | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0ca68fe6-1e18-3a0f-a652-e56a2508270e | -18.09137 | -45.44164 | 2025-09-07 04:00:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f09e884-2e97-33f8-8409-3782dcb23018 | -20.07858 | -43.74901 | 2025-09-07 04:00:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 391d5955-d758-3a9c-9a70-0e1bef1156b0 | -15.84151 | -52.27414 | 2025-09-07 04:00:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b2fbcc24-dac9-39e5-baba-e5b65b727bd2 | -15.88447 | -52.1964 | 2025-09-07 04:00:00 | NPP-375D | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 62ea4a5c-7548-34e1-a635-278c98e3493b | -17.55663 | -44.40353 | 2025-09-07 04:00:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d20cc5bc-ccaf-3684-a293-ba11d261a982 | -17.37803 | -49.24295 | 2025-09-07 04:00:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 73ea29fe-4606-377c-b21c-bfe97833a181 | -16.70432 | -45.98541 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a174bc9d-6cb8-3268-be2d-71e3b3decd4a | -19.64928 | -46.06755 | 2025-09-07 04:00:00 | NPP-375D | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c503faae-0806-3912-8998-f62acd2cb954 | -13.858 | -46.24667 | 2025-09-07 04:00:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0f50a30-d22c-3f3b-b38f-8cef819350fa | -13.66912 | -46.96001 | 2025-09-07 04:00:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc0ff9e4-918a-37b9-b780-4381737c9a70 | -13.71287 | -46.8773 | 2025-09-07 04:00:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 65a26cc4-ddbe-3b89-9a01-434e15dbf2a1 | -17.92909 | -49.45275 | 2025-09-07 04:00:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f17dbf68-577b-38db-8147-abac9541bbf6 | -19.94363 | -43.61266 | 2025-09-07 04:00:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e406d501-89c6-392f-9105-79991b6eb6e3 | -15.85582 | -48.12916 | 2025-09-07 04:00:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7bffff1b-1beb-3dcd-a3f3-372a04989040 | -15.17575 | -47.9769 | 2025-09-07 04:00:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1a2e6e0a-b292-32cb-afb4-0f6a49071ac8 | -16.28737 | -45.6859 | 2025-09-07 04:00:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bc44f0c1-4484-389b-b2b9-e4a1da519425 | -15.00709 | -48.00973 | 2025-09-07 04:00:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9234e16-e444-3b47-b4be-7519d7848e2f | -17.65811 | -44.27378 | 2025-09-07 04:00:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 411ee974-8850-3404-b091-4a104120d733 | -20.07513 | -43.74827 | 2025-09-07 04:00:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 26ab08cf-1433-33ae-bad3-106dab4e8185 | -19.2152 | -46.80956 | 2025-09-07 04:00:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f31ad6c5-d2dd-3277-84d5-7bd8818cef28 | -16.29619 | -45.68753 | 2025-09-07 04:00:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| daaed0d0-78f6-3a42-9b09-c3a481401819 | -14.27084 | -44.97646 | 2025-09-07 04:00:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 526b564d-8f63-3f53-947e-83c8108eab1e | -18.49949 | -49.51643 | 2025-09-07 04:00:00 | NPP-375D | CACHOEIRA DOURADA | MINAS GERAIS | Brasil | 3109808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1a2d1ffe-27eb-33cb-8aba-55bce35bf790 | -16.92089 | -45.78727 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 13bd9542-3857-3513-b7cd-014682c685e9 | -15.84785 | -52.27872 | 2025-09-07 04:00:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 80027ad1-18c0-3ed1-acc8-3aaeadab22ff | -17.68283 | -43.55162 | 2025-09-07 04:00:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2ac7204-8e66-37ca-9007-82e39341b73f | -19.50665 | -42.57027 | 2025-09-07 04:00:00 | NPP-375D | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d23ff3ad-7c11-34bc-8476-cc1773ef66c5 | -12.78845 | -52.96088 | 2025-09-07 04:00:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e427ff5a-8daf-3f21-a8ca-e0c3b06400c7 | -13.82831 | -46.26172 | 2025-09-07 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c4bbebb-ec9c-3eeb-9ebc-3e6347191017 | -17.68805 | -44.51205 | 2025-09-07 04:00:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f8552acb-7c94-390b-855f-8714eb0e6e29 | -14.8539 | -46.69198 | 2025-09-07 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a39beeed-a517-3e82-98c2-dc3387842069 | -17.36264 | -42.64058 | 2025-09-07 04:00:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 17.2 |
| ad8f5b90-7d59-3127-99aa-72804c7c6bfc | -16.29952 | -45.69193 | 2025-09-07 04:00:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da6ff649-a524-3154-90da-4f6d04630e21 | -19.89205 | -41.43768 | 2025-09-07 04:00:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 33ac0b13-616e-3c4d-b05d-6d0682e4bc3d | -20.04364 | -41.22547 | 2025-09-07 04:00:00 | NPP-375D | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| dbc1f461-a47e-3f89-be3f-255f73f31e30 | -16.29875 | -45.69187 | 2025-09-07 04:00:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb159d97-49bc-3d74-a105-af01d6213b79 | -13.54886 | -48.10707 | 2025-09-07 04:00:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81cac18d-5308-3bcf-9210-4ac69864d2c9 | -15.0082 | -48.00406 | 2025-09-07 04:00:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 289c5c9a-e88a-320b-a1a8-6c3255272628 | -19.8837 | -45.02452 | 2025-09-07 04:00:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 447ac2f4-454b-3fca-9c8e-790ff75885b0 | -17.67444 | -43.53716 | 2025-09-07 04:00:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5d65c733-d6f9-3423-b016-92929828a3d0 | -18.99766 | -48.44232 | 2025-09-07 04:00:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d90728e-341a-3837-9929-d8bfa9d32de8 | -18.63461 | -42.76968 | 2025-09-07 04:00:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cb38b45a-bd0e-3898-b39d-ac249e565745 | -19.90146 | -41.44312 | 2025-09-07 04:00:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b1b29359-37e5-3feb-bbcc-ff6bf6df47c6 | -13.83412 | -46.25459 | 2025-09-07 04:00:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a63a952-8b4c-3ad4-82ab-6030be8bed17 | -19.4775 | -47.76618 | 2025-09-07 04:00:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 378931e8-4a3e-3a89-a210-9b26c50ad4d5 | -18.68905 | -44.4538 | 2025-09-07 04:00:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6136970-3bbc-3ec7-8289-76fd1917ae50 | -13.36348 | -46.83225 | 2025-09-07 04:00:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23b0530f-7e3d-3b1a-88ef-46cee7ac66ea | -14.79048 | -48.11012 | 2025-09-07 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 38271fab-ad8c-3038-a866-a88a0f3c8670 | -15.1768 | -47.97144 | 2025-09-07 04:00:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fcb74a15-f32d-3b76-a663-800701470e55 | -18.07653 | -47.99111 | 2025-09-07 04:00:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 735d78ff-3b1f-3208-b517-5458e6e9394d | -17.6959 | -44.4886 | 2025-09-07 04:00:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4bd9b9d2-bbf8-30d7-8f46-99f0fabf6b0d | -18.13338 | -45.34193 | 2025-09-07 04:00:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a17fcaef-8d07-325d-83df-4b83b0c66e7f | -18.60298 | -43.64651 | 2025-09-07 04:00:00 | NPP-375D | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 32691eb0-84c5-3bb5-a244-ee768507efe0 | -13.91611 | -48.0239 | 2025-09-07 04:00:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8935a15f-3fd3-3da4-be65-c6231f7f496e | -15.54305 | -42.65968 | 2025-09-07 04:00:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 9069b065-a66d-3f91-9786-2e07c9ec3425 | -19.16682 | -43.0782 | 2025-09-07 04:00:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |


[Clique aqui para ver as próximas entradas](README37.md)
