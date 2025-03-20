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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b0fb256-e654-37e9-b87f-eb1392db2768 | -11.76947 | -37.89378 | 2025-03-20 04:02:00 | NPP-375D | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 36117a6e-3562-30de-a708-aae1dced9a17 | -5.97052 | -43.75074 | 2025-03-20 04:02:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dba671b7-9690-3fd9-910c-f2a8be4f12eb | -12.28844 | -43.53955 | 2025-03-20 04:02:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cf4a647b-fd2d-3226-9f2d-8f0d106ac023 | -7.05913 | -44.38125 | 2025-03-20 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9d8d593b-c474-3ea7-860e-830a9e66ca53 | -11.77034 | -37.89227 | 2025-03-20 04:02:00 | NPP-375D | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6267d1da-3955-3c51-aa57-c698f2845e95 | -10.87634 | -44.17476 | 2025-03-20 04:02:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56dce44b-868b-3359-9138-0aacd478b1cd | -12.09392 | -45.64005 | 2025-03-20 04:02:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2996f361-82ce-3364-8405-016dc4b515be | -12.58598 | -48.33233 | 2025-03-20 04:02:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 342a3bed-fe46-3cec-8c25-23026340359b | -12.33038 | -48.00877 | 2025-03-20 04:02:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 973e148a-698d-3098-9258-ba105f2a82d5 | -12.29275 | -43.53931 | 2025-03-20 04:02:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 99d6341c-5820-3dac-9e3d-335338a1ab02 | -12.19893 | -39.31815 | 2025-03-20 04:02:00 | NPP-375D | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 93f235ef-6f9e-30fd-b232-bb06434d6939 | -12.0965 | -45.62524 | 2025-03-20 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 550daf4e-3839-3057-a016-ff847c9f7545 | -7.06253 | -44.37976 | 2025-03-20 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| abc5eb6b-6bf1-3834-87ed-8bfa7b0a0e5d | -10.88068 | -44.17114 | 2025-03-20 04:02:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 043715a7-cb60-3216-a475-bca5c4b5c00b | -12.91106 | -45.05938 | 2025-03-20 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b1665b02-3025-3c94-b3e2-6843ed4ca2c1 | -11.45775 | -39.94088 | 2025-03-20 04:02:00 | NPP-375D | SÃO JOSÉ DO JACUÍPE | BAHIA | Brasil | 2929370 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8578da4d-e526-30c5-baf3-3108855caf22 | -5.96737 | -43.75285 | 2025-03-20 04:02:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 865b6d75-5909-3523-b2f0-6e56bf78a0d8 | -16.02415 | -42.11972 | 2025-03-20 04:04:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9d3e34d4-b972-313d-8180-84af20e7be08 | -19.83236 | -40.10823 | 2025-03-20 04:04:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c2b228d8-71b4-3ac0-86c0-6afd61123580 | -14.83088 | -46.55564 | 2025-03-20 04:04:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86bed7d3-c390-3540-bb19-f9e9f0d14f8b | -15.3512 | -46.95534 | 2025-03-20 04:04:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b621443-2f46-369d-a67a-afa4bb5de557 | -16.60386 | -44.01575 | 2025-03-20 04:04:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 231fe153-95d8-3e1c-bcf5-1ddc99f4590d | -14.83181 | -46.55049 | 2025-03-20 04:04:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ddf691a-06c7-31c5-8ff7-b724e78050a9 | -18.11771 | -39.684 | 2025-03-20 04:04:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d960a7da-2a4d-3f9d-ad33-bba1a8bb6edf | -15.35057 | -46.95889 | 2025-03-20 04:04:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04891f1c-8d24-3339-b82f-273f054e56f0 | -17.75224 | -42.89353 | 2025-03-20 04:04:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b13abfa-c9a5-3fa1-ada4-806057e806cd | -17.34327 | -41.60111 | 2025-03-20 04:04:00 | NPP-375D | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a92ca478-e374-3110-bf13-03ca50702aea | -17.77944 | -42.80872 | 2025-03-20 04:04:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 425d72da-0d80-3d6b-8aa7-e9d48eec994e | -19.83175 | -40.11247 | 2025-03-20 04:04:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 32da076b-bd06-393d-9c41-bf44afd55ee4 | -15.34658 | -46.95808 | 2025-03-20 04:04:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47907c73-73c3-3b07-ae7e-82c7a8136626 | -15.23762 | -43.75542 | 2025-03-20 04:04:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6fb6d424-eefc-3a4f-9352-755428b80930 | -17.78277 | -42.80929 | 2025-03-20 04:04:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c5046394-2155-3f1d-97a1-9ba4e05cdf5f | -15.0794 | -48.94504 | 2025-03-20 04:04:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e86acd27-88a5-3e06-9ee1-9e041afb7b37 | -16.68176 | -43.88457 | 2025-03-20 04:04:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d4df88b7-16aa-3ae6-8f9c-fb28d11ca058 | -14.85805 | -45.20033 | 2025-03-20 04:04:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49ddac64-02be-31da-8782-f2440907927c | -15.23699 | -43.75924 | 2025-03-20 04:04:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5578548c-9a3e-3112-a44e-72d8507c7b0a | -16.08513 | -46.62396 | 2025-03-20 04:04:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 004c0d8c-1490-3bfb-85eb-bacef4071252 | -19.83531 | -40.11304 | 2025-03-20 04:04:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 245f421e-5c43-3797-b0b9-eaa058e442f7 | -17.37753 | -42.48386 | 2025-03-20 04:04:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87663768-d28b-3f9f-aaae-b7f283034801 | -19.83591 | -40.1088 | 2025-03-20 04:04:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 666cd398-e97d-35a4-8be7-ee9fd3057596 | -15.34593 | -46.96167 | 2025-03-20 04:04:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 718f5a4a-927f-3a5e-8d13-fa1b627992a2 | -14.73031 | -46.8334 | 2025-03-20 04:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cec3c426-2e75-370e-a4d3-53635c0b8501 | -22.54103 | -48.81226 | 2025-03-20 04:06:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 509a084f-2f67-36a6-a910-78d57ef5ce7a | -22.61325 | -46.9799 | 2025-03-20 04:06:00 | NPP-375D | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3424ee7b-2d74-3c1c-b25a-3b5b510a656f | -19.42818 | -54.78482 | 2025-03-20 04:06:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b1196d8-f427-3ce8-8656-dccb76e20458 | -19.42786 | -54.78579 | 2025-03-20 04:06:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bcde94b-bb87-3934-b9cb-d7cfa17081b8 | -21.24548 | -54.04576 | 2025-03-20 04:06:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f630089-1752-3ab9-8044-3f7236bb1ba5 | -19.4222 | -54.78307 | 2025-03-20 04:06:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 761e082b-fed4-3925-9659-a96c69e39d83 | -21.003 | -48.64468 | 2025-03-20 04:06:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| eb8cc48c-fae5-373c-8d84-6318f4b62d75 | -19.43381 | -54.78764 | 2025-03-20 04:06:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac44a13e-59b3-38c8-8579-fdd9181c0bf7 | -25.52535 | -54.59887 | 2025-03-20 04:06:00 | NPP-375D | FOZ DO IGUAÇU | PARANÁ | Brasil | 4108304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6538614f-738d-30bc-9aab-7663df0d8522 | -20.98363 | -48.63641 | 2025-03-20 04:06:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a629452c-5d1d-3342-a90f-6143989f8f1a | -21.24236 | -54.04637 | 2025-03-20 04:06:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14a13dba-4804-37b9-b7eb-6e7f45f4b002 | -21.11815 | -55.66697 | 2025-03-20 04:06:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6c9819a7-c806-3795-881c-ca11e8be47df | -21.23897 | -56.46512 | 2025-03-20 04:06:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e51007ce-e728-3b7b-8355-eaadd2e069b6 | -21.11939 | -55.66172 | 2025-03-20 04:06:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a940da1-67ee-3286-bbe4-c50b48aa6633 | -20.98764 | -48.63733 | 2025-03-20 04:06:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 009e03ce-35bb-362b-8d9a-a4711a16c923 | -19.42188 | -54.78404 | 2025-03-20 04:06:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6ca9a70-ed6a-34d8-915d-ac83359ccf5d | -27.33466 | -50.57616 | 2025-03-20 04:08:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 80ae4c3a-d488-392c-ab39-76ef99483389 | -29.66949 | -51.29219 | 2025-03-20 04:08:00 | NPP-375D | CAPELA DE SANTANA | RIO GRANDE DO SUL | Brasil | 4304689 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 259d1f74-1402-3dcd-85de-2fc3cdb31ad6 | -30.74375 | -52.66171 | 2025-03-20 04:08:00 | NPP-375D | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| 953991bf-0b57-38c6-8880-994a4f06c6d6 | -29.87309 | -51.15779 | 2025-03-20 04:08:00 | NPP-375D | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| b81730cc-3796-3859-aa4e-50305883c24d | -29.66869 | -51.29623 | 2025-03-20 04:08:00 | NPP-375D | CAPELA DE SANTANA | RIO GRANDE DO SUL | Brasil | 4304689 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 5ee611c9-6fde-3027-8aec-48a320aa19cc | -27.68888 | -48.75285 | 2025-03-20 04:08:00 | NPP-375D | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2af77d44-cc97-3aae-8a33-b5f5346b066f | -27.68523 | -48.75199 | 2025-03-20 04:08:00 | NPP-375D | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1a3759c2-2246-3ffd-a2dd-b115034e8f46 | -6.24159 | -44.82649 | 2025-03-20 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c025cb7-90fd-3263-a699-1ae966bab9fa | -7.06052 | -44.38048 | 2025-03-20 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3e6c659-459b-3b67-8133-a16fd939b35f | -7.06168 | -44.37296 | 2025-03-20 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 46955780-bd1c-35d8-825d-c3b0c614fbba | -7.0651 | -44.37349 | 2025-03-20 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6601a718-72c9-3018-a3dc-f3f2f198df3c | -7.05994 | -44.38422 | 2025-03-20 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2e839db-726b-3e1b-a98c-ca63e13f8ec3 | -5.67524 | -45.212 | 2025-03-20 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d7a69c6-7d41-3735-b842-fe3b8f02a9d4 | -6.24494 | -44.82702 | 2025-03-20 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5411d825-07b9-3d88-af51-9067b4da19b1 | -7.05768 | -44.37621 | 2025-03-20 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 362ee51c-c4be-3c0f-b95d-33ad7bfdc994 | -6.83515 | -44.32007 | 2025-03-20 04:23:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8330ada8-3cbb-3817-9a2b-274fff608da5 | -5.97014 | -43.75257 | 2025-03-20 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18621422-9d17-3333-885d-c646839e1e8b | -7.0611 | -44.37672 | 2025-03-20 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5a61bbf-47a3-3b80-a0e9-d750a4fe2720 | -7.0571 | -44.37996 | 2025-03-20 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b3025a4-7c79-3065-9725-9e4ece34064f | -7.24377 | -44.78006 | 2025-03-20 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5e2fb94b-3502-3d10-ba1e-ab6f221d04d6 | -7.05652 | -44.3837 | 2025-03-20 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b599735d-a01d-303a-b3c0-4a730b5eb870 | -7.24771 | -44.77695 | 2025-03-20 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd6289df-6cb7-3f72-8657-de2b10113a12 | -7.2432 | -44.7837 | 2025-03-20 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22aca078-9bb7-3959-8d4b-64f1bb1e495d | -7.24715 | -44.78059 | 2025-03-20 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4ac90b9-7064-3177-ae26-38e39f40ed6a | -12.09824 | -45.62315 | 2025-03-20 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fac25ee1-f6fb-34c9-8293-8e0c10a92265 | -14.85745 | -45.19881 | 2025-03-20 04:25:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14d732b2-6b02-3705-abb8-56d2c5724335 | -12.33083 | -49.99255 | 2025-03-20 04:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b821195-fad2-3df2-b3c4-a1142c02d90d | -11.57297 | -47.6299 | 2025-03-20 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 649fb0c5-a5cb-3064-b699-72b22adda8db | -12.09369 | -45.63013 | 2025-03-20 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1a924e9-2a59-3029-a56c-ad560352d128 | -12.32866 | -48.0065 | 2025-03-20 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 130e1c56-8148-312f-97e6-2f3d0344e72c | -13.26154 | -54.38954 | 2025-03-20 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b54a5f6-a73f-35a1-8917-9016e439c8fb | -12.09483 | -45.62263 | 2025-03-20 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fd0374a-bfe8-362b-92b6-2c86128d01bf | -12.09767 | -45.62691 | 2025-03-20 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df0c26b0-314d-3f1e-a9e4-6ab5dc228e6c | -12.09994 | -45.63493 | 2025-03-20 04:25:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad75d826-7caa-39d3-8b5d-65a77f391811 | -12.90947 | -45.06338 | 2025-03-20 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 273af0bc-13de-3a7b-b742-9d9679b5a920 | -12.91357 | -45.05993 | 2025-03-20 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| efe814f2-241b-380f-8643-6823242f31ae | -12.09937 | -45.63868 | 2025-03-20 04:25:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9219aaa0-b43b-3231-a6d7-c325f6d8871f | -12.58584 | -48.33227 | 2025-03-20 04:25:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a2f0907a-00f3-3b8f-904e-c10c87a28490 | -12.09085 | -45.62585 | 2025-03-20 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4513efa7-1f8a-3114-83df-b2795bd6b463 | -15.35097 | -46.95708 | 2025-03-20 04:25:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26143993-71e6-37d9-808e-7dc8fcf0bcd9 | -11.57572 | -47.63395 | 2025-03-20 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a2db519-bf40-3b1f-b6ce-df3a006f7eb9 | -11.57628 | -47.63044 | 2025-03-20 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README3.md)
