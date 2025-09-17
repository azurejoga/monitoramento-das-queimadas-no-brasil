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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a7dadd8-439e-3825-9d78-f95e815ecdb3 | -12.3968 | -51.41551 | 2025-09-17 04:34:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 8e5224d0-31af-3da7-89c5-02aed018339a | -12.97369 | -47.94483 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06190cb3-0311-39c3-97e9-224972730fef | -12.38707 | -51.40991 | 2025-09-17 04:34:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6d82a97-fe80-3892-bba3-d552e73e3425 | -14.90451 | -51.69787 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abd23725-9132-3b74-a13b-4ce0787380d2 | -14.83975 | -51.68714 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0f181652-eb43-3445-873a-694238090b8b | -12.28971 | -50.12843 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53e915ec-3cb9-365a-b958-53e864bdf0f4 | -12.69716 | -45.8061 | 2025-09-17 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3d9bea3b-36da-3c59-8ded-7e79df90497e | -17.32444 | -46.82175 | 2025-09-17 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82ea8bf5-81d5-35e9-80b8-b7a5f6903053 | -15.98004 | -46.44596 | 2025-09-17 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2464f089-7a53-358b-908e-128dc920a0ee | -13.03033 | -47.95806 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebd83449-bb08-3d25-9b00-aa56b019ae11 | -12.06605 | -46.53756 | 2025-09-17 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c4319e5-4810-3e4a-ad24-e1f044c30bc6 | -13.21498 | -47.31466 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57b2db73-211f-30fd-b435-88abf1235b36 | -15.9861 | -46.45609 | 2025-09-17 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9aa4f841-7738-3ab3-8f1f-048541f3f928 | -13.21662 | -47.28002 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28306882-fc5b-3102-9bef-c73ca885a868 | -16.84755 | -44.07405 | 2025-09-17 04:34:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ac75a05-4c4d-3efd-bc83-a44e5fefa8c8 | -17.32824 | -46.79487 | 2025-09-17 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 598ce046-3aab-3a04-b12e-83540c766da8 | -15.39347 | -46.14404 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5ba2bb1-53b9-3e84-aef0-e33767e5a42d | -14.60239 | -46.32837 | 2025-09-17 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3880641-edb2-31f9-ae6e-e77415867174 | -11.59502 | -49.81667 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bd6654e8-e6e1-304c-b312-00fa5b0a9815 | -15.42164 | -46.11929 | 2025-09-17 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffdf122b-b8eb-395d-8f3f-3e4c172eadf2 | -16.69271 | -54.96212 | 2025-09-17 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c3124e5-d20c-3471-80d1-d7d8504dacfb | -13.22522 | -47.29322 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9c32169-9e65-3244-8fb4-579e6f36aa35 | -12.71477 | -47.98241 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05a95802-e254-3721-bfe3-0bc69b7bfd56 | -14.81697 | -48.10793 | 2025-09-17 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| d3fc879b-c78c-38ee-9926-e34c92781fa7 | -14.90792 | -51.69847 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ef9ad4b-930c-3ebf-be46-60974513d185 | -15.39565 | -46.14259 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 527933d3-2b72-3818-b64b-d8380274f0d1 | -17.96603 | -46.00174 | 2025-09-17 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eb8f1453-cc23-3b44-9ac0-92fcc0796bde | -12.7243 | -48.00998 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 55ed051f-07ab-3682-b606-4e4eb250c80d | -14.81205 | -51.7058 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8fc7f733-11d5-3d54-a10b-5600dddbdce8 | -13.03035 | -47.98051 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fed97c59-f965-3180-b470-0dde4f7608a4 | -14.78389 | -60.22931 | 2025-09-17 04:34:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6561d87-628a-3ab7-b684-8672b7e2d2e1 | -12.10211 | -44.81887 | 2025-09-17 04:34:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 47c4885c-d463-307a-85fa-213d777387d0 | -14.85416 | -45.12639 | 2025-09-17 04:34:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef6dd41f-5b49-311b-b9c2-929735e30e88 | -11.77317 | -44.74376 | 2025-09-17 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ceb910cb-aed2-3327-a134-75f57e2e0c52 | -15.40182 | -46.15284 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d33073b3-2629-369e-8958-9926fa940a54 | -14.20689 | -47.00693 | 2025-09-17 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb7a26df-f3d1-39ce-ab0c-e555e5a6c542 | -12.35447 | -47.05743 | 2025-09-17 04:34:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef3a3f60-4cc3-376b-96ef-246439506997 | -14.60112 | -46.3905 | 2025-09-17 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe917d05-071e-3aa2-b730-2f0bf97433bc | -12.28378 | -43.83075 | 2025-09-17 04:34:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11315e6e-16e2-317a-94d5-dac224830905 | -14.82914 | -51.70881 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a89e9ce7-8064-3eb3-ab2b-efd774f07b9b | -14.82093 | -48.10471 | 2025-09-17 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8dfd8c59-5573-3cf9-b844-fb768f5619f4 | -13.327 | -43.0994 | 2025-09-17 04:34:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8c8abeaf-d593-3d28-abc8-53ebfec49d8b | -13.25606 | -54.24695 | 2025-09-17 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2238fcd8-f66a-33d1-963b-da25c0031cd8 | -18.18869 | -44.53686 | 2025-09-17 04:34:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3b8928bb-5926-3b2f-a754-3a26b6ec2f59 | -12.11411 | -44.83282 | 2025-09-17 04:34:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da9541e9-d008-312f-9634-d4ecc4a0b526 | -12.96529 | -47.95476 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61b99a5f-ab88-34bf-9515-a62cc1699c9d | -14.78685 | -51.70921 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5c00778-d688-3303-ab1f-3d2282b9e83a | -17.33492 | -46.80064 | 2025-09-17 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 249b2a53-56dc-32b6-9417-3d1db758a0bd | -14.63129 | -46.38708 | 2025-09-17 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b20c283-9c87-300b-a132-846f656e1469 | -14.77923 | -60.22321 | 2025-09-17 04:34:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5c37636-b506-3d97-b2bb-82692b57e641 | -12.71421 | -47.98604 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e730015a-66b2-3f20-b517-92d07a6176b3 | -16.42521 | -45.66949 | 2025-09-17 04:34:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| edf8640e-f18b-36a5-8d2c-7277a523ef94 | -17.56332 | -43.79263 | 2025-09-17 04:34:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be2b94cb-6a39-3873-8e67-e8dd50e976ea | -15.39377 | -46.12869 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78af5e4c-1cb9-387c-be20-239caf43ae7c | -15.43085 | -46.1621 | 2025-09-17 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f8a07d2e-4eac-317b-b229-463a54b339e5 | -16.28014 | -45.68111 | 2025-09-17 04:34:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a17056e5-bb6f-30fd-8af2-58849b4187cd | -14.90982 | -51.68706 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fcb2a99f-de9f-32c5-909d-df9680a919c7 | -13.17714 | -47.3086 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9ede0c3-fec2-3591-8c38-3f024c0d8707 | -15.42094 | -46.15162 | 2025-09-17 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bdecc16b-992c-36c8-8818-3b6d7a175ec9 | -16.70429 | -54.94305 | 2025-09-17 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ee02c8e3-0021-3e4f-aeb5-738ec96e1c89 | -14.90362 | -51.68205 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb3b049f-73b4-3f1d-9000-b76a9bd9466e | -12.70724 | -47.73724 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c27e9c56-801d-3213-8db4-640d1102c47c | -13.0337 | -47.95856 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e9aec6e-4702-3dfc-a127-974a3d714d04 | -12.72318 | -47.99491 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cbf17592-33cd-33d6-89cb-5635804fd693 | -14.69972 | -50.39359 | 2025-09-17 04:34:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08247b99-36bc-3ed4-87cb-462645b00b6e | -12.09309 | -44.82708 | 2025-09-17 04:34:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8b391165-70f8-3af5-918c-3e8ee4cf843c | -18.17461 | -45.18118 | 2025-09-17 04:34:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73fdaa3c-60ee-3655-9828-2520d76167eb | -17.04699 | -45.89605 | 2025-09-17 04:34:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1d243bac-1786-3301-9bae-8ed28e29c833 | -15.40244 | -46.14831 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3617c391-8a03-3810-95ed-fdec4a2460e4 | -18.36936 | -43.3228 | 2025-09-17 04:34:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 6af3aaa0-277c-393b-b6e7-90635c60f537 | -14.57061 | -47.41052 | 2025-09-17 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| afbdfa94-bffa-3da0-90d2-5fac0898de00 | -12.43487 | -49.72863 | 2025-09-17 04:34:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdbc3192-fe36-3f07-85b7-5a95f684231d | -12.71111 | -44.67395 | 2025-09-17 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 177d5f64-b9c2-3d6c-90f7-41f03989cc45 | -17.04765 | -45.89109 | 2025-09-17 04:34:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4d205c58-709b-3367-8ee8-fcb0754080b1 | -14.80796 | -48.12175 | 2025-09-17 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c907441-324c-3b8c-a762-e54157dffb9c | -14.83382 | -51.70179 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0f73a683-1f61-305d-8924-045e9e926ef7 | -18.19242 | -44.53643 | 2025-09-17 04:34:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e7b545b-a8a3-3c14-abf8-3a1029515896 | -16.42232 | -45.67091 | 2025-09-17 04:34:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4928037e-5aba-369f-bf3f-9a35ced73fbd | -15.42838 | -46.15264 | 2025-09-17 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 00287ec6-8149-3096-b4bc-4f00417c2e89 | -11.07463 | -49.75671 | 2025-09-17 04:34:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6094ed4b-8fae-3458-a037-4ad9ee0f5052 | -12.84875 | -47.19419 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5cdfbf7-263d-3ffc-ba66-6e93f9609084 | -14.80052 | -51.71162 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 498df678-45da-3408-96db-d23b40c98087 | -14.60204 | -46.33013 | 2025-09-17 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 143080ce-989c-336b-949d-e68772be546b | -15.55409 | -47.17211 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 564760d6-e3a8-3d81-8046-07b5c33649a2 | -17.32079 | -46.82114 | 2025-09-17 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c0a407f-7a93-304b-b067-eab33956989c | -11.60168 | -49.81776 | 2025-09-17 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc0c1261-fe65-31c3-971c-f071ea42da9c | -12.8453 | -47.1937 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 781b825a-060f-3420-a771-96b49b4e951f | -14.83633 | -51.68654 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e77a92be-7633-3ffc-9544-6f2f775e8d84 | -12.11353 | -44.8086 | 2025-09-17 04:34:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c871bd38-674a-3682-857b-1e2e2f12a8b2 | -14.7801 | -60.21895 | 2025-09-17 04:34:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fe5e4f3-c480-3bc1-8c4a-f3bee55ec495 | -12.5988 | -47.98658 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92690173-8eb1-3021-a09e-b14e3d80b1c9 | -15.72376 | -39.32158 | 2025-09-17 04:34:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 974c6b73-cd8e-3b09-b131-fe287f0dafd8 | -17.23764 | -43.43689 | 2025-09-17 04:34:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97ab44a3-6c3f-3b8d-8e5c-41feeec4a9e4 | -14.97057 | -53.40615 | 2025-09-17 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a69680f3-3430-31d6-8d51-78872202f015 | -18.53954 | -48.13021 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 553b8767-ed5a-3959-9d93-66f808d5176f | -12.06135 | -46.54496 | 2025-09-17 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 703ffa5f-d355-3d7a-8fae-9d5e8798776c | -13.32232 | -48.74939 | 2025-09-17 04:34:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5fdbd6c-ecee-38d2-a5fb-9223f8ccbb5c | -12.86624 | -47.14186 | 2025-09-17 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c498cde-ddb6-3a67-9bd5-0b2886995934 | -14.97134 | -53.40171 | 2025-09-17 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a7918bc-c691-35cb-8db5-eda00d47eb64 | -15.42158 | -46.14701 | 2025-09-17 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |


[Clique aqui para ver as próximas entradas](README48.md)
