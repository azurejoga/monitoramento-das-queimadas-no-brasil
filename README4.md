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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67cb336a-85fc-3162-bd32-4e47859dbccc | -20.33755 | -47.10536 | 2025-10-05 00:30:00 | TERRA_M-M | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 31bdd6c3-6c58-341b-9193-47720a7421bb | -19.59925 | -44.87407 | 2025-10-05 00:30:00 | TERRA_M-M | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1b1f4a63-7742-3a5d-9b3a-91c32d07169a | -18.63526 | -46.50009 | 2025-10-05 00:30:00 | TERRA_M-M | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 90fdc0d7-10b8-36c3-8211-57dde50d5dbd | -16.74976 | -43.96695 | 2025-10-05 00:30:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8fd0f96d-730c-3780-b581-0e16d9924cc3 | -19.6544 | -44.99591 | 2025-10-05 00:30:00 | TERRA_M-M | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 63ce998a-090e-3fcf-9666-c50b8b895920 | -17.55574 | -46.76701 | 2025-10-05 00:30:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 814437ff-35a2-349e-b680-06b4a7daf003 | -18.38334 | -46.95113 | 2025-10-05 00:30:00 | TERRA_M-M | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ec5c19a8-cf2f-32f7-8ab5-ed6893058233 | -20.32911 | -47.73426 | 2025-10-05 00:30:00 | TERRA_M-M | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 97bf5ed9-9fa9-3467-bb45-5704bfdbef25 | -19.95164 | -44.63677 | 2025-10-05 00:30:00 | TERRA_M-M | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 5d4431c4-43ce-361c-af13-8ccda0b9d164 | -19.59074 | -44.62963 | 2025-10-05 00:30:00 | TERRA_M-M | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1ef57794-2183-37f5-9989-4be2cd6c70c3 | -19.65295 | -44.98603 | 2025-10-05 00:30:00 | TERRA_M-M | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.6 |
| db748cde-7980-3255-a6ee-8059c3677ec3 | -17.20173 | -44.44628 | 2025-10-05 00:30:00 | TERRA_M-M | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 35.0 |
| b025c4c6-cf3b-3d44-8993-da2f5cf3501e | -19.66199 | -44.98455 | 2025-10-05 00:30:00 | TERRA_M-M | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f84fa917-71e4-3914-8691-2bb6791567c7 | -17.3929 | -46.64778 | 2025-10-05 00:30:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a93b7918-e7a6-3f4c-b346-491d058a0c43 | -16.57671 | -46.35837 | 2025-10-05 00:30:00 | TERRA_M-M | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| eeb17934-6d21-3d95-9ddb-297c63269890 | -18.45519 | -49.44528 | 2025-10-05 00:30:00 | TERRA_M-M | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a033f580-f544-3c51-a676-4dbca0cbf8b2 | -15.7976 | -41.47262 | 2025-10-05 00:30:00 | TERRA_M-M | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| 1dc07afa-b176-3760-88ee-6ee0e67f31b1 | -19.50589 | -50.3789 | 2025-10-05 00:30:00 | TERRA_M-M | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 8bb46d72-d61a-37b3-bc9e-179c8d843dad | -19.63877 | -45.97846 | 2025-10-05 00:30:00 | TERRA_M-M | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e886c952-6a4e-3de2-b800-71e75d577dd2 | -18.61922 | -43.18951 | 2025-10-05 00:30:00 | TERRA_M-M | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| 1025473d-6ddf-3ea7-9a3e-ded2f6e816f7 | -18.00585 | -45.01579 | 2025-10-05 00:30:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 7de96577-ace1-3b27-a97b-226aae3ae634 | -19.06807 | -46.90068 | 2025-10-05 00:30:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 07aac1f9-40db-3da8-97f5-40ab9cce3690 | -14.93207 | -46.84626 | 2025-10-05 00:33:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 2d26901b-8cd1-3c70-a5dd-574d115b0130 | -10.03136 | -50.40993 | 2025-10-05 00:33:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5038d5ae-9a07-32ec-83b4-de115d380441 | -10.93681 | -47.08921 | 2025-10-05 00:33:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7f7e758d-0ab4-382e-8a10-6a3b6a329eb5 | -12.90595 | -47.32123 | 2025-10-05 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 220baf74-157e-3832-ae3c-6bb0f89eebf6 | -14.32211 | -47.69205 | 2025-10-05 00:33:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 4ef98f54-c3cf-3213-bcea-c7140c2c2509 | -8.79058 | -40.56115 | 2025-10-05 00:33:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 48.1 |
| 1397c06b-13b6-30ee-965d-eb48546f2650 | -12.44926 | -44.74701 | 2025-10-05 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 1ef86144-acf5-38ea-aade-8be341dd6cbd | -13.30812 | -47.62445 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a33fac9d-45f7-3e8b-a096-c3be0f6d073f | -10.57552 | -48.7165 | 2025-10-05 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2eb412c1-1cd1-33be-9335-7889f422e9ed | -13.0898 | -47.91423 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| ad3a8152-3977-34eb-81bf-e70997b0d4e8 | -11.77818 | -47.55384 | 2025-10-05 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| ed0cf100-668d-3ecd-b49e-60c8959290a1 | -11.81243 | -48.87176 | 2025-10-05 00:33:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ef30ad51-674a-34bb-b53b-f239f5022799 | -14.65973 | -48.33862 | 2025-10-05 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5d0ae491-e5d1-3021-8ab9-c8d3628b0206 | -10.66076 | -48.4705 | 2025-10-05 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 67448ce5-1716-3998-967f-c1db1c9bcbed | -14.80124 | -44.89384 | 2025-10-05 00:33:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 1141f0e7-5be4-34a6-995e-9917fbd72406 | -15.93289 | -48.99435 | 2025-10-05 00:33:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d10a06f6-4517-377b-93f6-43d4894d09f0 | -15.91131 | -48.82777 | 2025-10-05 00:33:00 | TERRA_M-M | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 225.5 |
| a9403278-9e05-3d89-a24c-6c979368a4a1 | -11.46634 | -51.51932 | 2025-10-05 00:33:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8b5b3f25-26b6-35f8-a67c-38146c66ea3f | -13.29866 | -48.0918 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 47c1190c-9d26-3bfc-bf52-23405f58996f | -13.20297 | -48.52679 | 2025-10-05 00:33:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c9cec2fc-0c18-3368-82ef-b537dcd6a7f8 | -13.09105 | -47.92322 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c2d67aca-a35a-34a7-a03a-e56d1394d606 | -13.15011 | -50.96789 | 2025-10-05 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 28.0 |
| c98ef946-f2da-3343-8012-53bfec5db132 | -10.6235 | -48.67318 | 2025-10-05 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ec479ba7-e9fb-3b06-a98d-eadbd797b1a4 | -15.16758 | -43.62655 | 2025-10-05 00:33:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 0734281b-9be3-327c-b059-035f445f2730 | -15.56188 | -48.20215 | 2025-10-05 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9c471afb-8a18-304e-bd73-b5e027d4dc68 | -11.82121 | -45.06686 | 2025-10-05 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| dcc71077-17ba-327c-bf6c-c3d8b6930aa6 | -8.54859 | -46.27844 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| c6619f2d-be3b-338d-bfc1-9b970cc414b6 | -10.73079 | -48.63632 | 2025-10-05 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 09a2ed28-3fd7-342e-9547-3cd9c3b488d9 | -13.303 | -47.78156 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| af7152f2-b421-3c4c-9851-5eea6b60de0f | -8.38721 | -45.82577 | 2025-10-05 00:33:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 38ce2fb6-deab-3882-965e-41906e67293e | -13.46037 | -47.26637 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 63b7ed47-5620-3c79-bcdc-8155797a6b09 | -11.86656 | -56.86581 | 2025-10-05 00:33:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 4072d6d1-b528-3d3f-8f3e-70c777c97535 | -14.16198 | -44.68001 | 2025-10-05 00:33:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 34d8d8c2-6436-33ef-aab2-2a0ab9b684a9 | -12.58088 | -54.77996 | 2025-10-05 00:33:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| e49b184d-7cfb-3924-b9e7-5c24c3444619 | -13.35921 | -48.05812 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7ccb822c-5ebf-3854-8108-12e6ee0a0a17 | -13.37235 | -47.55375 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| c6b9ea2f-d028-3caf-9ead-7b7d832acb81 | -16.36244 | -47.05809 | 2025-10-05 00:33:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 496a9b19-cd13-3ef2-8265-c79785dd473e | -10.73961 | -48.63506 | 2025-10-05 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 76b7e26c-f2ea-3063-99f8-dd1aea7079b6 | -11.10963 | -47.13649 | 2025-10-05 00:33:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| e7b8793c-ea4c-3d8d-a3c3-02866b825d85 | -10.82559 | -47.99154 | 2025-10-05 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d539a902-e41f-3d9e-83e1-13f8977bb25a | -11.04499 | -47.79129 | 2025-10-05 00:33:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 35c168c4-7f45-3138-bb3a-2857b10149de | -10.71452 | -44.17531 | 2025-10-05 00:33:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 71167919-e29a-3e9b-b7bc-2f0f44c95091 | -12.39307 | -51.10668 | 2025-10-05 00:33:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 19.2 |
| b585c08e-6db5-3ec6-87ab-14b8f48eedfc | -10.7387 | -47.90044 | 2025-10-05 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9542b624-9dd8-339e-90f5-332869a78b4f | -13.08856 | -47.90525 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 93cf666f-524d-3488-a75f-cede763a0b2c | -11.67725 | -43.90896 | 2025-10-05 00:33:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 56d6f621-5752-3a4a-a72e-b80ae049a922 | -13.58451 | -48.16024 | 2025-10-05 00:33:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 250b69b7-ac69-38bd-95f5-c639a86dba49 | -10.87629 | -50.82416 | 2025-10-05 00:33:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| dae6ade8-cc93-32e4-9116-4c2f83b0ec77 | -13.85063 | -43.99148 | 2025-10-05 00:33:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 70171cc3-be10-3b85-b63f-fa5ee70d654b | -13.91825 | -48.16988 | 2025-10-05 00:33:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3e41c5fe-c4d5-3754-8a03-df0206d82ca6 | -13.27665 | -47.59241 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 36763fac-6549-3e4e-bee4-2512cd2ab82e | -14.30303 | -52.92625 | 2025-10-05 00:33:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 2507c064-4f51-3dfa-a837-e27478e5b9de | -15.54547 | -46.81181 | 2025-10-05 00:33:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 507cec10-78f3-3ba2-9e24-da3c72f05f6a | -10.01477 | -48.27109 | 2025-10-05 00:33:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 96c4c63f-e044-365c-b9cc-9136055d52b0 | -10.01353 | -48.26218 | 2025-10-05 00:33:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7ee701ac-4121-3b3c-b6fb-96d67a1b2ac0 | -15.94205 | -48.99311 | 2025-10-05 00:33:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a297fc04-82b4-373d-92a0-adba9a02465d | -13.13584 | -50.93517 | 2025-10-05 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 0ae59378-936f-3c2f-b88f-cf6d179e7a19 | -14.08861 | -50.15444 | 2025-10-05 00:33:00 | TERRA_M-M | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0ec5cde4-eeaa-3fc7-b41b-6406e37d4387 | -11.89882 | -43.32294 | 2025-10-05 00:33:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6bf01fe4-745e-31ac-a355-e3e85ca88bf7 | -11.01741 | -46.68867 | 2025-10-05 00:33:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bbacc62a-404e-323d-9fad-e87bb594aca7 | -11.1164 | -49.85633 | 2025-10-05 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ab5b154a-cd35-37b4-b2b8-bee9ef5a95d8 | -10.83316 | -47.98128 | 2025-10-05 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1de8d607-4bea-31e9-a495-7e229b49664a | -8.42564 | -45.80198 | 2025-10-05 00:33:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7c96f526-ee3d-30f4-a612-3dbf777b892f | -12.94146 | -51.00808 | 2025-10-05 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 3f511305-12cc-31a2-ae15-a0e47f94201c | -13.30114 | -48.10984 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| e497894d-b8df-3c89-b97d-9328a040ff3f | -15.55067 | -46.84855 | 2025-10-05 00:33:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b3c16e8e-c92f-3a7a-a71e-82d8d31d4028 | -13.32061 | -47.77897 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 463686b4-b87a-339e-8f09-facdeea796dc | -12.46373 | -45.53157 | 2025-10-05 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 9b184991-d1f7-3bf7-83fc-2768d8205320 | -13.14715 | -50.94518 | 2025-10-05 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| e3899af2-2df2-370a-8b24-4a0c84d21567 | -13.00006 | -44.59076 | 2025-10-05 00:33:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| aff31dbc-efde-398b-b454-a32e5c049519 | -14.82787 | -52.92461 | 2025-10-05 00:33:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e1238afd-b659-3d01-b4c7-be6044077fe5 | -15.78119 | -49.09858 | 2025-10-05 00:33:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ec0763f8-ad7f-3b90-b9ca-7b73deb5d4b0 | -12.56153 | -48.15689 | 2025-10-05 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 72e27f03-9d51-36cf-9a4e-fe71d41de8b3 | -11.85358 | -44.94474 | 2025-10-05 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 0ff971c7-cbfc-388f-a99a-74ec4cca8340 | -11.71824 | -45.34598 | 2025-10-05 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 1332c265-af6d-3ad9-8324-3fa39be19d18 | -13.44267 | -47.26891 | 2025-10-05 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5d0c39f3-3bc4-3b7e-96dd-9bb244d423ac | -9.04408 | -47.01163 | 2025-10-05 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9e25d924-ce35-35a1-8214-8cf9589bc779 | -12.2699 | -49.19318 | 2025-10-05 00:33:00 | TERRA_M-M | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |


[Clique aqui para ver as próximas entradas](README5.md)
