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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8118799-7a1d-3963-b2e1-fd4733dfa625 | -9.6104 | -40.342 | 2025-10-08 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 122.1 |
| e35f1c84-4bfe-3c45-8c5c-513ae1dd125d | -5.1414 | -44.967 | 2025-10-08 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 342.4 |
| 57e90901-2688-3706-9a8c-6cfdde6ea26e | -13.7165 | -45.7064 | 2025-10-08 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 17e6c85b-35d9-3d56-a473-6af1298927f4 | -6.949 | -63.1048 | 2025-10-08 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| c912a67e-68d7-3a50-9e57-5c3790992866 | -10.3729 | -50.2722 | 2025-10-08 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 8f9c8c4c-0d8f-34ca-a5dc-8f332641408f | -13.7359 | -45.7031 | 2025-10-08 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| a335a8f9-7301-3ad1-aa2e-db7239b01bd7 | -3.7937 | -49.4211 | 2025-10-08 00:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| d2df9f86-4265-3860-9c4a-295c2fe69067 | -5.8657 | -43.3981 | 2025-10-08 00:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 2cefc550-92de-3acd-adf1-5731135ac158 | -4.6504 | -43.2038 | 2025-10-08 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 166.6 |
| 679cc865-cd1d-3425-9e78-81d2a12ddfd3 | -12.0314 | -45.1901 | 2025-10-08 00:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 8d2cedab-ffde-385f-a9c7-a58b2109bd42 | -3.4422 | -45.598 | 2025-10-08 00:30:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 43bfa727-5bab-31f1-a17e-3be092301b3f | -14.7184 | -46.0636 | 2025-10-08 00:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 172.4 |
| 28c31108-f7b8-3fec-a89b-4ed6159230b7 | -14.6988 | -46.0671 | 2025-10-08 00:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 165.7 |
| d4beb39d-ea95-30ae-a8d2-147f060ea9b8 | -11.4534 | -50.198 | 2025-10-08 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 77152f56-0db5-3a3e-9588-b30adc42fcc5 | -10.93 | -51.0229 | 2025-10-08 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 24b3954d-5631-3582-ab5a-8dfdb052495b | -5.8469 | -43.3995 | 2025-10-08 00:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 154.8 |
| e379823c-1578-3172-9af7-95863c9e2083 | -13.7364 | -45.68 | 2025-10-08 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 9e215c4e-3caa-35fb-938b-b5d9767e3eff | -4.6691 | -43.2026 | 2025-10-08 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| d09c0872-d4e3-32be-a168-3364d2a2c082 | -9.6108 | -40.3171 | 2025-10-08 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 80.1 |
| 61c99205-cf08-3bbd-bfc3-444d43684f15 | -5.1416 | -44.9443 | 2025-10-08 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 48afbda3-3c08-37f4-8f0d-e3c61fee04bb | -19.8584 | -46.1569 | 2025-10-08 00:30:00 | GOES-19 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 108.8 |
| d2b103b9-316a-3066-9dbf-c0cbde425afa | -6.9982 | -42.878 | 2025-10-08 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 121.4 |
| 968f8220-c2fc-3126-ae91-b423c4133578 | -11.3378 | -56.1997 | 2025-10-08 00:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 69621d9f-05b1-31f4-af85-b1429af63bba | -5.8467 | -43.4229 | 2025-10-08 00:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 2a7d7b15-f01b-334a-afed-ff65cc86c5b1 | -13.7923 | -45.7859 | 2025-10-08 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 77d8a2ca-7c71-3e48-96dd-a0bf7095ab53 | -6.9979 | -42.9016 | 2025-10-08 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 59.7 |
| 4fd977ab-701e-3a07-9ad2-1ae0d303acb7 | -9.6295 | -40.3392 | 2025-10-08 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 70.8 |
| 546b4961-7022-3325-91e1-7a3a813443e3 | -14.7184 | -46.0636 | 2025-10-08 00:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 68.5 |
| d068db3e-cede-38f1-8e54-5cb741c8035c | -6.949 | -63.1048 | 2025-10-08 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 0c5b152e-0560-3cec-956a-677a9ef16e88 | -5.8467 | -43.4229 | 2025-10-08 00:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 96bbbfab-ddcc-338b-b717-7988ebacd8c7 | -5.8469 | -43.3995 | 2025-10-08 00:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 859c6599-79cc-3858-a0da-822b417a74e7 | -12.031 | -45.2132 | 2025-10-08 00:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| df6a7e04-6475-3f52-bd25-14b6e168ae2c | -4.6691 | -43.2026 | 2025-10-08 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 52888907-ba50-3ff7-994d-43c776949731 | -9.6108 | -40.3171 | 2025-10-08 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 70.6 |
| 5e17a193-d5cf-3e4c-9998-988972337b2b | -10.3727 | -50.2936 | 2025-10-08 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 485137a9-b987-3451-b7b8-94eb1c8e2aae | -7.7922 | -44.2229 | 2025-10-08 00:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.1 |
| dde0e86e-7600-37be-8dc1-2c3d58fd0d73 | -4.4977 | -46.3731 | 2025-10-08 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 9ab5351f-f4ae-3b66-a633-a94993b64ce3 | -4.8557 | -45.7511 | 2025-10-08 00:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 3f53396d-dbee-3525-bf75-5f60f03293c2 | -11.6888 | -50.9833 | 2025-10-08 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 325.1 |
| dfab5f3c-b26b-3525-a2a9-03d9e7e9952d | -5.1227 | -44.9682 | 2025-10-08 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 02ad6d2d-98f2-30c7-81ae-c3c62cc87046 | -7.0167 | -42.8998 | 2025-10-08 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.4 |
| ac2460f8-99e6-33b5-adf1-743840fbb571 | -11.6885 | -51.0046 | 2025-10-08 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 143.0 |
| bb35929f-d560-3f5a-b894-46980fc77b15 | -4.6505 | -43.1805 | 2025-10-08 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 29d608bf-74a0-343c-9294-ba1c9af1c219 | -13.7359 | -45.7031 | 2025-10-08 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 234.0 |
| 9455ac1a-7a9c-37a2-9c43-aa2807363893 | -5.1412 | -44.9897 | 2025-10-08 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 69eccbdc-be59-3379-a32f-4ae0a094ce18 | -7.017 | -42.8762 | 2025-10-08 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 110.5 |
| 8c08efdc-3a6d-3f2c-9a4d-6c75f081f5b3 | -4.6504 | -43.2038 | 2025-10-08 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 139.9 |
| f16ce773-83ce-320b-8a6b-c711d3719ef9 | -11.4534 | -50.198 | 2025-10-08 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 451805eb-5c46-3cb7-abd6-59a0512b80ba | -10.93 | -51.0229 | 2025-10-08 00:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 119.7 |
| ce4390b1-1f22-35d0-8478-c004bcd54dff | -11.4531 | -50.2195 | 2025-10-08 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 802804e9-db82-34d0-ae32-7c9b19b0f1eb | -13.7364 | -45.68 | 2025-10-08 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 123.6 |
| f122cde9-d42a-3db8-839c-6824ef6679fa | -19.8584 | -46.1569 | 2025-10-08 00:40:00 | GOES-19 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 9d3fe840-c233-3a35-93ca-a8aae3db5b4e | -9.6104 | -40.342 | 2025-10-08 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 123.2 |
| 6689dd9f-402a-3da1-be7c-e67387837733 | -11.6698 | -50.9854 | 2025-10-08 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 184.4 |
| d5f4c063-fdca-3193-8501-4066e40ed004 | -11.6701 | -50.9641 | 2025-10-08 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 0e72050e-0fff-335f-b932-69d9cadf4445 | -13.7165 | -45.7064 | 2025-10-08 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 129.1 |
| cb4d16d6-476c-309c-859e-3db3b787e905 | -3.7937 | -49.4211 | 2025-10-08 00:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| f49db807-23b1-3ec5-a574-8faf66876d9f | -6.6946 | -58.8065 | 2025-10-08 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| e5c2df02-50d6-3b1e-89aa-7ad478f87794 | -4.6875 | -45.828 | 2025-10-08 00:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 101.5 |
| b2b5a074-390a-3894-8238-eb9e04c1811a | -12.0036 | -46.7667 | 2025-10-08 00:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| fee3937a-6859-3b36-b923-075c8b461537 | -11.6891 | -50.9619 | 2025-10-08 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| f6361afc-5745-3f1d-98b5-e5b851495a58 | -12.3971 | -63.8811 | 2025-10-08 00:40:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 44b4450e-6969-3fd5-9880-a55c185d7156 | -13.8112 | -45.8057 | 2025-10-08 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| a8644e75-ad38-30e9-ae77-2d900a1915ca | -10.3729 | -50.2722 | 2025-10-08 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 062550c8-f62f-32a5-a5e9-2bb3feba0e79 | -4.4978 | -46.3509 | 2025-10-08 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 68dfcd3a-57cd-3f17-a112-96e9ecac8fa7 | -4.6317 | -43.205 | 2025-10-08 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 4fdcf50f-785d-30ee-a720-2c4b0e4497f8 | -13.7169 | -45.6833 | 2025-10-08 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| e8ddebc7-0a3f-3ca2-88eb-72b4296d7384 | -13.8117 | -45.7826 | 2025-10-08 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 146.7 |
| dffdb002-0134-3406-8d1b-2712c25dc210 | -5.2601 | -44.1368 | 2025-10-08 00:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 9eb87c46-8832-3a64-b4c1-279577493e11 | -5.1414 | -44.967 | 2025-10-08 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 342.0 |
| 58fac2e3-09e1-3a5b-b87d-52ac69bf17ab | -3.4422 | -45.598 | 2025-10-08 00:40:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 584e4c2c-d36d-337b-980d-2e88ce1b54d1 | -4.6692 | -43.1793 | 2025-10-08 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 0ff5f979-e4c9-3a71-a28a-140c19a7b61e | -6.9982 | -42.878 | 2025-10-08 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.4 |
| f2fa7f5b-416c-30ee-8c59-7c7e8d587473 | -4.6873 | -45.8504 | 2025-10-08 00:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 92.8 |
| fb2cbbda-b5e7-38fa-86c2-2a2fa849642a | -5.1416 | -44.9443 | 2025-10-08 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 170.9 |
| 99d540cc-3b88-3dbe-a992-3c02fae7d84c | -13.7918 | -45.809 | 2025-10-08 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| a2c55f56-751b-37c4-8abc-8596193d9dae | -10.911 | -51.0249 | 2025-10-08 00:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 154.9 |
| fbe3917c-f500-3647-ae09-e19249ce9d0d | -7.5874 | -64.5097 | 2025-10-08 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| fa27cc63-6e58-303c-b65d-258a90b8d277 | -4.4977 | -46.3731 | 2025-10-08 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 281868c3-5dd5-3cc8-b545-6177fd7e82dc | -10.9297 | -51.0442 | 2025-10-08 00:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| b5222f9d-deae-311c-a59c-b3f3277283c4 | -4.6873 | -45.8504 | 2025-10-08 00:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 83f369aa-f241-30f1-81f1-0ba6c0634e4f | -11.6698 | -50.9854 | 2025-10-08 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 98decb58-ba88-36d2-9d82-4f2eba34096c | -13.7359 | -45.7031 | 2025-10-08 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| b8dc2c08-ee4f-3f72-a7af-f12e5fc773ae | -5.1414 | -44.967 | 2025-10-08 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 322.9 |
| 34dbafd4-aa82-38b7-b1ad-9511abe2489e | -11.6891 | -50.9619 | 2025-10-08 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 112.6 |
| d5b9b053-1c9c-3dfe-ada2-670e7b9904bf | -9.6104 | -40.342 | 2025-10-08 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 801770fb-9ca2-36c9-9cd1-fd2e750d550b | -9.6295 | -40.3392 | 2025-10-08 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 83.8 |
| a818bc43-a9f4-346b-a4a6-cced089e8aef | -6.6946 | -58.8065 | 2025-10-08 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| ff3fe18d-3431-3c6b-b4ff-c476be8c8653 | -4.8557 | -45.7511 | 2025-10-08 00:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 104.6 |
| a7116359-d0a5-3ece-8f30-90c35f637705 | -12.3971 | -63.8811 | 2025-10-08 00:50:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 59.2 |
| cf00167d-a8dd-3840-a887-2641b49818b7 | -12.0314 | -45.1901 | 2025-10-08 00:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| aec18db6-d526-34d0-b33d-bae23df5babe | -4.6875 | -45.828 | 2025-10-08 00:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 7a4341ec-1412-31ad-96dd-8872a170e902 | -5.1416 | -44.9443 | 2025-10-08 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 183.3 |
| 612c97a1-a5ef-3012-b2e0-891104ec2450 | -7.017 | -42.8762 | 2025-10-08 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 111.8 |
| 2833586e-9ec3-3c84-bcd6-1826f7ef6ecc | -7.6474 | -63.4584 | 2025-10-08 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 2f59c5c3-1af1-3b01-965a-ef0ca6161a52 | -11.6888 | -50.9833 | 2025-10-08 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 368.0 |
| c1b653fa-afb4-381f-9a3f-235ce1e4e632 | -13.8117 | -45.7826 | 2025-10-08 00:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 924572b1-3930-3476-a5df-402e2456b5e2 | -4.4978 | -46.3509 | 2025-10-08 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 3cf08a5e-d33a-32d4-9b1f-a768a13ea34f | -7.0167 | -42.8998 | 2025-10-08 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 73d6b214-a324-339d-ac2a-3784f33c3ffb | -11.6885 | -51.0046 | 2025-10-08 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 177.9 |


[Clique aqui para ver as próximas entradas](README4.md)
