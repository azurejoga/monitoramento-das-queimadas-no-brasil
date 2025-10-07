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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d960c87-3a19-3484-bb9e-ae5bead9bf33 | -20.10266 | -44.19074 | 2025-10-07 04:40:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e0699a4d-ae4d-3cf2-bcbb-27b4fe2a3c0c | -18.16722 | -53.37963 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e8d96125-77c8-3273-8d9a-fda603333c66 | -23.31849 | -45.75604 | 2025-10-07 04:40:00 | NPP-375D | JAMBEIRO | SÃO PAULO | Brasil | 3524907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 4a43a01f-76c8-3794-b808-2e9c20c891e8 | -19.38469 | -47.42675 | 2025-10-07 04:40:00 | NPP-375D | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eb7b63f4-a39d-338c-b47c-c2b431f8e7cc | -18.15379 | -53.39405 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c4c1666-5b9b-31f5-afd5-3ea04d223d6d | -18.15311 | -53.37685 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e893bdfb-ca11-3557-a256-8f06f970b601 | -20.07848 | -49.59949 | 2025-10-07 04:40:00 | NPP-375D | RIOLÂNDIA | SÃO PAULO | Brasil | 3544202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| cc7034db-e826-342d-8b76-9727a8a8f172 | -22.55461 | -44.45109 | 2025-10-07 04:40:00 | NPP-375D | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f1d0e192-7629-3355-9259-e6e698928302 | -21.90227 | -44.87965 | 2025-10-07 04:40:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e65b1f9d-4928-3649-aa69-f24278fa3bdf | -21.48957 | -46.91321 | 2025-10-07 04:40:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5645225f-4e26-38f7-9530-cbbd22770f17 | -23.14716 | -46.67261 | 2025-10-07 04:40:00 | NPP-375D | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 046b6961-9a1e-363c-9d8c-ed432df47b51 | -19.87984 | -46.73569 | 2025-10-07 04:40:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f34f55d8-da3c-3544-b678-abd26f80ac63 | -20.07906 | -49.59565 | 2025-10-07 04:40:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.9 |
| 8ade6250-e2dd-364c-8057-dd5ee24cc91c | -19.09021 | -48.98962 | 2025-10-07 04:40:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 404f3d17-1c12-3d13-ba14-b3d7c7beea1c | -18.17705 | -53.38605 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1558986f-4e54-3ffd-b53f-7a11d55f4f7c | -19.02797 | -44.7334 | 2025-10-07 04:40:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c8a727a3-173b-36f0-80b7-dd7467ac063a | -18.28442 | -53.32793 | 2025-10-07 04:40:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2b77ffa-48cb-3da4-afaf-893f4f529335 | -18.84311 | -48.29305 | 2025-10-07 04:40:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5b0cc26-d959-3be6-bc3d-4e28a8583f28 | -19.93229 | -46.72337 | 2025-10-07 04:40:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 653b4a41-d496-38df-8071-d97746959e64 | -22.90581 | -45.58624 | 2025-10-07 04:40:00 | NPP-375D | TREMEMBÉ | SÃO PAULO | Brasil | 3554805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e548dc37-e3a9-391b-8d6e-c11ea2c31628 | -20.20321 | -43.92377 | 2025-10-07 04:40:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f2cdd153-68ba-351a-a99f-3b5d9f130c68 | -23.09959 | -46.1911 | 2025-10-07 04:40:00 | NPP-375D | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 04fc3711-48fa-37f1-959a-4a0c6689a339 | -20.09656 | -44.20395 | 2025-10-07 04:40:00 | NPP-375D | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 786593e2-872c-3740-9642-331a7288135e | -22.15707 | -49.38398 | 2025-10-07 04:40:00 | NPP-375D | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 487b2722-3c10-3116-9fdb-f176c376a5d5 | -22.15825 | -49.37584 | 2025-10-07 04:40:00 | NPP-375D | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff2cd376-82fc-3b11-94df-41a53d46eaed | -20.32619 | -45.11581 | 2025-10-07 04:40:00 | NPP-375D | PEDRA DO INDAIÁ | MINAS GERAIS | Brasil | 3148905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3796b41a-2305-3f3d-b963-2412738f62a1 | -21.18851 | -45.61629 | 2025-10-07 04:40:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efeaa20e-97ed-3634-8134-6cab83f50f93 | -21.48287 | -46.71613 | 2025-10-07 04:40:00 | NPP-375D | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a0e3b7c4-1816-34ef-a07e-a43b7b69d2d1 | -22.17038 | -49.39027 | 2025-10-07 04:40:00 | NPP-375D | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f51bd65f-ca62-3e78-97c7-c50971d90a13 | -22.0939 | -44.79526 | 2025-10-07 04:40:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0edd35c2-3a67-38e0-bf3d-497c3f9e0cc4 | -22.16054 | -49.38456 | 2025-10-07 04:40:00 | NPP-375D | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0af4c7f7-2e76-305e-bafd-63e1bdb7ad87 | -18.16383 | -53.3569 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c21caa55-8023-3bad-b25b-85ba69904da0 | -18.15887 | -53.36457 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 38959b39-0ba8-3da0-b8d6-8cec86487f74 | -20.07963 | -49.59182 | 2025-10-07 04:40:00 | NPP-375D | RIOLÂNDIA | SÃO PAULO | Brasil | 3544202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.9 |
| 7e0f309b-42e8-35b7-a572-8fe8ae61440e | -21.61006 | -43.99643 | 2025-10-07 04:40:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 1c7bedd7-915b-3e23-b4fb-77bfbc3d188c | -19.79141 | -45.84668 | 2025-10-07 04:40:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 650180a6-46ec-3824-a75d-1acaecd4aaa7 | -19.80564 | -46.05511 | 2025-10-07 04:40:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34cf81cc-026d-348f-8b8b-c7839a767a6f | -21.08086 | -46.9086 | 2025-10-07 04:40:00 | NPP-375D | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a36622b8-1521-3c9b-a2cd-40f06db1a6d8 | -19.68796 | -45.98178 | 2025-10-07 04:40:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 640fb7bb-bb72-3cd9-a3ac-4a7b7b7e23ac | -18.14889 | -53.38018 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02f88ff2-7443-399e-a62c-7fa3ea63c4a6 | -18.92799 | -49.48964 | 2025-10-07 04:40:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26109b6b-731c-3e8a-b3b8-03a7d710a439 | -23.31711 | -45.75493 | 2025-10-07 04:40:00 | NPP-375D | JAMBEIRO | SÃO PAULO | Brasil | 3524907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fa650d52-4544-3698-84ef-9401c077b2e8 | -20.19131 | -45.4171 | 2025-10-07 04:40:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a7d71731-5d6d-3f28-ac19-fe9026a23f8c | -21.1045 | -44.21499 | 2025-10-07 04:40:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9d769dc1-78bb-3ffc-b940-d2cd6ccd0caa | -21.5205 | -45.5975 | 2025-10-07 04:40:00 | NPP-375D | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 1e274de9-54bf-3cfa-af5b-a7ef134afcfe | -22.31744 | -42.5358 | 2025-10-07 04:40:00 | NPP-375D | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 38ae0c32-0207-39f4-a776-045896c7b1d7 | -18.97119 | -47.83127 | 2025-10-07 04:40:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6900269f-ab38-32e2-a52e-50038eda161a | -19.3916 | -45.9117 | 2025-10-07 04:40:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96f696fd-b260-3295-ab16-c6ca9a7b56dd | -22.16691 | -49.38973 | 2025-10-07 04:40:00 | NPP-375D | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44e1fd20-1b46-38f9-aacf-d6650a87aba4 | -18.11448 | -53.34746 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3e191827-6563-3b41-99b1-75729c941bb0 | -18.10621 | -53.35654 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed9e9419-dce1-369d-974f-e92c65feb4bb | -20.05874 | -49.54504 | 2025-10-07 04:40:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| fc1a9cc4-7cb2-3cbc-966a-91264fdf96f9 | -22.54444 | -44.459 | 2025-10-07 04:40:00 | NPP-375D | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 21.6 |
| 3ed86f81-d16d-3d25-bd29-16d7de351ae7 | -18.10588 | -53.35493 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc8c2cf2-6a01-319b-be31-6ac9978ce8c9 | -22.17561 | -49.37871 | 2025-10-07 04:40:00 | NPP-375D | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4aa9d993-960e-376d-ad07-e05c634ef1d9 | -18.11018 | -53.35118 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7e12cf04-0803-3a64-9341-e1e7af11fe6f | -18.92518 | -49.48531 | 2025-10-07 04:40:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| dbf904bf-d147-34d0-9e02-d30cd064b162 | -18.1496 | -53.37605 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b408b30c-eee9-362f-b2eb-cf3618603ed1 | -18.10944 | -53.3554 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3db73484-fd34-31c1-bb12-074d6b58402a | -18.6585 | -48.17876 | 2025-10-07 04:40:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4ea7fcb4-2951-3aa2-8e82-d8ef202dab7f | -18.17075 | -53.38028 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 276ed365-7d7f-3e20-a68b-f32859119b84 | -18.15452 | -53.38982 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1803387d-f3b5-31b0-8cc0-c7413f3e44e1 | -21.22942 | -47.54991 | 2025-10-07 04:40:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fa55a7b-f0bb-35ec-9793-88d46d4efe20 | -18.10439 | -53.36343 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cff3d9a-776c-37f6-bba7-085c44ef71db | -21.90564 | -44.88909 | 2025-10-07 04:40:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 0de1f07b-89c0-3daf-b037-3460b3c0d8f9 | -18.92122 | -49.48856 | 2025-10-07 04:40:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cd8b71b3-0598-3e79-afc5-098449f3bb61 | -22.17503 | -49.38274 | 2025-10-07 04:40:00 | NPP-375D | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c7a57bbe-cd01-3bea-aab0-de910d84136c | -20.2515 | -45.48445 | 2025-10-07 04:40:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2ee31fb2-a41e-3c8d-b6b9-1facd9a511fa | -18.26472 | -53.31579 | 2025-10-07 04:40:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 88a7b7da-4188-3724-87b7-f4cdea14d2c5 | -23.15182 | -46.56841 | 2025-10-07 04:40:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 66192763-9bc6-339b-bcd0-a33e75b13cc3 | -21.49435 | -46.02221 | 2025-10-07 04:40:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 89504136-fc36-3e47-bc56-271f440cc668 | -18.92461 | -49.4891 | 2025-10-07 04:40:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| be67a802-dab5-3625-b21e-0416535f0dff | -18.17922 | -53.37339 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9589e8ae-1e28-394c-a06c-4ca2afadb776 | -18.10721 | -53.36815 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97e81d05-e3b8-3864-9a1a-3029cd6fad47 | -21.61166 | -44.00047 | 2025-10-07 04:40:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| c420792b-9844-36ab-9744-58fdf4172463 | -18.16311 | -53.36107 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 758c93c9-d3f0-3d2d-ae90-10846fca2d05 | -21.76911 | -47.78249 | 2025-10-07 04:40:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 220194d3-4542-3bf8-818c-7bf3269fd926 | -18.13909 | -53.37356 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 717525b2-b306-3b90-850b-58f7b7f5f3e1 | -22.55005 | -44.45037 | 2025-10-07 04:40:00 | NPP-375D | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| 42171524-f796-3c24-925e-734bc1ff64c4 | -18.78007 | -44.62162 | 2025-10-07 04:40:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 92f55652-aa45-3011-898e-02fdeca21df6 | -18.12081 | -53.35292 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 17384861-0f12-3e31-9e8f-b21c7a5a4ca3 | -18.15873 | -53.38654 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0aa1250-e809-3520-b6f7-0cb231e7859e | -20.11333 | -44.40979 | 2025-10-07 04:40:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 28685444-0697-3c5e-86c2-fd2d40d4cee0 | -20.20783 | -43.92412 | 2025-10-07 04:40:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8f7c88a0-ca89-3ce7-9d45-44cbffd4d3af | -20.9844 | -45.58024 | 2025-10-07 04:40:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3d66778e-d6ee-3c74-84de-1a7b8c0b1bde | -18.97181 | -47.82697 | 2025-10-07 04:40:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f14504c2-133b-32f4-9417-fd06d0860e6e | -22.67286 | -49.19654 | 2025-10-07 04:40:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a8f500ae-97e5-3931-8d88-1a821a165514 | -22.31968 | -47.13248 | 2025-10-07 04:40:00 | NPP-375D | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ea2f4f1d-ed74-3524-98ce-25e7f1002022 | -18.14331 | -53.37024 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e9de260-22c4-3780-9085-fde3aa5b53f0 | -19.93436 | -44.64085 | 2025-10-07 04:40:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a7cff917-df3c-3143-a0dd-38f8172fd0a5 | -18.12154 | -53.34872 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ebab62b-ac43-3dd4-994f-fce57237c924 | -18.14609 | -53.37525 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab544dbe-9d2c-3d88-9136-88d8ce27d5b1 | -22.01467 | -49.55176 | 2025-10-07 04:40:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ce9bed1f-5608-31f1-8c9e-45455b73b2ad | -19.95737 | -44.63275 | 2025-10-07 04:40:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0d1fa80-088f-335b-8994-dc9eaad5b39a | -23.07114 | -45.99802 | 2025-10-07 04:40:00 | NPP-375D | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 073fc72e-7ce0-372b-8482-251b5c6b41ec | -19.63662 | -43.77407 | 2025-10-07 04:40:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 31d65efb-c3a9-3a51-bdd8-e5b8a4308d2c | -18.27248 | -53.33401 | 2025-10-07 04:40:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f6ff98f-b419-30d9-a30a-2024fd8ef74c | -23.0723 | -45.99398 | 2025-10-07 04:40:00 | NPP-375D | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3a558e2e-6c7c-3766-9da3-c23082a2fb2f | -18.10692 | -53.35233 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 513b51bc-6ff0-3a7a-aee8-7a43270d63e0 | -20.09862 | -44.1861 | 2025-10-07 04:40:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README79.md)
