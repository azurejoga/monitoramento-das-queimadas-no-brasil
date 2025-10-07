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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13b2a8aa-9396-3394-89d7-e233ccffe42f | -18.1176 | -53.3548 | 2025-10-07 08:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 03cb50bb-90ca-3fb8-9df6-9b41fe1d2418 | -15.6397 | -52.5474 | 2025-10-07 08:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 1be55129-db0d-3254-b1da-c398e446409e | -15.6198 | -52.5715 | 2025-10-07 08:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 769a005a-2e02-37d7-b690-ea4d529cd08d | -15.6206 | -52.5288 | 2025-10-07 08:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 16c605f2-ac36-3765-b2b4-2dcc24102906 | -15.6202 | -52.5501 | 2025-10-07 08:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 180.3 |
| cf4a2d66-2aa5-35aa-96bc-42ebf0b04f38 | -18.1176 | -53.3548 | 2025-10-07 08:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 93.2 |
| dd4dfc17-3870-3d49-b34d-001cca44fe43 | -13.2424 | -51.672 | 2025-10-07 08:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| fc704e51-5088-319c-a34f-ed8e0f7c3fd8 | -15.6202 | -52.5501 | 2025-10-07 08:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 4a588a0d-c9dc-3608-9b36-91eeefdd1d21 | -15.6198 | -52.5715 | 2025-10-07 08:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| b5158351-2e28-3a7f-9832-337263bf6a31 | -18.1181 | -53.3333 | 2025-10-07 08:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 75.0 |
| a1a04cf9-63f6-3ba1-a492-114d88368436 | -18.1176 | -53.3548 | 2025-10-07 08:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 85.5 |
| d2e6bc3d-f5fb-3f62-854b-d0fb9389fc28 | -14.7775 | -46.03 | 2025-10-07 08:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 170.1 |
| fcd568d7-2495-3796-a429-009681cebf18 | -14.777 | -46.0532 | 2025-10-07 08:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 478.5 |
| a2fe46ef-e124-3dd2-aeef-12f0c1ae251c | -14.7765 | -46.0763 | 2025-10-07 08:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 957a8bb2-9289-3626-9218-111e589a0b67 | -14.7966 | -46.0497 | 2025-10-07 08:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 117.0 |
| d4abf986-1b0c-31dd-9457-92811621aa9f | -14.7765 | -46.0763 | 2025-10-07 09:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 305.9 |
| 7c1eb385-ad04-379c-92c7-7def19e26f13 | -14.7961 | -46.0728 | 2025-10-07 09:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 162.8 |
| 0721c96e-c930-34a3-8953-331792ce4f07 | -14.777 | -46.0532 | 2025-10-07 09:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 603.5 |
| 814f6d0c-21aa-3ef1-b1e4-93a3d0fbf079 | -14.7775 | -46.03 | 2025-10-07 09:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 0b8f3fe1-2325-33cd-a69b-e5cf6eb4e272 | -14.7966 | -46.0497 | 2025-10-07 09:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 295.6 |
| cef63288-8809-3e7d-bd80-cf512b43722c | -14.777 | -46.0532 | 2025-10-07 09:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 282.3 |
| 79fd3f0b-d3f7-3455-b4e2-0e2c9e0d424f | -10.9288 | -51.1078 | 2025-10-07 09:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.2 |
| eb3248f7-8432-3f62-8258-4247018a6b94 | -14.7966 | -46.0497 | 2025-10-07 09:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 166.5 |
| 87ae7ef2-f1a9-3304-b91b-c86559f8f3ef | -14.7389 | -46.0138 | 2025-10-07 09:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 133.6 |
| c5b22014-3b60-3298-b11a-1813fac640c5 | -14.7765 | -46.0763 | 2025-10-07 09:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 27faf6b3-0744-339a-82bf-bae916669011 | -14.7961 | -46.0728 | 2025-10-07 09:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 104.6 |
| c90bf131-fd8f-3490-b8c8-01642ef1ce9a | -14.7585 | -46.0104 | 2025-10-07 09:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 01d28941-29da-35e6-8c8b-3bf51b515470 | -14.7389 | -46.0138 | 2025-10-07 09:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 589dad8d-a3e5-386c-82de-862bcc206861 | -14.7389 | -46.0138 | 2025-10-07 09:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 3b684485-4e6d-310b-88a3-a0a3799ca7d0 | -14.7585 | -46.0104 | 2025-10-07 09:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 76bca27b-0f26-382b-b8ce-f76c57dbccb6 | -10.4294 | -50.2877 | 2025-10-07 09:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 113.4 |
| af7d9b2a-18a0-3c7c-b7c1-e54335bc0ff4 | -14.777 | -46.0532 | 2025-10-07 09:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 115.7 |
| be9964fd-d68b-3015-a2a5-88b1c8dc7488 | -14.7966 | -46.0497 | 2025-10-07 09:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 934b90e7-c9c3-32e3-9b01-e60c23804ebd | -14.7961 | -46.0728 | 2025-10-07 09:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 100.4 |
| b745a9e0-d621-3120-8a75-5dd02824a73e | -14.7389 | -46.0138 | 2025-10-07 09:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 60f02830-9489-3b51-84e0-d9185c8743a3 | -14.7585 | -46.0104 | 2025-10-07 09:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 6b5f3df4-ed2c-3047-91ed-658832b4464e | -14.7585 | -46.0104 | 2025-10-07 09:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 37562918-aea2-31a8-be6f-70bb2cf07eef | -14.7389 | -46.0138 | 2025-10-07 09:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 543b4d63-79e2-3b31-ae63-d3171f773e8c | -18.9846 | -47.8282 | 2025-10-07 10:00:00 | GOES-19 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 189.7 |
| 88036b6e-01b9-31fc-a671-3400c67d6545 | -11.6656 | -46.4073 | 2025-10-07 10:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 8fcce32a-c2b7-331d-b9d2-989292366ebd | -14.7966 | -46.0497 | 2025-10-07 10:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 3e484ab6-94ad-30e1-8464-9e79e1d3d99b | -14.7775 | -46.03 | 2025-10-07 10:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 520c0d9d-4c8a-356a-b55e-ba464a02e7a8 | -14.777 | -46.0532 | 2025-10-07 10:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 094c6fb9-7f29-3a68-b36d-fb66059cfbf3 | -14.7585 | -46.0104 | 2025-10-07 10:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 127.0 |
| deb89f53-6a56-3ea1-9e57-fddb80e989f7 | -14.7389 | -46.0138 | 2025-10-07 10:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 6fd028bb-1c92-366f-bc78-e44ee5997f00 | -18.9846 | -47.8282 | 2025-10-07 10:10:00 | GOES-19 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 112.2 |
| dba9b0ba-eb2e-3d43-abdc-69584c4769f6 | -14.7389 | -46.0138 | 2025-10-07 10:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 2880ca8b-0c8f-325c-89c5-d163811c05ed | -14.777 | -46.0532 | 2025-10-07 10:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 86c7d578-6ac7-3697-9ba6-e049e7a7d9fd | -14.7966 | -46.0497 | 2025-10-07 10:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 106.0 |
| d6a4c054-2cbd-3bdf-ba60-3b9bbfa2beac | -12.3796 | -47.1633 | 2025-10-07 10:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| b1ff548d-4ee4-31ff-bff5-15b507389e55 | -14.7389 | -46.0138 | 2025-10-07 10:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 213e7a1c-977a-3150-82f2-78b2581a37db | -14.7389 | -46.0138 | 2025-10-07 10:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 135.3 |
| fbc0869f-e873-36f9-8791-06dccd258165 | -10.4245 | -45.3907 | 2025-10-07 10:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 170.3 |
| d3270ace-8381-318b-bc55-d3100b53459e | -10.4054 | -45.3931 | 2025-10-07 10:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 0c887d11-8367-31e0-bf5f-ac26e3c7ab60 | -12.3792 | -47.1858 | 2025-10-07 10:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| c70cbc11-72a9-3aec-9a9b-804e113c8b2f | -12.3796 | -47.1633 | 2025-10-07 10:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 187.4 |
| 9bb38dd9-1ca1-39ea-a90c-4f88b36ef509 | -14.7585 | -46.0104 | 2025-10-07 10:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 9bc3428d-d6e4-3f8e-8b4a-5315ebd2b34e | -12.3988 | -47.1606 | 2025-10-07 10:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 30d5c386-f2ff-3e7b-822b-61dcb2b7658f | -14.9224 | -51.4292 | 2025-10-07 10:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| b905a052-4de0-3935-9396-244154fa49d7 | -11.8447 | -44.9176 | 2025-10-07 10:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| ddd71c5f-9991-3039-bc85-f5bb817d6105 | -12.3792 | -47.1858 | 2025-10-07 10:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 3af17a58-8343-3407-b618-df6e8c3b3c9b | -12.3988 | -47.1606 | 2025-10-07 10:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 327.8 |
| e78b5ee3-035b-3b7a-b99c-c23fcfc9e4b6 | -14.7384 | -46.037 | 2025-10-07 10:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 06c9d513-25ea-32d0-a38f-18e05ea0fe02 | -14.7389 | -46.0138 | 2025-10-07 10:50:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 105.1 |
| cb9bde23-7ca7-3a10-95aa-16d1b791b8c1 | -12.6159 | -44.7519 | 2025-10-07 10:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 662272e8-ea4c-38f9-ae19-79f92189ba4b | -12.3796 | -47.1633 | 2025-10-07 10:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 271.1 |
| 662d129f-9007-3616-ade6-4ddb410d6d57 | -10.9116 | -47.0682 | 2025-10-07 10:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| b2a562ac-0254-3790-b445-5e43b2ca7111 | -12.3984 | -47.1831 | 2025-10-07 10:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 183.2 |
| dff1cb54-15b9-3e5e-baa3-2270b9847f80 | -10.9307 | -47.0658 | 2025-10-07 10:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 426550ce-0da0-3a9a-b835-d9534fb6b427 | -14.9228 | -51.4076 | 2025-10-07 10:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 967af533-3c03-3645-84bf-850d9e562dba | -10.4245 | -45.3907 | 2025-10-07 10:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 0e2999ef-4de7-3871-a9fc-7343481a4509 | -14.9418 | -51.4264 | 2025-10-07 11:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 193eff88-25b8-3e54-9a04-3d0c3cd24aed | -14.7389 | -46.0138 | 2025-10-07 11:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 0a79e82f-cd0b-3a3d-8f62-5c082ec46e83 | -12.3796 | -47.1633 | 2025-10-07 11:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 29ffb414-109d-3bd1-bbe9-ba2cc9bc6f1e | -14.758 | -46.0335 | 2025-10-07 11:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 78.1 |
| ab386a04-2a00-3d21-9c89-da1d667a843a | -14.9228 | -51.4076 | 2025-10-07 11:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 237.1 |
| 788aae6c-e287-395c-9f77-b6dbd0c35f4a | -10.4245 | -45.3907 | 2025-10-07 11:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 26771d59-499c-38d9-bf97-c9c3bafc363c | -12.6159 | -44.7519 | 2025-10-07 11:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| cd7e143d-fc71-3dc2-b2a6-14bb8546f2bf | -14.9224 | -51.4292 | 2025-10-07 11:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 248.9 |
| 78333db5-befb-343c-8755-61faf8da23a3 | -14.7585 | -46.0104 | 2025-10-07 11:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 89.4 |
| f541895d-0d39-373d-9967-6e52d652ea1c | -14.2953 | -45.8382 | 2025-10-07 11:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 198.9 |
| 03a374df-c3b5-3863-928a-3bf13e721d28 | -10.4245 | -45.3907 | 2025-10-07 11:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 7216c84e-f79d-3127-88cf-1aeb2a8d2191 | -14.9228 | -51.4076 | 2025-10-07 11:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 286baef1-1be4-3c12-9a35-f3818aae8008 | -17.3531 | -46.8306 | 2025-10-07 11:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 63c48d20-5224-3d08-8012-151943642c84 | -14.9224 | -51.4292 | 2025-10-07 11:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 835006dc-ad4a-358c-82c1-3d86ce3119c5 | -14.7389 | -46.0138 | 2025-10-07 11:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 113.6 |
| edd105db-8e4e-333c-99a2-9eb6933464db | -10.9307 | -47.0658 | 2025-10-07 11:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 82cd5eba-fa31-3605-8a1b-7e9403c46c5b | -10.1573 | -45.4701 | 2025-10-07 11:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 101.1 |
| e2aee2ee-5376-32e3-83db-d3d64509e031 | -14.9418 | -51.4264 | 2025-10-07 11:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| c4106877-6eca-3df5-bbf9-b13406070a21 | -14.2949 | -45.8613 | 2025-10-07 11:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| ee0348b0-4c68-36c3-b23f-761ad9c48274 | -12.3796 | -47.1633 | 2025-10-07 11:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 185.9 |
| f76f933f-eccd-349f-bb2c-fd7ea6faf58c | -11.8447 | -44.9176 | 2025-10-07 11:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| eca0273f-e1bb-36c3-958e-c2af10f73575 | -14.7384 | -46.037 | 2025-10-07 11:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 5a0d611d-4e4e-3cae-a698-87f0b8a02b72 | -10.1753 | -45.5363 | 2025-10-07 11:20:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 53c64c45-1d47-3c96-b726-4ff11257130d | -11.8447 | -44.9176 | 2025-10-07 11:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 750c89c6-f780-3387-915c-24892cbd1b6d | -14.9228 | -51.4076 | 2025-10-07 11:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 6bf3d6c6-e817-355a-bfc5-0edc3d144be7 | -13.3899 | -47.5984 | 2025-10-07 11:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 51ccab0a-1d78-3adc-aed3-d4d1b09eda5f | -12.3796 | -47.1633 | 2025-10-07 11:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| bf2faf40-22da-3c88-aca8-253c7c9cc341 | -14.758 | -46.0335 | 2025-10-07 11:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 0bb93658-c52b-308e-b1af-a266c2bd58f4 | -10.1943 | -45.5339 | 2025-10-07 11:20:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |


[Clique aqui para ver as próximas entradas](README111.md)
