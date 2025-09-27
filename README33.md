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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0881183e-6781-3a45-b086-99804bbafd57 | -12.05555 | -47.6561 | 2025-09-27 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 702943e1-9961-3fe7-bda9-263362d48bf6 | -9.98264 | -43.58293 | 2025-09-27 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 934af881-2883-3717-abdc-f96cbeb87b8b | -11.77375 | -43.76205 | 2025-09-27 04:23:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05711e4b-fdfe-37f3-89ae-197c074aa0e0 | -11.43054 | -45.01076 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83e5a796-bea4-35d4-b7eb-bfc50e982c6f | -12.03731 | -47.05936 | 2025-09-27 04:23:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7a5d066-5bdf-39b3-adbb-8788dfb16ca3 | -12.98755 | -47.10142 | 2025-09-27 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 62a6ba9f-ccc1-3140-a4b8-56a053e4c421 | -11.40883 | -43.50653 | 2025-09-27 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c83f432-6452-3230-a2a7-143760e19cc2 | -7.86727 | -45.29123 | 2025-09-27 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6cfc430-53db-3ee1-93e8-50705afae340 | -8.51229 | -44.61314 | 2025-09-27 04:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d087a11-d047-3775-a4a6-a6d299900439 | -10.57003 | -44.07259 | 2025-09-27 04:23:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 062e52ee-0a8d-35e7-b5e7-85296fab5a01 | -11.44697 | -48.5263 | 2025-09-27 04:23:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e3717764-d48a-3837-90c7-2bb3a0a352a1 | -7.6505 | -43.82613 | 2025-09-27 04:23:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a7489f9-ec2e-3b87-beeb-07a6bc01b9f8 | -12.36349 | -44.14814 | 2025-09-27 04:23:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb31e8e7-6f53-363d-bb43-850703dc5237 | -12.27594 | -44.06099 | 2025-09-27 04:23:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 705e0d70-64e8-3fcd-a0a2-3575f2ecf9d7 | -8.66157 | -43.99222 | 2025-09-27 04:23:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5a55ecd-bde3-306b-829c-e5368c81d583 | -10.18177 | -44.872 | 2025-09-27 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0e158a3-723b-3e72-a25f-c49ade177eca | -13.04657 | -47.06683 | 2025-09-27 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 19eec2bf-523a-39fe-a9c5-99b959cdb08c | -11.82967 | -46.62014 | 2025-09-27 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bbd25334-a9ec-3cfb-b99b-74dd851b746f | -12.96403 | -48.91023 | 2025-09-27 04:23:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 289cf396-54eb-3566-bf3a-fe52e1f4ad1e | -9.84302 | -49.29891 | 2025-09-27 04:23:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70106bb5-b61d-3d06-a6b9-8a37302faaab | -8.84108 | -46.21159 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 56e68238-b45a-3bb2-a0ad-c97f70fd6256 | -11.69707 | -44.45104 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b21de6b-a05c-3de6-8ab4-67fbc6506e1e | -8.83325 | -46.21755 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8072e824-5a57-3842-8d91-994c94fd9fd6 | -12.61924 | -48.14 | 2025-09-27 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6753054b-e5f8-31f8-8a9a-0d462c155d61 | -11.29359 | -47.81208 | 2025-09-27 04:23:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59354bb5-9627-3300-8b13-56e084fab244 | -12.27709 | -44.05338 | 2025-09-27 04:23:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb1801d6-57a9-3dcf-8c66-3b1de7e3105b | -8.36952 | -41.40164 | 2025-09-27 04:23:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 66b05c27-c1f2-3606-85da-bbdd6697fce0 | -10.11789 | -45.34566 | 2025-09-27 04:23:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33e24c56-f984-3c65-90ce-9c33c8f880e8 | -12.02942 | -47.06546 | 2025-09-27 04:23:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe31c1be-a56f-34ea-9426-72d14a9011bb | -8.26152 | -44.93926 | 2025-09-27 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ebf7f860-100f-304b-a210-fde59814f419 | -10.02988 | -45.41072 | 2025-09-27 04:23:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b05eb42-a674-3b8a-9560-965eeb312a0b | -9.16862 | -46.63171 | 2025-09-27 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e2bdac1-b4e8-3ab2-acd3-046b7051868a | -12.65191 | -51.68364 | 2025-09-27 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de0fc60d-2dc0-3484-8d6f-dbbfe62c2a78 | -11.3845 | -45.0293 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6204add2-8941-3acf-8ec2-95c33da02977 | -12.29343 | -45.65427 | 2025-09-27 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6775c7a0-7b35-354f-9619-cd360348697d | -12.30825 | -44.35135 | 2025-09-27 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 007eef19-4d9f-3cd4-b3af-7b417bd3f850 | -10.7972 | -45.37167 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74102224-a071-3b96-afdc-b3a8c141e2f8 | -8.12441 | -44.12598 | 2025-09-27 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f3bb5e0-a99c-3e04-aaef-8ab24fc5dd5e | -11.36439 | -45.00417 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17dbdbcf-79af-3338-853b-fc7b2fa1eafe | -8.72091 | -47.98369 | 2025-09-27 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75310e66-f3ad-3294-a398-bd88951831ef | -11.68404 | -44.42261 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e9edeed-ff1e-3cde-96ca-03c2734820a2 | -7.3758 | -47.02739 | 2025-09-27 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 99910c70-32c4-3f06-a62c-cecfb4acbd26 | -11.91238 | -44.80202 | 2025-09-27 04:23:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14700b12-346b-300d-9302-cd996f418519 | -11.97233 | -46.59658 | 2025-09-27 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7addd36-0da3-3f76-94d8-3a019478708d | -12.65394 | -51.67223 | 2025-09-27 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6dde85c7-c88c-3158-b07f-0b879ebb75df | -8.52622 | -44.63333 | 2025-09-27 04:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee272b68-9189-3565-b348-74a17ce75305 | -11.43664 | -44.9712 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2f6db10b-c765-30c2-b1af-6f56a95b03fb | -11.35103 | -45.02397 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b32068c-afa6-3812-982e-1da4f5084425 | -9.05418 | -45.50948 | 2025-09-27 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c0c6857-b317-34e0-a822-f2fa084e7939 | -11.54232 | -46.95155 | 2025-09-27 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9892550e-e647-3fed-9d91-8686328a3365 | -11.43039 | -44.92252 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19888825-0a28-3a70-b118-686cbb245157 | -9.87277 | -45.90684 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aec850a0-f415-3d82-8eba-448e43d66659 | -10.18186 | -46.93372 | 2025-09-27 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21f55a3e-274e-350b-a2c8-80ef3cd3a552 | -10.11342 | -45.30901 | 2025-09-27 04:23:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1098f58b-6420-3a59-8807-b1316242bff5 | -11.43552 | -44.97844 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ff66748-e8f6-374a-815f-59f946664b8f | -8.05707 | -48.16138 | 2025-09-27 04:23:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e873c65e-ec2e-3adf-9d9d-97b84ce50e95 | -11.57405 | -50.21121 | 2025-09-27 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d795068e-aefe-3832-b8d1-a461b395e537 | -12.98813 | -47.09784 | 2025-09-27 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5c1d0db8-1584-3cd1-beb8-3c2f295c8a19 | -10.28641 | -45.2211 | 2025-09-27 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 03fd82a4-913d-3021-8ea7-bf11034b205f | -11.02193 | -44.64518 | 2025-09-27 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33e8f67c-0198-3fc7-a3a3-b12849c52eb3 | -11.04273 | -51.55798 | 2025-09-27 04:23:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 567c8b31-ae24-3431-afa4-8550d4db7e55 | -9.674 | -46.33156 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0393446b-e253-3393-8099-8e6bd003e1bc | -12.64914 | -51.67514 | 2025-09-27 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a17afd1-ecf9-3538-a1de-e50e5f92bb20 | -10.40158 | -46.1366 | 2025-09-27 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8bbbc49-f3ab-3b18-86de-5641385ecbe6 | -11.35603 | -45.01381 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f63f7efc-858b-35cb-9545-b1cb6d55d10d | -9.1663 | -46.64614 | 2025-09-27 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42ba1cf0-90ca-3d3f-8a66-284d3b0cded2 | -9.98092 | -43.57106 | 2025-09-27 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 05a430cb-cc3a-31bb-8f32-3966f2d7a5d4 | -10.39881 | -46.13253 | 2025-09-27 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d6e8c6b-6dea-3f5c-ab6f-5cd1812de9f6 | -11.97547 | -47.90862 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f405fd06-49c0-3b71-8e50-d59383e82e06 | -11.4191 | -44.96141 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb999d14-83e8-330c-bb28-4ada948a3b67 | -8.83381 | -46.214 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65003b4d-7699-3ea6-bc88-8a11775caefb | -11.35714 | -45.00667 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 430a4a8c-fe46-37e1-8ad5-f2dadc751da2 | -11.35324 | -45.0097 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 049dcdb0-056e-3dd5-9648-f38aea58825d | -10.29085 | -45.2146 | 2025-09-27 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5aeee4d1-d7d0-3435-b217-a9ae133efae0 | -9.75798 | -46.14148 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48eaac0c-ee44-3368-9ccd-aa702fc1cdb4 | -12.284 | -44.05442 | 2025-09-27 04:23:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e96cde0f-87b0-39f0-89fa-1c01027b5fdb | -11.97578 | -47.88529 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3aefde98-b066-3bd2-8d79-e40c0b305c4e | -12.05275 | -47.6518 | 2025-09-27 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2c7957f-ffc8-3f3a-831b-b3b53fefbb81 | -10.60118 | -49.64017 | 2025-09-27 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4642b7d3-d2e6-334c-bda6-d32fcf75a181 | -11.97672 | -47.90104 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bc5f45ed-c1b6-3b22-87c2-01c440525065 | -11.6914 | -44.41999 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7207253-067b-3f8b-b919-5935d94d1bd8 | -8.83257 | -46.26492 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0999ff77-99c3-3289-be18-39b2cc8a32c2 | -11.54132 | -46.94794 | 2025-09-27 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fc48b11-4789-3150-99b8-a5ffe3fa2d8f | -11.50185 | -43.53646 | 2025-09-27 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab2e0522-3303-380d-8fb2-688d60155d78 | -11.04208 | -45.87576 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61e6a9df-6fd7-3ed5-9c25-d8ee07d197a4 | -11.6965 | -44.40947 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4522a7ef-a5ef-3390-8ac4-7f173eb3d8f1 | -7.87998 | -44.02954 | 2025-09-27 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9bd7af6-9713-344b-b3b4-3be9659d5f1f | -9.09727 | -48.90828 | 2025-09-27 04:23:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2c651114-5e3f-3aab-8fbd-d2dfeb4c0ad4 | -10.19621 | -44.84524 | 2025-09-27 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e014ca21-8322-32df-a12b-5bd0448cfb18 | -11.97299 | -47.88086 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa5eb1a1-3cab-3784-b777-a391c94f02c6 | -12.5517 | -45.84453 | 2025-09-27 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a956c9bb-7ec1-3379-a2c2-59a40035e677 | -12.22966 | -47.18736 | 2025-09-27 04:23:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6b6862f7-35d9-3e86-9f8f-3e37ad4416f1 | -10.94273 | -44.30215 | 2025-09-27 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa29c34e-87fc-38bc-8801-549cffab0565 | -13.18923 | -47.4286 | 2025-09-27 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8ea7e35-a0e6-3af1-bd7b-15178d6319d4 | -10.40102 | -46.14013 | 2025-09-27 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dfac0a01-08e1-3d25-88fe-f648eb8c3a2e | -9.97746 | -43.59374 | 2025-09-27 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f04ce687-f80e-3d3b-8037-35eda61390d7 | -8.86743 | -47.81862 | 2025-09-27 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30eea868-2bbf-3a08-aa29-6add1de1e793 | -10.10066 | -45.30336 | 2025-09-27 04:23:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2251d49c-970a-3143-b41f-f3a0d24b8786 | -13.18308 | -47.42383 | 2025-09-27 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97bda867-eac6-33f4-87be-498a6f79e6c3 | -10.40379 | -46.14421 | 2025-09-27 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README34.md)
