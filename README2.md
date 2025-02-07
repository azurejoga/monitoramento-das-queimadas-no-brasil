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
| af903143-0740-364f-8ad4-208cbe6be604 | -10.36356 | -44.8432 | 2025-02-07 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eebd0680-e0c8-3d18-8e8b-5d854123883a | -9.2702 | -47.91409 | 2025-02-07 03:53:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2df40638-1b23-3d38-bb60-44c16d9ae78b | -6.32607 | -43.37154 | 2025-02-07 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 148b441c-848f-3887-b654-a0966cd97c4a | -12.73284 | -42.69719 | 2025-02-07 03:53:00 | NOAA-20 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 508967bb-715a-3d00-8d71-77b650c73035 | -9.27077 | -47.9109 | 2025-02-07 03:53:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a981c153-e131-3462-a848-c89f0519a75b | -9.9854 | -48.08944 | 2025-02-07 03:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b5fb338-4f20-387f-974b-9204ad96200a | -12.10451 | -44.7394 | 2025-02-07 03:53:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c6f6c9df-5611-373f-b204-ecedb74a59df | -10.80679 | -44.51078 | 2025-02-07 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96ad900e-2b66-33f9-a50d-3f33b0677ca0 | -11.95835 | -44.67104 | 2025-02-07 03:53:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83dd1e3b-a7ea-3989-a1d6-fa155c55896c | -8.94289 | -44.24447 | 2025-02-07 03:53:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 066da3b8-66fb-3f29-9d5a-8b58fc4dabfd | -19.83809 | -40.0833 | 2025-02-07 03:55:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c939e3c2-bd91-3db9-88f4-0290f2295e39 | -20.42789 | -40.95317 | 2025-02-07 03:55:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4b86ac7d-12d0-3df9-9ca3-4ac182943d7b | -16.6786 | -43.88586 | 2025-02-07 03:55:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b2e1c5d-d1e5-3b69-9163-3b3c7a2bcfb9 | -20.20488 | -46.67536 | 2025-02-07 03:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5eb84dc2-5e25-32d2-94f4-13e7b458b000 | -15.16461 | -45.6327 | 2025-02-07 03:55:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 592f40be-4125-35f7-887d-9be1373ab580 | -20.19908 | -46.66256 | 2025-02-07 03:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f53daa9-e940-31a8-b420-e44f82ff7fcf | -20.49289 | -44.14796 | 2025-02-07 03:55:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b94ef434-a610-33cf-bae9-5eeb936dc7cb | -13.36266 | -43.8316 | 2025-02-07 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 609cd0d6-59ce-36eb-a2f6-3927ec0bd72f | -15.16863 | -45.63345 | 2025-02-07 03:55:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09d7ade1-61b2-3b10-9fd3-722e22204847 | -16.8066 | -40.44996 | 2025-02-07 03:55:00 | NOAA-20 | PALMÓPOLIS | MINAS GERAIS | Brasil | 3146750 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bea3d4d9-6ef5-3b48-91b2-80f62d13695e | -19.37534 | -44.81872 | 2025-02-07 03:55:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cb1ba3e-3366-3d51-bff1-612bfdb278fc | -8.35196 | -45.18383 | 2025-02-07 03:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6eef5d3-74cf-3108-a262-8e12eed725e7 | -17.09515 | -43.80555 | 2025-02-07 03:55:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4fc6974-01d0-33c7-976a-59cbeb7ae64b | -7.85717 | -40.3827 | 2025-02-07 03:55:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4aa83633-f130-3302-be89-220df2a57954 | -14.17981 | -43.65622 | 2025-02-07 03:55:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9673223b-63ce-3f22-a143-10fafb5ad159 | -13.36365 | -43.83469 | 2025-02-07 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c92a263-b440-3ac7-a3c3-9fb5978071ba | -16.01059 | -47.62948 | 2025-02-07 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4cb1d63e-2ccd-3962-80fa-4397655ed42a | -20.04342 | -44.35838 | 2025-02-07 03:55:00 | NOAA-20 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4cb66ab8-27e4-3f7d-9be8-fc83686c8d7d | -19.43624 | -44.34056 | 2025-02-07 03:55:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a028b854-552b-3c15-b819-eea0db379df1 | -20.19807 | -46.66799 | 2025-02-07 03:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35eb63d9-a566-3f97-a260-a9dde7a2899c | -20.49463 | -44.14744 | 2025-02-07 03:55:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f3bf527c-e094-32b6-b24d-cb01b805f834 | -19.9344 | -41.26966 | 2025-02-07 03:55:00 | NOAA-20 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 258bd9e2-5bdb-3c8d-825d-37cf643eff16 | -14.33691 | -44.11505 | 2025-02-07 03:55:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9f5c603d-2def-3df9-969a-6d6e17068df2 | -19.71826 | -40.3532 | 2025-02-07 03:55:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2ff8499c-fb38-3fce-b69a-b0fed9ee6761 | -17.74852 | -44.75435 | 2025-02-07 03:55:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f2167b1-af31-34ec-948f-f6ec37d46b74 | -8.93986 | -44.24006 | 2025-02-07 03:55:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ba18c7b-0068-3e94-8811-f8c956f6211f | -17.83924 | -42.79678 | 2025-02-07 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1705a12f-a751-3c53-8b4f-f22c22ab73e9 | -20.20197 | -46.66898 | 2025-02-07 03:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ced2feae-4cfe-3c84-a3ee-5aa4957a4425 | -15.07975 | -48.94631 | 2025-02-07 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf1bcc0c-a538-3d9e-9ba0-47678d300c5d | -8.93924 | -44.24375 | 2025-02-07 03:55:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77c5d3aa-3487-383e-a84c-45598c337b52 | -19.16458 | -40.14148 | 2025-02-07 03:55:00 | NOAA-20 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6ff9ed41-1cd1-30fe-a757-3dac90a25783 | -19.84331 | -40.26614 | 2025-02-07 03:55:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f831beec-602f-3b39-add5-451492885df6 | -20.20097 | -46.67437 | 2025-02-07 03:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f925fa16-2bc1-3772-8ff7-f1a8c325d8b0 | -22.90222 | -43.75542 | 2025-02-07 03:57:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3cfcf28f-2cdb-3126-ba68-5544b2467e03 | -22.67489 | -42.8587 | 2025-02-07 03:57:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 51f24e09-350f-31af-a9a8-ecc9173395b9 | -23.31125 | -46.11434 | 2025-02-07 03:57:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 06c9f17a-86f9-39c2-aebd-5b695782b4b9 | -22.78082 | -43.04476 | 2025-02-07 03:57:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 36177a61-5dd2-34ac-8e38-ad6e2a950d1e | -22.78144 | -43.04099 | 2025-02-07 03:57:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 327e590b-aee2-32a4-aad8-72b1da707874 | -22.6755 | -42.85495 | 2025-02-07 03:57:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a9c2cad7-959b-3b6e-801e-c19b330c0bf6 | -23.3367 | -46.77491 | 2025-02-07 03:57:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d3149cd2-df09-33f3-80fa-d745932fa503 | -23.31236 | -46.1123 | 2025-02-07 03:57:00 | NOAA-20 | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 68aecb1d-b1a6-3773-8471-c0c1e522d416 | -22.93322 | -43.31778 | 2025-02-07 03:57:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 45bc60f2-d227-3e6c-b140-b823854bde0b | -20.76198 | -46.76736 | 2025-02-07 03:57:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| eebf9f3e-4e86-3d66-be3a-64aff003c1ed | -21.62635 | -43.4661 | 2025-02-07 03:57:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9ceac629-9b3d-37e0-9dfc-fe68529c307d | -21.62235 | -43.46928 | 2025-02-07 03:57:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f384b97a-baab-3975-a41e-0fc7574af895 | -23.98414 | -48.91983 | 2025-02-07 03:57:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64e92195-45bd-3d3e-8e64-87c854a34aa7 | -20.8749 | -44.44223 | 2025-02-07 03:57:00 | NOAA-20 | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 3fcb0d76-66bc-3a65-b8d9-3d05f889044f | -20.87585 | -44.44141 | 2025-02-07 03:57:00 | NOAA-20 | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 962c18d7-1097-3322-bf67-93b4821a018b | -20.88378 | -43.06731 | 2025-02-07 03:57:00 | NOAA-20 | SENADOR FIRMINO | MINAS GERAIS | Brasil | 3165701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3535687f-c772-3b01-b01b-c8e973b5dced | -23.63094 | -46.42781 | 2025-02-07 03:57:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a866c74d-b36f-3edf-af6a-0a106376ce14 | -23.69736 | -46.68076 | 2025-02-07 03:57:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6d149076-7074-350c-bb27-0a611f6f12a2 | -23.4047 | -46.55465 | 2025-02-07 03:57:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| eab67711-cf6a-3d52-9cb9-ab5dc3a44ec1 | -22.85622 | -42.98122 | 2025-02-07 03:57:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fed7d775-5f3a-3c17-900d-44f9187f6028 | -20.87514 | -44.44552 | 2025-02-07 03:57:00 | NOAA-20 | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b8bc8ecc-6dc4-329d-975a-8bb3dbfee949 | -20.89901 | -43.82073 | 2025-02-07 03:57:00 | NOAA-20 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 12c77248-7e3d-31e5-ab23-b281e71a836b | -5.91454 | -45.40178 | 2025-02-07 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f302434a-863d-3809-8890-008316a79649 | -6.25433 | -48.03629 | 2025-02-07 04:44:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb4e3cea-f549-3ae7-98ce-cfbdc04f23df | -5.84661 | -45.3579 | 2025-02-07 04:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8306069b-6bb3-325d-80e3-8c95d34ae659 | -5.3712 | -46.25082 | 2025-02-07 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 577b1ca6-0bda-3869-bc58-fedde8583b43 | -10.39855 | -46.689 | 2025-02-07 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ce7a760-a202-39a5-b315-37bc0a766c57 | -11.96232 | -44.66793 | 2025-02-07 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cea1c2fb-cb6d-314f-94ef-0bf6c9531149 | -11.57499 | -47.62195 | 2025-02-07 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc5d5140-8ea8-33e2-a034-ecca6c74927f | -13.49734 | -47.41729 | 2025-02-07 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5928974d-9301-3580-8915-c40fd006607f | -10.53788 | -44.67641 | 2025-02-07 04:46:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57c4476d-2391-358c-87c7-e3f5c0dcfccc | -11.4539 | -52.92299 | 2025-02-07 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcf75583-d442-3264-a2ba-4c4e74ae83ae | -11.45115 | -52.91891 | 2025-02-07 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76a65f55-1212-32c5-bac9-6e6469a15444 | -10.72847 | -49.55112 | 2025-02-07 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bae6a0b2-6812-37ea-8e6c-57349bb65284 | -11.57887 | -47.62251 | 2025-02-07 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a3a088e-e0c7-36c3-886f-6f75d9fd6b26 | -11.58276 | -47.62304 | 2025-02-07 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eee5737b-b543-35b2-be92-965cd44d0d07 | -10.39806 | -46.6926 | 2025-02-07 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ff67f97-b5b5-375a-a2ab-9e764f3d9757 | -14.34083 | -44.11642 | 2025-02-07 04:46:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bbea5f3b-cca9-3d77-8bf5-6c0a37d97dd1 | -11.3579 | -48.01326 | 2025-02-07 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 19efda14-5cf8-3a78-b1ea-b93c85130188 | -8.94455 | -44.24283 | 2025-02-07 04:46:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 740be8be-86fd-3557-905b-15b64002e838 | -9.98635 | -48.08457 | 2025-02-07 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b62d109-2547-3c11-8aae-cc9dd54b37a6 | -9.27167 | -47.90951 | 2025-02-07 04:46:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 036de05d-ad9d-34a2-83d0-e21694d8f298 | -10.28382 | -48.3294 | 2025-02-07 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d4b69cb-9247-3f5f-a349-02a3cd35ba5e | -11.33405 | -48.9973 | 2025-02-07 04:46:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fd53b4b-9722-375a-bf1f-7c6497544fec | -11.39572 | -52.94623 | 2025-02-07 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c173776-1c23-3571-9138-ef94f2211a92 | -8.93987 | -44.24212 | 2025-02-07 04:46:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 730b994d-1733-37e4-9989-e5fdaeafe0df | -11.36168 | -48.01383 | 2025-02-07 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b62dd99e-6b2e-3394-b70f-9cbe8292b9db | -11.45058 | -52.92245 | 2025-02-07 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7beb3690-373b-34ff-b4d0-c07d297624d5 | -11.39515 | -52.94977 | 2025-02-07 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa1c7339-8748-3833-b675-5f8c970e042b | -17.46589 | -40.86572 | 2025-02-07 04:48:00 | NOAA-21 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| bfb0fd0c-7b77-3840-a06a-91bb2bed9de1 | -20.20595 | -46.67068 | 2025-02-07 04:48:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1887a70-2a70-3202-b766-ed9e301a6387 | -20.20539 | -46.67571 | 2025-02-07 04:48:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd08dc08-40b7-354c-a3b4-e883d2ac678a | -13.62833 | -55.44955 | 2025-02-07 04:48:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8674090d-861e-3b1c-a85a-7c6964b9e353 | -16.58119 | -39.15175 | 2025-02-07 04:48:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 8da9f11a-891f-3902-9dca-fd0ca8cafd2b | -20.20128 | -46.67027 | 2025-02-07 04:48:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c864da6-61b1-3168-8c10-26ce47113049 | -17.46574 | -40.86725 | 2025-02-07 04:48:00 | NOAA-21 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| eaac65e4-c10f-326b-8983-7fa99236b3ff | -20.20183 | -46.66531 | 2025-02-07 04:48:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README3.md)
