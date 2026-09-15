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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74c6080a-e333-31ac-93cd-342a235dcfc3 | -2.77697 | -49.45584 | 2026-09-15 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0951791c-446b-3e7b-9a0c-1c4beba92898 | -5.63431 | -40.85117 | 2026-09-15 04:12:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9515ebcc-f137-35da-ac76-d580d1a4da99 | -2.81811 | -51.34005 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1aa54fd-7895-3f43-9b70-70f784c75c97 | -4.95329 | -45.147 | 2026-09-15 04:12:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| afe7f11b-b1fa-30c0-9b01-9637f5b8aa82 | -2.90601 | -50.43864 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dc810340-4e24-337e-a90a-6396fed2f26f | -5.63375 | -40.85466 | 2026-09-15 04:12:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7bf538ba-d200-3a96-b605-babcaad4c04e | -4.49448 | -45.91104 | 2026-09-15 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64f4e618-4941-345b-8aea-bb1057ef0a05 | -4.66802 | -42.0854 | 2026-09-15 04:12:00 | NPP-375D | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 75106229-4cd1-3130-bf36-00897e131912 | -2.96237 | -50.40467 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f7cc4bad-ec20-3128-bb35-0d498226905a | -4.24636 | -38.06248 | 2026-09-15 04:12:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| d37b2f5d-4143-3e80-a868-1f0f947a06d0 | -5.64046 | -40.85573 | 2026-09-15 04:12:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8b037184-dcca-3577-b2d1-d779961c4700 | -2.90104 | -50.39689 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a615d558-fe17-34d7-ab87-dd04cb5faa77 | -4.80452 | -42.88062 | 2026-09-15 04:12:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e0f3504-d8ea-3971-a241-85bf1d17104c | -3.25505 | -47.0895 | 2026-09-15 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54925272-2be5-32cd-9e39-39529d008fa4 | -4.47019 | -38.50597 | 2026-09-15 04:12:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 60b9fb11-7417-303f-9c6e-a3fb9eb73d0a | -2.03551 | -46.94285 | 2026-09-15 04:12:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a526fffb-574b-3ce1-8bcb-2e1473d81942 | -2.89535 | -50.42698 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8d537540-458a-3bb7-ba1c-d40cb5ae2535 | -2.8233 | -51.34144 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e653b3fa-731e-3d68-bcd2-aec2e635ba45 | -2.95701 | -50.39898 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ade5e820-a258-3918-9d0c-8ecae54bab47 | -3.07772 | -50.57759 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 195fb063-d400-35d5-8a28-dacecef8218f | -2.901 | -50.39419 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4fdfbeea-c058-325e-afda-754dc8953ea5 | -2.91328 | -50.39626 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad040a46-81b2-3884-a3e7-377e68e6e737 | -2.9002 | -50.39885 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 502bf0a7-3f08-3622-82b0-17bd27a1976f | -3.66986 | -40.58094 | 2026-09-15 04:12:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3830b31c-e016-39b6-a054-77c3fd9412d4 | -3.39586 | -50.76039 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8ce471bd-4e60-319d-b0fc-4d448c17fde0 | -3.23093 | -50.59203 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 50c5803c-2cff-352d-84d5-3bc1ac902613 | -3.66254 | -40.58344 | 2026-09-15 04:12:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 28ecd820-6a2c-3f80-b50f-8ba5c41c880e | -3.49362 | -50.37509 | 2026-09-15 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1b943f2-3008-3d30-9c24-cff787cc639f | -5.55796 | -43.43701 | 2026-09-15 04:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b66babe0-63e2-36d6-afc1-93d19ae2e7b9 | -3.86123 | -51.98798 | 2026-09-15 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34657dd4-018f-39f5-9777-ef56c8200233 | -2.96316 | -50.39997 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d27f6458-2aef-32ac-8d18-a8c3b2ce5bf2 | -2.92235 | -50.41712 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2cf9d80-0953-3c82-bd88-cb7c1f30267d | -3.64727 | -42.93203 | 2026-09-15 04:12:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf6af766-e6d4-3714-9f0f-32f6eb24e772 | -5.79791 | -43.64989 | 2026-09-15 04:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3064f3b-d844-3a82-b262-c72ee5eb3084 | -5.73997 | -43.27406 | 2026-09-15 04:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 68bb0796-9452-3a2b-aaed-f1c2812e071d | -2.89639 | -50.42509 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b50fc57a-fc25-3969-a8d3-756fa84f91ee | -2.89407 | -50.43914 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b5cfed6b-a028-3b71-9d2b-c7a79432fb36 | -4.18668 | -48.68407 | 2026-09-15 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 55f35561-23e7-34a2-8a88-d2259d5dc1e2 | -4.67921 | -42.08319 | 2026-09-15 04:12:00 | NPP-375D | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c3e42851-b2d7-3fa3-8479-c0978c344530 | -4.18195 | -49.40439 | 2026-09-15 04:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 038dbdf2-7d9d-36ee-82b0-c6f1455b9a84 | -4.36132 | -47.78273 | 2026-09-15 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 66959901-c6e2-3ad9-93e5-d0d8ce9fc3b7 | -2.8918 | -50.41459 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34632d8c-3498-3f52-bd5a-21147faf08f3 | -4.67154 | -42.08596 | 2026-09-15 04:12:00 | NPP-375D | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| fc80b1a3-46a3-3a7d-b456-dfc26c370d51 | -2.88792 | -50.43808 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a8b72406-88c1-35a9-9beb-c3c66ac9f3aa | -3.66928 | -40.58451 | 2026-09-15 04:12:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8c59e495-3122-3f73-ae2d-1ffeeaa668da | -4.67569 | -42.08262 | 2026-09-15 04:12:00 | NPP-375D | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c3ac5fab-a98e-39fc-b389-11d27e63bde8 | -2.92635 | -50.39368 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d2300a7-a220-37d7-8302-7e67f0ad22e7 | -2.89795 | -50.41565 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f5e2cd2-f982-34bd-b73a-e2f66d9ca698 | -4.95393 | -45.14323 | 2026-09-15 04:12:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 15f36dcd-81eb-3992-a46a-0123c30d0e7a | -5.53009 | -43.37343 | 2026-09-15 04:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2025b71-40d3-39c0-ab5b-1b70cde7e3d2 | -5.60829 | -44.84394 | 2026-09-15 04:12:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e5a1d232-2293-348e-809e-810e8f039b44 | -2.90794 | -50.39056 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 491331a0-f500-38ba-8da5-13d93ff8bf54 | -5.60423 | -44.8433 | 2026-09-15 04:12:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 52082226-d605-3854-8ff3-007e27a6c058 | -2.90392 | -50.41394 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7a51ea19-f1f1-3d0d-ad8c-e9abdd2d6c3b | -2.93168 | -50.39943 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2fea2c27-0b8d-383c-ab3e-14facd36222c | -4.3618 | -47.77988 | 2026-09-15 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8680469c-5592-3008-abbe-9c3065526532 | -3.07053 | -50.57334 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77c0d603-0a2c-3a6c-8081-22a1f9f0774a | -2.91862 | -50.40193 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af1a42f5-16af-3ffa-a9f5-dae303f83828 | -3.23174 | -50.58727 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c5d9fea0-f9da-36ec-8735-d06ecb7f8e37 | -2.88759 | -50.43523 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 265b15f6-55a7-3ee6-872c-b6f40a2adc47 | -4.66865 | -42.08149 | 2026-09-15 04:12:00 | NPP-375D | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1ebebb52-6b75-3b4a-9e2c-7ec57577007b | -3.96549 | -43.1138 | 2026-09-15 04:12:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c172d317-37f3-32f2-94b2-a500cdbbcbc7 | -5.63486 | -40.8477 | 2026-09-15 04:12:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 00dcc110-cdc0-34b5-b946-a5c99e36a545 | -2.96394 | -50.3953 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee79be8a-deca-388c-95ca-fc723343a5d2 | -2.90926 | -50.4197 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| df65a030-8c76-34e6-87f2-91d676930744 | -2.32549 | -47.20255 | 2026-09-15 04:12:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3195532a-4ab5-300e-80b3-66a2a4eb4194 | -2.9146 | -50.42548 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5f4dddaf-0bef-308d-b34d-2707a3821081 | -2.90634 | -50.39989 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0201f691-8fe8-35d3-a3e9-3a73e1ae74a2 | -2.91621 | -50.41605 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b34ffcfa-0437-3bbf-8c36-8316c90c6e3d | -2.91408 | -50.39157 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8caf2d8-cf3b-3691-854e-b59bb38431d4 | -2.93089 | -50.40412 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 670da003-a486-3849-bd5a-d3a65761cfc5 | -3.39672 | -50.75546 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa00ddef-831e-3915-a2e1-583cc65efe2c | -2.94851 | -50.41196 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0935b680-33dc-391d-b911-5e62ce29a617 | -2.89002 | -50.42121 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8c44883a-e841-3e00-954f-d72eb0930d58 | -3.07759 | -50.56935 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cc823d62-6703-34b0-93ff-716aeb6241ba | -5.60771 | -44.84748 | 2026-09-15 04:12:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 98033f29-b658-3f6b-aa8a-3829c7d339c3 | -2.91943 | -50.39724 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 518b93c0-e51c-3cf6-90ad-dc9f249cfb1c | -3.37361 | -45.08974 | 2026-09-15 04:12:00 | NPP-375D | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ec66e263-9b07-3d86-8002-b6c8e6ad7d58 | -2.8884 | -50.43057 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9df2ab9-d0e7-3367-8960-120a97a6c0ca | -2.91701 | -50.41136 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aacf3ed5-f5f6-3ed8-af0f-3827200f7cf3 | -2.95087 | -50.39796 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df17a852-c399-3570-80b5-7388aa7d28ad | -2.91297 | -50.43497 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aee2d1dd-0db9-3515-8d6d-a615d22bd992 | -5.55496 | -43.43928 | 2026-09-15 04:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3e2260e2-d200-3d95-987f-ad6aa96a28d3 | -3.22556 | -50.58621 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f7a7eed8-b8cd-3b94-9f7a-02d6a4913488 | -5.63094 | -40.85068 | 2026-09-15 04:12:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 923f460c-e8b1-36e0-985a-1b0922323c63 | -4.67217 | -42.08205 | 2026-09-15 04:12:00 | NPP-375D | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 51296a83-dd83-3e23-9939-d9a9d0fddc0f | -3.77233 | -51.34976 | 2026-09-15 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8efe64b-b569-3be4-b304-92a5c04a8b54 | -3.96923 | -43.11441 | 2026-09-15 04:12:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c553556-e906-323c-a4ad-f42e68cdcaf7 | -2.94476 | -50.39678 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 136a40d1-c4dc-3980-ada1-e43360d8e09d | -2.89778 | -50.41288 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b2b1949-32fd-3ba9-a872-c8242baeff48 | -2.82708 | -49.22739 | 2026-09-15 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c0cd2896-016e-395a-be06-185b0f502f19 | -2.91007 | -50.41499 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 22b3bf78-5969-36d6-bee5-90e5a25117ae | -4.24693 | -38.05888 | 2026-09-15 04:12:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 400363c0-9383-348c-a0cf-dbfcbb54a63d | -2.90765 | -50.42908 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fcc3db02-3871-378c-b746-80ff293b5fff | -2.04047 | -46.94366 | 2026-09-15 04:12:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c3d6807-a07e-38f6-851c-4e66c54d6fef | -2.82643 | -49.23129 | 2026-09-15 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a8fc1b90-b7be-31a3-a786-6f233e13de00 | -2.9052 | -50.44339 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 79797e1a-fdbf-3556-ac29-771080e06cc6 | -2.90231 | -50.42331 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 054892ab-364a-328a-93d7-39ed813cfe9e | -2.77627 | -49.45996 | 2026-09-15 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0216b936-87fc-3d37-9757-0417a712bd6a | -2.91992 | -50.43133 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README24.md)
