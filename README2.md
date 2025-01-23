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
| 5e00a6ca-34bd-3876-b0d6-2791c32f97ea | -12.07805 | -38.01712 | 2025-01-23 03:12:00 | NPP-375D | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 03dc8711-c29a-37dd-8042-da72a5b7d74a | -6.77978 | -35.16695 | 2025-01-23 03:12:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 30a5c9c2-5727-3e05-b702-f80b3b786473 | -6.78458 | -35.16793 | 2025-01-23 03:12:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a33b0882-67d4-3fe4-bd48-a0a2b4e75075 | -8.87819 | -35.41115 | 2025-01-23 03:12:00 | NPP-375D | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| f70e0115-9d59-3ddd-ba15-79b9b32d8afe | -7.41622 | -35.0571 | 2025-01-23 03:12:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 245b662c-2bd9-387b-906b-2a64595f4aa6 | -10.35357 | -38.7105 | 2025-01-23 03:12:00 | NPP-375D | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| daa554c0-cf6e-3d59-ab21-3c91334fdd42 | -9.75678 | -36.97998 | 2025-01-23 03:12:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| db79a30c-8ad7-39c7-b12d-a57b6206128d | -8.8791 | -35.4061 | 2025-01-23 03:12:00 | NPP-375D | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| 013198a3-bf17-3edb-9753-dd58e394de7a | -12.08334 | -38.01832 | 2025-01-23 03:12:00 | NPP-375D | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 08d3dc4c-d93d-366b-8dbd-fa5cd3ad53bd | -6.79812 | -35.17591 | 2025-01-23 03:12:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 68a027ff-7db5-3782-b7d7-9579bc7dfe60 | -10.53768 | -42.43246 | 2025-01-23 03:12:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8372c123-720b-3390-a4d2-915d7facbeb3 | -9.75744 | -36.97645 | 2025-01-23 03:12:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 331de3e9-c09f-3edd-b0ad-8e19d3f186ca | -15.87593 | -38.98896 | 2025-01-23 03:14:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b9196ca8-a68d-3842-afae-dddec7a31fcd | 1.3403 | -60.0461 | 2025-01-23 03:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.2 |
| b9ee65a2-87ef-317c-905c-7069f019058c | 1.3221 | -60.0272 | 2025-01-23 03:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 07c7c815-c8bb-36d3-b008-83958f87b683 | 1.3221 | -60.0463 | 2025-01-23 03:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 13fdfbbc-7168-3866-b697-dac3b18f76d4 | 1.3221 | -60.0463 | 2025-01-23 03:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 2e37917e-5115-305d-a676-1f2408fe4a62 | 1.3403 | -60.0461 | 2025-01-23 03:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 9ff03fb2-98f8-3048-aab7-d6ba777f0807 | -6.07509 | -35.26136 | 2025-01-23 03:34:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 278b9f16-7fcc-3155-907e-0c706a817020 | -9.49991 | -35.59621 | 2025-01-23 03:34:00 | NOAA-20 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 79ee4de5-e587-3a12-bb4b-b2b2fa829a6e | -9.75914 | -36.98165 | 2025-01-23 03:34:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 66d7665b-082e-3b6b-ba61-3891f9596d0f | -6.01436 | -39.41739 | 2025-01-23 03:34:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 80988059-7aba-3e60-9509-7fe0e729e3e3 | -7.41761 | -35.05576 | 2025-01-23 03:34:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 132aee31-1f1e-35a3-8c87-b05267b0e334 | -5.90816 | -35.73144 | 2025-01-23 03:34:00 | NOAA-20 | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2997b784-e828-3943-bc10-c77ac616d1c1 | -7.82313 | -35.18261 | 2025-01-23 03:34:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 836f901a-cd8e-32d9-aa70-da846b15feef | -3.60441 | -38.95121 | 2025-01-23 03:34:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a1abedea-d78d-323c-ada5-29da8f53a257 | -6.07112 | -35.26441 | 2025-01-23 03:34:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 3035fccb-e6fd-33e8-a124-c80f6f5d66df | -6.79732 | -35.17768 | 2025-01-23 03:34:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b64c9e8b-0379-349a-b361-36e64a26b60d | -10.35454 | -38.71078 | 2025-01-23 03:34:00 | NOAA-20 | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| de290cbb-9e31-3a73-8b38-d59079e76d45 | -3.60012 | -38.9505 | 2025-01-23 03:34:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 34957ee1-ae34-3331-ab5b-0232f7fc475f | -9.75981 | -36.97759 | 2025-01-23 03:34:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9fb958d5-3ed7-3c83-b806-d924dcc6a96c | -8.41145 | -40.56935 | 2025-01-23 03:34:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1921c74d-f822-3c5b-8a56-d2a69ecd1d43 | -6.0717 | -35.26077 | 2025-01-23 03:34:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 33498ac3-2e14-35fc-a49c-f48a89f3637d | -7.96284 | -35.23812 | 2025-01-23 03:34:00 | NOAA-20 | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0a53d1f5-cb25-38cb-9fde-6bd30682af3d | -8.36559 | -35.30993 | 2025-01-23 03:34:00 | NOAA-20 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 9bbf4431-63f7-3220-8fdd-365cfe6d31a7 | -9.75117 | -35.8483 | 2025-01-23 03:34:00 | NOAA-20 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 80e876a7-4076-3968-a63f-3af1b74672a8 | -9.75633 | -36.97681 | 2025-01-23 03:34:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 815423ac-b08f-3787-bd66-193da0d5665b | -7.9662 | -35.23867 | 2025-01-23 03:34:00 | NOAA-20 | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 13785ec7-0e71-3e69-9f93-d586f70b7f22 | -12.08057 | -38.01844 | 2025-01-23 03:36:00 | NOAA-20 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5422b7b7-7cc6-3673-97ec-834009ab2e5f | -15.43321 | -40.5033 | 2025-01-23 03:36:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3f53d9a4-008e-390b-b96c-2435e761f2fe | -12.45489 | -43.56577 | 2025-01-23 03:36:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34f7897d-a9cc-3f04-bcd8-857bf9dee760 | -11.45395 | -39.27502 | 2025-01-23 03:36:00 | NOAA-20 | CONCEIÇÃO DO COITÉ | BAHIA | Brasil | 2908408 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1a772a72-48a3-3caa-8ffc-1d43258d79e8 | -13.03382 | -40.33571 | 2025-01-23 03:36:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ef3598df-dba6-3689-8c9b-af89e4107dd4 | -16.04972 | -39.14874 | 2025-01-23 03:36:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| da4fcc14-1eb5-3f60-96f5-255ca31b0d89 | -15.87751 | -38.9916 | 2025-01-23 03:36:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2e6212e7-eb0d-3ca5-b768-fe7368401d5b | -10.53414 | -42.43427 | 2025-01-23 03:36:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f94de813-673e-3d14-95c0-8453632fbbe7 | -11.18641 | -40.19098 | 2025-01-23 03:36:00 | NOAA-20 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c0f1f896-18ce-3808-a6f4-15bc29e9764d | -13.03443 | -40.33226 | 2025-01-23 03:36:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2d730f58-01c1-3674-8746-baf8cb70f007 | -12.11739 | -38.08533 | 2025-01-23 03:36:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c8eb053c-daf1-3182-90fd-3cd654f26223 | -12.08128 | -38.01422 | 2025-01-23 03:36:00 | NOAA-20 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6c2e2ffa-b2fb-30ff-a011-18d0c456d85f | -12.11809 | -38.08112 | 2025-01-23 03:36:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 036ebcb3-3069-337a-b316-d86ded887e1c | -12.45992 | -43.56678 | 2025-01-23 03:36:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3d82dfbf-ddcf-39ff-b954-47249da5de6e | -15.87823 | -38.98736 | 2025-01-23 03:36:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5a35a099-d579-303d-a743-c66cb93c58f6 | -11.65747 | -38.92752 | 2025-01-23 03:36:00 | NOAA-20 | SERRINHA | BAHIA | Brasil | 2930501 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e91a5e6b-e041-31b0-8cf1-ded48ede1b55 | -20.3462 | -40.36049 | 2025-01-23 03:38:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2e4e1335-5f3e-3193-bd3b-2b2a73d83378 | -18.89327 | -39.90314 | 2025-01-23 03:38:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 30584450-2d51-3dcd-88f0-4a93655b027b | -20.34588 | -40.36293 | 2025-01-23 03:38:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fa4c9311-1595-346f-aa48-4d8e47d9bddc | -17.9003 | -39.46275 | 2025-01-23 03:38:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1a9a8c60-b5b8-3d35-9b34-831feceeb819 | -20.98518 | -43.03779 | 2025-01-23 03:38:00 | NOAA-20 | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1a4d6617-2655-3ba5-b97b-ff4a87df0619 | -18.96428 | -39.90601 | 2025-01-23 03:38:00 | NOAA-20 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| aa731255-8dfb-38b7-8af9-b5ef6f3e9680 | -16.34205 | -43.51593 | 2025-01-23 03:38:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c25c686-8c79-3428-ae35-05aaa95579de | 1.3221 | -60.0463 | 2025-01-23 03:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 90849127-e689-3341-bd02-4e88541b3059 | 1.3403 | -60.0461 | 2025-01-23 03:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 665a052c-4815-3175-aa78-fb19558b98c2 | 1.3403 | -60.0271 | 2025-01-23 03:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 7aede473-7520-35b1-887f-0b57a348db8d | 1.3221 | -60.0272 | 2025-01-23 03:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.4 |
| b535636f-5c11-312d-b022-cbd16ec725ec | -26.00441 | -51.33033 | 2025-01-23 03:40:00 | NOAA-20 | CRUZ MACHADO | PARANÁ | Brasil | 4106803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 85f8289a-4366-3402-8744-fb2bc2267c64 | -32.38697 | -52.39905 | 2025-01-23 03:42:00 | NOAA-20 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 73a56c32-c165-3250-b25f-c7ce4a67d0ae | -29.64965 | -54.20243 | 2025-01-23 03:42:00 | NOAA-20 | SÃO PEDRO DO SUL | RIO GRANDE DO SUL | Brasil | 4319406 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 19a6fdae-7952-3ece-8c71-7ff7c3e161a0 | -29.64322 | -54.19989 | 2025-01-23 03:42:00 | NOAA-20 | SÃO PEDRO DO SUL | RIO GRANDE DO SUL | Brasil | 4319406 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 875179bb-536f-3e76-aa9d-acda33811784 | -32.38578 | -52.40358 | 2025-01-23 03:42:00 | NOAA-20 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| c24f55cc-6227-3e09-8eef-920848c59984 | 1.3221 | -60.0463 | 2025-01-23 03:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 114.8 |
| cd23bbb3-d2f2-3101-89e4-e926b638c921 | 1.3403 | -60.0461 | 2025-01-23 03:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 9faaed85-6895-3f90-8bfe-0b612ec62a38 | 1.3221 | -60.0272 | 2025-01-23 03:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 73.3 |
| a7885b40-845d-3bfa-96ce-643c80cd3fbe | 1.3221 | -60.0463 | 2025-01-23 04:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 6e58a458-7b48-3d2d-a70b-fcf5898ed47f | 1.3403 | -60.0461 | 2025-01-23 04:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 740b1094-461b-381f-9f55-acb8021f24ed | 1.3221 | -60.0463 | 2025-01-23 04:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 40.5 |
| fefb26d0-7e66-310d-a246-4e2b7cce0dee | 1.3221 | -60.0463 | 2025-01-23 04:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 7330dc49-efab-3b75-910f-3ca2194e3164 | 1.3221 | -60.0272 | 2025-01-23 04:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.3 |
| a5f89599-a820-3942-9624-4430abdf1fb5 | -7.00981 | -34.99909 | 2025-01-23 04:23:00 | AQUA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 74.3 |
| 1c076e14-8da0-3630-8011-f9df03f1a5e7 | -7.00464 | -34.99286 | 2025-01-23 04:23:00 | AQUA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 58.8 |
| c70b7c20-1fce-3ed2-962a-a907122b6778 | -7.00193 | -35.01001 | 2025-01-23 04:23:00 | AQUA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 21.6 |
| e2b60036-c581-34f7-b2af-a77d52fc3397 | -5.36153 | -45.17382 | 2025-01-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98b02891-ba33-3fdf-9c0a-0b47a8647992 | -3.40636 | -47.14275 | 2025-01-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c1443579-b3e5-34e1-a9d5-9f6fe25a4d3a | -4.32724 | -39.15574 | 2025-01-23 04:25:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ecfd8968-e507-3bd6-86ef-8c318d020e36 | -1.95851 | -54.74244 | 2025-01-23 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6bb95e88-c656-33d9-90f3-b1ff3f102fd5 | -6.04019 | -46.25687 | 2025-01-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 547c4964-5f3a-3691-90ba-1eb5fdad9590 | -5.2075 | -43.30186 | 2025-01-23 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab286d1c-f8c7-3b62-9277-740478085c26 | -6.09307 | -46.67865 | 2025-01-23 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f1c355ed-2d19-342c-8590-ee1429388e36 | -6.66158 | -47.603 | 2025-01-23 04:25:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d820fd9d-2682-3ba4-afa3-fb918885ad29 | -3.13793 | -40.04697 | 2025-01-23 04:25:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 89ea545d-0d28-3f5a-8ab8-58e6b1edc2ff | -3.13324 | -40.05006 | 2025-01-23 04:25:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 34ab21ca-c393-34c7-9acd-32eced34e9da | -6.6588 | -47.59889 | 2025-01-23 04:25:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9fb0022-0e36-3680-a4ad-702b9ba92fec | -1.68282 | -45.78503 | 2025-01-23 04:25:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c35b6576-ba6e-30d9-ae8a-40c4463b00f5 | -6.661 | -47.60657 | 2025-01-23 04:25:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f0b0c81-ed98-3c56-9206-855f1206e743 | -5.21803 | -43.30355 | 2025-01-23 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70aa2de2-a143-3167-8a15-a4efee4b1331 | -5.54207 | -45.78683 | 2025-01-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e4fdcdf-2a8d-3f25-92b2-d73579e82cb0 | -7.96832 | -35.239 | 2025-01-23 04:25:00 | NOAA-21 | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 99505076-7fc5-39e0-a7e9-779e4294058e | -6.85146 | -47.84276 | 2025-01-23 04:25:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a69d0f72-fb3a-3a10-abe6-a6d15e9c7302 | -5.85917 | -46.41497 | 2025-01-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 542b36d6-8fa7-37b2-848a-24f338790b97 | -5.40229 | -45.15208 | 2025-01-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README3.md)
