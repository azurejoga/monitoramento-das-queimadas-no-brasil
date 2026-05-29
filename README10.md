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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e1b23e5-9919-3d7e-93e2-613a63fc3096 | -10.81459 | -56.59444 | 2026-05-29 05:14:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 227081a6-90a9-308b-aa33-480e2f938fc3 | -7.50727 | -55.00518 | 2026-05-29 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c756ee58-dc15-3dd1-ba08-2a003abb6052 | -12.29672 | -57.40471 | 2026-05-29 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ecbc0a62-bf35-3a4b-bca9-05f53eb34321 | -18.46344 | -54.70746 | 2026-05-29 05:16:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1736ca2e-bb45-361b-b937-5c4dde39be5b | -13.17641 | -52.70687 | 2026-05-29 05:16:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a090c32-5abf-319e-890f-592f447262ee | -11.79351 | -57.01217 | 2026-05-29 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c220d5b1-5bcf-3840-9339-dccbcc31de7e | -14.17358 | -52.86086 | 2026-05-29 05:16:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0794b440-0050-3f6f-a1f8-5150225a1565 | -16.17113 | -58.47451 | 2026-05-29 05:16:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 803c3f8e-4b46-342b-a846-ea645823746f | -16.17168 | -58.47084 | 2026-05-29 05:16:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4a57a151-cbcf-3f24-b6bd-89cbd954ae60 | -14.81586 | -56.44957 | 2026-05-29 05:16:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9b78708-78e4-3238-87fb-1eff63be6aa1 | -14.01078 | -54.00075 | 2026-05-29 05:16:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5dd6ac84-d2f2-3b6b-b3e6-e863ada8e96c | -13.64089 | -55.75381 | 2026-05-29 05:16:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ffbd14d2-87d7-3fea-a184-feef03c7b025 | -15.42896 | -56.32172 | 2026-05-29 05:16:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b9a161f-2e04-38d1-bd3f-d3e1629dd907 | -11.72941 | -56.83606 | 2026-05-29 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3f1f1d8-d6ca-3c6e-8dd5-3a6befbe5ca7 | -19.68521 | -54.35033 | 2026-05-29 05:16:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e58e440-47ba-387c-8137-69c8041e8e1a | -13.63727 | -55.75326 | 2026-05-29 05:16:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c739bea-3d63-3407-bb89-7d6a83b8846a | -12.68759 | -54.58215 | 2026-05-29 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6879acd-851c-3f8b-ae33-893bf38b24ab | -13.18074 | -52.70752 | 2026-05-29 05:16:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f49923d2-0409-3f78-b70e-4b9e31b85992 | -18.46295 | -54.71133 | 2026-05-29 05:16:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d51bcac0-481c-3c77-a4d7-d22e4dac577a | -14.17738 | -52.86573 | 2026-05-29 05:16:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e11740fc-3210-302b-9265-846245acb4e9 | -16.17783 | -58.47561 | 2026-05-29 05:16:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| efe70911-fe5f-3d8c-b613-e40e2fb8dbd8 | -18.45935 | -54.70688 | 2026-05-29 05:16:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 975067e4-7c29-37b1-aea2-a20e37e222a0 | -13.11541 | -51.72334 | 2026-05-29 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc8b1883-f355-3ee2-8589-4f2022bc0046 | -11.7969 | -57.01271 | 2026-05-29 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae8cb3ad-714f-3e10-9bc4-c7d8fa607e91 | -13.64192 | -55.75227 | 2026-05-29 05:16:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dea4efe9-0731-3bb4-9785-4287abbefa75 | -19.68947 | -54.35089 | 2026-05-29 05:16:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7330c2fa-ba86-3ea0-b7ed-629c564d1999 | -12.36611 | -54.16806 | 2026-05-29 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f1c9fc4-56bb-3164-bce6-539504acd61d | -18.46754 | -54.70805 | 2026-05-29 05:16:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a26b713-5977-3c97-a10f-b23c6fdbdc55 | -16.17448 | -58.47506 | 2026-05-29 05:16:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 75340b2d-6f7a-31c8-8acc-c1f617cff467 | -19.68471 | -54.35443 | 2026-05-29 05:16:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5738b72c-135f-38b1-8092-2a8956321d4c | -16.21802 | -59.66004 | 2026-05-29 05:16:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 990895bb-a2a9-3480-8ee4-684d5d64f52f | -13.18563 | -52.70398 | 2026-05-29 05:16:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33cbe28a-6cef-3869-8a4d-63ac9a7633cf | -12.36256 | -54.16865 | 2026-05-29 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 908beea2-6c33-3a0a-8fa4-1d1ed639d058 | -16.16401 | -58.48468 | 2026-05-29 05:16:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 17af3fc3-6ae5-3c90-8f56-be8a6102b801 | -16.17392 | -58.47872 | 2026-05-29 05:16:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 61286e8b-b5b0-385a-9c9f-c73708d910d0 | -16.17504 | -58.47139 | 2026-05-29 05:16:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 91e8f09f-df35-3c1e-a296-8994a81539f2 | -16.1657 | -58.47368 | 2026-05-29 05:16:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0a3aa71a-e801-301e-b586-f729bc03c3e1 | -12.80464 | -54.87225 | 2026-05-29 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f67fc27-76bd-38c3-90b0-56f0f0403de3 | -11.79633 | -57.01637 | 2026-05-29 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08d9ff9c-14ea-30fc-84ac-b9ab94b1de63 | -13.11684 | -51.72155 | 2026-05-29 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df9d02cd-a604-3183-808c-9e7c0f3b2cc4 | -12.36221 | -54.1675 | 2026-05-29 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 259826fe-f717-3ced-98f1-ae6d8f3d398b | -12.30008 | -57.40524 | 2026-05-29 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d273d220-1a07-365e-87d7-45c8691cf017 | -12.80421 | -54.87017 | 2026-05-29 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 169a17bd-3575-3a6e-a74c-d41a55f29e88 | -14.17793 | -52.8615 | 2026-05-29 05:16:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 770ea185-41c5-3e41-93b0-d90f50c758bf | -16.16778 | -58.47396 | 2026-05-29 05:16:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 92c28167-3662-39c9-a19e-e50c4fd0c4e0 | -18.11683 | -54.51396 | 2026-05-29 05:16:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5dc42007-701a-3348-9576-f422af96e47f | -13.18507 | -52.70813 | 2026-05-29 05:16:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e902de0-7bbd-3787-ae5a-f47c94758090 | -16.16833 | -58.4703 | 2026-05-29 05:16:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a60af8f8-e9cc-344f-9a1d-db4842cb89b8 | -16.16611 | -58.48496 | 2026-05-29 05:16:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e37c8d96-6f02-3fbf-a1ad-e9810cfcb2b8 | -12.30344 | -57.40577 | 2026-05-29 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ebcebea-4131-3f94-9a87-90ed9ef39caf | -14.81291 | -56.44491 | 2026-05-29 05:16:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be0a7feb-4bc2-3cfb-b5c2-9046a3d45187 | -12.80089 | -54.87168 | 2026-05-29 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5b07305-f317-33c9-befa-20ea910b3b29 | -12.36325 | -54.16364 | 2026-05-29 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04501a33-3ebc-36ec-b4c5-b885bf968a5d | -13.64451 | -55.75436 | 2026-05-29 05:16:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab1a30ed-4052-330f-96f2-50f46c3a57a2 | -16.17224 | -58.46718 | 2026-05-29 05:16:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ff9dea02-4739-38a1-a894-0cf7145c4cca | -21.39825 | -48.70966 | 2026-05-29 05:18:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 436873f3-283c-3a1c-962a-376744015028 | -21.3978 | -48.71476 | 2026-05-29 05:18:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91963291-b9e0-361c-875a-39243c585944 | -21.39652 | -48.70924 | 2026-05-29 05:18:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 817d05ea-4dde-3832-9c70-16688600cfb2 | -21.39611 | -48.71434 | 2026-05-29 05:18:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 321e96e1-104f-3db2-80ed-61c9ebed7e8d | -11.591 | -47.4496 | 2026-05-29 05:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| b7fb36e7-ae10-3c11-8147-cdd7301aba10 | -11.591 | -47.4496 | 2026-05-29 05:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| e4387d94-681e-300e-9b4a-9b1163e6f3d0 | -11.591 | -47.4496 | 2026-05-29 05:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 62171e22-c0d6-3fef-b3ab-a65e20de1d35 | -11.591 | -47.4496 | 2026-05-29 05:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| e4d4a5c1-97c3-3a09-bfc0-67fee7a91b44 | -11.591 | -47.4496 | 2026-05-29 06:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 9da6dd4f-9b4f-3e5b-9318-4617f3154e79 | -11.591 | -47.4496 | 2026-05-29 06:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| cb7b0349-271e-3401-8821-89aded20110b | -5.3244 | -44.68936 | 2026-05-29 06:12:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 9e32f20f-592f-3a95-9c80-03981ca1981f | -6.98864 | -42.87576 | 2026-05-29 06:12:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 168a4c09-18b5-3b54-a4af-581cb92fb627 | -6.99607 | -42.88583 | 2026-05-29 06:12:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a4f13460-4d71-3d81-bb34-cea5637ac0f1 | -5.94391 | -43.48657 | 2026-05-29 06:12:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d7df9a6c-f60c-3438-b21e-e6482aa11d39 | -6.08642 | -44.00104 | 2026-05-29 06:12:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 50a9f8fb-e0cc-36ac-b2cc-6ac6ad434d9a | -5.95276 | -43.48787 | 2026-05-29 06:12:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b36c71f5-5a87-3191-bdc7-420b3ebc5d32 | -6.98731 | -42.88452 | 2026-05-29 06:12:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 2efcfb4c-d88c-3f8c-8e42-c65a98cf7ffb | -7.00361 | -45.00388 | 2026-05-29 06:12:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a0feaae3-17d8-382c-bae9-5c13540b423e | -6.39417 | -44.1665 | 2026-05-29 06:12:00 | AQUA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 6b977773-e970-3671-aaa0-46ce398e134a | -8.67955 | -48.30394 | 2026-05-29 06:14:00 | AQUA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b19a10af-95f3-3a61-b66b-6bc1b9982a7d | -11.60011 | -47.42934 | 2026-05-29 06:14:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4de7180b-2ec4-3fd6-ba3a-10dbe53100f9 | -11.58802 | -47.43968 | 2026-05-29 06:14:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 437590ab-a7e7-3b6e-b3e5-7423b8168376 | -11.59064 | -47.43333 | 2026-05-29 06:14:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 48ba3003-9f87-3e71-a9be-0900174455a9 | -11.58872 | -47.44531 | 2026-05-29 06:14:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 3f76694d-5d71-3914-a2ad-1646abd68994 | -11.58603 | -47.4516 | 2026-05-29 06:14:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| aa53b3a1-231b-3955-9cb7-81e93efb093c | -10.97772 | -45.09523 | 2026-05-29 06:14:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ff3cfef3-8394-337d-9cd7-8981de6e44b2 | -11.59811 | -47.44138 | 2026-05-29 06:14:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 48.6 |
| a3b6d188-c8fb-330e-b06a-60a6a051466b | -11.591 | -47.4496 | 2026-05-29 06:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 0cfa8b76-2bca-332c-a153-1912a736f6b0 | -11.591 | -47.4496 | 2026-05-29 06:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 36a353c9-3680-3206-a159-8714d1180dfb | -11.591 | -47.4496 | 2026-05-29 06:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| de0545fc-5a7e-3a09-ac2f-ba2ba9c53208 | -11.591 | -47.4496 | 2026-05-29 06:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 2a5e81b7-2367-3381-aa72-ef27d4187665 | -11.591 | -47.4496 | 2026-05-29 07:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 9f8c955c-3715-3794-9e17-104811b64d17 | -11.591 | -47.4496 | 2026-05-29 07:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| db7331f1-7a5f-3ed7-b974-711dd6397eac | -11.591 | -47.4496 | 2026-05-29 07:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 6ea987a9-2543-399f-98b1-bd254d3a47cf | -11.591 | -47.4496 | 2026-05-29 07:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 089e7b27-a013-3be5-9040-9105605383a3 | -11.591 | -47.4496 | 2026-05-29 08:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 45d9af4d-0a61-3aeb-9b01-e6204e3f36e8 | -11.591 | -47.4496 | 2026-05-29 08:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| ff8ee95a-dd6f-327b-9eea-fc0d6533a598 | -11.591 | -47.4496 | 2026-05-29 08:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 23eef058-c966-358d-9677-1faf67601a90 | -11.591 | -47.4496 | 2026-05-29 08:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 4a4e0f80-64c8-3f6c-b313-c3a2b2d50291 | -10.8192 | -46.9009 | 2026-05-29 10:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 5da1f318-d80a-3d34-9510-e62864d3335d | -10.8382 | -46.8985 | 2026-05-29 10:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 210.0 |
| a7f70a14-3964-3beb-ad5e-0b4b07f571ac | -10.8192 | -46.9009 | 2026-05-29 10:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 219.3 |
| 9a35d232-da06-35fa-9626-5e0da9683d40 | -8.8348 | -46.7247 | 2026-05-29 10:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 6e283dee-0b3d-324a-ac38-6069ca71ed9b | -10.8382 | -46.8985 | 2026-05-29 11:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| ca33a1e7-c7d7-30f4-9e65-5bce772b43b2 | -10.8192 | -46.9009 | 2026-05-29 11:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 218.2 |


[Clique aqui para ver as próximas entradas](README11.md)
