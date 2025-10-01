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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4e9bdd1-51ed-3bcc-a22f-1e7d3be78aff | -20.23542 | -43.8782 | 2025-10-01 04:53:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 52fd6514-0cf1-3b01-ae3f-38e0459a6b0f | -19.85878 | -42.58668 | 2025-10-01 04:53:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a9c128a6-f132-3bff-9eb9-6a6e1591684e | -17.41076 | -47.16775 | 2025-10-01 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63475724-1dcb-34ea-86a3-3999cf3a25c7 | -18.48808 | -44.01928 | 2025-10-01 04:53:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 25301b60-928f-3552-a619-fd74975863b4 | -18.70938 | -49.16906 | 2025-10-01 04:53:00 | NPP-375D | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afd67e3d-c3c0-3011-8382-5c70ce27ce3d | -20.02442 | -44.54528 | 2025-10-01 04:53:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ec6b49f9-14bc-3762-a4ca-26dbd9da905a | -17.40262 | -47.16123 | 2025-10-01 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cfc1d822-3eb2-3eed-bb7c-3f07125e2681 | -21.9783 | -47.88721 | 2025-10-01 04:53:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ddfa6c8-a5f9-3e50-aa62-afebabd27a1c | -16.76762 | -51.33979 | 2025-10-01 04:53:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 44e4cea2-1323-3d70-a4cc-41e387af8157 | -20.849 | -49.43538 | 2025-10-01 04:53:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 73d1b167-0dd5-36ba-bd0b-e2578394595b | -16.83201 | -48.85041 | 2025-10-01 04:53:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23220c86-8bf2-3676-8450-4babd985a32d | -17.57816 | -45.38528 | 2025-10-01 04:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d845fbd-7272-36ed-81c7-8b468c49f92e | -19.89148 | -42.62946 | 2025-10-01 04:53:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b8391fc7-7a2e-381f-a48f-0b7d67fc76b9 | -17.28385 | -44.92036 | 2025-10-01 04:53:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8a8f4937-e5f7-3993-8570-f4ae36d3a23f | -17.96104 | -45.03876 | 2025-10-01 04:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a2294a7-8675-3353-bdcf-a95edd8fceb7 | -23.17135 | -45.73381 | 2025-10-01 04:53:00 | NPP-375D | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d571428f-a16a-3e5d-9412-5fd174c2ba87 | -17.67432 | -47.26381 | 2025-10-01 04:53:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3547c14e-7620-3300-8f59-e7f8fd2d0a06 | -15.8371 | -56.38803 | 2025-10-01 04:53:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfa0e028-fc44-3092-9213-9b6cfc802a10 | -15.3417 | -56.63557 | 2025-10-01 04:53:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a48f94c9-611c-376f-b602-4a2f722b88ba | -15.28721 | -56.79465 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3aee437-d6d2-3872-8ac7-1889ddd9146f | -22.11941 | -44.70392 | 2025-10-01 04:53:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f7d2a0c2-2bef-3d59-8913-ebe503260f55 | -17.57887 | -45.38602 | 2025-10-01 04:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02279236-83f8-3df3-9d41-4b155f6f6b15 | -15.84809 | -54.01796 | 2025-10-01 04:53:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a851cee2-82b6-3984-bcd5-05aa9ba5ebbd | -22.76449 | -45.78759 | 2025-10-01 04:53:00 | NPP-375D | SAPUCAÍ-MIRIM | MINAS GERAIS | Brasil | 3165404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 71cec0ac-3f02-3ca7-b1ad-6a6f0faffd33 | -17.40806 | -47.15347 | 2025-10-01 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 284b2e99-34f2-3865-ac3c-771d3a428f58 | -15.84983 | -59.59624 | 2025-10-01 04:53:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 400b5f45-b444-3438-8224-8235304d91cf | -22.43603 | -48.31473 | 2025-10-01 04:53:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 52f80cb8-4a8e-30da-8ff4-ac3708d24469 | -20.84832 | -49.44083 | 2025-10-01 04:53:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2f46d8fb-54a0-36f7-ab99-2491d7495413 | -15.34269 | -56.96058 | 2025-10-01 04:53:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 548f626f-d28a-3051-a5a0-5f7554ea642b | -22.7763 | -47.61396 | 2025-10-01 04:53:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 00343ea1-45dd-3b56-a1af-c3971afad020 | -17.43663 | -47.13994 | 2025-10-01 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd06edbc-ed67-3207-8016-0a0b14d3f121 | -20.63023 | -46.22101 | 2025-10-01 04:53:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 077cd05e-cc05-3114-9d1a-ccdd9a2694bd | -15.29251 | -56.78628 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53e53a0f-6c62-334f-a4b2-4aa0d8c66ab8 | -16.24887 | -50.93452 | 2025-10-01 04:53:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96c478ae-fff2-387d-9d37-3ccfcc8391f5 | -15.26881 | -56.79068 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d79f8e1d-a998-3b02-847a-d3935cba073d | -15.34269 | -56.96282 | 2025-10-01 04:53:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0be6b5ff-3173-32f1-ac74-19adff55e7cd | -22.57704 | -46.7789 | 2025-10-01 04:53:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.6 |
| 32f354c9-2a3c-3153-8eee-7b8d5d21a409 | -19.37802 | -42.77787 | 2025-10-01 04:53:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ca959bb0-6306-3b68-9c3e-52f65fffa651 | -20.62533 | -46.22044 | 2025-10-01 04:53:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f18ed3a4-ef13-32c3-9e3d-a51b97ca6182 | -19.86771 | -43.8243 | 2025-10-01 04:53:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 8b7c16c1-8fed-3d25-b354-d68f8214dd46 | -22.44044 | -48.31499 | 2025-10-01 04:53:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0a79445a-83d1-3178-a9d6-b0c9b0fd29a8 | -20.49471 | -43.93634 | 2025-10-01 04:53:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| fd445426-b597-3183-9621-1cea92f7eefa | -19.86514 | -43.82195 | 2025-10-01 04:53:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| a6972441-d29b-3a3b-8581-d034278e3ae4 | -16.25238 | -50.93507 | 2025-10-01 04:53:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cbe81ca7-88cc-3de8-98d3-d1d35f0821f5 | -19.63593 | -46.55252 | 2025-10-01 04:53:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9595e79-0e7a-34d3-932b-f42e5f05736f | -19.85825 | -42.58725 | 2025-10-01 04:53:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 664ee276-8dea-3614-8a0b-fee125b44b64 | -16.36171 | -49.96436 | 2025-10-01 04:53:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8ca55871-9e8a-3cc3-b7e6-f8361810a83d | -20.48524 | -43.94655 | 2025-10-01 04:53:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 396217d6-a024-3717-96e0-03f9033bd4be | -15.26756 | -56.77622 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8dc96c54-932d-333b-9b60-b7cc398a8355 | -17.96397 | -45.01233 | 2025-10-01 04:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf931df3-f372-3ee1-a2c5-6a0e10ffc179 | -20.12533 | -46.33614 | 2025-10-01 04:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 519bd42c-e64a-321a-9557-ddef91b1b6f3 | -18.70384 | -49.16932 | 2025-10-01 04:53:00 | NPP-375D | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8300c24e-d795-3c52-9adc-e1e7b5a7aad6 | -19.9346 | -43.89899 | 2025-10-01 04:53:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| aa2ad578-096f-3cc1-9868-cd7c88a9cf8b | -17.96841 | -45.0191 | 2025-10-01 04:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cb28081-94fb-342a-b817-0007dc85c523 | -23.16592 | -45.73722 | 2025-10-01 04:53:00 | NPP-375D | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 45b0f557-5b51-3613-b071-ba265bc29787 | -20.32835 | -43.03909 | 2025-10-01 04:53:00 | NPP-375D | BARRA LONGA | MINAS GERAIS | Brasil | 3105707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a4b2df0a-2958-3fe9-9cb0-86740427d297 | -22.43217 | -48.30985 | 2025-10-01 04:53:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a0774e7e-54c0-37be-99eb-f49aaaea8148 | -15.25303 | -56.78366 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd63c71b-97d2-301c-b706-5857bd98a708 | -18.80965 | -47.55348 | 2025-10-01 04:53:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f621dab1-a9d9-33a7-9ce6-0fb56b7f499c | -19.74365 | -42.01159 | 2025-10-01 04:53:00 | NPP-375D | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8ad64a7c-7aeb-3960-96a8-302a2c74f756 | -20.49176 | -43.93859 | 2025-10-01 04:53:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 43c84fad-a7cd-36c9-9eb8-4b1d9132700d | -16.76357 | -51.34321 | 2025-10-01 04:53:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aab2aa11-6c55-3b6e-b559-4c15e75bb3d6 | -22.65684 | -46.74632 | 2025-10-01 04:53:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8161bb4d-5d69-3531-b7d7-06e0819f0359 | -18.61006 | -43.27448 | 2025-10-01 04:53:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8ff583c7-d659-3490-966c-fa3c60372672 | -19.85832 | -42.59151 | 2025-10-01 04:53:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b999bd44-cd21-3993-958f-1e9922069c49 | -18.80513 | -47.55043 | 2025-10-01 04:53:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eea071a4-9c6c-3ee0-81f8-0b35563b8c18 | -22.25729 | -43.4355 | 2025-10-01 04:53:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b76447ad-0cc8-3d88-939a-bd375d385a7f | -15.27332 | -56.7868 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a5f70be3-f3b0-3cb7-8550-3e89deb47460 | -16.25296 | -50.93109 | 2025-10-01 04:53:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25a74000-4fe7-3476-a519-bc36f0a20b78 | -20.4868 | -43.95953 | 2025-10-01 04:53:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3e854a19-bba2-36df-b976-c167fc940a32 | -15.27699 | -56.78767 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4dec858-0a74-3f8f-bf57-a4fa63258bbd | -17.20649 | -46.98312 | 2025-10-01 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9fbf4aad-3a5d-3c08-a6f4-3709ff021d6e | -15.23804 | -56.80412 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 560bd147-0a4a-3067-a800-eb9c8372fd12 | -18.30853 | -46.61243 | 2025-10-01 04:53:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce289745-490c-366f-a246-54292d8f42eb | -20.02544 | -44.53517 | 2025-10-01 04:53:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cf70d98b-f515-3438-b074-5941e7493800 | -18.70777 | -49.16996 | 2025-10-01 04:53:00 | NPP-375D | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5df7b8bc-bddc-34c6-9bb5-a5e8de888003 | -22.28668 | -47.73166 | 2025-10-01 04:53:00 | NPP-375D | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa1dee60-45e5-3229-b1c6-7e8488f90e2e | -15.26826 | -56.77225 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f20a4d02-9c27-364e-9984-a46709198411 | -18.96547 | -47.86908 | 2025-10-01 04:53:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6457624-227e-32f5-8b0f-4d318a4d8897 | -20.58603 | -45.88553 | 2025-10-01 04:53:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0340180-2e2c-3347-82fd-08bc8832e376 | -17.4037 | -47.15253 | 2025-10-01 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07e95e1e-4634-36a4-9950-638e1e1bf0ab | -16.19084 | -57.60137 | 2025-10-01 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 5c34fa24-66d5-3e52-9431-add548a1fd46 | -19.16144 | -44.53139 | 2025-10-01 04:53:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d90ef5ad-afea-3645-bf96-bee04f1dc3b5 | -20.21966 | -43.44668 | 2025-10-01 04:53:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8b92ab44-6ba0-3c84-80a3-ff1e15e89f24 | -19.81123 | -44.0701 | 2025-10-01 04:53:00 | NPP-375D | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f07de9b-d8e5-3990-860e-d3b34843bdc8 | -20.22481 | -43.44405 | 2025-10-01 04:53:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 619b59ed-9736-3bc0-a9e6-b50ddfbcfe6a | -20.11861 | -46.33768 | 2025-10-01 04:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5947f85a-2c32-336a-949a-ce781609744f | -22.06038 | -43.07545 | 2025-10-01 04:53:00 | NPP-375D | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 02cdc3b5-95a2-37a6-a999-9fd08085d3ac | -17.21607 | -49.61494 | 2025-10-01 04:53:00 | NPP-375D | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71af093a-3048-380f-a231-38c4089ceeb3 | -23.20782 | -45.10983 | 2025-10-01 04:53:00 | NPP-375D | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fde954ef-ed75-3a79-a53a-65281d90ec99 | -16.25646 | -50.93164 | 2025-10-01 04:53:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1cb9f559-f548-3450-abc4-fee7dc6459db | -17.40095 | -47.17468 | 2025-10-01 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1c65cb4-bd1b-3554-bdb7-81c941381586 | -17.51038 | -43.4855 | 2025-10-01 04:53:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79074a3c-47f4-31de-b017-d7e07962b459 | -20.47608 | -43.95204 | 2025-10-01 04:53:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5b8e4cc1-0df0-3f00-a535-914d3a4bf8a9 | -18.62933 | -50.70679 | 2025-10-01 04:53:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5fc6d6d2-bed4-3d5a-ae02-08780a097875 | -15.25673 | -56.85123 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6132ffb1-da96-3729-bd4d-378fdc87666c | -20.4792 | -43.94968 | 2025-10-01 04:53:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 18255680-089d-3ca6-8050-a4a8738368ed | -16.24479 | -50.93794 | 2025-10-01 04:53:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab6d4836-50fc-38d5-94bf-326e718a92f8 | -19.88564 | -42.62815 | 2025-10-01 04:53:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4f238ed4-e25b-37e6-86f0-ec3aff3bd2bc | -17.95821 | -45.01746 | 2025-10-01 04:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README117.md)
