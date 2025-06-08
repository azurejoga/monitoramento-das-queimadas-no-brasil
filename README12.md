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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72ee91c3-e2fb-341d-9257-6613952af7a5 | -21.38787 | -48.64024 | 2025-06-08 04:27:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f07de66-ccd1-3dd5-b86d-6519131b9ebe | -20.66078 | -50.10628 | 2025-06-08 04:27:00 | NOAA-20 | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d859fe64-d2c5-3ee7-900a-1f5c5d8c09f5 | -16.06769 | -43.65601 | 2025-06-08 04:27:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d588d28-3f76-3eab-8d7d-c06e08bfce59 | -14.88606 | -48.11729 | 2025-06-08 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 36b7c577-24a4-30d4-a411-4fe57bafe770 | -19.93011 | -47.26635 | 2025-06-08 04:27:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de6b68de-8394-3566-bfe6-45c7b1c7e39e | -16.63883 | -49.44231 | 2025-06-08 04:27:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 43cb1592-5a40-38cc-b7bd-2386bd241b11 | -13.46957 | -56.85872 | 2025-06-08 04:27:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 073e07ac-bdb0-3450-8186-3d2710639438 | -13.47177 | -56.85287 | 2025-06-08 04:27:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1899d06d-3b70-3493-a5e3-9064e34105c6 | -13.88215 | -56.20888 | 2025-06-08 04:27:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf9211f3-e545-391f-be32-33b4334dd132 | -15.07775 | -48.9436 | 2025-06-08 04:27:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 19977fef-b414-3c5a-946f-e58a479b1def | -17.75335 | -42.89306 | 2025-06-08 04:27:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d33822e-9bf7-31a3-a99e-a621e9be9095 | -20.99409 | -51.79327 | 2025-06-08 04:27:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 697173b6-aa5b-3ec7-9e27-349e53d6ac4d | -15.52211 | -42.62449 | 2025-06-08 04:27:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 648aef53-d870-3155-a1d7-4a5a5614134b | -15.4966 | -44.41117 | 2025-06-08 04:27:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7d5db4c9-3f74-3ead-8df3-93e16e4dc824 | -30.15018 | -52.02325 | 2025-06-08 04:32:00 | NOAA-20 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 56e66799-cb66-3e43-b1c6-9a93fea82610 | -4.59966 | -38.51854 | 2025-06-08 04:36:00 | AQUA_M-M | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 37.8 |
| b51187ec-a4cf-3d1b-bb44-66cdf6bbb99b | -4.60884 | -38.51225 | 2025-06-08 04:36:00 | AQUA_M-M | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 28.4 |
| 2a8ccd0c-1039-38f5-bc5d-c2737dc4b944 | -7.86617 | -47.89209 | 2025-06-08 05:16:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 95ff8fb0-6751-3080-aaf0-fedabdc2d812 | -3.88304 | -54.21383 | 2025-06-08 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b063c8eb-6238-334c-b599-c76552968824 | -6.8797 | -47.23802 | 2025-06-08 05:16:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6c9cf23f-6760-3a56-893a-efaf37fc1d8f | -6.44855 | -45.73202 | 2025-06-08 05:16:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 875c7cb4-8aa5-3402-ab8b-5fd243bb63c5 | -5.57722 | -45.20647 | 2025-06-08 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e278e7b6-be2e-3764-b081-d6e1748cd800 | -2.95409 | -60.01614 | 2025-06-08 05:16:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f71e155b-e884-3d94-9577-fe214913c09b | -3.04895 | -49.43719 | 2025-06-08 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c8b856f-3743-351c-857b-233a7a970878 | -7.87237 | -47.89299 | 2025-06-08 05:16:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7e6657f-13d8-3e6e-b984-c74aac41ce6d | -6.44867 | -45.72984 | 2025-06-08 05:16:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bf1b7a71-e508-3565-8d64-968edc6d4c86 | -6.31732 | -48.47813 | 2025-06-08 05:16:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 045e2f2c-a7e6-36ae-851a-351be15d0f29 | -6.44941 | -45.72562 | 2025-06-08 05:16:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf941f8b-8022-3f1a-9182-a63a7bb39886 | -3.25817 | -47.53907 | 2025-06-08 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6de0a42d-e4ab-3733-882c-2065bc1bacd1 | -3.04942 | -49.43399 | 2025-06-08 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fca92c34-bb0b-3a9f-ac1e-31fdae583d29 | -7.87176 | -47.89774 | 2025-06-08 05:16:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aaf0493d-2e29-3e43-bd19-626c036e89c5 | -6.87439 | -47.24796 | 2025-06-08 05:16:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4da78e28-50c3-3ebf-a1f8-82cbb2c5f2f4 | -6.31077 | -48.48248 | 2025-06-08 05:16:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 853d0f24-6d05-3f69-b527-6cda8bd56024 | -6.23825 | -48.53571 | 2025-06-08 05:16:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9830b0f-e6c7-397b-979b-30d8240b1069 | -3.0485 | -49.44031 | 2025-06-08 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be23613c-b19d-3e8f-a8d6-8f61ff990692 | -3.98693 | -48.41385 | 2025-06-08 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25b482a3-0ee6-3961-bbab-8c4ef786b44a | -6.24343 | -48.54115 | 2025-06-08 05:16:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9dfb47b8-0851-3d5f-9920-3d45c86f984e | -3.04327 | -49.43954 | 2025-06-08 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d0c1b6f-caeb-375b-a9c0-e0f03e383b7b | -6.87897 | -47.24332 | 2025-06-08 05:16:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| dada6aaa-880e-3ffa-8efb-257ccce0e67a | -7.86076 | -47.89173 | 2025-06-08 05:16:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d7117a9-e512-3e03-b9fc-a20a25456f01 | -2.91889 | -48.23565 | 2025-06-08 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e1cd969c-0c11-3120-9f6b-a6737fd583ec | -4.42085 | -47.66393 | 2025-06-08 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2a35c017-a652-343d-93ff-e4061dcc871a | -6.23761 | -48.54033 | 2025-06-08 05:16:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 925c9850-6b37-3071-9f7a-9b956fc90bbd | -6.4495 | -45.72341 | 2025-06-08 05:16:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0541acaa-99f6-351b-b958-7324c3d704ab | -6.88145 | -47.24348 | 2025-06-08 05:16:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 752abec4-8d92-307c-b072-acd054ba8066 | -6.24866 | -48.54617 | 2025-06-08 05:16:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d1b27ea-7248-3802-a3da-8513fdd2231c | -7.87115 | -47.9025 | 2025-06-08 05:16:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b55dce0f-4682-324f-9e73-ea744912da49 | -6.49883 | -47.49031 | 2025-06-08 05:16:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11ed3478-31d5-3d63-b6e3-798bc45625c4 | -3.25216 | -47.53859 | 2025-06-08 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41aeb890-57af-3ed9-9aff-307c7cff78e2 | -5.57485 | -45.20382 | 2025-06-08 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 65d0ce68-8e27-3109-a449-96fe76000b03 | -6.87507 | -47.24267 | 2025-06-08 05:16:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e5577a0-fc1c-35e1-95c1-77b05ec03153 | -7.86557 | -47.89685 | 2025-06-08 05:16:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8455fa3d-e9b7-3cf3-b9db-987ed9eebb0e | -7.86496 | -47.90162 | 2025-06-08 05:16:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c405df3e-cc68-3d24-bcf8-102b8ec2b519 | -6.49818 | -47.49537 | 2025-06-08 05:16:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7cc4b1b0-19af-33a4-bad6-7443c48e8a80 | -6.88213 | -47.23819 | 2025-06-08 05:16:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0608026b-f685-348b-80b9-f0e8da6b0f63 | -12.97097 | -46.75893 | 2025-06-08 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0e87da55-300c-38e3-914f-5eb082a74f58 | -9.91836 | -59.90919 | 2025-06-08 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3159118-8118-3a57-9741-820701a22135 | -9.40244 | -48.44513 | 2025-06-08 05:18:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b65e18a8-796d-3500-8c28-9bd95ebcace4 | -12.66273 | -58.2152 | 2025-06-08 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab8415c6-7f70-31d9-8295-ffa7c1961fdf | -11.12038 | -54.64303 | 2025-06-08 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ea115006-89d8-3bc1-947e-c44d9008f778 | -10.4971 | -53.66227 | 2025-06-08 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e758d103-3613-3def-8be5-048a3aa0baa1 | -11.12241 | -54.65853 | 2025-06-08 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76149b41-7d5c-36d5-93ea-b0aacc7567b3 | -12.37352 | -57.4016 | 2025-06-08 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c107d1f2-d426-3740-9d93-072bf4bbab20 | -10.39779 | -47.00248 | 2025-06-08 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| d0703409-60c6-3725-bbd6-0abf2fc8f73a | -11.25656 | -60.79286 | 2025-06-08 05:18:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5b008b3-cd73-352c-ba65-f14917d0de6a | -10.30069 | -57.13377 | 2025-06-08 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4392d2e9-2f0a-3285-a3b0-bd8049dbc43d | -12.53244 | -58.36055 | 2025-06-08 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97098b65-156e-3f14-8ee4-010bfe0af860 | -11.25381 | -60.78881 | 2025-06-08 05:18:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbd39d5d-3804-317c-809d-d447b1a03df3 | -10.94617 | -55.33375 | 2025-06-08 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dbaff227-6bc4-3fac-ba12-7288a79c7169 | -9.92809 | -48.69117 | 2025-06-08 05:18:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8be4c951-53db-3a7c-86b9-2d40ce44950b | -9.64439 | -65.73949 | 2025-06-08 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7472b1fe-0c66-314f-922a-9c5cda3f7fcd | -12.3765 | -57.40627 | 2025-06-08 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2186b9b1-23a6-314e-85ab-624145a8226d | -12.37709 | -57.40214 | 2025-06-08 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fc980268-c3e9-351a-9be5-9f997fc2d80c | -11.54823 | -56.44805 | 2025-06-08 05:18:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99cb5c63-b75d-3ae0-82dc-b950ddfa5224 | -11.38916 | -54.76794 | 2025-06-08 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43f6630d-3e29-3849-9445-2fb14ceaf860 | -12.36639 | -57.40051 | 2025-06-08 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 644329ae-2010-30e4-a653-685efb193a93 | -11.39275 | -54.77225 | 2025-06-08 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67f7b808-6324-3556-9f38-f86be7c169d1 | -9.0721 | -47.14325 | 2025-06-08 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccddbf6d-6bea-3c09-a8f0-2f9d620e1d4d | -8.77591 | -47.18564 | 2025-06-08 05:18:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3eeaeaa3-e569-39e8-885f-67e4572a0c2e | -12.66906 | -58.22011 | 2025-06-08 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5e240bd-6477-308b-acad-423c90fd8a1f | -13.37287 | -54.25159 | 2025-06-08 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ecca7926-87b5-3f4e-a6cc-c90d1f76e858 | -10.33826 | -57.49186 | 2025-06-08 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa62d3e5-992c-3f9e-b8a2-d669822c4d52 | -10.87899 | -54.30342 | 2025-06-08 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 759e3a81-0dc3-3a00-a779-df4efb7584a7 | -11.54696 | -56.45702 | 2025-06-08 05:18:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 51db4390-50cb-39dd-af27-db53b2801672 | -12.3658 | -57.40463 | 2025-06-08 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 109fac80-cfa7-3260-b65b-04cb1dc56ff5 | -11.12293 | -54.6548 | 2025-06-08 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c2ccf6e-c82e-3cd8-9b52-4cd7fb84c6eb | -12.37948 | -57.41093 | 2025-06-08 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 193a5444-6df2-3e60-bf15-a536f263d677 | -10.87952 | -54.29947 | 2025-06-08 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8de548b-9784-34ec-8f59-c9de09d5613e | -11.38864 | -54.77168 | 2025-06-08 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6621d80a-4ba7-36ed-8825-833428c06335 | -12.15926 | -57.73245 | 2025-06-08 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2297b062-6138-3d40-b99c-f5ac960af75c | -11.54017 | -56.45144 | 2025-06-08 05:18:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b392cf99-dcb0-3b35-9fc6-0acfc3354457 | -8.5295 | -50.02479 | 2025-06-08 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2bfe22db-daf6-3a68-bc51-4c27fed37af9 | -12.27295 | -55.0784 | 2025-06-08 05:18:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 890041e9-d5c1-38db-8fae-ecad49d31c83 | -12.37889 | -57.41504 | 2025-06-08 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 91dbdd51-905d-3feb-a858-a613e3ba3f20 | -12.96446 | -46.75291 | 2025-06-08 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cc36aef5-680b-3a8b-b314-33fcac72d423 | -9.64734 | -55.16498 | 2025-06-08 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b91bf88-b50d-34be-8b87-d5411bf9260f | -12.52102 | -58.3665 | 2025-06-08 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f85be17a-3a36-34a2-b8a8-f11a4040ef5f | -11.1188 | -54.65426 | 2025-06-08 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a4b9de0-3d6c-35cf-abb8-f95c567839f2 | -12.36937 | -57.40519 | 2025-06-08 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 489a648f-388c-35f4-86ba-d822df1733ba | -12.3663 | -57.40657 | 2025-06-08 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README13.md)
