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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0bf3810-adc6-30e3-bb35-b2975e839bac | -8.4296 | -54.7262 | 2026-09-20 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| dc5f64f8-b455-39d9-8c42-a931e46af2ea | -6.1109 | -57.684 | 2026-09-20 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| c47416bf-6754-3732-8c6e-837049484724 | -11.1225 | -49.4601 | 2026-09-20 16:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 127.3 |
| cb09691c-995e-38da-84d4-6846dc319f6c | -3.6632 | -58.8643 | 2026-09-20 16:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 78ac7812-667e-3479-9e68-8baf63b05164 | -6.6332 | -45.4244 | 2026-09-20 16:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 5adb406a-7123-3ce4-8d18-71726acc1239 | -1.5858 | -54.4552 | 2026-09-20 16:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 12a105ff-c58b-3b92-b19b-26c3a4a02ddb | -10.2793 | -50.2177 | 2026-09-20 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 868bd4de-9c2c-351a-9671-a8a343e86de0 | -11.0048 | -49.7325 | 2026-09-20 16:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 5213f2f8-a0cb-3c2b-8790-9e3bf7ab9d5a | -8.1688 | -54.7432 | 2026-09-20 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 135.3 |
| adf91341-87f3-3072-89e2-ce0f9be3e06a | -10.2748 | -50.5592 | 2026-09-20 16:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| bbfb28aa-be4f-3ba1-b3e8-6aca43f04f3f | -3.6398 | -60.5656 | 2026-09-20 16:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 134d6328-ec0e-3e1b-9ee9-fbd3caa296f4 | -10.8282 | -50.1601 | 2026-09-20 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 189.5 |
| 78da052d-b15d-3199-ae10-c8aa438f844e | -1.2082 | -49.2539 | 2026-09-20 16:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 50191056-5f68-3b7f-bd18-658a29de189e | -6.0928 | -57.6262 | 2026-09-20 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 908ab5fd-201d-3f8b-8ba4-9cdba80ee72d | -10.2787 | -50.2605 | 2026-09-20 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| ee6ab1c7-48f1-3d66-96c7-5002eafe7c4a | -2.8962 | -58.2825 | 2026-09-20 16:10:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| aafe5567-6ece-3429-be6e-07231de6f3f1 | -3.2955 | -59.4476 | 2026-09-20 16:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 90.2 |
| c4bddee9-1503-32eb-810e-bf7e6b95d910 | -6.8411 | -58.9939 | 2026-09-20 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 1a24a9dd-2e9b-3642-b523-8d154dd31341 | -10.8656 | -50.1989 | 2026-09-20 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 141.1 |
| c03e2c4b-d87c-39c9-a99e-8c67a67bfc92 | -2.8975 | -57.7793 | 2026-09-20 16:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 31c5d792-1403-3cf6-9b63-941470b8b965 | 1.1503 | -51.0188 | 2026-09-20 16:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 09a1a551-e753-311b-bc2d-e37d96abc5f0 | -6.1113 | -57.6255 | 2026-09-20 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| d083f4c1-0fe8-3562-9094-e4e6b15decf9 | -1.5858 | -54.4353 | 2026-09-20 16:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 3ab98051-a1cd-3d37-8b13-9eeb864e019d | -6.5829 | -58.9851 | 2026-09-20 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 0ff0cf33-da0d-32f8-b486-f79ce7fa8c9c | -9.0239 | -48.1622 | 2026-09-20 16:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| c5a16971-af2d-3b6e-90d6-e3bff0ca8626 | -3.0901 | -61.1816 | 2026-09-20 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| fce79dd7-3f37-3758-b31a-fc73edbe8414 | -3.1079 | -61.408 | 2026-09-20 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 9a99976b-9b24-3445-988c-d9df3e7657c8 | -11.44 | -45.34 | 2026-09-20 16:15:00 | MSG-03 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4aca1c54-d484-3514-8174-4ccef58f8b07 | -7.3 | -46.75 | 2026-09-20 16:15:00 | MSG-03 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 64e40471-b4b3-3dfb-b3e7-0e3520423102 | -11.04 | -54.9 | 2026-09-20 16:15:00 | MSG-03 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 293a46ea-839a-31f0-8452-5d180983a012 | -6.92 | -42.94 | 2026-09-20 16:15:00 | MSG-03 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9acb69f8-e11a-3cb2-8125-0bd108258aa4 | -8.77 | -44.23 | 2026-09-20 16:15:00 | MSG-03 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1d024872-fef4-3cf0-b01b-efce7f50f1b9 | -10.38 | -50.29 | 2026-09-20 16:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c4fcc0d5-8a6b-3e0f-9d26-6412387455f4 | -14.1 | -52.11 | 2026-09-20 16:15:00 | MSG-03 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c74fe4b6-0432-36b5-84c2-4049c53d2c0a | -8.77 | -44.28 | 2026-09-20 16:15:00 | MSG-03 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 264d9221-e0ba-3460-ab1a-759e53814a5e | -10.75 | -50.79 | 2026-09-20 16:15:00 | MSG-03 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 33b3f17d-6308-34bd-9158-4fc393eb43f3 | -6.57 | -44.88 | 2026-09-20 16:15:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e6d94c7-7cfc-33c1-9c57-33cefa6ce4ec | -6.9 | -43.69 | 2026-09-20 16:15:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7982c340-3033-3b56-af87-c784613c7656 | -8.8 | -44.28 | 2026-09-20 16:15:00 | MSG-03 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 68659b2a-2262-330e-87c2-e4d05e03eac0 | -10.65 | -50.65 | 2026-09-20 16:15:00 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6e75e9ff-f6df-39ab-89e9-252d3ad6829b | -6.92 | -42.89 | 2026-09-20 16:15:00 | MSG-03 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6df55293-ff31-386c-98f3-28a1f8e9d3dc | -6.93 | -43.74 | 2026-09-20 16:15:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4907de58-db4d-37ba-a084-718ee56b5f79 | -10.68 | -50.66 | 2026-09-20 16:15:00 | MSG-03 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c44ff301-8148-36e2-a7fd-4a7329aa2f32 | -10.89 | -53.95 | 2026-09-20 16:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d2da3ede-b76c-321f-912f-9a41b33b689e | -10.35 | -50.17 | 2026-09-20 16:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6b504e54-7461-3eff-8a6a-9ea7ff8b1f17 | -10.35 | -50.23 | 2026-09-20 16:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb943ae4-986c-34c7-87d2-105280d7badf | -11.07 | -54.91 | 2026-09-20 16:15:00 | MSG-03 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3f7fbf9c-9f19-3518-a7e5-ecc915fbae86 | -11.4 | -44.07 | 2026-09-20 16:15:00 | MSG-03 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 09eb31d6-d8c1-305e-97b0-e073896ce2b1 | -11.11 | -54.03 | 2026-09-20 16:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9a36a58f-94e8-3757-a4c0-f541e695c01c | -10.41 | -50.3 | 2026-09-20 16:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 80f5ffe3-597e-3cef-a36b-1640a20e16c6 | -11.5 | -45.4 | 2026-09-20 16:15:00 | MSG-03 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9160eb66-0412-33f6-ae83-728e357669c4 | -10.41 | -50.25 | 2026-09-20 16:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dab02f49-5d16-3768-801b-2abeae245865 | -9.86 | -48.4 | 2026-09-20 16:15:00 | MSG-03 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c223c132-f6c8-37df-acb4-d68eddb16ed4 | -8.19 | -54.75 | 2026-09-20 16:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4812ddc4-c9db-3bee-afbb-478a8d567b4e | -6.54 | -44.87 | 2026-09-20 16:15:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc657cd4-1fc9-3d87-a8b5-d5e22e7f82eb | -6.9 | -43.74 | 2026-09-20 16:15:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 34a95e5b-957d-3318-b0ea-148d696aebaf | -12.52 | -50.04 | 2026-09-20 16:15:00 | MSG-03 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08ee6aba-ea9f-39a8-8cd4-0352c952bcb6 | -9.83 | -48.39 | 2026-09-20 16:15:00 | MSG-03 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 06514e32-6147-3217-9065-6b91f691a800 | -9.86 | -48.45 | 2026-09-20 16:15:00 | MSG-03 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0a71a12a-4b6f-327b-999d-9ad0e6e4b742 | -10.51 | -51.0 | 2026-09-20 16:15:00 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e7a200a9-2b02-34d5-baf7-8bf5c80def34 | -10.69 | -50.71 | 2026-09-20 16:15:00 | MSG-03 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f6ec1880-9050-324b-a7c7-0e0881802eb6 | -11.89 | -49.99 | 2026-09-20 16:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1fdbe2d3-7d4a-39a1-aa9f-9c2454c50804 | -11.5 | -45.35 | 2026-09-20 16:15:00 | MSG-03 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 51836c19-d6d3-3752-8909-779d05d22fe4 | -11.68 | -43.41 | 2026-09-20 16:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c52f2ed3-b97a-393d-b61a-29ed555b86ca | -10.38 | -50.24 | 2026-09-20 16:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4cd6b14a-fe8e-307d-a3f2-dca127652ffb | -10.2787 | -50.2605 | 2026-09-20 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| ef42d445-2e3a-3bab-bc1c-38e839f5b0e0 | -9.2676 | -48.2472 | 2026-09-20 16:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 4fd98281-84f2-3c3c-bc64-49c771357ef7 | -6.8032 | -59.1693 | 2026-09-20 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| d7117f87-24b6-3f1a-bc6d-85e3bfdb617e | -10.279 | -50.2391 | 2026-09-20 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| ad0c4ecc-e569-30f4-b74c-f75d1d0b8c5a | -6.7263 | -45.4846 | 2026-09-20 16:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 47f2ec86-0ddd-390d-9fe9-1e2e320ca573 | 2.2187 | -50.8977 | 2026-09-20 16:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 82.4 |
| d1e9dc16-8253-340c-9c25-be2f0bfb39ad | -2.9143 | -58.3401 | 2026-09-20 16:20:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 177.0 |
| c42c3e27-aae4-34cc-a1fb-3747b5a5f3dd | -6.7463 | -59.4416 | 2026-09-20 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| c731fbb3-50a1-3c03-bee7-d26831f460f1 | -6.1113 | -57.6255 | 2026-09-20 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 28fc3f6f-4121-3750-b508-babb9c1c8f5f | -10.2793 | -50.2177 | 2026-09-20 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| acd0d97f-072a-31d3-ad8d-903d5c57d75d | -1.1345 | -49.2123 | 2026-09-20 16:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 2e4cde92-a71f-3ddc-8fcc-6dd9b77811f8 | -8.1688 | -54.7432 | 2026-09-20 16:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 131.9 |
| 85997e2c-5a57-3a8b-aba2-611b685d5d8f | -3.1079 | -61.408 | 2026-09-20 16:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 4465f900-f046-3b4d-861a-6b9bca3dc724 | -2.8962 | -58.2825 | 2026-09-20 16:20:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| be0d8d7b-eeff-389b-bd0b-cde13964a89a | -3.6398 | -60.5656 | 2026-09-20 16:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| c9ec4ee4-e8ad-312f-9b08-ca0bdc54a2a1 | -6.5444 | -44.9327 | 2026-09-20 16:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 8bf0f0e1-63bf-3582-843c-a5f6021f0b65 | -9.8136 | -48.3218 | 2026-09-20 16:20:00 | GOES-19 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 0d97e02c-5e1f-36ab-9ea6-3f1ecceead29 | -10.1145 | -48.4205 | 2026-09-20 16:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 80dc359b-a6cb-3b5a-b98b-9038aff878b0 | -10.567 | -51.3137 | 2026-09-20 16:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| c9ed7b4a-fb70-3552-ba90-646176bd5884 | -2.9157 | -57.7983 | 2026-09-20 16:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| c3676272-a15e-3749-ac35-833bf5c8f4a7 | -3.6632 | -58.8643 | 2026-09-20 16:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| b8d1e0ed-26ef-3344-9239-0677723cabb1 | -6.0928 | -57.6262 | 2026-09-20 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 1f9a9618-97c6-33e8-b361-c020a4dc8137 | -6.7863 | -58.8995 | 2026-09-20 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 48a85463-87b7-3457-b8f5-7e53a73bb6b9 | -10.567 | -51.3137 | 2026-09-20 16:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 1d41563f-6d8e-3801-96ab-7ec65c78bd08 | -10.8282 | -50.1601 | 2026-09-20 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 197.7 |
| 58d84e8a-9f27-3611-b8c2-f1ee192e6256 | -2.9143 | -58.3401 | 2026-09-20 16:30:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 156.1 |
| d3a99c76-48c6-3b3c-819a-c37e527ee692 | -3.1079 | -61.408 | 2026-09-20 16:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 4176ed65-83e9-3039-947a-bfb6a4abbfdc | -6.0928 | -57.6262 | 2026-09-20 16:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 720a7f64-9690-326e-8de1-360991abbe2b | -10.8093 | -50.1621 | 2026-09-20 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 8e748155-a0ab-34fe-9502-abe9cc0f8793 | -10.1145 | -48.4205 | 2026-09-20 16:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 7a96c98f-e414-3360-9d23-7afef860b621 | -8.1688 | -54.7432 | 2026-09-20 16:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 151.3 |
| 0cdd79e5-b0f6-3c17-afdc-a46128e2c22e | -6.1112 | -57.645 | 2026-09-20 16:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 297906bb-63d7-3abd-8a7e-63bbe4d30ae3 | -10.8279 | -50.1815 | 2026-09-20 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 0aa7c76e-7c79-336e-a79a-63e214083d8e | -10.809 | -50.1836 | 2026-09-20 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 51a460e2-f113-3c25-a4e1-1ad12e13ea6e | -3.6398 | -60.5656 | 2026-09-20 16:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |


[Clique aqui para ver as próximas entradas](README143.md)
