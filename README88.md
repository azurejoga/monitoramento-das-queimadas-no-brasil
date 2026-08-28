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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9db5659-0d45-3ac9-ab08-77559a6cb08e | -11.2128 | -53.9976 | 2026-08-28 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 150.6 |
| f97b9957-faa8-3e55-af24-17088205e1d9 | -11.1639 | -45.5897 | 2026-08-28 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| c65cde84-2b42-380f-adac-14d5db66961b | -14.3372 | -51.7234 | 2026-08-28 16:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 45.0 |
| b9eab5e1-b3c9-3243-9f67-a7381ec691ba | -10.4981 | -64.5005 | 2026-08-28 16:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 51a58dba-b6c9-3a27-9b17-036219884922 | -8.3718 | -62.697 | 2026-08-28 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.9 |
| b829561f-c643-3a86-a7c6-cfc58bb20362 | -8.3717 | -62.716 | 2026-08-28 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 9233659f-1e1b-35b3-84f4-e1730dec9c8d | -11.1732 | -51.2304 | 2026-08-28 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 208ff6a4-8090-319e-91fa-f023bb4f6946 | -13.2472 | -51.3735 | 2026-08-28 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.8 |
| ee999a3c-c814-3873-9529-f0e7e45c3210 | -3.2901 | -61.5747 | 2026-08-28 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 0b4ef7ed-c5a2-3281-a368-c6bd6d22944d | -6.7833 | -59.4208 | 2026-08-28 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 4877cedc-13de-3d49-9e2d-ea249c277be9 | -6.137 | -53.5259 | 2026-08-28 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| bab33d73-fe66-362c-8774-471e658fa07d | -8.5964 | -54.8361 | 2026-08-28 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 3e98929a-9a02-3fd8-96a3-a702dad72bee | -6.695 | -58.7291 | 2026-08-28 16:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 8dc27060-198d-32f0-86f5-d7e4e8609b1a | -6.5607 | -56.5464 | 2026-08-28 16:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 366027e0-74f3-3429-a5d9-ff64ecab7689 | -4.903 | -56.279 | 2026-08-28 16:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| f090609a-5577-38d4-bc36-db1e2c30af05 | -10.8653 | -50.2203 | 2026-08-28 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 9c61915b-bed6-36c4-95d8-b41eaf21c9a7 | -12.2281 | -50.5578 | 2026-08-28 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 5f41a0e4-4771-3174-807f-cee4df10a613 | -12.209 | -50.5601 | 2026-08-28 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 8fa6ded1-2790-310f-9041-ed08d6c92553 | -6.1656 | -57.7988 | 2026-08-28 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 188.1 |
| c837b50d-fec0-3dad-b567-d9f92d4241d7 | -6.6913 | -56.3427 | 2026-08-28 16:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 9f39b5f1-b738-3840-8ba9-ff17f73cef08 | -6.5608 | -56.5266 | 2026-08-28 16:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 76b67c0e-57bd-3499-9a9e-812d0ccac3a0 | -6.8358 | -59.9379 | 2026-08-28 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 295.2 |
| da990486-f67f-3dfe-9b08-ad463f67571a | -9.2477 | -57.0697 | 2026-08-28 16:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 14c30756-c621-3829-aa8c-d3170abb78be | -14.2402 | -51.7576 | 2026-08-28 16:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 7a7737f4-54f5-359f-ab97-b5974e7f91cd | -10.498 | -64.5193 | 2026-08-28 16:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 74.4 |
| cfba3e9f-c10f-32b7-badc-8ceeeefb698d | -8.8184 | -49.6308 | 2026-08-28 16:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 9df8b97b-6b8c-313f-87a0-9852feb9ce00 | -10.5601 | -50.4022 | 2026-08-28 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 140dd6ec-4b57-3fa4-9bf5-f787e6c28685 | -10.8422 | -50.5219 | 2026-08-28 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 15e79dcd-b945-3853-b7bd-a33cff82fad2 | -8.8372 | -49.6291 | 2026-08-28 16:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 8f9d93bd-2a14-3d97-bc4f-703db88293a5 | -8.5779 | -54.8172 | 2026-08-28 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 344e8399-4967-349d-8145-0f95f684fe0e | -8.8187 | -49.6093 | 2026-08-28 16:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 9ab8403f-e823-3a8f-ae9d-38a5f9a76d70 | -6.7451 | -59.6533 | 2026-08-28 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 01fe3c2f-9df4-3cd0-9238-15f243457b84 | -8.6881 | -49.5353 | 2026-08-28 16:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| f2170c38-8d82-39cf-8fa8-dc09b6cebd29 | -8.5971 | -54.7553 | 2026-08-28 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| ad9b1102-05cd-30c2-a0c2-16b99595c33c | -9.2475 | -57.0894 | 2026-08-28 16:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 14689f39-16b1-362a-bbcb-d5df22113e31 | -8.3902 | -62.7152 | 2026-08-28 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 798c2b03-c072-33fe-8d5f-0e00f2b868f6 | -11.1922 | -51.2284 | 2026-08-28 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.7 |
| b3806822-2420-36d5-9e78-0519c2a893b0 | -8.0551 | -45.839 | 2026-08-28 16:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 178.1 |
| 8b2dc8b9-c38f-3023-a0dd-ce332b8644d4 | -10.8993 | -50.4945 | 2026-08-28 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 39.7 |
| c455b6ec-4c21-3c4a-8997-2c170c796900 | -12.3041 | -50.5701 | 2026-08-28 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 207.8 |
| c2792aec-1e4f-3d03-9e91-36f93d2b0ac3 | -10.8801 | -50.5179 | 2026-08-28 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 6edb03b3-d7c8-3563-a095-74419546f60e | -8.5777 | -54.8373 | 2026-08-28 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| a20772d2-b617-3668-b5dd-55e10ea2e47e | -21.38464 | -44.62061 | 2026-08-28 16:03:00 | NOAA-20 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f1c41d28-6603-35e3-829f-ae772fabeb66 | -23.5421 | -47.30719 | 2026-08-28 16:03:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 320b48f9-e928-370b-b0f2-6d152c78d187 | -23.54428 | -47.30776 | 2026-08-28 16:03:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 28bd9520-7dea-33bf-b9fa-1b0fe8b898dd | -20.46966 | -48.79115 | 2026-08-28 16:03:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 23b95961-94c3-3b68-8fc1-d616e88e6086 | -20.46914 | -48.78438 | 2026-08-28 16:03:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 060e97b1-7bb0-33f9-bbcd-4a0fd7f9737e | -21.4554 | -45.77066 | 2026-08-28 16:03:00 | NOAA-20 | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| bd190f8e-ad95-3282-a4a7-08f4e57819a0 | -21.32471 | -45.93047 | 2026-08-28 16:03:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 79ffcd98-8289-3f96-8121-a2ee085c0c2f | -23.53776 | -47.30947 | 2026-08-28 16:03:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 61784484-6051-3013-b34e-63b55cb9eebe | -21.32177 | -45.9325 | 2026-08-28 16:03:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 8938f550-572c-3db9-b41f-b946ee1f0e74 | -19.84976 | -43.9744 | 2026-08-28 16:03:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd213939-811d-36ca-a37b-0e3568519df5 | -18.9921 | -40.73039 | 2026-08-28 16:03:00 | NOAA-20 | ÁGUIA BRANCA | ESPÍRITO SANTO | Brasil | 3200136 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 2585e304-007c-3895-9965-1af218cfde01 | -21.106 | -46.24783 | 2026-08-28 16:03:00 | NOAA-20 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 91635dc9-3cb7-3ce1-b679-699d6dc4dd49 | -23.54252 | -47.31345 | 2026-08-28 16:03:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 6c43ee14-a464-3592-9286-bfb049444f94 | -8.67037 | -49.54638 | 2026-08-28 16:05:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| a074e0c9-0008-3c0e-b657-4f59d9aeacbf | -13.65195 | -47.73893 | 2026-08-28 16:05:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e9ba862f-cb32-3677-95eb-3e89d066ba89 | -12.39206 | -48.20863 | 2026-08-28 16:05:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ba2aeab9-ef90-3936-9496-a0f4d3c888ff | -17.07199 | -47.18586 | 2026-08-28 16:05:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 21.4 |
| dd28ca9c-3569-3fe4-b3a7-2ac0f5305250 | -7.09298 | -42.2132 | 2026-08-28 16:05:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 6e70a518-10e2-3039-aba6-0ece21f0b754 | -9.51056 | -48.02732 | 2026-08-28 16:05:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 7528844e-3e84-3c0c-be99-410b70bbf423 | -7.98904 | -45.50236 | 2026-08-28 16:05:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 380d356c-4a33-38ae-a8c2-041022799810 | -5.58656 | -42.72583 | 2026-08-28 16:05:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 17.1 |
| f12a6b66-e764-3fca-91c1-c92c31182e6e | -5.95316 | -44.80645 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2f21396d-5d55-38a0-ac07-68691aa803db | -6.90238 | -43.65191 | 2026-08-28 16:05:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 3d171cdf-993e-3f36-b6af-5bfffbd2d624 | -17.07805 | -41.05956 | 2026-08-28 16:05:00 | NOAA-20 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 0474b5f5-5aeb-3ee7-b755-8b0d76fcb0ad | -13.28426 | -40.3427 | 2026-08-28 16:05:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| a3c6b816-6d09-3180-b7d1-4fe1c4cdde87 | -7.61261 | -45.83483 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f568cf5f-dbcb-32e2-a561-956cef7d20a9 | -14.21842 | -45.30818 | 2026-08-28 16:05:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ffc84a5e-6bde-34a5-8731-46a731c4517f | -13.04432 | -40.22638 | 2026-08-28 16:05:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 9e766b4e-cccd-394a-b958-410b9944771c | -8.28741 | -40.86976 | 2026-08-28 16:05:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 37d0ff74-b057-3ab1-8fb1-31dc8b60a8e8 | -9.48788 | -45.63139 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7d090864-4327-35a6-9777-853847e74f20 | -14.18911 | -41.24279 | 2026-08-28 16:05:00 | NOAA-20 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f0222a34-1103-3143-b5b2-b258d64eae8f | -13.58774 | -45.77721 | 2026-08-28 16:05:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 44dff8f3-53c0-3039-98d7-04a934490cce | -12.39097 | -48.19884 | 2026-08-28 16:05:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| e24ed538-3b26-32ab-b369-f5a934770d41 | -15.09514 | -39.70634 | 2026-08-28 16:05:00 | NOAA-20 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 147ce9a5-71a5-38be-8b70-77987d0ab07b | -6.56696 | -45.32584 | 2026-08-28 16:05:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 9e94ebd4-61d4-38ce-894c-5df829e12bd3 | -7.62172 | -44.8233 | 2026-08-28 16:05:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1ed39b75-3ef8-3e52-8f7b-afe6cb6d71c8 | -6.83879 | -42.85568 | 2026-08-28 16:05:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| b6792d07-e871-35d1-a8ed-e4fed1dec216 | -14.18752 | -41.24337 | 2026-08-28 16:05:00 | NOAA-20 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 723e6748-9786-37ca-9e6a-0e3996aa08b4 | -8.06305 | -45.84674 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2c3f5db9-2dbe-3238-8403-b0eea0996e91 | -8.78124 | -50.05921 | 2026-08-28 16:05:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| b9ec3593-a8a3-3f8c-bc5f-0f94987e0a34 | -8.96205 | -45.74127 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 1ef3c4bc-240d-3fb2-9ee0-77a812a3acd4 | -12.14472 | -39.07677 | 2026-08-28 16:05:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 14ca4142-77a8-3e29-9ce4-4ea9d84a5e62 | -12.78617 | -45.94664 | 2026-08-28 16:05:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 8fe392f0-06b9-3f4c-a8ba-81a989f73422 | -6.56226 | -45.32662 | 2026-08-28 16:05:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| d03923c2-38ab-3a87-8803-b90798bfc25d | -5.95939 | -44.80315 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 1694c831-3ec3-33c7-9e96-2e5142183ec1 | -13.35189 | -46.90536 | 2026-08-28 16:05:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6159bc32-540a-3cc7-b7b4-74c24f52e730 | -7.0815 | -42.80221 | 2026-08-28 16:05:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 89a70c8a-3066-33ac-8c84-9d0719480366 | -6.84782 | -42.86155 | 2026-08-28 16:05:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f1df7a66-5bdf-3bb5-969a-f605fdf10ed4 | -12.38679 | -48.21053 | 2026-08-28 16:05:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 48677814-70aa-31de-b63e-cc0b527a5086 | -7.19697 | -42.7388 | 2026-08-28 16:05:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 5c8d3c61-6c44-3d3a-b99b-6decc4cc7858 | -14.30239 | -42.13019 | 2026-08-28 16:05:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 16380dae-ff85-3480-96c4-ea000c65a9da | -6.5635 | -45.324 | 2026-08-28 16:05:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 14f9d448-16f6-3122-9de4-57512d258168 | -6.55949 | -45.3298 | 2026-08-28 16:05:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 8b934e62-8884-3976-9ef8-0ef8e2b89e95 | -7.21139 | -42.7543 | 2026-08-28 16:05:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 762c059d-4318-3281-98c3-1036d3656140 | -12.26318 | -45.06761 | 2026-08-28 16:05:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61de7850-2e4e-31fb-bee8-441ef538cd81 | -6.90553 | -43.64364 | 2026-08-28 16:05:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 493f5ae6-3b34-3e2c-a702-dbd4b59be68d | -14.22714 | -45.24678 | 2026-08-28 16:05:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fc5fba02-6981-31e4-9051-d2beb7732ce4 | -8.08222 | -45.83788 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |


[Clique aqui para ver as próximas entradas](README89.md)
