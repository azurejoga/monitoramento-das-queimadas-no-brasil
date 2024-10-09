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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3dcca9e8-df22-3852-b05b-c5263a10100a | -14.08857 | -44.15191 | 2024-10-09 04:40:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2510b30d-507c-3e2f-b39f-47384d7f0814 | -14.08806 | -44.15465 | 2024-10-09 04:40:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ef77fbda-12b7-330a-a9c0-f7d0b1141c13 | -14.08409 | -44.14928 | 2024-10-09 04:40:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 233bc283-55cb-3a8c-8dc3-85598eac7be3 | -14.08401 | -44.1513 | 2024-10-09 04:40:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9a991f9f-652c-3bb2-9156-e614c51d4dae | -14.0835 | -44.15403 | 2024-10-09 04:40:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 12a4ab40-83c8-3a10-bddc-46d4edb72340 | -14.08233 | -44.09317 | 2024-10-09 04:40:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb95364e-3d8c-39fc-9961-8a14ef749574 | -14.06662 | -44.47168 | 2024-10-09 04:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4f9ed446-53f0-3593-85fd-cf96b07bfc7d | -14.06217 | -44.47097 | 2024-10-09 04:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cfcc308e-1e1e-3c14-8498-64c9e71cb891 | -14.06037 | -44.46762 | 2024-10-09 04:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ed7ec4b-602c-3385-a5ad-b460ec2a7506 | -14.05976 | -44.47214 | 2024-10-09 04:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d554850a-4c48-3b2b-97b0-fd94a1743366 | -14.05771 | -44.47031 | 2024-10-09 04:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf3f1dd3-2b2e-3b93-8b6e-8a34707b72d5 | -14.03387 | -43.56654 | 2024-10-09 04:40:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4d38fe1-0f30-3341-8519-deb5a8110d14 | -13.93821 | -44.54449 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04a8daad-215d-3ee5-8459-7e368bc6f6f5 | -13.93762 | -44.54889 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65f906db-f51c-3aa9-97ca-bff1bed94ece | -13.93695 | -44.54655 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a138d7cc-d5c5-300a-bfe0-657959bd61c2 | -13.93378 | -44.54392 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e67c0344-500b-32f4-ae1c-00dc94fe0dda | -13.93319 | -44.5483 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99449f4c-74f2-33fa-8218-c00f4df9988b | -13.93252 | -44.54595 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29eff90f-c3a2-3ad8-b151-3878a93602c0 | -13.91959 | -44.51489 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f47b786-b6ae-3c5e-8512-78d55a64de4e | -13.91901 | -44.51927 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e008d71f-7581-37b3-8b5e-a9ab9c9afed5 | -13.91573 | -44.50988 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4208f4c0-e9a9-3572-9da4-b1406819cb3e | -13.91514 | -44.51432 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f0814bb-8bf9-308f-a6d0-b87b70ae84ae | -13.91338 | -44.52766 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| df620425-8a57-3be2-aa14-869b39ce6f90 | -13.91325 | -44.63003 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b0868d21-46dd-3a68-912e-22d8027ce29c | -13.91267 | -44.63436 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9340dbd1-40ac-3e40-bb27-d20aedc05626 | -13.91188 | -44.50481 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8cd7e2d8-42dd-3251-9f52-b3ff6cb59dd2 | -13.91129 | -44.50931 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1b682f0-b897-3fb5-b2e4-6f97e7295333 | -13.9107 | -44.51376 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be00736e-c9da-391f-b013-ca59612f14ef | -13.90941 | -44.62518 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f6e8fc32-422c-3fbd-b05c-0d94315436c5 | -13.90884 | -44.62948 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cf222c2d-cf76-3580-b028-de7c9b038d38 | -13.90743 | -44.50426 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e28ac3f1-cc21-3972-a9f3-72b825837204 | -13.90685 | -44.50874 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b4840fd-bce8-3133-b296-5667cf6d39ed | -13.90626 | -44.5132 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b331882f-b7a3-34d4-b8de-a76e5835fd76 | -13.87458 | -44.65144 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| e8a69d9a-c218-3912-8931-62480047d82e | -13.87077 | -44.64637 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 315d39f6-4ebb-3d4b-9996-8c1e1f44a1f9 | -15.08206 | -51.23091 | 2024-10-09 04:40:00 | NPP-375D | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ec4fcae-ea19-3f94-afca-1efafa37c51d | -15.07929 | -51.22678 | 2024-10-09 04:40:00 | NPP-375D | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0560a9f8-0e8e-333d-8bd4-cd5ba358609e | -15.07723 | -48.94551 | 2024-10-09 04:40:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc514593-aa54-3433-8030-77b072534e20 | -14.95229 | -50.06387 | 2024-10-09 04:40:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c294a5b-53a8-324d-8031-6671d7ac9d0b | -14.84208 | -51.07733 | 2024-10-09 04:40:00 | NPP-375D | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ded90775-429d-3816-8184-54677a0e3e50 | -14.83875 | -51.07678 | 2024-10-09 04:40:00 | NPP-375D | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f6881f3-c3b1-349e-8b0f-341eee6a61bb | -14.83757 | -48.05193 | 2024-10-09 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36781a88-7dbd-3371-a429-81da9a53ef8e | -14.83599 | -51.07265 | 2024-10-09 04:40:00 | NPP-375D | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58de20ce-ee19-3bbf-b4cf-8d0e1649526e | -14.80809 | -46.63601 | 2024-10-09 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7551bd4b-492a-3820-b170-faa886b0f986 | -14.79706 | -49.98671 | 2024-10-09 04:40:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ce0843b8-3f03-346d-9424-76e8bb242976 | -14.78635 | -48.96303 | 2024-10-09 04:40:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65449021-ee0f-3e37-b9b0-7d694a31c40d | -14.67936 | -47.30793 | 2024-10-09 04:40:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac17b734-2541-32ec-a257-7aa7c702d323 | -14.67871 | -47.31258 | 2024-10-09 04:40:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 495988e3-c644-3254-8fb7-cd58a8c7fb7c | -14.55974 | -49.84798 | 2024-10-09 04:40:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be0c336e-2193-3743-a60f-876542be1375 | -14.49358 | -49.26743 | 2024-10-09 04:40:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e99aed64-c88d-364e-90a2-9e7a91904c6d | -14.24683 | -49.22244 | 2024-10-09 04:40:00 | NPP-375D | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca56b08e-5bdf-30b8-97ad-ea8df0ddff5c | -14.15377 | -47.35165 | 2024-10-09 04:40:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66dc3fd4-8913-33bd-8ada-cedad40c35ee | -14.05333 | -49.41661 | 2024-10-09 04:40:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 568d90ad-e29f-3957-9745-afbb18a71520 | -14.03159 | -50.55815 | 2024-10-09 04:40:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc00d0a2-b8e8-3072-bb65-ffc2084df87b | -14.03103 | -50.56172 | 2024-10-09 04:40:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b1cbbf6-f1b0-36b0-b877-c0f98f411e0e | -13.93229 | -47.31456 | 2024-10-09 04:40:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76239ecb-6010-3087-b4f8-8498a282c44b | -13.92859 | -47.3139 | 2024-10-09 04:40:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bda92a36-b976-3e39-bbdf-c789b28ad471 | -18.97073 | -45.08934 | 2024-10-09 04:40:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7502c7b5-ad20-31a9-9ffd-26ff68f5cbb5 | -18.96613 | -45.08887 | 2024-10-09 04:40:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 139818bb-39f1-3047-8443-1a2f05419d9e | -18.31122 | -43.81306 | 2024-10-09 04:40:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08300f13-c190-31f4-b673-2ddf573ca2a6 | -17.92968 | -44.56564 | 2024-10-09 04:40:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a82c3b6e-8738-3b39-be97-c91d7d2efa1a | -17.87919 | -43.29142 | 2024-10-09 04:40:00 | NPP-375D | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1d6b807-181c-3cd3-a179-5f9066a5fe6e | -17.87415 | -43.29041 | 2024-10-09 04:40:00 | NPP-375D | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8304aa55-bfd5-3f94-88d1-b9ba8d52aae8 | -17.59435 | -44.50045 | 2024-10-09 04:40:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2081db3b-b296-3bd4-a303-f0871d664feb | -17.39392 | -43.4283 | 2024-10-09 04:40:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad83b703-05f7-346c-8cdd-fbd882f2bde5 | -17.37121 | -42.6256 | 2024-10-09 04:40:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18b4b5e0-50d2-324b-a1e9-3a812676d6fd | -17.37083 | -42.62896 | 2024-10-09 04:40:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0fcec79c-8d0d-324b-9d83-363f89a14a75 | -17.37014 | -42.62848 | 2024-10-09 04:40:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a33059bd-7558-3413-b6ee-2fff80ec9938 | -16.6798 | -43.88596 | 2024-10-09 04:40:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4194de6-d04c-366c-8142-83c244c1b141 | -16.67832 | -43.88665 | 2024-10-09 04:40:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4344c2a6-5fb9-3357-bbf2-619ab5ed4712 | -16.64863 | -42.22298 | 2024-10-09 04:40:00 | NPP-375D | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0a034105-342e-37e2-9f8e-987de2cae2e9 | -16.64821 | -42.22665 | 2024-10-09 04:40:00 | NPP-375D | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3868e1d6-5441-3e4c-bdd3-7010d880bf28 | -13.70058 | -49.85613 | 2024-10-09 04:40:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8b42ded-0f22-322c-8708-e6b2b8e39386 | -13.62358 | -48.48377 | 2024-10-09 04:40:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4c711068-c3a4-3583-b8f6-727be8519324 | -13.62009 | -48.48312 | 2024-10-09 04:40:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60793aca-220c-352c-a10f-4805b92ff312 | -13.56188 | -48.65301 | 2024-10-09 04:40:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04db7b32-8cf0-3f81-9d6c-65bff8671272 | -13.14306 | -48.59092 | 2024-10-09 04:40:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c497593d-4c1a-3c22-90dc-6e5763881317 | -13.10655 | -48.76318 | 2024-10-09 04:40:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc0111b8-d845-3ec9-8c50-0fada83d46dd | -12.99635 | -46.23554 | 2024-10-09 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40d6f1bd-a4fd-32bc-b001-eb545cec7cfb | -12.99316 | -46.22973 | 2024-10-09 04:40:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18639110-ab1f-3fab-a170-760043d3427a | -12.99247 | -46.23473 | 2024-10-09 04:40:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3797fa4f-4470-33d4-8507-990bdab9c454 | -12.98999 | -46.22374 | 2024-10-09 04:40:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c904389-a2b2-3398-9484-9b67a7b7d06d | -12.98928 | -46.22886 | 2024-10-09 04:40:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ee73c96-4400-3b78-bbb3-e8cfddca21b6 | -12.98746 | -46.21311 | 2024-10-09 04:40:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d3633b4-d519-30e2-b632-03c92bc5926a | -12.98611 | -46.22286 | 2024-10-09 04:40:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ac2a4b0-34e0-3f2e-9140-009fbd3b64c8 | -12.98357 | -46.21229 | 2024-10-09 04:40:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bab9161e-ba1e-3b9c-b3ff-b84c25bd2eae | -12.98035 | -46.20662 | 2024-10-09 04:40:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b25a0d22-1ae1-3d45-b05f-8df711f1f188 | -12.97968 | -46.21146 | 2024-10-09 04:40:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 320218dd-70c8-3fc5-8cac-229b9419945d | -15.27142 | -41.63949 | 2024-10-09 04:40:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| dd0cd84c-66e9-340f-88d4-d9c4be4566f8 | -15.271 | -41.64323 | 2024-10-09 04:40:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4c9aff0d-d7c6-39b8-b048-d4be4b4acbd8 | -18.65861 | -41.50366 | 2024-10-09 04:40:00 | NPP-375D | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| f6dc5aab-8a58-32d3-b3ee-de88eb29c24e | -18.65857 | -41.50316 | 2024-10-09 04:40:00 | NPP-375D | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 8db2fe0a-e813-3d75-9442-379c0ba4d679 | -18.65809 | -41.50855 | 2024-10-09 04:40:00 | NPP-375D | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| fbe1956c-ad4a-3d18-bf22-b60479d1fb63 | -18.65809 | -41.50806 | 2024-10-09 04:40:00 | NPP-375D | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| ab606f88-2b91-3a6e-9e4d-c7aa2f8e6bb7 | -18.62569 | -41.13115 | 2024-10-09 04:40:00 | NPP-375D | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ff6b7634-3555-32c5-96ce-43382cc768f0 | -18.62529 | -41.13523 | 2024-10-09 04:40:00 | NPP-375D | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 043d0e13-83ee-3105-9897-aa64d7cde608 | -18.59683 | -42.33866 | 2024-10-09 04:40:00 | NPP-375D | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| f5ee08f9-83e3-3ca6-b6c7-4ef33b53380c | -18.59645 | -42.34237 | 2024-10-09 04:40:00 | NPP-375D | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 73b86c63-48ee-370f-827c-cc4eeea3eb94 | -18.59606 | -42.34605 | 2024-10-09 04:40:00 | NPP-375D | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 1696263f-355d-3434-a506-03d8cd96702f | -18.59064 | -42.34501 | 2024-10-09 04:40:00 | NPP-375D | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |


[Clique aqui para ver as próximas entradas](README130.md)
