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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a856a591-df9a-3447-8424-375643729df9 | -6.29435 | -43.60074 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 546b6dda-6dfa-3038-a219-95af98c06570 | -6.46952 | -53.4015 | 2025-09-04 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f01b14bd-08d8-364f-848e-cad13fc9f593 | -6.77201 | -44.49459 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92eb8e44-3fef-3927-aaf4-af1de6d6d682 | -5.38992 | -45.94485 | 2025-09-04 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bbad4170-f11e-3864-89e0-1f06b47f3168 | -6.22307 | -42.45113 | 2025-09-04 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0c7c752d-1a33-33a3-b4cf-25b9a2db82bf | -3.16276 | -48.60606 | 2025-09-04 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0908c394-eab8-36a5-92c7-0aa57abd90a7 | -5.89354 | -42.98433 | 2025-09-04 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 4da455ec-a3d4-3f72-9312-44cfec45d22e | -8.02469 | -44.10725 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4635c269-0cca-3407-92a5-975472485a38 | -6.32836 | -45.66244 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77f406f2-e9b8-34d0-804c-c7830e8ce256 | -6.47031 | -53.39683 | 2025-09-04 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3814502e-2906-346b-9831-b41ec976bb5e | -6.29021 | -43.6042 | 2025-09-04 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c1b6c33-da58-3f37-8883-a6e2e115bd45 | -6.79133 | -44.43647 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3351c1e-34e0-3fe5-8b0e-bc1ff11b57d1 | -6.25318 | -43.29961 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f1b99f1f-4682-34cb-bff1-b07bf1ba8235 | -6.85745 | -44.27971 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 860edd1f-d065-3dc5-a26a-ef9de49f1dcd | -4.89746 | -44.95605 | 2025-09-04 04:25:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33ba4dae-87bf-38e8-bc85-3f258e4dcc49 | -5.53854 | -46.43008 | 2025-09-04 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60395ec8-7dcf-3a46-9355-395fc71f406b | -6.92972 | -45.55513 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 935a7b12-86d4-3b54-aafa-5b41560476fd | -5.17651 | -43.04424 | 2025-09-04 04:25:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc488e67-deb5-3695-bcce-396a400b25e3 | -5.70451 | -45.16693 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fbd84fcc-7834-378e-95f7-ff890a432136 | -6.50095 | -43.07338 | 2025-09-04 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d1d0438-2d27-3c12-9210-042eb72953b2 | -6.22884 | -42.43812 | 2025-09-04 04:25:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 30aca152-7d1b-326f-a1db-18e34d16a328 | -5.67513 | -43.66943 | 2025-09-04 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5053e98e-3f9b-3530-b36c-2841a49fa196 | -5.76672 | -44.8744 | 2025-09-04 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de57ed81-1f53-3f93-8443-c0de0383ced0 | -6.78431 | -44.29574 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a5e222b9-22af-37bb-9ab3-802dbfc62ea7 | -7.196 | -44.9998 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b749b603-5334-3601-9016-47cd152870e7 | -5.70839 | -45.16391 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 492c6f7f-d40c-3728-a4d3-a3bc8f0aef54 | -6.89354 | -45.57123 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 562e859c-c2f8-3cb3-9e62-af4a43d6d55a | -6.2631 | -43.59179 | 2025-09-04 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84505535-cea5-3847-8f52-89137352b7e0 | -6.85571 | -44.26786 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c32e072-2f1a-3b00-a319-b74460142c15 | -6.33642 | -42.69973 | 2025-09-04 04:25:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6ae3e140-afe4-3c82-b5f5-590243206827 | -6.83211 | -44.28349 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d237e02-1b4f-36ac-865d-b4064a8f8f92 | -6.24722 | -43.55245 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 879152f1-f09c-39f7-a52b-7dcad1d4ee93 | -6.44608 | -49.9461 | 2025-09-04 04:25:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cb76422-c517-310e-b84c-c00adfed941d | -6.26858 | -42.64468 | 2025-09-04 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 92ae3e12-89ca-373d-9a48-12532bb8a5d3 | -6.73624 | -45.92632 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00e99e13-8c75-3102-bb86-a449ecd92bf9 | -6.87244 | -45.57534 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| dae6df61-c602-38e7-b432-d86c9f240846 | -5.60344 | -45.02827 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1bb08181-a8f1-32c3-8478-b9d802d1d576 | -5.61123 | -45.02222 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c00d54d-ef9d-398f-b7df-c9f96544d0c0 | -5.88222 | -43.23479 | 2025-09-04 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 962002e0-9c4d-3f3b-9f5c-433f2d0ba8ef | -8.02055 | -44.13524 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4113f868-46e7-3108-83cf-a3d37bb7016f | -6.73394 | -42.27102 | 2025-09-04 04:25:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f794e558-d724-39fa-9bdd-5556c7993d5a | -5.68975 | -45.39483 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58328695-4e1a-3d3b-9076-c82daa785a47 | -7.14814 | -46.75269 | 2025-09-04 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65ef47b6-653b-31bc-9eeb-d8d09adce77f | -5.75115 | -45.41552 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48f83164-8954-382d-8570-3a82b3ff602c | -6.2313 | -43.56192 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01228006-0030-3f7c-b152-a8ed2d4dae22 | -5.35234 | -45.09063 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72e48928-f37d-3e74-b9ca-8e453cf36d2e | -6.7885 | -44.45518 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ab6dbb20-5b5f-3ac7-a44f-5b00d783cfc9 | -5.76724 | -45.42158 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb02d65e-6378-3d5c-b79f-33b994fe659e | -6.23532 | -43.55996 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28e45dd6-970d-38ed-ab86-ef7b1a86c316 | -7.92946 | -44.9304 | 2025-09-04 04:25:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ae288474-965b-3610-aeef-14c5eaabf841 | -7.15759 | -45.22668 | 2025-09-04 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a2396f0-e63d-382c-a3da-8c1847b7e7fb | -6.19684 | -47.84524 | 2025-09-04 04:25:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e449f52c-4b3d-3c6b-b60e-cae40ddf8501 | -5.80773 | -45.62054 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42a4a901-e6ef-3669-ab74-b02f80014748 | -6.07182 | -45.54063 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95eafac0-b890-3836-8a67-e4c2357ab271 | -8.00974 | -44.03671 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0242506e-ff60-38ef-ac15-7a0d4f1de172 | -6.42385 | -44.43198 | 2025-09-04 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f67e796-7a5f-3262-8410-908992afcb1a | -5.77063 | -44.87133 | 2025-09-04 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4cf38a0-a4dd-3f5f-9ece-fbf02585637a | -6.61999 | -43.96577 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3fbb85b-64c8-3b6c-81d9-52f860394fb2 | -6.51528 | -43.50368 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a6b8e8b-497e-356d-b23d-8f506880c5ff | -3.36291 | -43.37188 | 2025-09-04 04:25:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f17a85b0-eecd-3578-9d77-3f3f20a58543 | -7.50846 | -45.37207 | 2025-09-04 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fad450c-4078-3632-bae8-bdaf756ee1ff | -6.27226 | -43.50619 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83235c16-1c95-36d8-ae8d-d7f7d581836c | -5.31031 | -55.86162 | 2025-09-04 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5e53d23-7bb9-3ce8-beb8-b143569cf72e | -6.89075 | -45.56721 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5d29fed-4507-352a-8eef-bff2fe13b5a1 | -8.02358 | -44.04158 | 2025-09-04 04:25:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47ba03c3-9c58-3f66-bd88-aff490756805 | -5.31643 | -55.85907 | 2025-09-04 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 403a16d7-55a6-39ca-8e51-ce3d6926fe0e | -6.23482 | -43.53955 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 57f52bd3-ae4a-370f-acff-4f4ee60e6541 | -6.49666 | -43.07714 | 2025-09-04 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f476376c-4c37-3869-8029-5b209910ae8e | -4.83346 | -42.73613 | 2025-09-04 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11ad2ba9-c024-3134-9417-848041f274e6 | -8.04516 | -44.13904 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 195ce4c7-cf9e-3b69-9469-8ed520f8c228 | -8.01793 | -44.78667 | 2025-09-04 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e6b02c27-3a3c-3408-857f-158b16af8fbd | -3.5426 | -49.06312 | 2025-09-04 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b5c15db-15b8-3cc3-9363-4f3b503f0924 | -5.02926 | -56.10991 | 2025-09-04 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7892c6b-1135-3a5a-9fc5-6656b075627e | -7.94139 | -44.9436 | 2025-09-04 04:25:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c5ebe707-635e-3ddf-a08d-7068b8abdcef | -5.98685 | -43.81797 | 2025-09-04 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc057ff2-127c-3e95-baa1-e89f5e401413 | -7.59247 | -45.13815 | 2025-09-04 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f966132-1b1c-3341-b8b3-7760930ebea1 | -6.29081 | -43.6002 | 2025-09-04 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 822b53ee-ca8f-37e6-89f6-69aff6fd2f4a | -6.13096 | -44.14638 | 2025-09-04 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5a688dc-64d8-3844-bf3f-d67d875be9f0 | -8.02229 | -44.14775 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d0fbe37-88dc-3fbf-8ff6-25146a3ef641 | -6.28351 | -43.50399 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2a753ddc-6103-3ce8-97fb-b3b190083b55 | -6.72296 | -45.15655 | 2025-09-04 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03e4f2fe-f768-3be0-ac66-6db187e9661f | -2.96364 | -49.34914 | 2025-09-04 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01c13bb8-8d5c-3523-a78a-54d083d581b4 | -6.67947 | -48.41208 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3ba8c543-19f0-378e-bfd1-d48d14fd49ab | -6.96472 | -44.33486 | 2025-09-04 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3eb5f10d-30af-3988-a8b1-157d7787384b | -5.4116 | -42.33195 | 2025-09-04 04:25:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 86a950c3-ad43-34ee-a95a-c37e1b6bf408 | -6.36282 | -44.4415 | 2025-09-04 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e34d7c0-b43d-32a9-9e6e-080387fd845a | -4.78208 | -43.81918 | 2025-09-04 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 408d5879-08f0-3ef2-b25a-37ee80ded37c | -6.17315 | -47.285 | 2025-09-04 04:25:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fb70b12-52ce-32ef-ae03-0fc2d986500d | -8.03813 | -44.13792 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b34ff72d-87a0-35bb-a633-90576a790ae4 | -6.42774 | -43.62802 | 2025-09-04 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f064d33-af87-350d-bcec-d7782c5d86cf | -3.22378 | -47.12792 | 2025-09-04 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb237e56-dd94-3738-bc95-9d8ebe5edce4 | -5.89284 | -44.34888 | 2025-09-04 04:25:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9610ecb5-24ce-356d-9575-508d96848b9d | -6.85054 | -44.27861 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f872c668-e0c2-3720-9ddc-ea4109c1af34 | -5.78407 | -46.16569 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b4dd5298-9d09-3efd-9059-ac7f52f7c8c8 | -6.29264 | -43.58809 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e87d3fe5-5c17-3e46-b913-b74d667b286a | -6.24545 | -42.63426 | 2025-09-04 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 69172104-b657-3e82-945a-5ca53f172377 | -6.20954 | -43.39429 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c36406c-bfe5-3cdb-9974-e270fdb6e90e | -7.44336 | -42.03511 | 2025-09-04 04:25:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8d224fb9-ec93-3a23-bf01-ffb5586385fe | -7.4991 | -44.80923 | 2025-09-04 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 572f953d-ca8e-33fe-b1b7-cfc1f1f08544 | -4.91841 | -43.14528 | 2025-09-04 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README33.md)
