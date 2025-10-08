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
| 4d2882b1-3b9a-33d9-9400-6d5c738730f9 | -21.41268 | -45.12386 | 2025-10-08 04:19:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| ab4cf2f3-59a1-3f23-a149-51ef4eb1392d | -16.1318 | -47.91413 | 2025-10-08 04:19:00 | NPP-375D | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1142f72c-6907-3446-a5d6-9b4905091301 | -8.26881 | -47.00999 | 2025-10-08 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7243290a-d006-31fb-b25b-519397fda3ed | -7.80446 | -44.17814 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab4ab3ff-c575-3236-b5f4-dfdb28dac80b | -13.5616 | -46.50476 | 2025-10-08 04:19:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 740a2963-d6d3-37a4-974d-1a0ca2ef30a0 | -8.50842 | -44.22578 | 2025-10-08 04:19:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5a48af4-4b20-376f-9f46-1979530aed15 | -18.03576 | -57.5281 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 947580bf-1fcb-392b-8b32-86dc9d4ff57d | -10.09198 | -40.7781 | 2025-10-08 04:19:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 20ec6495-ddc3-3a81-ad6b-7d96b8abb354 | -8.39626 | -49.73791 | 2025-10-08 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27411917-3eb1-36cf-8a56-65294fa5ef64 | -8.22332 | -46.83047 | 2025-10-08 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96a0e3bf-f622-39d0-99ed-49d9009e66f4 | -8.41352 | -46.80792 | 2025-10-08 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94496050-5c18-3704-bd14-e71e7e55a941 | -17.27072 | -58.11816 | 2025-10-08 04:19:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8f21bfa1-6f96-3d1f-be90-3580b42bc553 | -14.69019 | -48.41699 | 2025-10-08 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e8c9405-b038-3da6-9a6f-0d7249230d2c | -15.06847 | -49.48693 | 2025-10-08 04:19:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f8f82ad1-126c-3337-b953-bb46bdba32a3 | -14.09898 | -44.30604 | 2025-10-08 04:19:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b192260-5bf7-3f41-8992-d97f8cce0121 | -16.76098 | -43.97739 | 2025-10-08 04:19:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3775bd34-d30f-301d-95fa-b497bd3963cc | -8.22372 | -44.15862 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a0d23fa9-ed03-35b9-8433-873d3e965064 | -7.78656 | -44.22576 | 2025-10-08 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8aca7445-d563-32f9-84b9-5bab9dafdb6f | -16.12897 | -47.90947 | 2025-10-08 04:19:00 | NPP-375D | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 705b81b7-4730-319b-a10e-207558632e7f | -8.62254 | -45.10761 | 2025-10-08 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b4f7283-08e6-3206-8803-1add6b745cf9 | -8.51681 | -46.28141 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46f0906d-501e-3941-a9f3-adcf28a92424 | -9.09072 | -47.96357 | 2025-10-08 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 84ae4044-0ace-3388-b26c-a327e02f0622 | -17.28654 | -42.64926 | 2025-10-08 04:19:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d49610bf-f50b-36de-a019-b73f213f7160 | -15.9929 | -50.84146 | 2025-10-08 04:19:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 27c5e836-9854-3b13-a768-1eff352191b8 | -13.80004 | -45.80003 | 2025-10-08 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 481d22d8-89f0-3165-ae59-e63c1828bcfb | -18.45208 | -42.91203 | 2025-10-08 04:19:00 | NPP-375D | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c02218e8-64f4-339a-8d00-28cb29b1945c | -18.40563 | -45.21158 | 2025-10-08 04:19:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ef049db0-9bb3-3509-bea2-d956e1c539d2 | -18.07609 | -44.44977 | 2025-10-08 04:19:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 523634a8-db8c-37ca-95f7-d3802c390f14 | -14.3861 | -46.01358 | 2025-10-08 04:19:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e24b75f3-67f7-3d0f-85b6-6e1e8aa86dab | -19.83539 | -46.161 | 2025-10-08 04:19:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04f9665b-45ec-39ba-98a4-a988a83ce02d | -13.69765 | -47.94948 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a92028da-0661-36f2-9b0c-f313907929f1 | -17.26493 | -58.12382 | 2025-10-08 04:19:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a0727963-950f-3bfc-94f7-374864f94d3b | -9.16086 | -43.01892 | 2025-10-08 04:19:00 | NPP-375D | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f3dff194-f83b-366f-8ea8-47c1a37d4d7a | -7.81894 | -44.17327 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 819f052f-5eeb-332b-bde9-ca960fa0fc77 | -17.85261 | -44.31452 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97a6398d-faa4-3205-8526-b23e1b628a9d | -19.71811 | -43.90972 | 2025-10-08 04:19:00 | NPP-375D | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c727ca4a-6a8f-33cb-87f4-61a25cb8a703 | -14.93672 | -46.79429 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 02d3e3ed-991e-3333-a681-ae3cdbda1aec | -17.13636 | -45.78389 | 2025-10-08 04:19:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa6fca65-a1b4-3f8e-96fd-cc1a99b291d0 | -15.24127 | -46.36829 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 24cbef1d-21f6-3ba4-874a-f6f95ea5f8aa | -7.79047 | -44.22278 | 2025-10-08 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f9b0355-edb2-30f6-bc90-b90f13127f81 | -13.8466 | -51.86777 | 2025-10-08 04:19:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0f47e3de-6ed6-36aa-a240-04b3966a6063 | -19.85536 | -46.16451 | 2025-10-08 04:19:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42313e34-28e0-35c2-9d4f-724f2c625659 | -14.83229 | -48.41736 | 2025-10-08 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04a17931-79c7-35c4-8b09-4e94cf208d5a | -13.30979 | -48.02956 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a213799d-6603-3d7e-abce-94de8f4bb9b7 | -14.71378 | -46.06866 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f557e7fa-fbb6-372c-a292-69bafad458de | -8.47506 | -46.29585 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5a675b8-3d38-32ea-9e34-d1e517c3a57b | -20.86447 | -45.2049 | 2025-10-08 04:19:00 | NPP-375D | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2406a0a5-e0a8-39e4-b272-d3a4a2e75a1b | -17.43257 | -45.8116 | 2025-10-08 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3ecb9a2-b269-34d4-89c2-5b77354ccfe9 | -17.28235 | -42.65297 | 2025-10-08 04:19:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0dbcfb13-ed93-3f39-aa6a-0afcaad31877 | -17.28535 | -42.6578 | 2025-10-08 04:19:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1fe82b47-f9b7-31cb-bd1a-70fffcd29077 | -8.23257 | -44.18885 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d45558d8-5e43-3997-aecd-94e992091a2e | -15.26409 | -46.33453 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7cb44c9d-99f0-3d1e-8617-d7949e7b2538 | -15.88846 | -46.25696 | 2025-10-08 04:19:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb5006d8-fdc8-3c91-a4a4-e23fa6421b94 | -17.14046 | -43.46344 | 2025-10-08 04:19:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a50256c0-1e55-3f0d-bdb3-be8565269496 | -15.3891 | -48.02903 | 2025-10-08 04:19:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f123ad40-daeb-3102-b75c-740582aedeab | -16.06546 | -47.77419 | 2025-10-08 04:19:00 | NPP-375D | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e677b4a4-ae4b-3418-97f0-7b26ecf63c78 | -8.51615 | -46.2854 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6f0ce3d-c537-3d99-b6e8-25011bd89b31 | -17.45348 | -43.39197 | 2025-10-08 04:19:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1d555b8-e254-3973-905b-8f9331e85b93 | -14.39202 | -46.0292 | 2025-10-08 04:19:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a31cddf1-52d1-3a68-9883-4ee3af515eb4 | -8.11042 | -44.77723 | 2025-10-08 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dfb2a60d-f943-3df1-96d3-47aff5c755a9 | -8.19082 | -43.3442 | 2025-10-08 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 8ccc0fcd-ac08-3a49-9ded-a96225117f2d | -18.06257 | -44.47036 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a45f2e82-eb29-3e20-9576-d4656f3ff5e1 | -7.80774 | -44.22194 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 421d56cb-3e3c-3a99-9c3f-2b1a7e2b488e | -16.33026 | -47.07547 | 2025-10-08 04:19:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b15e1e3-4c54-35a2-a1be-76dc8383702f | -15.39828 | -47.99683 | 2025-10-08 04:19:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a0ff475-0513-3e05-becf-cf932b8f1597 | -15.30819 | -46.16936 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61a6038a-7878-354b-be13-0e38bb5c0bf8 | -9.20538 | -46.89599 | 2025-10-08 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91dfbd95-7913-30d1-994e-5c37a20561a5 | -9.67988 | -45.675 | 2025-10-08 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32ac7b24-5d91-3bdb-9e99-71eecd8e69db | -8.22316 | -44.16213 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c670547f-ec0c-3cdf-971d-7ecec4356f55 | -14.14321 | -43.17569 | 2025-10-08 04:19:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c943d7a1-93ff-34a4-a0fc-335ed915864e | -13.84834 | -51.85846 | 2025-10-08 04:19:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5b4425fc-763d-3ea6-8438-6df76e24e8db | -19.71464 | -43.9091 | 2025-10-08 04:19:00 | NPP-375D | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b787485d-e0e5-3bbe-b943-292a8af7f475 | -8.53251 | -46.23069 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd18340a-bfb3-312e-800b-58cba96fc0cb | -8.51836 | -46.29395 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce44c089-1925-3dc5-87a0-6056c6a40e7b | -8.15567 | -50.16974 | 2025-10-08 04:19:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dae67d7d-2dc0-3863-a482-2b3cd5b387af | -13.85114 | -51.86871 | 2025-10-08 04:19:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40372f11-4fa0-31a1-b3f5-0754a82065ee | -19.50602 | -43.83596 | 2025-10-08 04:19:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a30e3090-72b1-3f0a-b970-3bfb3b26f6c1 | -14.36508 | -45.23522 | 2025-10-08 04:19:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed087999-02b1-3745-a537-74ae5effd69f | -14.70464 | -45.84037 | 2025-10-08 04:19:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea7d3f0a-cf1d-31d2-8750-3929a689fe47 | -15.38222 | -47.30544 | 2025-10-08 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3e88bf6-ebf8-3516-a495-938c0f3e8a95 | -14.9584 | -46.83268 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5f17f409-657f-3a23-9ba9-882a53ba1521 | -13.85288 | -51.85942 | 2025-10-08 04:19:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f4347114-d92d-3364-9107-ddf0dcec65d2 | -14.94357 | -46.79528 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e02194bd-e1d6-3e25-94c3-369ea96f1ee9 | -15.99528 | -50.96787 | 2025-10-08 04:19:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4c64ec3f-16a3-37b7-8abf-15523c5b2a58 | -14.88976 | -42.26317 | 2025-10-08 04:19:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 100cd741-4143-3523-aa1d-96d2df9fd1d5 | -20.28158 | -48.513 | 2025-10-08 04:19:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd963b1a-e2b0-31cf-ac82-50910b7ca1ae | -14.79485 | -41.62837 | 2025-10-08 04:19:00 | NPP-375D | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5107b416-6808-37a1-a66b-09cc36a80aed | -18.55032 | -41.57421 | 2025-10-08 04:19:00 | NPP-375D | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 011fb9e6-7eb3-3428-a8b1-3e522ff83d4e | -14.70907 | -46.00472 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5855f37b-14b1-31a1-83dd-bbbefee5aafd | -14.36627 | -47.73423 | 2025-10-08 04:19:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5d4d701c-dedc-33f7-af64-cd081c82c8fb | -18.04601 | -43.147 | 2025-10-08 04:19:00 | NPP-375D | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f4a25f88-570b-31a4-a432-ce6ca1235e6e | -17.37439 | -45.0567 | 2025-10-08 04:19:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 004131ac-74c8-3d70-958b-6b387da941d1 | -17.28126 | -42.65006 | 2025-10-08 04:19:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9b02a03-b91f-3c14-b5fa-36120e8be4d3 | -7.2407 | -48.4774 | 2025-10-08 04:19:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 278344ac-4c65-3b85-8ed8-cb14742a487f | -16.58334 | -46.55984 | 2025-10-08 04:19:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b4bb92a-6781-3a0c-9e38-66d6ea8cb8d0 | -14.94698 | -46.79583 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 399958d5-4488-3994-a357-d3b25e579802 | -13.32587 | -48.02324 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d5792d8d-5004-3b8f-915a-bc699568500f | -13.74252 | -45.76084 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a88337de-088c-3472-bdf3-785be5a059f2 | -16.33803 | -47.04968 | 2025-10-08 04:19:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4062a436-d1dd-388f-9783-624708412afb | -18.03008 | -44.96515 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README50.md)
