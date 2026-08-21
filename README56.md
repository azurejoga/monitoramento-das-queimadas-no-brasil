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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f078c8c0-3d9f-3d55-a2b9-f9d8b3d45375 | -6.88013 | -43.74646 | 2026-08-21 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3514bbd4-36a3-3e46-8d78-9491e6fc2665 | -14.56951 | -52.99249 | 2026-08-21 05:23:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbbb323d-2a85-3152-a737-d8822e0984a6 | -5.86952 | -57.661 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9083cd0e-c802-33cb-afe4-856c6cc5b697 | -6.22623 | -55.48336 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9841f35-ec20-36bc-bf2f-e07fe6f69271 | -6.75167 | -59.46313 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c1fca32-5862-32ce-b535-37bb8c4265a1 | -6.66639 | -52.88304 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3af5128-53ea-3aef-a12b-99f0ca98f13d | -6.2223 | -55.61892 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ad11882-0ed4-3dd7-957b-ec21d4b7bd62 | -6.60621 | -58.39019 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| becc7e25-fec3-31aa-a1b6-d7193a80bc9e | -6.89848 | -59.44115 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d15612c2-2cd7-340a-8e1c-f163e25afd48 | -6.25437 | -48.65126 | 2026-08-21 05:23:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8272807f-bf40-3e1c-ba32-39045f2205d8 | -13.37979 | -54.37323 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 39.7 |
| e899c945-0e87-38a4-b04a-47e605e66693 | -8.56979 | -54.66855 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f7de8e7-bf85-3b16-a84c-1a5b4d53dea1 | -6.88531 | -56.42984 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d2132a0-1516-3757-a8ef-2cd49e1dc28e | -6.854 | -59.43389 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 99f99e38-5701-3235-986f-a1bb8211a0dd | -6.7551 | -59.4637 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e20fbd33-913c-325a-9ed3-d0a3c199472c | -9.21848 | -59.76719 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f2bf414f-3b2f-3c82-8c56-c7c83a17086e | -7.14394 | -47.50569 | 2026-08-21 05:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db5ee5b7-cbfd-36da-98ae-888405674fff | -6.31496 | -55.9219 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76215b9d-c74b-3c72-b77a-2e66405b9e7f | -6.43432 | -52.71998 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba85cf9f-4b9e-3601-9f45-d1c042680da5 | -6.42285 | -54.94004 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19e3e832-f401-3bc6-afe7-678aa480ddac | -6.2339 | -55.41166 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70a69e3b-ab91-38e1-98ba-d25d79e2cecf | -14.33078 | -51.90639 | 2026-08-21 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 03a85173-cf30-39cc-902a-e799cd2d6146 | -8.58936 | -54.73696 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07605e4a-96f8-35ab-a29b-b98cf7fbabb1 | -9.30796 | -56.81061 | 2026-08-21 05:23:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b5476c2-67e0-37c4-86aa-636812eb3f0a | -12.5095 | -54.756 | 2026-08-21 05:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bd55c38-c36d-3ff1-9a20-839fca15da90 | -6.22565 | -55.48708 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39de3f32-83c1-36a8-b7dd-2fb703c580e7 | -9.20989 | -59.7771 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58946469-50c7-36a4-9086-6d319502cae1 | -9.11744 | -60.34425 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bcbf2770-76a9-3380-a7ee-f517d9c7fa60 | -6.69836 | -59.10027 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8b4e1ac-d5a7-36f2-938e-80fd410c7018 | -6.86732 | -59.02703 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 794d1c69-528f-3bf5-b403-f6f74fa3215c | -6.25174 | -55.41046 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6313dcc0-a795-3d7b-8c7b-6075eb290fb2 | -4.94008 | -55.78574 | 2026-08-21 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 311db9be-3538-3ffb-a251-d1b6d0664fdb | -13.40689 | -54.36914 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36f7e2b6-191c-372b-bc73-1bdddfad17a8 | -6.4327 | -52.7433 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae84fe2c-91ca-37d5-a745-4345af864a30 | -6.69984 | -58.94081 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d8380bdb-f75a-34dc-8a46-ec3f998f232b | -6.91394 | -59.34508 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07d59aa0-0455-36e9-8b08-db1d0a80d6d1 | -6.43185 | -52.72215 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 582a5fb3-040a-30af-b966-508067097741 | -7.01308 | -59.5501 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8408bdc8-b50e-3b66-bdae-797a6dc72d16 | -6.57932 | -58.99598 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 91a223ac-afdc-31a1-a12a-c1a1ea0c8c27 | -6.48204 | -55.90264 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35b88d33-d943-3360-92d7-ba494fa8253f | -12.49806 | -54.7542 | 2026-08-21 05:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d9f34ffc-ade3-3666-8136-ce2422052b51 | -15.00208 | -52.68409 | 2026-08-21 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 880546fb-a9ac-3306-877e-c23872441b93 | -6.69588 | -58.94384 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3316bae-8d34-3465-815a-5e32ecc41a9d | -9.21609 | -59.7819 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 72164324-6997-3413-9afa-4a7f3bd9f238 | -13.38624 | -54.38467 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 372db6be-19b6-37c1-8739-c1fbdb457f18 | -9.99963 | -48.56109 | 2026-08-21 05:23:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b24d62e4-e7ba-395c-8179-40f5fecaeb10 | -6.89566 | -59.43689 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7768be8d-fa4d-3a4b-81be-9634820227f4 | -4.10485 | -56.36425 | 2026-08-21 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d100187-0029-3d23-8272-c06fcfc807cb | -7.74299 | -61.09452 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 63546c36-c281-3974-84ff-4a19e17aaf02 | -8.57997 | -54.77454 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cb81513-ed6e-3055-a720-55cc59df2699 | -4.01571 | -48.06581 | 2026-08-21 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92107d52-b4a8-3776-a195-e5927cb48bfa | -4.90578 | -56.26716 | 2026-08-21 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78f44504-03b2-3969-8a8e-d6250e5b0d92 | -13.09445 | -58.18432 | 2026-08-21 05:23:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ffcd860-02f1-3c7b-9f9f-dca9dea02cfe | -6.58108 | -58.98512 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03e25fc8-0615-3bed-8384-0c11e8fc190c | -6.6539 | -56.43751 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b0c17cc-bc15-3f72-97c8-6f498ba4dc52 | -6.86265 | -59.42386 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df7d8f3c-e2e3-3721-ae8a-a2475cca656b | -6.34986 | -44.07948 | 2026-08-21 05:23:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 108e8318-3e81-329f-a43a-979b92a1d07f | -6.13388 | -59.90849 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de3abe4e-d1a9-3885-bbb7-b861a8636ab3 | -14.11538 | -58.83989 | 2026-08-21 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29725f1d-d5bf-3d68-b213-529b3d66c880 | -13.67339 | -48.7644 | 2026-08-21 05:23:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81771403-e695-3b7e-9a37-cb0e401976de | -6.86445 | -59.41275 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ccb7c122-31f2-3c91-acc6-fcc117acebb2 | -8.57934 | -54.77874 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96c48f17-41a6-30e9-8257-f4d3f5ff980b | -8.71739 | -49.61324 | 2026-08-21 05:23:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9752d70c-59e6-35de-8434-ef7b1378e262 | -7.74805 | -61.08667 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af2e9a8e-bb72-31ad-a2e7-2b4c34c25992 | -6.11794 | -59.91791 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de6cf625-4507-3d38-8a4f-9ac836c9cb74 | -3.91312 | -56.1196 | 2026-08-21 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b73c4497-4420-3eb2-a0d8-fc6dc8d3ef3a | -5.66443 | -51.64366 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7a029b66-507b-3e24-8eeb-63152ea23a59 | -7.37259 | -45.81957 | 2026-08-21 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 5ad7282c-22f9-3bcf-9ddc-f945c1fb5552 | -8.15917 | -46.72926 | 2026-08-21 05:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60d8a68c-5ddf-336c-a484-6cc609df194b | -9.79867 | -46.6436 | 2026-08-21 05:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c6ebf9cf-3119-3b70-a3b7-fbbfb39e6ce9 | -6.81778 | -59.39761 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 859c6a5a-a196-322f-a721-6ed9bed124b8 | -8.65496 | -54.61826 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c21f792b-4fff-3d9d-a15e-4fe9e9b59e13 | -6.43193 | -52.74841 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4206a386-aab1-3791-a10d-12428aadfa43 | -3.20522 | -61.27749 | 2026-08-21 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f349de51-d614-37ab-a2ed-a01f23e22c39 | -14.31664 | -51.90429 | 2026-08-21 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce9159f5-2e50-3b17-8520-19b028802b4b | -14.22999 | -51.93212 | 2026-08-21 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ddb00900-07de-3c0e-ae8e-d416b2a3f933 | -6.64377 | -56.41415 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a8fd890-4f43-317d-bbe6-32e651f35c76 | -15.00265 | -52.67965 | 2026-08-21 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b1498f5-4f69-35be-80b3-8174e21cc05c | -6.85339 | -59.4376 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b0dfd6c7-c61e-3d69-97c1-dd4a84a2214e | -6.0095 | -57.80037 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3463c0b3-e737-3af5-925e-810be428869f | -6.37586 | -54.94096 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 811114d8-ba44-392c-a483-9dc92311ffd9 | -8.52677 | -55.34001 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9aa52d86-2e9c-334d-93c9-999f43097985 | -6.66271 | -56.35863 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43f6adaa-7c26-3de8-a6a6-46fd126087cd | -8.16563 | -46.73116 | 2026-08-21 05:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 010d9b21-97cb-332c-80b6-63fc9e68cc24 | -13.63969 | -51.76408 | 2026-08-21 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f625423-1145-34b7-97d7-e7709f6a5c61 | -6.88822 | -59.43945 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a6ff3ac-f1b1-3c0b-b5fc-54d1e248f46b | -7.63124 | -45.76424 | 2026-08-21 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4689c1af-d2d0-3b25-8ac1-c01392a12536 | -13.43679 | -51.79138 | 2026-08-21 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c947b5d2-e101-3b8d-b336-c5bcfa55770a | -6.7976 | -59.44006 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2713e44b-e4f3-3119-b37a-edfa2f108841 | -8.90096 | -60.54427 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c5157cb3-2160-3559-a75f-7d90d9424614 | -6.94478 | -52.7875 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67b91ea6-480f-3ae2-86df-9b5516584f57 | -6.82804 | -59.39925 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2609f98b-5f3b-36cc-8578-4d22dfc26b81 | -7.25599 | -49.89925 | 2026-08-21 05:23:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 48d6c2a8-072b-325d-8745-6da05c565a54 | -13.37835 | -54.3835 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| acb16b75-8d44-3155-8bce-6da3f558f77b | -9.05947 | -50.88671 | 2026-08-21 05:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac04f620-23e2-3828-8dd6-5f89b6a10add | -6.75227 | -59.45943 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a1b11c6-deb6-3ad6-bdf3-cdd81e8db730 | -9.05985 | -60.43365 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2261a1f9-a9cc-3010-a69d-68f35854badd | -9.21389 | -59.77397 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb58d4d8-9f59-30d7-ac4c-7878c26975d0 | -8.56806 | -54.65512 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 317ed063-a605-3ebe-bac3-03f2da7b2d62 | -8.58679 | -54.75398 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README57.md)
