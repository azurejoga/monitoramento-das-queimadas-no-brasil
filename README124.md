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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5373a2c1-0ea9-3933-bd4d-b44ac80131f6 | -13.2801 | -51.7099 | 2025-09-13 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 7368d9f4-b332-3c61-8b85-7b4388e07dbb | -11.7826 | -47.402 | 2025-09-13 12:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 296ab085-64d6-36d2-a68b-c43f16c86c61 | -15.1363 | -52.4679 | 2025-09-13 12:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 509fd40c-81ac-390e-9b94-d43962c291fa | -15.4517 | -47.3291 | 2025-09-13 12:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 126.5 |
| e0541b48-68dd-39b7-a17b-d75de035ad22 | -13.2609 | -51.7122 | 2025-09-13 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 92121c0a-0383-3067-babb-06707de96ac9 | -12.5979 | -45.7021 | 2025-09-13 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 382bd8ed-1d41-3031-9106-3cf243a51e50 | -13.9168 | -48.2998 | 2025-09-13 12:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 58.5 |
| b54c7444-617e-35ec-ad28-b47bc5ee0de8 | -11.1066 | -51.9538 | 2025-09-13 12:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 789e071c-3ff6-3661-aa93-a3e51b6fbb1a | -14.1698 | -46.2735 | 2025-09-13 12:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 116.1 |
| bef985cb-5733-3f81-bba7-c0e3e204feab | -14.4204 | -47.3011 | 2025-09-13 12:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 181.6 |
| f19e15f4-9c5b-3a63-b34f-fd5ac35b9f91 | -10.9283 | -47.2223 | 2025-09-13 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 7f41f93f-3037-38fe-ac0c-33a268dad451 | -12.1044 | -47.5816 | 2025-09-13 12:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| cbf3feb9-9989-37e2-853a-6a5baf9fc6f0 | -18.0065 | -46.9499 | 2025-09-13 12:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 124.3 |
| ddb15cd6-48ea-35ae-b9e2-a48c6f44c6d3 | -12.9398 | -48.0213 | 2025-09-13 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 60dc042b-4786-32ea-aeaa-a49c0f30a6e2 | -12.5791 | -45.6821 | 2025-09-13 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 1c0ac9b5-8fde-354a-92ae-bc27c7d9ac0d | -15.0436 | -50.1337 | 2025-09-13 12:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 2e9a0824-ba06-3774-ac07-4975568c7c19 | -14.29 | -46.0924 | 2025-09-13 12:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 211.8 |
| d9071c0e-7471-34af-9b1d-6ae0ac2f8306 | -15.1359 | -52.4892 | 2025-09-13 12:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 164.4 |
| b1dcec08-078d-3adf-ab97-717e86250eb4 | -9.2656 | -59.4191 | 2025-09-13 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| c71387c2-0332-3901-8697-ca4c03f58b3c | -12.1236 | -47.579 | 2025-09-13 12:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 2d55170e-fb6f-3d5c-bede-7086215da0f4 | -8.4967 | -45.1597 | 2025-09-13 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 114.4 |
| b0ea8e51-63a5-3634-a035-087fe978e4fe | -15.4713 | -47.3256 | 2025-09-13 12:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 59aaf3d9-ef57-34a5-af20-ae1880f4233a | -12.9402 | -47.9991 | 2025-09-13 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| a3fed96d-3898-3c65-ba38-66b4bb6d3320 | -17.4142 | -49.2519 | 2025-09-13 12:40:00 | GOES-19 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 9af69742-7a63-3db1-9a41-9041dd4d0f0d | -16.0791 | -50.0151 | 2025-09-13 12:40:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 93.6 |
| eb1a5378-d07c-3479-8e9b-40cd4128025c | -12.5787 | -45.7051 | 2025-09-13 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 176.5 |
| bb1b8dfb-ac0c-3dbc-9aa0-5a9c3e6e3f4c | -11.8698 | -46.7627 | 2025-09-13 12:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 3731dc37-59b4-33cc-87f5-d44a3f804c4c | -12.8452 | -47.9459 | 2025-09-13 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 61846fe7-3d30-3265-a8f2-bb2339b0508b | -14.2088 | -46.2669 | 2025-09-13 12:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 128.4 |
| c6572d6b-087e-3940-9aa2-887aa0b10dda | -7.4322 | -44.4194 | 2025-09-13 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 34bef8c8-14d7-3021-8571-64949cc502a9 | -8.497 | -45.1369 | 2025-09-13 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 203.0 |
| d2ea9bde-c456-32f3-936d-fc4e52d93be9 | -14.4398 | -47.2979 | 2025-09-13 12:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 254.0 |
| f6c33ab5-b320-3de0-adbd-bd833277c2f3 | -9.2658 | -59.3997 | 2025-09-13 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 937019f9-6c20-371a-bb2f-e3184bacd744 | -11.1259 | -51.9309 | 2025-09-13 12:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| d3a19bb9-b1da-37df-92dc-b6a8540c8017 | -13.2222 | -51.7382 | 2025-09-13 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 114.9 |
| e4a7bfc9-8081-3102-b535-b80f0e62a1a2 | -16.0796 | -49.993 | 2025-09-13 12:40:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 80057e2f-fa09-3733-b3bc-f8117c2f1a63 | -13.9185 | -48.2105 | 2025-09-13 12:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 90.0 |
| a3f63737-80d7-3b51-b405-72f745e05ba4 | -12.8456 | -47.9236 | 2025-09-13 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 181.2 |
| 20026e77-7796-3c23-89b6-b0f6d284cf08 | -14.1694 | -46.2965 | 2025-09-13 12:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 186.3 |
| 8151a7c0-6d5f-3f41-b384-efb8d9e94bd9 | -10.9286 | -47.2 | 2025-09-13 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| cbf9f887-9277-3539-96d0-2cc4371faad6 | -15.1554 | -52.4865 | 2025-09-13 12:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 9efd8b23-5bb8-3ad4-89e1-7c730070fd26 | -12.8259 | -47.9486 | 2025-09-13 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| c3ba216a-99f8-3cc5-bbc4-909bfe8b2cf8 | -13.8979 | -48.2804 | 2025-09-13 12:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| d6387f85-8709-3c22-bf6b-bbb998896534 | -14.4394 | -47.3206 | 2025-09-13 12:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 205.8 |
| b16ab860-fcd4-3f73-b7da-b24b9f75c47f | -11.1898 | -51.3978 | 2025-09-13 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 2580fd4b-958f-3b92-a8f5-8007156fb478 | -16.3422 | -51.5217 | 2025-09-13 12:40:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 2f9440e7-88c5-3d21-8de4-8cc2190f5b0c | -19.6462 | -45.0859 | 2025-09-13 12:40:00 | GOES-19 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 93.1 |
| e602de69-13d0-3316-b771-630d420ae7d5 | -18.0041 | -48.6451 | 2025-09-13 12:40:00 | GOES-19 | MARZAGÃO | GOIÁS | Brasil | 5212907 | 52 | 33 | nan | nan | nan | Cerrado | 84.1 |
| b2ddeb07-83f1-363a-8fad-f3fb80e892b2 | -15.155 | -52.5078 | 2025-09-13 12:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 784ebdbd-6ead-3478-a6db-3dea47a32728 | -9.5004 | -55.9788 | 2025-09-13 12:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 110.8 |
| ecbaa37d-0ecd-33be-8e57-cbed7844b69c | -11.4119 | -50.4383 | 2025-09-13 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 117.0 |
| ba184ce4-a86e-3e69-b074-8345a05c459c | -15.8648 | -47.2322 | 2025-09-13 12:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 35cba5ca-4c61-3abf-b02d-d0ed2fbc2f7d | -11.1152 | -51.3211 | 2025-09-13 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 8157f750-9c5f-393e-8115-b6f5432f1996 | -11.1149 | -51.3423 | 2025-09-13 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.1 |
| bbc15109-370d-3b07-85a9-87befe4223f4 | -13.203 | -51.7406 | 2025-09-13 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 2d6ef5db-b9b1-3ade-ad43-15c1ca0ec3ae | -8.5159 | -45.1349 | 2025-09-13 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 185.8 |
| 4caddbcb-4040-33ad-ba93-7a5dc09465cb | -11.1896 | -51.419 | 2025-09-13 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 160.8 |
| f4e277ec-f08f-3896-a0ee-93049209c3cb | -16.0595 | -50.0183 | 2025-09-13 12:40:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 0ae13dcf-1980-38eb-b761-d75835161c39 | -16.4906 | -55.1276 | 2025-09-13 12:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| f727f759-24fc-37b6-8c76-babdac1192d1 | -12.8263 | -47.9263 | 2025-09-13 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 144ace75-77a4-34f3-a151-10d675a1d45e | -21.3715 | -51.1655 | 2025-09-13 12:40:00 | GOES-19 | LAVÍNIA | SÃO PAULO | Brasil | 3526506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.9 |
| fd40cbf5-11e0-3356-bcb6-981ee99c599e | -14.1893 | -46.2702 | 2025-09-13 12:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 238.7 |
| 2b7429b0-9e31-3c07-ba29-719e8e56d7d5 | -14.4199 | -47.3238 | 2025-09-13 12:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 214ad89e-f892-339e-86a2-98c1eababde8 | -16.0595 | -50.0183 | 2025-09-13 12:50:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 217.9 |
| 6a902606-3a91-306f-8539-d85d1161f4e3 | -14.4199 | -47.3238 | 2025-09-13 12:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 94.0 |
| cf62b989-6c93-3a57-b3f2-b4358dba37d7 | -15.4713 | -47.3256 | 2025-09-13 12:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 18f9bb94-65b1-3308-8f88-22bce785f94e | -12.8456 | -47.9236 | 2025-09-13 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 195.4 |
| c6519971-8940-3878-9525-6e4b632f10c7 | -12.8259 | -47.9486 | 2025-09-13 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 4dc55834-9ad4-3a36-850d-f31ffab775e2 | -10.8972 | -45.58 | 2025-09-13 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| d0b26a71-a7eb-3979-a8b2-5a934ba6d54d | -8.4967 | -45.1597 | 2025-09-13 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 4a0245ec-a84a-351e-9877-95fd250c5954 | -14.1694 | -46.2965 | 2025-09-13 12:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 7d4aef32-cf2a-33a3-a71b-9a29f95180ce | -9.5006 | -55.9588 | 2025-09-13 12:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 113.4 |
| df42176c-dd67-30a2-aae6-89e361f890e9 | -15.0436 | -50.1337 | 2025-09-13 12:50:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 97.0 |
| cba0f634-462e-3e1d-abe8-073ad359d052 | -18.0065 | -46.9499 | 2025-09-13 12:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 7635e80c-c3e9-32b2-9be9-d2432ed304aa | -10.8976 | -45.5572 | 2025-09-13 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 178.8 |
| 79e63d8f-89c8-30aa-a48a-20d0259d77d4 | -13.2341 | -43.7554 | 2025-09-13 12:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| a16e4de5-dce0-3c72-a968-832f1a6a95cd | -14.1698 | -46.2735 | 2025-09-13 12:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 1895ed75-1768-375a-bdd0-54e35c440850 | -11.8853 | -50.5554 | 2025-09-13 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 6eaf8048-5595-3b19-aada-9bb2faa59e4e | -15.0863 | -48.0016 | 2025-09-13 12:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 038d58af-13fd-31c5-b5a3-75bf4190c6dd | -12.9591 | -48.0186 | 2025-09-13 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| c4adeea3-6608-3203-9045-47d36f4a7f4f | -17.4142 | -49.2519 | 2025-09-13 12:50:00 | GOES-19 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 42ec69aa-ca62-314e-a545-89db65959ebe | -12.8263 | -47.9263 | 2025-09-13 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 169.2 |
| cc5b1ba8-2e1d-348e-bceb-fa1da660ec2d | -15.8845 | -47.2286 | 2025-09-13 12:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 146.5 |
| afeb0a8f-0925-3253-b2b0-4010337a0605 | -15.1363 | -52.4679 | 2025-09-13 12:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 84.3 |
| f9ae0197-1a8c-399e-9634-4985dc29ee8b | -13.2801 | -51.7099 | 2025-09-13 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 7c440e4f-374e-3684-b79e-3463af858829 | -10.6575 | -46.292 | 2025-09-13 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 239d65af-1eee-3702-b923-b889b348def5 | -15.8648 | -47.2322 | 2025-09-13 12:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 172.2 |
| e4d12759-0f76-3aee-b1d7-4724b099d26d | -15.1359 | -52.4892 | 2025-09-13 12:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 4028a1ca-ec30-36e9-85a2-2604de56179c | -13.2609 | -51.7122 | 2025-09-13 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 6a25b2c4-de70-3934-9a94-1cdcf96a28d6 | -12.1236 | -47.579 | 2025-09-13 12:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| d33c9e58-6b1e-360a-ab2c-8da1f1e44521 | -15.1244 | -48.0401 | 2025-09-13 12:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 251afeca-55a0-3ade-b530-9e021dfe0f67 | -15.4517 | -47.3291 | 2025-09-13 12:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 58bda04e-f06a-3bb4-bfb0-eb0eb434cffe | -19.3417 | -45.1132 | 2025-09-13 12:50:00 | GOES-19 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 165.8 |
| b1621c70-ca02-3c9f-b32a-6e32118fc511 | -17.292 | -46.0996 | 2025-09-13 12:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 102.7 |
| c65808ac-b345-39ed-b453-9ff82fb4976c | -16.0796 | -49.993 | 2025-09-13 12:50:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 1ad13c24-fedf-3bdd-9bfc-c2d0d86b4172 | -12.9398 | -48.0213 | 2025-09-13 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| e4b8c53e-42e5-37c8-a971-8e9b7afab567 | -15.8643 | -47.2551 | 2025-09-13 12:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 95.4 |
| ef28e7a1-eb4b-3dff-a426-f435fb22f46b | -15.1554 | -52.4865 | 2025-09-13 12:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 183.9 |
| d32cc4db-2a83-38cc-8f0e-d89e20ccc5f4 | -12.1044 | -47.5816 | 2025-09-13 12:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 6ba3ac03-4702-3118-b8fb-3d480cd51a6f | -10.8785 | -45.5597 | 2025-09-13 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 173.3 |


[Clique aqui para ver as próximas entradas](README125.md)
