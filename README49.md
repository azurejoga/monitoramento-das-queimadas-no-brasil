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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d91678f5-98d1-37b4-972c-3eed6243fcb6 | -21.06214 | -50.30232 | 2025-08-16 04:36:00 | NOAA-20 | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 20f08232-8486-3518-b47a-10a6ef03f6e6 | -22.53516 | -46.80053 | 2025-08-16 04:36:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ed736189-6f9d-30c8-827a-9dd708092211 | -21.06157 | -50.30609 | 2025-08-16 04:36:00 | NOAA-20 | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8b226d42-f7ae-3611-9b1f-c729d7aa612a | -19.66565 | -49.37633 | 2025-08-16 04:36:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d0efb00a-1e1b-333b-9162-02fa68d1c1fe | -19.36422 | -42.93317 | 2025-08-16 04:36:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0119aded-d3ca-30e8-a2a4-76d026227761 | -23.27054 | -51.20645 | 2025-08-16 04:36:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4de5ef59-ff1b-3f7b-a182-83c1efeb5af1 | -20.39165 | -54.78021 | 2025-08-16 04:36:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02351bc9-ef62-3f15-83ea-b0e910077d93 | -19.36276 | -42.934 | 2025-08-16 04:36:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 04e3467c-fe54-312b-b058-5e84ff8f396a | -19.95452 | -44.1445 | 2025-08-16 04:36:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 76875071-bc7d-3270-bb12-9c775caedf52 | -20.66353 | -49.39014 | 2025-08-16 04:36:00 | NOAA-20 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 62be6630-93b9-3abe-9417-9d19efd9acec | -20.07861 | -49.42131 | 2025-08-16 04:36:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 24803961-fffc-3ec4-830f-6cd24f21afc3 | -21.38172 | -45.74351 | 2025-08-16 04:36:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2227a286-888f-3be9-b213-4c3a38c75fd5 | -22.78122 | -50.19971 | 2025-08-16 04:36:00 | NOAA-20 | PALMITAL | SÃO PAULO | Brasil | 3535309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ab14e8c4-fd9f-3487-b9c3-35d6bda2eebf | -22.34421 | -47.31627 | 2025-08-16 04:36:00 | NOAA-20 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 361875e2-f4d7-3416-b7ad-c2c596d7a7b6 | -20.42071 | -46.53342 | 2025-08-16 04:36:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca204630-4a94-38c5-9206-eef838c6c9ea | -22.53984 | -46.88507 | 2025-08-16 04:36:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d86c1c05-2b97-3a23-b1db-ffdb2bc7c5db | -19.21228 | -44.29574 | 2025-08-16 04:36:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc8a9b92-6529-3f10-b5ee-406face56e6b | -20.41488 | -46.54813 | 2025-08-16 04:36:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 86dc6984-b3ce-354e-a269-123a382d622c | -23.18252 | -46.75462 | 2025-08-16 04:36:00 | NOAA-20 | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b6a814c3-6804-3bfe-b599-f78892e613a9 | -20.41518 | -46.5416 | 2025-08-16 04:36:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6ec06bc5-e875-3e58-aab7-d6ce40adf97e | -23.78692 | -51.8822 | 2025-08-16 04:36:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 56e8adf9-f792-3a57-9fcc-8a0a26613bb4 | -20.08258 | -49.41801 | 2025-08-16 04:36:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 22deff11-d768-3a5c-8ffe-52a55212f478 | -20.04754 | -44.63039 | 2025-08-16 04:36:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b315d1a3-5a7e-34df-88d2-6ec9417f80d8 | -22.97625 | -48.80782 | 2025-08-16 04:36:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a8cf15e-fd0e-36e7-b5f3-43c9e8faaa4c | -22.98042 | -48.80404 | 2025-08-16 04:36:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 159dde3e-d916-35d8-b4ee-326308b65358 | -20.41583 | -46.53671 | 2025-08-16 04:36:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 719e5813-1a71-334d-8e65-912da2935ee3 | -21.52706 | -49.1434 | 2025-08-16 04:36:00 | NOAA-20 | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dbf0bd99-820a-363c-acea-261a1c7c5f25 | -20.41453 | -46.54647 | 2025-08-16 04:36:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fc7bc04e-b9c3-316d-8fef-edb890cafea0 | -20.16008 | -47.29166 | 2025-08-16 04:36:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b69aac49-0ca4-3f85-b9d2-40b90a115aa6 | -20.41551 | -46.54316 | 2025-08-16 04:36:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f057dae-b0e7-3df5-bde2-f5e5bfa582c3 | -18.48455 | -50.42905 | 2025-08-16 04:36:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 444f99d8-23a3-3fa0-9d61-52035aa82072 | -22.97686 | -48.80345 | 2025-08-16 04:36:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 695a4d5f-452c-3d27-80e5-10bae655380b | -21.52648 | -49.14748 | 2025-08-16 04:36:00 | NOAA-20 | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 65946a22-a3b6-3363-a76e-7dc402f70ef2 | -22.53854 | -46.89552 | 2025-08-16 04:36:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c6840d71-89cd-36ad-827d-44477d7ffd68 | -22.53527 | -46.88974 | 2025-08-16 04:36:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 39a7129c-c068-3201-990f-d8ca48470564 | -21.38371 | -45.74494 | 2025-08-16 04:36:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b0f810bb-d6fb-30ed-aa28-f6d3edf16cfc | -22.5341 | -46.80183 | 2025-08-16 04:36:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6039b9ab-9b72-30b4-af5f-14d05b68ee01 | -19.12132 | -46.67865 | 2025-08-16 04:36:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c019183-8a09-30ae-b795-e48b695f90a1 | -20.59713 | -51.6107 | 2025-08-16 04:36:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4ca390f6-8b58-34d4-9abc-47c9dbb38b12 | -20.41613 | -46.53826 | 2025-08-16 04:36:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d4bf4a0-3ee0-3662-bc8a-f6937934a211 | -20.04702 | -44.63475 | 2025-08-16 04:36:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6cabd1b1-ed4a-36f0-b68d-b28c2edb0da2 | -22.66908 | -52.85702 | 2025-08-16 04:36:00 | NOAA-20 | DIAMANTE DO NORTE | PARANÁ | Brasil | 4107108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 285a6804-4d9c-3032-8fb8-25e16878a6d5 | -22.9585 | -46.69708 | 2025-08-16 04:36:00 | NOAA-20 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ab761400-58e9-3432-ba4b-f335b50092dd | -26.64195 | -53.70141 | 2025-08-16 04:38:00 | NOAA-20 | PARAÍSO | SANTA CATARINA | Brasil | 4212239 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 76daf4b0-5e15-3965-a61a-d2c9ead047ba | -30.34142 | -52.36958 | 2025-08-16 04:38:00 | NOAA-20 | PANTANO GRANDE | RIO GRANDE DO SUL | Brasil | 4313953 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| acade66e-ed91-395c-93e6-fafc97345b33 | -26.10447 | -50.17809 | 2025-08-16 04:38:00 | NOAA-20 | MAFRA | SANTA CATARINA | Brasil | 4210100 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| fc7118dc-6efb-3669-ae98-d18649a09bd5 | -24.04809 | -52.20817 | 2025-08-16 04:38:00 | NOAA-20 | CAMPO MOURÃO | PARANÁ | Brasil | 4104303 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ed9a9ffd-9532-3837-9299-28fc07d1bdc9 | -28.83932 | -51.71561 | 2025-08-16 04:38:00 | NOAA-20 | FAGUNDES VARELA | RIO GRANDE DO SUL | Brasil | 4307864 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ddb05c9c-12e8-3b8c-b178-a8f42fee63c1 | -28.87773 | -56.25144 | 2025-08-16 04:38:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| b579b730-7863-3e59-a6ab-6d76b6c6c2dc | -28.55845 | -50.26587 | 2025-08-16 04:38:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6f228f9e-d7e1-38ac-ac7e-0c1124e5c1b6 | -24.91696 | -52.36244 | 2025-08-16 04:38:00 | NOAA-20 | PALMITAL | PARANÁ | Brasil | 4117800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| cd56742b-7270-3113-aff4-c22504b59d04 | -24.24033 | -50.20797 | 2025-08-16 04:38:00 | NOAA-20 | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 46766771-09d4-30e9-96f2-6e69c4f04146 | -14.9632 | -54.7143 | 2025-08-16 04:40:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 54.8 |
| f43375cb-8a7f-32ac-9113-d947b9397b71 | -9.4992 | -60.547 | 2025-08-16 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| dc4f84e4-0e8c-313f-94ac-748290ee1c31 | -9.1709 | -59.6374 | 2025-08-16 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 3bd83a01-10da-3f06-8a22-999e0c199a6f | -8.9709 | -61.6842 | 2025-08-16 04:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 72.0 |
| fe057349-4ea1-3588-8fd5-fbe36cd11209 | -7.9148 | -61.7478 | 2025-08-16 04:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 3549d342-8005-3c8f-b036-3991a53046fa | -8.9708 | -61.7033 | 2025-08-16 04:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 1bcf500d-4046-326c-b19f-56961aca10d0 | -14.9435 | -54.7374 | 2025-08-16 04:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 3ec43bbb-e1fe-3c47-a8ff-4c4b8827c532 | -6.9487 | -59.5297 | 2025-08-16 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 30142a62-d465-3f97-9b67-2b9eacee9e57 | -14.9438 | -54.7166 | 2025-08-16 04:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 147613a6-98dd-33cb-bdcd-db24373a49a6 | -7.9149 | -61.7288 | 2025-08-16 04:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| a0723bd3-5d4c-3491-a8bc-ea7a17a39625 | -6.9486 | -59.549 | 2025-08-16 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 72e5589d-9b19-3707-9c92-cde8946b257e | -14.9441 | -54.6959 | 2025-08-16 04:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 74c2d9de-d987-382d-9b9b-51ddd4e2812e | -14.9628 | -54.7351 | 2025-08-16 04:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| e28c6171-4c1d-3031-93ac-dbdb575472fe | -8.9893 | -61.7024 | 2025-08-16 04:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| c287e1da-f0ef-35f3-93ff-8d1a300ad58d | -6.9303 | -59.5305 | 2025-08-16 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 3fe62524-45be-3ac9-8dfa-7326f19a6447 | -14.9628 | -54.7351 | 2025-08-16 04:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 57439e7c-2a3e-30ef-b497-8e57b825e529 | -8.9708 | -61.7033 | 2025-08-16 04:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 76.1 |
| c5ab1618-2d67-3382-81e7-cc81349ce291 | -8.9893 | -61.7024 | 2025-08-16 04:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 8311ab41-5b39-33fe-bb61-fd2dc03e833c | -6.9486 | -59.549 | 2025-08-16 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 2dca8f3d-eb67-36d1-96ca-a41193edc457 | -8.9709 | -61.6842 | 2025-08-16 04:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| c81c3807-0004-3920-810a-a560a53097a2 | -20.0929 | -49.4228 | 2025-08-16 04:50:00 | GOES-19 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.0 |
| db0af567-0210-3cd2-a87d-1fd9f3e1c61d | -8.9706 | -61.7224 | 2025-08-16 04:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 43.8 |
| a2020184-8c3e-3496-b836-08de8b2aad25 | -14.9438 | -54.7166 | 2025-08-16 04:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| d3dd7d20-815d-39c3-a570-be66ce7cd438 | -4.9118 | -43.257 | 2025-08-16 04:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| a3826260-ece2-3a28-9a96-e551854a3216 | -7.9149 | -61.7288 | 2025-08-16 04:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 955d012b-28f1-380c-99ef-e625c57d8d33 | -20.0725 | -49.4271 | 2025-08-16 04:50:00 | GOES-19 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.5 |
| 55726a0e-a979-3d2b-8a4b-79cbc8c6ace4 | -6.9487 | -59.5297 | 2025-08-16 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 12bc9c31-fabd-37aa-803b-89630f37236f | -9.1708 | -59.6568 | 2025-08-16 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 5640dd78-9785-3adc-a9cb-6aae00c83b48 | -9.1709 | -59.6374 | 2025-08-16 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| ef26f042-5d1c-3099-94dc-468c7e73c481 | -14.9441 | -54.6959 | 2025-08-16 04:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 9d2b8789-1787-36bc-9f9f-969fdbfb7b04 | -14.9441 | -54.6959 | 2025-08-16 05:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 3c4257c9-653a-3602-b4ed-3496e937028b | -9.1708 | -59.6568 | 2025-08-16 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 1d3b2a21-7035-32e2-95f3-6ff75a4357da | -14.8696 | -60.0839 | 2025-08-16 05:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 19f55b5a-4bb5-34ad-9a72-d3c10b85aedf | -9.1709 | -59.6374 | 2025-08-16 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| c523e99e-0d2a-3cef-80dd-a67dfd9da5df | -8.9893 | -61.7024 | 2025-08-16 05:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 2271513d-8435-327f-9660-a05faf2c5e1a | -4.9118 | -43.257 | 2025-08-16 05:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 0a43986a-ca15-3cb1-9714-493ce3425373 | -8.9709 | -61.6842 | 2025-08-16 05:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 3ecba083-fe5d-3118-884e-e04842b90d19 | -6.9302 | -59.5497 | 2025-08-16 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 7893b2c9-c976-3918-b45d-82a222084209 | -8.9708 | -61.7033 | 2025-08-16 05:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 7eac9473-8b29-3cb5-9193-e9bffe3a5023 | -8.9892 | -61.7215 | 2025-08-16 05:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 9591f574-13a1-3c78-bc93-7f438109acf4 | -14.9435 | -54.7374 | 2025-08-16 05:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| e4abcd1b-11ad-3a7d-9fbc-97285d8e8022 | -6.9487 | -59.5297 | 2025-08-16 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 76134643-b304-3c3f-abfb-c2f482713895 | -6.9486 | -59.549 | 2025-08-16 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 7fbab597-f441-3907-a504-f070cfb242e9 | -13.50017 | -43.60291 | 2025-08-16 05:04:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| abfcc596-c50d-34d5-9000-141d1b12492e | -6.95117 | -42.86223 | 2025-08-16 05:04:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 24.7 |
| c6709e46-910b-3b2c-a25b-6bc4bcd11fd5 | -4.91957 | -43.25139 | 2025-08-16 05:04:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 9df60a90-3b4a-3f40-bd1d-8d793681ec7a | -6.95342 | -42.85492 | 2025-08-16 05:04:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 31.0 |
| c2cb53d0-cede-3980-936f-9a4c8f7be55c | -4.91084 | -43.25782 | 2025-08-16 05:04:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |


[Clique aqui para ver as próximas entradas](README50.md)
