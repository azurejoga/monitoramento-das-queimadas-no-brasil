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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4053bba6-25f9-36c2-9940-e812b0c890a7 | -23.32975 | -46.55086 | 2025-09-11 04:27:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7e27b373-3c40-335f-8151-c74bfbbca77f | -23.31067 | -47.34245 | 2025-09-11 04:27:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1e5f2969-8a33-32a3-ba92-4c69f64999fc | -23.11049 | -46.85922 | 2025-09-11 04:27:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bcbe4110-55b2-3ea9-acd1-3853dda142bc | -23.33339 | -47.30662 | 2025-09-11 04:27:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 93bb3d4f-0790-3fad-a7d6-f12072e729d8 | -23.34057 | -47.21203 | 2025-09-11 04:27:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a45fcaa5-6315-3fa4-a149-66c801c4d907 | -22.6692 | -53.12296 | 2025-09-11 04:27:00 | NPP-375D | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a7aacdd2-9c3d-3875-8fdc-a0f7c8e453a9 | -21.69069 | -56.51195 | 2025-09-11 04:27:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4204aac6-e027-3188-8a8a-34e5bc81a924 | -23.16281 | -47.32939 | 2025-09-11 04:27:00 | NPP-375D | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 81fc1793-c35c-323c-a643-47e66d556bf3 | -23.1474 | -48.25445 | 2025-09-11 04:27:00 | NPP-375D | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 1f340198-83d9-3f0e-8e78-a865c68b7121 | -23.23066 | -46.69934 | 2025-09-11 04:27:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8afc60d8-aea4-3dd5-9c35-cffa3dbe4ee1 | -23.30671 | -47.34571 | 2025-09-11 04:27:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8a8f1779-1e68-3fd7-aaac-5890580dc23c | -23.06676 | -54.20257 | 2025-09-11 04:27:00 | NPP-375D | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ac587e87-370b-3957-a2bb-472b16e8dd17 | -23.33163 | -47.31833 | 2025-09-11 04:27:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ca70f55d-52db-3a93-89a1-fad5a84ba065 | -23.33443 | -47.3228 | 2025-09-11 04:27:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 36f687a2-2aff-39b7-ab91-84d27a85573f | -23.67207 | -46.82336 | 2025-09-11 04:27:00 | NPP-375D | EMBU DAS ARTES | SÃO PAULO | Brasil | 3515004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 70f60b47-fbe4-348e-bad9-935213a34413 | -23.10654 | -49.79284 | 2025-09-11 04:27:00 | NPP-375D | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bd3326f4-9e2f-376b-89f8-cd7dac611305 | -23.14681 | -48.25823 | 2025-09-11 04:27:00 | NPP-375D | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0280f386-62c1-3768-b82f-b7e698804d03 | -21.68808 | -56.51076 | 2025-09-11 04:27:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e15ee250-0a8d-3ef0-bf23-c8c9af142441 | -22.97413 | -49.74818 | 2025-09-11 04:27:00 | NPP-375D | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 5358b0f3-ef84-3e2f-a80e-cff410e5145f | -22.59193 | -51.89937 | 2025-09-11 04:27:00 | NPP-375D | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 043e8a9e-0f55-3bb9-99e4-4f92e0d46606 | -23.14785 | -46.93861 | 2025-09-11 04:27:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c90b14b0-1300-31e3-85a7-63528eb51480 | -22.66439 | -53.12726 | 2025-09-11 04:27:00 | NPP-375D | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bf8ecf90-f791-3af3-8780-fb147756902a | -22.59357 | -51.89034 | 2025-09-11 04:27:00 | NPP-375D | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| 85ce6268-71da-3109-a423-5455081c738c | -22.59523 | -51.88128 | 2025-09-11 04:27:00 | NPP-375D | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b975c086-2248-3425-ae85-3b170f0ea3ab | -23.47302 | -46.20624 | 2025-09-11 04:27:00 | NPP-375D | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4c731833-4b37-35e1-908c-55c3b4277df4 | -23.76913 | -49.04805 | 2025-09-11 04:27:00 | NPP-375D | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a7c2e766-1905-3579-be05-e8d74bf87f5a | -23.59901 | -46.97176 | 2025-09-11 04:27:00 | NPP-375D | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1bf030f7-bbfa-3fb2-84d9-71cb81081e02 | -24.4744 | -50.81323 | 2025-09-11 04:27:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 35ed7e15-37c7-349f-8bb3-a5a18b11b09f | -22.93168 | -48.38249 | 2025-09-11 04:27:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 5796db29-4e11-329f-9b57-a5eb02014c26 | -23.14622 | -48.26202 | 2025-09-11 04:27:00 | NPP-375D | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 60fed897-7f14-33a3-81a8-535c6e3617aa | -23.35075 | -47.21378 | 2025-09-11 04:27:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a20bf0d2-52fc-3f5a-ae9c-34ea6201bdaf | -22.97076 | -49.74754 | 2025-09-11 04:27:00 | NPP-375D | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a5a731cb-ecf7-3b44-a606-369ff5efe3bd | -23.52156 | -46.97446 | 2025-09-11 04:27:00 | NPP-375D | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 30c5df5b-bb7e-3be9-836c-f0e4821e3bec | -23.34116 | -47.20813 | 2025-09-11 04:27:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 5be34711-12da-3941-8261-7a3a67959658 | -23.76852 | -49.05183 | 2025-09-11 04:27:00 | NPP-375D | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ec5e4506-e060-35cd-9538-3b35eed47caf | -22.87557 | -49.19672 | 2025-09-11 04:27:00 | NPP-375D | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 59ba5b75-c843-317e-b1f4-567680fece54 | -23.34913 | -47.31739 | 2025-09-11 04:27:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 86dc263e-bc03-3fbd-8849-433cdf5f5ed1 | -23.34237 | -47.3162 | 2025-09-11 04:27:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c8d28728-c46c-3f40-9186-ee1b9ff2cea4 | -22.8769 | -48.53467 | 2025-09-11 04:27:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8b3c4414-ae1c-3e91-ae11-93ce9a153e53 | -22.58995 | -51.89211 | 2025-09-11 04:27:00 | NPP-375D | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 7344e50f-fbd2-39b2-a9e2-d46a4b7bfb1b | -22.58634 | -51.89129 | 2025-09-11 04:27:00 | NPP-375D | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6295aa51-0b96-3319-9405-18ab7723298e | -23.4736 | -46.20218 | 2025-09-11 04:27:00 | NPP-375D | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1954814d-c70f-3a63-a23b-580dcc3dacc7 | -23.02913 | -50.10992 | 2025-09-11 04:27:00 | NPP-375D | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8c7af8db-d377-3f07-ad2a-bc51910b3921 | -23.38972 | -46.85631 | 2025-09-11 04:27:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 62b5c793-1733-3747-9996-dc02ae217dae | -23.33899 | -47.3156 | 2025-09-11 04:27:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 407f847a-52f3-3f5c-bee2-92a11a41a40c | -22.59517 | -51.88385 | 2025-09-11 04:27:00 | NPP-375D | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 66f3eed3-eb0a-3f95-8218-9ae935464d64 | -22.59436 | -51.88838 | 2025-09-11 04:27:00 | NPP-375D | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 501e54e8-8652-3449-a499-5140e0fcfb29 | -23.06753 | -54.19865 | 2025-09-11 04:27:00 | NPP-375D | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ed9c0969-03c3-3532-8cd1-c6689b8aa45b | -22.59356 | -51.89291 | 2025-09-11 04:27:00 | NPP-375D | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 110a5750-a748-38ec-8ec0-0146db236bfb | -23.09558 | -52.47246 | 2025-09-11 04:27:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| bb86072d-5935-307b-85bf-b91958339ad9 | -23.38913 | -46.86026 | 2025-09-11 04:27:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f309b3eb-51a8-363e-aab4-23318f5adb21 | -23.34946 | -47.31622 | 2025-09-11 04:27:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ec58bacb-a80e-3e94-92c8-9636cef7384a | -24.51836 | -49.79472 | 2025-09-11 04:27:00 | NPP-375D | PIRAÍ DO SUL | PARANÁ | Brasil | 4119400 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2a0b36ea-21ad-3ffc-be2a-493c04c16e81 | -22.9311 | -48.38625 | 2025-09-11 04:27:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 728ccdd5-fed3-3376-8089-7fe1cae07baf | -22.59156 | -51.88303 | 2025-09-11 04:27:00 | NPP-375D | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 369d0c2f-67a9-312e-a89f-a2004d63271d | -22.5944 | -51.88581 | 2025-09-11 04:27:00 | NPP-375D | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| c5ea3941-4d66-37d4-b208-250321290842 | -23.33105 | -47.32223 | 2025-09-11 04:27:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 441b8dd2-2bbf-33fc-b422-2d8c2a77b9b6 | -22.86451 | -51.23176 | 2025-09-11 04:27:00 | NPP-375D | ALVORADA DO SUL | PARANÁ | Brasil | 4100806 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4d7184dd-fcc7-34aa-98d8-78b720e6bca9 | -23.3356 | -47.315 | 2025-09-11 04:27:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 865f6a09-671a-3d23-b1e9-eb101bb5eb87 | -22.59801 | -51.88662 | 2025-09-11 04:27:00 | NPP-375D | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| a07f51fb-090a-3ca2-bd42-994fd4c8995c | -22.97749 | -49.74883 | 2025-09-11 04:27:00 | NPP-375D | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 00f6756d-fea0-3778-ae5d-f96c4a93314e | -23.25453 | -45.97351 | 2025-09-11 04:27:00 | NPP-375D | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d3e533ab-4211-3178-9847-ff8a718c21b4 | -23.23181 | -46.69136 | 2025-09-11 04:27:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1f62d3a1-9ac3-3f62-9774-a7ead3412d93 | -22.59276 | -51.89744 | 2025-09-11 04:27:00 | NPP-375D | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 83c8ec66-24a2-3df6-b2ef-f9ee4b6b4eb8 | -23.23238 | -46.68736 | 2025-09-11 04:27:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bf7f7c52-a7d1-3c7c-9802-1d63d2a89345 | -23.77186 | -49.05246 | 2025-09-11 04:27:00 | NPP-375D | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4dfbfbc2-785c-3f2a-aeb6-3db9a67fc6a9 | -22.58915 | -51.89666 | 2025-09-11 04:27:00 | NPP-375D | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 51b79362-eb80-306f-b3ee-decf92a704c8 | -22.59076 | -51.88757 | 2025-09-11 04:27:00 | NPP-375D | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 216a1f2f-f799-327f-a94c-b839dc59503f | -23.34794 | -47.20929 | 2025-09-11 04:27:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 95dc5987-934d-301d-aabf-75e326ed517b | -23.25394 | -45.97776 | 2025-09-11 04:27:00 | NPP-375D | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 304f03dd-3125-3616-9d94-09efba859341 | -23.34595 | -47.15261 | 2025-09-11 04:27:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 25685a80-7d96-3836-a8a1-f7a8109b6ede | -23.22845 | -49.42934 | 2025-09-11 04:27:00 | NPP-375D | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| adf97665-4751-3ef9-aeaa-0f613cebadf0 | -23.35249 | -47.20211 | 2025-09-11 04:27:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dbdd81e1-1b1c-3301-91e7-5c99929b0ff5 | -22.59275 | -51.89486 | 2025-09-11 04:27:00 | NPP-375D | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 5d57f09a-cf46-315e-9e89-be8833acfb05 | -22.58553 | -51.89584 | 2025-09-11 04:27:00 | NPP-375D | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5ea5c8a6-7c2c-3d37-b184-14e8f49f38d0 | -23.34736 | -47.21317 | 2025-09-11 04:27:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f0df5350-3f2c-32ea-a6c0-a1875b892806 | -24.1975 | -51.76127 | 2025-09-11 04:27:00 | NPP-375D | JARDIM ALEGRE | PARANÁ | Brasil | 4112504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7dbd0f58-a5ad-384b-9eba-bc45e9acc31e | -23.34397 | -47.21259 | 2025-09-11 04:27:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 70214b13-bb38-3797-8dde-52eead08c4b3 | -22.59798 | -51.88918 | 2025-09-11 04:27:00 | NPP-375D | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| eb1f9f10-7d5f-3260-986d-cd4ca678d29c | -23.35414 | -47.21439 | 2025-09-11 04:27:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b8ac105e-23f8-3c52-b018-e716c8db55ac | 4.13126 | -59.97295 | 2025-09-11 04:42:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ea4982dd-9fc9-3479-97cf-c5a613af48e4 | 1.02887 | -51.3474 | 2025-09-11 04:42:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22661775-5816-3167-832b-21cf6fa7c44b | 1.0323 | -51.34686 | 2025-09-11 04:42:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f954be0d-70f3-3ae2-ab80-35eb98499fcc | 0.16365 | -51.1055 | 2025-09-11 04:42:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fabf356-6570-36a0-9af9-4e74a806c0d1 | -0.13169 | -49.16785 | 2025-09-11 04:42:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70afdecf-df7e-31f3-8dcc-63c9b3e848f5 | 0.7563 | -50.77182 | 2025-09-11 04:42:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06f192b4-d7de-3553-b931-b676c06967eb | -7.98844 | -45.79638 | 2025-09-11 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6d0d0fb2-5e90-39d1-95bb-1ac66a2baee9 | -3.45736 | -54.61425 | 2025-09-11 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5490ff8-2792-3c61-847c-17a6c0070a84 | -6.32665 | -47.74677 | 2025-09-11 04:44:00 | NOAA-20 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| afd41d72-2a29-3c12-9d5d-56d89aa6d793 | -7.90236 | -46.25715 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| db501527-3f87-37a7-b24f-375b5a362968 | -8.07866 | -52.35627 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 511aa4fa-30dc-36ef-90f6-4149551e215c | -8.73578 | -47.09058 | 2025-09-11 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c856eab1-f15a-36f3-b56c-58ba6e505e3b | -8.04109 | -49.05703 | 2025-09-11 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 70c3acd9-c663-3073-b58c-1a3d6a67e0df | -6.68397 | -44.54345 | 2025-09-11 04:44:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1798fbb3-548d-337d-9344-7804aca95b67 | -6.65257 | -51.99118 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85e92a94-ff63-3969-94f5-1995b6c643f8 | -3.32793 | -54.90891 | 2025-09-11 04:44:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1769e3e7-62ca-3cd6-b9d0-9fecef5ac99e | -6.72596 | -51.9563 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6af977d4-ff06-3ca2-af29-fc829f2fd612 | -6.74657 | -46.00663 | 2025-09-11 04:44:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1e9cff4-b6b2-32a6-b9aa-3e6a188294f1 | -5.40734 | -45.93001 | 2025-09-11 04:44:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2c46dea-46d2-3daf-83fa-6fd7f0c1f040 | -5.69219 | -43.33984 | 2025-09-11 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README84.md)
