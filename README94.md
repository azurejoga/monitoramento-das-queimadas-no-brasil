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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42589106-83ed-3614-b157-922c9504eea8 | -17.59279 | -45.80511 | 2026-09-28 16:22:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| d7375f8e-6088-339b-a095-ab02a69ed33f | -18.13125 | -44.3609 | 2026-09-28 16:22:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 49b9e21b-e0f8-3ae4-a3c0-f2a42df2bfe4 | -17.20496 | -42.21137 | 2026-09-28 16:22:00 | NOAA-20 | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| ba802572-7f83-3a0d-aab3-c8820eaa32db | -17.72411 | -44.33854 | 2026-09-28 16:22:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 320c5959-e775-3cce-9f0f-a1bec285827a | -19.41061 | -48.44206 | 2026-09-28 16:22:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 29fc8181-1510-3c00-b41d-3bc43f3384fa | -19.41519 | -48.44574 | 2026-09-28 16:22:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 6a7dea5e-b08c-3a99-b57e-ec0e8576e627 | -17.83031 | -44.38496 | 2026-09-28 16:22:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8dc4e3f4-cd26-3179-a9ae-6deeb7fe72f8 | -21.57934 | -45.81868 | 2026-09-28 16:22:00 | NOAA-20 | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 714a412c-9189-395d-8023-d7e598d1ac16 | -18.80283 | -42.22943 | 2026-09-28 16:22:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 8695ce07-5c83-39ae-a3ae-081842db03d3 | -17.79445 | -47.15596 | 2026-09-28 16:22:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 46e6cff1-4490-37a9-89c0-7836ea214ea8 | -21.25569 | -46.07043 | 2026-09-28 16:22:00 | NOAA-20 | ALTEROSA | MINAS GERAIS | Brasil | 3102001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 60c61e54-c2e2-3b6c-bf46-f09cb88a6bc8 | -19.99179 | -43.24704 | 2026-09-28 16:22:00 | NOAA-20 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 18a77665-7049-33bf-b1b7-34ae363465df | -20.56167 | -47.00822 | 2026-09-28 16:22:00 | NOAA-20 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 99677638-4013-3dd3-b983-6fa9d2626e28 | -17.895 | -44.53165 | 2026-09-28 16:22:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ec52cbf1-925f-3fca-be26-9b0e6bfe40d2 | -19.15646 | -40.25802 | 2026-09-28 16:22:00 | NOAA-20 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| fdbe038e-fdcd-35e9-9cee-0a4a9966c5ac | -19.13062 | -46.67896 | 2026-09-28 16:22:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 214a4a66-a904-3226-b965-d34f3d50c0cf | -20.75761 | -51.30857 | 2026-09-28 16:22:00 | NOAA-20 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| a38e478f-8fe7-36de-ad96-29a038c14873 | -18.06336 | -41.43216 | 2026-09-28 16:22:00 | NOAA-20 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 8ab979cf-cb77-352d-8e94-53185c1fcbf5 | -18.18935 | -43.84377 | 2026-09-28 16:22:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 596571d0-84f9-3674-ad3e-871d578cf173 | -18.77386 | -45.10755 | 2026-09-28 16:22:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f44dc8ad-1a14-3a1a-bbb0-aaa0bdee0572 | -21.00471 | -46.47091 | 2026-09-28 16:22:00 | NOAA-20 | BOM JESUS DA PENHA | MINAS GERAIS | Brasil | 3107604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 536a4c15-b527-388a-ad7d-f8c81ffcdd20 | -18.32043 | -41.49557 | 2026-09-28 16:22:00 | NOAA-20 | PESCADOR | MINAS GERAIS | Brasil | 3150000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| aa184d17-3621-3cb8-a80c-050f78f165b7 | -22.76542 | -46.48246 | 2026-09-28 16:22:00 | NOAA-20 | PEDRA BELA | SÃO PAULO | Brasil | 3536802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 4585dc89-9fcb-3d35-a876-be40a3960697 | -24.95975 | -50.96922 | 2026-09-28 16:22:00 | NOAA-20 | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| fb366fa7-3f25-322c-8a58-f9e9a7c58981 | -19.04035 | -40.79756 | 2026-09-28 16:22:00 | NOAA-20 | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 2a27b702-32fd-38cf-8425-97b6947d459e | -17.86248 | -43.03467 | 2026-09-28 16:22:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd98b1d6-bdd5-3311-80cf-fe70cec4aabf | -20.75706 | -51.30497 | 2026-09-28 16:22:00 | NOAA-20 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 5324293e-23b7-3616-82d5-2b5cc64d6922 | -21.90905 | -45.3514 | 2026-09-28 16:22:00 | NOAA-20 | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| a8fbe816-9f5a-30b9-a0d9-0eea9dbb9192 | -17.59329 | -45.80901 | 2026-09-28 16:22:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 9c9a2bbe-982a-355e-a941-8348bc62b83c | -18.46375 | -46.43139 | 2026-09-28 16:22:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5e19272f-cea6-3232-8b39-91ff6016d3c9 | -21.53694 | -45.61112 | 2026-09-28 16:22:00 | NOAA-20 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 2e710c21-858e-3e3b-a0c7-1922b34348bc | -21.53746 | -45.61555 | 2026-09-28 16:22:00 | NOAA-20 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 3de822cb-acdf-3b71-a9f2-6470ebc4a80b | -20.36728 | -47.09678 | 2026-09-28 16:22:00 | NOAA-20 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 601a391e-a37e-3059-9b48-4a8b263c3122 | -18.6801 | -48.62525 | 2026-09-28 16:22:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 44.8 |
| dd29cf99-a553-3568-8c96-84d6174344ef | -18.12985 | -47.55334 | 2026-09-28 16:22:00 | NOAA-20 | DAVINÓPOLIS | GOIÁS | Brasil | 5206909 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 288ba193-f3b6-3926-ae08-429b2d4d34f6 | -21.09464 | -43.26313 | 2026-09-28 16:22:00 | NOAA-20 | MERCÊS | MINAS GERAIS | Brasil | 3141603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d3419ea6-18d9-3e4e-beba-c1916b14c1d8 | -21.40179 | -45.16424 | 2026-09-28 16:22:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| aaf4a8d0-5e10-3804-8c47-0ca84734c756 | -20.29562 | -42.05138 | 2026-09-28 16:22:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 980e0423-bd4a-3561-9a33-00368bebbf29 | -21.3625 | -43.79799 | 2026-09-28 16:22:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 13e3bf61-c986-33e9-acac-c1ece9e0a3d7 | -20.37419 | -41.56283 | 2026-09-28 16:22:00 | NOAA-20 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 7477d31b-1295-3e53-8aec-3e548170a236 | -19.13511 | -46.67849 | 2026-09-28 16:22:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 5119ea0f-5ce9-3286-9cd6-aafd5f05a8dc | -20.29911 | -42.05078 | 2026-09-28 16:22:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 31277996-d1f1-3cb1-b649-63d2eb9d3699 | -18.09523 | -44.03068 | 2026-09-28 16:22:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a52d377a-b296-3549-8d06-7c06ca9e559e | -19.1452 | -42.22959 | 2026-09-28 16:22:00 | NOAA-20 | PERIQUITO | MINAS GERAIS | Brasil | 3149952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 2c56c18e-5700-311d-872a-f350a9adbce6 | -23.04911 | -51.15837 | 2026-09-28 16:22:00 | NOAA-20 | SERTANÓPOLIS | PARANÁ | Brasil | 4126504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| fc9f86dd-561e-3d08-bcc3-9db7497537c7 | -22.24924 | -44.6691 | 2026-09-28 16:22:00 | NOAA-20 | ITAMONTE | MINAS GERAIS | Brasil | 3133006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 2fb84fc9-8250-3809-a844-dcff2d61f7a2 | -17.01629 | -39.53308 | 2026-09-28 16:22:00 | NOAA-20 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5f3e2a95-6379-39cb-826e-69df7125b988 | -18.74198 | -48.22824 | 2026-09-28 16:22:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 90b76d3b-d453-35cd-9bf9-163824a804ac | -21.1144 | -43.68139 | 2026-09-28 16:22:00 | NOAA-20 | ALFREDO VASCONCELOS | MINAS GERAIS | Brasil | 3101631 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 4ef52085-7d35-354b-a7e8-19a016587da2 | -16.79286 | -39.40659 | 2026-09-28 16:22:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c5ad980a-1a58-334b-90ce-4434c1cb9a64 | -18.00096 | -41.91634 | 2026-09-28 16:22:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| e9c5ec15-668b-37b1-9d75-12e682dadbea | -17.93275 | -42.71202 | 2026-09-28 16:22:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c4a36b57-586b-3fb5-abfe-7afa14f0d708 | -16.72289 | -39.87321 | 2026-09-28 16:22:00 | NOAA-20 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 89bdb025-4d1c-3838-9f48-312bcf0dd213 | -20.78172 | -51.30279 | 2026-09-28 16:22:00 | NOAA-20 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 58d368a7-2d45-37c9-a81e-30c362fcc78d | -19.26601 | -47.29155 | 2026-09-28 16:22:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f0b705bb-76f5-39f6-8900-f65c1eac2ded | -21.74589 | -46.11363 | 2026-09-28 16:22:00 | NOAA-20 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 588e0d01-11ad-3641-9ef6-9c5d4ad51dda | -20.99139 | -46.28666 | 2026-09-28 16:22:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 52838c65-13f5-33a5-b0c2-6c638f939ddd | -21.54176 | -45.6148 | 2026-09-28 16:22:00 | NOAA-20 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a123913c-51f2-34b1-a570-f2d02abbf85a | -18.74409 | -48.23305 | 2026-09-28 16:22:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| b11bf0bd-0a8e-3e3a-84b3-43f50839ac6f | -21.23117 | -44.34648 | 2026-09-28 16:22:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 1cc78e18-3e11-3194-add5-734b0f85ef67 | -20.35598 | -46.38559 | 2026-09-28 16:22:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4c1296e6-8d21-381c-b35c-49ee6fe4de0e | -18.34967 | -42.31105 | 2026-09-28 16:22:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| d74f772f-d3eb-35da-a3e5-8d359589adf5 | -21.47113 | -43.774 | 2026-09-28 16:22:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| f40410ac-af98-31e7-bbf3-b665dcbfe84a | -17.89042 | -45.05745 | 2026-09-28 16:22:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9c741f20-2711-3f04-b30e-27cd4d9867d6 | -17.20838 | -42.21083 | 2026-09-28 16:22:00 | NOAA-20 | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 6a3d1123-f433-3a03-a8f2-255d32e58a48 | -18.15751 | -47.91338 | 2026-09-28 16:22:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5896e679-7124-3040-800c-e8fa405f897b | -18.02021 | -39.70258 | 2026-09-28 16:22:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 193cdc92-c859-3886-b6b2-5f1da0cd3929 | -20.85962 | -44.89314 | 2026-09-28 16:22:00 | NOAA-20 | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1134d0bc-2ab0-301e-93e1-6835ad4a764d | -19.32844 | -40.7772 | 2026-09-28 16:22:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d3bea913-aefa-36a2-9263-28697608f204 | -20.76423 | -51.31314 | 2026-09-28 16:22:00 | NOAA-20 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| 86166fa7-322a-35df-ade6-d3b8ca33e8eb | -17.93625 | -42.71147 | 2026-09-28 16:22:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| f167c832-7c42-3cc3-b015-4d9104fa1c55 | -21.53901 | -47.12488 | 2026-09-28 16:22:00 | NOAA-20 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 2d3d34af-9a93-36df-ad6a-bf8566f93198 | -19.90649 | -41.91624 | 2026-09-28 16:22:00 | NOAA-20 | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 5fa0045a-4469-3ace-a13e-0d09170119ef | -16.26173 | -39.4192 | 2026-09-28 16:24:00 | NOAA-20 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 815de1a2-ebae-3e00-9ff0-98491d89fb08 | -14.37916 | -40.34475 | 2026-09-28 16:24:00 | NOAA-20 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| cf1b8860-3f20-3c4e-b49e-e7c6a8f8389a | -13.93691 | -47.81569 | 2026-09-28 16:24:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8979b03c-4ecd-31c6-ad8e-2ae419146256 | -11.20869 | -44.75801 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ea8f7118-9864-3247-b8af-d2f632240146 | -15.05626 | -54.60254 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 6cbfd88a-ae22-3d71-9aa1-bcd1119b5d9a | -12.43382 | -44.14658 | 2026-09-28 16:24:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 47d31461-ff31-3080-bb8c-d291d399c415 | -12.5906 | -51.94322 | 2026-09-28 16:24:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f56d0f79-478e-3bea-ba28-97ca981f42cf | -15.40666 | -47.90687 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 406fc280-8323-342f-8994-7d880b2e0a1d | -12.86977 | -44.81594 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 145.5 |
| b710b2fe-26c7-3908-a2f4-4ba647ff59d3 | -12.59315 | -51.96581 | 2026-09-28 16:24:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 248d8212-ea13-3dd5-8029-a707d9ce13a1 | -15.40206 | -47.90768 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| aeadc1dc-ae3f-3a02-885e-2aaffabdc32d | -11.85893 | -47.10534 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fa88cc0b-7057-32b4-a075-a85f6e3f0a87 | -12.0811 | -38.86873 | 2026-09-28 16:24:00 | NOAA-20 | SANTANÓPOLIS | BAHIA | Brasil | 2928307 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| c72b6bef-cbff-36c5-a9c1-4ae1f60e4d1c | -11.68094 | -44.53239 | 2026-09-28 16:24:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 16430285-17cb-33ba-b779-a8fabd3b851b | -11.21851 | -44.78752 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 7cbb2ebc-acde-3c6e-ae4e-9b994ad0bcd4 | -15.15197 | -43.57706 | 2026-09-28 16:24:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 22.5 |
| eb1ca77d-3090-38fe-8d28-211782a8a18a | -12.87283 | -44.81103 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 145.5 |
| f65e1845-ef4a-33f0-a640-4166fef9f7d0 | -11.53824 | -47.38659 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 1078f5b0-d17d-31ab-888c-3f9cb0839bdf | -11.37763 | -43.38241 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| b0e41c44-6ca0-3456-aa34-e82a15c11291 | -16.11735 | -41.60752 | 2026-09-28 16:24:00 | NOAA-20 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 2f35c5b1-5a38-3f1d-b4ae-a642d2c13999 | -12.65165 | -39.83627 | 2026-09-28 16:24:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 224.6 |
| a4848b17-62da-33bb-b58b-de8d8d9ec198 | -14.66936 | -41.1067 | 2026-09-28 16:24:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cb97e20e-cb8c-3686-a471-6cb4c330e6eb | -14.48817 | -45.23016 | 2026-09-28 16:24:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| cbab5807-b390-30b9-9e36-83064b84f69e | -15.21307 | -46.19053 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| deecb455-1385-3f88-9c28-613c39aa9c0e | -12.79645 | -50.59249 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 6f285ec4-15a7-3c2b-9f48-e28935b22561 | -14.12121 | -46.29042 | 2026-09-28 16:24:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 50b4c30e-4ff4-3f38-b93f-e18ccd15bf32 | -12.48788 | -44.72507 | 2026-09-28 16:24:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README95.md)
