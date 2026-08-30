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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4539c1ba-8c5e-3aa5-8329-3cf4c4697d2c | -14.15683 | -52.81207 | 2026-08-30 04:17:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 02fdc8cb-72d1-3c36-a144-95aa1d4caf97 | -15.65215 | -45.91711 | 2026-08-30 04:17:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cd7c40e5-fef1-305a-881d-544b2f1fed97 | -16.35073 | -50.99099 | 2026-08-30 04:17:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 084a3a17-2698-36c1-a52e-c295680672b9 | -14.1618 | -52.81773 | 2026-08-30 04:17:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2718e5ad-a666-3c80-8779-56659ce44209 | -14.39369 | -52.56108 | 2026-08-30 04:17:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e08787ab-4ddf-375a-a935-eaed019e4e6e | -14.23311 | -52.84438 | 2026-08-30 04:17:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eaa09377-7325-3d35-b5fd-da5e256d37ec | -15.45665 | -52.81227 | 2026-08-30 04:17:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4f6a422-f9d8-3c91-8b89-74c35671ce09 | -16.35189 | -50.98515 | 2026-08-30 04:17:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa194731-1a3a-312b-b2fb-dd53e21a1495 | -20.92809 | -46.03889 | 2026-08-30 04:17:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2859d24b-3902-3eeb-9a37-50ca85f0e5ed | -20.11782 | -48.27365 | 2026-08-30 04:17:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 25.4 |
| a8bae91a-1045-3231-8c72-0e7b28a1d588 | -17.53635 | -44.61503 | 2026-08-30 04:17:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5672cae-3d67-3858-8a80-ee285794140b | -16.89399 | -39.31591 | 2026-08-30 04:17:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9f28518d-81ad-3671-9cd1-a5a693879565 | -16.71905 | -47.63449 | 2026-08-30 04:17:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 889e9e44-3c9a-316b-81f6-e860909e446e | -18.52548 | -42.84966 | 2026-08-30 04:17:00 | NPP-375D | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dd959973-075f-3855-bcf4-2f98e3e11c6a | -18.52558 | -42.15612 | 2026-08-30 04:17:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 78d3514f-31f1-3688-a2d7-acd72fdb9d1b | -17.79585 | -39.70401 | 2026-08-30 04:17:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a6b59341-973a-30b2-be03-7d0ed9110e76 | -14.15094 | -52.81093 | 2026-08-30 04:17:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a5f9c9d-dd04-3920-961f-8342cc92fbee | -13.85954 | -54.11454 | 2026-08-30 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da4d5bdf-623c-394a-a347-a41e0997c124 | -15.10727 | -48.16895 | 2026-08-30 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc69e83d-0376-3ab7-8ed9-0a51693a116b | -14.90003 | -47.74815 | 2026-08-30 04:17:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 166867b5-08e1-378c-9ac1-21ef11ce4a0e | -14.7565 | -48.7424 | 2026-08-30 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d2fab72-d6cd-3a81-b1dc-2c6067dfe77e | -15.13824 | -50.63556 | 2026-08-30 04:17:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0161bdb6-c4d1-3ee0-8454-0ab1720a74b3 | -18.82456 | -47.45971 | 2026-08-30 04:17:00 | NPP-375D | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5866710-5e8d-3aae-9343-ae7064189fe4 | -20.10992 | -48.27195 | 2026-08-30 04:17:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 17679541-ad0a-3be5-a601-16d531e5a02f | -20.11093 | -48.26655 | 2026-08-30 04:17:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6fe7068b-0162-351f-818d-61d8294f76bb | -15.12382 | -53.58615 | 2026-08-30 04:17:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a118140e-9c34-3f67-be1c-09a23ea3ef83 | -17.851 | -39.76263 | 2026-08-30 04:17:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1444e4ac-971d-3d33-8686-2594834f7078 | -14.0356 | -54.01773 | 2026-08-30 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9fd6ee2-b901-3dd4-af8e-f57d5de06449 | -19.23597 | -46.73394 | 2026-08-30 04:17:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7ef38ba-a7c6-3c75-b587-6da924bda406 | -21.60654 | -46.07095 | 2026-08-30 04:17:00 | NPP-375D | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 37ae9108-6d39-3b1d-bec0-d8d0359d8b6d | -20.20265 | -40.39499 | 2026-08-30 04:17:00 | NPP-375D | SANTA LEOPOLDINA | ESPÍRITO SANTO | Brasil | 3204500 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8681aaf2-e3d7-3469-9305-a8fde71a0417 | -19.07857 | -57.39888 | 2026-08-30 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0105d1fd-1d0f-324d-8f09-89fa58ce7daf | -17.273 | -46.04033 | 2026-08-30 04:17:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80c46ffa-7a9f-3cc8-843f-7354ab573def | -14.44691 | -46.22823 | 2026-08-30 04:17:00 | NPP-375D | DAMIANÓPOLIS | GOIÁS | Brasil | 5206701 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8a842a4-3202-3c38-9ced-097114659644 | -18.46138 | -44.89901 | 2026-08-30 04:17:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a324a05-f3c1-397c-ae1e-29e526528dd2 | -21.34084 | -45.66303 | 2026-08-30 04:17:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 026433f1-93cd-3acc-bf7d-7eb35834b751 | -19.87663 | -44.61573 | 2026-08-30 04:17:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d73f923b-df8e-39a8-81d2-72bc4b8412cd | -14.93708 | -56.33691 | 2026-08-30 04:17:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eb2bde9e-4197-3040-9b44-daea1ed9397a | -16.35242 | -50.9825 | 2026-08-30 04:17:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60898ced-e23f-3fbd-a7b5-60a29bb86552 | -16.34794 | -50.97876 | 2026-08-30 04:17:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 88981a2a-3b63-386d-8119-b92f770f85b0 | -14.44207 | -52.55936 | 2026-08-30 04:17:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| efd071e6-07e4-32de-b9a2-bf3365e2a7fc | -14.19658 | -52.87234 | 2026-08-30 04:17:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f63f1f45-6094-335a-9f1d-0a2dc424562e | -14.44219 | -52.55687 | 2026-08-30 04:17:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 628a495c-794d-394f-bee9-ea0bdb779edd | -19.23229 | -46.73318 | 2026-08-30 04:17:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16bd17a7-7553-3ecc-9e86-517c7ce64426 | -14.77273 | -48.73815 | 2026-08-30 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78db4be2-6172-34c7-9f67-0e220c375df4 | -14.24065 | -54.65076 | 2026-08-30 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89a9afa7-45a4-3855-a5f2-57a3d2d5a086 | -14.90074 | -47.7443 | 2026-08-30 04:17:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4755c40-ee14-3bbc-acdb-9fbe835cd39e | -15.11981 | -53.57534 | 2026-08-30 04:17:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98b66b19-2635-3b26-8f92-8e7263d8f9af | -15.38553 | -52.66134 | 2026-08-30 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abd12749-a81e-37b5-9cdb-8d75b3669a67 | -17.7968 | -39.7066 | 2026-08-30 04:17:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 34539b42-b12b-3052-8adc-380461942198 | -14.77353 | -48.73395 | 2026-08-30 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99ba7418-2881-3f7b-a00c-ec5bc6a651a2 | -19.08339 | -57.40002 | 2026-08-30 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 027351bb-ddd1-3184-b6e7-9adb339fd617 | -14.3971 | -52.57369 | 2026-08-30 04:17:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c0fc8cde-4b46-39f6-8081-9fa99ff81e13 | -14.16553 | -52.8156 | 2026-08-30 04:17:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4138abaf-b55e-3a62-ba08-1d832a77632b | -18.66057 | -46.85042 | 2026-08-30 04:17:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60399f16-6952-3cce-a547-651ccd91606c | -14.16856 | -52.81459 | 2026-08-30 04:17:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94069193-0f38-39ad-83f7-5b6694698218 | -17.79322 | -39.70605 | 2026-08-30 04:17:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a96ec73c-c39a-3c64-918f-4bcd2a542cc6 | -14.77157 | -48.73607 | 2026-08-30 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d174a837-d18e-327a-91c2-86456095abed | -14.15771 | -52.80775 | 2026-08-30 04:17:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1ba5f463-67ce-33bc-8a5c-fe14023ee0bd | -14.14327 | -52.8184 | 2026-08-30 04:17:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fdcdf960-0634-3330-ad8e-57f79da0ebae | -14.77598 | -48.7373 | 2026-08-30 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a86e62e1-babf-3a40-ab62-0b6853792740 | -14.03288 | -54.02088 | 2026-08-30 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 401bfcec-d677-3986-8586-75c62f50cede | -17.41704 | -42.6308 | 2026-08-30 04:17:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 20482b1d-b435-3d47-9f9f-7b71ce3124c9 | -19.87325 | -44.61512 | 2026-08-30 04:17:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 984738b1-3898-3b97-96d1-d1bd409402bb | -16.35394 | -51.00114 | 2026-08-30 04:17:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9afd8109-9c4d-399e-bfaf-cef9b41ede5a | -16.86848 | -43.58093 | 2026-08-30 04:17:00 | NPP-375D | JURAMENTO | MINAS GERAIS | Brasil | 3136801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a8a4b34-2f5d-325a-a70c-fc32678686a4 | -18.46482 | -44.89968 | 2026-08-30 04:17:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bcafb8aa-7c98-3e55-8676-b2f286376851 | -20.39446 | -45.4842 | 2026-08-30 04:17:00 | NPP-375D | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97d17ad6-49a2-3e6a-8479-433bf00dcf74 | -20.11488 | -48.26739 | 2026-08-30 04:17:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6d6dbf4a-b043-375b-a518-e2448d86cde2 | -14.7663 | -48.73951 | 2026-08-30 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2b62faf6-84c4-335b-bcd9-74402cbea094 | -14.42012 | -52.54933 | 2026-08-30 04:17:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6c9b37df-de0c-34c3-a2de-c40b7e7f9d47 | -17.41762 | -42.62724 | 2026-08-30 04:17:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 734fe0fb-d1dd-392e-8598-bf04f1a7f81d | -14.76744 | -48.74152 | 2026-08-30 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4be9d370-c508-3c48-baff-dbbafd53e88d | -19.0987 | -46.23879 | 2026-08-30 04:17:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 81426f2b-482c-39a0-b4f8-3677dc61841e | -18.52615 | -42.15245 | 2026-08-30 04:17:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 00aacece-8546-38e3-ada9-305f4cc59419 | -16.35904 | -51.00181 | 2026-08-30 04:17:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fdf24a9-f4fd-3155-94b8-f955ba5cef55 | -14.75729 | -48.73811 | 2026-08-30 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8559734-d254-3435-8e5c-8568369dba92 | -16.28179 | -42.57546 | 2026-08-30 04:17:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0fbe761-e9d4-34f0-8dc7-f18816a7e11c | -20.80552 | -45.61813 | 2026-08-30 04:17:00 | NPP-375D | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2393634c-729a-3b63-9d92-5f7b278a0709 | -16.87184 | -43.58152 | 2026-08-30 04:17:00 | NPP-375D | JURAMENTO | MINAS GERAIS | Brasil | 3136801 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d745e62c-020a-3b41-8927-366529f33ef0 | -14.98857 | -48.1771 | 2026-08-30 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1130dcef-c2fe-3ebd-9e6b-5d9ff845a3b7 | -16.27956 | -42.57563 | 2026-08-30 04:17:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9f6a7d4e-aa9d-3d9b-b2d3-83a3d5cc20eb | -15.39132 | -52.66204 | 2026-08-30 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8df6c290-d096-3053-bb24-7979cab66561 | -15.12483 | -53.58145 | 2026-08-30 04:17:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31b6cfdf-b1bc-356a-8012-01587c11e708 | -17.537 | -44.6111 | 2026-08-30 04:17:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5293d1ae-a42b-3e3f-b50a-35526fdd39ae | -20.80483 | -45.62212 | 2026-08-30 04:17:00 | NPP-375D | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e72f048-1810-31f1-a527-c59c303543b3 | -18.10882 | -42.8754 | 2026-08-30 04:17:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bef8c1ff-e0d7-35ca-a3f9-97578782c60b | -14.21071 | -52.86358 | 2026-08-30 04:17:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8df6826-d210-3698-8bee-79e045de61ab | -19.80957 | -46.75131 | 2026-08-30 04:17:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22e49be5-cce9-3c88-86f3-b1696fcc39f7 | -18.66513 | -46.84651 | 2026-08-30 04:17:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2754c0b4-dccc-3610-8fd8-cc7c73a0322c | -18.46415 | -44.90363 | 2026-08-30 04:17:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54d6e93a-29d5-3fb1-9b5d-6ba90f8c85ec | -14.33577 | -47.22982 | 2026-08-30 04:17:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30d70279-8a7c-3e90-8d1c-0918e26d1e60 | -20.11387 | -48.2728 | 2026-08-30 04:17:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0d02836f-1ab5-398f-892b-f0a4d498ebe3 | -19.80816 | -46.75367 | 2026-08-30 04:17:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 090ee2ae-b372-37c0-9437-41d5fd7fb423 | -17.90602 | -39.92883 | 2026-08-30 04:17:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4aa71b24-ab10-3b15-8e70-460821b7ff24 | -19.07649 | -57.39812 | 2026-08-30 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 50491fc4-e46a-329f-bc76-9ba834a66956 | -17.79523 | -39.70824 | 2026-08-30 04:17:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c79ad28a-84bd-3689-bf34-cdb15a4f4796 | -16.22716 | -39.14246 | 2026-08-30 04:17:00 | NPP-375D | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2a94daf0-e9f1-3152-ad25-1a39229c125d | -14.40697 | -52.55487 | 2026-08-30 04:17:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 930f1ed3-a573-3c52-a062-07072687517d | -14.43474 | -52.56371 | 2026-08-30 04:17:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README33.md)
