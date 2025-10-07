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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e3e5b18-760b-3799-845d-80ec9c72c689 | -11.03564 | -50.91922 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 14553a69-99a7-3311-bc2c-e58280f9968f | -10.87497 | -51.03134 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 52558706-33ee-3ee5-9956-f95307bc8f5d | -7.04451 | -43.93354 | 2025-10-07 04:08:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d84d3b0b-d5dd-373d-98b1-6fd058e2a79c | -6.13601 | -42.67263 | 2025-10-07 04:08:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a4d7aaae-5dff-3854-86b0-98478bbeba77 | -10.41662 | -48.09426 | 2025-10-07 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f75e1525-7b46-30c7-aa26-a4e48c3c5d8d | -11.9486 | -46.45953 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| da42d11c-bb51-3998-9c04-70b809d717fd | -12.67561 | -42.70743 | 2025-10-07 04:08:00 | NOAA-21 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bc6545df-0a48-333c-9a7e-9de67eb4b9cb | -5.17305 | -50.64653 | 2025-10-07 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc785ba0-4bd5-3ba1-8616-94e5654e86f0 | -10.18611 | -45.53637 | 2025-10-07 04:08:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3ab3e5b3-5f72-3b07-9eb1-9c4a3b010f97 | -5.25579 | -46.48849 | 2025-10-07 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ec42f06-31b0-374b-aff8-d5805bf82e75 | -9.1252 | -44.3886 | 2025-10-07 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 688f6e4b-37c5-39f4-87aa-c38b06e25e10 | -10.7413 | -50.48792 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| bd36089d-dad5-33b5-8f9b-5c89a645a257 | -8.58508 | -44.33717 | 2025-10-07 04:08:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3544cc8c-0c4c-3ade-b7eb-b0c799202030 | -11.26786 | -48.8479 | 2025-10-07 04:08:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8bdcd8de-32eb-35ac-9f3d-b6cec64b14ff | -9.6845 | -48.39365 | 2025-10-07 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5e312f49-bb1d-3b4c-8c02-d26e31d6fc18 | -8.1719 | -50.16043 | 2025-10-07 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 09b263b4-5271-37f2-a487-2e6d7c606f5d | -5.15329 | -49.85045 | 2025-10-07 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f077c6c4-f2f1-3156-8e1e-c101efc46699 | -5.74912 | -40.45114 | 2025-10-07 04:08:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| feee88f6-1376-3f12-96c0-5db60c2839f9 | -10.87943 | -51.03524 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 14b6ff88-21a3-36e5-b248-a066d7bc8f60 | -7.17143 | -40.40389 | 2025-10-07 04:08:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a1047b94-3dc3-327d-9b8b-5e93d132fefd | -10.9977 | -49.58223 | 2025-10-07 04:08:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2017ebab-ee6b-3673-88fb-6601468e2397 | -8.56894 | -46.23933 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 90aa63a0-77b9-3869-9ec8-3121d46a17ad | -5.09386 | -44.87437 | 2025-10-07 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9292b3c-023e-3297-9440-23c0bb05ff94 | -4.68703 | -45.8458 | 2025-10-07 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 58.2 |
| c347f01e-6b38-375c-bf01-69c79d4ab338 | -11.72246 | -44.43823 | 2025-10-07 04:08:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff7e60f2-42a6-38a1-8e9b-39e1971caa56 | -10.44579 | -50.34836 | 2025-10-07 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d6b0a69a-ab75-30c8-8bd0-189f62077d1e | -6.39765 | -42.16112 | 2025-10-07 04:08:00 | NOAA-21 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 2e35a81e-6d5c-30c4-a003-d668521062bc | -10.8095 | -48.60232 | 2025-10-07 04:08:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfe885e5-4c9b-3a1b-91f0-370304e31dd7 | -5.5009 | -43.06497 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| fbe63d4b-d1b6-366b-a5b8-d755df09805a | -8.96633 | -50.80233 | 2025-10-07 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8a9837f-48ef-3aab-ba28-6cc5e9abbda8 | -10.91792 | -47.06276 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f4dceef7-e4d4-3bf8-91f9-2b20bd2ad4fd | -7.78647 | -42.61219 | 2025-10-07 04:08:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8796977e-7b77-36bb-a621-2bfaa0f75b9b | -7.70953 | -42.38875 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 26863582-98a4-32a4-92de-2defb98c97fa | -7.6989 | -48.06182 | 2025-10-07 04:08:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ada942a3-6e6d-3019-a7cf-f634a821558a | -11.72584 | -44.43879 | 2025-10-07 04:08:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53787509-6417-37f9-809b-066d163ac2d6 | -11.80842 | -45.04785 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1488a6a9-b391-38e9-b737-24c65ee9592a | -5.25436 | -46.57389 | 2025-10-07 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a5a0f591-f6ce-39ca-9022-3a6766afff85 | -9.20039 | -47.8476 | 2025-10-07 04:08:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f69bfd4-2302-302c-b42b-0c86e2e07bbe | -5.77537 | -45.74056 | 2025-10-07 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c98b76a-92e3-3faa-8da2-156bdc64c5c0 | -8.62194 | -44.93213 | 2025-10-07 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0375cdea-6e09-320d-9ee9-3f076c4b757d | -8.88441 | -47.66378 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 89558203-7a6a-356e-ac3e-7c1495188119 | -8.74618 | -48.87244 | 2025-10-07 04:08:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b2b6ca0-0963-371e-8bd3-bba02db36650 | -10.90551 | -47.10369 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8693745-ccd4-3b94-957f-c45e7f68b80c | -10.25718 | -44.36642 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 34843f98-62e1-30cd-bf31-731fe60e0fe3 | -8.53098 | -46.25934 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb33241b-d423-3599-b90e-d2c3a19c3b30 | -7.00984 | -42.29104 | 2025-10-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 656d6858-714e-3034-90f9-4f15c48f711d | -11.94356 | -46.44475 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 98587adf-168d-32fa-a0b8-0daf6ecdaf51 | -6.2393 | -43.25986 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7bf78d5-2625-30b1-a5d3-794641512915 | -6.24093 | -43.27134 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4358b934-2112-30aa-8ec1-14af37dc2170 | -7.67757 | -42.59078 | 2025-10-07 04:08:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| db0d8d9c-9f0e-3f8c-9af7-16dae91ad40f | -5.23938 | -46.56428 | 2025-10-07 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1fc2715a-71d1-367e-9610-6f29091daf98 | -10.03337 | -48.2888 | 2025-10-07 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ccd5ad3a-9ba3-37f3-b918-377fc0662fe8 | -7.02557 | -42.79587 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 42bd336d-35b3-317b-a63a-0621ad8d9655 | -9.33252 | -54.51736 | 2025-10-07 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a12e650-6318-33e5-b295-5c446aa1d6a6 | -8.55004 | -46.26249 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b398d783-913d-3755-9e6f-c421f9bd42bd | -7.29015 | -41.98473 | 2025-10-07 04:08:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ebb8ace7-09fd-3251-bc52-b1fa5562f324 | -8.48588 | -46.27125 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e877b2d1-69ea-399c-8a63-dc6307fdc920 | -5.80312 | -45.21785 | 2025-10-07 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0909fe02-9dde-317f-b57b-ca474f7cb6e3 | -5.34114 | -43.38074 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d373995-d559-3add-9816-321bd5eefae4 | -8.61906 | -44.92751 | 2025-10-07 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f377718a-b8e9-3554-bc13-d6ef3eae48a3 | -10.62259 | -48.7047 | 2025-10-07 04:08:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 549e5f9e-a44d-3f26-bf5f-6fc8ac6412d8 | -5.25147 | -46.5661 | 2025-10-07 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c7fc032b-17bc-3a0c-b8bb-b3d8d98ea8a7 | -8.59261 | -44.33448 | 2025-10-07 04:08:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b111b32e-daf1-3a4e-81ca-5a7f4c3cd6d1 | -5.25679 | -46.48492 | 2025-10-07 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 239cb645-b60b-3cb1-9dd1-650fc0a6510e | -5.11552 | -43.20824 | 2025-10-07 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f85c6afa-bbcd-3533-a22c-9c03ea705d32 | -5.49973 | -43.07227 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| bedb7185-a99d-3993-b144-09244bbc2694 | -8.54781 | -46.25223 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b522212d-28a9-379b-b478-6de2f0f5fb39 | -11.29492 | -48.27244 | 2025-10-07 04:08:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5180e816-912f-389f-842e-75837035c4cc | -6.59128 | -44.62584 | 2025-10-07 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fea360cd-d64d-3b26-a182-750c48155fb2 | -5.24209 | -46.57203 | 2025-10-07 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| faf4fd23-1732-3db3-ad0d-8770455dcfba | -6.36382 | -41.61468 | 2025-10-07 04:08:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9f98b61f-2757-38a3-b19b-0993ba488574 | -5.51553 | -44.40836 | 2025-10-07 04:08:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55069f34-96a6-3b1d-a1f5-206d7d5db412 | -11.86883 | -44.93942 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9bf36d8d-e30e-3dd3-9eb0-cf75182fe5fb | -11.16786 | -47.73331 | 2025-10-07 04:08:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c6ef8c8-d3c5-3b1e-8b03-f9e1e89e7509 | -11.93922 | -43.04426 | 2025-10-07 04:08:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f6a995a7-623b-3486-be56-9a40a730dda0 | -5.28321 | -47.52261 | 2025-10-07 04:08:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a24198ce-8ea6-3727-ba52-4e5d8e5bb6dd | -7.80348 | -44.13139 | 2025-10-07 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5ca56b6-e16c-3a39-afde-10617dcc0f55 | -10.06997 | -50.5172 | 2025-10-07 04:08:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4ff1ceba-825c-3c34-a272-b2b3dcf63dc2 | -10.43325 | -50.3349 | 2025-10-07 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 95278cfc-2cf5-3eb1-b926-7fc1d664b5e3 | -11.38819 | -43.49184 | 2025-10-07 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82c85127-5922-340b-87aa-42e0a14ec8ac | -8.52113 | -46.24794 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24ee6672-fa65-3425-920f-b18e7c035b7b | -8.68357 | -47.08016 | 2025-10-07 04:08:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 48c38975-0b81-326c-81ee-c97584cab3dc | -6.64952 | -41.98869 | 2025-10-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| df1bc1b6-9103-34ea-9250-d5f34712f7c2 | -10.23017 | -52.69796 | 2025-10-07 04:08:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1023b31-b4b6-3204-bee7-41a97a28c274 | -11.67173 | -46.34256 | 2025-10-07 04:08:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27d85ec4-a20b-3c78-b99e-67cabb5d7179 | -6.25065 | -43.25414 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8c1eeb5-fce1-30a1-8b16-b99657febc2e | -8.2224 | -49.14406 | 2025-10-07 04:08:00 | NOAA-21 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 66e95ab1-21ef-3e1a-b8a8-83ab7fa3fda8 | -5.14066 | -43.82709 | 2025-10-07 04:08:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32845505-a96a-371c-aca6-8e0c08c76421 | -6.52522 | -49.8438 | 2025-10-07 04:08:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdd02779-d1d7-346c-b33e-017f73d294e3 | -7.72001 | -42.40821 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ce076caa-4eec-38dd-94ca-4b5612245d8e | -5.49634 | -43.07173 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| dab7a1a7-1540-336c-9253-3c86b57cb0f4 | -12.11772 | -45.13913 | 2025-10-07 04:08:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62f8bdc8-869b-3a7f-9015-be91556150ab | -8.53019 | -46.2641 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8b6c2d8-1afe-3bf6-ab8f-35403379a7da | -8.52092 | -48.23376 | 2025-10-07 04:08:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29cc6988-ad9c-30bd-afa7-e5fac524503c | -9.68089 | -48.38899 | 2025-10-07 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60a03978-1564-3446-b752-179f19034898 | -10.885 | -51.03321 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 787f413d-00ce-3f2e-9f9c-04f24c632df4 | -6.72783 | -42.80321 | 2025-10-07 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 59b2d7bf-5516-3b96-984b-ee3cb99f9ba9 | -6.75659 | -42.23624 | 2025-10-07 04:08:00 | NOAA-21 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5e771e06-8cbf-3ee2-99a5-cf8117c5e0ce | -7.30167 | -41.97593 | 2025-10-07 04:08:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| abd7d901-f89d-31bf-ac25-18426406d5c4 | -6.45677 | -42.79639 | 2025-10-07 04:08:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |


[Clique aqui para ver as próximas entradas](README24.md)
