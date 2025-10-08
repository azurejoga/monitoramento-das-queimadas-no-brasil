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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34561ba5-0361-3091-896f-0a375f78267f | -20.18591 | -43.93772 | 2025-10-08 04:42:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 79ad2527-0d18-310b-a2f8-4344c4adfafb | -22.30637 | -49.92115 | 2025-10-08 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 195bcf5d-5a77-3cef-99d8-411ce61ecb5c | -20.17045 | -42.20525 | 2025-10-08 04:42:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| eab7bcdf-133f-389b-8f0b-c85daceb5b51 | -19.83209 | -46.16846 | 2025-10-08 04:42:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 35012e4e-9a3c-3a4f-b7ed-f236065cadad | -17.9371 | -57.50586 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 96c7f6b3-b066-3a51-a2ba-dccccb30645c | -20.58091 | -46.34966 | 2025-10-08 04:42:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18cd05e1-90bb-3db4-bd5e-e9ef91986afc | -17.89631 | -57.65715 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 74a0c706-eab7-3f7a-8c4a-2d5aa597f369 | -19.84863 | -46.16136 | 2025-10-08 04:42:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a46f50d-e1fe-3cff-bfe3-b68d8507cbec | -17.82161 | -57.61016 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 684efbdf-bcb1-3ddd-864b-c829fd894c28 | -17.94938 | -57.50808 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| cb78ad49-7abe-3d80-8ecf-f572a232531c | -17.96136 | -57.5059 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 879c57b1-68a3-3882-9264-1d099bca4978 | -20.39203 | -43.07243 | 2025-10-08 04:42:00 | NOAA-20 | ACAIACA | MINAS GERAIS | Brasil | 3100401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ecabd097-2801-316e-a17b-3ce0c9f2bdc7 | -22.10972 | -45.25659 | 2025-10-08 04:42:00 | NOAA-20 | OLÍMPIO NORONHA | MINAS GERAIS | Brasil | 3145505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8e47498b-fd87-3cae-96ab-391f3c013026 | -17.99756 | -57.49344 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0e00369c-91e7-3394-b32e-eb4b9ab0ad3a | -22.01512 | -49.71041 | 2025-10-08 04:42:00 | NOAA-20 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| bf5f4713-4562-3a85-a62b-8542b0f92747 | -19.82671 | -46.16203 | 2025-10-08 04:42:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2275a3fb-ce5a-31db-ad4c-670481fcca30 | -17.93111 | -57.51534 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| b45848ae-2aaf-3504-90a8-0a4191c20b21 | -17.82573 | -57.61095 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 49f64c05-c083-3860-b811-1dffadbba1fa | -18.0036 | -57.57433 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8a05fe49-dd5b-3448-b1c4-fbd5b36d600d | -17.82845 | -57.61937 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e0582ca7-0668-3718-b286-643f7c4f1093 | -21.33625 | -55.63 | 2025-10-08 04:42:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 307e8723-ce05-36f2-9f8e-a6695af72b63 | -17.8595 | -57.58033 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| fe47029f-23a6-3a95-94a5-6bb5b31c1720 | -17.93301 | -57.50508 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ef101dd7-9ba3-39af-877b-c21bbbae615c | -17.82864 | -57.63045 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 8df7b12d-7758-3479-9a1c-f04df067330e | -17.82798 | -57.63388 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 00c14505-7229-36a9-a955-fbb86e1f20f8 | -22.1107 | -45.24759 | 2025-10-08 04:42:00 | NOAA-20 | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| bdc57ef6-55c8-3409-a864-cb859f77576b | -20.16549 | -54.43643 | 2025-10-08 04:42:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 95a83529-bdb8-3852-b498-8edd92e96691 | -17.85323 | -57.59093 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| cbdf94c3-6bd2-356c-a99a-9ffb32d51353 | -19.84813 | -46.16557 | 2025-10-08 04:42:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4207e9d4-0cad-3ee4-9558-b72b6bd7dc46 | -17.99952 | -57.57343 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9b6a0630-c600-3c6b-a2ee-2034cf199b9b | -17.82798 | -57.64506 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| d675035d-6d56-3cc2-84d5-962ea22eb3ea | -22.01091 | -49.71425 | 2025-10-08 04:42:00 | NOAA-20 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 84ea76a9-460f-3ba9-8b81-4d9b85588586 | -17.96204 | -57.50235 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 31a36bea-6699-3369-8492-47c2dcb30661 | -17.94528 | -57.50739 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d96de327-93b1-328a-8554-43446e866913 | -22.37719 | -49.98008 | 2025-10-08 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 35fc79b5-4d4b-3a61-a2e6-f8cbbf0836ba | -20.16892 | -42.20332 | 2025-10-08 04:42:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1a582830-340a-3ef5-9c35-6ddaa1d6c759 | -21.35356 | -45.4188 | 2025-10-08 04:42:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c806a6e1-436e-37e3-a952-82cc46d1ed99 | -20.19971 | -43.95092 | 2025-10-08 04:42:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 80c5be11-d8c2-37d2-a158-bc04f2c30406 | -20.28932 | -48.51344 | 2025-10-08 04:42:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d33c427-dce5-35ce-a6d2-de4c74d2c43f | -22.39564 | -49.97859 | 2025-10-08 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 440a8871-dee4-38aa-a677-b205e7ff19cd | -20.39092 | -43.07281 | 2025-10-08 04:42:00 | NOAA-20 | ACAIACA | MINAS GERAIS | Brasil | 3100401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 18920bca-f4c0-35c9-abfa-7288ddddbbd8 | -17.84706 | -57.64603 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3c2600ae-9d66-351f-b95f-a0e7527cac8a | -22.3992 | -49.97919 | 2025-10-08 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0d07078e-ed6f-3053-b739-ce6ccf499fe6 | -17.93049 | -57.51865 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 43f4e78d-24d7-3ea7-a414-433fb47b6a4f | -19.85293 | -46.16196 | 2025-10-08 04:42:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a48c97d2-d3bf-3041-abbd-3fa096716b39 | -19.84764 | -46.16959 | 2025-10-08 04:42:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c041e91f-0d7d-347d-b326-3c71f09bc905 | -18.04166 | -57.52906 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8693bffb-8f8e-3599-8e36-42c3862bb119 | -20.2656 | -43.26094 | 2025-10-08 04:42:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| bd61eb1a-5ead-34f4-b314-364d87a93fa3 | -17.82515 | -57.63726 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.1 |
| a3f9dbe1-de13-32ab-beed-7e0b0eaf42e7 | -18.05111 | -57.52374 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5deef79a-9dc4-3635-a89c-e0be18a8cd0d | -18.03752 | -57.52859 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4e870c0e-616f-311e-a424-5a8db361e6f1 | -17.95001 | -57.50466 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9fdd2214-925b-394f-be6d-d8f72f3c5d02 | -17.93173 | -57.51198 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 8d0b1cae-2f00-3655-b712-aac475c1963d | -20.28557 | -48.51288 | 2025-10-08 04:42:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c2d19f1-1891-34bc-b2a4-12cdfdfd54d0 | -17.82578 | -57.63387 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2eb4f6c4-a274-3586-a529-17bae3399160 | -18.04991 | -57.55315 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| c08add6c-f5ee-33f2-bf96-313c59c985a3 | -18.05403 | -57.53075 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 9672072e-c529-3739-b32e-b79ee026fffe | -17.92704 | -57.51443 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 9b945297-fed5-3716-b99f-d835413e22b5 | -17.82588 | -57.62248 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 33aef2f4-84c5-3a3f-be4e-9958ce8a6680 | -22.28724 | -49.92745 | 2025-10-08 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d8f97488-c002-3394-b985-193245e17d64 | -20.49887 | -45.94786 | 2025-10-08 04:42:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbe1f91f-c88d-3715-ae4e-22df56560a04 | -17.82667 | -57.64076 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.3 |
| 46282b81-dc0f-3881-87a3-f724763a8963 | -18.05521 | -57.52441 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 3796a979-f04a-37cd-aef5-f05122a62cd5 | -17.94118 | -57.52964 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| a989c4b6-a925-38e1-9b61-36fe4c40eff7 | -20.19452 | -43.95124 | 2025-10-08 04:42:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2d22dce2-bde3-3022-995d-16d5d6171801 | -20.63281 | -54.75002 | 2025-10-08 04:42:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ae7b2b5-4339-30b7-a149-b12994160ed5 | -22.39378 | -50.01841 | 2025-10-08 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 04ee6894-7847-38e6-86ba-b2b08b34cc22 | -17.93315 | -57.52719 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 94339bd5-afc5-3d06-88e9-41f4a54fa101 | -18.01889 | -57.56056 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1d2102fe-85d2-34da-a3b1-8a3ad358154f | -18.05681 | -57.53865 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 000922f1-5401-3c88-95c8-41ac96342318 | -18.04594 | -57.55169 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| b6421759-13c8-38ac-a5e7-ed3fad867912 | -22.3885 | -49.97745 | 2025-10-08 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d9765dbf-097e-34b0-860a-f95f9d4fa208 | -20.20384 | -43.95837 | 2025-10-08 04:42:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 39b0d557-c30f-35b7-8511-3cc053e35829 | -18.05277 | -57.53756 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 360b4eba-3d5e-3e11-8d78-608867b8a5d9 | -20.12153 | -44.41957 | 2025-10-08 04:42:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ce4419d0-f68b-3d75-a045-34bfd22e004b | -17.82993 | -57.63449 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7c722993-9adc-360f-96e2-c036cb59385d | -17.84754 | -57.59845 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b5537ee8-e8c9-3db0-be1d-786d4b16b92e | -17.8308 | -57.64155 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 48881569-1e70-3791-82b6-d673476ce57b | -17.97567 | -57.49741 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1e42b7ca-5580-3a72-8776-349e09ef8792 | -22.01034 | -51.89513 | 2025-10-08 04:42:00 | NOAA-20 | PIQUEROBI | SÃO PAULO | Brasil | 3538303 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| ca995ace-8ed0-3176-846f-75d05cc34646 | -22.38492 | -49.97691 | 2025-10-08 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 930345ec-a9bf-3ee8-a4e2-46c662780371 | -17.86084 | -57.64103 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f9b23123-6b5a-30ed-853d-7f0cd796b077 | -20.19953 | -43.95171 | 2025-10-08 04:42:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 6c777e95-f2e1-3e1f-9a96-80a837767751 | -20.20472 | -43.95135 | 2025-10-08 04:42:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 6618fbeb-edf1-3140-8c17-ad0ee15dec9a | -18.05808 | -57.53172 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 8315b8bb-39d5-3e31-b9b5-04ef9c3224a2 | -19.47307 | -55.47927 | 2025-10-08 04:42:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| ddb9ae38-4c3f-394c-bfb6-458e93351df6 | -19.82571 | -46.17043 | 2025-10-08 04:42:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 18a46115-b65a-3e84-9444-1a820e5e26af | -17.97638 | -57.49365 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8436452e-493e-34c1-acbf-192440b4e9bf | -18.05076 | -57.54848 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 73c74605-d247-3314-8673-224af4646c22 | -18.01915 | -57.51361 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e7f44fa6-8661-3503-bb69-a065866cf778 | -17.86576 | -57.63763 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3cb3a1e0-fe21-321b-8704-6de5eba17476 | -20.168 | -42.21299 | 2025-10-08 04:42:00 | NOAA-20 | CAPUTIRA | MINAS GERAIS | Brasil | 3112901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 6026ca8c-db63-39aa-a795-b28106bce06e | -21.01708 | -50.6944 | 2025-10-08 04:42:00 | NOAA-20 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2457f464-3b3c-3ef2-aab3-a03e16c4602c | -17.86984 | -57.63866 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0120c503-d1cb-3f27-b219-af5b483bf925 | -22.38311 | -50.01653 | 2025-10-08 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| afb5f4a9-b76b-3d78-acb5-94ded17d2106 | -22.31352 | -49.92234 | 2025-10-08 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b3901313-4910-385f-8481-50384af0275c | -19.82729 | -46.1719 | 2025-10-08 04:42:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9d09c550-5ea1-3fb4-8811-8c5db3b2a417 | -17.96613 | -57.50309 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 96a2ddba-8a97-38a6-83f8-dc558aec7e4a | -17.84829 | -57.59448 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 191320f8-e474-3872-bba1-8d268ce139f6 | -18.03476 | -57.52068 | 2025-10-08 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |


[Clique aqui para ver as próximas entradas](README87.md)
