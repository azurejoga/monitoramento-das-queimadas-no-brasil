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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa63003c-f0a1-3927-8a46-e905f98cd677 | -21.48699 | -48.66322 | 2026-03-03 04:55:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53b69484-64a7-33a8-b5d5-bf8ef7a8a494 | -20.46472 | -55.04494 | 2026-03-03 04:55:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad6d3739-79b2-30c5-b18a-b084d3ab4124 | -17.52739 | -53.70842 | 2026-03-03 04:55:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49cb5d31-16e4-3230-97f7-1bfc30a6ef74 | -16.91532 | -52.36724 | 2026-03-03 04:55:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b770e91-7437-33f9-aa58-3302dcfe4417 | -18.80257 | -57.6357 | 2026-03-03 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| c3e8dfaa-81ea-35de-82a4-ee0a0e022574 | -20.80735 | -49.83884 | 2026-03-03 04:55:00 | NOAA-21 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 52b7e2e0-3879-33fe-b2ca-1815bfccdef0 | -20.46805 | -55.04552 | 2026-03-03 04:55:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76ef06e3-5b72-3a41-a26f-d5af50231360 | -18.814 | -51.61101 | 2026-03-03 04:55:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| aba27a31-ef6b-305d-893f-755152b64cda | -17.52795 | -53.70467 | 2026-03-03 04:55:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b7b48c9-9f0a-3b30-a0e8-e892867a88f1 | -20.81161 | -49.83949 | 2026-03-03 04:55:00 | NOAA-21 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 26fb4344-1431-3734-8f45-469d783d2cf2 | -20.80787 | -49.8346 | 2026-03-03 04:55:00 | NOAA-21 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1ea884de-ae43-387f-8cd8-7fc869b9eab7 | -20.47395 | -56.72922 | 2026-03-03 04:55:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa08713d-591c-35f6-a2e3-541ca607dc3d | -18.81527 | -51.60156 | 2026-03-03 04:55:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9090ab42-3344-3e12-a877-c90dc5c1f97b | -17.52906 | -53.69715 | 2026-03-03 04:55:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7def895-195b-3d6a-9a76-d7c276dcf23d | -18.79443 | -57.64225 | 2026-03-03 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3b668c41-195b-3f12-9784-ab83e8676d4d | -20.18408 | -45.41174 | 2026-03-03 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 643dd2d0-a814-31d4-9187-5cdc669413c0 | -21.63656 | -48.98428 | 2026-03-03 04:55:00 | NOAA-21 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d16d48e9-9f5e-39c1-ad8e-4a8110478e5f | -18.79981 | -57.63118 | 2026-03-03 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| cd3cce03-15ad-36dd-ba52-cf25fd56d715 | -20.06611 | -50.47007 | 2026-03-03 04:55:00 | NOAA-21 | TURMALINA | SÃO PAULO | Brasil | 3555307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f5023293-ebb1-36d0-96ab-650ef626511e | -20.81214 | -49.83522 | 2026-03-03 04:55:00 | NOAA-21 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 53f1ce75-e5d7-3365-b83d-1732cf4a3fca | -18.81027 | -51.61039 | 2026-03-03 04:55:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 63cfcdba-0990-3371-960e-843870433101 | -18.80717 | -51.60505 | 2026-03-03 04:55:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c029c04-db42-35fa-ab34-8f8bdf6febce | -21.70304 | -48.43145 | 2026-03-03 04:55:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 394376bb-e039-3935-a61d-e0a895e01598 | -18.79378 | -57.64616 | 2026-03-03 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9535c1b6-8fee-3d35-ad2c-30666a21acab | -21.70245 | -48.43678 | 2026-03-03 04:55:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a262c1b-b846-38f3-8cf5-6693e3a8861e | -27.26661 | -51.4558 | 2026-03-03 04:57:00 | NOAA-21 | ERVAL VELHO | SANTA CATARINA | Brasil | 4205209 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7d72a8fe-ffca-3822-87e3-79e26639a63f | -22.31247 | -54.72326 | 2026-03-03 04:57:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7b2843af-f947-3453-a77c-7f253681b8de | -27.98754 | -50.65445 | 2026-03-03 04:57:00 | NOAA-21 | CAPÃO ALTO | SANTA CATARINA | Brasil | 4203253 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f43d9703-059b-37f6-ab18-134dd687a7d6 | -21.80777 | -52.717 | 2026-03-03 04:57:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9d316ec3-aca6-3c61-aa7a-24988c229b72 | -21.80287 | -52.72569 | 2026-03-03 04:57:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a7385c7b-57cd-3504-9f59-1ac04def1350 | -21.80046 | -52.71587 | 2026-03-03 04:57:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5b736fde-f5c1-3775-8359-d75784e0c452 | -23.04489 | -52.3473 | 2026-03-03 04:57:00 | NOAA-21 | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f3eb3a9b-3931-3f4c-a436-e4caf531e312 | -25.22089 | -53.28162 | 2026-03-03 04:57:00 | NOAA-21 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 87bd35e6-1de7-3ecf-b16c-f3e019208afb | -25.22025 | -53.2865 | 2026-03-03 04:57:00 | NOAA-21 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 1b9b35cd-d07d-31b0-89d3-d97a6c47c6bf | -27.99198 | -50.65521 | 2026-03-03 04:57:00 | NOAA-21 | CAPÃO ALTO | SANTA CATARINA | Brasil | 4203253 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a1cce745-b740-3fab-a4e7-78bfcafbb8bd | -21.80108 | -52.71122 | 2026-03-03 04:57:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 41a2ff60-f7d8-3364-abd7-2997a1947a91 | -27.16885 | -51.37041 | 2026-03-03 04:57:00 | NOAA-21 | HERVAL D'OESTE | SANTA CATARINA | Brasil | 4206702 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d358db54-8349-333b-ac4e-e8dc6550d0e6 | -21.27753 | -57.50187 | 2026-03-03 04:57:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28a1431f-00c9-3ab2-ac3b-da0460609e2f | -27.24693 | -51.47893 | 2026-03-03 04:57:00 | NOAA-21 | ERVAL VELHO | SANTA CATARINA | Brasil | 4205209 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 52f8b3a1-452a-3140-b5ba-d583a37ce808 | -31.05542 | -53.13987 | 2026-03-03 04:59:00 | NOAA-21 | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 0.2 |
| 1f7ab438-d886-34ad-8e0b-07a4579a33a5 | -31.94156 | -52.16166 | 2026-03-03 04:59:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 0e89cee8-6b9e-3f4b-b545-9fbbd958a7dc | -30.45455 | -51.73934 | 2026-03-03 04:59:00 | NOAA-21 | BARÃO DO TRIUNFO | RIO GRANDE DO SUL | Brasil | 4301750 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| bf786b86-85cd-3fa4-8859-476dfb9e42c2 | -31.05073 | -53.14522 | 2026-03-03 04:59:00 | NOAA-21 | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 0.2 |
| 850afa34-8b08-3572-869c-cd296bcf85d8 | 1.5047 | -59.9116 | 2026-03-03 05:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.8 |
| b655928e-9ce6-3f00-8831-00a69af2ae27 | 1.5047 | -59.9116 | 2026-03-03 05:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 0834c9fd-edc7-31c4-b583-385f2908de12 | 2.31928 | -59.87455 | 2026-03-03 05:20:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5548d6e3-051e-30cd-8c8a-cb435220adcb | 3.88668 | -60.7628 | 2026-03-03 05:20:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c89e642f-eb44-3320-bd0e-3a516c31b3c8 | 4.2738 | -59.90475 | 2026-03-03 05:20:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17b000d5-2d1c-3a56-91c4-f44117885dbc | 3.03012 | -60.66312 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d58eca4-fd37-323c-96ae-2199afb948df | 2.52554 | -60.98896 | 2026-03-03 05:20:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5cc1d4af-0f64-32b2-93e5-59136ffee2ee | 2.90745 | -60.61557 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ba3a1cd-3241-36eb-afa8-a2a7a92a09c7 | 2.64816 | -60.1136 | 2026-03-03 05:20:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb03a2aa-f668-3d12-bd5c-19bef527d2f1 | 3.03388 | -60.66253 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88f7e891-e911-33eb-81d7-4610b1fd0168 | 2.89636 | -60.62438 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00cae73b-e34c-3235-ba38-1c31643ee9f9 | 3.11832 | -60.48273 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc0757da-daf9-3e11-824a-4eff8b1d3b69 | 3.56953 | -61.73327 | 2026-03-03 05:20:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 316a4740-7266-330e-b573-69943483d374 | 3.64137 | -60.97955 | 2026-03-03 05:20:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a85120b6-618e-3169-9b5e-3bf8286148a8 | 2.89332 | -60.62942 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dcc32f77-47ae-3438-9c2b-d2d2d99d4509 | 4.2417 | -59.91496 | 2026-03-03 05:20:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12d00dab-4bf6-3e97-9a40-fe03ea81be5a | 3.15631 | -60.70594 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb4cb766-3888-3359-830c-d473ff22b752 | 1.96159 | -60.51687 | 2026-03-03 05:20:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f8da14e-43ba-3272-8bcd-4430da809b93 | 3.16385 | -60.70475 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 588881c0-bac2-3a48-9f67-9ec3dbb77afe | 2.89384 | -60.62683 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e9b6534e-1844-379d-913d-df4664e9b06e | 2.42052 | -60.1114 | 2026-03-03 05:20:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f02c8982-f113-3662-8e9e-11c0db3de00d | 3.17537 | -59.91099 | 2026-03-03 05:20:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed20a453-5b47-351b-88a2-2c1d82c54cae | 4.64587 | -60.69678 | 2026-03-03 05:20:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be752ac2-c361-39a6-9f0f-605cee9211b0 | 3.9352 | -59.97964 | 2026-03-03 05:20:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 951ab99f-6d06-34e2-b4e5-bdef144693e8 | 3.63751 | -60.98013 | 2026-03-03 05:20:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e4e05cc-8225-322d-ab0d-2fd13bb6610c | 2.86505 | -60.81869 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3344b9c2-f0f4-324b-b1fb-b97aa6e3dd7b | 3.93586 | -59.98396 | 2026-03-03 05:20:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cfa71690-b0ab-34e7-a486-5b2a328b9209 | 2.22524 | -60.74836 | 2026-03-03 05:20:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfb5c357-074a-3a37-9fb0-2ba8ab6c2f30 | 1.96091 | -60.51252 | 2026-03-03 05:20:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aef833a1-e233-38c6-ac06-a1db9d14b783 | 2.6858 | -60.06944 | 2026-03-03 05:20:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3c681c3-98e1-38a9-919f-f5fa774cab00 | 3.05197 | -60.65512 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea6132cb-93bb-3842-83b7-c81a3b7c7de8 | 3.03764 | -60.66195 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 039e4f89-79fa-326f-b686-44bdb57e9019 | 2.88958 | -60.62999 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e3bcc140-2270-37df-8226-a76bd2d98b02 | 3.18434 | -60.68739 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6878692e-0dde-3398-92e1-34f4df8fa84f | 3.15114 | -60.69732 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 907bf33d-825d-36ca-8c49-148414cc6b04 | 2.86743 | -60.80898 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed4193ae-8f5a-33e3-b5a0-c2f2cd9919e0 | 3.17368 | -60.6933 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7188042b-8179-3b29-9f91-755c4fc2a2cc | 3.04822 | -60.65571 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29043e2f-478a-3a7a-bf86-31256f8047f4 | 3.63853 | -61.0389 | 2026-03-03 05:20:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e5f5335-ce09-3d0a-9e92-8bcf407a998e | 3.12272 | -60.48657 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8b5a68fc-07a4-352c-afbf-48f9f458e84d | 1.95055 | -60.51855 | 2026-03-03 05:20:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2f968e5a-a0f2-37cb-bb90-5f753ea90a8b | 3.02636 | -60.66369 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a65c22a8-8584-30b2-8e7b-aebbca1d6cab | 2.68283 | -60.07414 | 2026-03-03 05:20:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 651133f6-d571-31b6-9fb4-2037569d356f | 2.41598 | -60.70876 | 2026-03-03 05:20:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aefd72da-39f1-3410-82e5-2082d682ecc3 | 3.1549 | -60.69668 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 30856526-3b0d-30ab-a741-c25babc27f7f | 2.90881 | -60.62451 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a26e6c7-4d05-374f-8519-f13df985af21 | 3.17749 | -60.69297 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9cf84d8e-363e-3726-b44f-de4f7bf2d5e0 | 3.1207 | -60.47334 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73097a78-e61f-3374-8e4c-6d855109238e | 2.4169 | -60.11198 | 2026-03-03 05:20:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c4b38f4-7c6b-3d7c-906b-6c759a26a8d4 | 1.9789 | -60.70097 | 2026-03-03 05:20:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3da68d6-eca7-3d24-85ae-aac4ad3ebdc3 | 3.0407 | -60.65687 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f125cd6-fef4-3171-87b1-2017253be23a | 4.00365 | -60.11585 | 2026-03-03 05:20:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7937025d-101c-3acb-bcb2-0a2eba80ea6b | 2.89028 | -60.63445 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a95e01b9-5f51-3821-b0a5-4cb758be5395 | 2.65179 | -60.11304 | 2026-03-03 05:20:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a780f4c-f678-3fbd-ba14-4069cbfe070c | 2.90507 | -60.62509 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81f1c5c5-620a-38b7-9dad-d0cdb504fd95 | 2.67717 | -60.42262 | 2026-03-03 05:20:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a26b482-4142-3193-8f74-bcd0a81ce10b | 2.90813 | -60.62004 | 2026-03-03 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README6.md)
