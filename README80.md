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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ddbad12-7b9f-3f83-a145-31993ce17df0 | -16.4193 | -49.06539 | 2025-09-14 12:19:00 | TERRA_M-T | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ea2afe74-6915-3046-838c-1f597458f885 | -20.67525 | -54.6985 | 2025-09-14 12:19:00 | TERRA_M-T | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 203ebd78-c91a-3ef5-92bf-fd90d0a04f3d | -22.50736 | -50.62133 | 2025-09-14 12:19:00 | TERRA_M-T | PARAGUAÇU PAULISTA | SÃO PAULO | Brasil | 3535507 | 35 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 1a09801f-db8d-383f-a937-7b0feffb9c6f | -15.76559 | -52.2465 | 2025-09-14 12:19:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 2d68db8c-73d9-39eb-ae3f-5639e39464b0 | -15.78832 | -53.48709 | 2025-09-14 12:19:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 455e7b9e-0fd4-3fc3-8d3c-6307460465e3 | -16.41795 | -49.07464 | 2025-09-14 12:19:00 | TERRA_M-T | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2e411ed5-d3c5-3235-b4c6-319215fcf32a | -22.5339 | -52.99961 | 2025-09-14 12:19:00 | TERRA_M-T | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| f2b3e2c1-6088-396a-bac8-1363af0f8cbe | -16.99201 | -43.96516 | 2025-09-14 12:19:00 | TERRA_M-T | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 27.8 |
| f5c9a7cd-417d-36cd-98ce-8c0c80ca0325 | -14.26738 | -45.0616 | 2025-09-14 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e5e3904d-2365-3528-bb82-c5bf9c4964ad | -17.60693 | -44.17476 | 2025-09-14 12:19:00 | TERRA_M-T | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f1a28ab7-10e7-372f-94bd-9582be4194b8 | -15.26926 | -47.2508 | 2025-09-14 12:19:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6bec96de-e80d-395e-a2b3-5227afc84a91 | -18.60587 | -47.20768 | 2025-09-14 12:19:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| d8a626ab-6f23-3975-86f4-8a4f27b37964 | -13.26555 | -51.67324 | 2025-09-14 12:19:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 04f04ac5-598e-31fe-966a-a52057a2430d | -14.80183 | -48.14075 | 2025-09-14 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b65ed86b-fbfa-327a-b468-5dd9a75b791c | -17.61783 | -44.17638 | 2025-09-14 12:19:00 | TERRA_M-T | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5a316e40-c6a1-3604-93bd-b0d7ffd309d8 | -16.66404 | -49.78125 | 2025-09-14 12:19:00 | TERRA_M-T | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 6621b534-f11a-3fcc-a6e8-edd966929be6 | -14.48202 | -47.35235 | 2025-09-14 12:19:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ec6854ff-8006-31fe-a8ba-0d9ec9c8ce13 | -17.25727 | -47.24811 | 2025-09-14 12:19:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f6307f8b-dbd3-3260-9f28-82e46df40340 | -14.19481 | -46.15854 | 2025-09-14 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1b44918d-21bd-328a-9f62-f4362c3982af | -17.27266 | -46.10529 | 2025-09-14 12:19:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| abecd6cc-784c-3891-86e3-231a0d1b69d6 | -15.79481 | -52.19839 | 2025-09-14 12:19:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 1d3a0956-9226-349e-96c2-2c5713cc5611 | -15.75219 | -49.77097 | 2025-09-14 12:19:00 | TERRA_M-T | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5e9aa22e-9a7b-3512-a705-de2f338348b9 | -15.54008 | -48.3352 | 2025-09-14 12:19:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f0dc5409-1cb6-31fb-8647-c42d7edc0707 | -20.38233 | -50.51883 | 2025-09-14 12:19:00 | TERRA_M-T | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| a606db21-5f42-3f26-8e44-f1149c6d1da3 | -14.39611 | -52.90717 | 2025-09-14 12:19:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 7eb74ef5-10a8-3157-bcdf-6e903bf33e96 | -15.6388 | -44.37276 | 2025-09-14 12:19:00 | TERRA_M-T | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e32e0f0b-8a32-372f-8ee3-3684064f591b | -14.469 | -47.3065 | 2025-09-14 12:19:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 906d42bb-e616-3eeb-a005-dcee8bc5c716 | -13.92873 | -44.8415 | 2025-09-14 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 7a534f79-c617-3218-81e4-4df6de60b6a7 | -16.6565 | -49.76997 | 2025-09-14 12:19:00 | TERRA_M-T | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 72b8712a-45a6-3257-a959-52754d9e3600 | -15.80312 | -52.21267 | 2025-09-14 12:19:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 80623fa9-837f-3d0d-8b41-438143259c31 | -14.3162 | -46.08018 | 2025-09-14 12:19:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 103.2 |
| d80ffda5-84e9-38a1-951b-80c52fa0b4d5 | -14.11959 | -45.16488 | 2025-09-14 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c91eddc2-1945-300b-ac0b-2581fe49eec9 | -17.98722 | -46.95245 | 2025-09-14 12:19:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4ca39673-5c11-3259-b149-7bdbad6e0c40 | -14.81067 | -48.14206 | 2025-09-14 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 19.5 |
| ddf5026c-e613-3e4e-abfa-d266869b74c4 | -20.13039 | -46.86943 | 2025-09-14 12:19:00 | TERRA_M-T | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| aad92ba7-2a11-3bc9-bd9a-b545d8afccd5 | -16.66259 | -49.79094 | 2025-09-14 12:19:00 | TERRA_M-T | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 2b0b4b32-b536-30a3-81a4-f698d7385f47 | -13.18214 | -47.28526 | 2025-09-14 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 33.5 |
| bd35ea7e-965d-3f1d-a14e-8af96497e301 | -23.32561 | -47.63715 | 2025-09-14 12:19:00 | TERRA_M-T | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| e7e8bd4b-5235-3247-9282-d4eb410d4ce6 | -15.60505 | -47.94409 | 2025-09-14 12:19:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 02844da7-1f3c-3870-9dab-1538ad893270 | -15.08581 | -48.02531 | 2025-09-14 12:19:00 | TERRA_M-T | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9537e282-bb00-3753-a0c9-203d1325e8e2 | -14.32277 | -46.10139 | 2025-09-14 12:19:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 182.1 |
| e17afd32-7aa0-3a6f-beee-50f512482f2d | -14.48461 | -47.3337 | 2025-09-14 12:19:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 50ba8b3f-f36a-3f6b-b53b-f40bb0ba8695 | -17.36527 | -52.89277 | 2025-09-14 12:19:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 991779ff-e2c0-39b4-8654-18c22145f8aa | -18.46767 | -46.93825 | 2025-09-14 12:19:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8493050f-0894-3392-8f13-199741a12c79 | -15.79268 | -52.21141 | 2025-09-14 12:19:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 54bac54c-d858-316f-a0d9-c04bc21e32e9 | -15.97731 | -46.92233 | 2025-09-14 12:19:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c9711b5e-7d72-3dcd-a946-ace1753ad9b7 | -18.64152 | -51.79822 | 2025-09-14 12:19:00 | TERRA_M-T | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 7bac926a-3734-34b6-bf65-bb958dc6517c | -14.39175 | -47.07167 | 2025-09-14 12:19:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 20bdff58-e000-36f9-859b-232c0de1c604 | -14.32547 | -46.08138 | 2025-09-14 12:19:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 35.1 |
| bac5d2df-1940-38e6-be01-334e15a2be22 | -14.16869 | -46.15865 | 2025-09-14 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ff808af6-27b9-3386-8f6b-08627be41aaf | -17.14445 | -48.51407 | 2025-09-14 12:19:00 | TERRA_M-T | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7867ed74-b204-3af2-9584-8f80329b3f71 | -15.93378 | -47.23757 | 2025-09-14 12:19:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| c3716d16-ef4f-3463-92aa-3659291dd704 | -15.03661 | -47.99022 | 2025-09-14 12:19:00 | TERRA_M-T | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| a970acbc-96e0-3bca-be11-24f6be7a1a54 | -15.13231 | -48.02893 | 2025-09-14 12:19:00 | TERRA_M-T | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 98be9fea-aae5-379c-b169-3a13d7731654 | -15.08451 | -48.03442 | 2025-09-14 12:19:00 | TERRA_M-T | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 51ba3582-1b72-3f98-adf2-3c0cdd56ff08 | -12.699 | -54.67848 | 2025-09-14 12:19:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 673f4cd9-f37f-35b6-b9a2-7a176ddeac88 | -18.02412 | -46.95801 | 2025-09-14 12:19:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| ae6fef88-4e8f-3738-a74e-74da31207547 | -14.4665 | -55.95869 | 2025-09-14 12:19:00 | TERRA_M-T | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 29.6 |
| e3716a85-d180-3138-8578-6eff1cb7f0d2 | -14.42685 | -47.3476 | 2025-09-14 12:19:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 20.9 |
| e29bae33-a2be-36e8-800b-bbec4692d5ce | -14.40071 | -47.07296 | 2025-09-14 12:19:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| a526720e-8491-3136-98cb-02c80b755a1b | -22.79096 | -46.78924 | 2025-09-14 12:19:00 | TERRA_M-T | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.0 |
| 62da8d5b-9a56-372b-ae00-92ef082fe71f | -19.72034 | -45.44045 | 2025-09-14 12:19:00 | TERRA_M-T | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 7cdadaef-e926-3e25-9278-8c46e2bd36fb | -15.75964 | -52.23965 | 2025-09-14 12:19:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 9b3b4a6c-3d46-3a2e-9c00-59662b8514e6 | -15.16966 | -52.46765 | 2025-09-14 12:19:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| c70d1fb6-3dae-3e0f-9314-26bc95bdee58 | -15.41264 | -52.96999 | 2025-09-14 12:19:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| d8451c51-96bd-35d6-a1ec-f471ed7ab3e5 | -20.39132 | -50.52033 | 2025-09-14 12:19:00 | TERRA_M-T | PONTALINDA | SÃO PAULO | Brasil | 3540259 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| f19fe494-98c0-3b08-83f7-7e74c987c9e3 | -16.12994 | -47.87423 | 2025-09-14 12:19:00 | TERRA_M-T | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ee5869d3-f245-3289-b911-923324cb9769 | -15.04416 | -48.00059 | 2025-09-14 12:19:00 | TERRA_M-T | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f87364c4-7094-322b-8ed8-be3d09d64358 | -12.94209 | -54.73395 | 2025-09-14 12:19:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 6916399f-8086-340b-861a-65cf100b8688 | -18.62694 | -47.19047 | 2025-09-14 12:19:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 2bbfe116-6834-3c5d-8268-42f3cd69ea05 | -13.83804 | -47.34659 | 2025-09-14 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 50e87b5e-4810-380a-9b6a-0b6dc3049af6 | -13.9455 | -44.86699 | 2025-09-14 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 284.3 |
| 7afac5b5-ad0b-398f-b36e-23bb00ad522b | -16.0363 | -47.94839 | 2025-09-14 12:19:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 9fc53103-d084-3190-8d0a-490d8bfea765 | -14.48331 | -47.34306 | 2025-09-14 12:19:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| fbdd4ab8-fb76-35ae-b360-0118ba2032d4 | -15.72932 | -56.21882 | 2025-09-14 12:19:00 | TERRA_M-T | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 85c5cd18-2137-323c-b546-f362c164061f | -16.47732 | -49.29888 | 2025-09-14 12:19:00 | TERRA_M-T | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a8264a71-31a2-3532-b243-0ef6df59e23c | -15.17184 | -52.45398 | 2025-09-14 12:19:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 143f69ed-382f-3939-a508-49fde41682d7 | -15.60299 | -49.03492 | 2025-09-14 12:19:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| af97d59d-9c31-303e-b7ce-2e31ccbb7846 | -17.25857 | -47.23845 | 2025-09-14 12:19:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 60afe59e-5fce-38ff-8c02-22adece1cec4 | -14.32412 | -46.09138 | 2025-09-14 12:19:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 314.2 |
| f4284990-c4dc-3c60-abb8-a961e9189e38 | -14.42815 | -47.33834 | 2025-09-14 12:19:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 703b907d-9aec-3b55-bd84-13de5ac21317 | -15.58009 | -47.13288 | 2025-09-14 12:19:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 26f3f4c2-a12b-3b7f-bf89-70f15ada4890 | -15.75761 | -52.25242 | 2025-09-14 12:19:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ea5813ae-9267-32da-a189-fc0ee4df8643 | -22.49844 | -50.61982 | 2025-09-14 12:19:00 | TERRA_M-T | PARAGUAÇU PAULISTA | SÃO PAULO | Brasil | 3535507 | 35 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 05483867-9dfd-3fe7-ab52-8e3eed3aa093 | -15.17555 | -52.4609 | 2025-09-14 12:19:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 5b7c28c7-d4d0-3579-8bde-e279e957a662 | -14.30035 | -46.05755 | 2025-09-14 12:19:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7dec0b4c-8756-30cd-9cb5-a5a59da8b28a | -16.66551 | -49.77136 | 2025-09-14 12:19:00 | TERRA_M-T | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| da6c62d5-aeb4-3fad-8fc5-24d4dbaa30c1 | -22.49701 | -50.62947 | 2025-09-14 12:19:00 | TERRA_M-T | PARAGUAÇU PAULISTA | SÃO PAULO | Brasil | 3535507 | 35 | 33 | nan | nan | nan | Cerrado | 322.1 |
| 66367ecc-f553-3d25-a5c1-9b2082be1715 | -14.46952 | -55.96639 | 2025-09-14 12:19:00 | TERRA_M-T | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 3dd55742-53e6-338a-ada0-5d29b2459ed2 | -17.28777 | -48.73643 | 2025-09-14 12:19:00 | TERRA_M-T | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 16238ed9-50d1-3b34-8d9f-de35f2fa1e63 | -14.20271 | -46.16968 | 2025-09-14 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| dab81ed3-c0c7-3fb2-95da-46f514fb4815 | -22.49556 | -50.63914 | 2025-09-14 12:19:00 | TERRA_M-T | PARAGUAÇU PAULISTA | SÃO PAULO | Brasil | 3535507 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c3d2ca0b-59de-3431-acea-ebe41d2da7a1 | -16.43762 | -45.69485 | 2025-09-14 12:19:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 19.4 |
| eb670b92-ad92-3cf0-a468-e4e173af2b47 | -14.20927 | -46.19062 | 2025-09-14 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 24.5 |
| ceaeeaf5-afe1-3000-bc3b-d9a6ef4f0a58 | -14.29084 | -45.11025 | 2025-09-14 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 5e4de9e0-956f-32da-b563-979d0ca4da92 | -15.76543 | -53.48396 | 2025-09-14 12:19:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3f4e72ae-3829-3ba9-9906-a7306a2b73c4 | -18.02277 | -46.96803 | 2025-09-14 12:19:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 69ee30b6-5bed-3dca-a27b-57dd93284ea0 | -19.05342 | -47.70331 | 2025-09-14 12:19:00 | TERRA_M-T | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 98d06799-b186-374c-9c49-e9e0e11662c4 | -15.47098 | -47.32122 | 2025-09-14 12:19:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a9dced06-86a9-3369-8c0e-cc5c21e664b8 | -15.09906 | -52.497 | 2025-09-14 12:19:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |


[Clique aqui para ver as próximas entradas](README81.md)
