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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4db57aed-cf18-38c1-90e8-78473a6677a9 | -4.71025 | -46.45201 | 2025-11-14 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8916626-1481-3894-88f6-1ff17de3674c | -6.40073 | -46.56262 | 2025-11-14 04:25:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5aa183d0-46f8-3109-a1b7-adb76e278f8b | -6.99709 | -42.78262 | 2025-11-14 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 92397ed5-ac1b-3d2f-b98b-a4d8343795f4 | -5.34553 | -46.76183 | 2025-11-14 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4599d9c0-1ad4-3709-b4ef-7212ee8a3cff | -17.79549 | -44.97938 | 2025-11-14 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 84917a32-1d1e-3d53-9190-3fcde5f068de | -4.97886 | -48.36277 | 2025-11-14 04:25:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c142613-c710-3543-9ff0-9c4447b6892e | -15.55808 | -44.48695 | 2025-11-14 04:25:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ef4df4af-5351-33b2-af97-3e7a80916191 | -12.70538 | -45.42757 | 2025-11-14 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b35e7a21-4ffc-38aa-996b-3882d96c97f8 | -12.71984 | -45.42258 | 2025-11-14 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| c3d08a32-9ee8-3ac1-96ea-b5dee3a04695 | -12.59204 | -48.33571 | 2025-11-14 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b79b2d77-d306-3de6-9396-3ecccd457a55 | -5.33298 | -43.03585 | 2025-11-14 04:25:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff01559e-f933-3485-b8c5-aaf0b927181f | -5.97612 | -42.5968 | 2025-11-14 04:25:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 379d5b3c-65f6-3c48-9d31-3485c762e57d | -16.67961 | -47.70376 | 2025-11-14 04:25:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13765746-8d90-37c1-94bf-5189e353f41a | -4.94087 | -48.54809 | 2025-11-14 04:25:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b439a82-fe95-3a88-819a-1c4167d1214c | -6.13418 | -48.04982 | 2025-11-14 04:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf20944b-9dab-30bc-af9a-42c4b03d726e | -14.69647 | -46.62259 | 2025-11-14 04:25:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 86bf7e7a-7242-3d93-a46f-f7f5ff2e7a88 | -6.21772 | -39.65079 | 2025-11-14 04:25:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e109d025-5ed1-3d9f-a2d6-0f7805c37797 | -11.66422 | -48.46519 | 2025-11-14 04:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96bb9028-37ff-368a-a0ee-bc4bb0a5119c | -4.63943 | -48.75159 | 2025-11-14 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f13844bb-78e9-3af3-8b47-5ccef80696a1 | -5.84753 | -38.39973 | 2025-11-14 04:25:00 | NPP-375D | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5183c37c-5488-390e-bbea-280c767dfd82 | -11.25016 | -47.4978 | 2025-11-14 04:25:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aa829be1-0831-3cb2-b4bb-fbf81919590f | -15.15881 | -43.6081 | 2025-11-14 04:25:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1e1e6119-7da2-3489-b1a1-b73f64ce657a | -6.90001 | -42.09122 | 2025-11-14 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b4e83519-33b6-3f3f-b0c6-2fc1c39ac610 | -15.24578 | -47.94655 | 2025-11-14 04:25:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| beda6988-a41e-365c-ac17-cc32f03be315 | -6.3904 | -42.31557 | 2025-11-14 04:25:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fa71087e-746c-308b-bf51-385a086f0321 | -11.73457 | -44.66661 | 2025-11-14 04:25:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bd1b867-81fa-3aea-8675-a4954f5d7908 | -5.65637 | -41.08276 | 2025-11-14 04:25:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a0fcabb5-2f09-3b35-90ab-0e78b5ec5ebd | -5.65268 | -41.08226 | 2025-11-14 04:25:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aeb02e79-6242-323a-8fde-a30781dadc15 | -10.84871 | -48.02524 | 2025-11-14 04:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41b0c9a6-913a-34d4-856d-4d70fdc54f08 | -16.54535 | -49.35408 | 2025-11-14 04:25:00 | NPP-375D | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d5cf278-a9a5-3763-b1ad-e046e3b08fda | -10.78252 | -47.64091 | 2025-11-14 04:25:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f022d8b7-311e-33e5-af5e-f74c7df1186c | -6.10638 | -41.52798 | 2025-11-14 04:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4768c65b-e449-3288-a48c-34b8d32c1d8c | -4.68472 | -45.85276 | 2025-11-14 04:25:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbcfbe94-49ec-331c-b3bc-35cc2bf444e4 | -6.65194 | -43.53167 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 620c7b58-70b0-39c4-a59e-90434806b71e | -7.05855 | -43.58352 | 2025-11-14 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54e6f005-a6ba-32a2-b3fb-c917e2a3f015 | -6.61536 | -47.63799 | 2025-11-14 04:25:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 715a81fd-4d49-369d-981a-9907fc29069e | -11.85081 | -49.22338 | 2025-11-14 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 38faf1b9-2461-38e9-9219-c2d1eb65050e | -5.52153 | -41.75581 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ea46adec-614b-3e5f-b3b1-aae3ca93406a | -4.62439 | -46.13966 | 2025-11-14 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e29f1205-17ca-3171-a8d4-d53d5c20ad69 | -4.97667 | -43.0994 | 2025-11-14 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5f44971-87cc-372f-bfba-2a74945207be | -17.63103 | -46.70884 | 2025-11-14 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49ea3000-2e56-3be3-811a-264a63d803e2 | -4.97385 | -43.09532 | 2025-11-14 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4852ef13-764b-3ba2-88de-7e5c05f24c75 | -14.03171 | -48.01822 | 2025-11-14 04:25:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b6b63ba-985d-3819-b6b8-8c333e12f4fa | -11.85371 | -49.22831 | 2025-11-14 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 32859144-74b3-33cf-8b5f-46de35e4dc82 | -5.52508 | -41.75634 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 655672f2-5d49-3d91-b23b-d782aad73cb7 | -12.02151 | -43.72727 | 2025-11-14 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7f063275-14f5-3ebc-b01d-006c6d2214ef | -5.42301 | -43.26275 | 2025-11-14 04:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d44a2174-cea9-3dd7-9cd5-f9db19e38a01 | -5.75778 | -42.72394 | 2025-11-14 04:25:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 332c9369-df12-37bc-9a41-ff0e51f97556 | -6.14522 | -48.05145 | 2025-11-14 04:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abf11791-9e7a-32d0-ba5e-62f8cadc1b3e | -16.35731 | -46.00769 | 2025-11-14 04:25:00 | NPP-375D | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31a4ab5f-0a22-3e76-9638-14ae0038cb54 | -20.64488 | -41.70485 | 2025-11-14 04:27:00 | NPP-375D | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4648de2e-8f55-3e21-90e7-eace7e295197 | -19.47425 | -46.92413 | 2025-11-14 04:27:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aa354207-8282-38e6-b6c0-84bb83165250 | -20.10492 | -41.67654 | 2025-11-14 04:27:00 | NPP-375D | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c888ea06-34d6-33c4-8ace-7c4d304262fd | -19.07799 | -44.85937 | 2025-11-14 04:27:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5522d6e2-769f-367d-93aa-29a1568ea0eb | -20.53347 | -41.98498 | 2025-11-14 04:27:00 | NPP-375D | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c713ff9e-1ef6-3a2e-9769-6e20e728b621 | -20.10061 | -41.67596 | 2025-11-14 04:27:00 | NPP-375D | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6ccdad2a-d462-37a6-8c68-9f05e82b879d | -19.97539 | -44.85656 | 2025-11-14 04:27:00 | NPP-375D | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ae0c0c4-0f74-3eb9-8ffb-dc54e34ab4cf | -20.53682 | -41.98784 | 2025-11-14 04:27:00 | NPP-375D | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1cb7f278-0567-3945-867e-d5f293a0fdcf | -19.47482 | -46.92043 | 2025-11-14 04:27:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ea8cfe90-bd1d-3d5c-9f26-ddb84fb4f822 | -18.76415 | -45.28767 | 2025-11-14 04:27:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39cb1cc9-1b22-3256-ab04-023c741875d9 | -20.11451 | -45.83937 | 2025-11-14 04:27:00 | NPP-375D | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 734fc2e3-e427-3880-b023-a84688014fee | -20.39766 | -47.11198 | 2025-11-14 04:27:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b67bf8a9-ad95-37d0-a8a2-e09207151247 | -20.5373 | -41.98382 | 2025-11-14 04:27:00 | NPP-375D | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 72c9428a-6075-3f59-8247-a48a87ecffd4 | -20.59309 | -45.11113 | 2025-11-14 04:27:00 | NPP-375D | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e9b013e4-f13a-3e33-b1d5-95b8d54342f7 | -21.65455 | -48.63155 | 2025-11-14 04:27:00 | NPP-375D | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73bfd4b9-7854-3eba-81ef-46e856b3103d | -18.76474 | -45.28366 | 2025-11-14 04:27:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ab08947-1fb1-304b-af93-049396f78cc5 | -20.10436 | -41.68105 | 2025-11-14 04:27:00 | NPP-375D | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 46ca7170-af53-30e3-b875-43cf171466a6 | -19.49473 | -44.27673 | 2025-11-14 04:27:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05c94567-dba2-34bf-9dc1-84233f60d6b3 | -20.54106 | -41.98845 | 2025-11-14 04:27:00 | NPP-375D | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d0f5f92b-c69f-350a-bb79-a16a2fe52c43 | -20.53773 | -41.98545 | 2025-11-14 04:27:00 | NPP-375D | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7cd2f7d4-df46-3262-a62e-272d1df65f87 | -11.8677 | -49.2195 | 2025-11-14 04:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 508b1f98-ee66-3908-a5c4-24c7092f7e49 | 3.0911 | -60.7653 | 2025-11-14 04:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 86cf437e-25d1-3367-9fff-f9e0c6a3d3fb | -11.8486 | -49.2218 | 2025-11-14 04:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 127.5 |
| f3dd448a-162d-3b18-931e-fbf77675fbf3 | 3.1094 | -60.765 | 2025-11-14 04:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 70.3 |
| ffb1e2db-cc7c-3fc6-921f-59cd5b7ec3bb | -11.8677 | -49.2195 | 2025-11-14 04:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| c51672a5-8c30-3839-9805-3a22ed0771c5 | -11.8486 | -49.2218 | 2025-11-14 04:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 4c702fde-79b3-3707-903f-b8cb05292d4a | -12.6749 | -46.7378 | 2025-11-14 04:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 39dc04a4-5fa6-3e2d-9e6a-b05f8469db82 | -12.6557 | -46.7407 | 2025-11-14 04:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 36.4 |
| ca410268-7c5d-3812-9cd0-7aa805b31b6c | 3.1094 | -60.765 | 2025-11-14 04:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 75.1 |
| aceceb03-4c27-3393-bce9-af3df1090cd5 | 3.13862 | -60.7154 | 2025-11-14 04:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 17.9 |
| b7819c95-9788-3902-b5c5-dfaef4aa67ec | 3.15467 | -60.28783 | 2025-11-14 04:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f96d1a6b-6363-364a-a855-a1f0182e1654 | 3.10746 | -60.76807 | 2025-11-14 04:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 884dfbad-48f5-3675-bb05-5475200ea6d0 | 4.26249 | -59.85442 | 2025-11-14 04:42:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2860702b-28f8-3c91-97be-be5af6fcec12 | 3.61186 | -51.37453 | 2025-11-14 04:42:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2563a0f4-d7d3-3c4e-884d-e843fd956612 | 3.16013 | -60.28201 | 2025-11-14 04:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b7b18da-3f79-3c0d-85da-dcaa460a247f | 3.15932 | -60.28395 | 2025-11-14 04:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a39129b-89d2-3526-b541-59e450da8792 | 3.16002 | -60.28883 | 2025-11-14 04:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b780bc5-fe1a-3e38-bdc3-1ab015a5f14f | 3.1349 | -60.7199 | 2025-11-14 04:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dde6585e-e546-3d70-9cfb-0d8b7ffff64d | 3.16779 | -60.29078 | 2025-11-14 04:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e71b050-26f5-31ca-98cb-52c19c6a46fa | 3.53587 | -51.44602 | 2025-11-14 04:42:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91de8c87-cd9a-387b-bb4a-4ad34b6a2088 | 3.16632 | -60.28103 | 2025-11-14 04:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c012bca0-bae7-3d05-a27b-7ef18b7df3b2 | 4.26185 | -59.85006 | 2025-11-14 04:42:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eae0d778-3b9c-359c-83bd-2a9d63465902 | 3.10904 | -60.7666 | 2025-11-14 04:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 9c6727ba-7c94-3316-90f3-3f705f13af95 | 3.10668 | -60.76287 | 2025-11-14 04:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ed93c532-148d-3ec8-97ed-174e7b2c85dd | 4.26168 | -59.84836 | 2025-11-14 04:42:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23d6b29f-49e8-3da9-a3f9-ef2a5d63a3aa | 3.10108 | -60.76907 | 2025-11-14 04:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ed8d5fba-9a81-3fe8-a50a-6082d6805a25 | 3.16087 | -60.2869 | 2025-11-14 04:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62ec21b0-958a-3073-81bf-7a108fc363b8 | 3.13941 | -60.7206 | 2025-11-14 04:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 9eef4b1d-1033-3491-81b6-660fb0affc5d | 4.2623 | -59.85281 | 2025-11-14 04:42:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 35c79f96-b336-318d-984f-5a90d6fa0311 | 3.10824 | -60.77328 | 2025-11-14 04:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |


[Clique aqui para ver as próximas entradas](README39.md)
