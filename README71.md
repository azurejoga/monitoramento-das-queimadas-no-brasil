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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c2a11ab-2681-3794-9401-8d7a8be1f228 | -14.67939 | -48.26748 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9a1920fc-e362-31b7-9fc6-7f23363a5d79 | -10.20807 | -48.18638 | 2025-10-04 04:14:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97a89e32-8229-335f-a363-eb6ab0338d0c | -13.13277 | -47.91865 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92d267a4-4f7a-3475-bd29-d957c06af067 | -15.50097 | -45.91846 | 2025-10-04 04:14:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b320ffa-9e43-3349-b643-cba5d5607376 | -9.90952 | -43.80641 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 09d0b2f8-1e10-32a1-98f7-1433251b69e9 | -13.12688 | -47.82174 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 62118ad0-63bb-32d8-be01-8c747e4b3fe6 | -11.70437 | -47.51372 | 2025-10-04 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0a862dd-efcb-3ef9-b25b-822707622e12 | -8.12667 | -50.2479 | 2025-10-04 04:14:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 152b2261-00a4-3c1a-9a92-f82ac4dfbee6 | -14.67796 | -48.2757 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4f26b43-09e0-3b5b-bb34-1bcf30b8c9db | -13.23457 | -47.35938 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63c0f9ca-c9cc-3c41-8003-3f9d413590d9 | -13.35037 | -48.07379 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1c60c64c-7188-3510-a7e6-c1b63d9b5996 | -14.92296 | -48.33482 | 2025-10-04 04:14:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c539d6e-5a8f-3993-85ef-f67c7cd29e54 | -14.31025 | -45.86269 | 2025-10-04 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5549fc7e-b8ed-3885-b422-07aee988b714 | -11.8433 | -44.93405 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7de9d057-c5fa-3b2a-ab8f-f1a0dda8ea5e | -13.46456 | -47.26376 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f82b1bf-3e84-3c44-ba41-7e8c25397b95 | -13.13485 | -47.81874 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2cdfc20-9f84-3b1b-8960-ca28e858fa63 | -13.60195 | -48.18038 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 80aff7f0-a44a-3cd1-a3ce-7c27af942dfc | -11.95049 | -51.48838 | 2025-10-04 04:14:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b436bf60-9234-3b28-8c10-b82ec654772a | -10.82533 | -46.58438 | 2025-10-04 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cdc42dce-5a2c-32de-9346-65f5fbff2c50 | -9.66277 | -42.93123 | 2025-10-04 04:14:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 469dc286-cc12-3869-bd72-6c61a3405cf4 | -10.29574 | -50.38136 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc937346-355d-361e-bdcc-bbc8c8dd9076 | -11.49664 | -46.75481 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3f7bf8c-b45a-33e2-aa5f-7b0cd0fa410d | -15.33322 | -46.30247 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29f17104-ddab-30bd-a868-93a0b6501e0e | -11.79564 | -45.02087 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50926c19-c8ec-3847-a9b9-7674cd076e5c | -9.32892 | -45.76625 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 08955602-4e91-33c3-98c0-67e9140707a9 | -13.6629 | -47.8692 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fce0db5-4985-35ff-8ee7-f2538d64a991 | -7.93327 | -55.02328 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0220a1f9-537b-30eb-9ed4-caaf98891041 | -9.93997 | -50.89288 | 2025-10-04 04:14:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14a48168-bd1b-3434-9bc5-f6cce6c6a6d6 | -12.30713 | -45.3655 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3a0095a8-2288-33ab-9e0c-b0c57ff46335 | -9.95702 | -43.69894 | 2025-10-04 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b2ec018c-0a20-39e7-8a6a-fc347dd3e964 | -13.52242 | -47.24409 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d207a5b-6c2c-360e-8644-f9019600ceb3 | -11.48226 | -44.97992 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6cfab3d7-7671-3448-a78a-58a77e434e0d | -9.95534 | -43.66649 | 2025-10-04 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ca4eea3-be43-3f2f-8ec4-af54d331fcf2 | -13.26272 | -47.21258 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| da5a31c8-a1fc-3081-b04d-620b7dc1dd18 | -13.99642 | -48.20197 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 83cec301-7375-3c27-b456-720715703a64 | -11.85275 | -45.04518 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5dfa742c-977b-3af2-a6c1-fc2990b75998 | -11.87358 | -44.97915 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98adf6e9-ed5b-3c42-9757-f71274364d6a | -10.81123 | -46.73414 | 2025-10-04 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac97a8ec-7283-3e7d-a85e-0b02e002dce9 | -14.20169 | -46.07236 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b130f7da-8fab-382b-8b9b-8ed4d3815a30 | -13.31525 | -47.61378 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44819c3f-40fe-330a-a5dd-e77898e8b04b | -12.89997 | -54.75064 | 2025-10-04 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14186205-ad3b-3646-95cd-037313e6f2ad | -14.38728 | -45.97262 | 2025-10-04 04:14:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d35dbfc5-c9b6-38dd-976d-473fa3242e92 | -14.69409 | -48.09616 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a7d051f-25ec-3e86-acba-e79b30aeb0c1 | -8.84834 | -46.78756 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5413210-c9dc-3c2a-b566-a49bf10efd73 | -8.52217 | -50.03109 | 2025-10-04 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dbe0b3e7-7618-3a15-bd84-b29e9fb89a1f | -12.03352 | -45.20972 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3cb4cddf-e7b8-3bba-ba28-780192afdfe1 | -10.06971 | -48.18704 | 2025-10-04 04:14:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fbef9d9-f12d-3d4a-9ac3-6e134748a403 | -7.56295 | -47.1879 | 2025-10-04 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0322de72-7735-34d9-8921-83d0c6238f6a | -14.91905 | -46.89667 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78d5185d-6007-31f2-867e-f411116f4106 | -13.75156 | -48.0532 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 074d4717-b422-3d14-980a-8b08ed051ae1 | -9.94516 | -50.24319 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b078baed-b295-3a23-8164-f3e00fb296e7 | -11.82419 | -48.07289 | 2025-10-04 04:14:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 673db416-bf78-336c-9fcd-786a0fa1b38d | -8.62846 | -54.98613 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44593ef6-b9f0-36d6-a635-1aa37c506500 | -11.11364 | -47.89416 | 2025-10-04 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cd53fffe-a0dc-3c2a-8330-2805a4ec1316 | -14.45683 | -46.33893 | 2025-10-04 04:14:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3583837-45eb-3f2c-83af-672f20a502b1 | -9.9018 | -43.81233 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 377b1a57-7365-3d9c-856b-2d7c3d1b86c7 | -9.95978 | -43.70296 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0df4bc58-3027-312b-bf0c-4c1a129fb7c3 | -13.51126 | -47.24599 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 411dc91e-7a9a-3211-b401-bd4bb4003fba | -11.12604 | -55.46323 | 2025-10-04 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4db9f7ab-1e2e-323c-b259-f441904c2e10 | -11.90619 | -46.3724 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7cf516eb-b976-3ba5-b3ad-60cbc1ff0ddf | -8.76401 | -49.91351 | 2025-10-04 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fd3ae89-2175-33f6-a130-b2e254b7de65 | -11.5534 | -47.67553 | 2025-10-04 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 932b3e3f-20fd-3f4b-9e45-226598774887 | -11.79897 | -45.02142 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16a556a1-3d9d-30c8-b55d-426b34c8456d | -9.63834 | -54.31633 | 2025-10-04 04:14:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd2b28d7-bb1f-3dc1-bcf9-5551621bbc23 | -12.31206 | -45.3774 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 013942d4-6907-31a8-b26d-04621353813c | -8.9118 | -46.60496 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c25d93ab-c913-3483-a16c-687b66d53006 | -11.48069 | -44.97261 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2598f014-16aa-3d5a-bf7f-fb3b4f358211 | -9.76639 | -46.21554 | 2025-10-04 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67451417-241a-3431-b3bc-eb833644e0d7 | -13.11095 | -47.84941 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 83e53ce2-12cc-3a20-a38f-9e566ea1816c | -13.66225 | -47.29642 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8725b3e-ab4c-3b49-907b-0d4f984c28e9 | -14.93579 | -46.85931 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9a8531ae-cade-3d3e-89a4-faaf4f829ab7 | -14.9216 | -46.88134 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ccc6deca-723f-342b-a25b-a9ec7d894a63 | -13.54764 | -47.24441 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b748db91-95d7-3c70-83e6-f40c8d578ac3 | -13.38676 | -47.55235 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b8f5f232-8591-34bc-914d-d6d29e2fe348 | -10.1305 | -45.34993 | 2025-10-04 04:14:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eeaec1e8-e86b-37c8-bf6a-037101c3e04d | -13.74639 | -48.08338 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 022a9a35-7bd8-30c1-af4b-0d0a46364a85 | -13.32536 | -48.11009 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ea036d8e-5b5d-3429-9a32-3069612e945e | -12.85679 | -42.62669 | 2025-10-04 04:14:00 | NOAA-20 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3af03f0c-3e4f-3d59-926d-1707922c194c | -10.63976 | -49.13786 | 2025-10-04 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07275cd8-f0a6-3a13-a1b7-d8e16db5bcd5 | -14.21726 | -46.0827 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc643963-6486-33b5-8102-99c9b574a0c2 | -13.24138 | -48.48834 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee1b3af3-f392-3ded-8a56-bb31e94631ee | -13.27141 | -48.15995 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 75082db8-81c8-30d2-83b7-bdbc286b6b2c | -14.36153 | -43.8416 | 2025-10-04 04:14:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 56af0f59-0ba6-3b11-93ee-b815f4d74d9a | -8.97488 | -46.72545 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f79dd076-751d-3e72-adf3-ca8467f878a3 | -12.70625 | -48.57179 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6e48b10d-1023-39c6-9848-6c8bd3e87011 | -14.98344 | -46.8479 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d10a19a-37cd-3b07-a09c-e7231d311018 | -12.19981 | -47.77917 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e10ad7d2-15c5-35f3-84cf-0844c5fe770f | -13.98142 | -45.07641 | 2025-10-04 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 29d30ea7-e0cc-3d67-bacf-2a367e858a72 | -13.22058 | -47.84434 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 6823cc58-32b7-37b4-a2aa-f8cc653cc18a | -12.03524 | -45.19902 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6a2e0e3d-bf2a-3c3b-8152-4ccf94f02d33 | -13.63491 | -48.68479 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8cef0a86-05b2-3af8-a91c-e37a9d045787 | -8.22236 | -46.80996 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0258f431-a2b8-3519-a969-e6a247b425a2 | -12.04145 | -45.18173 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebd02737-a7c9-37ba-ae4c-d4e51268bbe7 | -14.91945 | -46.87312 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aff29bd5-bafe-3ff1-bc45-a9eb4eb58562 | -13.31807 | -47.57498 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 17802785-da1f-3f27-b681-1b5f9c6ae8f5 | -13.64109 | -48.67158 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d656f7f-a473-3cbd-b687-a6790d95bcd1 | -9.93787 | -50.23286 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d76a057-6999-3aeb-8920-451809f30e88 | -11.80182 | -45.02208 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b10f06e-42b8-3782-9156-4d5b063c99a8 | -10.27152 | -44.33044 | 2025-10-04 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c6e95a1-79fd-33b8-8924-4f6a965740aa | -13.34821 | -47.24342 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README72.md)
