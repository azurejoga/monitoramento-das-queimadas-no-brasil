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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a020d423-c282-3777-9117-60bab460939f | -4.76164 | -46.62325 | 2024-10-23 03:34:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| d9cf08c8-d3b5-39b3-9cad-c798cf186084 | -4.76041 | -46.63017 | 2024-10-23 03:34:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1cab566f-b177-3dc9-8045-22c1191b180f | -4.75914 | -46.62122 | 2024-10-23 03:34:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| addbf75c-fc47-34b3-b8e3-8b5a927f8295 | -4.75786 | -46.62814 | 2024-10-23 03:34:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a9b5450b-daf2-3c58-96d2-fa398ff6a45e | -4.75468 | -46.62168 | 2024-10-23 03:34:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| debd0db7-c9dc-3fcf-8256-1dac328e3ed4 | -4.75219 | -46.61963 | 2024-10-23 03:34:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2f0221b3-bf63-3077-a604-d2832a234a89 | -4.75096 | -46.62628 | 2024-10-23 03:34:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d55268ed-6a38-34d1-98b0-dd51bfd9cec8 | -4.74776 | -46.61992 | 2024-10-23 03:34:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| db90fbc4-0f04-3a3d-af50-214168c63e0e | -4.73957 | -46.66597 | 2024-10-23 03:34:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a24b218f-ae10-3f18-b681-2da4a47164bb | -4.73833 | -46.67291 | 2024-10-23 03:34:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b95cbb2-2025-37c0-aab7-036e55c30045 | -4.73552 | -46.67063 | 2024-10-23 03:34:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a279f49e-7412-33e7-8196-5d8d10f80b25 | -4.73421 | -46.67773 | 2024-10-23 03:34:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fa3988c1-17cc-3dbe-b4c5-68f360c3bf29 | -4.73016 | -46.67802 | 2024-10-23 03:34:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8c30f728-d281-3315-a22e-3e998a1799e7 | -4.72727 | -46.67597 | 2024-10-23 03:34:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 12ead386-b577-30f0-9598-7ffe471d0411 | -3.98185 | -46.47181 | 2024-10-23 03:34:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4f99ce5-0b55-3570-98bf-b0874728ece4 | -3.97496 | -46.46976 | 2024-10-23 03:34:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66872e26-e808-39b8-b12f-eb838aad4524 | -1.388 | -51.9867 | 2024-10-23 03:35:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| df5d9bfe-df23-3c41-9323-5dfb2cff31b5 | -1.3879 | -52.0072 | 2024-10-23 03:35:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 341c235e-d1bb-3904-9379-01fc1e545548 | -3.1102 | -54.146 | 2024-10-23 03:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 78f64475-81de-3d81-b394-f87f629d12ba | -3.1101 | -54.1661 | 2024-10-23 03:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 95318701-0b79-399a-b16e-00a8c2899302 | -3.0917 | -54.1666 | 2024-10-23 03:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 31412f80-ec62-374b-a029-0077708952db | -4.1719 | -47.9894 | 2024-10-23 03:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 2c08193e-34d5-322e-a3d0-33bd0ccaec7a | -4.7565 | -46.6249 | 2024-10-23 03:35:33 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 149e1e01-86ef-3737-8a62-ceb08c28a617 | -4.7254 | -45.7363 | 2024-10-23 03:35:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 52.1 |
| eeeee3ee-5986-3167-9c49-7f954aad5704 | -5.5671 | -43.2576 | 2024-10-23 03:35:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| c6216c3f-6f64-3ac6-9041-ad8926d173b0 | -5.5858 | -43.2562 | 2024-10-23 03:35:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 07187138-f3a0-35dc-b1dc-6e3cce5b3279 | -9.62127 | -36.76527 | 2024-10-23 03:36:00 | NPP-375D | CRAÍBAS | ALAGOAS | Brasil | 2702355 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1140c041-8aec-30f4-9d59-1b493e331101 | -9.45836 | -36.98141 | 2024-10-23 03:36:00 | NPP-375D | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b03de082-e9db-3c25-ad1f-e6fb2bd2de17 | -13.1032 | -43.36992 | 2024-10-23 03:36:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a8d2634-9799-3fc4-bb44-acbabf7103a2 | -13.09936 | -43.36306 | 2024-10-23 03:36:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce00acc7-4079-3eb3-86a8-3609eec603ae | -13.09915 | -43.3684 | 2024-10-23 03:36:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ec8634fc-6447-3a68-902a-ffe3d6d87dbd | -13.09823 | -43.36891 | 2024-10-23 03:36:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8df7f943-375b-355a-8bda-2d6b1ec28010 | -10.70326 | -44.38096 | 2024-10-23 03:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22e07c09-8a36-30da-a497-7b8b3ab80619 | -10.70255 | -44.38473 | 2024-10-23 03:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bfbdd175-75ac-325a-a3a4-0daa39b384ed | -10.60859 | -44.28107 | 2024-10-23 03:36:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72145d55-d838-3c66-a4f8-c511f4467568 | -10.60376 | -44.27631 | 2024-10-23 03:36:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5455015-d89b-324e-a022-036802a945af | -10.60308 | -44.2799 | 2024-10-23 03:36:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d995e809-103d-3192-bb4d-729b72e3c345 | -10.60239 | -44.28355 | 2024-10-23 03:36:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 936b23f5-59be-36aa-8607-77b6c1cfb2e7 | -10.6017 | -44.2872 | 2024-10-23 03:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 645d672d-9eb1-31be-bb14-7591463a0cfa | -10.75839 | -45.02406 | 2024-10-23 03:36:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 888126a2-8724-3ae8-9226-05bf5c52dd5a | -10.75759 | -45.02816 | 2024-10-23 03:36:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 890ddb40-df57-311c-94e0-fdeaba8b3f2b | -10.75261 | -45.02295 | 2024-10-23 03:36:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4147d408-8d00-3944-8553-c51f78574b65 | -11.12997 | -44.95623 | 2024-10-23 03:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a474656-de8e-37bd-b845-71ee98919a9f | -11.12923 | -44.9601 | 2024-10-23 03:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 597c1c24-29e3-39b5-b55b-788772e3998e | -10.99707 | -45.26726 | 2024-10-23 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c568398e-0cfe-3424-a70d-45b80c506df1 | -10.99129 | -45.26583 | 2024-10-23 03:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1545df19-b729-3282-ab47-bea7c525135e | -7.4479 | -43.62718 | 2024-10-23 03:36:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 246f411e-a967-3668-adb4-8ebde4f000c3 | -7.44231 | -43.62613 | 2024-10-23 03:36:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b638078-9299-3bc7-9edd-849340b450a2 | -10.59757 | -44.27878 | 2024-10-23 03:36:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 15804033-0b40-3509-9c84-b4a0defe9883 | -10.59688 | -44.28238 | 2024-10-23 03:36:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9e86ee4-c52d-36b8-a915-54acf20676d1 | -8.71307 | -44.00783 | 2024-10-23 03:36:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45ce1f83-9dea-3e63-b3b6-cef35115db65 | -8.71234 | -44.01178 | 2024-10-23 03:36:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ef329f8-3c44-3720-8a04-f16d8026d4b7 | -10.58376 | -44.29105 | 2024-10-23 03:36:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7cc717a7-2940-39ac-af33-b7a7aba78bc4 | -10.57823 | -44.28994 | 2024-10-23 03:36:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 365e0c7d-931a-375a-90c7-761b3d1a8e42 | -10.57752 | -44.29366 | 2024-10-23 03:36:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8d056d23-58aa-35db-ac3d-42342881a416 | -10.44923 | -44.89799 | 2024-10-23 03:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae0e4fc1-0278-36d4-8fbc-93a3e59d7e84 | -10.44425 | -44.89521 | 2024-10-23 03:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d9feb51-7480-377e-b6fb-e0498651da74 | -10.44348 | -44.89936 | 2024-10-23 03:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 398e8e5e-5572-3036-a78e-0bc87bfd6ba2 | -10.44345 | -44.89696 | 2024-10-23 03:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9ccc1b9c-0a55-33d8-8df9-823aba32cdd0 | -10.44264 | -44.9011 | 2024-10-23 03:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ae7e8bb5-0618-3ba1-84df-43be5548d627 | -10.43768 | -44.89841 | 2024-10-23 03:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 812d6dca-e114-3540-b670-b5a290d0881d | -8.53922 | -35.02008 | 2024-10-23 03:36:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1551c39e-bb3c-3a7d-ae8b-a484c7c1c844 | -9.37429 | -35.99786 | 2024-10-23 03:36:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5193d082-cc9c-3549-aaf3-b7eb8be36fd4 | -9.37368 | -36.00158 | 2024-10-23 03:36:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8457abc1-2840-36b3-8d98-0141d3e59a66 | -10.32136 | -36.65778 | 2024-10-23 03:36:00 | NPP-375D | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7938964f-9bed-3c16-a79f-1332daa499cb | -10.4989 | -36.72168 | 2024-10-23 03:36:00 | NPP-375D | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 28c55b04-1d7f-387d-84ac-a7f025f4fe1f | -9.34386 | -36.01196 | 2024-10-23 03:36:00 | NPP-375D | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ee66e868-333c-37d7-9d0f-646e23bcb37b | -9.34104 | -36.00766 | 2024-10-23 03:36:00 | NPP-375D | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| b4ad698f-5706-38d0-ac67-38503ecb999c | -9.34043 | -36.01139 | 2024-10-23 03:36:00 | NPP-375D | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 47227728-bf44-356b-b57c-eb114a43df5b | -11.06417 | -38.43676 | 2024-10-23 03:36:00 | NPP-375D | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e6a698cc-6618-3074-9ad5-686bcac900e8 | -11.06356 | -38.43895 | 2024-10-23 03:36:00 | NPP-375D | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 72a1a25d-fa4f-3adf-933b-89ef59e6cd54 | -9.14862 | -40.6549 | 2024-10-23 03:36:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 739cab26-ac60-3d11-94eb-118ec462b275 | -9.14493 | -40.64972 | 2024-10-23 03:36:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 26ef5cc9-a007-3475-a86a-d4762c4ed952 | -9.09541 | -40.3649 | 2024-10-23 03:36:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3710db29-a1e3-3fb5-8fee-7c61c6c39753 | -9.09513 | -40.36403 | 2024-10-23 03:36:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f6333d29-c9b9-39b7-b7e4-949f5d3dd63a | -10.65947 | -40.81683 | 2024-10-23 03:36:00 | NPP-375D | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a8433b8d-985f-301c-9452-8345ea235817 | -10.65508 | -40.81601 | 2024-10-23 03:36:00 | NPP-375D | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2e36e990-4811-35ae-9aa8-50c5299b343c | -7.33473 | -42.17532 | 2024-10-23 03:36:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d686f00c-c014-3480-85a3-2bc7985eb1f3 | -11.99279 | -43.08995 | 2024-10-23 03:36:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 549b4918-77a9-394c-abf6-5a5bd2710466 | -13.08584 | -42.28111 | 2024-10-23 03:36:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 84382a1e-0697-308c-b574-d8b79e2febe8 | -12.89789 | -43.18464 | 2024-10-23 03:36:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d821b03b-5a89-3c3e-9e69-1b463cd321f9 | -12.89656 | -43.18839 | 2024-10-23 03:36:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9a0337fc-680c-3740-95c1-6194d4fd33b0 | -7.50001 | -42.90905 | 2024-10-23 03:36:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e2ce6e86-c474-3c69-b5e2-be56f8325396 | -7.49464 | -42.90828 | 2024-10-23 03:36:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6ea295a8-4885-3860-b590-88b9a59f0c06 | -7.27296 | -43.63174 | 2024-10-23 03:36:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6b64bade-c824-3685-bcd1-6287aa836172 | -7.27226 | -43.63561 | 2024-10-23 03:36:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 800e217d-78ec-3d14-ae0f-c9959b7c51dd | -9.64871 | -43.90609 | 2024-10-23 03:36:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c3dde9d5-612a-3a3e-9451-3ecedd30c5b3 | -9.64804 | -43.90971 | 2024-10-23 03:36:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b7d3b21e-81c8-3539-8782-1fb42ad148cb | -9.64797 | -43.90937 | 2024-10-23 03:36:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f9396811-1e0f-37fe-a9f1-eca0ee43b588 | -7.31756 | -45.28199 | 2024-10-23 03:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07f30711-469a-3355-b1ee-730703bd68c9 | -7.31667 | -45.28679 | 2024-10-23 03:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 604f8bf9-0c6d-34e9-9e95-021ead154cd0 | -7.17445 | -45.14172 | 2024-10-23 03:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8e2d443e-a6fe-38d8-929b-8fa261e73d47 | -7.17301 | -45.13758 | 2024-10-23 03:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| edd14984-f12c-3d11-b800-d71dc6f9703e | -7.17214 | -45.14223 | 2024-10-23 03:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 31bcb951-f359-3f2a-a8d3-5514422f4fa6 | -7.16914 | -45.13573 | 2024-10-23 03:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8cfaa977-f9f3-3a0a-b32d-310825f0e201 | -7.16827 | -45.14053 | 2024-10-23 03:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 34704a2c-98de-3cf7-9e98-ac9ca1a2d12f | -7.16734 | -45.14568 | 2024-10-23 03:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2f16af53-58ae-3f38-9c9d-0ed8e5f70af2 | -7.16684 | -45.1364 | 2024-10-23 03:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 523ce7b3-310c-3674-98d7-fb5993626416 | -7.1659 | -45.14141 | 2024-10-23 03:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 979063d9-5cc7-35dc-8296-4b637aa341e3 | -7.1649 | -45.14671 | 2024-10-23 03:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README17.md)
